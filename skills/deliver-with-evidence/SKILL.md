---
name: deliver-with-evidence
description: Execute explicitly approved multi-step engineering plans with proportional Slice, Milestone, and Final verification, readable text evidence, and whole-goal acceptance. Use automatically when the user asks to implement, continue, finish, or take over an approved architecture migration, broad refactor, multi-work-package plan, or other end-to-end engineering program where local success could be mistaken for whole-goal completion; also use when explicitly invoked as $deliver-with-evidence. If no approved plan exists or a material plan revision is required, stop and hand planning to design-delivery-plan instead of authoring the plan. Do not use for status or metric questions, explanations, ordinary code review, unapproved planning, small fixes, or a single bounded implementation outside an approved program.
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

Select one mode for the current turn. A large surrounding program does not make
every bounded change a Milestone or Final task.

| Mode | Use when | Default evidence |
|---|---|---|
| Slice | Implementing one independently reviewable change within an approved plan | Affected tests, relevant static checks, repository-required smoke, and agent review |
| Milestone | Completing a work package or changing phase status | Slice evidence plus applicable negative, architecture, regression, and hygiene checks |
| Final | Proposing phase or goal `complete` | Complete acceptance conditions, required full and end-to-end checks, and a separate final review pass |

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
- a Milestone is a completed work package or phase;
- the Goal is complete only after every required work package and Final
  acceptance pass.

Never promote Slice or Milestone success to Goal completion.

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
approval, the executor may record the decision in a Goal Change Record and
continue delivery.

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

Before editing, assign a stable local Slice ID and record why it is selected,
the conditions it advances, its local outcome, preserved behavior, expected
scope, and exit evidence. After completion, move it to completed work, clear
the current pointer, and re-evaluate current code and evidence before selecting
another Slice. A predicted next direction is not current work until revalidated.

## Maintain Text Evidence

Prefer the project's existing plan and status documents. Place a committed
checkpoint beside the approved plan with a related name, or use
`docs/delivery.md` when no plan document exists. Use `.codex/delivery.md` only
as a local fallback. Update or commit checkpoints at Slice transitions and
delivery boundaries, not for every command, and omit machine- or
session-specific noise.

Record only what supports continuation and acceptance:

- approved plan and the current Slice contract;
- current `HEAD` and a concise worktree description;
- completed work packages;
- passed commands, what each observed, and which conditions that observation
  supports;
- review conclusions, known failures, and approved exceptions;
- concise Slice pointer changes and the exact resume action.

Record a pointer change only when selecting, completing, blocking, resuming, or
invalidating a Slice. Include the relevant `HEAD` and one short reason. Do not
turn the checkpoint into an activity log or invent transitions that predate
the available evidence.

Map evidence explicitly without imposing a file format:

- every required acceptance condition must be stably identifiable;
- every evidence item must name the condition or conditions it covers;
- one evidence item may cover multiple conditions;
- Milestone and Final acceptance must expose every required condition in scope
  that still lacks evidence.

Evidence claims must not exceed what the performed check can distinguish.
Passing behavior checks does not by itself establish structural ownership,
removal, or maintainability. Exact symbol or path absence does not by itself
establish that a responsibility was removed or replaced. Checkpoints, commit
messages, and acceptance documents may index evidence, but they are not primary
proof of implementation conditions.

Match evidence to the nature of the condition. Behavioral, structural,
replacement, security, performance, compatibility, and hygiene claims may need
different checks or review. When an approved condition claims that an
authority, dependency, fallback, side effect, or implementation is replaced,
verify that the replacement owns the intended responsibility, relevant
consumers use it, and the superseded path has the approved disposition. A
rename, move, or wrapper is not sufficient replacement evidence by itself.

Do not require JSON or duplicate evidence already present in an authoritative
project document. On resume, reuse evidence when the relevant code, tests,
rules, and plan are unchanged. After a clearly unrelated change, retain it by
judgment. When relevance is uncertain, rerun the related check.

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
6. run affected checks and repository-required pre-commit commands once;
7. review scope, architecture, obsolete paths, and maintainability;
8. update only affected plan, status, and text evidence, including the stable
   condition labels, Slice status, and pointer change when applicable;
9. commit when authorized and independently explainable and verifiable.

Do not build compatibility facades, dual tracks, or fallbacks unless the
approved external compatibility boundary requires them.

## Accept A Milestone

Read [references/acceptance-review.md](references/acceptance-review.md)
completely before changing a Work Package, Milestone, or phase to `complete`.

At a work-package or phase boundary, run the applicable layers once for the
current state:

1. smoke or reproduction;
2. targeted success and error paths;
3. negative migration checks;
4. architecture or dependency review;
5. required regression and static checks;
6. delivery and repository hygiene.

Reconstruct the conditions and intentional removals in the current acceptance
scope from the approved plan and current state. Prior Slice, commit, and
checkpoint completion labels are claims to verify, not proof. Challenge each
material completion claim with a plausible incomplete state and inspect whether
it exists.

Update Milestone or phase status only after every required condition in scope
maps to sufficient current evidence. If the review discovers a required
production change, leave Milestone acceptance, return to a Slice, and perform a
new Milestone pass after the change is verified. Keep the whole Goal `partial`
while later required work remains.

## Accept The Final Goal

Read [references/acceptance-review.md](references/acceptance-review.md)
completely before performing Final acceptance.

Before setting a phase or Goal to `complete`, verify:

- every required condition is explicitly mapped to one or more current evidence
  items, with no required label omitted;
- no condition was silently weakened;
- external compatibility promises pass;
- obsolete authorities, dependencies, fallbacks, and temporary migration paths
  are removed or explicitly approved;
- required full, end-to-end, static, architecture, and hygiene checks pass;
- plan, implementation, tests, and documentation agree;
- blocking exceptions are zero or approved.

Perform the final review as a distinct, falsification-oriented acceptance pass
over the whole Goal, not as an assumption inside the last Slice or status edit.
Reconstruct completion from the approved conditions and current state; prior
completion labels are claims to verify, not facts to inherit. For every material
completion claim, identify a plausible counterexample and inspect whether it
exists.

Use an independent reviewer when delegation is available, authorized, and
proportional to the risk. Otherwise perform a clean-room self-review that does
not trust implementation-ledger status. Record the review mode. If Final review
discovers a required production change, leave Final mode, implement and verify
the change, then start a new Final acceptance pass on the resulting state.

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

Update project status only when a work package, Milestone, exception, phase, or
Goal status changes. Do not edit status merely because a command passed.

For a commit, keep one topic and include the problem or feature, solution,
compatibility, verification, and explicit remaining work when applicable.

Lead reports with the achieved outcome. State verification performed,
compatibility preserved, remaining blockers, worktree state, and exact Slice,
Milestone, phase, and Goal status when relevant.

## Load Templates Only When Needed

Read [references/templates.md](references/templates.md) only when validating
plan intake, maintaining a checkpoint, recording an approved Goal change,
writing a handoff, producing an acceptance report, or drafting a structured
commit body. Do not use it to author or substantially revise a plan. Use only
the proportional sections needed for the current task.
