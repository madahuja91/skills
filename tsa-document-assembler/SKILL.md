---
name: tsa-document-assembler
description: Assembles TSA pack Markdown + arc42-C4 HTML with Mermaid, migration roadmap, and epic/story seeds from accepted TSA artifacts. Use when Manager invokes TSA Assembler.
---

# TSA Document Assembler

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Outputs

```text
tsa_pack/
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
