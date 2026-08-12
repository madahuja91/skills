---
name: SK-EPIC
description: >-
  Cluster developable stories into epics by capability, journey, or bounded
  context with Jira-quality narratives. Reject one mega-story per capability.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# SK-EPIC — Client-showable Epics

## Purpose
Write epics as a **product outcome package** for client steering:
why it exists, business value, scope, and a **set of developable stories** a delivery team can staff.

Audience: client PO / program lead reviewing a Functional Epic backlog.

## Inputs
- stories[], capabilities[]
- clustering_policy (default: capability / journey)
- Prefer `templates/epic.md`

## Outputs
- CS: `artifacts/cs/cs_epics.json` **required**
- TS: `artifacts/ts/ts_epics.json` **required**
- Nested `artifacts/{cs|ts}/epics/<EPIC-ID>/epic.md` **required**

## CLIENT DELIVERY STANDARD

An epic is client-showable only if:
1. Title is an **outcome** a PO would put on a roadmap (not `CAP-00x`, not `Operate …`)
2. **Why this epic** explains business pain/value in 2–4 plain sentences
3. **Child stories ≥2** when the capability has ≥3 FRs (default expectation)
4. Each child story has a one-line “why this story” a developer understands
5. Scope In/Out is explicit; Success metrics are observable
6. Trace IDs are appendix — not the epic narrative

### Forbidden
- “One child story is sufficient because evidence indicates…” when FRs clearly separate
- Epic that is only a restatement of a mega-story
- Capability inventory language with no delivery plan

## Clustering rules
- Group stories sharing one business outcome
- Prefer capability / journey / bounded context
- Every story has `epic_id`; epic lists `story_ids`
- If incoming stories are mega dumps → hand back to Story Generator to split **before** finalizing epics

## Procedure
1. Verify story sizing against SK-STORY client standard
2. Cluster; write outcome title + objective + why/value
3. Write scope, child-story plan, success metrics per `templates/epic.md`
4. Consistency check `epic_id` / `story_ids` / nested folders
5. Self-check: PO can staff 2+ developers on different child stories when warranted

## Must not
Ship 10×1 mega-story packs as a “client backlog.”
