---
name: SK-TARGET
description: >-
  Map gap register items to Target State epics/stories with legacy mapping,
  ADR refs, TSA components, and migration impact.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)


# SK-TARGET — Target Story Mapping

## Inputs
- gap_register, tsa_analysis, adr_decisions
- CS stories for legacy mapping

## Outputs
- `artifacts/ts/ts_stories.json` — **required** (each story includes **`epic_id`**)
- Nested Markdown — **required**:
  - `artifacts/ts/epics/<EPIC-ID>/stories/<STORY-ID>.md`
- Use with SK-EPIC for `ts_epics.json` + `artifacts/ts/epics/<EPIC-ID>/epic.md`
- Do not use a flat `artifacts/ts/stories/` primary layout

## Dual surface (mandatory)
JSON + Markdown for every epic/story. Do not finish with only one format.

## Required TS-only fields
Legacy Mapping, ADR References, TSA Component, Gap Analysis Summary,
Migration Impact (`New|Modified|Reused|Deprecated`) — plus all shared story fields.

## Procedure
1. Create/update one TS story per gap item (or coherent group)
2. Assign `TS-STORY-###`; link GAP/ADR/TSA/CS refs
3. Keep statements compliant with accepted ADRs and TSA contracts
4. Leave AC/tests for SK-AC / SK-TEST if next

## Must not
Ignore gap register or invent ADR conflicts.
