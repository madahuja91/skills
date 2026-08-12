---
name: technical-story-core
description: >-
  Shared LLD contract for all technical Story area skills. Stories must be completely technical, implementation-oriented, and must not redefine Feature business scope.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Technical Story Core

Version `2.0.0`.

## Purpose

Shared LLD contract for all technical Story area skills. Stories must be completely technical, implementation-oriented, and must not redefine Feature business scope.

## Workflow binding

- UI Agent
- BFF/API Agent
- Domain Agent
- Persistence Agent
- Messaging Agent
- Testing Agent
- Technical Story Orchestrator

## Responsibility

```yaml
owns: []
does_not_own: []
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
optional:
- sibling_stories
- target_contracts
```

## Source usage

```yaml
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
```

## Analysis

```yaml
areas: []
rules:
- Story must be completely technical.
- Story must be LLD-level and implementation-oriented.
- Story must translate Feature/FAC/AAC into an implementable technical slice.
- Story must not redefine the Feature's business scope.
- Story must not invent architecture decisions unsupported by architecture_blueprint.
- Migration implications must be included when applicable.
```

## LLD

```yaml
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
```

## Output

```yaml
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
```

## Traceability

```yaml
must_reference:
- feature_id
- fac_ids
- aac_ids
- architecture_blueprint_references
- migration_strategy_references
- current_state_evidence_references
id_generation: traceability-agent
```

## Quality

```yaml
completeness:
- Every applicable LLD area is addressed or explicitly marked not_applicable with
  rationale.
- Story can be understood and implemented without returning to the Feature for technical
  details.
consistency:
- Technical design is consistent with architecture_blueprint.
- Dependencies do not contradict sibling Stories.
validation:
- SAC is technically verifiable.
- No unresolved architectural assumptions remain.
```

## Constraints

```yaml
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
```

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
