# Review Decisions And Conditional Challenge

Use this contract for independent plan and Final reviews. The calling skill
defines when a reviewer is required; a challenge uses the same review boundary.

## Review And Decide Whether To Challenge

The reviewer first evaluates the goal, constraints, review scope, stable draft
or repository snapshots, and raw evidence. Its report identifies the reviewed
state, verdict, material findings and proposed corrections, supporting reasons
and evidence, and coverage limitations.

The reviewer normally supplies the independent verdict. Add a challenger when
an important design tradeoff remains disputed, evidence materially conflicts
with the review's reasoning, or a high-consequence acceptance judgment remains
uncertain. A user-requested challenge also qualifies. Record the concrete question
in the existing review entry. Clear blockers go to correction and missing evidence
to collection with the original reviewer.

For a triggered challenge, give the challenger the available report and access to
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

## Close The Review

Without a triggered challenge, record the reviewer's verdict. A `pass` with all
material findings resolved satisfies the independent review gate; `blocked` or
`incomplete` requires correction or evidence before acceptance.

Once a challenge is triggered, close it with both participants before acceptance.
Apply the agreement rules below to their conclusions on the current state,
retaining unaffected conclusions while their supporting inputs remain valid.

Agreement means the same acceptance verdict and compatible dispositions of
every material finding on the same current state. It does not require matching
wording, optional advice, or severity labels that do not change disposition.
A factual discrepancy is material when it could change acceptance, a finding's
disposition, or the validity of required evidence. For other report details,
the coordinator uses available evidence to record a supported correction or
uncertainty while retaining verdicts; that alone does not reopen paired review.

| Results | Review status | Next action |
|---|---|---|
| Both pass; every material finding is resolved | agreed-pass | Review gate satisfied; normal approval or acceptance still applies |
| Both confirm the blocking findings and their dispositions | agreed-blocked | Review has a settled result; correct blockers, not acceptance |
| Conflicting verdicts or material finding dispositions | pending | Reconcile disputed items |
| Unavailable participant, incomplete review or evidence, or incompatible snapshots | pending | Restore the missing prerequisite |

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
add avoidable complexity. Apply these complexity criteria within existing plan,
implementation-risk, and Final reviews.

First establish necessity for mechanisms, work items, tests, acceptance
conditions, and proposed corrections: which current requirement or existing
commitment would fail without them, under what actual conditions? Trace derived
plan, Slice, and test obligations to that need. Within the assigned scope,
compare cumulative design changes against the current goal's baseline, including
mechanisms retained through earlier corrections. Ground the answer in requirements
or current code, callers, inputs, trust boundaries, and deployment conditions;
prior incidents are not required. Recommend omitting
proposed work based only on unsupported future changes, imagined usage, or
speculative failure combinations; those scenarios do not justify extra proof
or user confirmation questions. Apply the blocking and correction thresholds below.

Then evaluate the smallest complete change that meets that need and required
safeguards, judging scope by responsibilities and behavior rather than line count.
When a proposed correction adds mechanisms, check whether simplifying the
affected design can remove the failure while preserving the required outcome.
Route a necessary, unapproved large-scale change to the coordinator with its
justification, scope, and principal costs and risks for the user's decision.
Honor explicitly approved scope under the tradeoff rules below.

A material complexity finding identifies a specific mechanism without current
value, a feasible simpler alternative preserving required behavior and
safeguards, and a significant avoidable maintenance or operational burden.
Support it with current consumers, responsibilities, or state transitions;
examples of concrete burden include duplicate state synchronization, extra
configuration ownership, or unnecessary dependency lifecycles. Style, line
counts, or a merely shorter alternative remain non-blocking.

In planning, demonstrated material avoidable complexity can block approval
even when the proposed behavior is correct. Implementation and Final apply the
same standard to complexity introduced by the work under review, weighing the
smallest correction's cost and regression risk. A disproportionate redesign
remains advice unless a required condition or concrete engineering failure
independently requires it. Changes to the approved contract return to the
coordinator under the existing approval rules.

For in-scope low-frequency scenarios, favor simple, explicit handling after
weighing likelihood and impact. Additional robustness needs a concrete benefit
proportionate to its implementation and maintenance burden. Surface only material
unresolved tradeoffs affecting current use, reliability, or operations for the
user's decision.

Honor a user's explicit acceptance of a specific design tradeoff and its cost;
general plan approval alone is not acceptance of every implementation choice.
Reopen that specific tradeoff only when new evidence exposes a material failure.
Preserve required security, data integrity, reliability, compatibility, and
recovery behavior.

Include a brief complexity conclusion in the existing review or challenge
report: name the consequential mechanisms examined and their current value,
or identify the supported simplification and burden removed. A report may
conclude that the scope adds no substantive complexity. Findings follow the
evidence; no inventory, separate review round, or finding quota is required.

## Availability And Recording

Required reviewers and triggered challengers run as native subagents. Keep startup, runtime, and access
failures separate from substantive verdicts; require an explicit verdict
supported by evidence for the reviewed state.

After one applicable recovery attempt, an unavailable required reviewer or
triggered challenger leaves that review pending. A disclosed local diagnostic
fallback can identify work to do, but cannot replace a required independent verdict.
Report the limitation and ask the user how to proceed. Only an
explicit user revision of this gate can authorize a different completion path;
record the exception and actual review coverage.

The coordinator alone records the reviewed state, reviewer result, material
dispositions, and any triggered challenge's reason, result and agreement status
in the existing plan-review summary or Delivery evidence. Link existing outputs;
no extra report or command transcript is required. A reviewer `pass`, or an
`agreed-pass` when challenged, satisfies the review gate. User approval and required
evidence still apply. Blocked, incomplete and pending reviews never authorize acceptance.
