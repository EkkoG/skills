# Reviewer And Challenger Agreement

Use this contract for paired plan and Final reviews. The calling skill defines
when to review and which roles participate; pairing adds no review boundaries.

## Review Then Challenge

The reviewer first evaluates the goal, constraints, review scope, stable draft
or repository snapshots, and raw evidence. Its report identifies the reviewed
state, verdict, material findings and proposed corrections, supporting reasons
and evidence, and coverage limitations.

After the report is available, give the challenger that report and access to
the same contract, reviewed state (including worktree changes), and raw evidence.
Require a report covering the supplied state before starting the challenge.
The challenger checks findings, blocker severity, the verdict's support, and
consequential omissions. It also challenges unnecessary complexity in both the
solution and the reviewer's proposed corrections. Scope evidence reads to
these judgments and plausible critical omissions; expand when concrete
counterevidence requires it. The reviewer owns full review coverage.

Both roles retain independent evidence-based judgment; supply no desired
conclusion. The challenger treats the report as claims to verify and returns
its own `pass`, `blocked`, or `incomplete` verdict on the reviewed state,
agreement or disagreement with material findings, new findings, and evidence
limitations. Missing required evidence prevents a pass.

## Decide Agreement

Agreement means the same acceptance verdict and compatible dispositions of
every material finding on the same current state. It does not require matching
wording, optional advice, or severity labels that do not change disposition.

| Results | Review status | Next action |
|---|---|---|
| Both pass; every material finding is resolved | agreed-pass | Review gate satisfied; normal approval or acceptance still applies |
| Both confirm the blocking findings and their dispositions | agreed-blocked | Review has a settled result; correct blockers, not acceptance |
| Conflicting verdicts or material finding dispositions | pending | Reconcile disputed items |
| Missing role, failed CLI, incomplete evidence, or incompatible snapshots | pending | Restore the missing prerequisite |

When the challenger confirms the verdict and material dispositions with no
new blocker or consequential gap, record agreement directly. New or disputed
material findings return to the original reviewer for targeted response.
Two blocked verdicts alone do not establish agreement on different blocker sets.

For a disagreement, the coordinator relays only the disputed items, both
rationales, and the relevant raw evidence to the same pair. Ask for explicit
dispositions such as retained blocker, resolved by correction, refuted by
evidence, or covered by a user-approved exception. Default to one targeted
reconciliation round. If disagreement remains, keep the gate pending and
present the exact dispute and needed evidence or user decision. Do not force
concessions or continue an open-ended debate.

Material plan or implementation changes invalidate the affected conclusions.
Follow the calling skill's correction rules and obtain verdicts covering the
current state before recording agreement; valid unaffected evidence is reusable.

## Preserve The Quality Threshold

Reviewers prioritize correctness and acceptance; challengers test the review's
reasoning, critical omissions, and whether the design or proposed corrections
add avoidable complexity.
Both check unnecessary abstractions, dependencies, state, speculative guards,
duplicate responsibilities, and unapproved scope. A complexity finding blocks
only when tied to an unmet requirement or a concrete correctness, security,
compatibility, authority, or other required-condition failure. An equivalent
simpler option alone is non-blocking. Preserve necessary safeguards and settled
user tradeoffs; reopen them only when new evidence exposes a material failure.

## Availability And Recording

Grok-backed roles use the [shared invocation helper](grok-cli.md). Keep runtime
failures separate from substantive verdicts; CLI completion alone is not a pass.

After one applicable recovery attempt, an unavailable reviewer or failed Grok
invocation leaves the paired gate pending. A disclosed local diagnostic
fallback can identify work to do, but cannot replace either participant or count
as agreement. Report the limitation and ask the user how to proceed. Only an
explicit user revision of this gate can authorize a different completion path;
record that as an exception, not as two-party agreement.

The coordinator alone records the state, both results, material dispositions,
and agreement status in the existing plan-review summary or Delivery evidence.
Link existing outputs; no extra report or command transcript is required.
`agreed-pass` makes a plan review-ready for user approval or satisfies the Final
review gate. It does not waive required evidence or grant implementation
authority. `agreed-blocked` and `pending` never authorize acceptance.
