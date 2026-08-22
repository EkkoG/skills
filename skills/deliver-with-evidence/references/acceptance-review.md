# Milestone And Final Acceptance Review

Use this procedure before proposing a Work Package, Milestone, or Goal as
complete. Review the approved outcome against the current implementation and
raw evidence rather than summarizing Delivery status.

## Set The Scope

For a Milestone, review the Work Package conditions being closed, their
dependencies, relevant compatibility promises, intentional removals, and
approved exceptions.

For Final, review every required Goal and Work Package condition, all external
compatibility promises, intentional removals, and approved exceptions.

Run the pass against one stable implementation snapshot and one complete packet
containing the approved contract, acceptance labels, current state, and raw
evidence.

## Reconstruct The Contract

Build a fresh condition matrix from the approved plan and current repository
state before relying on Delivery, commit, Slice, or prior Milestone completion
labels. Delivery may locate evidence, but its status fields are claims. An
acceptance report cannot prove itself.

For every condition, record:

- the current evidence and what it can distinguish;
- a plausible incomplete state or counterexample that was checked;
- material limitations and any approved exception;
- `verified` or `partial` status.

## Match Evidence To The Claim

Use evidence appropriate to the condition:

- behavior for observable success, errors, rejection, and data shape;
- structure for responsibility, ownership, dependency direction, and
  composition;
- replacement for new ownership, consumer routing, and old-path disposition;
- security or reliability for adverse inputs, failure boundaries, recovery, and
  leakage;
- performance for measured workload, threshold, variance, and comparison state;
- compatibility for promised inputs, outputs, and workflows;
- hygiene for static checks, generated content, packaging, and worktree state.

One evidence class does not automatically prove another. Existing behavior
tests do not prove structural migration, aggregate counts do not prove
architectural completeness, and exact-name absence proves only that searched
absence. A broader check may subsume a narrower check of the same class and
state, but it does not replace required architecture or removal review.

For replacement, removal, isolation, or deprecation claims, verify
proportionally that the replacement owns the responsibility, relevant
production consumers use it, the superseded path has the approved disposition,
and the responsibility was not merely renamed, moved, hidden, or wrapped.

## Challenge Completion

Select plausible counterexamples from the approved conditions and observed
system. Useful questions include whether an old path remains reachable, two
components still share authority, consumers bypass a replacement, tests cover
only preserved behavior, or an adverse compatibility or security path remains
unchecked.

Challenge only the current acceptance scope. Use representative cases that can
distinguish the approved outcome instead of exhaustive permutations or a
general-purpose analyzer.

## Apply The Blocking Threshold

Block acceptance only for:

- an unsatisfied required condition;
- a demonstrated correctness, security, permission, data, concurrency, or
  external compatibility failure;
- a failed required gate;
- missing evidence necessary for the claimed completion.

Treat style preferences, speculative extensions, stronger-than-approved proof,
and low-impact maintainability suggestions as non-blocking residual risks.

## Choose The Review Mode

Milestone review may be performed by the coordinating agent unless current
instructions require independence. Prefer independent review for broad or
high-risk Milestones when it is proportional.

Use an independent reviewer for Final when delegation is available, authorized,
and proportional. Give the reviewer the approved contract, stable current
state, and raw evidence without a desired verdict. The reviewer may read but
must not edit Delivery, and must independently evaluate its status claims.

Treat the review as independent only when its effective boundary is read-only.
Otherwise use a separate read-only turn or this clean-room fallback:

1. rebuild the whole-Goal matrix from the approved plan;
2. inspect current implementation before accepting prior status;
3. actively search for counterevidence;
4. disclose that the review was not independent.

Ask an initial review for the complete currently discoverable finding set.
Separate blockers from non-blocking advice and return missing evidence as one
bounded list rather than incremental findings.

## Correct Blocking Findings

Acceptance runs against stable code. When review requires a production change:

1. mark affected conditions partial and leave acceptance mode;
2. group blockers from the same boundary into one corrective Slice;
3. implement and run focused verification;
4. perform one targeted closure review of the original blockers and direct
   regression risks;
5. run deferred broad evidence once on the stable corrected state;
6. for Final, perform one complete Final pass on that final state.

Additional evidence without a production change does not invalidate the code
snapshot; return it to the pending verdict when that verdict was conditional on
the evidence.

Default to one regular corrective cycle. If the same finding class survives,
reconstruct the contract, counterexample, and Slice boundary before further
implementation. New advice extends the loop only when it demonstrates a
required-contract, correctness, security, permission, data, concurrency, or
external compatibility failure, or a regression introduced by the correction.

Milestone or Goal completion requires sufficient current evidence for every
condition in scope, no unresolved blocker, and explicit approval for every
exception.

## Acceptance Report

Use a durable report only when it helps later acceptance or handoff:

```markdown
# Acceptance

Reviewed state:
<HEAD and concise worktree state>

Review mode:
<Milestone, independent Final, or clean-room Final>

| Requirement | Type | Status | Current evidence | Counterexample checked | Exception |
|---|---|---|---|---|---|
| <ID> | behavior/structure/replacement/etc. | verified/partial | <Observation> | <Challenge and result> | <ID or none> |

Evidence limitations:
<Material limits>

Compatibility and removal review:
<Promises, replacement ownership, and remaining paths>

Verification summary:
<Focused, negative, structural, broad, and hygiene checks>

Status:
- Slice: complete/partial
- Work Package or Milestone: complete/partial/not applicable
- Goal: complete/partial

Blocking items:
<Exact unresolved requirements>
```
