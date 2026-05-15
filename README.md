# livenode-kx

> Give AI your judgment, not just your notes.

AI memory remembers what you know.  
livenode-kx preserves how you decide.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude-Code-blueviolet)](https://claude.ai/code)
[![日本語](https://img.shields.io/badge/lang-日本語-red.svg)](README_JP.md)

**[~85% context reduction](docs/concepts.md#1-noetic-cell) · 5 min setup · Works with Obsidian, Logseq, or any Markdown folder**

> *Reduction is estimated on a 500-note vault by reading only 2-line Claim sections vs. full ~50-line notes. See [concepts.md](docs/concepts.md) for the calculation.*

---

## What is livenode-kx?

livenode-kx is a 4-command Knowledge Transformation pipeline for Claude Code.

Drop a voice memo or quick note into `00_Inbox/`, run `/kx`, and get back a structured knowledge graph — Noetic Cell notes with 2-line Claim sections your AI reads instead of the full 50-line note. Run `/distill` at the end of a session and every decision you made gets persisted to `BRIEFING.md`, so your next session starts with full context. Over time, your AI stops producing generic output and starts producing output calibrated to the way you think.

**Works with Obsidian, Logseq, or any Markdown folder. No proprietary format. Your notes stay yours.**

---

## The Problem

Your knowledge exists. The AI can retrieve it.

But retrieval doesn't tell the AI *why* you make certain choices — what you'd accept, what you'd reject, how you reason about tradeoffs in your domain. So the output is 80-90% right, and you spend the remaining time correcting it.

That correction time isn't a skill issue. It's a structural gap: the AI has access to what you know, but not to how you decide. livenode-kx closes that gap by making your judgment persistent and accessible.

---

## How It Works

Most AI memory tools form a 2-layer system:

```
[Your Notes] ─────────────────────────→ [LLM]
              semantic distance            generic output
```

livenode-kx adds the missing judgment layer:

```
[Your Notes / External KB]
         │
         ▼
┌─────────────────────────────┐
│   Judgment Layer            │  ← livenode-kx
│                             │
│  • Structured claims        │
│    (Noetic Cell, staged)    │
│  • Decision history         │
│    (BRIEFING.md)            │
│  • YES/NO patterns          │
│    (AESTHETIC.md)           │
│  • Active context           │
│    (CLAIMS_INDEX)           │
└─────────────────────────────┘
         │
         ▼
    [LLM output]
    calibrated to your reasoning
```

Tools like mem0, MemGPT, and Zep solve retrieval — what you know. livenode-kx solves judgment — how you decide. They're complementary, not competing.

---

## Lifecycle — the 4 commands only work as a loop

`/kx` and `/distill` are not standalone utilities. They are **two halves of the cycle that accumulates judgment over time.**

```
                ┌──────────────────────────────────┐
                │                                  │
   ① You make decisions in a session              │
        │                                          │
        ▼                                          │
   ② /distill                                      │
       writes a handover into 00_Inbox/            │
       updates BRIEFING / VISION /                 │
       AESTHETIC / MEMORY                          │
        │                                          │
        ▼                                          │
   ③ /kx                                           │
       refines handovers in 00_Inbox/              │
       into Noetic Cell notes                      │
       saves atomic notes to notes/                │
       rebuilds CLAIMS_INDEX                       │
        │                                          │
        ▼                                          │
   ④ Next session calls /ref                       │
       enters via CLAIMS_INDEX, staged reading     │
       loads prior judgment as full context        │
        │                                          │
        └──────────────────────────────────────────┘
                back to ①
```

**The loop is the value.** Running `/distill` alone just piles up handovers. Running `/kx` alone never receives your decision history. Run both every session and your notes become a structured record of your judgment, not just your knowledge.

File destinations (BRIEFING.md / VISION.md / AESTHETIC.md / MEMORY.md) are configurable in `livenode-kx.config.yaml` under `distill:`. Defaults are at vault root; PARA users can set patterns like `01_Projects/{project}/BRIEFING.md`.

---

## The 4 Commands

| Command | What it does |
|---|---|
| `/kx` | Raw captures → structured Noetic Cell notes (5-phase pipeline) |
| `/distill` | Session → handover → BRIEFING update → AESTHETIC calibration |
| `/health` | Monthly vault check: schema, orphans, broken links, map balance |
| `/ref` | Staged reading via CLAIMS_INDEX — survey 500 notes in seconds |

---

## Quick Start

**Requirements:** [Claude Code](https://claude.ai/code) installed · A Markdown vault directory

### TL;DR (3 steps)

```bash
cp -r livenode-kx/skills/ /path/to/your-vault/.claude/skills/
cp livenode-kx/livenode-kx.config.yaml /path/to/your-vault/
cp livenode-kx/templates/CLAUDE.md.template /path/to/your-vault/CLAUDE.md
```

Open your vault in Claude Code and type `/kx`.

### Full setup (~5 minutes) → [docs/quickstart.md](docs/quickstart.md)

---

## Key Concepts

- **[Noetic Cell](docs/concepts.md#1-noetic-cell)** — why 5 sections beat flat text for AI retrieval (85% context reduction)
- **[Mining vs Summarizing](docs/concepts.md#2-mining-vs-summarizing)** — the philosophy behind `/kx`
- **[Judgment Layer](docs/architecture.md)** — the 3-layer architecture in depth

---

## Vault Compatibility

| Environment | Support |
|---|---|
| Obsidian vault | ✅ Full (local file ops) |
| Obsidian + MCP | ✅ Set `obsidian_mcp: true` in config |
| Any Markdown folder | ✅ Full |
| Logseq | ✅ Works (flat Markdown mode) |
| Cloudflare Artifacts | 🔜 Coming soon |

---

## Contributing

See [.claude/rules/contributing.md](.claude/rules/contributing.md).

Core invariant: **skills must be vault-agnostic.** No hardcoded paths, usernames, or domain names.

---

## License

MIT © livenode-kx contributors
