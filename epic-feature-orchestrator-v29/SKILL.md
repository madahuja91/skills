---
name: epic-feature-orchestrator-v29
description: >-
  Coordinate Epic, Feature, FAC and AAC generation before technical Story decomposition.
---

# Epic Feature Orchestration

Authoritative skill definition (identical to `skill.yaml` / `schema.json`):

```yaml
skill:
  id: epic-feature-orchestrator
  name: Epic Feature Orchestration
  version: 2.0.0
  purpose: Coordinate Epic, Feature, FAC and AAC generation before technical Story decomposition.
  execution:
  - bootstrap shared memory
  - swarm Capability, Requirement, Rule, Epic, Feature, FAC, AAC in parallel
  - enforce Epic -> Feature -> FAC -> AAC through shared memory even when agents run together
  - retry only the incomplete/failed agent, max 2 cycles
  - publish canonical Epic/Feature package for Story Swarm
  swarm:
    shared_memory: src/_internal/swarm/shared_memory.json
    sync_rules:
    - Feature Agent must not finalize until Epic IDs exist in shared memory.
    - FAC and AAC must not finalize until Feature IDs exist in shared memory.
    - Do not regenerate the whole swarm for one failed agent.
  canonical_output: src/artifacts/packages/epic-feature-package.json
  dependency_order:
  - Epic
  - Feature
  - FAC
  - AAC
  - Technical Story Decomposition
  handoff_to_story_swarm:
    required_context:
    - epic
    - feature
    - fac
    - aac
    - architecture_blueprint
    - migration_strategy
    - current_state_evidence
    - epic_names
  epic_names_handoff:
    when_empty: Epic Agent may propose titles.
    when_provided: Epic titles must match epic_names verbatim.

  success_gate:
  - FAC and AAC are mandatory for every Feature before SUCCESS.
  - Materialize FAC/FAC-###.json and AAC/AAC-###.json under each Feature folder.
  - Retry FAC Agent / AAC Agent (exact names) max 2 if missing; never mark SUCCESS with FAC=0 or AAC=0.
  - Dispatch only exact labels: Capability Agent, Requirement Agent, Rule Agent, Epic Agent, Feature Agent, FAC Agent, AAC Agent.
  rules:
  - Never ask Story agents to redefine Epic or Feature scope.
  - Never let technical Story decomposition change Feature business boundaries without governance review.
  - Feature count per Epic comes from UI feature_selection (epic-N-feature-M). Empty feature_selection → LLM decides how many Features that Epic needs. Never force a global 1:1 Epic:Feature ratio.
  - JSON agents write schema-complete JSON under src/artifacts/canonical/backlog/ only. Markdown Renderer (Claude Sonnet 4.5) writes matching .md twins under src/artifacts/projections/backlog/. Do not dual-write Markdown from JSON agents.
  - JSON path root: src/artifacts/canonical/backlog/. Markdown path root: src/artifacts/projections/backlog/.
  - All skill schema required_fields must be present and non-empty before status=complete; otherwise status=incomplete and retry.
  - Never write under src/canonical/ or use flat Feature/FAC/AAC siblings of Epic.
```

  # content rule: Never write BR/ADR/migration references; inline full details in every artifact.

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
