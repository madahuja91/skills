# CSA Skills Index

Schema-based skills for the Orchestrator + Swarm CSA workflow.

## Policy

1. Every skill directory has `SKILL.md` **and** `schema.json`.
2. Every `SKILL.md` includes a `## Schema` section linking its contract.
3. Specialist outputs validate against agent schemas (+ shared `csa-artifact-contract`).
4. Completeness reports validate against `quality-gate-framework` + the matching `gate-*` schema.
5. Catalog: [`catalog.json`](catalog.json) (meta-schema: [`catalog.schema.json`](catalog.schema.json)).

## Layout

```text
skills/
  shared/           # contracts, swarm shared memory, gates framework, legacy heuristics
  agents/           # specialist + validator + assembler (+ schemas)
  orchestrator/     # CSA Architecture Manager
  gates/            # per-artifact quality gates (+ schemas)
  standards/        # arc42/C4 HTML + Mermaid, DDD MD, lineage MD, epic-story MD
  catalog.json      # inventory of all skills + schema paths
```

## Shared memory (swarm sync)

Skill: `shared/csa-swarm-shared-memory` — `swarm_state.json` / `handoffs.jsonl` / `context_memory.md`.

## Mermaid diagrams

Skill: `standards/mermaid-diagrams` — required MD fences + HTML `pre.mermaid` rendering for C4, domain, lineage, integration, exec overview.

## Workflow

Import [`../workflow-CSA-Orchestrator-Swarm.json`](../workflow-CSA-Orchestrator-Swarm.json).

## Artifact paths (runtime)

| Path | Producer |
|------|----------|
| `artifacts/*.json` | Specialists / Manager |
| `artifacts/quality_gate_reports/*` | Completeness Validator |
| `csa_pack/**/*.md` | Document Assembler |
| `csa_pack/arc42-c4/*.html` | arc42-c4-views (+ Mermaid) |
| `csa_pack/machine/mermaid_diagrams.json` | Document Assembler |
| `csa_pack/machine/*.json` | Internal tooling |

## Pilot

See [`pilot/PILOT_RUNBOOK.md`](pilot/PILOT_RUNBOOK.md).
