#!/usr/bin/env python3
"""Validate livenode-kx note frontmatter in a notes/ directory."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = ["description", "type", "domain", "created", "topics"]
ALLOWED_TYPES = {"idea", "insight", "decision", "question", "tension", "synthesis"}


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value in {"", "[]"}:
        return [] if value == "[]" else ""
    if value.startswith("[") and value.endswith("]"):
        try:
            return ast.literal_eval(value)
        except (SyntaxError, ValueError):
            inner = value[1:-1].strip()
            return [] if not inner else [item.strip() for item in inner.split(",")]
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_frontmatter(raw: str) -> tuple[dict[str, Any] | None, str | None]:
    lines = raw.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing opening frontmatter delimiter"

    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break

    if end_index is None:
        return None, "missing closing frontmatter delimiter"

    frontmatter_text = "\n".join(lines[1:end_index])

    try:
        import yaml  # type: ignore

        data = yaml.safe_load(frontmatter_text) or {}
        if not isinstance(data, dict):
            return None, "frontmatter is not a YAML mapping"
        return data, None
    except ImportError:
        pass
    except Exception as exc:  # pragma: no cover - depends on optional PyYAML
        return None, f"invalid YAML frontmatter: {exc}"

    data: dict[str, Any] = {}
    for line_number, line in enumerate(frontmatter_text.splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not match:
            return None, f"unsupported frontmatter line {line_number}: {line}"
        key, value = match.groups()
        data[key] = parse_scalar(value)

    return data, None


def is_empty(value: Any) -> bool:
    return value is None or value == "" or value == []


def validate_file(path: Path) -> tuple[str, list[str]]:
    data, error = parse_frontmatter(path.read_text(encoding="utf-8"))
    if error:
        return "FAIL", [error]
    assert data is not None

    if data.get("type") == "moc":
        return "WARN", ["skipped domain map (type: moc)"]

    failures: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in data or is_empty(data[field]):
            failures.append(f"missing required field: {field}")

    note_type = data.get("type")
    if note_type and note_type not in ALLOWED_TYPES:
        failures.append(
            f"invalid type: {note_type!r}; expected one of {', '.join(sorted(ALLOWED_TYPES))}"
        )

    description = data.get("description")
    if "description" in data:
        if not isinstance(description, str) or not description.strip():
            failures.append("description must be a non-empty string")
        elif len(description) >= 200:
            failures.append("description must be under 200 characters")

    return ("FAIL", failures) if failures else ("PASS", ["schema ok"])


def main() -> int:
    default_notes = Path(__file__).resolve().parent.parent / "example-vault" / "notes"
    target = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else default_notes
    target = target.resolve()

    if not target.exists() or not target.is_dir():
        print(f"FAIL {target}: target notes directory does not exist")
        return 1

    markdown_files = sorted(target.glob("*.md"))
    if not markdown_files:
        print(f"WARN {target}: no markdown files found")
        return 0

    has_failures = False
    for path in markdown_files:
        if path.name == "CLAIMS_INDEX.md":
            print(f"SKIP {path.relative_to(target)}: generated index file")
            continue
        status, messages = validate_file(path)
        if status == "FAIL":
            has_failures = True
        print(f"{status} {path.relative_to(target)}: {'; '.join(messages)}")

    return 1 if has_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
