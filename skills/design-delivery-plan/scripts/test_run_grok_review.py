"""Offline behavioral tests; the fake CLI makes no network requests."""

import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest


RUNNER = Path(__file__).with_name("run_grok_review.py")
FAKE_CLI = r'''
import json, os, pathlib, subprocess, sys, time
args = sys.argv[1:]
with open(os.environ["FAKE_CAPTURE"], "a") as output:
    output.write(json.dumps({"args": args, "cwd": os.getcwd(),
                            "grok_home": os.environ.get("GROK_HOME"),
                            "prompt": pathlib.Path(args[args.index("--prompt-file") + 1]).read_text()}) + "\n")
mode = os.environ.get("FAKE_MODE", "success")
print('WARN No auth credentials for cli-chat-proxy', file=sys.stderr, flush=True)
if mode == "permission":
    print('FS_PERMISSION_DENIED: Operation not permitted', file=sys.stderr)
    sys.exit(1)
if mode == "failure":
    sys.exit(2)
if mode == "invalid":
    print("not a response")
    sys.exit(0)
if mode == "wait":
    time.sleep(0.35)
if mode == "children":
    subprocess.Popen([sys.executable, "-c",
                      "import os,pathlib,time; time.sleep(0.8); pathlib.Path(os.environ['FAKE_CHILD_MARKER']).touch()"])
    pathlib.Path(os.environ["FAKE_READY"]).touch()
    time.sleep(20)
print(json.dumps({"text": "" if mode == "empty" else "Verdict: blocked\nA concrete finding.",
                  "stopReason": "max_tokens" if mode == "partial" else "end_turn",
                  "thought": "PRIVATE_REASONING_SENTINEL",
                  "sessionId": "synthetic-session",
                  "modelUsage": {"configured-model": {"modelCalls": 1}}}))
'''


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="grok-runner-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.work = self.root / "repository"
        self.work.mkdir()
        self.bin = self.root / "bin"
        self.bin.mkdir()
        fake = self.bin / "grok"
        fake.write_text("#!" + sys.executable + "\n" + FAKE_CLI)
        fake.chmod(0o700)
        self.prompt = self.root / "input.txt"
        self.prompt.write_text("Synthetic input: $(touch SHOULD_NOT_EXIST) `echo literal`\n")
        self.capture = self.root / "calls.jsonl"
        self.marker = self.root / "child-survived"
        self.ready = self.root / "child-ready"
        self.env = dict(os.environ, PATH=str(self.bin), GROK_HOME="existing-config-location",
                        FAKE_CAPTURE=str(self.capture), FAKE_CHILD_MARKER=str(self.marker),
                        FAKE_READY=str(self.ready), PYTHONDONTWRITEBYTECODE="1")

    def command(self, *extra):
        return [sys.executable, str(RUNNER), "--cwd", str(self.work),
                "--prompt-file", str(self.prompt), "--output-root", str(self.root),
                "--heartbeat-seconds", "0.1", *extra]

    def run_cli(self, mode="success", *extra):
        process = subprocess.run(self.command(*extra), env=dict(self.env, FAKE_MODE=mode),
                                 capture_output=True, text=True, timeout=10)
        messages = [json.loads(line) for line in process.stdout.splitlines()]
        result = json.loads(Path(messages[-1]["result"]).read_text())
        return process, messages, result

    def test_success_preserves_configuration_and_is_not_a_review_pass(self):
        process, messages, result = self.run_cli()
        self.assertEqual(process.returncode, 0)
        self.assertEqual(result["status"], "completed")
        self.assertIn("Verdict: blocked", Path(result["report"]).read_text())
        self.assertNotIn("PRIVATE_REASONING_SENTINEL", process.stdout)
        self.assertNotIn("thought", result)
        calls = [json.loads(line) for line in self.capture.read_text().splitlines()]
        self.assertEqual(len(calls), 1)
        call = calls[0]
        self.assertEqual(call["grok_home"], "existing-config-location")
        self.assertEqual(call["cwd"], str(self.work.resolve()))
        self.assertEqual(call["prompt"], self.prompt.read_text())
        self.assertNotIn("--model", call["args"])
        self.assertNotIn("--reasoning-effort", call["args"])
        self.assertIn("read_file,grep,list_dir", call["args"])
        self.assertIn("MCPTool", call["args"])
        self.assertEqual(list(self.work.iterdir()), [])
        folder = Path(messages[-1]["result"]).parent
        self.assertEqual(folder.stat().st_mode & 0o777, 0o700)
        for artifact in folder.iterdir():
            self.assertEqual(artifact.stat().st_mode & 0o777, 0o600)

    def test_failure_classes_and_partial_outputs_never_pass(self):
        for mode, expected in (("permission", "permission_denied"), ("failure", "cli_failed"),
                               ("invalid", "invalid_output"), ("empty", "empty_response"),
                               ("partial", "incomplete_response")):
            with self.subTest(mode=mode):
                process, _, result = self.run_cli(mode)
                self.assertNotEqual(process.returncode, 0)
                self.assertEqual(result["failure"], expected)

    def test_progress_is_visible_before_completion(self):
        process, messages, result = self.run_cli("wait")
        self.assertEqual(process.returncode, 0)
        progress = [item for item in messages if item["status"] == "running"]
        self.assertGreaterEqual(len(progress), 3)
        self.assertTrue(any(item["stderr_bytes"] > 0 for item in progress))
        self.assertEqual(result["status"], "completed")

    def test_explicit_timeout_stops_descendants_and_retains_input(self):
        process, _, result = self.run_cli("children", "--timeout-seconds", "0.3")
        self.assertNotEqual(process.returncode, 0)
        self.assertEqual(result["status"], "timed_out")
        self.assertEqual(Path(result["prompt_file"]).read_text(), self.prompt.read_text())
        time.sleep(1)
        self.assertFalse(self.marker.exists())

    def test_sigterm_stops_descendants_and_records_interruption(self):
        process = subprocess.Popen(self.command(), env=dict(self.env, FAKE_MODE="children"),
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            deadline = time.monotonic() + 5
            while not self.ready.exists() and time.monotonic() < deadline:
                time.sleep(0.02)
            self.assertTrue(self.ready.exists())
            process.send_signal(signal.SIGTERM)
            stdout, _ = process.communicate(timeout=7)
            result = json.loads(Path(json.loads(stdout.splitlines()[-1])["result"]).read_text())
            self.assertEqual(result["status"], "interrupted")
            time.sleep(1)
            self.assertFalse(self.marker.exists())
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate()

    def test_retry_uses_saved_input_and_preserves_prior_evidence(self):
        _, _, first = self.run_cli("permission")
        self.prompt.write_text("Changed input must not replace the saved attempt")
        _, _, second = self.run_cli("success", "--prompt-file", first["prompt_file"])
        self.assertEqual(first["prompt_sha256"], second["prompt_sha256"])
        self.assertNotEqual(first["prompt_file"], second["prompt_file"])
        self.assertTrue(Path(first["stderr"]).exists())
        self.assertEqual(len(self.capture.read_text().splitlines()), 2)

    def test_explicit_overrides_only(self):
        self.run_cli("success", "--model", "requested-model", "--reasoning-effort", "high")
        args = json.loads(self.capture.read_text())["args"]
        self.assertEqual(args[args.index("--model") + 1], "requested-model")
        self.assertEqual(args[args.index("--reasoning-effort") + 1], "high")

    def test_missing_cli_records_failure_without_launch(self):
        self.env["PATH"] = ""
        process, _, result = self.run_cli()
        self.assertNotEqual(process.returncode, 0)
        self.assertEqual(result["failure"], "cli_not_found")
        self.assertFalse(self.capture.exists())

    def test_invalid_input_does_not_launch(self):
        self.prompt.write_bytes(b"\xff")
        process = subprocess.run(self.command(), env=self.env, capture_output=True)
        self.assertEqual(process.returncode, 2)
        self.assertFalse(self.capture.exists())


if __name__ == "__main__":
    unittest.main()
