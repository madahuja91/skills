# Document Assembler Quality Rubric

| Metric | Pass |
|--------|------|
| Markdown sections 00, 04–10 present | required |
| `arc42-c4/index.html` + context/containers/components HTML | required |
| No C4 `.md` files (`01`/`02`/`03`) | required |
| `README.md` links to HTML index | required |
| machine artifacts synced | required |
| traceability_graph.json present | required |
| No epic/story seed outputs | required |
| No silent drops of critical gaps | required |
| **Schema conformance** against `output-schemas/csa-pack-schema-bundle.json` | required (blocking) |
| Executive has inventory tables + readiness scorecard + ≥5 risks | required (blocking) |
| Sections 00, 04–08, 10 each contain evidence-backed tables | required (blocking) |
| `index.html` hub has required anchors + Mermaid runtime + CSA framing | required (blocking) |
| C4 detail pages contain required Mermaid diagrams and valid links | required (blocking) |
| CSA index must not be TSA migration-strategy framed | required (blocking) |
| Markdown sections obey `csa-section-boundaries` (no copy-paste across 00/04–10) | required (blocking) |
| No table-to-prose duplication (SSOT) | required (blocking) |
| Primary pack is `csa_pack/00`–`10` (not mega-pack / `*-report.md` substitutes) | required (blocking) |
