---
name: csa-section-boundaries
description: Enforces SSOT across the lean 5-doc CSA pack and HTML index. Use during Assembler and gate-csa-document.
---

# CSA Section Boundaries (lean pack)

## Schema

Contract: [`schema.json`](schema.json)

## Single source of truth

| Concern | Owner | Elsewhere |
|---------|-------|-----------|
| Metrics, readiness, top risks | `Executive_Summary.md` (+ `index.html`) | Link only |
| Domains, capabilities, glossary | `Business_Architecture.md` | Link only |
| Layers, components, runtime, tech debt | `Application_Architecture.md` + `arc42-c4/` | Link only |
| Stores, lineage, SP rules, integrations | `Data_and_Integration.md` | Link only |
| Full risk/gap register + traceability | `Risks_Gaps_and_Traceability.md` | Exec may keep top-5 only |

## Forbidden

- Numbered `00`/`04`–`10` Markdown as client deliverables
- Mega `*_Rich_Pack.md` as the only pack
- Copy-paste catalogs across the 5 docs (Jaccard > 0.32 fails)

## Cross-link example

`See [Business Architecture](./Business_Architecture.md) and [HTML hub](./arc42-c4/index.html#domains).`
