---
name: commit
description: Inspect local changes and create focused, reviewable Git commits. Use automatically after completing and verifying implementation work in a Git repository when the current task's changes form a coherent commit; also use when the user explicitly asks to commit. Do not use for read-only work, planning or review, intentionally partial or failing work, non-Git workspaces, or push or pull-request-only requests.
---

# Commit Changes

Create one or more local commits that are independently understandable and
verifiable. Commit only; never push, create a branch, or open a pull request
unless the user separately requests it.

When invoked automatically, commit only completed and verified changes owned by
the current task. Do not create a checkpoint commit for partial work, include
unrelated changes, or commit when the user or repository instructions require
the worktree to remain uncommitted. If the current-task changes cannot be
safely isolated, leave them uncommitted and report the boundary.

## Workflow

1. Inspect `git status --short`, staged and unstaged diffs, and recent commit
   subjects before staging anything.
2. Determine the intended scope from the user's request. Preserve unrelated
   user changes. If ownership of a changed file is ambiguous, ask before
   staging it.
3. Choose a practical commit shape. Prefer one commit for a single coherent
   change. If the diff contains clearly independent concerns, briefly suggest
   a useful split, usually two or three commits, before staging. Treat this as
   a recommendation: do not insist, block the commit, or over-split when the
   user prefers one commit or the review benefit is marginal. Never split
   merely by file type.
4. Run the relevant available checks for each commit group. Report failures or
   checks that could not be run; never hide or bypass commit hooks.
5. Stage explicit paths for the current group. Do not use `git add .`,
   `git add -A`, or `git add --all` when the worktree contains mixed changes.
6. Review `git diff --cached` before committing. Follow the repository's recent
   commit-message convention; if none is clear, use a concise imperative
   subject.
7. Add a body when context is useful:
   - For a bug fix, explain the problem or root cause and the solution.
   - For a feature, explain the capability and the implementation approach.
   - Mention meaningful validation, compatibility concerns, or tradeoffs.
8. After committing, report each commit hash and subject, the validation run,
   and any remaining uncommitted changes.

Do not amend, rewrite history, or include unrelated changes unless the user
explicitly asks for that operation.
