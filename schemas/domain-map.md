# Domain Map Schema

A domain map is a Map of Content (MOC) file for one livenode-kx domain. It gives agents and humans a stable entry point into all notes that belong to that domain.

## Rules

- A domain map lists all notes belonging to a domain via `[[wikilinks]]`.
- Its frontmatter must include `type: moc`.
- Naming convention: `{domain-name}-map.md`, for example `cycling-tourism-map.md`.
- Domain maps are excluded from health checks and orphan detection.
- Domain maps should be referenced from note frontmatter `topics`.

## Cross-Domain Connections

Cross-domain connections are the most valuable links in livenode-kx.

When a note links to two different domain maps, it represents knowledge synthesis across domains. These notes should be treated as high-value graph bridges because they often reveal reusable patterns, strategic insight, or decisions that only become visible when two domains are compared.

## Template

```markdown
---
type: moc
domain: [your-domain]
description: "Map of all notes in the {domain} domain"
---

# {Domain} Map

## Core Claims
- [[your-first-note]]
- [[your-second-note]]

## Sub-domains (optional)
```
