---
name: gate-epic-story-readiness
description: Final gate ensuring functions/epics/stories Markdown seeds are CSA-traceable before epic generation. Use after epic_story_seeds Markdown files are written.
---

# Gate: Epic/Story Readiness

## Schema

Authoritative evaluation contract: [`schema.json`](schema.json)

Markdown seed structure: `skills/standards/epic-story-mapping/schema.json`.

## Pass requires

- `functions.md`, `epics.md`, `stories.md` present
- Every Function ≥1 Epic; every Epic has CSA refs; every Story has capability, trace IDs, AC hooks
- No critical unresolved in-scope gaps

Emit `gate_id: gate-epic-story-readiness`.
