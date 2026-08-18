---
name: design-delivery-plan
description: Design approval-ready, evidence-aware engineering plans for complex multi-step work. Use when the user asks to plan or substantially revise a broad feature, refactor, migration, cleanup, security, reliability, performance, or other engineering program that needs architecture decisions, dependency-ordered work packages, stable acceptance conditions, and a clean handoff to an execution workflow such as deliver-with-evidence. Also use when explicitly invoked in Plan mode for that purpose. Do not use for implementation, status reporting, ordinary code review, small fixes, or a single bounded task.
---

# Design Delivery Plan

Create a plan that another agent can execute without inventing scope or
mistaking local progress for whole-goal completion. Keep the plan adaptable:
fix outcomes and boundaries, not every future file or Slice.

## Respect Authority

Apply system, user, repository, and project instructions before this skill.
Inspect existing plans and decisions before creating replacements. Preserve an
approved plan unless the user asked to revise it or new evidence makes a change
necessary.

## Stay In Planning

Do not implement the plan, edit production code, record delivery evidence as
passed, or approve the plan on the user's behalf. Use read-only inspection to
understand the current system. Write a project plan document only when the user
explicitly requests it and the active mode permits writing; otherwise return
the plan in the conversation.

Mark the result as draft or unapproved. Stop after presenting it for review.

## Require Enough Evidence To Plan

Call a plan approval-ready only when the relevant implementation, existing
decisions, and external contract can be inspected well enough to support its
material architecture and decomposition. If the actual system is unavailable
or critical facts are missing:

- state what could and could not be inspected;
- list the specific discovery needed to close the gaps;
- return an evidence-gap report rather than the full plan template;
- do not assign `G-*`, `WP-*`, or acceptance labels and do not propose an
  implementation Slice;
- include a short conceptual direction only when it helps explain the missing
  decisions, and label it non-binding;
- stop with planning blocked unless the user explicitly asked for an
  assumption-based conceptual plan.

Do not compensate for missing evidence with additional architectural detail.

## Build The Plan

### 1. Establish Current Reality

Inspect the relevant code, entry points, data flow, tests, documents, recent
decisions, and worktree state. Distinguish:

- observed facts;
- reasonable conclusions from those facts;
- assumptions;
- decisions that still require user approval.

Do not turn the user's initial implementation idea into a plan without checking
whether the current system supports a better approach.

Before continuing, decide whether the available evidence is sufficient for the
material decisions the plan would ask the user to approve. Apply the evidence
adequacy rule above when it is not.

### 2. Define The Goal Contract

State:

- the externally observable final outcome;
- required scope and explicit non-goals;
- compatibility, security, performance, operational, and delivery constraints;
- intentional behavior changes and removals;
- the condition under which the whole Goal is complete.

Give every required whole-goal condition a stable unique label such as `G-01`.
Do not use implementation activity as the final outcome.

### 3. Design Only What The Goal Needs

When architecture is material, describe responsibility boundaries, authority,
important data flow, and ownership. Explain which current problems the design
solves and its meaningful costs.

Compare alternatives only when a real decision exists. Do not manufacture a
fixed number of options. Record unresolved decisions instead of hiding them in
implementation details.

### 4. Decompose Outcome-Based Work Packages

Order Work Packages by dependency and independently reviewable outcome. Each
package must have:

- a stable ID such as `WP-01`;
- the problem or capability it owns;
- its outcome, scope, and prohibited expansion;
- dependencies on other packages;
- the intended implementation boundary without a file-by-file script;
- compatibility impact and intentional removals when relevant;
- stable acceptance labels such as `WP-01-01`;
- proportional positive, negative, and review evidence suggestions.

Do not split packages merely by directory, technical layer, team, or file type.
Do not pre-plan every Slice. The execution workflow should select the smallest
Slice from current code and evidence at run time. Make dependencies clear
enough to identify which package outcomes are ready without prescribing their
implementation sequence.

### 5. Design Proportional Acceptance

Recommend machine evidence for externally observable behavior, errors,
rejection, data loss, security boundaries, performance thresholds, and explicit
dependency rules. Recommend agent review for architecture cohesion, naming,
abstraction value, obsolete API removal, directory responsibility, and
maintainability when automation would cost more than it proves.

When replacing an authority, dependency, fallback, side effect, or old path,
state the negative evidence needed to prove that replacement. Do not add
migration sections to unrelated plans. Do not require a separate command or
structured evidence record for every condition.

### 6. Run An Anti-Overdesign Review

Challenge the draft before presenting it:

- Does every abstraction solve a current, evidenced problem?
- Is any framework, extension point, adapter, or compatibility layer justified
  only by a hypothetical future?
- Are one-call wrappers, duplicate authorities, or internal compatibility
  mirrors being retained without an external requirement?
- Are Work Packages expressing outcomes rather than organizational structure?
- Is verification effort proportional to risk?
- Has the plan frozen decisions that should remain Slice-time judgments?
- Can a more local design achieve the same observable result with less lasting
  structure?

Revise the plan when the answer exposes avoidable complexity. Do not weaken a
real external requirement merely to make the implementation smaller.

### 7. Prepare The Handoff

Recommend only the first smallest reviewable Slice, including why it should be
first, the conditions it advances, its local outcome, preserved behavior,
expected scope, and exit evidence. Treat it as a recommendation for the
observed state: the execution workflow must revalidate it and may refine Slice
boundaries without changing approved Work Packages or Goal conditions.

List the architecture decisions, assumptions, and exceptions the user should
review. End with an explicit approval boundary.

## Use The Plan Template

Read [references/plan-template.md](references/plan-template.md) completely when
creating or substantially revising a full plan. Use only sections relevant to
the task; ordinary Markdown is sufficient. The stable labels and semantic
content are the handoff contract, not the exact formatting.

## Handoff Contract

An execution workflow can take over only after user approval. It should be able
to find, without inference:

- the final outcome and compatibility promises;
- Goal and Work Package boundaries;
- every required acceptance label;
- intentional removals and conditional negative evidence;
- unresolved risks, decisions, and approved exceptions;
- the recommended first Slice.

The planner proposes evidence; the executor records actual results. The planner
does not create completion status or claim evidence that has not been run.
