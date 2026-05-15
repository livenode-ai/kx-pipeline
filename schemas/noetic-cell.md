# Noetic Cell Schema

A Noetic Cell is livenode-kx's core note format for insight, decision, and synthesis notes. It turns raw material into an atomic claim that can be read quickly, connected reliably, and revisited later.

## Structure

### 主張（Claim）

The central claim of the note in 1-2 sentences. This is the minimum readable unit: an agent should be able to understand what the note contributes by reading this section alone.

Use this section for the answer, stance, hypothesis, decision, or question that the note preserves.

### 根拠（Evidence）

The reasoning behind the claim: qualitative logic, causal explanation, observed patterns, or source-grounded rationale.

Use this section when the note needs to explain why the claim is credible or why the decision was made.

### データ（Data）

Quantitative facts, tables, cited references, measurements, or other source-backed data.

Use this section only when concrete data exists. If the source does not contain data, omit the section rather than inventing support.

### 制約（Constraints）

The conditions, limits, exceptions, or boundaries under which the claim holds.

Use this section when the original source states explicit limitations, dependencies, unresolved issues, or scope boundaries. Do not add speculative constraints.

### 接続（Links）

Wikilinks to related notes, with the relationship stated clearly: extends, grounds, contradicts, exemplifies, reframes, depends_on, or similar.

Use this section to make the note part of the knowledge graph. Every mature note should connect to at least one other note or domain map.

## Section Requirements by Note Type

- `insight`, `decision`, and `synthesis` notes should use the full Noetic Cell structure when possible: 主張, 根拠, データ, 制約, 接続.
- `データ（Data）` may be omitted when no data exists in the source.
- `制約（Constraints）` may be omitted when no explicit constraints exist in the source.
- `idea` and `question` notes may use only `主張（Claim）` and `接続（Links）` when the thought is still early-stage.
- `tension` notes should include `主張（Claim）`, `根拠（Evidence）`, `制約（Constraints）`, and `接続（Links）` when the contradiction or tradeoff needs explanation.

## Staged Reading Protocol

Agents should read notes in stages instead of full-reading everything.

1. Scan filenames, frontmatter `description`, `type`, `domain`, and `topics`.
2. Grep for `## 主張（Claim）` across candidate notes to identify the relevant claims first.
3. Read `## 接続（Links）` to understand graph position and cross-domain relevance.
4. Full-read the note only when the claim is relevant, the evidence is needed, or the note is a connection hub.
5. Prefer domain maps and `CLAIMS_INDEX.md` for broad orientation before reading individual notes.

This protocol keeps agent context small while preserving access to deeper reasoning when needed.

## Quality Gates

Before saving a Noetic Cell, check:

1. The title is a claim, not a label.
2. `description` adds mechanism, scope, or implication beyond the title.
3. Frontmatter includes `type`, `domain`, `created`, and `topics`.
4. `topics` includes at least one domain map wikilink.
5. `主張（Claim）` is atomic and understandable without reading the whole note.
6. `根拠（Evidence）` explains why, not just what.
7. `データ（Data）` contains only real source-backed facts.
8. `制約（Constraints）` contains only explicit limits from the source.
9. `接続（Links）` names relationships, not vague "related" links.
10. The body develops the title instead of restating it.
