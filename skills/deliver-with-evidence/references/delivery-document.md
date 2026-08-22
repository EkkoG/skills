# Delivery Document

Use this reference when initializing, resuming, or structurally updating the
private Delivery document. Keep project documents authoritative and copy only
the contract and state needed for reliable resumption and acceptance.

## Resolve The Path

Use a path explicitly required by the user, approved plan, or repository
instructions. Otherwise use:

```text
$CODEX_HOME/state/delivery/<repo-key>/<goal-id>/delivery.md
```

`CODEX_HOME` defaults to `~/.codex`.

For the default path:

- form `<repo-key>` from a safe resolved workspace basename plus the first 10
  lowercase hexadecimal characters of SHA-256 over the UTF-8 resolved absolute
  root path;
- enumerate existing `<repo-key>/*/delivery.md` files before creating a Goal;
- resume only when exactly one document's workspace, Goal title, plan source,
  and initial approval identify the same work;
- stop and reconcile when multiple documents match or an explicitly selected
  document belongs to different work;
- when no document matches, generate `<goal-id>` once from a readable Goal
  slug plus a short random suffix such as 12 UUID hex characters;
- retain an existing Goal ID and path across later approved Goal changes.

Keep the default root outside the target repository. Use a repository-local
path only when current instructions explicitly require it. Create private
directories and files where supported, normally `0700` for directories and
`0600` for the document.

## Preserve One Writer

The coordinating agent is the only writer. Delegated discovery,
implementation, and review return results for serialized integration and never
edit the document.

Keep one active coordinator per Goal. If another active coordinator, conflicting
state, or an ambiguous resume candidate is detected, stop and reconcile the
approved contract, current implementation, evidence, and next action before
writing.

Write through a private temporary file in the same directory and replace the
document atomically. Do not overwrite a document whose recorded workspace,
Goal, plan source, or initial approval identifies different work.

## Template

```markdown
# Delivery Document

- Workspace: `<repository or target workspace root>`
- Repository key: `<safe basename>-<root hash prefix>`
- Goal: `<approved Goal title>`
- Goal ID: `<stable generated ID>`
- Delivery path: `<exact persistent path>`
- Plan source: `<path, conversation, issue, or other authority>`
- Initial approval: `<first approval boundary and date>`
- Current approval: `<latest approval boundary and date>`
- Goal status: partial
- Current Slice: `<ID, or none>`
- Slice status: `<in progress, blocked, or none>`
- Based on HEAD: `<commit or not applicable>`
- Worktree: `<clean, concise dirty paths, or non-Git baseline>`

## Approved Contract

- Final outcome: <Complete current Goal>
- Scope and boundaries: <Required work and authority limits>
- Stable exclusions: <Current exclusions>
- Work Package dependency graph: <Stable IDs and dependency edges>
- Required acceptance: <Every current Goal and Work Package label>
- Material architecture and decisions: <Resume-critical current decisions>
- Compatibility and removals: <Promises and negative obligations, or none>
- Risks, assumptions, and exceptions: <Material current context>

### `<WP-ID>`

- Status: <pending, in progress, review-ready, blocked, or complete>
- Outcome: <Reviewable result>
- Owned scope and exclusions: <Included and prohibited responsibility>
- Dependencies: <Required Work Packages or none>
- Implementation boundary: <Authority, data flow, or behavior>
- Acceptance: <Stable labels>
- Compatibility, removals, and risks: <Applicable details>

## Review Boundaries

### `<boundary ID>`

- Status: <pending, review-ready, reviewed, or invalidated>
- Includes: <Work Package and acceptance labels>
- Authority and risk: <Shared review scope>
- Stable dependencies: <Required state or none>
- Dependent work: <Production work that waits for the verdict, or none>
- Review snapshot: <HEAD and concise worktree state, or pending>
- Focused evidence: <Condition-linked evidence references, or pending>
- Verdict: <No blocker, blockers, deferred to Final, or pending>
- Invalidated evidence: <Affected labels and reason, or none>

## Current Slice Contract

- Why now: <Selection reason>
- Covers: <Stable acceptance labels>
- Local outcome: <One reviewable result>
- Preserved behavior: <External promises or boundaries>
- Expected scope: <Relevant responsibility or authority>
- Exit evidence: <Checks or review needed>

## Completed

- `<Slice ID>` <Result and covered labels>

## Goal Change History

- <References or embedded Goal Change Records, or none>

## Evidence

- PASS [G-01] `<evidence title>`
  - Method: <Reproducible command, inspection, or review>
  - Observed: <What was established>
  - Supports: <Condition within that observation>
  - Limits: <Material claims not established>
  - State: <HEAD or other relevant state>
  - Artifact: <Persistent location when useful, or none>

## Missing Evidence

- <Required condition without sufficient current evidence, or none>

## Known Failures Or Exceptions

- <Existing failure, baseline, or approved exception>

## Resume

<Exact continuation point or re-evaluation action>
```

Omit optional fields that do not apply. When a durable plan exists, link it and
copy only resume-critical details. For a conversation-only plan, embed enough
of the approved contract to resume every Work Package without guessing.

## Record Useful State And Evidence

Initialize the document before the first production edit with the approved
contract, Work Package status, current implementation state, missing evidence,
and exact next action.

Update it when selecting, completing, blocking, resuming, or invalidating a
Slice; when a review boundary becomes review-ready, reviewed, or invalidated;
and at Milestone or Final acceptance. Record concise state transitions,
condition-linked evidence, known failures or exceptions, and the next action.
Do not keep a command transcript or reconstruct unsupported history.

Every reusable evidence item names the conditions it supports and retains a
reproducible method, relevant state, observed result or durable artifact, and
material limits. One item may support several conditions. Delivery status,
commit text, and acceptance reports locate evidence but do not prove the
implementation claim.

Reuse evidence when the relevant code, tests, rules, and contract are unchanged.
When later work changes a reviewed authority, mark the affected evidence and
conditions invalid without discarding unaffected records. Revalidate the
changed scope at the next relevant stable boundary or Final. Rerun evidence
when relevance or reproducibility is uncertain. Retain the completed document
unless another approved retention rule applies.

When a material Goal change is approved, update Current approval, the complete
current Approved Contract, affected status, and the Goal Change Record in one
atomic write. Keep Initial approval unchanged.
