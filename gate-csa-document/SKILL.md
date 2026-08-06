---
name: gate-csa-document
description: Quality gate for assembled csa_pack Markdown sections, arc42-C4 HTML index, rich narrative depth, and machine artifacts. Use after Document Assembler.
---

# Gate: CSA Document

## Schema

Authoritative evaluation contract: [`schema.json`](schema.json)

Pack manifest must also conform to `skills/agents/csa-document-assembler/schema.json`.
Schema and SSOT policy: skill **`csa-rich-content`**.

## Pass requires

- Pack under single `active_root` only (no `src/src`; `active-root-hygiene` pass)
- Markdown sections: `00`, `04`–`10`, `README.md` (**Markdown only**)
- HTML: `arc42-c4/index.html`, `context.html`, `containers.html`, `components.html` (**HTML only** — never C4 `.md`)
- No C4 Markdown (`01`/`02`/`03`)
- Machine artifacts synced + `traceability_graph.json` + `mermaid_diagrams.json`
- Required Mermaid diagrams present and correctly fenced/rendered (`mermaid-diagrams`):
  - MD: `diag-exec-overview`, `diag-domain-context-map`, `diag-lineage-critical`, `diag-integration-landscape`
  - HTML: `diag-c4-context`, `diag-c4-containers`, `diag-c4-components` with Mermaid runtime on those pages
- Critical gaps documented in `10_gaps_risks_assumptions.md`
- **Schema conformance (blocking):** validate mapped section artifacts against `skills/agents/csa-document-assembler/output-schemas/csa-pack-schema-bundle.json`
- **SSOT compliance (blocking):** table facts appear once in owner sections; no paragraph restatement of table rows (`table_prose_duplication`)
- **`index.html` hub (blocking):** required anchors (`overview`…`pack`), Mermaid runtime, and CSA framing (no TSA migration-strategy body)
- **Anti-redundancy (blocking):** obey `csa-section-boundaries` — fail Jaccard > 0.32 between Markdown siblings or duplicated owned catalogs (`section_anti_redundancy`)
- **Pack shape (blocking):** `csa_pack/00`–`10` present; mega-pack-only or `*-report.md` substitutes without sectioned pack = fail

Emit report with `gate_id: gate-csa-document`. Observed fields must include failed schema paths, duplicated ownership evidence, table-prose duplication evidence, and pair similarity when redundancy checks fail.
