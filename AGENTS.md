# AGENTS.md

livenode-kx is a portable knowledge transformation toolkit for Claude Code and Obsidian-style vaults.

Primary files to understand:

- `skills/*/SKILL.md`
- `schemas/`
- `livenode-kx.config.yaml`

Key constraint: `example-vault/` must stay clean and generic. Do not add real personal data, usernames, private paths, or domain-specific notes.

Return protocol:

```text
Task:     What you did in one line
Diff:     Changed files and key points only
Decision: Decisions made and why
Risk:     Uncertain points or unresolved issues
Next:     What needs human review
```
