---
name: feature-generation
description: >-
  Generate functional Features under an Epic, preserving the functional current-state boundary while aligning it with the target transformation.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Feature Generation

Version `2.0.0`.

## Purpose

Generate functional Features under an Epic, preserving the functional current-state boundary while aligning it with the target transformation.

## Responsibility

```yaml
owns:
- functional capability decomposition
- Feature boundaries
- functional scope
- functional rules and scenarios
does_not_own:
- LLD
- technical Story decomposition
- SAC
```

## Inputs

```yaml
required:
- epic
- codebase
- csa_output
- architecture_blueprint
- migration_strategy
```

## Source usage

```yaml
codebase:
  purpose: Evidence of actual functional behavior.
csa_output:
  purpose: Primary functional current-state source.
architecture_blueprint:
  purpose: Target functional boundary and capability alignment.
migration_strategy:
  purpose: Identify transformation constraints affecting the Feature.
```

## Analysis

```yaml
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
- Architecture and migration information may influence the Feature boundary but must
  not turn it into an LLD artifact.
```

## Naming

```yaml
pattern: <Functional Capability>
examples:
- Category Data Upload and Validation
- Customer Registration and Profile Management
- Order Submission and Status Management
```

## Output

```yaml
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
```

## Constraints

```yaml
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

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.
