# Delivery Plan Template

Use this as a flexible checklist, not a required schema. Omit sections that do
not apply. When material current-state evidence is unavailable, return an
evidence-gap report instead of this template.

## Status

Draft and unapproved.

## Objective

Describe the externally observable final outcome and whole-goal completion
boundary.

## Scope And Constraints

- Required scope and stable exclusions
- Compatibility promises and intentional behavior changes
- Security, permission, performance, operational, or delivery constraints

## Current State

Summarize observed architecture, authority, data flow, tests, documentation,
known problems, and reusable parts. Separate facts, conclusions, and assumptions.

## Decisions And Target Design

Describe current responsibilities, ownership, important data flow, problems
solved, material costs, and unresolved choices. Keep the target self-contained
and compare only alternatives that still require a decision.

## Work Packages

For each dependency-ordered package:

### WP-01: Outcome

- Owned outcome and scope
- Prohibited expansion
- Dependencies
- Implementation or authority boundary
- Review boundary and rationale
- Compatibility impact and intentional removals
- Acceptance conditions: `WP-01-01`, `WP-01-02`, ...
- Suggested positive, negative, and review evidence
- Remaining risks or decisions

## Goal Acceptance

| ID | Required condition | Suggested evidence | Status |
|---|---|---|---|
| G-01 | Observable whole-goal condition | Test, inspection, review, or artifact | planned |

Keep Slice, Work Package or Milestone, and whole-Goal completion distinct.

## Acceptance Strategy

Describe the proportional smoke, targeted, regression, structural, security,
performance, compatibility, and hygiene evidence that applies. For a structural
or old-path guard, name the representative escape classes and false-positive
boundary needed for the approved claim.

## Risks, Assumptions, And Decisions

List material risks, current assumptions, decisions still required, approved
exceptions, and conditions that would require plan revision.

## Simplification Review

Record any lasting abstraction, compatibility layer, review boundary, or Work
Package split that needs explanation. Remove structure that lacks a current
requirement or evidence-backed reason.

## Recommended First Slice

- Why first
- Acceptance conditions advanced
- Smallest reviewable local outcome
- Preserved behavior
- Expected scope
- Exit evidence

## Review And Approval

Highlight the decisions the user should review and state that implementation
begins only after explicit approval. Confirm that a first-time reader can
understand the target and current constraints without earlier discussion.
