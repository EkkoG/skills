# Delivery Document

Use this reference only when initializing or maintaining the private Delivery
document. Keep authoritative project documents authoritative and copy only the
contract and state needed for reliable resumption and acceptance.

```markdown
# Delivery Document

- Workspace: `<repository or target workspace root>`
- Repository key: `<safe basename>-<root hash prefix>`
- Goal: `<approved Goal title>`
- Goal ID: `<safe slug>-<generated short random suffix>`
- Delivery path: `<exact persistent path>`
- Plan source: `<path, conversation, issue, or other authority>`
- Initial approval: `<first approval boundary and date; never rewritten>`
- Current approval: `<latest approval boundary and date>`
- Goal status: partial
- Current Slice: `<ID, or none>`
- Slice status: `<in progress, blocked, or none>`
- Based on HEAD: `<commit or not applicable>`
- Worktree: `<clean, concise dirty paths, or non-Git baseline>`

## Approved Contract

- Final outcome: <Current externally observable Goal>
- Scope and boundaries: <Current required work and authority limits>
- Non-goals: <Current stable exclusions>
- Work Package order: <Stable IDs in dependency order>
- Required acceptance: <Every current Goal and Work Package label>
- Material decisions and architecture: <Only current decisions execution must preserve>
- Compatibility and removals: <Current promises, removals, and negative obligations, or none>
- Risks, assumptions, and exceptions: <Only material current resume context>

### `<WP-ID>`

- Status: <pending, in progress, blocked, or complete>
- Outcome: <Reviewable result>
- Owned scope: <Responsibilities or surfaces included>
- Must not expand into: <Stable exclusions>
- Implementation boundary: <Authority, data flow, or behavioral constraint>
- Dependencies: <Earlier Work Packages or none>
- Acceptance: <Stable labels owned by this Work Package>
- Compatibility, removals, and risks: <Only current applicable details>

## Current Slice Contract

- Why now: <Selection reason>
- Covers: <Stable acceptance labels>
- Local outcome: <One reviewable result>
- Preserved behavior: <External promises or boundaries>
- Expected scope: <Relevant responsibility or authority>
- Exit evidence: <Checks or review needed to finish>

## Completed

- `<Slice ID>` <Completed result and covered labels>

## Slice Transitions

- `<old pointer> -> <new pointer>` at `<commit>`: <Short reason>

## Goal Change History

- <References or embedded Goal Change Records, or none>

## Evidence

- PASS [G-01] `<command or observation>`
  - Observed: <What was established>
  - Supports: <Condition within that observation>
  - Limits: <Material claims this does not establish>
  - State: <HEAD or other relevant state>
- REVIEW [G-02, WP-04-03] <Boundary or quality>
  - Observed: <Conclusion and relevant paths>
  - Counterexample checked: <Plausible incomplete state and result>

## Missing evidence

- <Required condition with no current evidence, or none>

## Known failures or exceptions

- <Existing failure, baseline, or approved exception>

## Resume

<Exact continuation point, or where to re-evaluate when no Slice is active>
```

The Approved Contract always describes the complete current target. When a
material Goal change is approved, update that contract and affected state in
the same atomic write that appends the historical Goal Change Record. A reader
must not need to merge history to determine what is currently approved.

Generate a Goal ID once and retain the exact path. Omit optional fields and the
current Slice contract when they do not apply. Record transitions only for
selection, completion, blocking, resumption, or invalidation; do not use them
as an activity log or reconstruct unsupported history.

When the plan has a durable source, link it and copy only resume-critical
details. For a conversation-only plan, retain enough readable contract detail
to resume every Work Package without guessing while avoiding unnecessary
design prose.
