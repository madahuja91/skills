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

1. Schema completeness first (`minItems` + evidence).
2. SSOT: tables once; insight bullets only.
3. No stubs / empty inventories.
4. Machine JSON under `csa_pack/machine/sections/` then render MD.

## Specialist list floors

| Artifact | Minimum depth |
|----------|---------------|
| `domain.json` | ≥3 domains or all evidenced; ≥8 capabilities |
| `architecture.json` | ≥5 layers or all evidenced; dense components |
| `lineage.json` | ≥3 stores; ≥10 lineage rows when SQL/code supports |
| `integration.json` | ≥6 integrations or all evidenced |

## Blocking checks

required files, section machine JSON, schema conformance, section_min_rows, specialist_list_depth, SSOT, index hub richness, anti-redundancy, pack shape.

Do **not** fail on word count.
