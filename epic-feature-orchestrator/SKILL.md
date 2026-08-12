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

## Execution

- bootstrap shared memory
- swarm Capability, Requirement, Rule, Epic, Feature, FAC, AAC in parallel
- enforce Epic -> Feature -> FAC -> AAC through shared memory even when agents run together
- retry only the incomplete/failed agent, max 2 cycles
- publish canonical Epic/Feature package for Story Swarm

## Swarm

```yaml
shared_memory: src/_internal/swarm/shared_memory.json
sync_rules:
- Feature Agent must not finalize until Epic IDs exist in shared memory.
- FAC and AAC must not finalize until Feature IDs exist in shared memory.
- Do not regenerate the whole swarm for one failed agent.
```

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

## Canonical output

`src/artifacts/packages/epic-feature-package.json`

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.
