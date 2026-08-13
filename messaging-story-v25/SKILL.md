---
name: messaging-story-v25
description: >-
  Generate a completely technical, LLD-level Messaging Story.
---

# Messaging Story

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: messaging-story
  name: Messaging Story
  version: 2.0.0
  purpose: Generate a completely technical, LLD-level Messaging Story.
  story_area: Messaging
  responsibility:
    owns:
    - technical implementation design for the Messaging slice
    - LLD details required for engineering implementation
    - Story-level SAC
    does_not_own:
    - business Feature definition
    - Feature-level FAC
    - Feature-level AAC
    - unrelated technical areas
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
    primary: architecture_blueprint messaging decisions/contracts + migration_strategy + AAC
    architecture_blueprint: Authoritative target architecture/design source.
    migration_strategy: Authoritative source for transition and compatibility constraints.
    current_state_evidence: Reference only to preserve existing functional intent and identify migration impact.
  analysis:
    areas:
    - event/topic/queue
    - producer
    - consumer
    - message/event schema
    - serialization
    - partition/key strategy
    - ordering
    - delivery semantics
    - retry
    - dead-letter handling
    - idempotency
    - consumer state
    - failure handling
    - event versioning
    - observability
    rules:
    - Determine applicability from the Feature and target architecture.
    - Do not force irrelevant LLD sections.
    - If an LLD area is not applicable, explicitly state not_applicable and explain why.
    - Resolve cross-story contracts and dependencies before finalizing the Story.
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
    - validation_and_error_handling
    - security
    - observability
    - transaction_and_consistency
    - migration_considerations
    - backward_compatibility
    - testing_strategy
    conditional:
    - producer
    - consumer
    - partitioning
    - retry
    - dlq
    - event_versioning
  technical_detail_rules:
  - Identify existing component(s) to modify where evidence supports it.
  - Identify target component(s) to create or change.
  - Describe component responsibilities and boundaries.
  - Describe interfaces/contracts including inputs, outputs and failure behavior where applicable.
  - Describe data flow from entry point to downstream boundary.
  - Describe dependencies and sequencing with sibling Stories.
  - Describe implementation changes at class/component/module level when supported by the target design.
  - Include configuration changes where required.
  - Include error handling and validation ownership.
  - Include security/authorization implications where applicable.
  - Include observability requirements where applicable.
  - Include transaction/consistency behavior where applicable.
  - Include migration/coexistence/backward compatibility implications.
  - Identify testing strategy and test evidence.
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
    - security
    - observability
    - transaction_and_consistency
    - migration_considerations
    - backward_compatibility
    - testing_strategy
    - sac
    - traceability
  sac_rules:
  - SAC must verify implementation behavior, not restate business acceptance.
  - Include positive, negative and boundary scenarios where applicable.
  - Include contract/interface verification where applicable.
  - Include migration/compatibility verification where applicable.
  - SAC must be independently testable by engineering/QA.
  traceability:
    must_reference:
    - feature_id
    - fac_ids
    - aac_ids
    - architecture_blueprint_references
    - migration_strategy_references
    - current_state_evidence_references
    - sibling_story_dependencies
    id_generation: traceability-agent
  quality:
    completeness:
    - All applicable LLD areas covered.
    - No placeholder technical decisions remain unresolved.
    consistency:
    - Align with architecture_blueprint.
    - Align with migration_strategy.
    - No conflict with sibling Stories.
    validation:
    - Story is implementation-ready.
    - SAC is technically verifiable.
  constraints:
    must:
    - set area exactly to "Messaging"
    - remain completely technical
    - preserve Feature business intent
    must_not:
    - add new business requirements
    - invent architecture decisions
    - use non-approved Story area names
    - reduce the Story to generic statements such as "implement API" or "create UI"
```


## Dual-write + schema gate
- When writing a backlog JSON artifact, immediately write the matching Markdown twin under src/artifacts/projections/backlog/ with the same nested folders and ID (do not wait for Governance PASS).
- JSON path root: src/artifacts/canonical/backlog/. Markdown path root: src/artifacts/projections/backlog/.
- All skill schema required_fields must be present and non-empty before status=complete; otherwise status=incomplete and retry.
- Never write under src/canonical/ or use flat Feature/FAC/AAC siblings of Epic.
