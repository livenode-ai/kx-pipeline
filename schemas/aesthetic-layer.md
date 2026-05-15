# Aesthetic Layer Schema

`AESTHETIC.md` is a judgment calibration log in the livenode-kx system. It captures the owner's taste, judgment axis, and sense of what "feels right" so AI output can become less generic and more owner-authentic over time.

## AESTHETIC.md vs CLAUDE.md

- `CLAUDE.md` = instructions and rules for the AI: what to do.
- `AESTHETIC.md` = the owner's judgment axis and aesthetic sense log: how to align with the owner's taste.

## Purpose

The purpose of `AESTHETIC.md` is to capture the delta between what AI outputs and what the human considers correct, authentic, or tasteful.

Over time, this builds a calibration layer that reduces the gap between generic AI output and owner-authentic output. It is especially useful for voice, framing, product judgment, copy, design preference, and strategic taste that cannot be fully expressed as static rules.

## Structure

### NO Patterns

AI-generic outputs the owner rejects.

Record patterns that feel wrong, too generic, too polished, too corporate, too verbose, too clever, too cautious, or otherwise misaligned with the owner's judgment.

### YES Patterns

Outputs the owner considers authentic.

Record phrasing, framing, structure, decisions, examples, or tonal moves that the owner says feel right.

### Delta Log

Specific calibration instances with date, AI output, what was wrong, and correction.

Recommended entry format:

```markdown
## YYYY-MM-DD

- AI output: [what the AI produced]
- What was wrong: [why it missed the owner's judgment]
- Correction: [what would have felt right]
```

## How It Accumulates

1. During a session, the owner says "that's not right" or "that's exactly right."
2. During `/distill` Step 3.5, the AI appends the calibration point to `AESTHETIC.md`.
3. Over time, `AESTHETIC.md` becomes a calibration reference for all AI interactions.

## Trigger Phrase

When the owner says `判断軸に追記して`, append the relevant calibration point to `AESTHETIC.md`.
