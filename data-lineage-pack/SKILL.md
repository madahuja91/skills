---
name: data-lineage-pack
description: Standard structure for CSA data architecture and lineage documentation. Use during Data Lineage analysis and Assembler section 06.
---

# Data Lineage Pack

## Schema

Markdown section contract: [schema.json](schema.json)

## Section 06 outline

1. Data stores inventory
2. System-level flows
3. Critical entity lineage (table or field)
4. Transformation & validation points
5. Data quality risks
6. Gaps (missing DDL, undocumented ETL)

### Required Mermaid (`mermaid-diagrams`)

Include **`diag-lineage-critical`**: a fenced Mermaid `flowchart LR` (language tag `mermaid`) under System Flows or Critical Entity Lineage. Nodes/edges must come from accepted `lineage.json` only.

Prefer honesty on depth: state `lineage_scope` clearly.