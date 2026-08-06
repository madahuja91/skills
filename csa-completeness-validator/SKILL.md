---
name: csa-completeness-validator
description: Per-lane CSA gate checker; after join, renders lean csa_pack from artifact schemas as legacy-only docs. No workflow meta in the pack. No Assembler/deliverables/machine.
---

# Completeness Validation Agent Skill

## Schema

Invocation contract: [schema.json](schema.json)

**HARD:** obey `csa-parallel-lane-gates` and `csa-section-boundaries`.

## Role

1. **Lane mode** — validate one specialist `artifacts/*.json` gate.
2. **Final mode** — render lean `csa_pack/` from accepted artifacts, then validate.

Never invent architecture facts. Never invoke Document Assembler.

## HARD write scope

| Allowed | Forbidden |
|---------|-----------|
| `artifacts/quality_gate_reports/*` | `deliverables/**` |
| `_internal/completeness_validation/*` | `csa_pack/machine/**` |
| `_internal/swarm/*` (status only) | Numbered `01_`–`05_` client MD |
| `csa_pack/{5 named MD, README, arc42-c4/*.html}` **final only** | Gate reports inside `csa_pack/` |

## HARD: `csa_pack` content policy

Client docs are **legacy codebase + schema inventories only**.

Include: stack, modules, domains, capabilities, rules, components, C4, data stores, entity attributes, lineage, SP logic, integrations, contracts, resilience, evidence-backed risks/gaps.

Exclude from every `csa_pack/**` file:

- Workflow/swarm/orchestrator/Manager/Completeness/Assembler/lane/join/rework text
- Gate PASS/FAIL, gate_id, attempt, max_reruns, remediation briefs for agents
- `swarm_state`, handoffs, checkpoint, ACTIVE_ROOT, run_plan, artifacts_index process notes
- “How this pack was generated” process narrative

Put all of that under `_internal/` or `artifacts/quality_gate_reports/` only.

## Lane mode procedure

1. `active-root-hygiene`
2. Validate artifact against specialist schema (exact field names)
3. Evidence + SP/MQ checks
4. Write gate report under `artifacts/quality_gate_reports/`
5. Update `swarm_state.loop` + artifacts_index

## Final mode procedure (packager)

Inputs: accepted `artifacts/{discovery,domain,architecture,lineage,integration}.json`

1. Join checklist: four specialist gates accepted.
2. Render Markdown from **schema fields only** (`csa-section-boundaries`).
3. Build `csa_pack/arc42-c4/*.html` from architecture/integration evidence (legacy views only).
4. Write `csa_pack/README.md` as a doc index (no workflow status).
5. Validate pack shape + **no workflow-meta leakage** into `csa_pack/`.
6. Write final gate report under `artifacts/quality_gate_reports/` only.
7. Set `loop.completeness` PASS/FAIL in swarm state (not in client MD).

## Mapping gate → skill

| gate_id | artifact |
|---------|----------|
| gate-discover | artifacts/discovery.json |
| gate-business-domain | artifacts/domain.json |
| gate-tech-architecture | artifacts/architecture.json |
| gate-data-lineage | artifacts/lineage.json |
| gate-integration | artifacts/integration.json |
| gate-csa-document | csa_pack/ (legacy content only) |

## Rules

- `max_reruns` = 2
- Prefer missing schema-field remediation over HTML cosmetics
- Do not soft-pass invented stacks
- Fail final gate if `csa_pack` contains workflow/swarm/gate process language
