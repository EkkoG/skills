---
name: design-delivery-plan
description: Design approval-ready, evidence-aware engineering plans for complex multi-step work. Use when the user asks to plan or substantially revise a broad feature, refactor, migration, cleanup, security, reliability, performance, or other engineering program that needs architecture decisions, dependency-ordered work packages, stable acceptance conditions, and a clean handoff to an execution workflow such as deliver-with-evidence. Also use when explicitly invoked in Plan mode for that purpose. Do not use for implementation, status reporting, ordinary code review, small fixes, or a single bounded task.
---

# Design Delivery Plan

Create a plan that another agent can execute without inventing scope or
mistaking local progress for whole-goal completion. Fix outcomes, boundaries,
and acceptance conditions while leaving Slice-time implementation choices open.

## Work From Current Authority

Apply system, user, repository, and project instructions before this skill.
Inspect existing plans and decisions before drafting or revising a plan.

Maintain the plan as a self-contained statement of the user's latest decisions.
Keep only alternatives that still require a decision. Put decision history only
in artifacts whose purpose is historical record, such as an ADR, changelog,
retrospective, or delivery record. Before presenting a revision, check that a
first-time reader can understand every current outcome and constraint without
the earlier discussion.

Stay in planning. Use read-only inspection, do not edit production code or
record unperformed evidence, and do not approve the plan for the user. Write a
project plan file only when the user explicitly requests it and writing is
authorized. Present the result as draft and stop at the approval boundary.

## Require Enough Evidence

Call a plan approval-ready only when the relevant implementation, existing
decisions, tests, and external contract can be inspected well enough to support
its material architecture and decomposition.

When critical facts are unavailable, return an evidence-gap report instead of
a formal plan. State what was inspected, what remains unknown, and the bounded
discovery needed. Do not assign Goal, Work Package, acceptance, or Slice labels
until the evidence supports those contracts. A conceptual direction may be
included when useful, but label it non-binding. More design detail does not
compensate for missing evidence.

## Build The Plan

### Establish Current Reality

Inspect the relevant entry points, authority boundaries, data flow, tests,
documents, recent decisions, and worktree state. Separate observed facts,
supported conclusions, assumptions, and decisions that still need approval.
Check whether the user's initial implementation idea fits the current system
before turning it into the target design.

### Define The Goal Contract

State the externally observable final outcome, required scope, stable scope
exclusions, intentional behavior changes, and the condition under which the
whole Goal is complete. Include applicable compatibility, security,
performance, operational, permission, and delivery constraints.

Give every required whole-goal condition a stable label such as `G-01`.
Describe outcomes rather than implementation activity.

### Design Only What The Goal Needs

Describe material responsibility boundaries, authority, ownership, and data
flow. Explain the current problem each lasting abstraction solves and its
meaningful cost. Compare alternatives only when a real unresolved decision
exists; otherwise describe the selected target directly.

### Decompose Outcome-Based Work Packages

Express Work Package dependencies as a directed acyclic graph of independently
reviewable outcomes. Stable IDs identify packages; numbering does not prescribe
execution or completion order. Each package needs:

- a stable ID such as `WP-01` and one owned outcome;
- included scope, prohibited expansion, and dependencies;
- the intended authority or implementation boundary;
- any stable risk review boundary it shares with other packages, plus the later
  work that must wait for that verdict;
- applicable compatibility impact and intentional removals;
- stable acceptance labels such as `WP-01-01`;
- proportional evidence suggestions, risks, and unresolved decisions.

Do not split packages by directory, layer, file type, tests, or documentation
when those pieces complete one outcome and share an acceptance boundary. Split
only for a material dependency, risk, rollback, ownership, or acceptance
difference.

A risk review boundary may contain one package or several packages that share
the same authority, risk, and acceptance scope. Define the boundary by those
facts rather than package numbering or expected completion order. Add one only
when an independent implementation verdict will protect later work; do not
assign a reviewer to every package by default.

Do not pre-plan every Slice. The execution workflow selects the smallest
reviewable Slice from current code and evidence. The plan only needs enough
dependency and boundary information to make that choice safely.

### Design Proportional Acceptance

Use machine evidence for observable behavior, errors, rejection, data loss,
security boundaries, performance thresholds, and enforceable dependency rules.
Use review for architecture, ownership, obsolete path removal, abstraction
value, and maintainability when automation would cost more than it proves.

When replacing an authority, dependency, fallback, side effect, or old path,
state the positive evidence for the replacement and the negative evidence for
the approved disposition of the old path. For structural guards, describe only
the representative escape classes and false-positive boundary needed to test
the approved claim; do not design a general analyzer in the plan.

## Simplify And Challenge The Draft

Before presentation, remove avoidable structure:

- abstractions without a current evidenced problem;
- hypothetical extension points or internal compatibility layers;
- duplicate authorities, one-call wrappers, and unnecessary adapters;
- Work Packages that only mirror repository organization;
- separate orchestration for implementation, tests, guards, or documentation
  that share one outcome;
- repeated review or verification that does not increase acceptance confidence.

Keep real external requirements even when they make the implementation larger.

For a broad or high-risk plan, use one independent read-only review when
delegation is available, authorized, and proportional. Give the reviewer the
user goal, raw constraints, current-state evidence, and draft plan without a
desired verdict. Ask for missing scope, unsupported assumptions, dependency
errors, unverifiable acceptance, compatibility gaps, and avoidable design.

Separate approval blockers from optional simplification advice. Re-review only
when resolving a blocker materially changes the Goal contract, architecture,
dependency order, compatibility, permissions, or acceptance strength, and then
scope the pass to that changed boundary and direct regressions. When independent
review is unavailable, perform the same challenge as a clean-room pass and
disclose the limitation when it matters. Treat a review as independent only
when its effective boundary is read-only.

## Prepare Approval And Handoff

Read [references/plan-template.md](references/plan-template.md) completely when
creating or substantially revising a full plan. Use only sections relevant to
the work; stable labels and semantic content are the contract, not exact
formatting.

Recommend the first smallest reviewable Slice with its reason, conditions,
local outcome, preserved behavior, expected scope, and exit evidence. Present
it as a recommendation that execution must revalidate, not a frozen script.

Highlight material decisions, assumptions, exceptions, and risks for the user.
End with an explicit approval boundary. The handoff must let an execution
workflow find without inference:

- the final outcome and compatibility promises;
- Goal and Work Package boundaries and dependencies;
- every required acceptance label;
- intentional removals and required negative evidence;
- unresolved decisions, risks, and approved exceptions;
- the recommended first Slice.

After approval, the execution workflow initializes its persistent delivery
document before the first production edit. Planning proposes evidence; execution
records actual results.
