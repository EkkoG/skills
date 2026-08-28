# Delivery Document

Use this reference when initializing, resuming, or structurally updating the
private Delivery document. Keep project documents authoritative and copy only
the contract and state needed for reliable resumption and acceptance.

## Resolve The Path And Permission

Use a path explicitly required by the user, approved plan, or repository
instructions. Otherwise use:

```text
$CODEX_HOME/state/delivery/<repo-key>/<goal-id>/delivery.md
```

`CODEX_HOME` defaults to `~/.codex`.

For the default path:

- choose the primary or coordinating workspace root;
- form `<repo-key>` from a safe resolved root basename plus the first 10
  lowercase hexadecimal characters of SHA-256 over the UTF-8 resolved absolute
  root path;
- enumerate existing `<repo-key>/*/delivery.md` files before creating a Goal;
- resume only when exactly one document's coordinating workspace, Goal title,
  plan source, and initial approval identify the same work;
- stop and reconcile when multiple documents match or an explicitly selected
  document belongs to different work;
- when no document matches, generate `<goal-id>` once from a readable Goal slug
  plus a short random suffix such as 12 UUID hex characters;
- retain an existing Goal ID and path across later approved Goal changes.

Keep the default root outside every target repository. Use a repository-local
path only when current instructions explicitly require it. If the required
external path is not writable, request permission for that exact path or ask
for an approved alternate and stop before the first production edit. Plan
approval does not authorize sandbox escalation, and lack of access does not
authorize silently moving Delivery into a repository.

Create private directories and files where supported, normally `0700` for
directories and `0600` for the document.

## Preserve One Writer

The coordinating agent is the only writer. Delegated discovery,
implementation, and review return results for serialized integration and never
edit the document.

Keep one active coordinator per Goal. If another active coordinator,
conflicting state, or an ambiguous resume candidate is detected, stop and
reconcile the approved contract, current implementation, evidence, repository
states, and next action before writing.

Write through a private temporary file in the same directory and replace the
document atomically. Do not overwrite a document whose coordinating workspace,
Goal, plan source, or initial approval identifies different work.

## Template

```markdown
# Delivery Document

- Coordinating workspace: `<primary repository or target workspace root>`
- Repository key: `<safe basename>-<root hash prefix>`
- Goal: `<approved Goal title>`
- Goal ID: `<stable generated ID>`
- Delivery path: `<exact persistent path>`
- Plan source: `<path, conversation, issue, or other authority>`
- Initial approval: `<first approval boundary and date>`
- Current approval: `<latest approval boundary and date>`
- Goal status: partial
- Current Slice: `<WP-01-S01, or none>`
- Current Slice title: `<short outcome title, or none>`
- Slice status: `<in progress, commit-ready, blocked, or none>`

## Repository States

| Repository | Resolved root | Goal scope | HEAD | Worktree |
|---|---|---|---|---|
| `<name>` | `<absolute path>` | `<owned Goal responsibility>` | `<commit or not applicable>` | `<clean, concise dirty paths, or non-Git baseline>` |

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

### `<boundary description>`

- Status: <pending, review-ready, reviewed, or invalidated>
- Includes: <Work Packages and acceptance labels>
- Authority and risk: <Shared review scope>
- Stable dependencies: <Required state or none>
- Dependent work: <Production work that waits for the verdict, or none>
- Review snapshot: <Repository HEADs and concise worktree states, or pending>
- Focused evidence: <Condition-linked evidence references, or pending>
- Verdict: <No blocker, blockers, deferred to Final, or pending>
- Invalidated evidence: <Affected labels and reason, or none>

## Current Slice Contract

- Slice ID: `<WP-01-S01>`
- Title: <Short outcome title>
- Why now: <Selection reason>
- Covers: <Stable acceptance labels>
- Local outcome: <One reviewable result>
- Preserved behavior: <External promises or boundaries>
- Expected scope: <Relevant responsibility or authority>
- Exit evidence: <Checks or review needed>

## Completed

- `WP-01-S01` - <Title, result, and covered labels>

## Commit Checkpoints

### <Stable outcome and date>

- Included Slices: `<Slice IDs>`
- Status: <complete or partial>

| Repository | Commit | Remaining worktree |
|---|---|---|
| `<resolved root or name>` | `<hash, commit-ready, or failed>` | `<concise state>` |

- Blocker: <Exact partial-commit failure or none>

## Goal Change History

- <References or embedded Goal Change Records, or none>

## Evidence

- PASS [G-01] `<evidence title>`
  - Method: <Reproducible command, inspection, or review>
  - Observed: <What was established>
  - Supports: <Condition within that observation>
  - Limits: <Material claims not established>
  - State: <Repository HEADs or other relevant state>
  - Artifact: <Persistent location when useful, or none>

## Missing Evidence

- <Required condition without sufficient current evidence, or none>

## Known Failures Or Exceptions

- <Existing failure, partial repository commit, baseline, or approved exception>

## Resume

<Exact continuation point or re-evaluation action>
```

Omit optional fields that do not apply. When a durable plan exists, link it and
copy only resume-critical details. For a conversation-only plan, embed enough
of the approved contract to resume every Work Package without guessing.

## Record Repository State And Commit Checkpoints

List every repository whose production state or commit history participates in
the Goal. Record its resolved root, owned Goal scope, current HEAD, and concise
worktree state. Refresh affected rows when selecting, completing, blocking,
resuming, or invalidating a Slice and at every acceptance boundary.

One logical commit checkpoint may contain a hash for each participating
repository. Treat it as complete only when every intended repository commit
succeeds. If some commits succeed and another fails, atomically record the
successful hashes, failed repository, current worktrees, exact blocker, and
resume action as a partial checkpoint. Do not claim a single stable checkpoint
or continue dependent production work until the partial state is reconciled.

When commit creation is not authorized, record the coherent scope as
`commit-ready` with its included Slices and current repository states. Do not
infer Git-history authorization from approval to implement the plan.

After Slice evidence is accepted and the commit decision is resolved, perform
one atomic Delivery update containing Slice completion, repository states,
commit hashes or `commit-ready` status, accepted evidence, and the next action.
If commit creation fails, use that update to record the exact blocker and any
partial repository state rather than recording a completed checkpoint.

## Record Useful State And Evidence

Initialize the document before the first production edit with the approved
contract, Work Package status, repository states, missing evidence, and exact
next action.

Update it when selecting, completing, blocking, resuming, or invalidating a
Slice; when a Work Package or review boundary changes state; when a commit
checkpoint changes; and at Milestone or Final acceptance. Record concise state
transitions, condition-linked evidence, known failures or exceptions, and the
next action. Do not keep a command transcript or reconstruct unsupported
history.

Every reusable evidence item names the conditions it supports and retains a
reproducible method, relevant repository state, observed result or durable
artifact, and material limits. One item may support several conditions.
Delivery status, commit text, and acceptance reports locate evidence but do not
prove the implementation claim.

Reuse evidence when the relevant code, tests, rules, contract, and repository
snapshots are unchanged. When later work changes a reviewed authority, mark
the affected evidence and conditions invalid without discarding unaffected
records. Revalidate changed scope at the next relevant boundary or Final.
Rerun evidence when relevance or reproducibility is uncertain. Retain the
completed document unless another approved retention rule applies.

When a material Goal change is approved, update Current approval, the complete
current Approved Contract, affected status, repository states, and the Goal
Change Record in one atomic write. Keep Initial approval unchanged.
