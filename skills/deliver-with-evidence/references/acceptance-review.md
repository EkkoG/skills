# Milestone And Final Acceptance Review

Use this procedure when proposing a Work Package, Milestone boundary, or Goal as
complete. Apply it proportionally to the current acceptance scope. It is a
review of the approved outcome and current implementation, not a summary of the
delivery ledger.

## Set The Acceptance Scope

For a Milestone, review only the Work Package conditions currently being
closed, their dependencies, relevant compatibility promises, intentional
removals, and approved exceptions. Do not require unrelated later Work Packages
or whole-Goal checks.

For Final acceptance, review every required Goal condition, all required Work
Packages, external compatibility promises, intentional removals, and approved
exceptions.

## Reconstruct The Contract

Start from the approved plan and current repository state. Enumerate every
required condition in the acceptance scope and build a fresh acceptance view
before relying on delivery-document, commit, Slice, or prior Milestone
completion labels.

Delivery documents may locate commands, changes, and earlier review notes.
Treat their status fields as claims requiring current evidence. An acceptance
report cannot prove itself, and one completion statement cannot prove another.

## Judge Evidence Sufficiency

For each condition, record what was observed and why that observation can
distinguish success from a plausible incomplete state. State material limits
when evidence could otherwise be overread.

Common evidence classes include:

- behavior: externally observable success, errors, rejection, and data shape;
- structure: responsibility, ownership, dependency direction, and composition;
- replacement: new ownership, consumer routing, and old-path disposition;
- security or reliability: adverse inputs, failure boundaries, recovery, and
  leakage constraints;
- performance: measured workload, threshold, variance, and comparison state;
- compatibility: promised inputs, outputs, workflows, and approved breaks;
- hygiene: static checks, generated content, repository state, and packaging.

Evidence from one class does not automatically prove another. In particular:

- passing existing behavior tests does not prove a structural migration unless
  the checks can distinguish the old and new structures;
- aggregate test counts do not establish architectural completeness;
- exact-name or exact-path negative searches prove only the searched absence;
- documentation and commit text index evidence but do not prove code state;
- a broader behavior suite may subsume narrower behavior checks, but it does
  not subsume a required architecture or removal review.

## Challenge Completion Claims

Treat each material completion claim as a hypothesis to challenge. Identify a
plausible counterexample appropriate to that condition, inspect for it, and
record the result. Examples of generic questions include:

- Could an approved old path, fallback, or dependency still be reachable?
- Could two components still own the same decision?
- Could the proposed replacement exist while relevant consumers still bypass
  it?
- Could passing tests exercise only preserved behavior rather than the claimed
  structural change?
- Could an approved removal have been renamed, moved, wrapped, or made private
  without changing responsibility?
- Could a compatibility, security, performance, or operational boundary remain
  untested on an important adverse path?

These are prompts, not a fixed checklist. Select counterexamples from the
approved conditions and observed system. Milestone review needs only challenges
material to its current scope; Final review challenges the whole Goal.

## Review Replacement Claims

Apply this section only when the approved plan requires replacement, removal,
isolation, or deprecation of an existing authority, dependency, fallback, side
effect, or implementation.

Verify proportionally that:

1. the replacement owns the intended responsibility;
2. relevant production consumers use the replacement;
3. the superseded path is removed, isolated, unreachable, or retained exactly
   as the approved plan allows;
4. the same responsibility has not merely been renamed, moved, hidden, or
   wrapped.

Do not require deletion when the approved plan permits another disposition.
Do not accept exact spelling changes as semantic replacement evidence.

## Choose The Review Mode

Milestone review may be performed by the coordinating agent unless project or
higher-level instructions require another reviewer. Keep it proportional to
the Work Package risk and scope.

Prefer an independent reviewer for broad or high-risk Final acceptance when
delegation is available, authorized, and proportional. Give that reviewer the
approved plan, current state, and raw evidence needed to evaluate the outcome;
do not provide the intended verdict. The reviewer may use the delivery document
to locate evidence, but must treat its status fields as unverified claims and
must not edit it. Return findings to the coordinating agent for serialized
recording.

When independent Final review is unavailable, perform a clean-room self-review:

- rebuild the whole-Goal condition matrix from the plan;
- inspect current implementation before accepting prior status labels;
- actively search for counterevidence;
- disclose that the review was not independent.

## Stop And Restart When Needed

Acceptance runs against a stable implementation state. If review finds a
required production change, mark the affected conditions partial, leave the
current acceptance mode, and return to the appropriate Slice. After the change
and its verification, start a new acceptance pass for that boundary; do not
continue the invalidated pass by editing the verdict in place.

A Work Package, Milestone boundary, or Goal may be complete only when every
required condition in its scope has sufficient current evidence,
counterevidence review exposes no unresolved blocker, and all exceptions are
explicitly approved.

## Acceptance Report

Use this structure only when a durable Milestone or Final report is useful:

```markdown
# Acceptance

Reviewed state:
<HEAD and concise worktree state>

Review mode:
<milestone review, independent Final, or clean-room Final self-review>

| Requirement | Type | Status | Current evidence | Counterevidence checked | Exception |
|---|---|---|---|---|---|
| <ID> | behavior/structure/replacement/etc. | verified/partial | <Observation and relevant code> | <Challenge and result> | <ID or none> |

Goal changes reviewed:
<None, or decision records>

Architecture and dependency review:
<Added, removed, and remaining edges>

Legacy authority review:
<What no longer controls behavior and what still does>

Evidence limitations:
<What major checks establish and what they do not establish>

Completion challenges:
<Material counterexamples sought, results, and unresolved findings>

Compatibility review:
<External compatibility versus unfinished internal migration>

Verification summary:
<Smoke, targeted, negative, architecture, regression, and hygiene>

Status:
- Slice: complete/partial
- Work Package or Milestone: complete/partial/not applicable
- Goal: complete/partial

Blocking items:
<Exact unresolved requirements>
```
