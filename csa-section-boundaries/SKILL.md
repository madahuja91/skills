---
name: csa-section-boundaries
description: SSOT for lean 5-doc CSA pack rendered by Completeness from artifacts. Forbids deliverables/ and csa_pack/machine duplicates.
---

# CSA Section Boundaries (lean pack)

## Schema

[`schema.json`](schema.json)

## Single source of truth

| Concern | Artifact SSOT | Client owner doc |
|---------|---------------|------------------|
| Metrics, readiness, top risks, effort, strategy | discovery + specialist summaries | `Executive_Summary.md` |
| Domains, capabilities, flows, dispatch, flags, providers | `artifacts/domain.json` | `Business_Architecture.md` |
| Layers, components, deploy, security, cross-cutting | `artifacts/architecture.json` | `Application_Architecture.md` |
| Stores, entity attributes, lineage, SP, integrations, contracts, resilience | `artifacts/lineage.json` + `integration.json` | `Data_and_Integration.md` |
| Gaps, risks, remediations, regression, traceability | union of specialist gaps | `Risks_Gaps_and_Traceability.md` |

JSON SSOT is **`artifacts/`**. Completeness renders Markdown/HTML from those files.

## Forbidden client outputs

- `deliverables/`
- `csa_pack/machine/` (including `sections/`)
- Numbered `00`/`01`–`05`/`04`–`10` Markdown packs
- Gate reports inside `csa_pack/`
- Duplicate catalogs across the five docs (Jaccard > 0.32)

## Allowed under `csa_pack/` only

1. `Executive_Summary.md`
2. `Business_Architecture.md`
3. `Application_Architecture.md`
4. `Data_and_Integration.md`
5. `Risks_Gaps_and_Traceability.md`
6. `README.md`
7. `arc42-c4/*.html`
