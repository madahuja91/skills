---
name: csa-document-assembler
description: Assembles lean CSA pack (5 client Markdown docs + arc42/C4 HTML) from accepted specialist artifacts. Use after gated specialists.
---

# CSA Document Assembler

## Schema

- Manifest: [schema.json](schema.json)
- Section contracts: [output-schemas/](output-schemas/) + [csa-pack-schema-bundle.json](output-schemas/csa-pack-schema-bundle.json)

## Client deliverables (only these)

Clients need Current State Architecture to answer: what exists, how business maps, how it is built, how data/integrations move, what blocks modernization.

| File | Purpose |
|------|---------|
| `Executive_Summary.md` | Scope, metrics, readiness, top findings/risks |
| `Business_Architecture.md` | Domains/DDD + capabilities |
| `Application_Architecture.md` | Layers/components/runtime/tech debt + link to C4 HTML |
| `Data_and_Integration.md` | Stores, lineage, SP logic, integrations |
| `Risks_Gaps_and_Traceability.md` | Gaps/risks/assumptions + capability→component→integration→lineage links |
| `README.md` | Pack index |
| `arc42-c4/*.html` | C4 / arc42 visual hub (not duplicate Markdown) |

**Do not generate** numbered `00`/`04`–`10` files, mega `*_Rich_Pack.md`, epic/story seeds, or other narrative extras.

## HARD: Machine JSON then Markdown

1. Write schema-valid JSON under `csa_pack/machine/sections/`:
   - `Executive_Summary.json`
   - `Business_Architecture.json`
   - `Application_Architecture.json`
   - `Data_and_Integration.json`
   - `Risks_Gaps_and_Traceability.json`
2. Render matching `.md` from those JSON files only.
3. Build `arc42-c4/` HTML via `arc42-c4-views` + required Mermaid diagrams.

## Inputs

Accepted: `artifacts/{discovery,domain,architecture,lineage,integration}.json` + quality gate summary.

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
    index.html
    context.html
    containers.html
    components.html
  machine/
    sections/*.json
    discovery.json
    domain.json
    architecture.json
    lineage.json
    integration.json
    mermaid_diagrams.json
    traceability_graph.json
    quality_gate_summary.json
    pack_manifest.json
```

Load: `csa-rich-content`, `csa-section-boundaries`, `mermaid-diagrams`, `arc42-c4-views`, `csa-artifact-contract`.

## Rules

- No invented systems/queues/packages.
- Inventories meet schema `minItems` with evidence[]; expand rows, not fluff.
- SSOT: tables once per owner doc; cross-link elsewhere.
- Write only under ACTIVE_ROOT (`src/`).
