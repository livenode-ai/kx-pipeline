# Key Concepts

Three ideas power livenode-kx. You don't need to understand all of them to start — but they explain why the system works the way it does.

---

## 1. Noetic Cell

A Noetic Cell is a structured 5-section note. It's the core unit of knowledge in livenode-kx.

```markdown
## 主張（Claim）
The core assertion in 1-2 sentences.

## 根拠（Evidence）
Why this is true — logic and qualitative reasoning.

## データ（Data）
Quantitative data, tables, cited facts.
(Omit this section if no data exists)

## 制約（Constraints）
The conditions under which this claim holds. Limits and boundaries.
Only what the source explicitly states — never AI-inferred.

## 接続（Links）
[[Wikilinks]] to related notes with relationship type:
extends | grounds | contradicts | exemplifies
```

**Why 5 sections?**

Because AI can read the Claim section in 2 lines and decide whether the full note is relevant. Without structure, reading one note to check relevance costs the same as reading it to extract knowledge. With Noetic Cells, you get staged reading:

1. Read `CLAIMS_INDEX.md` — all claims in one file (generated automatically by `/kx` Phase 6)
2. `grep "## 主張" note.md -A 3` — 2-line claim check
3. Full `Read` — only when you need evidence or data

This staged reading reduces context consumption by an estimated ~85% on a 500-note vault compared to naive full-text retrieval (based on reading 2-line claims vs. full notes averaging 50+ lines).

**Which note types use it?**

| Type | Sections required |
|---|---|
| `insight` | All 5 |
| `decision` | All 5 |
| `synthesis` | All 5 |
| `idea` | 主張 + 接続 only |
| `question` | 主張 + 接続 only |
| `tension` | 主張 + 接続 only |

---

## 2. Mining vs Summarizing

The `/kx` pipeline is built around a specific philosophy: **Mining, not Summarizing.**

**Summarizing** compresses a source into a shorter version. Information is lost. The output is useful for recall, not for connection.

**Mining** extracts every independent idea as a separate, atomic note. No compression — just separation. Each note has one claim and stands on its own.

Why it matters:

- A voice memo about a client meeting might contain 4 independent insights. Summarizing produces one note that can only be linked as a whole. Mining produces 4 notes that can each connect to different parts of your graph.
- Cross-domain connections only emerge when ideas are atomic. "The cycling event model proves the consulting hypothesis" is a connection between two atomic notes — it can't form if they're bundled in a summary.

**The extraction rule:** "Would a future session be better off having this as a searchable note?" If yes, extract it. "I already know this" is not a reason to skip.

---

## 3. Weight vs Distance (Capability Declaration Protocol)

Standard RAG retrieves by **semantic distance** — vector similarity between your query and your notes. The closest vectors win.

livenode-kx introduces a different signal: **domain weight**.

Every note has an optional `domain_weight` field (0.0–1.0) in its frontmatter. This represents the note owner's confidence and expertise level for that claim — not how semantically similar it is to a query.

The Capability Declaration Protocol extends this idea to node-to-node connections. When a livenode-kx vault responds to a query, it can package the `domain_weight` alongside other signals into a structured declaration — think of it as metadata about how confident the knowledge source is, before the actual answer is delivered:

```json
{
  "answer": "L1 response",
  "noetic_cells": 47,
  "domain_weight": 0.9,
  "connectable_axes": ["cycling-tourism", "municipal-consulting"],
  "coverage": "core"
}
```

Before a livenode-kx-equipped AI answers a query, it can "declare" what it knows and how confidently — like a TCP handshake before content transfer. The AI that receives this declaration can decide whether the coverage is sufficient, or whether to fetch additional context.

**Current status:** `domain_weight` is a schema field (see `schemas/note-frontmatter.yaml`). The routing logic is not yet implemented — it's tracked as a future issue. The concept is documented here because it explains the design direction of the schema.
