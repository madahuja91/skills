---
name: csa5-ddd-domain-pack
description: DDD structuring for CSA domain model — bounded contexts, aggregates, entities, and business rules as Markdown. Use during Business Domain analysis and Completeness FINAL render of Business_Architecture.md.
---

# DDD Domain Pack

## Schema

Markdown section contract: [schema.json](schema.json)

## Mapping

| DDD | CSA field |
|-----|-----------|
| Bounded context | `business_domains[]` (`DOM-*`) |
| Aggregate / Entity / VO | `entities[]` |
| Domain service | entity_type `service` or capability |
| Invariant / policy | `business_rules[]` (`BR-*`) |
| Context map | `cross_domain_dependencies` |

## Writing `Business_Architecture.md` (Markdown)

For each domain: purpose, ubiquitous language (canonical names), entities, key rules with evidence links, upstream/downstream contexts. Capabilities and flows belong in this same owner doc.

### Required Mermaid (`mermaid-diagrams`)

Include **`diag-domain-context-map`**: a fenced Mermaid `flowchart` (language tag `mermaid`) under **Context Map** showing bounded contexts and upstream/downstream edges from `cross_domain_dependencies` / domain evidence. Do not invent contexts.

Link to C4 HTML via `../arc42-c4/index.html` for container/component views — do not duplicate C4 diagrams here.