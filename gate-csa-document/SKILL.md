---
name: gate-csa-document
description: Quality gate for assembled csa_pack machine section JSON, Markdown sections, arc42-C4 HTML, structural depth floors, and SSOT. Use after Document Assembler.
---

# Gate: CSA Document

## Schema

Authoritative evaluation contract: [`schema.json`](schema.json)

Pack manifest must also conform to `skills/agents/csa-document-assembler/schema.json`.
Schema and structural-depth policy: skill **`csa-rich-content`**.

## Pass requires

- Pack under single `active_root` only (no `src/src`; `active-root-hygiene` pass)
- **Machine section JSON first:** all of `csa_pack/machine/sections/{00,04,05,06,07,08,09,10}_*.json` present and schema-valid
- Markdown sections: `00`, `04`–`10`, `README.md` rendered from those JSON files
- HTML: `arc42-c4/index.html`, `context.html`, `containers.html`, `components.html`
- No C4 Markdown (`01`/`02`/`03`)
- Machine artifacts synced + `traceability_graph.json` + `mermaid_diagrams.json`
- Required Mermaid diagrams present (`mermaid-diagrams`)
- Critical gaps documented in `10_gaps_risks_assumptions.md`
- **Schema conformance (blocking):** validate section machine JSON against `output-schemas/*.schema.json` via `csa-pack-schema-bundle.json`
- **Section min rows (blocking):** enforce `csa-rich-content.section_min_rows` (not word counts)
- **SSOT (blocking):** table facts once in owner sections; no paragraph restatement of table rows
- **`index.html` hub (blocking):** required anchors, Mermaid runtime, CSA framing
- **Anti-redundancy (blocking):** `csa-section-boundaries` — Jaccard > 0.32 fails
- **Pack shape (blocking):** sectioned `csa_pack/00`–`10` present (mega-pack-only fails)

Do **not** fail on word count. Do **fail** on empty/`minItems`-short inventories without evidence-exhaustion gaps in `10`.

Emit report with `gate_id: gate-csa-document`. Observed fields must include failed schema paths, missing section JSON, min-row shortfalls, duplication evidence, and pair similarity when redundancy checks fail.
