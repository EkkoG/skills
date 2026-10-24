# Shared Grok Invocation

Both Grok-backed roles use `scripts/run_grok_review.py` from this installed
`design-delivery-plan` skill. The coordinator supplies its absolute path in the
task packet, including for Final. The script uses Python 3's standard library.

## Input And Authority

The coordinator supplies an existing, authorized private review directory:
`reviews/` beside `plan.md` for planning, or beside `delivery.md` for Final.
Create it with user-only permissions, normally `0700`, through normal approval
when needed. Prepare one private UTF-8 prompt file there, or reuse the
coordinator's existing packet. The coordinator can supply this file when the
role lacks scratch-write permission.
Include the role's challenge contract,
current plan or approved Goal, reviewed state, necessary evidence and limits.
Initial input excludes prior verdicts and review history; give current-contract
excerpts when a source document mixes them. Let Grok inspect bounded raw evidence
through its read tools instead of performing another full review in Codex first.

The user's explicit request to use Grok authorizes sending the necessary
task-relevant review materials to the CLI's configured service. Proceed within
that scope. Keep secrets and unrelated material out of the packet. Use the existing
CLI environment and configuration; model and effort come from that configuration
unless the user explicitly overrides them. Obtain model identity from result
metadata when available, not from credential/configuration files.

## One Invocation

```sh
python3 /absolute/skill/scripts/run_grok_review.py \
  --cwd /absolute/repository \
  --prompt-file /absolute/persistent/reviews/review-prompt.txt \
  --output-root /absolute/persistent/reviews
```

Use this entry point directly with the supplied `--output-root`. It snapshots
the prompt, invokes Grok once with read-only tools and no Web/subagents, and
retains a unique private output folder inside that persistent review directory.
Files are user-private. The script does not read credentials, alter Grok
configuration, grant permissions or retry.

Grok needs network access and writes its own runtime/session state. If the active
execution environment requires approval for that access, use its normal approval
mechanism for this exact helper invocation, identifying the material and configured
destination.
Read-only tool limits are behavioral constraints, not OS sandbox isolation.

## Observe And Recover

The helper prints a starting/running/final status and a heartbeat every 30
seconds with elapsed time, output byte counts and the `result.json` path.
It writes stdout and stderr directly to private files while Grok runs. Byte
growth shows activity, not substantive review progress; silence is not failure.
Wait in normal short windows. Use one bounded status or diagnostic check if
stagnation is suspected. Avoid repeatedly reading Grok's sessions or configuration.

There is no implicit process deadline. `--timeout-seconds` sets an explicit
whole-process limit when needed; polling intervals are not deadlines. An explicit
timeout or interruption terminates the invocation's process group and retains
the attempt's artifacts.

For `permission_denied`, request the required normal approval and rerun using
the saved `prompt.txt`. Other nonzero CLI exits remain `cli_failed`; a model-list
refresh warning alone does not prove authentication failure. Inspect only a
bounded, redacted diagnostic excerpt if needed. A rejected approval before
launch has no helper result: distinguish an explicit denial from a transient
approval-service error. An explicit denial stops the action; a transient service
error permits one normal recovery request for the same authorized operation.
Keep the gate pending if that recovery fails, under the shared agreement rules.

## Return

Read `result.json` and `report.md`. `completed` means a successful CLI exit and
a nonempty final response with `stopReason=end_turn`, not an acceptance verdict.
Return Grok's verdict and findings faithfully; missing evidence or an incomplete
assessment still prevents agreement. Partial output is never a pass.

`stdout.json` is retained privately and may contain internal reasoning; report
only the extracted final text and selected metadata. Runtime diagnostics can
contain sensitive material and must be redacted before sharing. Link existing
artifacts instead of copying a full transcript. Retain the prompt, result and
logs through recovery/handoff; each retry gets a new directory without replacing
earlier evidence. Confirm referenced files exist before giving a rerun command.
