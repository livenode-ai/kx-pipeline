# livenode-kx

livenode-kx is a portable knowledge transformation toolkit for Claude Code and Obsidian-style vaults.

## Structure

- `skills/`: Claude Code skills for capture, distillation, health checks, and references.
- `schemas/`: Validation schemas for config and generated knowledge files.
- `templates/`: Generic starter files users can copy into their vaults.
- `example-vault/`: Clean sample vault used for docs and tests.
- `docs/`: Contributor and user documentation.
- `tests/`: Validation and regression checks.

## Working Rules

The `skills/` files are the primary deliverable. Changes there affect all users, so keep edits intentional and testable.

Test schema and example-vault changes with:

```sh
python3 tests/validate_schema.py example-vault/notes
```

Skills must be vault-agnostic. Do not hardcode local paths, usernames, personal data, or domain names.
