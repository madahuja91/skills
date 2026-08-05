---
name: csa-section-boundaries
description: Enforces separation of concerns across CSA pack Markdown sections and HTML index — no duplicated summaries/evidence dumps. Use during Document Assembler and gate-csa-document.
---

# CSA Section Boundaries (anti-duplication)

## Schema

Contract: [`schema.json`](schema.json)

## Problem this solves

Client packs fail trust when every Markdown file repeats the same executive stack summary, discovery counts, evidence baseline tables, and risk scorecard.  
**`arc42-c4/index.html` may consolidate.** Markdown siblings must be **distinct deep-dives** with cross-links — not copy-paste.

## HARD: Single source of truth

| Concern | Canonical location | Elsewhere |
|---------|-------------------|-----------|
| Full inventory counts / module map | `00_executive_summary.md` **and/or** `index.html#inventory` | Link only — do not reprint full count tables |
| Modernization readiness scorecard | `00` + `index.html#overview` | Link only |
| Full ranked risk register (≥5) | `10_gaps_risks_assumptions.md` (+ short top-5 in `00`/`index`) | Other files: ≤2 risks if needed for local context, else link to `10` |
| DDD domains / entities / rules | `04_domain_model_ddd.md` | Index may summarize; other MD must not re-list all domains |
| Capabilities / flows | `05_business_capabilities.md` | No full capability reprint in `04`/`06`/`07` |
| Data stores / SP transformations / field lineage | `06_data_architecture_lineage.md` | Domain may cite SP **as business rules** without full DDL inventory |
| Integrations (MQ/SOAP/HTTP/CORBA) | `07_integration_landscape.md` | Tech arch mentions adapters briefly; no full integration catalog |
| Layers / components / debt / EOL | `08_runtime_ops_tech_debt.md` + architecture facts in `00`/`index#stack` | Domain must not own framework/EOL matrices |
| Traceability matrices | `09_traceability_matrix.md` | Others link |
| Rich consolidated HTML hub | `arc42-c4/index.html` | MD sections deepen one concern; do not mirror entire index |

## Per-section MUST / MUST-NOT

### `00_executive_summary.md`
- **MUST:** scope, inventory highlights, stack snapshot, readiness scorecard, top risks, link to `arc42-c4/index.html`
- **MUST-NOT:** full domain entity catalogs, full field-lineage tables, full MQ/API catalogs

### `04_domain_model_ddd.md`
- **MUST:** bounded contexts, ubiquitous language, entities/aggregates, business rules (incl. SP-as-rules), context-map Mermaid
- **MUST-NOT:** framework version matrices, HTTP/MQ payload catalogs, full DDL column dumps, discovery extension-count tables, readiness scorecard reprint

### `05_business_capabilities.md`
- **MUST:** capability inventory, actors, flows, screen/capability mapping
- **MUST-NOT:** C4 container catalogs, full SP transformation inventories, tech-debt EOL tables

### `06_data_architecture_lineage.md`
- **MUST:** stores, DDL/entities, SP/iBATIS transformation nodes, field lineage, data-quality risks, lineage Mermaid
- **MUST-NOT:** DDD ubiquitous-language essays, executive roadmap, UI framework versions, full integration broker catalog

### `07_integration_landscape.md`
- **MUST:** external I/O catalog (MQ/SOAP/HTTP/CORBA/files), contracts/queues, reliability gaps, landscape Mermaid
- **MUST-NOT:** internal DDL schemas as primary content, DDD aggregate catalogs, discovery file-extension rollups

### `08_runtime_ops_tech_debt.md`
- **MUST:** runtime/packaging evidence, debt register, ops/resilience gaps
- **MUST-NOT:** full business-capability maps, full lineage field tables

### `09_traceability_matrix.md`
- **MUST:** matrices linking IDs across domains/capabilities/components/integrations/lineage
- **MUST-NOT:** narrative reprints of `04`–`08`

### `10_gaps_risks_assumptions.md`
- **MUST:** ranked gaps/risks/assumptions/missing evidence
- **MUST-NOT:** full positive inventories already in `00`/`index`

### `arc42-c4/index.html`
- **MUST:** rich hub with required anchors (see `arc42-c4-views`)
- **MAY:** summarize all concerns
- Markdown files still must remain unique deep-dives (index summary ≠ license to duplicate into every `.md`)

## Cross-link rule

When another section already owns a table, write:

`See [Inventory](./00_executive_summary.md) and [HTML hub](./arc42-c4/index.html#inventory).`

Do **not** paste the table again.

## Forbidden client deliverable shapes

Do **not** ship parallel client reports that mirror the same content under other names as the primary pack, e.g.:

- `output/discovery-report.md`, `business-domain-report.md`, … **as substitutes** for `csa_pack/00`–`10`
- A single mega `CCDS_CSA_Rich_Pack.md` **instead of** sectioned `csa_pack/*.md`

Specialist working notes, if any, belong under `_internal/` only. Client pack = `csa_pack/` (+ HTML).

## Anti-redundancy gate (blocking)

`gate-csa-document` / Completeness MUST fail when:

1. Any pair of `00`,`04`–`10` Markdown files has token Jaccard similarity **> 0.32** (after lowercasing; ignore pure Mermaid fences if needed), OR
2. The same owned artifact appears in ≥2 Markdown files:
   - full “Exact Counts by Extension” / discovery rollup tables outside `00`
   - full “Modernization readiness scorecard” outside `00`
   - full bounded-context catalog outside `04`
   - full integration catalog outside `07`
   - full field-lineage/SP transformation inventory outside `06`
3. Assembler omitted `csa_pack/00`–`10` and only wrote a mega-pack or specialist `*-report.md` files

Emit `check_id: section_anti_redundancy` with observed pair scores / duplicated headings.
