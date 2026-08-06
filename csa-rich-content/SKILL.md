---
name: csa-rich-content
description: Enforces schema-complete CSA specialist JSON and Markdown/HTML packs with structural depth floors (not word fluff). Use for specialists, Assembler, and gate-csa-document.
---

# CSA Output Quality (schema-first + structural depth)

## Schema

Depth and structure contract: [`schema.json`](schema.json)

## Core policy

1. **Schema completeness first**: every required array must meet `minItems` and nested required fields with evidence.
2. **SSOT**: data in tables/diagrams once; insights only as bullets that do not restate table rows.
3. **No stubs**: empty inventories, 1-row catalogs, or “see machine/*.json” fail.
4. **No fluff**: do not pad with repeated paragraphs; expand with real evidenced rows.

## HARD: Specialist list floors (blocking unless evidence exhausted)

If evidence is exhausted, document gaps in `10` and still emit all found rows.

| Artifact | Minimum depth |
|----------|---------------|
| `discovery.json` | Full inventory retained; do not sample-only |
| `domain.json` | ≥3 domains **or** all evidenced; each with ≥1 entity and ≥1 rule when present; ≥8 capabilities |
| `architecture.json` | ≥5 layers **or** all evidenced; ≥12 components across layers when code supports |
| `lineage.json` | ≥3 data stores; ≥10 lineage rows when SQL/code supports; ≥5 SP business rules when SP evidence exists |
| `integration.json` | ≥6 integrations **or** all evidenced endpoints/queues/adapters |

Every list item needs stable ID, name, concise description, and `evidence[]` with real paths.

## HARD: Pack machine JSON then Markdown

Assembler MUST write schema-valid section JSON under `csa_pack/machine/sections/` then render Markdown from those JSON files:

- `00_executive_summary.json` → `00_executive_summary.md`
- `04_domain_model_ddd.json` → `04_domain_model_ddd.md`
- `05_business_capabilities.json` → `05_business_capabilities.md`
- `06_data_architecture_lineage.json` → `06_data_architecture_lineage.md`
- `07_integration_landscape.json` → `07_integration_landscape.md`
- `08_runtime_ops_tech_debt.json` → `08_runtime_ops_tech_debt.md`
- `09_traceability_matrix.json` → `09_traceability_matrix.md`
- `10_gaps_risks_assumptions.json` → `10_gaps_risks_assumptions.md`

Validate each JSON against `skills/agents/csa-document-assembler/output-schemas/*.schema.json`.

## HARD: Structural completeness (not word floors)

Fail when any of these are missed:

1. Required files missing
2. Section machine JSON missing or schema-invalid (`schema_conformance`)
3. Inventory `minItems` not met without documented evidence exhaustion
4. Table/prose duplication or section ownership violation
5. Stub index.html (missing required anchors/tables/Mermaid)

## Completeness enforcement

Completeness validates schema + minItems on machine section JSON and specialist artifacts.  
Do **not** fail on word count. Do **fail** on empty required arrays and missing evidence.
