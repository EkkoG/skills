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

## Keep Implementation Minimal

Implement only the current approved outcome. Prefer the simplest, most direct,
verifiable and maintainable option with the smallest complete change. If a
necessary large-scale change is not already explicitly authorized, return it
to the coordinator before affected implementation. Explain why a smaller change
is insufficient, the proposed scope, and principal costs and risks so the
coordinator can obtain the user's decision through the existing approval path.
Continue within explicitly approved bounds. Add complexity only when a simpler
option cannot meet an explicit requirement, and explain that requirement.

Keep simple logic at its call site. Extract a helper or abstraction for actual
reuse, a genuinely complex boundary, or a clear concept that improves readability.
Follow existing project idioms. Add state, dependencies, fallback paths, or
compatibility layers only for current requirements or concrete failure modes.
Preserve the contract's required security, reliability, and compatibility.

For low-frequency scenarios, prefer simple handling, weighing likelihood and
impact against implementation and maintenance cost. Return material unresolved
tradeoffs, such as manual recovery, slower recovery, or limits on supported
scenarios, to the coordinator for the user's decision.

Validate unknown input at its owning input or trust boundary. Within that
boundary, rely on guarantees already established by validation, construction,
or types; reassess when data or trust boundaries change.

Exercise the actual implementation rather than copies of its logic; prefer
fixtures and real code paths, using test doubles where isolation requires them.

As design choices emerge during implementation, check the current requirement,
existing capability, and simplest sufficient approach before adding a mechanism.
Routine local choices remain with the implementation owner. Carry out design
choices specifically settled by the approved contract within their agreed bounds.

Return an unresolved material design choice to the coordinator before introducing
the mechanism or its dependent consumers. Examples include an independent source
of truth, persistence, a background lifecycle, a shared cross-module layer, or
changed ownership when they materially affect responsibility, coupling,
operational burden, or reversibility. Pause the affected production work;
independent work within the assigned Slice may continue. Briefly explain the
current need, why the simpler existing path is insufficient, added maintenance
cost, and recommended choice. A helper or local data structure with no such
impact remains an ordinary implementation decision.

The coordinator resolves choices within the approved contract and records
material decisions in the existing Slice/Delivery entry. Material requirement
tradeoffs or changes to approved boundaries follow the existing user approval
and plan-change rules. Review dispatch still follows the risk criteria below.
For material hardening beyond scope, include the failure scenario, likelihood,
impact, and complexity cost in the decision request.

## Route Execution Roles

- Use `explorer` only before Slice selection when a bounded unknown can change
  Slice scope, authority, dependencies, or acceptance. The `executor` owns
  ordinary Slice-local discovery.
- Delegate every non-trivial approved production Slice to `executor`, including
  resumed and corrective Slices. The main agent may implement a simple low-risk
  Slice directly. Treat a Slice as non-trivial when it crosses files or
  modules, changes a shared authority, needs isolated write context, or has
  acceptance evidence that the main thread cannot safely own. Reuse an executor
  for continuing work and corrections within one domain, authority and
  acceptance context. Start a fresh executor for an independent domain with a
  minimal complete packet; stop the prior writer before transferring ownership.
- Use `implementation_reviewer` only at a stable pre-Final boundary with a
  concrete failure risk whose discovery at Final would materially increase
  harm or rework. Explain the failure scenario and delayed-discovery cost using
  actual behavior or authority. Dependencies identify downstream work that must
  wait for this verdict. Other changes receive focused verification and Final
  coverage. Reuse the reviewer for original-blocker and direct-regression
  closure; start fresh for a new boundary.
- Start Final with a fresh `final_reviewer` on the stable Whole-Goal packet.
  After its report is available, use a fresh `challenger`, which invokes Grok
  to challenge that report and consequential omissions against the same state
  and raw evidence. Reuse the pair for local corrective closure; the criteria
  for a fresh full review and required agreement are in
  [references/acceptance-review.md](references/acceptance-review.md).
  Implementation-risk review remains a single `implementation_reviewer` pass.
  Review roles use only non-mutating reads; checks requiring writes return to
  the coordinator. A writable sandbox does not block review; disclose the lack
  of sandbox isolation. Unavailability follows that reference's fallback rules.
- Start delegated execution and review work with `fork_turns="none"` and a
  self-contained packet; reference exact paths rather than copying long
  documents.

Before falling back for a required role, establish an explicit tool or policy
restriction, or an actual start/resume failure that remains after one applicable
recovery attempt. Judge availability separately for each role; task listings
describe existing tasks, not which roles can be started. Recover invocation
conflicts by reusing an eligible agent or choosing a unique task name. Disclose
the restriction or error and recovery outcome, and record them in Delivery.
If `executor` remains unavailable, the coordinator may take over the authorized
Slice only after the previous writer has stopped, retaining the same
verification and review gates.

Give delegated roles a self-contained packet with the workspace, stable
repository states, approved conditions, exact scope and exclusions, preserved
behavior, required evidence, and raw-evidence locations. Include the constraints
from Keep Implementation Minimal in every executor packet. Give each reviewer
and challenger the installed absolute path to the
[shared quality criteria](../design-delivery-plan/references/review-agreement.md#preserve-the-quality-threshold)
and require reading and applying that section. Do not suggest a desired verdict.
Delegated roles return evidence and findings; they do not edit
Delivery, change the plan, select later work, create commits, or declare a
formal boundary complete. Return one compact result with changed scope,
outcome, reproducible evidence and locations, verification-state references,
limitations and whether production writing has stopped. Keep one production
writer; independent work may continue during review when it cannot invalidate
the reviewed state.

## Coordinate The Delivery

The coordinating agent alone interprets the contract, selects the current
Slice, accepts evidence, updates Delivery, changes formal status, records
approved exceptions, and declares Work Package, Milestone, or Goal completion.
Accept results by matching the supplied raw evidence to required conditions
and checking relevance, limits and unresolved blockers. The executor owns local
diagnosis, implementation and checks; the reviewer owns independent challenge.
Main investigates code or reproduces checks when evidence conflicts, material
gaps or consequential decisions require it, rather than repeating both roles.

Resume the recorded unfinished Slice when its contract, dependencies, and code
state remain valid. Otherwise choose one dependency-ready outcome that removes
a blocker or advances a ready package. A Slice owns one complete result,
including local discovery, implementation, necessary tests, guards and
documentation. The executor continues routine diagnosis and corrections within
that contract without a new packet for each failed check. Return material
scope, permission, dependency or risk-boundary decisions to Main. Do not
pre-plan later Slices.

Assign IDs as `<WP-ID>-S<NN>`, for example `WP-01-S01`. Allocate an ID only at
selection and never rename, renumber, or reuse a recorded ID. Record why it is
current, the acceptance labels it advances, local outcome, preserved behavior,
expected scope, and focused exit evidence.

The implementation owner completes the Slice and focused evidence before
reporting a stable result. The coordinator records acceptance, repository and
commit state, evidence links and next action in one Delivery update. Existing
logs and the result packet normally suffice; create separate reports or
snapshot manifests only for a concrete recovery, reproducibility or concurrency
need.

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
dependencies, fixed snapshots, and focused evidence are stable. Defer broad
evidence until the boundary that owns it. Read the applicable sections of
[references/acceptance-review.md](references/acceptance-review.md) before
closing a Work Package, Milestone, or Goal.

Close a Work Package locally when its conditions and dependencies have current
evidence. Use a Milestone for one stable boundary containing one or more Work
Packages.

Open Final only after known production changes, required documentation, and the
evidence packet are stable. Request the initial full review from `final_reviewer`,
then give its report and the same packet to `challenger` for focused challenge.
Final passes only when both agree on a pass and all material dispositions on
that state. Batch blockers from one boundary into a corrective Slice. Once it
is stable and invalidated evidence is refreshed, use the correction procedure
in the acceptance reference to close affected conditions with the existing pair
or restart full review when its criteria apply. Reconcile verdict-only
disagreements with the existing pair.

Run focused checks on each corrected state as needed to finish its outcome.
Reserve expensive boundary-wide checks, final builds and Whole-Goal hygiene
for their relevant stable source. Preflight is not a substitute for these
required gates. Reuse valid evidence; rerun only checks affected by changed
code, inputs, tests, rules or contract. Documentation-only, formatting-only and
unrelated changes do not invalidate production evidence.

Delivery status and commit records locate evidence but do not prove completion.
Report the achieved outcome, verification, preserved behavior, blockers,
repository state, and exact Slice, Work Package, Milestone, and Goal status.
Read [references/handoff.md](references/handoff.md) before writing an explicit
execution handoff.
