---
name: csa-document-assembler
description: Assembles Hybrid CSA pack from accepted artifacts using machine-JSON-first, schema-complete Markdown + arc42/C4 HTML. Use when Manager invokes Document Assembler after gated specialists.
---

# CSA Document Assembler

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

Per-section machine contracts: [output-schemas/](output-schemas/) + [csa-pack-schema-bundle.json](output-schemas/csa-pack-schema-bundle.json)

## Goal

Produce industry-standard Current State Architecture documentation with strict schema conformance, structural inventory depth, and zero table/prose duplication.

## Output format rules (mandatory)

| Deliverable | Format |
|-------------|--------|
| Section machine JSON (`00`, `04`–`10`) | **JSON** under `csa_pack/machine/sections/` (schema-validated first) |
| CSA narrative sections (`00`, `04`–`10`) | **Markdown** rendered from those JSON files |
| arc42 / C4 views | **HTML** under `csa_pack/arc42-c4/` (skill `arc42-c4-views`) |
| Specialist copies | `csa_pack/machine/{discovery,domain,architecture,lineage,integration}.json` |

Do **not** write C4 content as `.md`. Do **not** invent Markdown without writing the matching section JSON first.

## HARD: Machine JSON then Markdown

1. Build each section object to pass the matching `output-schemas/*.schema.json` (`minItems`, required fields, evidence).
2. Write `csa_pack/machine/sections/{id}.json`.
3. Render `csa_pack/{id}.md` from that JSON only (tables for inventories; bullets for insights).
4. Fail if MD exists without valid section JSON, or if any `minItems` floor is missed without documented evidence exhaustion in `10`.

Industry floors (blocking unless evidence exhausted and logged in `10`):

| Section | Key floor |
|---------|-----------|
| `00` | ≥5 metrics, ≥4 scorecard dims, ≥5 findings, ≥5 risks |
| `04` | ≥3 bounded contexts, ≥8 glossary terms |
| `05` | ≥8 capabilities |
| `06` | ≥3 stores, ≥10 lineage rows, ≥5 SP rules when SP evidence exists |
| `07` | ≥6 integrations |
| `08` | ≥5 tech-debt items, ≥3 runtime evidence rows |
| `09` | ≥10 traceability links |
| `10` | ≥5 gaps, ≥5 risks, ≥3 assumptions |

## HARD: Rich content + unique sections

Obey **`csa-rich-content`** and **`csa-section-boundaries`**.

- Meet **structural depth floors** (row/list `minItems`) — not word fluff.
- `arc42-c4/index.html` = consolidated hub.
- `csa_pack/00`, `04`–`10` = distinct deep-dives; cross-link instead of duplicate.
- Do **not** replace sectioned pack with mega `*_Rich_Pack.md` only.

## Inputs (accepted only)

- `artifacts/discovery.json`
- `artifacts/domain.json`
- `artifacts/architecture.json`
- `artifacts/lineage.json`
- `artifacts/integration.json`
- `artifacts/quality_gate_reports/**` (summary)

## Outputs

```text
csa_pack/
  00_executive_summary.md
  04_domain_model_ddd.md
  05_business_capabilities.md
  06_data_architecture_lineage.md
  07_integration_landscape.md
  08_runtime_ops_tech_debt.md
  09_traceability_matrix.md
  10_gaps_risks_assumptions.md
  README.md
  arc42-c4/
    index.html
    context.html
    containers.html
    components.html
  machine/
    sections/
      00_executive_summary.json
      04_domain_model_ddd.json
      05_business_capabilities.json
      06_data_architecture_lineage.json
      07_integration_landscape.json
      08_runtime_ops_tech_debt.json
      09_traceability_matrix.json
      10_gaps_risks_assumptions.json
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

Load skills: `csa-rich-content`, `csa-section-boundaries`, `mermaid-diagrams`, `arc42-c4-views`, `ddd-domain-pack`, `data-lineage-pack`, `csa-artifact-contract`.

## Procedure

1. Copy accepted specialist JSON into `csa_pack/machine/`.
2. **Populate** `machine/sections/*.json` from specialist artifacts until each passes its schema (`minItems` + evidence).
3. Render Markdown `00`, `04`–`10` from those section JSON files with section ownership. Apply **`mermaid-diagrams`**:
   - `00` → `diag-exec-overview`
   - `04` → `diag-domain-context-map`
   - `06` → `diag-lineage-critical`
   - `07` → `diag-integration-landscape`
4. Build **HTML** C4/arc42 site via `arc42-c4-views`.
5. Write `machine/mermaid_diagrams.json`, `machine/traceability_graph.json`.
6. Aggregate gaps into ranked `10` (JSON + MD).
7. Apply **`csa-section-boundaries`** (cross-link; no catalog paste).
8. Validate against `output-schemas/csa-pack-schema-bundle.json`.
9. Write `machine/pack_manifest.json` + `machine/quality_gate_summary.json`.

## Rules

- Do not invent systems, queues, packages, or versions.
- Expand inventories with evidenced rows — do not stop at sample stubs.
- Do not stop at “see machine/*.json”.
- Mark assumptions when confidence was pass_with_warnings.
- **HARD disk rule:** write every file under `swarm_state.active_root` using relative paths. Never invent external output trees outside ACTIVE_ROOT.
