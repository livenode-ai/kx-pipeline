# Contributing to livenode-kx

## Core Invariant

**Skills must be vault-agnostic.** No hardcoded paths, usernames, domain names, or user-specific tool names.

If you find yourself writing `/Users/someone/` or `cycling-tourism-map` in a skill file, stop. Move it to `livenode-kx.config.yaml` instead.

## What to Contribute

- **Skill improvements** — better phrasing, clearer phase descriptions, edge case handling
- **Schema additions** — new frontmatter fields with rationale
- **Example vault content** — more realistic sample notes (must be generic/fictional)
- **docs/** — concept explanations, architecture updates
- **tests/** — more validation rules in `validate_schema.py`

## What Not to Contribute (yet)

- New skills beyond the core 4 — open an issue first to discuss
- Cloudflare / iOS integration code — separate repos
- Domain-specific templates (cycling, consulting, etc.) — these belong in user vaults, not here

## Skill Modification Guidelines

When editing a `skills/*/SKILL.md`:

1. Keep the YAML frontmatter `allowed-tools` minimal — only what the skill actually needs
2. Never reference Obsidian MCP tools as required — they're optional (config flag)
3. Test your change against `example-vault/` by running the skill with Claude Code
4. Run `python3 tests/validate_schema.py example-vault/notes/` to verify example vault passes

## Schema Evolution

Adding a new frontmatter field:
1. Add it to `schemas/note-frontmatter.yaml` with description and `required: false`
2. Add it to the quality gate in `skills/kx/SKILL.md` if it should be validated
3. Add validation to `tests/validate_schema.py` if it's required
4. Update `example-vault/notes/` sample note to include the field

## Commit Style

```
feat: add X to /kx Phase 2
fix: health diagnostic 4 map detection on non-standard vaults
docs: clarify Noetic Cell usage for question type notes
```

## PR Checklist

- [ ] `python3 tests/validate_schema.py example-vault/notes/` passes
- [ ] No hardcoded paths or usernames in skill files
- [ ] `livenode-kx.config.yaml` updated if new config options added
- [ ] `schemas/` updated if frontmatter changed
