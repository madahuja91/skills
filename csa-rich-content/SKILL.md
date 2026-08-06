---
name: csa-rich-content
description: Enforces lean schema-complete CSA pack (5 docs) with structural depth floors. Use for specialists, Assembler, and gate-csa-document.
---

# CSA Output Quality (lean pack + structural depth)

## Schema

Depth contract: [`schema.json`](schema.json)

## Client pack (only)

1. `Executive_Summary.md`
2. `Business_Architecture.md`
3. `Application_Architecture.md`
4. `Data_and_Integration.md`
5. `Risks_Gaps_and_Traceability.md`
6. `README.md` + `arc42-c4/*.html`

No numbered `00`/`04`–`10` files. No mega-pack substitutes.

## Core policy

1. Schema completeness first (`minItems` + evidence + substance sections).
2. SSOT: tables once; insight bullets only (`csa-section-boundaries`).
3. No stubs / empty inventories.
4. Machine JSON under `csa_pack/machine/sections/` then render MD.
5. Same five client docs only — fold reference sections into owners; never add documents.

## Specialist list floors

| Artifact | Minimum depth |
|----------|---------------|
| `domain.json` | ≥3 domains; ≥8 capabilities; dispatch/feature/provider/workflow fields when evidenced |
| `architecture.json` | ≥5 layers; dense components; deployment + security + cross-cutting |
| `lineage.json` | ≥3 stores; ≥10 lineage rows; entity_catalog with attributes |
| `integration.json` | ≥6 integrations; contracts + exception maps + resilience posture |

## Blocking checks

required files, section machine JSON, schema conformance, section_min_rows (including substance sections), specialist_list_depth, SSOT, index hub richness, anti-redundancy, pack shape.

Prefer substance schema failures over cosmetic-only HTML/Jaccard fails when inventories are complete.

Do **not** fail on word count.
