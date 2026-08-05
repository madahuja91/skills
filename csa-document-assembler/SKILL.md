---
name: csa-document-assembler
description: Assembles Hybrid CSA pack — deep Markdown deliverables with required Mermaid, arc42-C4 HTML index with Mermaid runtime, and Markdown epic/story seeds from accepted machine artifacts. Use when Manager invokes Document Assembler after gated specialists.
---

# CSA Document Assembler

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)


## Goal

Produce industry-standard Current State Architecture documentation for modernization epic/story generation — **reference-quality depth**, not stubs.

## Output format rules (mandatory)

| Deliverable | Format |
|-------------|--------|
| CSA narrative sections (`00`, `04`–`10`) | **Markdown** (`.md`) |
| arc42 / C4 views | **HTML index site** under `csa_pack/arc42-c4/` (skill `arc42-c4-views`) |
| Epic / story seeds | **Markdown** (`.md`) |
| Specialist working copies | `machine/*.json` only (internal tooling — not human primary deliverable) |

Do **not** write C4 content as `.md`. Do **not** write human narrative sections as `.html` except under `arc42-c4/`.

## HARD: Rich content + unique sections

Obey skills **`csa-rich-content`** and **`csa-section-boundaries`**.

- Meet word floors with **section-owned** depth — not by pasting the HTML index / discovery rollup into every file.
- `arc42-c4/index.html` = consolidated hub (allowed to summarize all concerns).
- `csa_pack/00`, `04`–`10` = distinct deep-dives; cross-link instead of duplicate.
- Do **not** replace sectioned pack with `*-report.md` or a single mega `*_Rich_Pack.md` as the only Markdown deliverable.

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

Optional when evidence supports: `business_logic.md`, `resilience_gaps.md`, `oas/*.yaml`.

Load skills: `csa-rich-content`, `csa-section-boundaries`, `mermaid-diagrams`, `arc42-c4-views`, `ddd-domain-pack`, `data-lineage-pack`, `csa-artifact-contract`.

## Procedure

1. Copy accepted machine JSON into `csa_pack/machine/`.
2. **Exhaustively expand** Markdown sections `00`, `04`–`10` from accepted artifacts — each section owns only its concern (`csa-section-boundaries`). Put full consolidation in `index.html`. Apply **`mermaid-diagrams`** for required MD diagrams:
   - `00` → `diag-exec-overview`
   - `04` → `diag-domain-context-map`
   - `06` → `diag-lineage-critical`
   - `07` → `diag-integration-landscape`
   - optional: `05` capability map, `08` runtime when evidence exists
3. Build **HTML** C4/arc42 site via `arc42-c4-views` + `mermaid-diagrams` → `csa_pack/arc42-c4/*.html`.
   - **`index.html` is the rich hub** (≥5000 words, ≥8 tables, ≥2 Mermaid, all required anchors) consolidating inventory/stack/domains/data/integrations/C4/runtime/risks/traceability — **as-is CSA**, not TSA migration strategy.
   - `context.html` / `containers.html` / `components.html` deepen C4 (≥800 words each + required Mermaid).
4. Write `machine/mermaid_diagrams.json` inventory conforming to `standards/mermaid-diagrams/schema.json`.
5. In `00_executive_summary.md` and `README.md`, link to `./arc42-c4/index.html` (not to removed C4 `.md` files).
6. Construct `machine/traceability_graph.json`, then write a **wide** `09_traceability_matrix.md`.
7. Aggregate gaps into a **ranked** `10_gaps_risks_assumptions.md` (canonical risk register).
8. Apply **`csa-section-boundaries`**: strip duplicated scorecards/inventories/catalogs from non-owner Markdown; replace with cross-links to owner section or `index.html#…`.
9. Self-check word floors from `csa-rich-content` **and** anti-redundancy from `csa-section-boundaries`; rewrite overlapping sections before finishing.
10. Write `machine/pack_manifest.json` + `machine/quality_gate_summary.json`.

## Rules

- Do not invent systems, queues, packages, or versions.
- You **may and must** expand discovery + specialist JSON into long human docs (tables, inventories, scorecards) **into the owning section / HTML hub only**.
- Do not stop at “see machine/*.json”.
- Do not paste the same Evidence Baseline / readiness scorecard / full domain catalog into every Markdown file.
- Mark assumptions clearly when confidence was pass_with_warnings.
- Required Mermaid diagrams must render correctly (MD fences + HTML `pre.mermaid` + runtime).
- Primary client Markdown lives under `csa_pack/00`–`10` + `README.md` only (plus HTML).
