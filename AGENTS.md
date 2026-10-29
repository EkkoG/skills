# Synchronization

- Synchronization defaults to full mode. Run `scripts/sync-skills.sh` or its
  explicit equivalent `scripts/sync-skills.sh --full` using the configured local
  skills, agents, and user-instructions sources.
- Mirror complete agent TOML files, including model, reasoning effort,
  permissions, and instructions. Source overrides must point to the user's
  requested source; isolated fixtures may override sources for tests.
- When remote synchronization is requested, mirror all four maintained skills,
  all agent files, and `user-AGENTS.md` from this repository into their installed
  locations. Verify the complete maintained file set and contents, including
  models, rather than only the current diff. Limit removals to the maintained
  skill directories and agents directory.
- The synchronization scope excludes `config.toml`, credentials, plans,
  Delivery records, and sessions. Publishing still follows the user's request.
