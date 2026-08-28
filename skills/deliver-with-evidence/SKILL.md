---
name: deliver-with-evidence
description: Execute explicitly approved multi-step engineering plans with proportional Slice, Work Package, Milestone, and Final verification, readable evidence, and whole-goal acceptance. Use automatically when the user asks to implement, continue, finish, or take over an approved architecture migration, broad refactor, multi-work-package plan, or other end-to-end engineering program where local success could be mistaken for whole-goal completion; also use when explicitly invoked as $deliver-with-evidence for such an approved multi-step program. If no approved plan exists or a material plan revision is required, stop and hand planning to design-delivery-plan instead of authoring the plan. Do not use for status or metric questions, explanations, ordinary code review, unapproved planning, small fixes, or a single bounded implementation outside an approved program.
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

Use these completion levels:

| Level | Meaning | Completion authority and evidence |
|---|---|---|
| Slice | One cohesive, reviewable implementation result | Focused affected checks and necessary smoke |
| Work Package | Its approved outcome, dependencies, and acceptance labels have sufficient current evidence | Closed locally by the coordinating agent; independent review only when it is also a risk or review boundary |
| Milestone | One stable boundary containing one or more Work Packages | Applicable package evidence plus the broad, structural, compatibility, regression, hygiene, and review evidence required at that boundary |
| Final | The whole approved Goal | Every Goal and Work Package condition, required broad evidence, and a distinct whole-Goal acceptance pass |

Choose the smallest level that matches the current claim. Package numbering and
completion order do not define Milestones. Slice, Work Package, or Milestone
success never implies Goal completion. Reserve expensive full-suite,
end-to-end, and exhaustive compatibility checks for the stable boundary that
needs them unless the approved plan, repository rules, or immediate risk
requires them earlier.

## Preserve Coordination Authority

The coordinating agent alone interprets the approved plan, selects the current
Slice, writes Delivery, changes formal status, approves exceptions, accepts
evidence, and declares Work Package, Milestone, or Goal completion.

When delegation is available, authorized, and proportional:

- use bounded read-only discovery only when a specific uncertainty must be
  resolved before selecting or contracting the Slice;
- delegate one approved Slice contract to one production-writing capability,
  leaving its bounded local discovery, implementation, and focused verification
  inside that Slice;
- use independent read-only review at qualifying implementation-risk boundaries
  and whole-Goal acceptance;
- provide a self-contained packet with workspace, stable repository states,
  approved conditions, exact scope and exclusions, preserved behavior, required
  evidence, and readable raw-evidence locations;
- request findings without suggesting a desired verdict.

Delegated work returns the local outcome, acceptance labels, changed
authorities, reproducible verification, stable snapshot, boundary signals,
blockers, and residual risks. It must not expand the Slice, change the plan,
choose later work, edit Delivery, create commits, or mark a formal boundary
complete. Keep only one production writer active. Parallelize only independent
work that cannot invalidate a pending result.

On receipt, check that the result matches the Slice contract, every reported
repository snapshot is still current, its evidence supports the claimed
outcome, and no blocker, conflict, or scope expansion remains. Reuse accepted
evidence without repeating the same exploration, focused checks, or ordinary
implementation review. Gather more evidence only when state changed, evidence
is missing or contradictory, work exceeded its contract, or acceptance needs a
different evidence class.

Treat read-only work as independent only when its effective sandbox is
read-only. Otherwise use a separate read-only turn or the clean-room fallback
in the acceptance reference and disclose the limitation. When delegation is
unavailable, perform the bounded work sequentially without dropping required
review.

## Maintain The Delivery Document

Every plan executed through this skill requires a private persistent Delivery
document before the first production edit. Read
[references/delivery-document.md](references/delivery-document.md) completely
before initializing or resuming it, and follow that reference for path
selection, permissions, repository-state records, evidence, commit checkpoints,
and updates.

Use an explicitly approved path when provided; otherwise use the private
`$CODEX_HOME/state/delivery/` hierarchy, with `CODEX_HOME` defaulting to
`~/.codex`. If the required external path is not writable, request exact access
or an approved alternate path and stop before production edits. Plan approval
does not authorize sandbox escalation or a repository-local substitute.

The coordinating agent is the sole writer. Integrate delegated results
serially and replace the document atomically. Keep one active coordinator for a
Goal; if concurrent coordination or conflicting Delivery state is detected,
stop and reconcile the contract, implementation, repository states, evidence,
and next action before writing.

Record the approved contract and current repository states before selecting the
first Slice. Update Delivery when selecting, completing, blocking, resuming, or
invalidating a Slice; when repository state or a commit checkpoint changes; and
at Work Package, Milestone, or Final acceptance. Record acceptance-linked
evidence and the exact next action, not a command transcript. Retain the
document after completion unless an approved retention rule says otherwise.

## Handle Plan Changes

Refine local file scope, Slice boundaries, order among dependency-ready work,
and focused verification when the approved Goal, Work Package outcomes,
compatibility promises, removals, permissions, and exceptions remain unchanged.

When evidence requires a material contract change:

1. stop before implementing the changed target;
2. record the conflicting evidence and approved condition;
3. hand substantial revision to `$design-delivery-plan`;
4. resume only after explicit user approval.

Before implementing an approved revision, read
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
pre-plan every later Slice or create separate Slices for implementation-internal
file steps.

Assign the next Slice ID under its owning Work Package using `<WP-ID>-S<NN>`,
for example `WP-01-S01`, `WP-01-S02`, and `WP-02-S01`. Number independently
within each Work Package and pad the Slice number to at least two digits.
Allocate an ID only when selecting the Slice; never rename, renumber, or reuse a
recorded ID. Keep titles and correction relationships outside the ID.

Record why the Slice is current, the acceptance labels it advances, one local
outcome, preserved behavior, expected authority or implementation scope, and
focused exit evidence. Revalidate current state before selecting another Slice.

## Execute A Slice

For the selected Slice:

1. inspect the relevant authority boundary and every affected worktree;
2. implement the smallest reviewable result;
3. remove superseded implementation when the approved compatibility boundary
   does not retain it;
4. add positive evidence that the new path works and proportional negative
   evidence for required replacement or removal;
5. run focused affected tests, relevant static checks, and necessary smoke;
6. resolve required focused-check failures and return a stable implementation;
7. decide whether the result completes a Work Package or makes an acceptance or
   risk boundary review-ready;
8. apply the commit-boundary procedure, then atomically record Slice completion,
   repository states, accepted evidence, and the next action in Delivery.

Keep broad evidence deferred until the stable boundary that owns it. A
production correction returns through a corrective Slice before acceptance
resumes.

## Preserve Stable Commit Boundaries

A commit checkpoint groups one or more completed Slices into a coherent,
independently understandable, and recoverable change. It is not an acceptance
level, review boundary, or separately identified planning object. Commit timing
is independent from reviewer timing.

After accepting Slice evidence, create a checkpoint when the completed work is
focused-verified, contains no half-migration or internally inconsistent state,
and one of these applies:

- adjacent completed Slices form one useful behavior or authority outcome;
- the next production work changes repository, authority, risk, or ownership;
- continuing would materially complicate attribution, review, or rollback;
- interruption or handoff should preserve the stable implementation.

Continue without committing when the next Slice directly completes the same
unfinished outcome. Do not commit failed, incomplete, or inconsistent state.

Create local commits automatically only when current user instructions,
repository instructions, or an approved workflow explicitly authorize commit
creation. Approval to implement a plan alone does not authorize changing Git
history. If authorization is absent, record the coherent state as
`commit-ready`, preserve its intended scope, and request authorization before
committing.

When authorized, use an available commit workflow for scope isolation, staging,
commit shape, message style, and reporting. Otherwise use native Git with the
same minimum contract: include only the stable checkpoint, preserve unrelated
changes, follow repository conventions, inspect the staged diff, and report the
hash and remaining worktree state. Do not push, create branches, amend, or
rewrite history as part of checkpoint creation.

For multi-repository work, commit each repository's coherent portion
independently. A logical checkpoint is stable only after all intended repository
commits succeed. If only some succeed, atomically record the exact partial
repository state and blocker in Delivery, do not claim the checkpoint complete,
and stop before dependent production work.

After the commit decision -- commit, `commit-ready`, or coherent continuation
without a commit -- update Delivery once with the completed Slice, current
repository states, commit state, accepted evidence, and next action. Reuse
accepted verification; a commit does not require another acceptance pass.

## Review Stable Risk Boundaries

A risk review boundary is review-ready when its owned conditions are
implemented, dependencies are stable, focused evidence names fixed repository
snapshots, and no active writer is changing the same authority.

Use independent implementation review before Final only when:

- later production semantically depends on the boundary's authority, behavior,
  or evidence, so late correction would invalidate or materially rework it; or
- an approved security, permission, data-integrity, or migration boundary has a
  high-impact failure mode whose first discovery at Final would materially
  enlarge correction or rollback scope.

Execution order alone is not dependency. When later work does not rely on the
boundary, record it as implemented and locally verified and defer independent
challenge to Final. One boundary may contain one or more Work Packages sharing
authority, risk, and acceptance scope. Independent stable boundaries may be
reviewed in parallel when neither can invalidate the other's snapshot.

At a qualifying pre-Final risk boundary, obtain the stable implementation
verdict before running boundary-wide broad evidence unless the approved plan,
repository rules, or immediate risk requires that evidence in the review
packet. After a no-blocker verdict, run the boundary's required broad evidence
once. Defer an unchanged program-wide suite to the nearest shared Milestone
when no downstream decision needs its intermediate result.

## Accept Work Packages, Milestones, And Final

Read [references/acceptance-review.md](references/acceptance-review.md)
completely before marking a Work Package, Milestone, or Goal complete. That
reference is canonical for acceptance scope, evidence classes, counterexamples,
blocking thresholds, independent review, and correction.

Close a Work Package locally when its approved acceptance labels and
dependencies have sufficient current evidence. It does not require a
Milestone-style or independent review unless it is part of a qualifying risk or
review boundary.

Accept a Milestone against one stable boundary containing one or more Work
Packages, their applicable conditions, and stable dependencies. Keep the Goal
partial while later required work remains.

For Final:

1. establish the stable final implementation across every repository;
2. run the required whole-Goal broad and hygiene evidence once on that state;
3. give the reviewer the complete approved contract, repository snapshots, raw
   evidence, and material limitations without a desired verdict;
4. if a blocker requires production change, leave Final and use a corrective
   Slice;
5. rerun only evidence invalidated by the correction, then perform a new
   complete Final pass on the corrected stable state.

Delivery status and commit records locate evidence but do not prove completion.
When independent review is unavailable or cannot be guaranteed read-only, use
the acceptance reference's clean-room fallback and disclose the limitation.

## Report Precisely

Update formal status only when a Slice pointer, Work Package, Milestone,
exception, repository checkpoint, or Goal state changes. Lead reports with the
achieved outcome, verification, preserved compatibility, remaining blockers,
repository and worktree state, and exact Slice, Milestone, and Goal status when
relevant.

Before writing an explicit execution handoff, read
[references/handoff.md](references/handoff.md). Do not use execution references
to author or substantially revise a plan.
