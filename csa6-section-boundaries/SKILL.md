---
name: csa6-section-boundaries
description: SSOT for lean 5-doc CSA pack — legacy codebase content only from artifact schemas. Forbids workflow/swarm/gate meta and deliverables/machine duplicates.
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
| Gaps, risks, remediations, regression, traceability | union of specialist **codebase** gaps | `Risks_Gaps_and_Traceability.md` |

JSON SSOT is **`artifacts/`**. Completeness renders Markdown/HTML from schema fields only.

## HARD: Client pack = legacy content only

Every `csa_pack/**` file must describe the **legacy codebase** using schema inventories (domains, components, lineage, integrations, risks grounded in evidence paths).

**Forbidden in `csa_pack/` (including README and HTML):**

- Swarm / orchestrator / Manager / Completeness / Assembler / lane / join / rework language
- Gate IDs, PASS/FAIL/PASS_WITH_WARNINGS, attempt counts, max_reruns
- `artifacts_index`, `swarm_state`, `handoffs`, checkpoint.seq, ACTIVE_ROOT, run_plan
- Quality-gate scorecards as the document purpose (scores belong in `artifacts/quality_gate_reports/` only)
- Instructions to agents, “next steps for the workflow”, remediation briefs aimed at specialists
- Duplicate process narrative (“this section was assembled after join…”)

Workflow meta stays under `_internal/` and `artifacts/quality_gate_reports/` only.

## Forbidden client outputs

- `deliverables/`
- `csa_pack/machine/` (including `sections/`)
- Any Markdown filename not in the allowed six
- Gate reports inside `csa_pack/`
- Duplicate catalogs across the five docs (Jaccard > 0.32)
- Workflow/orchestration meta (see above)

## Allowed under `csa_pack/` only

1. `Executive_Summary.md`
2. `Business_Architecture.md`
3. `Application_Architecture.md`
4. `Data_and_Integration.md`
5. `Risks_Gaps_and_Traceability.md`
6. `README.md` (pack index of legacy docs — no workflow status)
7. `arc42-c4/*.html`
