---
skill_revision: 2026-08-12-v21
name: swarm-orchestration-v21
description: >-
  Manager rules for parallel specialist swarms, shared-memory sync, selective dispatch, 2-cycle retry, and canonical JSON placeholders.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Swarm Orchestration

Version `2.1.0`.

## Purpose

Manager rules for parallel specialist swarms, shared-memory sync, selective dispatch, 2-cycle retry, and canonical JSON placeholders.

## Manager responsibility

```yaml
owns:
- specialist selection (run vs skip)
- fan-out / fan-in
- shared-memory bootstrap and sync
- incomplete/failed agent retry (max 2 cycles per agent)
- bounded package publication
- correction routing to the failed agent, not the whole swarm
does_not_own:
- generating specialist content itself
- inventing skipped-area Stories
- publishing Jira/Markdown before Governance PASS
```

## Retry

```yaml
max_cycles_per_agent: 2
rules:
- If a specialist output is missing, incomplete, invalid, or status is failed/incomplete,
  the owning orchestrator retries THAT agent only.
- Do not regenerate the entire swarm on a single agent failure.
- After 2 failed retries, mark the agent failed, record owner + reason in shared memory,
  and escalate to Workflow Orchestrator / Governance.
- Governance FAIL routes correction to the owning orchestrator; that orchestrator
  retries only the failed agent(s); then return to Governance. Workflow Orchestrator
  allows max 2 Governance cycles.
- Never retry a skipped agent.
```

## Swarm pattern

- Dispatch independent specialists in parallel.
- Create and maintain shared memory so parallel agents stay in sync.
- Fan-in only complete (or explicitly skipped) specialist outputs.
- Logical dependency order is enforced through shared memory even when agents are dispatched in parallel.

## Shared memory

```yaml
path: src/_internal/swarm/shared_memory.json
required_slots:
- agent_status
- retry_count
- requirements
- epic_names
- epics
- features
- fac
- aac
- selected_areas
- skipped_areas
- stories
- contracts
- correction
rules:
- Orchestrator creates the file before dispatch if missing.
- Every specialist reads shared memory before writing.
- Every specialist writes its slot and agent_status after finishing.
- Epic -> Feature -> FAC -> AAC: Feature Agent must not finalize until Epic IDs exist
    in shared memory; FAC and AAC must not finalize until Feature IDs exist.
- Story area agents must not generate unless their area is in selected_areas.
```

## Selective dispatch

```yaml
story_areas:
- UI
- BFF/API
- Domain
- Persistence
- Messaging
- Testing
rules:
- Story Decomposer runs first and writes selected_areas and skipped_areas with rationale.
- Technical Story Orchestrator runs only selected area agents.
- Unselected area agents must immediately return status=skipped, write no Story, and
  not consume retry budget.
- Do not create a Story merely because an area agent exists on the graph.
```

## Specialist output contract

```yaml
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
status_enum:
- candidate
- complete
- incomplete
- failed
- skipped
placeholder:
  artifactType: <requirement|epic|feature|fac|aac|current_state_evidence|architecture_context|story_decomposition|technical_story|quality|traceability|jira_projection|markdown>
  id: <REQ-###|EPIC-###|FEAT-###|FAC-###|AAC-###|ST-###|SAC-###|PKG-###>
  parentId: <parent id or null>
  area: <UI|BFF/API|Domain|Persistence|Messaging|Testing|null>
  status: complete
  sourceReferences: []
  content: {}
  acceptanceCriteria: []
  confidence: {}
  validation: {}
  outputPath: src/artifacts/specialists/<agent>/<id>.json
```

## Canonical placeholders

```yaml
active_root: src
packages:
  current_state_evidence: src/artifacts/packages/current-state-evidence.json
  architecture_context: src/artifacts/packages/architecture-context.json
  epic_feature_package: src/artifacts/packages/epic-feature-package.json
  story_decomposition: src/artifacts/packages/story-decomposition.json
  technical_story_package: src/artifacts/packages/technical-story-package.json
canonical:
  backlog_root: src/artifacts/canonical/backlog/
  backlog_index: src/artifacts/canonical/backlog/index.json
  requirement: src/artifacts/canonical/backlog/Requirement/REQ-###/REQ-###.json
  epic: src/artifacts/canonical/backlog/Epic/EPIC-###/EPIC-###.json
  feature: src/artifacts/canonical/backlog/Epic/EPIC-###/Feature/FEAT-###/FEAT-###.json
  fac: src/artifacts/canonical/backlog/Epic/EPIC-###/Feature/FEAT-###/FAC/FAC-###.json
  aac: src/artifacts/canonical/backlog/Epic/EPIC-###/Feature/FEAT-###/AAC/AAC-###.json
  story: src/artifacts/canonical/backlog/Epic/EPIC-###/Feature/FEAT-###/Technical-Stories/ST-###/ST-###.json
  sac: src/artifacts/canonical/backlog/Epic/EPIC-###/Feature/FEAT-###/Technical-Stories/ST-###/SAC/SAC-###.json
  traceability: src/artifacts/canonical/backlog/Traceability/traceability.json
  validation: src/artifacts/canonical/backlog/Validation/validation.json
projections:
  jira_import: src/artifacts/projections/jira-import.json
  backlog_markdown_root: src/artifacts/projections/backlog/
  backlog_readme: src/artifacts/projections/backlog/README.md
swarm:
  shared_memory: src/_internal/swarm/shared_memory.json
rules:
- Create backlog folder tree placeholders so downstream agents have stable paths.
- Empty placeholder shape is {"schema_version":"2.0.0","status":"pending","items":[]}.
- Canonical JSON folder tree is the source of truth. Markdown folder tree and Jira are projections only.
- Markdown mirrors JSON 1:1 under projections/backlog/ (same folders/IDs; .md instead of .json).
- Write projections only after Governance PASS.
```

## ID prefixes

- REQ
- EPIC
- FEAT
- FAC
- AAC
- ST
- SAC

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
- Regenerate an entire swarm for a single failed agent.

## JSON / Markdown parity (mandatory)

`src/artifacts/canonical/backlog/` (JSON) and `src/artifacts/projections/backlog/` (Markdown)
MUST convey the **same information**.

Rules:
- Same folder tree and same IDs (REQ/EPIC/FEAT/FAC/AAC/ST/SAC).
- Every JSON file has a matching `.md` at the same relative path (and vice versa after PASS).
- Every field present in a JSON artifact must appear in its Markdown twin (no silent drops).
- Markdown must not invent content absent from JSON.
- `index.json` ↔ `README.md` must list the same IDs/paths.
- Traceability and Validation have both JSON and MD twins.

## Exact Story area enum (only these)

Technical Stories are selected **only** from this closed set:

1. UI
2. BFF/API
3. Domain
4. Persistence
5. Messaging
6. Testing

Rules:
- Story Decomposer decides required vs skipped per Feature (not all six are mandatory every time).
- Selected areas → generate one Story each under Technical-Stories/.
- Skipped areas → status=skipped, no Story file, no SAC.
- Area names in Story JSON/MD must match the enum exactly (including `BFF/API`).
