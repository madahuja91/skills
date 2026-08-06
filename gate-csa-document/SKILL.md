---
name: gate-csa-document
description: Quality gate for lean csa_pack rendered by Completeness from artifacts. Forbids deliverables/ and csa_pack/machine/.
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
- **Forbidden:** `deliverables/`, `csa_pack/machine/`, numbered `01_`–`05_` packs, gate reports inside `csa_pack/`
- Pack rendered by Completeness (no Document Assembler)
- Substance mapped from artifact schemas; missing required specialist fields are blockers

Emit `gate_id: gate-csa-document`.
