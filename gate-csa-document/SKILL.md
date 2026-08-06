---
name: gate-csa-document
description: Quality gate for lean csa_pack — legacy schema content only. Forbids workflow meta, deliverables/, and csa_pack/machine/.
---

# Gate: CSA Document

## Schema

[`schema.json`](schema.json) · policy `csa-rich-content` · ownership `csa-section-boundaries`

## Pass requires

- Single `active_root`; `active-root-hygiene` pass
- Shared memory present under `_internal/swarm/`
- Accepted specialist artifacts under `artifacts/` (JSON SSOT)
- Markdown: five named docs + README under `csa_pack/`
- HTML: `csa_pack/arc42-c4/{index,context,containers,components}.html`
- Pack content is **legacy codebase + schema inventories only**
- **Forbidden paths:** `deliverables/`, `csa_pack/machine/`, numbered `01_`–`05_` packs, gate reports inside `csa_pack/`
- **Forbidden content in `csa_pack/`:** swarm/orchestrator/Completeness/Assembler/lane/join/rework text; gate PASS/FAIL; ACTIVE_ROOT; handoffs; checkpoint; agent remediation briefs
- Substance mapped from artifact schemas; missing required specialist fields are blockers

Emit `gate_id: gate-csa-document`.
