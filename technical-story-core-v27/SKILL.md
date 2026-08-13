---
name: technical-story-core-v27
description: >-
  Shared LLD contract for all technical Story area skills. Stories must be completely technical, implementation-oriented, and must not redefine Feature business scope.
---

# Technical Story Core

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: technical-story-core
  name: Technical Story Core
  version: 2.0.0
  purpose: Shared LLD contract for all technical Story area skills. Stories must be completely technical, implementation-oriented, and must not redefine Feature business scope.
  responsibility:
    owns: []
    does_not_own: []
  inputs:
    required:
    - feature
    - fac
    - aac
    - architecture_blueprint
    - migration_strategy
    - current_state_evidence
    optional:
    - sibling_stories
    - target_contracts
  source_usage:
    current_state_evidence:
      purpose: Preserve functional intent and understand legacy behavior.
    architecture_blueprint:
      purpose: Define target architecture, boundaries, contracts and design decisions.
    migration_strategy:
      purpose: Define coexistence, sequencing, compatibility, cutover and migration constraints.
    fac:
      purpose: Preserve business acceptance outcomes.
    aac:
      purpose: Enforce Feature-level architecture/design acceptance.
  analysis:
    areas: []
    rules:
    - Story must be completely technical.
    - Story must be LLD-level and implementation-oriented.
    - Story must translate Feature/FAC/AAC into an implementable technical slice.
    - Story must not redefine the Feature's business scope.
    - Story must not invent architecture decisions unsupported by architecture_blueprint.
    - Migration implications must be included when applicable.
  lld:
    mandatory:
    - technical_objective
    - technical_scope
    - target_components
    - component_responsibilities
    - interfaces_and_contracts
    - data_flow
    - dependencies
    - implementation_changes
    - configuration_changes
    - validation_and_error_handling
    - security
    - observability
    - transaction_and_consistency
    - migration_considerations
    - backward_compatibility
    - testing_strategy
    conditional:
    - persistence_model
    - messaging_contract
    - state_management
    - deployment_configuration
  output:
    schema: technical-story
    required_fields:
    - id
    - area
    - title
    - technical_objective
    - technical_scope
    - target_components
    - component_responsibilities
    - interfaces_and_contracts
    - data_flow
    - dependencies
    - implementation_changes
    - validation_and_error_handling
    - migration_considerations
    - testing_strategy
    - sac
    - traceability
  traceability:
    must_reference:
    - feature_id
    - fac_ids
    - aac_ids
    - architecture_blueprint_references
    - migration_strategy_references
    - current_state_evidence_references
    id_generation: traceability-agent
  quality:
    completeness:
    - Every applicable LLD area is addressed or explicitly marked not_applicable with rationale.
    - Story can be understood and implemented without returning to the Feature for technical details.
    consistency:
    - Technical design is consistent with architecture_blueprint.
    - Dependencies do not contradict sibling Stories.
    validation:
    - SAC is technically verifiable.
    - No unresolved architectural assumptions remain.
  constraints:
    must:
    - use exact approved Story area name.
    - separate current-state evidence from target-state design.
    - identify impacted components and interfaces.
    - make migration impact explicit where applicable.
    must_not:
    - use Frontend instead of UI.
    - use Backend instead of BFF/API.
    - create additional Story area names.
    - turn Story into a task checklist.
    - generate a Story when the area is not in shared memory selected_areas.
  skip_rule:
  - Read src/_internal/swarm/shared_memory.json selected_areas first.
  - If this agent's area is not selected, return status=skipped and write no Story.
  specialist_output_contract:
    path: src/artifacts/specialists/<area>/<id>.json
    required_fields:
    - artifactType
    - id
    - parentId
    - area
    - status
    - sourceReferences
    - content
    - acceptanceCriteria
    - confidence
    - validation
    - outputPath
```


## Dual-write + schema gate
- JSON agents write schema-complete JSON under src/artifacts/canonical/backlog/ only. Markdown Renderer (Claude Sonnet 4.5) writes matching .md twins under src/artifacts/projections/backlog/. Do not dual-write Markdown from JSON agents.
- JSON path root: src/artifacts/canonical/backlog/. Markdown path root: src/artifacts/projections/backlog/.
- All skill schema required_fields must be present and non-empty before status=complete; otherwise status=incomplete and retry.
- Never write under src/canonical/ or use flat Feature/FAC/AAC siblings of Epic.
