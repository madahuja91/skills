---
name: backlog-quality-v28
description: >-
  Validate the backlog for architectural correctness and LLD readiness.
---

# Backlog Quality

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: backlog-quality
  name: Backlog Quality
  version: 2.0.0
  purpose: Validate the backlog for architectural correctness and LLD readiness.
  gates:
    epic:
    - business capability/outcome only
    - no implementation detail
    feature:
    - functional boundary
    - implementation-neutral
    fac:
    - Feature-level
    - business/functional and testable
    aac:
    - Feature-level
    - architecture/design and traceable to architecture_blueprint or migration_strategy
    story:
    - completely technical
    - LLD-level
    - implementation-ready
    - correct Story area
    - all applicable LLD sections covered
    sac:
    - Story-level
    - technically verifiable
  exact_story_area_enum:
  - UI
  - BFF/API
  - Domain
  - Persistence
  - Messaging
  - Testing
  blocking_conditions:
  - FAIL if any Epic/Feature/FAC/AAC/ST/SAC JSON is missing skill schema required_fields.
  - FAIL if any canonical JSON lacks a Markdown twin under src/artifacts/projections/backlog/ with the same nested path.
  - FAIL if Story area skills (UI/BFF-API/Domain/Persistence/Messaging/Testing) omit area or core required LLD fields.
  - Story is generic rather than technical.
  - Story lacks target components or interfaces where applicable.
  - Story lacks data flow where applicable.
  - Story lacks migration consideration where applicable.
  - Story has unresolved architecture assumptions.
  - Story uses an invalid area name.
  - SAC only repeats FAC.
  - Story conflicts with sibling Story contracts.
  - A skipped area still has a Story.
  - A selected area has no Story.

  - Missing REQ or FAC or AAC or ST or SAC folder-tree files (counts zero on disk).
  - Package-only technical stories without Technical-Stories/<Area>/ST-###.json.
  - Projection published with fewer Epics than canonical (Epic removal).
  - Orchestrator reported SUCCESS while hierarchy incomplete.
  canonical_output: src/artifacts/canonical/validation.json
```


## Dual-write + schema gate
- JSON agents write schema-complete JSON under src/artifacts/canonical/backlog/ only. Markdown Renderer (Claude Sonnet 4.5) writes matching .md twins under src/artifacts/projections/backlog/. Do not dual-write Markdown from JSON agents.
- JSON path root: src/artifacts/canonical/backlog/. Markdown path root: src/artifacts/projections/backlog/.
- All skill schema required_fields must be present and non-empty before status=complete; otherwise status=incomplete and retry.
- Never write under src/canonical/ or use flat Feature/FAC/AAC siblings of Epic.

  # content rule: Never write BR/ADR/migration references; inline full details in every artifact.
