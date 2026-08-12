---
name: story-decomposition
description: >-
  Determine the minimum set of completely technical LLD Stories required to implement a Feature.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Technical Story Decomposition

Version `2.0.0`.

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

- Create only areas required by the target design.
- Do not create a Story merely because an area exists in the enum.
- Do not create separate Features for UI and backend concerns.
- Keep all technical slices under the same Feature.
- Every selected area must have a clear technical responsibility.
- Testing is selected when dedicated technical validation is required; individual Stories must still include their own testing strategy.
- Identify dependencies and ordering between Stories.
- Detect whether a single Story would become too broad and split only by approved area.
- Write selected_areas and skipped_areas so the Technical Story manager can RUN selected agents and SKIP the rest.
- Do not generate Story LLD.

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
