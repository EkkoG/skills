---
name: deliver-with-evidence
description: Execute explicitly approved multi-step engineering plans with proportional Slice, Milestone, and Final verification, readable text evidence, and whole-goal acceptance. Use automatically when the user asks to implement, continue, finish, or take over an approved architecture migration, broad refactor, multi-work-package plan, or other end-to-end engineering program where local success could be mistaken for whole-goal completion; also use when explicitly invoked as $deliver-with-evidence for such an approved multi-step program. If no approved plan exists or a material plan revision is required, stop and hand planning to design-delivery-plan instead of authoring the plan. Do not use for status or metric questions, explanations, ordinary code review, unapproved planning, small fixes, or a single bounded implementation outside an approved program.
---

# Deliver With Evidence

Execute the smallest reviewable unit of an approved multi-step plan, preserve
reusable evidence, and keep local progress separate from whole-Goal completion.

## Respect Authority

Apply system, developer, user, repository, and referenced project instructions
before this skill. Treat natural-language project rules as valid contracts; do
not require machine-readable acceptance for every condition.

## Start From An Approved Contract

Before production work, confirm that the user approved a plan containing:

- the observable final outcome, scope, boundaries, and stable exclusions;
- Work Packages with reviewable outcomes and an explicit dependency graph;
- stable labels for every required Work Package and Goal condition;
- applicable compatibility promises, intentional removals, architecture,
  negative evidence obligations, risks, and approved exceptions.

If the approved contract is absent or materially incomplete, report the exact
gap, hand planning to `$design-delivery-plan`, and stop before changing
production content. Reuse a sufficient approved plan instead of rebuilding it.

Treat completion at three levels:

| Mode | Boundary | Typical evidence |
|---|---|---|
| Slice | One independently reviewable change | Focused tests, relevant static checks, and necessary smoke |
| Milestone | One stable acceptance or risk review boundary containing one or more Work Packages | Applicable Slice evidence plus structural, compatibility, regression, and hygiene checks |
| Final | The whole approved Goal | Every acceptance condition, required broad checks, and a distinct whole-Goal review |

Choose the smallest mode that matches the current work. A large program does
not make every change a Milestone, and Slice or Milestone success never implies
Goal completion. If acceptance discovers a required production change, leave
acceptance mode and return through a corrective Slice.

Reserve expensive full-suite, end-to-end, and exhaustive compatibility checks
for the stable boundary that needs them unless the approved plan, repository
rules, or immediate risk requires them earlier.

## Preserve Coordination Authority

The coordinating agent alone interprets the approved plan, selects the current
Slice, writes the Delivery document, changes status, approves exceptions, and
declares Work Package or Goal completion.

When delegation is available, authorized, and proportional:

- use bounded read-only discovery only when a specific uncertainty must be
  resolved before selecting or contracting the Slice; leave Slice-local
  discovery to the production-writing capability;
- delegate one approved Slice contract to one production-writing capability;
- use independent read-only review for risky implementation boundaries and
  whole-Goal acceptance;
- provide a self-contained packet with workspace, stable state, approved
  conditions, exact scope and exclusions, preserved behavior, required
  evidence, and raw-evidence locations; use precise readable references instead
  of copying long plans, Delivery content, or evidence into the packet;
- require focused affected checks by default; reserve full-suite, end-to-end,
  and exhaustive compatibility evidence for the coordinating agent at the
  stable boundary described below;
- request findings without suggesting the desired verdict.

Delegated work returns a concise closure report with the local outcome,
acceptance labels, changed authorities, reproducible verification, stable
snapshot, review-boundary signals, blockers, and residual risks. It must not
expand the Slice, change the plan, choose later work, edit the Delivery
document, or mark any boundary complete. Keep only one production writer
active. Parallelize only independent work that cannot invalidate the pending
result.

On receipt, the coordinating agent checks that the result matches the Slice
contract, the reported snapshot is still current, the evidence is sufficient
for the claimed outcome, and no blocker, conflict, or scope expansion remains.
When those checks pass, reuse the delegated evidence without repeating the same
exploration, affected checks, or ordinary implementation review. Gather more
evidence only when the state changed, evidence is missing or contradictory, the
work exceeded its contract, or the acceptance claim requires a different
evidence class.

Treat read-only work as independent only when its effective sandbox is
read-only. Otherwise use a separate read-only turn or a clean-room fallback and
disclose the limitation when it affects acceptance. When delegation is
unavailable, perform the same bounded work sequentially without silently
dropping required review.

## Maintain The Delivery Document

Every plan executed through this skill requires a private persistent Delivery
document before the first production edit. Read
[references/delivery-document.md](references/delivery-document.md) completely
before initializing or resuming it, and follow that reference for path
selection, contents, evidence records, permissions, and updates.

Use an explicitly approved path when provided; otherwise use the private
`$CODEX_HOME/state/delivery/` hierarchy, with `CODEX_HOME` defaulting to
`~/.codex`. Repository-local Delivery is used only when current instructions
explicitly require it.

The coordinating agent is the sole writer. Integrate delegated results
serially and replace the document atomically. Keep one active coordinator for a
Goal; if concurrent coordination or conflicting Delivery state is detected,
stop and reconcile the current contract, implementation state, and evidence
before writing.

Record the approved contract and current state before selecting the first
Slice. Update Delivery when selecting, completing, blocking, resuming, or
invalidating a Slice and at Milestone or Final acceptance boundaries. Record
acceptance-linked evidence and the next exact action, not a command transcript.
Retain the document after completion unless an approved retention rule says
otherwise.

## Handle Plan Changes

Refine local file scope, Slice boundaries, order among dependency-ready work,
and focused verification when the approved Goal, Work Package outcomes,
compatibility promises, removals, permissions, and exceptions remain unchanged.

When evidence requires a material contract change:

1. stop before implementing the changed target;
2. record the conflicting evidence and approved condition;
3. hand substantial revision to `$design-delivery-plan`;
4. resume only after explicit user approval.

Before implementing the approved revision, read
[references/goal-change-record.md](references/goal-change-record.md), update the
complete current contract and affected status atomically, and append the change
record. Keep the initial approval stable and make the current target readable
without reconstructing history.

## Select The Current Slice

Resume the recorded unfinished Slice when its contract, dependencies, and code
state remain valid. Otherwise choose one dependency-ready Work Package outcome
that removes a blocker or half-migrated state, or advances a ready package with
the smallest useful risk boundary. Reject work that needs a material plan
decision or lacks independently reviewable exit evidence.

A Slice normally contains one cohesive outcome. Keep production changes,
targeted tests, structural guards, and necessary documentation together when
they share an authority and acceptance boundary. Split only for a material
dependency, risk, rollback, ownership, or acceptance difference. Do not
pre-plan every later Slice. Let the delegated implementation capability handle
the Slice's bounded local discovery, file-level steps, consumer updates,
superseded-path cleanup, and focused verification; do not create separate
Slices merely for those internal steps.

Before editing, assign the next Slice ID under the Work Package that owns the
outcome. Use `<WP-ID>-S<NN>`, for example `WP-01-S01`, `WP-01-S02`, and
`WP-02-S01`. Number Slices independently within each Work Package and pad the
Slice number to at least two digits. Allocate an ID only when selecting the
Slice; never rename, renumber, or reuse a recorded ID. Keep the Slice title and
any correction or follow-up relationship outside the ID.

Record:

- why it is current and which acceptance labels it advances;
- one local outcome and the behavior it preserves;
- the expected authority or implementation scope;
- focused exit evidence and any bounded structural counterexamples required.

Revalidate current code and evidence before selecting another Slice.

## Execute A Slice

For the selected Slice:

1. inspect the relevant authority boundary and worktree;
2. implement the smallest reviewable result;
3. remove superseded implementation when the approved compatibility boundary
   does not retain it;
4. add positive evidence that the new path works and proportional negative
   evidence for required replacement or removal;
5. run focused affected tests, relevant static checks, and necessary smoke;
6. resolve required focused-check failures and return a stable implementation
   with focused evidence;
7. record the completed Slice and whether it makes an acceptance or risk review
   boundary review-ready;
8. keep broad evidence deferred until the stable boundary's acceptance pass,
   after any required no-blocker implementation verdict.

Start an implementation verdict from one stable snapshot and one complete
packet. A review may gather facts earlier, but it should not issue incremental
verdicts against moving code. Broad evidence added without a production change
does not invalidate that code verdict; return it to the reviewer only when the
verdict was explicitly conditional on the missing evidence.

Block a Slice only for an approved-condition violation, demonstrated
correctness, security, permission, data, concurrency, or external compatibility
failure, failed required gate, or evidence gap needed for the claimed
completion. Treat style preferences, hypothetical extensions, and
stronger-than-contract proof as non-blocking advice.

Group blockers from one review boundary into one corrective Slice. Default to
one correction and targeted closure pass. If the same blocker class survives,
recheck the Slice contract, counterexample, and scope before further changes;
do not grow the correction into a general framework beyond the approved claim.

End with a verified worktree and recorded Delivery state, then evaluate the
stable commit boundary below. Add compatibility facades, dual tracks, or
fallbacks only when the approved external boundary requires them.

## Preserve Stable Commit Boundaries

A commit checkpoint groups one or more completed Slices into a coherent,
independently understandable and recoverable change. It is not an acceptance
level, review boundary, or separately identified planning object.

After accepting the Slice evidence and updating Delivery, create a focused
local commit through an available commit workflow when the completed work is
focused-verified, contains no half-migration or internally inconsistent state,
and one of these applies:

- adjacent completed Slices now form one useful behavior or authority outcome;
- the next production work changes repository, authority, risk, or ownership;
- continuing would materially complicate attribution, review, or rollback;
- an interruption or handoff should preserve the stable implementation.

Normally group adjacent Slices within the same authority instead of committing
each Slice or waiting for the entire Work Package. As a soft checkpoint, avoid
carrying more than three independently stable completed Slices uncommitted when
they can form a coherent commit. Ignore the count when a commit would expose an
invalid intermediate state.

Continue without committing when the next Slice directly completes the same
unfinished outcome. Do not commit failed, incomplete, or inconsistent state.
For multi-repository work, commit each repository independently when its own
coherent checkpoint is stable. The coordinating agent owns commit creation;
delegated implementation does not commit. Reuse accepted validation evidence
rather than repeating acceptance for the commit, record resulting hashes in
Delivery, and keep commit timing independent from review timing.

When a specialized commit workflow is available, use it for scope isolation,
staging, commit shape, message style, and reporting. Otherwise use native Git
while preserving the same minimum contract: include only the stable checkpoint,
preserve unrelated changes, follow repository message conventions, review the
staged diff, and report the resulting hash and remaining worktree state. Do not
push, create a branch, amend, or rewrite history as part of checkpoint creation.

## Review Stable Risk Boundaries

A risk review boundary is review-ready when its owned acceptance conditions are
implemented, relevant dependencies are stable, focused evidence names one fixed
snapshot, and no active production writer is changing the same authority.

Use an independent implementation review before Final only when:

- later production work semantically depends on the boundary's authority,
  behavior, or evidence, so a late correction would invalidate or materially
  rework that downstream work; or
- an approved security, permission, data-integrity, or migration boundary has a
  high-impact failure mode whose first discovery at Final would materially
  enlarge correction or rollback scope.

Merely running another Work Package later does not create a dependency. When
later work does not consume or rely on the reviewed boundary, preserve its
focused evidence and defer independent review to Final. Record the boundary as
implemented and locally verified with independent review deferred; do not claim
an independent verdict.

The boundary may contain one Work Package or several that share the same
authority, risk, and acceptance scope. Package numbering and completion order
do not control review timing. Genuinely independent review-ready boundaries may
be reviewed in parallel when neither can invalidate the other's snapshot.

After a no-blocker verdict, run the boundary-specific broad evidence needed for
its acceptance once on the reviewed state. When the same program-wide suite or
compatibility baseline applies unchanged to several independent boundaries and
no downstream decision needs an intermediate result, defer it to their nearest
shared Milestone and run it once there. Keep a Work Package partial only when
its own approved contract requires that deferred result. If later work changes
a reviewed authority, invalidate only the affected conditions and evidence.
Revalidate them at the next relevant stable boundary or Final; retain
unaffected evidence and package status.

## Accept Milestones And The Final Goal

Read [references/acceptance-review.md](references/acceptance-review.md)
completely before marking a Work Package, Milestone, or Goal complete. That
reference is the canonical acceptance, blocker, counterevidence, review, and
correction procedure.

Load this reference only when entering a Work Package or Milestone acceptance
pass or Final acceptance. Do not load it during Delivery initialization, Slice
selection, or ordinary Slice implementation.

For a Milestone, apply it to one stable acceptance or review boundary, its one
or more included Work Package conditions, and their dependencies. Keep the Goal
partial while later required work remains.

For Final, reconstruct every Goal and Work Package condition from the approved
contract and current implementation. Perform a distinct whole-Goal pass with
an independent reviewer when available, authorized, and proportional; otherwise
use the documented clean-room fallback. Delivery status fields locate evidence
but do not prove completion. A required production correction leaves Final
mode; complete the correction procedure before a new complete Final pass.

## Judge Evidence Proportionally

Match evidence to the claim. Behavior checks do not automatically prove
structural ownership or removal, and exact-name absence does not prove semantic
replacement. Delivery records, commits, and acceptance reports index evidence
but are not primary implementation proof.

Prefer focused evidence while code may change. Reuse authoritative evidence
when its relevant code, tests, rules, and contract are unchanged. Establish
expensive baselines once and rerun them only when their affecting state changes
or at the stable boundary that requires them. A broader check may subsume a
narrower check of the same class and state, but review cannot override a failed
required gate.

Classify broad evidence by scope. Keep evidence unique to a Work Package at its
own boundary. When several independent Work Packages converge on one downstream
Milestone, run an unchanged program-wide suite or compatibility comparison once
at that Milestone rather than after every package.

Do not run broad evidence merely to prepare a still-correctable implementation
for review. Unless the approved plan, repository rules, or immediate Slice risk
requires it earlier, first obtain the stable implementation verdict from
focused evidence, then run broad evidence once at the Work Package, Milestone,
or Final boundary.

Record known baseline failures precisely and require no new failures. Do not
turn a failed check into review evidence or rerun unaffected evidence merely
because another Slice completed.

## Report Precisely

Update status only when a Slice pointer, Work Package, Milestone, exception, or
Goal state changes. Lead reports with the achieved outcome, verification,
preserved compatibility, remaining blockers, worktree state, and exact Slice,
Milestone, and Goal status when relevant.

Before writing an explicit execution handoff, read
[references/handoff.md](references/handoff.md). Do not use execution references
to author or substantially revise a plan.
