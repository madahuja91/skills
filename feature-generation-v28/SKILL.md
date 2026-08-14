---
name: feature-generation-v28
description: >-
  Generate functional Features under an Epic, preserving the functional current-state boundary while aligning it with the target transformation.
---

# Feature Generation

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: feature-generation
  name: Feature Generation
  version: 2.0.0
  purpose: Generate functional Features under an Epic, preserving the functional current-state boundary while aligning it with the target transformation.
  responsibility:
    owns:
    - functional capability decomposition
    - Feature boundaries
    - functional scope
    - functional rules and scenarios
    does_not_own:
    - LLD
    - technical Story decomposition
    - SAC
  inputs:
    required:
    - epic
    - codebase
    - csa_output
    - architecture_blueprint
    - migration_strategy
  source_usage:
    codebase:
      purpose: Evidence of actual functional behavior.
    csa_output:
      purpose: Primary functional current-state source.
    architecture_blueprint:
      purpose: Target functional boundary and capability alignment.
    migration_strategy:
      purpose: Identify transformation constraints affecting the Feature.
  analysis:
    mandatory_areas:
    - functional capability
    - actors
    - business workflow
    - functional behavior
    - business rules
    - functional validations
    - inputs and outputs at functional level
    - dependencies at functional level
    - current-state evidence
    - target-state intent
    - migration impact
    rules:
    - Feature must represent one coherent functional capability.
    - Feature must be independently understandable.
    - Feature must be small enough to decompose into technical Stories.
    - Preserve current-state functional meaning even when target implementation changes.
    - Architecture and migration information may influence the Feature boundary but must not turn it into an LLD artifact.
    - Honor UI feature_selection. Token epic-N-feature-M means Epic N (1-based, matching epic_names order) gets exactly M Features. Empty feature_selection → LLM decides Feature count from evidence. epic_names still controls Epic titles only.
  output:
    schema: feature
    required_fields:
    - id
    - epic_id
    - title
    - description
    - functional_objective
    - functional_scope
    - actors
    - functional_flow
    - business_rules
    - functional_validations
    - dependencies
    - current_state
    - target_state_intent
    - migration_considerations
    - traceability
  naming:
    pattern: <Functional Capability>
    examples:
    - Category Data Upload and Validation
    - Customer Registration and Profile Management
    - Order Submission and Status Management
  constraints:
    must:
    - remain functional
    - be implementation-neutral
    - trace to current-state evidence
    - explain target transformation intent where supported
    must_not:
    - become a UI Feature
    - become a BFF/API Feature
    - become a Domain Feature
    - contain classes or method names
    - contain database tables
    - contain implementation tasks
    - contain LLD design
```


## Dual-write + schema gate
- JSON agents write schema-complete JSON under src/artifacts/canonical/backlog/ only. Markdown Renderer (Claude Sonnet 4.5) writes matching .md twins under src/artifacts/projections/backlog/. Do not dual-write Markdown from JSON agents.
- JSON path root: src/artifacts/canonical/backlog/. Markdown path root: src/artifacts/projections/backlog/.
- All skill schema required_fields must be present and non-empty before status=complete; otherwise status=incomplete and retry.
- Never write under src/canonical/ or use flat Feature/FAC/AAC siblings of Epic.

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
