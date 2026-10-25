---
name: design-delivery-plan
description: Design approval-ready engineering plans for complex multi-step work. Use for broad features, refactors, migrations, cleanup, security, reliability, performance, or other programs needing dependency-aware outcomes and acceptance conditions. Do not use for implementation, status questions, ordinary review, small fixes, or one bounded change.
---

# Design Delivery Plan

Produce a self-contained draft that another agent can execute without
inventing scope or confusing local progress with Goal completion. Stay in
planning and stop at the user's approval boundary.

## Decide Whether To Plan

Use this skill when the work has multiple dependent outcomes, meaningful
architecture or compatibility decisions, or enough breadth that a local fix
could be mistaken for completion. Handle a single clear change directly.

Apply system, user, repository, and project instructions first. Inspect current
implementation, decisions, tests, documents, and worktree state before fixing
the target. Keep the plan aligned with the user's latest decisions and make it
understandable to a first-time reader.

## Persist The Plan

Save the first complete draft before delegated review or presentation. Use an
explicitly required plan path; otherwise keep it outside target repositories at:

```text
$CODEX_HOME/state/plans/<repo-key>/<plan-id>/plan.md
```

`CODEX_HOME` defaults to `~/.codex`. Form `<repo-key>` from the safe basename of
the resolved coordinating workspace plus the first 10 lowercase hex characters
of SHA-256 over its UTF-8 absolute path, matching Delivery's repository key.
Choose an unused `<plan-id>` once, such as `YYYYMMDD-HHMMSS-goal-slug`, and retain
that path through revisions, approval, execution, and resumption.

The coordinator alone updates the plan. Record the coordinating workspace,
draft or approved status, and the user's approval reference when given. Give
reviewers this persistent path; keep recovery-critical supporting material and
review results alongside it, using `reviews/` for review artifacts. Reuse durable
sources by reference. On resume, read the saved plan and latest user decisions
before continuing; keep the plan after delivery.

Use private directories and files, normally `0700` and `0600`. Obtain any
missing write permission through normal approval; if unavailable, report the
blocker before delegated review or formal handoff. Saving a draft does not
authorize implementation. Small direct tasks do not create plan files.

## Route Planning Roles

- Use `explorer` only for a bounded, read-only question whose answer can change
  Goal scope, a Work Package boundary, dependencies, or first Slice selection.
  Reuse its evidence in the current planning pass.
- For a broad or high-risk plan, use `plan_reviewer` once before presenting the
  draft for approval. Give it the latest goal, raw current-state evidence, and
  draft plan without a desired verdict. Reuse it for targeted closure of
  material plan changes or disputed findings.
- For the same broad or high-risk candidate, incorporate the review findings
  into a stable draft, then use a fresh `plan_challenger` once before user
  approval. It invokes the local Grok CLI for the cross-model challenge of
  assumptions, design choices, and avoidable complexity. Supply the
  latest goal, constraints, settled decisions, current draft, raw-evidence
  locations, and unresolved facts without prior reviewer verdicts or an
  expected conclusion. Keep both passes on stable drafts in this order.
  Supply the installed [Grok invocation reference](references/grok-cli.md)
  and its helper path in the challenger packet.
- Complete paired review under
  [references/review-agreement.md](references/review-agreement.md). Both roles
  must agree on the current draft's verdict and material finding dispositions.
  If incorporating findings changes the design, obtain targeted confirmation
  from the original reviewer on that draft before recording agreement. The
  coordinator relays disputes and records results; optional simplifications
  remain advice. An agreed pass makes the draft ready for user approval.
- Treat the draft as one approval candidate. Wording, formatting, and Slice-level
  refinements reuse unaffected conclusions. Material changes to the Goal
  contract, architecture, dependency graph, permissions, compatibility, or
  acceptance strength require targeted closure by the affected role. Evidence
  closing a required gap and disputed findings return to the existing pair;
  do not automatically rerun the full review chain.
- Assess breadth and risk from intended behavior, authority, compatibility and
  uncertainty, not the names of touched files or modules. Material changes to
  public contracts, permissions, data integrity or migrations qualify; otherwise
  use independent plan review only when scope or uncertainty warrants it.
- Start delegated planning work with `fork_turns="none"` and a self-contained
  task packet; reference exact paths instead of copying long documents.
- Planning uses `plan_reviewer` and `plan_challenger`; execution roles belong
  to approved-plan execution.
- Use main-thread fallback for a required role only after an explicit tool or
  policy restriction, or an actual start/resume failure that remains after one
  applicable recovery attempt. Judge availability separately for each role;
  task listings describe existing tasks, not which roles can be started.
  Recover invocation conflicts by reusing an eligible agent or choosing a
  unique task name. Disclose the restriction or error, recovery outcome, and
  lack of independent reviewer context before doing the bounded work locally.
  For paired review, local fallback is diagnostic only: an unavailable
  `plan_reviewer`, `plan_challenger`, or Grok invocation leaves agreement
  pending under the shared agreement contract. Disclose the limitation and
  ask the user how to proceed; Main cannot substitute its own agreement.
- Reviewers, challengers, and explorers in writable sandboxes continue under
  their no-write contracts and disclose the lack of sandbox isolation.

## Build The Contract

Establish current reality and separate facts, conclusions, assumptions, and
pending decisions. Define:

- one observable final outcome and the condition for Whole Goal completion;
- required scope, stable exclusions, intentional behavior changes, and
  compatibility, security, performance, permission, and delivery constraints;
- outcome-based Work Packages with stable IDs, owned boundaries, exclusions,
  dependency edges, acceptance labels, risks, and proportional evidence;
- material reuse, extension, composition, or separation decisions, including
  the responsibility that remains local.

Use IDs such as `G-01`, `WP-01`, and `WP-01-01`. Dependencies form a DAG;
numbering does not prescribe execution order. Do not pre-plan every Slice.
Execution chooses a complete reviewable outcome from current code and evidence,
including the diagnosis, implementation and verification needed to finish it.

Define a risk review boundary only when later work depends on its authority,
behavior, or evidence, or when a high-impact security, permission,
data-integrity, or migration failure would be materially more costly to find
at Final. Name the behavior at risk and the specific downstream work that must
wait. A boundary may contain one or more Work Packages; independent work need
not wait for an entire package's review.

## Keep Acceptance Proportional

Match evidence to the claim: behavior, structure, replacement/removal,
security or reliability, performance, compatibility, and hygiene each prove
different things. State positive evidence for replacements and proportional
negative evidence for an approved old-path disposition. Do not design a
general analyzer or exhaustive test matrix when representative cases prove the
contract. Separate cheap early feasibility checks for uncertain toolchains,
required gates or evidence access from focused implementation checks and final
acceptance. Reserve expensive final suites and builds for relevant stable
source; earlier independent evidence is reusable when its inputs stay valid.

Start from the smallest change to the existing implementation that meets the
outcome. Add abstractions, layers, or recovery mechanisms only for a current
requirement or a concrete failure under the actual input, trust, and deployment
boundaries. For material hardening beyond scope, present the failure scenario,
likelihood, impact, and complexity cost for the user's decision. Preserve
required security, reliability, and compatibility. Before presentation, remove
hypothetical extension points, package splits that only mirror directories,
and repeated checks that add no confidence.

## Prepare Approval And Handoff

Read [references/plan-template.md](references/plan-template.md) when creating
or substantially revising a full plan, using only the sections needed for the
current work. Recommend the first smallest reviewable Slice, subject to
execution-time revalidation.

The handoff must expose the final outcome, boundaries, dependency graph,
acceptance labels, compatibility promises, intentional removals, required
negative evidence, risks, approved exceptions, participating repositories,
and first-Slice recommendation. Planning proposes evidence; execution records
actual results.

Keep production code unchanged and distinguish proposed checks from observed
results. User approval authorizes execution. After approval, `deliver-with-evidence`
creates the persistent Delivery document before the first production edit and
links this plan as its source.
