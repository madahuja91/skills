---
name: SK-STORY
description: >-
  Generate Current State functional stories from capabilities, FRs, and rules
  using Jira-quality clarity: actionable titles, user-value description,
  concrete what/how, developable story size (not one mega-story per capability).
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# SK-STORY — Client-showable Current State Stories

## Purpose
Write stories as if a **senior BA** is preparing a **client review / Jira backlog**:
a product owner can prioritize them, a developer can estimate and build them, a tester can verify them — **without reading the legacy dump**.

Audience: client BA / PO / delivery lead — **not** an internal AI pipeline log.

## Inputs
- capabilities, requirements, rules
- Template version (default 1.1.0+)
- Prefer `templates/current-state-story.md`

## Outputs
- `artifacts/cs/cs_stories.json` — **required**
- Nested Markdown — **required**: `artifacts/cs/epics/<EPIC-ID>/stories/<STORY-ID>.md`

## Dual surface (mandatory)
1. JSON entry including **`epic_id`**
2. Matching Markdown under the parent epic folder

---

## CLIENT DELIVERY STANDARD (non-negotiable)

A story is **client-showable** only if all are true:

1. **Sprint-sized** — one primary user/system journey; typically **1–3 FRs**
2. **Title** reads like a Jira Summary (verb + outcome), ≤80 chars
3. **Description** answers What / How / Why in plain business English
4. **FR/BR tables** use full testable statements (not ID-only tables)
5. **Traceability IDs** stay in an appendix — they must not dominate the hero text
6. A new reader can answer in 60 seconds: *Who? What changes? How do we know it’s done?*

### Forbidden (client will reject these)
- One story per capability when that capability has ≥3 FRs
- Titles: `Operate …`, `Support the observed…`, `Handle … capability`
- Descriptions that only say “support observed web/service/PLSQL behavior”
- Mega “and …” titles covering 3+ unrelated journeys
- Circular AC stubs (“performs FR-00x”)
- Shipping for swarm speed / gate PASS while narrative is thin

### Gold sample (tone to match)

**Title:** `Search transaction batches and review exception detail`

**User story:** As a CCDS operations user, I want to search batches by batch or subfile id and open exception detail, so that I can decide the next payment/receipt action with full lineage.

**What:** The batch function returns summary rows and exception records keyed by batch, subfile, and transaction ids…

**How:** 1) Open batch search → 2) Enter batch/subfile id → 3) System loads summary + exceptions → 4) User opens a row to review lineage fields.

---

## HARD sizing rules

### Split when any differ
1. Actor / role  
2. Entry point (UI / REST / package / MQ)  
3. Demoable business outcome  
4. Distinct failure family (authz vs validation vs concurrency)

### Target shape
- Capability with ≥3 FRs → typically **2–6 stories** under one epic  
- Story with ≥4 FRs → **re-split before handoff**  
- 1 story for a whole capability is allowed **only** if ≤2 tightly related FRs, same actor, same entry point

---

## Narrative structure (JSON `description` + Markdown)

1. **User story:** `As a <role>, I want <action>, so that <value>.`
2. **What happens:** 3–6 plain sentences (this story only)
3. **How it works:** numbered steps (entry → validate → process/persist/integrate → outcome)
4. **Scope In / Out:** bullets; Out of scope should name sibling stories when split
5. **Business objective:** one outcome sentence for **this** story
6. **FR table:** ID | Priority | **full statement**
7. **BR table:** ID | Type | **concrete rule** | linked FRs
8. **Assumptions / Dependencies** when known
9. **Edge cases** with expected handling
10. Leave AC/Tests empty or stub for SK-AC / SK-TEST — never circular
11. **Traceability** as appendix only

Use `templates/current-state-story.md` section order.

## Procedure
1. Group FRs by actor + entry point + demoable outcome (not capability alone)
2. Author each story to the CLIENT DELIVERY STANDARD
3. Assign `CS-STORY-###`, `epic_id`, primary capability
4. Write nested MD + JSON
5. Self-check sizing (≥4 FRs → split) and client 60-second test
6. No target-state / ADR / TSA / migration content

## Self-check
- [ ] Client PO could paste title+description into Jira today
- [ ] Developer knows entry point and outcome without opening other stories
- [ ] Not a capability dump; FR statements are full English
- [ ] Nested MD + JSON both exist; epic_id set

## Must not
Mega-story packing; boilerplate wrappers; circular AC; inventing second ACTIVE_ROOT from stale `/memories`.
