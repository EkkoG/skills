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

## Maintain Text Evidence

Prefer the project's existing plan and status documents. If they do not provide
a suitable checkpoint, use an uncommitted `.codex/delivery-v2.md`.

Record only what supports continuation and acceptance:

- approved plan and current Slice;
- current `HEAD` and a concise worktree description;
- completed work packages;
- passed commands and what each proves;
- review conclusions, known failures, and approved exceptions;
- exact remaining work or next action.

Map evidence explicitly without imposing a file format:

- every required acceptance condition must be stably identifiable;
- every evidence item must name the condition or conditions it covers;
- one evidence item may cover multiple conditions;
- Final acceptance must expose every required condition still lacking evidence.

Do not require JSON or duplicate evidence already present in an authoritative
project document. On resume, reuse evidence when the relevant code, tests,
rules, and plan are unchanged. After a clearly unrelated change, retain it by
judgment. When relevance is uncertain, rerun the related check.

## Execute A Slice

Before editing, state the local outcome, preserved external behavior, expected
scope, and acceptance evidence. Then:

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
   condition labels covered by new evidence;
9. commit when authorized and independently explainable and verifiable.

Do not build compatibility facades, dual tracks, or fallbacks unless the
approved external compatibility boundary requires them.

## Accept A Milestone

At a work-package or phase boundary, run the applicable layers once for the
current state:

1. smoke or reproduction;
2. targeted success and error paths;
3. negative migration checks;
4. architecture or dependency review;
5. required regression and static checks;
6. delivery and repository hygiene.

Update Milestone or phase status only after every required condition in that
scope maps to current evidence. Keep the whole Goal `partial` while later
required work remains.

## Accept The Final Goal

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

Perform the final review as a distinct acceptance pass over the whole Goal, not
as an assumption inside the last Slice or status edit. The reviewer may be the
coordinating agent unless higher-level instructions require independence.

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
