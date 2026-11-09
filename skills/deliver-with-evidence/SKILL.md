---
name: deliver-with-evidence
description: Execute an explicitly approved multi-step engineering plan with proportional evidence, role-based review, Delivery tracking, and local commits. Use for approved broad refactors, migrations, and end-to-end programs; do not use for planning, status questions, ordinary review, or a single bounded fix.
---

# Deliver With Evidence

Execute one reviewable part of an approved plan at a time and keep local
progress distinct from Whole Goal completion.

## Start From Approval

Before production work, verify that the approved contract contains the final
outcome, scope and exclusions, Work Packages and dependency graph, acceptance
labels, compatibility promises, intentional removals, risks, exceptions, and
required evidence. If it is missing or materially changed, stop and hand the
work to `$design-delivery-plan`.

Every approved plan executed through this skill requires a private persistent
Delivery document before the first production edit. Read the relevant parts of
[references/delivery-document.md](references/delivery-document.md) for path,
permissions, fields, repository state, and atomic updates. The coordinating
agent is its only writer. Keep the document after completion.

Before costly work, resolve material unknowns about toolchains, required gates
or evidence access with the cheapest useful preflight. This establishes
feasibility, not acceptance, and does not itself require a reviewer. Keep
routine preflight and its in-scope fixes within the current Slice.
Retain working toolchain commands in Delivery and reuse them on resumption
while the relevant environment remains unchanged.

## Keep Implementation Minimal

Implement only the current approved outcome. Within the assigned scope, judge
cumulative changes against the goal's comparison baseline. Retain it in Delivery
from the plan, or establish it from the approved goal and available pre-change
evidence when absent. Prefer the simplest, most direct,
verifiable and maintainable option with the smallest complete change. If a
necessary large-scale change is not already explicitly authorized, explain why
a smaller change is insufficient, the proposed scope, and principal costs and
risks, and obtain the user's decision before affected implementation.
Continue within explicitly approved bounds. Add complexity only when a simpler
option cannot meet an in-scope need established below, and explain that need.

Keep simple logic at its call site. Extract a helper or abstraction for actual
reuse, a genuinely complex boundary, or a clear concept that improves readability.
Follow existing project idioms. Add state, dependencies, fallback paths, or
compatibility layers only for approved requirements, existing commitments, or
failure paths supported by current code, callers, inputs, trust boundaries,
and deployment conditions. Establish that scope basis before designing the
handling; prior incidents are not required. Scenarios based only on unsupported
future changes, imagined usage, or speculative failure combinations generate
no new implementation work, tests, acceptance conditions, or user confirmation
questions.
Preserve required security, data integrity, reliability, and compatibility.

For in-scope low-frequency scenarios, prefer simple, explicit handling, weighing
likelihood and impact against implementation and maintenance cost. Surface only
material unresolved tradeoffs affecting current use, reliability, or operations
for the user's decision, such as manual recovery or limits on supported scenarios.

Validate unknown input at its owning input or trust boundary. Within that
boundary, rely on guarantees already established by validation, construction,
or types; reassess when data or trust boundaries change.

Exercise the actual implementation rather than copies of its logic; prefer
fixtures and real code paths, using test doubles where isolation requires them.

As implementation or correction adds a mechanism, check the current requirement,
existing capability, and whether simplifying the affected design removes the need.
Main resolves routine local choices and carries out design choices specifically
settled by the approved contract within their agreed bounds.

Resolve material design choices before introducing the mechanism or its dependent
consumers. Examples include an independent source
of truth, persistence, a background lifecycle, a shared cross-module layer, or
changed ownership when they materially affect responsibility, coupling,
operational burden, or reversibility. Pause the affected production work;
independent work within the assigned Slice may continue. Main evaluates the
current need, why the simpler existing path is insufficient, and maintenance
cost. A helper or local data structure with no such impact remains an ordinary
implementation decision.

The coordinator resolves choices within the approved contract and records
material decisions in the existing Slice/Delivery entry. Material requirement
tradeoffs or changes to approved boundaries follow the existing user approval
and plan-change rules. Review dispatch still follows the risk criteria below.

## Route Execution Roles

- Main is the sole production and Delivery writer. It implements consecutive
  dependency-ready Slices, including local discovery, verification, documentation
  and corrections, retaining the working context between Slices.
- Use `explorer` only before Slice selection when a bounded unknown can change
  Slice scope, authority, dependencies, or acceptance. Main handles ordinary
  Slice-local discovery.
- Use `implementation_reviewer` only at a stable pre-Final boundary with a
  concrete failure risk whose discovery at Final would materially increase
  harm or rework. Explain the failure scenario and delayed-discovery cost using
  actual behavior or authority. Dependencies identify downstream work that must
  wait for this verdict. Other changes receive focused verification and Final
  coverage. Reuse the reviewer for original-blocker and direct-regression
  closure; start fresh for a new boundary.
- Start Final with a fresh `final_reviewer` on the stable Whole-Goal packet.
  After its report, use a fresh `challenger` by default to challenge that report
  against the same packet. `agreed-pass` closes the independent review gate.
  Review closure, correction and availability rules are in
  [references/acceptance-review.md](references/acceptance-review.md).
  Implementation-risk review remains a single `implementation_reviewer` pass.
  Review roles use only non-mutating reads; checks requiring writes return to
  the coordinator. A writable sandbox does not block review; disclose the lack
  of sandbox isolation. Unavailability follows that reference's fallback rules.
- Start each new delegated role, including replacements, with
  `spawn_agent(..., fork_turns="none")`. Supply the review packet in the
  delegation message, with task context and exact paths to existing sources.
  For an ended role's same-boundary correction, use `followup_task`
  to start its next turn. Use `send_message` only to supplement a running pass;
  it does not start a turn. A new review boundary gets a fresh reviewer.

Before falling back for a required role, establish an explicit tool or policy
restriction, or an actual start/resume failure that remains after one applicable
recovery attempt. Judge availability separately for each role; task listings
describe existing tasks, not which roles can be started. Recover invocation
conflicts by reusing an eligible agent or choosing a unique task name. Disclose
the restriction or error and recovery outcome, and record them in Delivery.

Make that message self-contained: identify the workspace, goal baseline,
stable repository states, exact scope and exclusions, and reference approved
conditions, preserved behavior, required evidence and raw-evidence locations
in the existing plan and Delivery. Give each
reviewer and challenger the installed absolute path to the
[shared quality criteria](../design-delivery-plan/references/review-agreement.md#preserve-the-quality-threshold)
and require reading and applying that section. Do not suggest a desired verdict.
Delegated roles use only non-mutating reads and return one compact result with
reviewed scope and state, findings, evidence locations, limitations, and a verdict
when reviewing. Main alone edits code, tests, plans and Delivery, selects work,
creates commits and declares formal completion. Keep the reviewed scope unchanged
until the complete review and any required challenge return. Independent work
may continue when it preserves the reviewed state.

## Coordinate The Delivery

The coordinating agent alone interprets the contract, selects the current
Slice, accepts evidence, updates Delivery, changes formal status, records
approved exceptions, and declares Work Package, Milestone, or Goal completion.
Accept results by matching the supplied raw evidence to required conditions
and checking relevance, limits and unresolved blockers. Main owns diagnosis,
implementation and checks; independent reviewers evaluate acceptance.

Resume the recorded unfinished Slice when its contract, dependencies, and code
state remain valid. Otherwise choose one dependency-ready outcome that removes
a blocker or advances a ready package. A Slice owns one complete result,
including local discovery, implementation, necessary tests, guards and
documentation. Main continues routine diagnosis and corrections within that
contract, resolving material scope, permission, dependency or risk-boundary
decisions under the approved contract. Do not pre-plan later Slices.

Assign IDs as `<WP-ID>-S<NN>`, for example `WP-01-S01`. Allocate an ID only at
selection and never rename, renumber, or reuse a recorded ID. Record why it is
current, the acceptance labels it advances, local outcome, preserved behavior,
expected scope, and focused exit evidence. Resolve its acceptance labels directly
from the approved source, preserving required behavior, intentional removals and
constraints. A Slice adds execution scope and evidence, while the source conditions
remain authoritative. Before editing, align its local outcome and scope with those
conditions and identify what this Slice will establish. Correct conflicting Slice
wording against the approved source; use plan-change rules when that source
contract itself must change. Keep conditions only partly covered by a Slice
partial until their remaining work and evidence are complete.

After a Slice and its focused evidence are stable, Main records acceptance,
repository and commit state, evidence links and the next action in one Delivery
update using its observations and independent findings. Existing logs and review
results normally suffice; create separate reports or snapshot manifests only
for a concrete recovery, reproducibility or concurrency need.

When evidence requires a material contract change, stop before implementing it,
record the conflict, use `$design-delivery-plan`, and resume only after user
approval. For an approved revision, read
[references/goal-change-record.md](references/goal-change-record.md) and update
the current contract and affected status atomically.

## Commit Stable Checkpoints

After accepting focused Slice evidence, create a local checkpoint when the
result is coherent, recoverable, and continuing would complicate attribution,
rollback, ownership, or interruption recovery. Adjacent Slices may share one
checkpoint when they form one outcome. Continue without committing when the
next Slice directly completes the same unfinished outcome. Never commit failed,
incomplete, or inconsistent state.

Execution of an approved plan authorizes these focused local commits unless the
user or repository explicitly opts out. Use the `commit` skill for staging,
scope, message style, and reporting. Include only the stable checkpoint;
preserve unrelated changes; do not push, create branches, amend, rebase, or
rewrite history. For multiple repositories, all intended repository commits
must succeed before a logical checkpoint is complete; otherwise record the
partial state and blocker and stop dependent work.

## Review And Accept

Record a risk boundary as review-ready only when its implementation,
dependencies, fixed snapshots, and focused evidence are stable. Match the
conditions being submitted to their approved source and current evidence;
identify any remaining work explicitly in the packet. Defer broad
evidence until the boundary that owns it. Read the applicable sections of
[references/acceptance-review.md](references/acceptance-review.md) before
closing a Work Package, Milestone, or Goal.

Close a Work Package locally when its conditions and dependencies have current
evidence. Use a Milestone for one stable boundary containing one or more Work
Packages.

Open Final only after known production changes, required documentation, and the
evidence packet are stable. Obtain Whole-Goal `agreed-pass` from
`final_reviewer` followed by `challenger` under the acceptance reference. Batch
blockers from one boundary into a corrective Slice. Once it is stable and invalidated
evidence is refreshed, close affected conditions with the original reviewer
followed by the original challenger, or restart full review when the reference's
criteria apply.

Run focused checks on each corrected state as needed to finish its outcome.
Reserve expensive boundary-wide checks, final builds and Whole-Goal hygiene
for their relevant stable source. Preflight is not a substitute for these
required gates. Reuse valid evidence; rerun only checks affected by changed
code, inputs, tests, rules or contract. Documentation-only, formatting-only and
unrelated changes do not invalidate production evidence.
When durable output is needed, capture it in the original check; reuse existing
valid output when assembling later review artifacts.

Delivery status and commit records locate evidence but do not prove completion.
Before declaring the Whole Goal complete, account for every required condition
and confirm that both Final verdicts cover the current relevant state under the
acceptance reference's correction and exception rules.
Report the achieved outcome, verification, preserved behavior, blockers,
repository state, and exact Slice, Work Package, Milestone, and Goal status.
Read [references/handoff.md](references/handoff.md) before writing an explicit
execution handoff.
