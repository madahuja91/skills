---
name: gate-csa-document
description: Quality gate for assembled csa_pack Markdown sections, arc42-C4 HTML index, and machine artifacts. Use after Document Assembler.
---

# Gate: CSA Document

## Schema

Authoritative evaluation contract: [`schema.json`](schema.json)

Pack manifest must also conform to `skills/agents/csa-document-assembler/schema.json`.

## Pass requires

- Markdown sections: `00`, `04`–`10`, `README.md`
- HTML: `arc42-c4/index.html`, `context.html`, `containers.html`, `components.html`
- No C4 Markdown (`01`/`02`/`03`)
- Machine artifacts synced + `traceability_graph.json` + `mermaid_diagrams.json`
- Required Mermaid diagrams present and correctly fenced/rendered (`mermaid-diagrams`):
  - MD: `diag-exec-overview`, `diag-domain-context-map`, `diag-lineage-critical`, `diag-integration-landscape`
  - HTML: `diag-c4-context`, `diag-c4-containers`, `diag-c4-components` with Mermaid runtime on those pages
- Critical gaps documented in `10_gaps_risks_assumptions.md`

Emit report with `gate_id: gate-csa-document`.
