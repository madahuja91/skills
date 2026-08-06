---
name: csa-completeness-validator
description: Per-lane CSA gate checker; after join, renders lean csa_pack from artifacts and validates it. Replaces Document Assembler. Never writes deliverables/ or csa_pack/machine/.
---

# Completeness Validation Agent Skill

## Schema

Invocation contract: [schema.json](schema.json)

**HARD:** obey `csa-parallel-lane-gates`.

## Role

1. **Lane mode** — validate one specialist `artifacts/*.json` gate.
2. **Final mode** — after all lanes accepted, **render** lean `csa_pack/` from those artifacts, then validate pack shape + substance mapping.

Never invent architecture facts. Never call/assume Document Assembler.

## HARD write scope

| Allowed | Forbidden |
|---------|-----------|
| `artifacts/quality_gate_reports/*` | `deliverables/**` |
| `_internal/completeness_validation/*` | `csa_pack/machine/**` |
| `_internal/swarm/*` (status only) | Numbered `01_`–`05_` client MD |
| `csa_pack/{5 named MD, README, arc42-c4/*.html}` **final mode only** | Gate reports inside `csa_pack/` |

If `deliverables/` or `csa_pack/machine/` exist → delete them and fail if they reappear.

## Lane mode procedure

1. `active-root-hygiene`
2. Validate artifact against specialist schema (`business_domains` / `architecture_layers` / etc. — exact schema field names)
3. Evidence + SP/MQ checks
4. Write gate report under `artifacts/quality_gate_reports/`
5. Update `swarm_state.loop` + artifacts_index

## Final mode procedure (packager)

Inputs: accepted `artifacts/{discovery,domain,architecture,lineage,integration}.json`

1. Confirm four specialist gates accepted (join checklist).
2. Render Markdown sections per `csa-section-boundaries` + pack output field expectations in `csa-rich-content` (map from artifact fields; do not invent).
3. Build `csa_pack/arc42-c4/*.html` via `arc42-c4-views` + Mermaid from architecture/integration artifacts.
4. Write `csa_pack/README.md` index linking the five docs + HTML hub.
5. Validate:
   - Only allowed client files under `csa_pack/`
   - No `deliverables/`, no `machine/`
   - Required substance present (or blocking gaps listing missing schema fields)
6. Write `artifacts/quality_gate_reports/gate-csa-document-final.json` (+ optional `_internal/completeness_validation/final.md`)
7. Set `loop.completeness` PASS/FAIL

## Mapping gate → skill

| gate_id | artifact |
|---------|----------|
| gate-discover | artifacts/discovery.json |
| gate-business-domain | artifacts/domain.json |
| gate-tech-architecture | artifacts/architecture.json |
| gate-data-lineage | artifacts/lineage.json |
| gate-integration | artifacts/integration.json |
| gate-csa-document | csa_pack/ (rendered by this agent) |

## Rules

- `max_reruns` = 2
- Prefer missing schema-field remediation over HTML cosmetics
- Do not soft-pass invented stacks
