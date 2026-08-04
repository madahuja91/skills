---
name: gate-tsa-epic-story-readiness
description: Quality gate for TSA epic_story_seeds Markdown. Use when Completeness Validator evaluates that artifact.
---

# Gate: gate-tsa-epic-story-readiness

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Pass requires

- Schema-valid artifact for `epic_story_seeds Markdown`
- Stack claims cite ADR; baseline cites CSA
- No invented technologies
- Blocking gaps listed when unresolved ADR decisions block design

Emit report with `gate_id: gate-tsa-epic-story-readiness`.
