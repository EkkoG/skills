# Delivery Plan Template

Use this as a flexible checklist, not a required schema. Omit sections that do
not apply and add domain-specific detail when it changes the decision.

## Status

Draft and unapproved.

Do not use this full template when material current-state evidence is
unavailable. Return a blocked evidence-gap report without formal Goal, Work
Package, acceptance, or Slice labels instead.

## Objective

Describe the externally observable final outcome and the whole-goal completion
boundary.

## Scope And Constraints

- Required scope
- Explicit non-goals
- Compatibility promises
- Security, performance, operational, or delivery constraints
- Intentional behavior changes

## Current State

Summarize observed architecture, authority, data flow, tests, documentation,
known problems, and reusable parts. Separate facts, conclusions, and assumptions.

## Decisions And Target Design

Explain the selected responsibilities, ownership, important data flow, problems
solved, tradeoffs, rejected alternatives when material, and unresolved choices.

## Work Packages

For each dependency-ordered package:

### WP-01: Outcome

- Problem or capability
- Owned scope
- Prohibited scope
- Dependencies
- Implementation boundary
- Compatibility impact
- Intentional removals, if any
- Acceptance conditions: `WP-01-01`, `WP-01-02`, ...
- Suggested positive, negative, and review evidence
- Remaining decisions or risks

Repeat only for packages required by the Goal.

## Goal Acceptance

| ID | Required condition | Suggested evidence | Status |
|---|---|---|---|
| G-01 | Observable whole-goal condition | Test, inspection, review, or artifact | planned |

Keep Work Package completion, phase or milestone completion, and whole-goal
completion distinct.

## Acceptance Strategy

Describe proportional smoke, targeted, regression, static, security,
performance, architecture, negative migration, and hygiene checks as applicable.
Allow review where automation would cost more than it proves.

## Risks, Assumptions, And Decisions

List known risks, current assumptions, user decisions still required, approved
exceptions, and the conditions that would require revising the plan.

## Anti-Overdesign Review

Record conclusions about current necessity, abstraction value, internal
compatibility, hypothetical extension points, duplicate authority, and whether
any design can be made more local without weakening the Goal.

## Recommended First Slice

State the smallest reviewable local outcome, preserved behavior, expected scope,
and suggested verification. Do not predefine every later Slice.

## Review And Approval

Highlight the decisions the user should review. State that implementation must
not begin until the plan is explicitly approved.
