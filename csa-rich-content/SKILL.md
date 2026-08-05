---
name: csa-rich-content
description: Enforces deep, long-form CSA specialist JSON and Markdown/HTML pack narratives (reference-quality depth). Use for every specialist write and Document Assembler / gate-csa-document validation.
---

# CSA Rich Content (mandatory depth)

## Schema

Depth contract: [`schema.json`](schema.json)

Thin stub summaries that only satisfy file presence **FAIL**. Target quality is reference packs like multi-thousand-word executive summaries and a **rich arc42 `index.html` hub** — not outline bullets.

## HARD: Specialist machine JSON (before Completeness pass)

Expand evidence-backed inventories. Prefer more real rows over short prose.

| Artifact | Minimum depth (blocking unless evidence truly exhausted — then document gaps) |
|----------|--------------------------------------------------------------------------------|
| `discovery.json` | Full inventory retained; do not collapse to a handful of sample files |
| `domain.json` | ≥6 domains **or** all evidenced domains; each with ≥3 entities and ≥2 business rules when code/DDL supports it; ≥8 capabilities with description + evidence |
| `architecture.json` | ≥5 layers; ≥12 components across layers; C4 context/containers/components with named elements + evidence; debt categories with concrete examples |
| `lineage.json` | ≥8 data sources **or** all evidenced; ≥15 field_lineage rows when schema/SQL/code supports; transformations with SP/package call evidence |
| `integration.json` | ≥8 integrations **or** all evidenced endpoints/queues/adapters; each with pattern, direction, endpoints/queues, reliability gaps, evidence |

Every list item needs: stable ID, human name, 2–4 sentence description, `evidence[]` with real paths. Never invent systems.

## HARD: Markdown pack minimums (`csa_pack/`)

Count **words** in each file (Assembler + `gate-csa-document`). Below floor = **fail** (blocking).

| File | Min words | Required substance (must include) |
|------|-----------|-----------------------------------|
| `00_executive_summary.md` | 1200 | Component/inventory tables; tech stack summary; modernization readiness scorecard; top ≥5 risks with impact + mitigation; evidence/confidence; Mermaid overview |
| `04_domain_model_ddd.md` | 900 | Per-domain sections (purpose, ubiquitous language, entities table, rules table, dependencies); context-map Mermaid |
| `05_business_capabilities.md` | 800 | Capability inventory table; per-capability flows/actors/systems/evidence; optional capability Mermaid |
| `06_data_architecture_lineage.md` | 900 | Sources table; critical field lineage tables; transformation/SP call chains; quality/security risks; lineage Mermaid |
| `07_integration_landscape.md` | 900 | Integration catalog table; inbound/outbound flows; MQ/SOAP/HTTP/CORBA detail when evidenced; reliability gaps; landscape Mermaid |
| `08_runtime_ops_tech_debt.md` | 700 | Runtime/packaging evidence; debt register with severity; resilience/ops gaps; open questions |
| `09_traceability_matrix.md` | 500 | Wide matrices (capability↔component↔integration↔lineage); not a 5-row stub |
| `10_gaps_risks_assumptions.md` | 800 | Ranked risks; assumptions; missing evidence; remediation themes |
| `README.md` | 200 | Index of all sections + prominent link to `arc42-c4/index.html` as primary HTML hub |

Do **not** require `epic_story_seeds/` (out of scope).

## HARD: HTML C4 — rich `index.html` hub

Obey `arc42-c4-views`.

| File | Min words (text) | Extra blocking checks |
|------|------------------|------------------------|
| `arc42-c4/index.html` | **5000** | ≥8 `<table>`; ≥2 Mermaid blocks + runtime; all anchors: overview, inventory, stack, architecture, domains, data, integrations, c4, runtime, risks, traceability, pack; CSA framing (as-is) — no TSA migration-strategy body |
| `arc42-c4/context.html` | 800 | Mermaid `diag-c4-context` + runtime |
| `arc42-c4/containers.html` | 800 | Mermaid `diag-c4-containers` + runtime |
| `arc42-c4/components.html` | 800 | Mermaid `diag-c4-components` + runtime |

`index.html` must consolidate CSA information (inventory, stack, domains, data, integrations, C4, debt, risks, traceability). Detail pages deepen C4; they do not replace the hub.

## Assembler expansion rules

1. **Expand, do not paraphrase.** Turn every domain, capability, component, integration, and lineage row into tables and prose in **both** Markdown and the HTML index hub.
2. Use `discovery.json` inventory counts and representative paths for executive + `#inventory` tables.
3. **Do not invent** facts. Thin evidence → long Gaps sections with explicit unknowns — still meet floors.
4. Anti-patterns that **fail**: stub index with only nav links; “see machine/*.json”; unlabeled 3-box diagrams; TSA migration/effort/target-microservice sections inside CSA index.

## Completeness / gate enforcement

For `gate-csa-document`, Completeness MUST:

1. Word-count each required Markdown/HTML file.
2. Fail if any floor in this skill is missed (`narrative_depth_minimums`).
3. Fail if executive summary lacks scorecard **or** ≥5 risks (`executive_richness`).
4. Fail if major MD sections lack ≥1 Markdown table (`narrative_tables_present`) for 00, 04–08, 10.
5. Fail if `index.html` missing required anchors, table/Mermaid floors, or is a stub hub (`index_html_hub_richness`).

Specialist gates SHOULD fail shallow lists even if schema-valid.
