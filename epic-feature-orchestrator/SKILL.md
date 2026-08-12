---
name: epic-feature-orchestrator
description: >-
  Coordinate Epic, Feature, FAC and AAC generation before technical Story decomposition.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Epic Feature Orchestration

Version `2.0.0`.

## Purpose

Coordinate Epic, Feature, FAC and AAC generation before technical Story decomposition.

## Workflow binding

- Workflow Orchestrator (coordination semantics)
- Epic/Feature Orchestrator

## Execution

- analyze requirement and sources
- generate candidate Epics
- validate Epic abstraction level
- decompose Epic into Features
- validate Feature functional boundaries
- generate FAC
- generate AAC
- perform cross-artifact quality validation
- publish canonical Epic/Feature context for Story Swarm

## Dependency order

- Epic
- Feature
- FAC
- AAC
- Technical Story Decomposition

## Handoff to Story swarm

```yaml
required_context:
- epic
- feature
- fac
- aac
- architecture_blueprint
- migration_strategy
- current_state_evidence
```

## Rules

- Never ask Story agents to redefine Epic or Feature scope.
- Never let technical Story decomposition change Feature business boundaries without governance review.

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
