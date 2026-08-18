# Reusable Execution Text Templates

Use only the sections proportional to the task. Keep project-specific documents
authoritative when they already cover the same information.

## Plan Requirements

Every plan must state:

- an observable final outcome;
- scope, boundaries, and explicit non-goals;
- reviewable work packages in dependency order;
- acceptance conditions for the work packages and whole goal;
- a stable ID or unique label for every required acceptance condition.

If these requirements are missing, report the exact gaps and hand planning to
`$design-delivery-plan`. Do not complete or repair the plan from this skill.

Every evidence item must name the acceptance condition or conditions it covers.
One item may cover multiple conditions, and the format may remain ordinary
Markdown. Before Milestone or Final completion, list every required condition
that still lacks current evidence.

Add only what the task requires:

- external compatibility promises when behavior, data, or workflows must stay
  stable;
- target architecture and responsibility boundaries for architecture work;
- intentional removals and negative migration evidence when replacing an old
  implementation, authority, dependency, fallback, or side effect;
- known exceptions, their impact, and removal conditions when unfinished or
  forbidden paths must temporarily remain.

Do not require a fixed format, determine every file or function in advance,
invent migration content for unrelated work, or demand machine evidence for
every acceptance condition.

Record and obtain approval before implementing a material change to:

- the final outcome;
- external compatibility promises;
- required work packages;
- whole-goal acceptance conditions;
- an intentional removal that would instead remain supported;
- a blocking condition that would become non-blocking.

Substantial plan changes belong to `$design-delivery-plan`. This skill may
record the approved result but must not design or self-approve it.

## Delivery Checkpoint

```markdown
# Delivery Checkpoint

- Plan: `<path>`
- Goal status: partial
- Current Slice: `<ID>`
- Based on HEAD: `<commit>`
- Worktree: `<clean, or concise dirty paths>`

## Completed

- <Completed work package or Slice>

## Evidence

- PASS [G-01] `<command>`
  - Proves: <Behavior or condition>
- REVIEW [G-02, WP-04-03] <Boundary or quality>
  - <Conclusion and relevant paths>

## Missing evidence

- <Required condition with no current evidence, or none>

## Known failures or exceptions

- <Existing failure, baseline, or approved exception>

## Next

<Exact next action>
```

## Goal Change Record

Use this only to record a material change that has already been planned,
reviewed, and explicitly approved. It is not a substitute for planning.

```markdown
# Goal Change: <Decision>

Original condition:
<Previous target or acceptance rule>

Reason:
<New evidence or constraint>

Replacement condition:
<New target>

Removed or changed acceptance:
<Exact conditions>

Risk:
<What becomes weaker or different>

Approval:
<User or governing decision>

Status impact:
<Why this does or does not change completion>
```

After approval, create this record before implementing against the changed
target.

## Handoff

```markdown
Completed scope:
<Exact local result>

Incomplete scope:
<Anything not done>

Legacy paths still present:
<Wrappers, duplicate authorities, or compatibility code>

Positive verification:
<New-path evidence>

Negative verification:
<Old-path absence evidence>

Known failures or exceptions:
<Exact items>

Cross-module risks:
<Seams requiring review>

Next action:
<Exact continuation point>
```

## Acceptance Report

```markdown
# Acceptance

| Requirement | Status | Code evidence | Verification | Exception |
|---|---|---|---|---|
| <ID> | verified/partial | <Path or symbol> | <Result> | <ID or none> |

Goal changes reviewed:
<None, or decision records>

Architecture and dependency review:
<Added, removed, and remaining edges>

Legacy authority review:
<What no longer controls behavior and what still does>

Compatibility review:
<External compatibility versus unfinished internal migration>

Verification summary:
<Smoke, targeted, negative, architecture, regression, and hygiene>

Status:
- Slice: complete/partial
- Milestone: complete/partial
- Phase: complete/partial
- Goal: complete/partial

Blocking items:
<Exact unresolved requirements>
```

## Commit Body

```text
Problem / Feature:
<Current problem or capability>

Solution:
<Implementation and boundaries>

Compatibility:
<Preserved and changed external behavior>

Verification:
<Positive, negative, targeted, and integration checks>

Remaining:
<Explicitly incomplete work>
```
