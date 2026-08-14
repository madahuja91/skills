---
name: story-decomposition-v24
description: >-
  Determine the minimum set of completely technical LLD Stories required to implement a Feature.
---

# Technical Story Decomposition

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: story-decomposition
  name: Technical Story Decomposition
  version: 2.0.0
  purpose: Determine the minimum set of completely technical LLD Stories required to implement a Feature.
  responsibility:
    owns:
    - technical slicing
    - area selection
    - cross-story dependency identification
    does_not_own:
    - Epic or Feature business scope
    - detailed implementation design of specialist Stories
  inputs:
    required:
    - feature
    - fac
    - aac
    - architecture_blueprint
    - migration_strategy
    - current_state_evidence
  exact_story_area_enum:
  - UI
  - BFF/API
  - Domain
  - Persistence
  - Messaging
  - Testing
  decomposition_rules:
  - Story layers are NOT always all six. If UI story_layer_selection includes epic-N-feature-M-story-<layers>, selected_areas for that Feature are only those layers. If story_layer_selection is empty, LLM/Story Decomposer decides selected_areas from evidence (may be a subset).
  - skipped_areas = exact_story_area_enum minus selected_areas. Skipped layers write no Story.
  - Create exactly one Story per selected layer. Do not create Stories for skipped layers.
  - Do not create separate Features for UI and backend concerns.
  - Keep all technical slices for a Feature under that Feature. Multiple Features per Epic are allowed when feature_selection or LLM decision says so.
  - Every selected area must have a clear technical responsibility.
  - Testing layer is included only when selected (via story_layer_selection or LLM decision). Every created Story still includes its own testing_strategy.
  - Identify dependencies and ordering between Stories (typical: Persistence/Domain before BFF/API/UI; Messaging with Domain/BFF; Testing last or parallel).
  - Write selected_areas and skipped_areas so the Technical Story manager can RUN selected agents and SKIP the rest.
  - Do not generate Story LLD.
  dispatch_contract:
    run: selected_areas
    skip: skipped_areas
    skipped_agent_status: skipped
  output:
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

## Feature / story selection (replaces 1-Feature-per-Epic and forced 6 layers)
- epic_names is unchanged: verbatim Epic titles when provided; LLM titles when empty.
- feature_selection empty → LLM decides Feature count per Epic.
- feature_selection `epic-1-feature-1, epic-2-feature-2` → Epic 1 gets 1 Feature, Epic 2 gets 2.
- story_layer_selection empty → LLM decides layers per Feature.
- story_layer_selection `epic-1-feature-1-story-ui, bff/api` → only UI and BFF/API Stories for that Feature.

## Human names, not bare IDs
Always write the artifact title/name with the id. Forbidden: referring to FEAT-001 / FAC-002 / AAC-001 / SAC-003 / ST-004 / EPIC-001 by number alone.

## Markdown must not dump JSON
Do not copy the full JSON document into Markdown. JSON lives under `src/artifacts/canonical/backlog/`. Markdown is a human-readable projection only.
