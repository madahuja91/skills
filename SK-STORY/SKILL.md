---
name: SK-STORY
description: >-
  Generate Current State functional stories from capabilities, FRs, and rules
  using the enterprise CS template.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)


# SK-STORY — Current State Story Generation

## Inputs
- capabilities, requirements, rules
- Template version (default 1.0.0)

## Outputs
- `artifacts/cs/cs_stories.json` (array of stories per story.schema) — **required**
- Nested Markdown under parent epic (industry hierarchy) — **required**:
  - `artifacts/cs/epics/<EPIC-ID>/stories/<STORY-ID>.md`
- Do **not** write a flat `artifacts/cs/stories/` folder as the primary layout

## Dual surface (mandatory)
Every story MUST be written as:
1. JSON entry in `cs_stories.json` (system of record) including **`epic_id`**
2. Matching Markdown under its parent epic folder

Do not finish with JSON-only or MD-only.

## Required story fields
ID, Title, Business Objective, Description, Functional Requirements, Business Rules,
Assumptions/Dependencies, Acceptance Criteria (may be filled later by SK-AC),
Data & Integration, Edge Cases, Testing Scenarios (may be filled by SK-TEST),
Traceability, Definition of Done.

## Procedure
1. Map must-priority FRs into cohesive stories based on evidence — **1 story is fine** when the flow is atomic
2. Split into multiple stories only when there are clear boundaries (different actors, flows, or FR clusters)
3. Assign `CS-STORY-###` IDs; keep one capability primary per story when possible; always set `epic_id` when epic is known
4. Embed FR/BR refs; leave AC/tests stubs only if SK-AC/SK-TEST will run next
5. Write nested MD under `epics/<EPIC-ID>/stories/` using tabular template
6. No target-state redesign

## Markdown formatting (required)
Use **tables** for: header attributes, FRs, BRs, assumptions/deps, AC (Given/When/Then columns), data/integration, edge cases, test scenarios, traceability, DoD.
Prefer enterprise templates under `templates/`. Avoid long prose bullets where a table fits.

## Must not
Add ADR/TSA/migration fields (those are Target State only). Force artificial story splits to meet a count quota.
