---
name: gate-csa-document
description: Quality gate for assembled csa_pack Markdown sections, arc42-C4 HTML index, rich narrative depth, and machine artifacts. Use after Document Assembler.
---

# Gate: CSA Document

## Schema

Authoritative evaluation contract: [`schema.json`](schema.json)

Pack manifest must also conform to `skills/agents/csa-document-assembler/schema.json`.
Depth floors: skill **`csa-rich-content`**.

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
- **Richness (blocking):** word-count every required MD/HTML file against `csa-rich-content` floors; fail stubs
- **Executive richness (blocking):** inventory/component tables, modernization readiness scorecard, ≥5 risks with mitigation
- **Tables (blocking):** Markdown tables in `00`, `04`–`08`, `10`
- **`index.html` hub (blocking):** ≥5000 words, ≥8 tables, ≥2 Mermaid + runtime, all required anchors (`overview`…`pack`); as-is CSA framing (no TSA migration-strategy body). Stub nav-only index fails (`index_html_hub_richness`)
- **Anti-redundancy (blocking):** obey `csa-section-boundaries` — fail Jaccard > 0.32 between Markdown siblings or duplicated owned catalogs (`section_anti_redundancy`)
- **Pack shape (blocking):** `csa_pack/00`–`10` present; mega-pack-only or `*-report.md` substitutes without sectioned pack = fail

Emit report with `gate_id: gate-csa-document`. Observed fields must include measured word counts / table / Mermaid counts / pair similarity when failing depth or redundancy checks.
