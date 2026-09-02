# Work Package, Milestone, And Final Acceptance Review

Use this procedure before proposing a Work Package, Milestone, or Goal as
complete. Review the approved outcome against current implementation and raw
evidence rather than summarizing Delivery status.

## Set The Scope

For a Work Package, review its approved outcome, dependencies, acceptance
labels, compatibility promises, intentional removals, and approved exceptions.
The coordinating agent may close it locally when every required condition has
sufficient current evidence. Independent review is required only when the Work
Package is also part of a qualifying risk or review boundary.

For a Milestone, review one stable acceptance or risk boundary containing one
or more Work Packages. Include the conditions being closed, stable
dependencies, relevant compatibility promises, intentional removals, and
approved exceptions. Package numbering and completion order do not define the
boundary.

For Final, review every required Goal and Work Package condition, all external
compatibility promises, intentional removals, and approved exceptions.

Run each pass against stable repository snapshots and one complete packet
containing the approved contract, acceptance labels, current state, raw
evidence, and material limitations.

## Reconstruct The Contract

Build a fresh condition matrix from the approved plan and current repository
state before relying on Delivery, commit, Slice, Work Package, or prior
Milestone completion labels. Delivery may locate evidence, but its status fields
are claims. An acceptance report cannot prove itself.

For every condition, record:

- the current evidence and what it can distinguish;
- a plausible incomplete state or counterexample that was checked;
- material limitations and any approved exception;
- `verified` or `partial` status.

For each approved existing-implementation decision, inspect the complete
current production scope that can own the responsibility, including relevant
code added after planning or during integration. Verify the selected reuse,
extension, composition, or separation; the responsibility intentionally kept
local; and the absence of an unapproved parallel implementation. A relevant
snapshot change makes the prior result stale.

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
architectural completeness, and exact-name absence proves only the searched
absence. A broader check may subsume a narrower check of the same class and
state, but it does not replace required architecture or removal evidence.

For replacement, removal, isolation, or deprecation claims, verify
proportionally that the replacement owns the responsibility, relevant
production consumers use it, the superseded path has the approved disposition,
and the responsibility was not merely renamed, moved, hidden, or wrapped.

Reuse authoritative evidence while its relevant code, tests, rules, contract,
and repository snapshots remain unchanged. Rerun only evidence whose support
has become stale, ambiguous, or invalidated. Record known baseline failures
precisely and require no new failures.

## Challenge Completion

Select plausible counterexamples from the approved conditions and observed
system. Useful questions include whether an old path remains reachable, two
components still share authority, consumers bypass a replacement, tests cover
only preserved behavior, or an adverse compatibility or security path remains
unchecked.

Challenge only the current acceptance scope. Use representative cases that can
distinguish the approved outcome instead of exhaustive permutations or a
general-purpose analyzer.

When a challenge exposes a blocking failure class, test representative
equivalent forms, entry paths, boundary cases, and direct safe neighbors before
returning the verdict. Report the currently discoverable class as one bounded
counterexample matrix rather than revealing one example per review round. Keep
the matrix proportional to the approved claim.

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

Work Package acceptance is normally a local coordinating decision. Use an
independent implementation review only when the package participates in a
qualifying risk or review boundary.

Milestone review may be performed by the coordinating agent unless current
instructions require independence. Use independent review before Final when
later production semantically depends on the boundary's authority, behavior,
or evidence, or when delaying a high-impact security, permission,
data-integrity, or migration failure would materially enlarge correction or
rollback scope. Execution order alone is not dependency. Otherwise record the
boundary as implemented and locally verified and defer independent challenge to
Final. Independent stable boundaries may be reviewed in parallel when neither
can invalidate the other's snapshot.

Use an independent reviewer for Final when delegation is available, authorized,
and proportional. Give the reviewer the approved contract, stable repository
snapshots, complete raw evidence, and material limitations without a desired
verdict. The reviewer may read but must not edit Delivery and must independently
evaluate its status claims.

Treat a review as independent only when its effective boundary is read-only.
Otherwise use a separate read-only turn or this clean-room fallback:

1. rebuild the current acceptance matrix from the approved plan, using the
   whole-Goal matrix for Final;
2. inspect current implementation before accepting prior status;
3. actively search for counterevidence;
4. disclose that the review was not independent.

Ask an initial review for the complete currently discoverable finding set and a
bounded counterexample matrix for each blocker class. Separate blockers from
non-blocking advice and return missing evidence as one bounded list rather than
incremental findings.

## Order Broad Evidence And Review

At a qualifying pre-Final implementation-risk boundary, a stable implementation
verdict may precede boundary-wide broad evidence. After a no-blocker verdict,
run the broad evidence owned by that boundary once on the reviewed state.

For Final, use this order:

1. establish stable final implementation across every repository;
2. have the coordinating agent run required whole-Goal broad and hygiene
   evidence once on those snapshots;
3. provide the complete packet and raw evidence to the Final reviewer;
4. issue the verdict against that one stable state.

A Final reviewer should not be asked to approve an incomplete evidence packet.
Additional evidence without a production change can return to a pending verdict
when the verdict was explicitly conditional on that evidence.

## Correct Blocking Findings

Acceptance runs against stable code. When review requires a production change:

1. mark affected conditions partial and leave acceptance mode;
2. group blockers from the same boundary into one corrective Slice;
3. implement and run focused verification;
4. perform one targeted closure review of each complete blocker-class matrix
   and its direct regression risks when that boundary requires independent
   implementation review;
5. rerun only broad or hygiene evidence invalidated by the correction;
6. for Final, perform a new complete Final pass on the corrected stable state.

Default to one regular corrective cycle. If the same finding class survives,
reconstruct the contract, counterexample, and Slice boundary before further
implementation. New advice extends the loop only when it demonstrates a
required-contract, correctness, security, permission, data, concurrency, or
external compatibility failure, or a regression introduced by the correction.

If later production work changes a reviewed authority, mark only the affected
conditions and evidence partial. Retain unaffected results and Work Package
status, and revalidate the changed scope at the next relevant boundary or
Final.

Completion requires sufficient current evidence for every condition in scope,
no unresolved blocker, and explicit approval for every exception.

## Acceptance Report

Use a durable report only when it helps later acceptance or handoff:

```markdown
# Acceptance

Reviewed repository states:
<Roots, HEADs, and concise worktree states>

Review mode:
<local Work Package, stable Milestone boundary, independent Final, or clean-room Final>

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
- Slice: complete/partial/not applicable
- Work Package: complete/partial/not applicable
- Milestone: complete/partial/not applicable
- Goal: complete/partial

Blocking items:
<Exact unresolved requirements>
```
