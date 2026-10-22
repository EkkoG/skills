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

For local Work Package or Milestone acceptance, the coordinator matches the
required conditions to current raw evidence, limits and blockers. Reuse the
existing condition mapping and deepen inspection where evidence is missing,
contradictory or stale. This is an acceptance decision, not a second execution
or independent review pass.

An independent reviewer reconstructs the contract for its assigned boundary;
Final reconstructs every Goal and Work Package condition from the approved
plan and current implementation. Delivery and prior reports locate evidence;
their completion labels are claims, not proof.

For every condition, record:

- the current evidence and what it can distinguish;
- a plausible incomplete state or counterexample that was checked;
- material limitations and any approved exception;
- `verified` or `partial` status.

Within the review scope, inspect current owners and consumers for each approved
reuse, extension, composition or separation decision, including integration
changes. Verify the intended local responsibility and absence of unapproved
parallel implementations. Local acceptance may reuse this evidence while its
relevant scope remains unchanged.

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

Within the assigned scope, check that new abstractions, modules, dependencies,
state and safeguards serve current requirements, reuse existing capabilities
where appropriate, and avoid unapproved parallel implementations. The reviewer
checks fidelity to approved design; the challenger independently tests the
necessity of complexity and simpler alternatives. Block overdesign only for a
concrete failure under the threshold above. A preference for a simpler design
does not justify reopening settled tradeoffs or starting another correction.

## Choose The Review Mode

Work Package and Milestone acceptance are normally coordinating decisions.
Use pre-Final review only for the actual behavior or authority risks defined
by the [execution role criteria](../SKILL.md#route-execution-roles), not a
module name, declaration edit or package completion event. Record the specific
downstream work that needs the verdict; independent work can continue. Otherwise
retain focused verification and defer independent challenge to Final. Reuse
the same reviewer for a boundary's corrective closure and a fresh reviewer for
a different boundary.

Final uses a fresh `final_reviewer` and fresh Grok-backed `challenger`. Give
both the approved contract, the same stable repository snapshots, complete raw
evidence, and material limitations without the other's initial verdict or a
desired conclusion. Both independently evaluate Delivery's status claims and
use only non-mutating reads; checks requiring writes return to the coordinator.
Read and apply the shared
[review-agreement contract](../../design-delivery-plan/references/review-agreement.md)
before closing Final. Implementation-risk review retains a single reviewer.

Independence comes from a separate reviewer context and evaluation of raw
evidence, not sandbox isolation. A writable sandbox does not block review:
follow the no-write contract and disclose the effective sandbox and lack of
isolation in the result. Once unavailability or lack of authorization is
established under the [role-routing criteria](../SKILL.md#route-execution-roles),
use this clean-room fallback for an implementation-risk review, or to collect
diagnostic evidence while a Final participant is unavailable:

1. rebuild the current acceptance matrix from the approved plan, using the
   whole-Goal matrix for Final;
2. inspect current implementation before accepting prior status;
3. actively search for counterevidence;
4. disclose that the review was not delegated and therefore lacks a separate
   reviewer context.

For Final, this fallback does not complete the paired gate. Keep agreement
pending and report the blocker; any different completion path needs an
explicit user revision of the gate, recorded as an exception rather than
agreement. A failed or incomplete Grok invocation is also an unavailable result.

Ask an initial review for the complete currently discoverable finding set and a
bounded counterexample matrix for each blocker class. Separate blockers from
non-blocking advice and return missing evidence as one bounded list rather than
incremental findings.

## Order Broad Evidence And Review

Resolve material toolchain, gate or evidence-access unknowns with cheap early
preflight. Its purpose is to reveal feasibility problems before expensive work,
not to replace required verification or trigger a review. Keep ordinary
in-scope diagnosis and correction with the implementation owner.

At a qualifying pre-Final implementation-risk boundary, a stable implementation
verdict may precede boundary-wide broad evidence. After a no-blocker verdict,
run the broad evidence owned by that boundary once on the reviewed state.

For Final, open the review only after known production changes, required
documentation, and the evidence packet are stable. Final review is an
acceptance gate rather than an iterative debugging pass. Use this order:

1. establish stable final implementation across every repository;
2. have the coordinator ensure required broad, build and hygiene evidence is
   current on those snapshots; the implementation owner may run it and valid
   existing results are reused;
3. provide the complete packet and raw evidence to the fresh Final pair;
4. reconcile material disagreements and record the agreed verdict against
   that one stable state.

A Final reviewer should not be asked to approve an incomplete evidence packet.
Additional evidence without a production change can return to a pending verdict
when the verdict was explicitly conditional on that evidence.

During implementation, rerun affected focused checks on corrected states as
needed to complete the outcome. Run expensive boundary-wide checks and final
builds on their relevant stable source, and required Whole-Goal evidence before
Final. Reuse evidence whose code, inputs, tests, rules and contract remain
unchanged. Documentation-only, formatting-only and unrelated changes do not
invalidate production evidence.

## Correct Blocking Findings

Acceptance runs against stable code. When review requires a production change:

1. mark affected conditions partial and leave acceptance mode;
2. group all blockers from the same boundary into one corrective Slice;
3. implement and run focused verification;
4. perform one targeted closure review of each complete blocker-class matrix
   and its direct regression risks when that boundary requires independent
   implementation review;
5. rerun only broad or hygiene evidence invalidated by the correction;
6. for Final, perform a new complete Final pass with a fresh pair on the
   corrected stable state.

Do not start another reviewer between findings from the same pass and the
corrective Slice. A new Final pass is justified only after the correction is
stable and the affected evidence has been refreshed.

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
no unresolved blocker, and explicit approval for every exception. Final also
requires the pair's agreed pass under the shared agreement contract.

## Acceptance Report

Use a durable report only when it helps later acceptance or handoff:

```markdown
# Acceptance

Reviewed repository states:
<Roots, HEADs, and concise worktree states>

Review mode:
<local Work Package, stable Milestone boundary, paired Final, or diagnostic fallback>

Paired review (when applicable):
<Both result references, agreed-pass/agreed-blocked/pending, material dispositions>

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
