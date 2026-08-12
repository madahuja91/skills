---
skill_revision: 2026-08-12-v21
name: backlog-quality-v21
description: >-
  Validate the backlog for architectural correctness and LLD readiness.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Backlog Quality

Version `2.1.0`.

## Purpose

Validate the backlog for architectural correctness and LLD readiness.

## Exact Story area enum

- UI
- BFF/API
- Domain
- Persistence
- Messaging
- Testing

## Gates

```yaml
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
```

## Epic names validation

When `epic_names` was provided and non-empty, every Epic title under `canonical/backlog/Epic/**/EPIC-###.json` must match a user-supplied name **verbatim** (exact string match). FAIL if any Epic title was renamed, rephrased, abbreviated, or casing-normalized.

## Blocking conditions

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

## Canonical output

`src/artifacts/canonical/backlog/Validation/validation.json`

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.

## JSON / Markdown parity (mandatory)

`src/artifacts/canonical/backlog/` (JSON) and `src/artifacts/projections/backlog/` (Markdown)
MUST convey the **same information**.

Rules:
- Same folder tree and same IDs (REQ/EPIC/FEAT/FAC/AAC/ST/SAC).
- Every JSON file has a matching `.md` at the same relative path (and vice versa after PASS).
- Every field present in a JSON artifact must appear in its Markdown twin (no silent drops).
- Markdown must not invent content absent from JSON.
- `index.json` ↔ `README.md` must list the same IDs/paths.
- Traceability and Validation have both JSON and MD twins.

## Exact Story area enum (only these)

Technical Stories are selected **only** from this closed set:

1. UI
2. BFF/API
3. Domain
4. Persistence
5. Messaging
6. Testing

Rules:
- Story Decomposer decides required vs skipped per Feature (not all six are mandatory every time).
- Selected areas → generate one Story each under Technical-Stories/.
- Skipped areas → status=skipped, no Story file, no SAC.
- Area names in Story JSON/MD must match the enum exactly (including `BFF/API`).
