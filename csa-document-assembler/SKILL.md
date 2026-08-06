---
name: csa-document-assembler
description: Thin-packages lean CSA pack (5 client Markdown docs + arc42/C4 HTML) from accepted specialist artifacts. Use after per-lane gated specialists.
---

# CSA Document Assembler

## Schema

- Manifest: [schema.json](schema.json)
- Section contracts: [output-schemas/](output-schemas/) + [csa-pack-schema-bundle.json](output-schemas/csa-pack-schema-bundle.json)

**HARD:** obey `csa-parallel-lane-gates` (thin render) and `csa-section-boundaries` (fold reference sections into the same five docs).

## Client deliverables (only these)

| File | Purpose |
|------|---------|
| `Executive_Summary.md` | Scope, metrics, readiness, top risks, effort, strategy waves, success metrics |
| `Business_Architecture.md` | Domains/capabilities + flows, dispatch rules, feature flags, provider selection |
| `Application_Architecture.md` | Layers/components, build/runtime, deployment, security, cross-cutting, tech debt + C4 HTML |
| `Data_and_Integration.md` | Stores, entity attributes, lineage, SP logic, integrations, contracts, exceptions, resilience |
| `Risks_Gaps_and_Traceability.md` | Gaps/risks/assumptions, remediations, regression flags, traceability |
| `README.md` | Pack index |
| `arc42-c4/*.html` | C4 / arc42 visual hub |

**Do not generate** numbered `00`/`04`–`10` files, `business_logic.md`, `resilience_gaps.md`, OAS YAML packs, mega `*_Rich_Pack.md`, or epic/story seeds.

## HARD: Thin package (no re-analysis)

1. Read accepted `artifacts/{discovery,domain,architecture,lineage,integration}.json` only.
2. Map fields into `csa_pack/machine/sections/*.json` per output-schemas (fill new substance sections from specialist fields).
3. Render matching `.md` from those JSON files only.
4. Build `arc42-c4/` HTML via `arc42-c4-views` + required Mermaid.
5. Do **not** re-scan source trees or invent inventories.

## Mapping hints (specialist → section)

| Section field | Primary specialist source |
|---------------|---------------------------|
| Exec effort/strategy/success | discovery + architecture debt + risks from all |
| Business flows/dispatch/flags/providers | `domain.json` |
| App deployment/security/cross-cutting/build | `architecture.json` |
| Entity catalog / lineage | `lineage.json` |
| Contracts / exceptions / resilience | `integration.json` |
| Remediations / regression flags | union of specialist gaps + gate warnings |

## Outputs

```text
csa_pack/
  Executive_Summary.md
  Business_Architecture.md
  Application_Architecture.md
  Data_and_Integration.md
  Risks_Gaps_and_Traceability.md
  README.md
  arc42-c4/
  machine/sections/*.json
  machine/*.json
```

Load: `csa-parallel-lane-gates`, `csa-rich-content`, `csa-section-boundaries`, `mermaid-diagrams`, `arc42-c4-views`, `csa-artifact-contract`.

## Rules

- No invented systems/queues/packages.
- Inventories meet schema `minItems` with evidence[].
- SSOT: tables once per owner doc; cross-link elsewhere.
- Write only under ACTIVE_ROOT (`src/`).
