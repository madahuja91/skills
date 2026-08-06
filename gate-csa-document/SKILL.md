---
name: gate-csa-document
description: Quality gate for lean csa_pack — legacy schema content only. Forbids workflow meta, deliverables/, and csa_pack/machine/.
---

# Gate: CSA Document

## Schema

[`schema.json`](schema.json) · policy `csa-rich-content` · ownership `csa-section-boundaries`

## Pass requires

- `ACTIVE_ROOT=src` preferred; `active-root-hygiene` pass
- Shared memory under `_internal/swarm/` (under ACTIVE_ROOT)
- Accepted specialist artifacts
- On disk under **`src/csa_pack/`**:
  - five named Markdown docs + `README.md`
  - `arc42-c4/{index,context,containers,components}.html`
- Pack content = legacy codebase + schema inventories only
- Forbidden: `deliverables/`, `csa_pack/machine/`, workflow meta inside pack

## HARD fail

- Any required `src/csa_pack/` file missing
- Chat-only / gate-report-only final
- Gate id other than `gate-csa-document`

Emit `gate_id: gate-csa-document`.
