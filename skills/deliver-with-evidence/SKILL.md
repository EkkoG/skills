---
name: deliver-with-evidence
description: Execute explicitly approved multi-step engineering plans with proportional Slice, Milestone, and Final verification, readable text evidence, and whole-goal acceptance. Use automatically when the user asks to implement, continue, finish, or take over an approved architecture migration, broad refactor, multi-work-package plan, or other end-to-end engineering program where local success could be mistaken for whole-goal completion; also use when explicitly invoked as $deliver-with-evidence for such an approved multi-step program. If no approved plan exists or a material plan revision is required, stop and hand planning to design-delivery-plan instead of authoring the plan. Do not use for status or metric questions, explanations, ordinary code review, unapproved planning, small fixes, or a single bounded implementation outside an approved program.
---

# Deliver With Evidence

Use repository instructions as the project contract. Execute the smallest
reviewable unit, preserve evidence in readable text, and keep local progress
separate from whole-goal completion.

## Respect Authority

Apply instructions in this order:

1. system, developer, and user instructions;
2. the closest applicable `AGENTS.md` files;
3. project documents referenced by those instructions;
4. this skill's defaults.

Use natural-language project rules. Do not require an adapter, schema, test
graph, or machine-verifiable acceptance for every condition.

## Choose The Smallest Mode

Operate in one mode at a time and select the smallest mode for the current
work. A large surrounding program does not make every bounded change a
Milestone or Final task.

A turn may transition to another mode only after the current mode finishes, its
delivery boundary is recorded, and the next acceptance scope is reconstructed.
Do not blend implementation evidence with Milestone or Final acceptance. If an
acceptance pass discovers a required production change, leave acceptance,
select a corrective Slice, and start a fresh acceptance pass after that Slice
is verified.

| Mode | Use when | Default evidence |
|---|---|---|
| Slice | Implementing one independently reviewable change within an approved plan | Affected tests, relevant static checks, repository-required smoke, and agent review |
| Milestone | Completing a Work Package | Slice evidence plus applicable negative, architecture, regression, and hygiene checks |
| Final | Proposing the whole Goal `complete` | Complete acceptance conditions, required full and end-to-end checks, and a separate final review pass |

Do not run Milestone or Final acceptance merely to answer a question or finish
one small Slice.

## Start From An Approved Plan

Before implementation, confirm that the user has seen and approved a plan that
states:

- the observable final outcome;
- scope, boundaries, and explicit non-goals;
- reviewable work packages in dependency order;
- acceptance conditions for work packages and the whole goal, with a stable ID
  or unique label for every required condition.

When relevant, also require external compatibility promises, target
architecture, intentional removals, negative migration evidence, and approved
exceptions. Do not force migration-specific sections onto unrelated work.

If no approved plan exists or required contract elements are missing, do not
create or substantially revise it. Report the exact planning gaps, direct the
task to `$design-delivery-plan`, and stop before changing production code.
Reuse a sufficient approved plan instead of rebuilding it.

Treat completion at three levels:

- a Slice is one independently reviewable change;
- a Milestone is an accepted Work Package boundary;
- the Goal is complete only after every required work package and Final
  acceptance pass.

Never promote Slice or Milestone success to Goal completion.

## Delegate Proportionally And Preserve Authority

The coordinating agent remains the sole owner of approved-plan interpretation,
current Slice selection, delivery-document writes, status changes, and any
claim that a Work Package or Goal is complete.

When delegation is available, authorized, and proportional:

- delegate bounded read-only discovery that reduces a specific uncertainty;
- delegate at most one approved Slice contract to an implementation capability;
- use an independent read-only review for risky implementation boundaries or
  whole-Goal acceptance;
- give delegated work the approved contract, current state, exact scope, and
  required evidence, without suggesting a desired review verdict.

Delegated work must not expand the Slice, change a Goal or Work Package,
approve an exception, select later work, update the delivery document, or mark
any delivery level complete. It returns changes, evidence, findings, and
blockers to the coordinating agent. If current code requires a material plan
decision, stop that work instead of guessing.

When delegation is unavailable, perform the same bounded work sequentially.
Use a clean-room review where independence would otherwise be useful, and
disclose the lack of independent review when it affects an acceptance claim.

Before treating delegated exploration or review as read-only, confirm that the
child's effective sandbox is read-only. A configured default is insufficient
when a live parent permission override can supersede it. If the effective child
boundary cannot be guaranteed, run the work from a separate read-only turn or
session; otherwise use the clean-room fallback and disclose that the review was
not independently sandboxed. Never silently substitute a no-edit prompt for an
enforced read-only boundary.

## Handle Plan Changes

Refine Slice boundaries, file scope, order, and local verification during
execution when doing so does not change an approved Goal condition, Work
Package outcome, compatibility promise, intentional removal, or exception.

When current evidence requires a material plan change:

1. stop before implementing against the changed target;
2. record the evidence and exact approved condition it conflicts with;
3. hand substantial planning or revision to `$design-delivery-plan`;
4. resume only after the user explicitly approves the revised plan.

Do not design the replacement target or approve it on the user's behalf. After
approval and before implementing the revised target, update the Delivery
document's Current approval and Approved Contract so they state the complete
current target in positive, self-contained language, update any affected status
and resume fields, and append a Goal Change Record for history. Perform those
changes as one serialized atomic document update. Keep Initial approval stable.
Resume from the current contract; do not require later readers to merge
historical records to discover what is currently approved.

## Select The Current Slice

On start or resume, continue the recorded unfinished Slice when its plan,
boundaries, and dependencies remain valid. Do not replace valid in-progress
work merely because another task looks easier.

When no valid Slice is active, choose from dependency-ready Work Packages,
unmet acceptance conditions, blockers, incomplete authority replacements, and
required removals. Reject candidates that need a material plan change or lack
one independently reviewable outcome and clear exit evidence. Prefer work that
removes a blocker or half-migrated state, then work that advances the earliest
ready package; break ties with smaller scope and earlier risk reduction. Do not
pre-plan every later Slice or use a mechanical score.

Before editing, assign a stable local Slice ID and write its selection reason,
conditions, local outcome, preserved behavior, expected scope, and exit
evidence to the delivery document. After completion, move it to completed work,
clear the current pointer, and re-evaluate current code and evidence before
selecting another Slice. A predicted next direction is not current work until
revalidated.

## Maintain The Delivery Document

Read [references/delivery-document.md](references/delivery-document.md)
completely before initializing or maintaining the Delivery document.

Every approved multi-step plan executed through this skill requires a private,
persistent delivery document. Initialize it before the first production edit.
Expected same-session completion, single-agent execution, or low interruption
risk does not waive this requirement. Small tasks outside this skill do not
create a delivery document.

Resolve the path in this order:

1. use a path explicitly required by the user, approved plan, or repository
   instructions;
2. for the default root, discover and resume an existing document for the same
   approved Goal when one exists;
3. only when no matching document exists, create
   `$CODEX_HOME/state/delivery/<repo-key>/<goal-id>/delivery.md`, where
   `CODEX_HOME` defaults to `~/.codex`.

For the default path:

- form `<repo-key>` from a safe repository or workspace basename plus the first
  10 lowercase hexadecimal characters of SHA-256 over the UTF-8 resolved
  absolute root path, so every agent derives the same key and same-named roots
  remain distinct;
- before generating a Goal ID, enumerate
  `$CODEX_HOME/state/delivery/<repo-key>/*/delivery.md`. Resume only when exactly
  one document's recorded workspace, Goal title, plan source, and initial
  approval boundary identify the same work. If multiple documents match, stop
  and reconcile them instead of guessing. If none match, create a new document;
- form `<goal-id>` from a readable Goal-title slug plus a short random suffix
  such as 12 UUID hex characters. Generate it once, record it, and never
  recompute it from plan text. Existing delivery documents keep their current
  IDs and paths;
- keep the delivery root outside the target repository. Compare the resolved
  repository and configured delivery roots before initialization; if the
  delivery root is inside the repository, require an approved external path.
  Use a repository-local path only when the user, approved plan, or repository
  rules explicitly require it;
- create user-private directories and files where supported, normally `0700`
  for directories and `0600` for the document.

If an explicitly selected candidate document already exists, resume it only
when its recorded workspace, Goal, plan source, and initial approval boundary
identify the same work. Otherwise do not overwrite it; reconcile the conflict
or obtain an approved alternate path.

The Markdown document is the sole delivery record. Private delivery state is
part of local orchestration and may record approved local role or model
decisions when they are needed to resume; reusable skills remain free of those
bindings.

The coordinating agent is the only authorized writer. Delegated discovery,
implementation, and review return evidence or findings for serialized
integration and never edit the document. Write through a private temporary
file in the same directory and replace the document atomically. When another
coordinating session may update the same document, acquire a cooperative
sibling lock before reading and writing; if the lock exists, stop and reconcile
instead of overwriting.

At initialization, record only what is needed to resume and accept the Goal:

- workspace, repository key, Goal title and ID, exact delivery path, plan
  source, initial and current approval boundaries, current `HEAD` or non-Git
  baseline, and concise worktree state;
- the approved final outcome, scope, boundaries, non-goals, Work Package order
  and full Work Package contracts, every stable acceptance label, and material
  compatibility promises, removals, decisions, risks, and exceptions;
- Work Package and Goal status, the current Slice contract, evidence already
  established, missing evidence, and the exact resume action.

When the plan has a durable source, point to it and copy only the parts needed
for safe resumption. When it exists only in conversation, embed the minimum
approved contract in readable Markdown without copying unnecessary design
prose.

Update the document when selecting, completing, blocking, resuming, or
invalidating a Slice, and at Milestone or Final acceptance boundaries. Record
only evidence that supports an acceptance condition, concise status changes,
known failures or exceptions, and the next exact action. Do not turn it into a
command transcript. Retain it after Goal completion unless another approved
retention rule applies.

Map evidence explicitly without imposing a file format:

- every required acceptance condition must be stably identifiable;
- every evidence item must name the condition or conditions it covers;
- one evidence item may cover multiple conditions;
- Milestone and Final acceptance must expose every required condition in scope
  that still lacks evidence.

Evidence claims must not exceed what the performed check can distinguish.
Passing behavior checks does not by itself establish structural ownership,
removal, or maintainability. Exact symbol or path absence does not by itself
establish that a responsibility was removed or replaced. Delivery documents,
commit messages, and acceptance reports may index evidence, but they are not
primary proof of implementation conditions.

Match evidence to the nature of the condition. Behavioral, structural,
replacement, security, performance, compatibility, and hygiene claims may need
different checks or review. When an approved condition claims that an
authority, dependency, fallback, side effect, or implementation is replaced,
verify that the replacement owns the intended responsibility, relevant
consumers use it, and the superseded path has the approved disposition. A
rename, move, or wrapper is not sufficient replacement evidence by itself.

Reuse authoritative project evidence instead of duplicating it in another
format. On resume, reuse evidence when the relevant code, tests, rules, and
plan are unchanged. After a clearly unrelated change, retain it by judgment.
When relevance is uncertain, rerun the related check.

## Execute A Slice

After selecting or resuming the current Slice:

1. inspect the relevant authority boundary and current worktree;
2. implement the smallest independently reviewable result;
3. remove superseded implementation when internal compatibility is not part of
   the approved boundary;
4. add positive evidence that the new path works;
5. when replacing an authority, dependency, fallback, or side effect, add
   negative evidence that the old path is absent, isolated, or no longer
   authoritative;
6. run affected checks and repository-required verification commands once;
7. review scope, architecture, obsolete paths, and maintainability;
8. update the delivery document and only affected project status, including the
   stable condition labels, Slice status, and pointer change when applicable.

End Slice execution with a verified worktree and recorded Delivery state.
Commit creation belongs to a separate workflow with its own trigger rules.

Do not build compatibility facades, dual tracks, or fallbacks unless the
approved external compatibility boundary requires them.

## Accept A Milestone

Read [references/acceptance-review.md](references/acceptance-review.md)
completely before changing a Work Package or Milestone boundary to `complete`.

Apply that procedure to the current Work Package scope and its applicable
evidence classes. Update Work Package status only when every required condition
has sufficient current evidence and no unapproved blocker remains. If review
finds a required production change, leave Milestone acceptance, return to a
Slice, and start a new Milestone pass after verification. Keep the whole Goal
`partial` while later required work remains.

## Accept The Final Goal

Read [references/acceptance-review.md](references/acceptance-review.md)
completely before performing Final acceptance.

Apply that procedure to every Goal and Work Package condition. Goal completion
requires current evidence for every label, unchanged acceptance strength,
fulfilled compatibility and removal obligations, applicable full and
end-to-end checks, agreement among plan, implementation, tests, and docs, and
zero unapproved blockers.

Perform Final as a distinct acceptance pass. Use an independent reviewer when
delegation is available, authorized, and proportional; otherwise use the
documented clean-room fallback. Delivery status fields remain claims, not
proof. If Final finds a required production change, leave Final mode, implement
and verify a corrective Slice, then start a new Final pass.

A Final pass may also close still-pending Work Package statuses when its
whole-Goal scope verifies every condition for those packages. Do not require a
separate, duplicative Milestone pass unless the approved plan or repository
rules require one.

## Judge Evidence Proportionally

Use machine evidence for externally observable behavior such as CLI, config,
templates, output, errors, rejection, and data loss. Use agent review for
architecture, directory responsibility, naming, obsolete API removal, and
maintainability when machine enforcement would cost more than it proves.

Review cannot override a failed required check. Do not repeat a targeted check
already covered by a broader check on the same state.

Record known baseline failures precisely and require no new failures. Do not
silently convert a failing gate into review evidence.

## Update And Report Precisely

Update delivery or project status only when a Slice pointer, Work Package,
Milestone, exception, or Goal status changes. Do not edit status merely
because a command passed.

Lead reports with the achieved outcome. State verification performed,
compatibility preserved, remaining blockers, worktree state, and exact Slice,
Milestone, and Goal status when relevant.

## Load Additional References Only When Needed

- Before recording an approved Goal change, read
  [references/goal-change-record.md](references/goal-change-record.md).
- Before writing a handoff, read [references/handoff.md](references/handoff.md).

Do not use these references to author or substantially revise a plan.
