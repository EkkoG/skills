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

- use bounded read-only discovery only to close a specific uncertainty;
- delegate one approved Slice contract to one production-writing capability;
- use independent read-only review for risky implementation boundaries and
  whole-Goal acceptance;
- provide a self-contained packet with workspace, stable state, approved
  conditions, exact scope and exclusions, preserved behavior, required
  evidence, and raw-evidence locations;
- require focused affected checks by default; reserve full-suite, end-to-end,
  and exhaustive compatibility evidence for the coordinating agent at the
  stable boundary described below;
- request findings without suggesting the desired verdict.

Delegated work returns changes, evidence, findings, and blockers. It must not
expand the Slice, change the plan, choose later work, edit the Delivery
document, or mark any boundary complete. Keep only one production writer
active. Parallelize only independent work that cannot invalidate the pending
result.

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
pre-plan every later Slice.

Before editing, assign a stable local Slice ID and record:

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

End with a verified worktree and recorded Delivery state. Commit creation is a
separate workflow. Add compatibility facades, dual tracks, or fallbacks only
when the approved external boundary requires them.

## Review Stable Risk Boundaries

A risk review boundary is review-ready when its owned acceptance conditions are
implemented, relevant dependencies are stable, focused evidence names one fixed
snapshot, and no active production writer is changing the same authority.

Use one independent implementation review when a review-ready boundary covers
public API, configuration or schema, external compatibility, security or
permissions, migration, concurrency, data integrity, or another approved
high-risk authority, and before later production work depends on its verdict.
If no later work depends on it, it may remain for Final unless current
instructions or the approved plan require earlier review.

The boundary may contain one Work Package or several that share the same
authority, risk, and acceptance scope. Package numbering and completion order
do not control review timing. Genuinely independent review-ready boundaries may
be reviewed in parallel when neither can invalidate the other's snapshot.

After a no-blocker verdict, run the boundary's deferred broad evidence once on
the reviewed state. If later work changes a reviewed authority, invalidate only
the affected conditions and evidence. Revalidate them at the next relevant
stable boundary or Final; retain unaffected evidence and package status.

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
