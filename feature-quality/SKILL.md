---
name: feature-quality
description: >-
  Validate that Epic and Feature artifacts stay at the correct abstraction level.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Epic Feature Quality

Version `2.0.0`.

## Purpose

Validate that Epic and Feature artifacts stay at the correct abstraction level.

## Hierarchy

- Epic -> Feature
- Feature -> FAC
- Feature -> AAC
- Feature -> technical Stories

## Epic gates

- business capability is clear
- business outcome is clear
- scope is high level
- no implementation detail
- can contain multiple Features

## Feature gates

- functional capability is clear
- functional boundary is coherent
- current-state evidence is present
- target transformation intent is supported
- functional rules are explicit
- Feature can be decomposed into technical Stories
- no LLD implementation content

## Blocking conditions

```yaml
epic:
- API endpoint appears
- database table appears
- class/method/service implementation appears
- infrastructure implementation appears
- implementation task appears
feature:
- Feature is named Frontend/Backend instead of functional capability
- Feature is only an implementation component
- Feature contains class-level design
- Feature contains database schema design
- Feature contains deployment steps
- Feature duplicates technical Story scope
```

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.
