---
name: tsa-document-assembler
description: Assembles TSA pack Markdown + arc42-C4 HTML with Mermaid, migration roadmap, and epic/story seeds from accepted TSA artifacts. Use when Manager invokes TSA Assembler.
---

# TSA Document Assembler

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Output format (mandatory)

| Deliverable | Format |
|-------------|--------|
| Sections `00`, `01`, `04`–`10`, README, epic/story seeds | **Markdown** (`.md`) |
| arc42 / C4 views | **HTML only** under `tsa_pack/arc42-c4/` (`index.html` + pages) |
| Specialist copies | `machine/*.json` (internal) |

Do **not** write C4 as `.md`. Do **not** write narrative sections as `.html` except under `arc42-c4/`.

Write everything under the single `swarm_state.active_root` on disk (no `src/src`). Never invent `/app/temp/csa-run` or a sibling `outputs/` tree outside ACTIVE_ROOT.

## Outputs

```text
ACTIVE_ROOT/tsa_pack/
  00_executive_summary.md
  01_target_stack_decisions.md
  04_target_domain_model.md
  05_target_capabilities.md
  06_target_data_architecture.md
  07_target_integration.md
  08_migration_strategy_roadmap.md
  09_traceability_csa_to_tsa.md
  10_risks_assumptions.md
  README.md
  arc42-c4/index.html (+ context/containers/components)
  epic_story_seeds/*.md
  machine/*.json
  machine/mermaid_diagrams.json
```

## Required Mermaid

exec overview, domain map, data flow, integration, migration waves, plus C4 HTML diagrams (`mermaid-diagrams`).
