---
name: SK-TARGET
description: >-
  Map gap register items to Target State epics/stories with Jira-quality clarity,
  legacy mapping, ADR refs, TSA components, and migration impact.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# SK-TARGET — Target Story Mapping (client-showable)

## Inputs
- gap_register, tsa_analysis, adr_decisions
- CS stories for legacy mapping

## Outputs
- `artifacts/ts/ts_stories.json` — **required** (each story includes **`epic_id`**)
- Nested Markdown — **required**:
  - `artifacts/ts/epics/<EPIC-ID>/stories/<STORY-ID>.md`
- Use with SK-EPIC for `ts_epics.json` + `artifacts/ts/epics/<EPIC-ID>/epic.md`

## Dual surface (mandatory)
JSON + Markdown for every story.

## CLIENT DELIVERY STANDARD
Same bar as SK-STORY: sprint-sized journeys, Jira-ready titles, As a / What / How / Scope,
full statements, appendix-only IDs. Plus clear migration impact a client migration lead can act on.

## Required TS-only fields
Legacy Mapping, ADR References, TSA Component, Gap Analysis Summary,
Migration Impact (`New|Modified|Reused|Deprecated`) — plus all shared story fields.

## HARD quality bar (same as SK-STORY, plus TS)
- Actionable title (no “Operate …”, no “Implement gap GAP-00x” alone)
- Description: `As a … I want … so that …` + What + How + Scope
- How must reference target components/APIs from TSA when known
- Migration impact and legacy mapping in dedicated tables (not only IDs in the title)
- AC/tests left for SK-AC/SK-TEST must not be circular stubs

## Sizing (same as SK-STORY)
- Do **not** dump one mega-story per capability/gap cluster when ≥3 separable build slices exist
- Prefer 1–3 gaps/FRs per story; split by actor, TSA component, or migration wave when demos differ

## Procedure
1. Create/update TS stories from gap items (or coherent groups) — developable slices, not mega dumps
2. Assign `TS-STORY-###`; link GAP/ADR/TSA/CS refs
3. Write Jira-quality narrative for build teams
4. Keep statements compliant with accepted ADRs and TSA contracts
5. Leave concrete AC/tests to SK-AC / SK-TEST

## Must not
Ignore gap register; invent ADR conflicts; ship boilerplate “implement target capability” text; ship one mega-story per domain.
