# Reviewer And Challenger Agreement

Use this contract for paired plan and Final reviews. The calling skill defines
when to review and which roles participate; pairing adds no review boundaries.

## Establish Comparable Results

Give both roles the same goal, constraints, review scope, draft revision or
repository snapshots (including relevant worktree changes), raw evidence, and
limitations. Initial assessments are independent: omit the other role's verdict
and any desired conclusion. Each role returns the reviewed state, a verdict of
`pass`, `blocked`, or `incomplete`, material findings with evidence, and critical
evidence gaps. Missing required evidence prevents a pass.

The challenger actively examines assumptions, avoidable complexity, and
counterexamples; it is not an endorsement step. Both roles retain their own
evidence-based judgment. Treat peer reports as claims to check.

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

If initial results already establish agreement, do not add a confirmation
round. Two blocked verdicts with different findings do not by themselves
establish agreement on the combined blocker set.

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

Reviewers prioritize correctness and acceptance; challengers emphasize design
assumptions and whether a simpler implementation meets the same contract.
Both check unnecessary abstractions, dependencies, state, speculative guards,
duplicate responsibilities, and unapproved scope. A complexity finding blocks
only when tied to an unmet requirement or a concrete correctness, security,
compatibility, authority, or other required-condition failure. An equivalent
simpler option alone is non-blocking. Preserve necessary safeguards and settled
user tradeoffs; reopen them only when new evidence exposes a material failure.

## Availability And Recording

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
