---
name: csa-rich-content
description: Enforces deep, long-form CSA specialist JSON and Markdown/HTML pack narratives (reference-quality depth). Use for every specialist write and Document Assembler / gate-csa-document validation.
---

# CSA Rich Content (mandatory depth)

## Schema

Depth contract: [`schema.json`](schema.json)

Thin stub summaries that only satisfy file presence **FAIL**. Target quality is reference packs like multi-thousand-word executive summaries, capability maps, tech-stack analyses, and risk reports — not outline bullets.

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
| `00_executive_summary.md` | 1200 | Component/inventory tables; tech stack summary; migration readiness scorecard with scored dimensions; top ≥5 risks with impact + mitigation; evidence/confidence; Mermaid overview |
| `04_domain_model_ddd.md` | 900 | Per-domain sections (purpose, ubiquitous language, entities table, rules table, dependencies); context-map Mermaid |
| `05_business_capabilities.md` | 800 | Capability inventory table; per-capability flows/actors/systems/evidence; optional capability Mermaid |
| `06_data_architecture_lineage.md` | 900 | Sources table; critical field lineage tables; transformation/SP call chains; quality/security risks; lineage Mermaid |
| `07_integration_landscape.md` | 900 | Integration catalog table; inbound/outbound flows; MQ/SOAP/HTTP/CORBA detail when evidenced; reliability gaps; landscape Mermaid |
| `08_runtime_ops_tech_debt.md` | 700 | Runtime/packaging evidence; debt register with severity; resilience/ops gaps; open questions |
| `09_traceability_matrix.md` | 500 | Wide matrices (capability↔component↔integration↔lineage↔epic); not a 5-row stub |
| `10_gaps_risks_assumptions.md` | 800 | Ranked risks; assumptions; missing evidence; remediation themes |
| `README.md` | 200 | Index of all sections + link to `arc42-c4/index.html` |
| `epic_story_seeds/functions.md` | 400 | One section per major capability/domain |
| `epic_story_seeds/epics.md` | 600 | ≥5 epics with CSA refs |
| `epic_story_seeds/stories.md` | 900 | ≥10 stories with acceptance-criteria hooks + CSA refs |

## HARD: HTML C4 (`arc42-c4/`)

Each of `index.html`, `context.html`, `containers.html`, `components.html`:

- ≥400 words of explanatory HTML prose **plus** required Mermaid diagram(s) with runtime init
- Named actors/systems/containers/components from accepted artifacts — not 3-box toy diagrams

## Assembler expansion rules

1. **Expand, do not paraphrase.** Turn every domain, capability, component, integration, and lineage row into tables and prose.
2. Use `discovery.json` inventory counts and representative paths to build executive inventory tables (languages, modules, WAR/EAR, SQL/packages, MQ, CORBA, configs).
3. **Do not invent** facts. If evidence is thin, write a long **Gaps / Unknowns** section and still meet word floors with evidenced detail + explicit unknowns.
4. Optional rich extras (when evidence exists): `csa_pack/business_logic.md`, `csa_pack/resilience_gaps.md`, OpenAPI-ish stubs under `csa_pack/oas/*.yaml` for evidenced service boundaries.
5. Anti-patterns that **fail** depth: outline-only bullets, “see machine/*.json”, single short paragraph per section, diagrams with unlabeled boxes only.

## Completeness / gate enforcement

For `gate-csa-document`, Completeness MUST:

1. Word-count each required Markdown/HTML file.
2. Fail if any floor in this skill is missed (`check_id: narrative_depth_minimums`).
3. Fail if executive summary lacks scorecard **or** ≥5 risks (`check_id: executive_richness`).
4. Fail if major MD sections lack at least one Markdown table (`check_id: narrative_tables_present`) for 00, 04–08, 10.

Specialist gates SHOULD fail shallow lists (few empty descriptions, missing evidence) even if schema-valid.
