---
name: csa-section-boundaries
description: Enforces SSOT across the lean 5-doc CSA pack and HTML index. Use during Assembler and gate-csa-document. Maps reference CSA sections into the same five docs without extras.
---

# CSA Section Boundaries (lean pack)

## Schema

Contract: [`schema.json`](schema.json)

## Single source of truth

| Concern | Owner | Elsewhere |
|---------|-------|-----------|
| Metrics, readiness, top risks, effort, strategy waves, success metrics | `Executive_Summary.md` (+ `index.html`) | Link only |
| Domains, capabilities, glossary, capability flows, dispatch/routing rules, feature flags, provider selection | `Business_Architecture.md` | Link only |
| Layers, components, build/runtime, deployment topology, security controls, cross-cutting (cache/logging/i18n), tech debt | `Application_Architecture.md` + `arc42-c4/` | Link only |
| Stores, entity attribute catalog, lineage, SP rules, integrations, interface contracts, exception maps, resilience posture | `Data_and_Integration.md` | Link only |
| Full risk/gap register, remediations, regression flags, traceability | `Risks_Gaps_and_Traceability.md` | Exec may keep top-5 only |

## Reference pack fold-in (no new client docs)

Map `csa_output_updated` style sections into the five owners:

| Reference section | Fold into |
|-------------------|-----------|
| Executive overview / component inventory highlights / readiness / top risks / effort / strategy / success metrics | `Executive_Summary` |
| Core capabilities / operation-context routing / vendor & billing matrices / feature flags / catalog & E2E flows | `Business_Architecture` |
| Build & runtime / framework / caching-logging-serialization as cross-cutting / security / deployment & infra diagrams | `Application_Architecture` + `arc42-c4` |
| Entity catalog / DB schema attributes / external data sources / data flows / OAS-like contracts / exception→status / resilience posture | `Data_and_Integration` |
| Gap check remediations / resilience critical gaps / regression flags / full risk register | `Risks_Gaps_and_Traceability` |

Do **not** emit separate `business_logic.md`, `resilience_gaps.md`, `exception_http_mapping.md`, `gap_check_report.md`, numbered `00`/`01`/`03`/`04`, or OAS YAML client deliverables.

## Forbidden

- Numbered `00`/`04`–`10` Markdown as client deliverables
- Mega `*_Rich_Pack.md` as the only pack
- Copy-paste catalogs across the 5 docs (Jaccard > 0.32 fails)
- Duplicating integration inventory inside Business Architecture or full entity attributes inside Business Architecture

## Cross-link example

`See [Business Architecture](./Business_Architecture.md) and [HTML hub](./arc42-c4/index.html#domains).`
