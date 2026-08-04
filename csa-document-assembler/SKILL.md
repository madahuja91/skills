---
name: csa-document-assembler
description: Assembles Hybrid CSA pack — Markdown deliverables with required Mermaid, arc42-C4 HTML index with Mermaid runtime, and Markdown epic/story seeds from accepted machine artifacts. Use when Manager invokes Document Assembler after gated specialists.
---

# CSA Document Assembler

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)


## Goal

Produce industry-standard Current State Architecture documentation for modernization epic/story generation.

## Output format rules (mandatory)

| Deliverable | Format |
|-------------|--------|
| CSA narrative sections (`00`, `04`–`10`) | **Markdown** (`.md`) |
| arc42 / C4 views | **HTML index site** under `csa_pack/arc42-c4/` (skill `arc42-c4-views`) |
| Epic / story seeds | **Markdown** (`.md`) |
| Specialist working copies | `machine/*.json` only (internal tooling — not human primary deliverable) |

Do **not** write C4 content as `.md`. Do **not** write human narrative sections as `.html` except under `arc42-c4/`.

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
  README.md                            # pack index linking MD sections + arc42-c4/index.html
  arc42-c4/
    index.html                         # HTML entry (C4/arc42)
    context.html
    containers.html
    components.html
  epic_story_seeds/
    functions.md
    epics.md
    stories.md
  machine/                             # internal JSON copies for gates/tooling
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

Load skills: `mermaid-diagrams`, `arc42-c4-views`, `ddd-domain-pack`, `data-lineage-pack`, `epic-story-mapping`, `csa-artifact-contract`.

## Procedure

1. Copy accepted machine JSON into `csa_pack/machine/`.
2. Write Markdown sections `00`, `04`–`10` from accepted artifacts (`ddd-domain-pack`, lineage, integration, etc.) and apply **`mermaid-diagrams`** for all required MD diagrams:
   - `00` → `diag-exec-overview`
   - `04` → `diag-domain-context-map`
   - `06` → `diag-lineage-critical`
   - `07` → `diag-integration-landscape`
   - optional: `05` capability map, `08` runtime when evidence exists
3. Build **HTML** C4/arc42 site via `arc42-c4-views` + `mermaid-diagrams` → `csa_pack/arc42-c4/*.html` with required Mermaid C4 diagrams and Mermaid runtime init.
4. Write `machine/mermaid_diagrams.json` inventory conforming to `standards/mermaid-diagrams/schema.json`.
5. In `00_executive_summary.md` and `README.md`, link to `./arc42-c4/index.html` (not to removed C4 `.md` files).
6. Construct `machine/traceability_graph.json`, then write `09_traceability_matrix.md`.
7. Aggregate gaps into `10_gaps_risks_assumptions.md`.
8. Generate **Markdown** epic/story seeds via `epic-story-mapping`.
9. Write `machine/pack_manifest.json` + `machine/quality_gate_summary.json`.

## Rules

- Do not re-analyze the codebase; assemble from accepted artifacts only.
- Every epic/story seed must cite CSA section paths and/or machine IDs.
- Mark assumptions clearly when confidence was pass_with_warnings.
- Required Mermaid diagrams must render correctly (MD fences + HTML `pre.mermaid` + runtime).
