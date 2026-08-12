---
name: SK-STORY
description: >-
  Generate Current State functional stories from capabilities, FRs, and rules
  using Jira-quality clarity: actionable titles, user-value description,
  concrete what/how, and industry-standard detail (not circular FR echoes).
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# SK-STORY — Current State Story Generation (Jira-quality)

## Purpose
Produce stories a BA, developer, or tester can execute without reading the whole legacy dump.
Stories document **current-state functional behavior** with the same clarity as a well-written Jira story:
**what** the user/system must achieve, **how** the flow works, and **how done is verified**.

## Inputs
- capabilities, requirements, rules
- Template version (default 1.0.0)

## Outputs
- `artifacts/cs/cs_stories.json` (array of stories per story.schema) — **required**
- Nested Markdown under parent epic — **required**:
  - `artifacts/cs/epics/<EPIC-ID>/stories/<STORY-ID>.md`
- Do **not** write a flat `artifacts/cs/stories/` folder as the primary layout

## Dual surface (mandatory)
1. JSON entry in `cs_stories.json` including **`epic_id`**
2. Matching Markdown under the parent epic folder

## HARD quality bar (block shipping if violated)

### Titles
- **Good:** verb + business outcome — e.g. `Authenticate CCDS users and establish session context`
- **Forbidden patterns:** `Operate <Capability>`, `Support the observed…`, `Handle <capability> capability`
- Max ~80 characters; no ID soup in the title

### Description (must be human-readable)
Use this structure in both JSON `description` and Markdown:

1. **User story line:** `As a <role>, I want <capability/action>, so that <business value>.`
2. **What happens (What):** 3–6 plain sentences of the business flow (screens/services/batches as observed).
3. **How it works (How):** numbered steps a developer/tester can follow (entry point → validations → persistence/integration → outcome).
4. **In scope / Out of scope:** short bullets.
5. **Do not** write only “support the observed capability through existing web/service/PLSQL…”.

### Business objective
One clear outcome sentence (value + actors), not a capability paraphrase.

### Functional requirements & rules
- Keep FR/BR IDs and statements, but statements must be **testable English**, not “the system shall perform FR-00x”.
- Put heavy legacy path refs in **Traceability / Source Refs**, not in the title/description hero text.

### Acceptance criteria & tests
- Prefer concrete stubs or leave empty for SK-AC / SK-TEST.
- **Never** invent circular AC like “Then the system performs FR-001”.

### Edge cases
- Real conditions + expected handling (message, reject, retry), not “Apply current-state validation as extracted.”

## Procedure
1. Map must-priority FRs into cohesive stories — **1 story is fine** when atomic.
2. Split when different actors, entry points, or independently valuable flows exist.
3. Assign `CS-STORY-###`; set `epic_id`; keep one primary capability.
4. Write Jira-quality title + description (As a / What / How / Scope).
5. Embed FR/BR tables with clear statements; keep source IDs in Traceability.
6. Write nested MD using `templates/current-state-story.md` structure (tables OK; description may use short paragraphs + numbered list for How).
7. No target-state redesign / ADR / TSA / migration content.

## Self-check before finish
- [ ] Title is actionable (no “Operate …”)
- [ ] Description has As a / What / How / Scope
- [ ] A new reader can explain what to verify without opening legacy code
- [ ] FR/BR linked; epic_id set; nested MD + JSON both exist
- [ ] Trace IDs are present but not drowning the narrative

## Must not
- Boilerplate capability wrappers
- Circular AC/test language
- Force artificial splits for count quotas
- Target-state redesign fields
