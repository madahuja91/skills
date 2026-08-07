---
name: gate-csa-document
description: Quality gate for lean 5-doc csa_pack + full arc42-c4 hub with required Mermaid diagrams. Missing diagrams or stub index = FAIL with owner for Manager re-run.
---

# Gate: CSA Document

## Schema

[`schema.json`](schema.json) · `csa-rich-content` · `csa-section-boundaries` · `mermaid-diagrams` · `arc42-c4-views` · pack `output-schemas`

## Who renders

**Completeness-Validation-Agent** renders and runs this gate in the same FINAL turn. No Document Assembler.

## Pass requires

- `ACTIVE_ROOT=src` preferred; shared memory present
- Accepted specialist artifacts schema-complete enough to feed pack
- On disk under **`src/csa_pack/`**:
  - five named MD docs + `README.md`
  - `arc42-c4/{index,context,containers,components}.html`
- **`pack_output_schema_conformance`:** every required field of each output-schema covered in MD
- **Min lines ≥ 200** per client MD; more OK; never a max
- **Mermaid (blocking):**
  - `diag-exec-overview` in Executive_Summary.md
  - `diag-domain-context-map` in Business_Architecture.md
  - `diag-runtime` in Application_Architecture.md
  - `diag-lineage-critical` + `diag-integration-landscape` in Data_and_Integration.md
  - `diag-c4-context|containers|components` on detail HTML pages
  - `index.html` ≥2 Mermaid blocks + classic `mermaid.min.js` + `mermaid.run` (not ESM-only)
- **`index.html` hub:** all 12 required anchors — stub/nav-only index = FAIL
- Pack = legacy evidence only (no workflow meta)

## HARD fail

- Any required pack file missing
- Any required diagram ID missing
- Stub `index.html` / missing anchors / no Mermaid runtime
- Chat-only final
- Numbered `00_`/`04_`–`10_` primary pack, epic-story, deliverables/, machine/

## Remediation → Manager

On fail set `target_agent_id` + `rerun_recommended` + `blocking_gaps` so Manager re-runs that specialist (or Completeness FINAL if render-only gap).

Emit `gate_id: gate-csa-document`.
