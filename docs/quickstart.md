# Quick Start

Get from zero to your first `/kx` run in under 5 minutes.

## Requirements

- [Claude Code](https://claude.ai/code) installed and authenticated
- A directory of Markdown files (your vault) — Obsidian, Logseq, or any folder

---

## TL;DR (3 commands)

```bash
cp -r /path/to/livenode-kx/skills/ /path/to/your-vault/.claude/skills/
cp /path/to/livenode-kx/livenode-kx.config.yaml /path/to/your-vault/
cp /path/to/livenode-kx/templates/CLAUDE.md.template /path/to/your-vault/CLAUDE.md
```

Then open your vault in Claude Code and run `/kx`.

---

## Step-by-Step

### Step 1: Copy skills into your vault

```bash
cp -r /path/to/livenode-kx/skills/ /path/to/your-vault/.claude/skills/
```

This installs the 4 commands (`/kx`, `/distill`, `/health`, `/ref`) into your Claude Code project settings.

### Step 2: Copy and configure

```bash
cp /path/to/livenode-kx/livenode-kx.config.yaml /path/to/your-vault/
```

Open `livenode-kx.config.yaml` and edit:

```yaml
domains:
  - name: "my-domain"        # e.g., "product-design"
    map: "my-domain-map"     # e.g., "product-design-map"
    description: "What this domain covers"
```

Everything else works with defaults.

### Step 3: Set up your CLAUDE.md

```bash
cp /path/to/livenode-kx/templates/CLAUDE.md.template /path/to/your-vault/CLAUDE.md
```

Fill in the `[PLACEHOLDER]` sections — your name, your vault's purpose, your active goals.

### Step 4: Create your first inbox item

Create `your-vault/00_Inbox/first-capture.md` with any text:

```markdown
Had a realization today — the reason our onboarding takes so long isn't complexity,
it's that every team member explains it differently. We need a canonical version.
Also, the pricing page confusion keeps coming up in sales calls. Related?
```

### Step 5: Run /kx

Open your vault directory in Claude Code (or run `claude` in the terminal from your vault directory) and type:

```
/kx
```

You'll see:

```
Found 1 file in inbox. Starting KX pipeline.

## KX Complete

- Sources processed: 1
- Notes created: 2
- Connections found: 1 (cross-domain: 0)
- Quality check: PASS

### Created Notes
- [[onboarding-inconsistency-signals-missing-canonical-process]] — insight
- [[pricing-page-confusion-correlates-with-sales-friction]] — idea

### Next Actions
- (none found in this source)
```

Your notes are now in `notes/`, structured and linked. `notes/CLAIMS_INDEX.md` has been generated.

---

## What to Do Next

1. **Run `/distill`** at the end of your first session — this creates a handover and updates `BRIEFING.md`.
2. **Run `/health`** after accumulating 20+ notes — checks for orphans and schema drift.
3. **Use `/ref`** when you want to ask a question against your knowledge base.
4. **Start `AESTHETIC.md`** — copy `templates/AESTHETIC.md.template` to your vault root and add your first YES/NO patterns.

---

## Troubleshooting

**`/kx` says "Inbox is empty"**
Make sure your file is in `00_Inbox/` (or the path set in `livenode-kx.config.yaml → vault.inbox`) and ends in `.md`.

**Notes aren't getting connected**
Phase 3 (Connect) links new notes to existing ones. On your first run with no existing notes, connections will be minimal. Run `/kx` again after accumulating 10+ notes.

**`/distill` fails on Todoist step**
Set `integrations.todoist: false` in your config (it's already `false` by default). Only enable if you have Todoist MCP configured.
