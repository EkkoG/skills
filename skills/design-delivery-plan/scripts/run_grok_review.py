#!/usr/bin/env python3
"""Run one Grok review using the existing CLI configuration and private artifacts."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import signal
import subprocess
import tempfile
import time


def positive_seconds(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("must be a positive finite number")
    return number


def save_result(folder, result):
    temporary = folder / "result.tmp"
    temporary.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    temporary.replace(folder / "result.json")


def announce(folder, result):
    print(json.dumps({
        "status": result["status"],
        "failure": result.get("failure"),
        "elapsed_seconds": result["elapsed_seconds"],
        "stdout_bytes": (folder / "stdout.json").stat().st_size if (folder / "stdout.json").exists() else 0,
        "stderr_bytes": (folder / "stderr.log").stat().st_size if (folder / "stderr.log").exists() else 0,
        "result": str(folder / "result.json"),
    }), flush=True)


def stop_process(process):
    # Grok's children must not outlive an interrupted or explicitly timed-out run.
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        pass
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    process.wait()


def collect_result(folder, result):
    if result["exit_code"] != 0:
        diagnostic = (folder / "stderr.log").read_text(encoding="utf-8", errors="replace")
        diagnostic += (folder / "stdout.json").read_text(encoding="utf-8", errors="replace")
        permission_error = any(marker in diagnostic for marker in (
            "FS_PERMISSION_DENIED", "Operation not permitted", "Permission denied",
            "unable to open database file",
        ))
        result.update(status="failed", failure="permission_denied" if permission_error else "cli_failed")
        return
    try:
        response = json.loads((folder / "stdout.json").read_text(encoding="utf-8"))
    except (ValueError, UnicodeError):
        result.update(status="incomplete", failure="invalid_output")
        return
    if not isinstance(response, dict):
        result.update(status="incomplete", failure="invalid_output")
        return
    report = response.get("text")
    if not isinstance(report, str) or not report.strip():
        result.update(status="incomplete", failure="empty_response")
        return
    (folder / "report.md").write_text(report + "\n", encoding="utf-8")
    result["report"] = str(folder / "report.md")
    result["stop_reason"] = response.get("stopReason")
    # Select final text and metadata only; raw JSON can also contain private reasoning.
    for field in ("sessionId", "requestId", "usage", "num_turns", "modelUsage"):
        if field in response:
            result[field] = response[field]
    if response.get("stopReason") != "end_turn":
        result.update(status="incomplete", failure="incomplete_response")
    else:
        result["status"] = "completed"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cwd", type=Path, required=True)
    parser.add_argument("--prompt-file", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, default=Path(tempfile.gettempdir()))
    parser.add_argument("--heartbeat-seconds", type=positive_seconds, default=30)
    parser.add_argument("--timeout-seconds", type=positive_seconds,
                        help="optional whole-process deadline; separate from polling")
    parser.add_argument("--model", help="only for an explicit user override")
    parser.add_argument("--reasoning-effort", help="only for an explicit user override")
    args = parser.parse_args()
    cwd = args.cwd.resolve()
    if not cwd.is_dir() or not args.output_root.is_dir():
        parser.error("cwd and output-root must be existing directories")
    try:
        prompt = args.prompt_file.read_bytes()
        if not prompt.decode("utf-8").strip():
            parser.error("prompt-file must contain a nonempty UTF-8 review packet")
    except (OSError, UnicodeError):
        parser.error("prompt-file must be readable UTF-8")

    executable = shutil.which("grok")
    # Private artifacts are retained for diagnosis and same-input retries.
    folder = Path(tempfile.mkdtemp(prefix="grok-review-", dir=args.output_root)).resolve()
    previous_umask = os.umask(0o077)
    started = time.monotonic()
    result = {
        "status": "starting", "exit_code": None, "elapsed_seconds": 0,
        "started_at": datetime.now(timezone.utc).isoformat(), "cwd": str(cwd),
        "executable": executable, "prompt_sha256": hashlib.sha256(prompt).hexdigest(),
        "prompt_file": str(folder / "prompt.txt"),
        "stdout": str(folder / "stdout.json"), "stderr": str(folder / "stderr.log"),
    }
    process = None
    previous_handler = signal.getsignal(signal.SIGTERM)

    def interrupt(signum, frame):
        raise KeyboardInterrupt

    signal.signal(signal.SIGTERM, interrupt)
    try:
        (folder / "prompt.txt").write_bytes(prompt)
        with (folder / "stdout.json").open("wb") as stdout, (folder / "stderr.log").open("wb") as stderr:
            save_result(folder, result)
            announce(folder, result)
            if executable is None:
                result.update(status="failed", failure="cli_not_found")
            else:
                command = [executable, "--prompt-file", str(folder / "prompt.txt"),
                           "--tools", "read_file,grep,list_dir", "--disallowed-tools", "Agent",
                           "--deny", "MCPTool", "--no-subagents", "--disable-web-search",
                           "--output-format", "json"]
                for option, value in (("--model", args.model), ("--reasoning-effort", args.reasoning_effort)):
                    if value:
                        command.extend((option, value))
                process = subprocess.Popen(command, cwd=cwd, stdin=subprocess.DEVNULL,
                                           stdout=stdout, stderr=stderr, start_new_session=True)
                result.update(status="running", pid=process.pid)
                save_result(folder, result)
                announce(folder, result)
                next_heartbeat = time.monotonic() + args.heartbeat_seconds
                while process.poll() is None:
                    elapsed = time.monotonic() - started
                    if args.timeout_seconds and elapsed >= args.timeout_seconds:
                        stop_process(process)
                        result.update(status="timed_out", failure="deadline_exceeded")
                        break
                    if time.monotonic() >= next_heartbeat:
                        result["elapsed_seconds"] = round(elapsed, 1)
                        save_result(folder, result)
                        announce(folder, result)
                        next_heartbeat = time.monotonic() + args.heartbeat_seconds
                    time.sleep(0.1)
                result["exit_code"] = process.returncode
        if result["status"] == "running":
            collect_result(folder, result)
    except KeyboardInterrupt:
        if process is not None:
            stop_process(process)
            result["exit_code"] = process.returncode
        result.update(status="interrupted", failure="interrupted")
    except OSError as error:
        if process is not None:
            stop_process(process)
            result["exit_code"] = process.returncode
        result.update(status="failed", failure="permission_denied" if isinstance(error, PermissionError) else "io_error")
    finally:
        result["elapsed_seconds"] = round(time.monotonic() - started, 1)
        save_result(folder, result)
        announce(folder, result)
        signal.signal(signal.SIGTERM, previous_handler)
        os.umask(previous_umask)
    return 0 if result["status"] == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
