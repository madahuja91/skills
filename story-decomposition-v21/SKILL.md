---
skill_revision: 2026-08-12-v21
name: story-decomposition-v21
description: >-
  Determine the minimum set of completely technical LLD Stories required to implement a Feature.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Technical Story Decomposition

Version `2.1.0`.

## Purpose

Determine the minimum set of completely technical LLD Stories required to implement a Feature.

## Responsibility

```yaml
owns:
- technical slicing
- area selection
- cross-story dependency identification
does_not_own:
- Epic or Feature business scope
- detailed implementation design of specialist Stories
```

## Inputs

```yaml
required:
- feature
- fac
- aac
- architecture_blueprint
- migration_strategy
- current_state_evidence
```

## Decomposition rules

- Default-select ALL six areas for every Feature: UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Skip an area ONLY when architecture + feature evidence shows zero work in that area; record strong rationale.
- Prefer full six-area coverage; do not skip merely for convenience.
- Do not create separate Features for UI and backend concerns.
- Keep all technical slices under the same Feature.
- Every selected area must have a clear technical responsibility.
- Testing is selected by default; individual Stories must still include their own testing strategy.
- Identify dependencies and ordering between Stories.
- Detect whether a single Story would become too broad and split only by approved area.
- Write selected_areas and skipped_areas so the Technical Story manager can RUN selected agents and SKIP the rest.
- Do not generate Story LLD.
- Write Stories under `Technical-Stories/<Area>/ST-###.json` (folder `BFF-API` for area `BFF/API`).

## Dispatch contract

```yaml
run: selected_areas
skip: skipped_areas
skipped_agent_status: skipped
```

## Exact Story area enum

- UI
- BFF/API
- Domain
- Persistence
- Messaging
- Testing

## Output

```yaml
schema: technical-story-decomposition
path: src/artifacts/packages/story-decomposition.json
required_fields:
- selected_areas
- skipped_areas
- rationale_per_area
- dependency_graph
- contract_boundaries
- traceability
```

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.

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
