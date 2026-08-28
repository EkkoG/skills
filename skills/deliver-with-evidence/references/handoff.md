# Handoff

Use only when another agent or session needs an explicit execution handoff.
Delivery remains the authoritative contract, status, and evidence record; the
handoff points to it and records only what the recipient needs to resume safely.

```markdown
Recipient and scope:
<Who should continue and the bounded responsibility being transferred>

Delivery document:
<Exact authoritative path>

Stable repository states:
<Each relevant root, HEAD or commit checkpoint, and concise worktree state>

Current position:
<Current Slice, Work Package or boundary, and exact status>

Material deltas or limitations:
<Only changes, blockers, permission limits, invalidated evidence, or risks not obvious from Delivery>

Resume action:
<Exact first action, including any state revalidation or permission needed>
```

Do not duplicate the approved contract, evidence matrix, completed-Slice list,
or full status history already maintained in Delivery.
