# Handoff

Use when execution continues in another coordinating session. Delivery records
the approved plan source, current contract, status and evidence; the handoff
points to it and records only what the next Main needs to resume safely.
Send this handoff as a message by default. Save a separate file only when needed
for recovery or explicitly requested; reference existing durable sources.
Continue within the current session using its existing context and relevant
deltas. Transfer coordination only after the previous Main has stopped writing.

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
