---
name: csa6-data-lineage-pack
description: Standard structure for CSA data architecture and lineage documentation. Use during Data Lineage analysis and Completeness FINAL render of Data_and_Integration.md.
---

# Data Lineage Pack

## Schema

Markdown section contract: [schema.json](schema.json)

## `Data_and_Integration.md` lineage half

1. Data stores inventory
2. System-level flows
3. Critical entity lineage (table or field)
4. Transformation & validation points
5. Data quality risks
6. Gaps (missing DDL, undocumented ETL)

Integration catalog/contracts live in the same file (owned jointly with integration.json).

### Required Mermaid (`mermaid-diagrams`)

Include **`diag-lineage-critical`**: a fenced Mermaid `flowchart LR` (language tag `mermaid`) under System Flows or Critical Entity Lineage. Nodes/edges must come from accepted `lineage.json` only.

Prefer honesty on depth: state `lineage_scope` clearly.