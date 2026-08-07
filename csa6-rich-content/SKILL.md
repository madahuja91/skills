---
name: csa6-rich-content
description: Enforces lean 5-doc CSA pack from artifacts SSOT — legacy schema content only. No workflow meta, machine/sections, or deliverables.
---

# CSA Output Quality

## Schema

[`schema.json`](schema.json)

## Client pack (only)

1. `Executive_Summary.md`
2. `Business_Architecture.md`
3. `Application_Architecture.md`
4. `Data_and_Integration.md`
5. `Risks_Gaps_and_Traceability.md`
6. `README.md` + `arc42-c4/*.html`

Rendered by **Completeness** from `artifacts/*.json`.  
**No** `csa_pack/machine/`. **No** `deliverables/`. **No** Assembler.

## Core policy

1. Specialist schema completeness first (`artifacts/*.json` required fields + evidence).
2. Completeness builds **pack substance** that validates against each `output-schemas/*.schema.json`, then renders five Markdown owners (`csa6-section-boundaries`).
3. **Thin Markdown = FAIL.** A short overview that omits required schema sections or **required Mermaid diagrams** does not pass even if the five filenames exist.
4. Fail if forbidden duplicate trees exist.
5. Prefer substance gaps over cosmetic HTML/Jaccard-only fails.
6. **Client pack = legacy only:** no workflow/swarm/gate/process meta in any `csa_pack/**` file.
7. **arc42 `index.html` must be a full hub** (12 anchors + ≥2 Mermaid + classic runtime). Stub index = FAIL.

## Specialist floors

| Artifact | Minimum |
|----------|---------|
| domain.json | ≥3 domains, ≥8 capabilities, workflows + dispatch when evidenced |
| architecture.json | ≥5 layers, deploy/security/cross-cutting/build + populated `c4_views` |
| lineage.json | ≥3 sources, ≥10 lineage rows, entity_catalog |
| integration.json | ≥6 integrations, contracts + exceptions + resilience |

## Pack document floors (blocking)

**Primary gate = section / schema coverage** for each individual document.  
Each client MD must cover **all** `required` fields of its output-schema (explicit headings/tables/lists — not a stub summary).

| Doc | Must show (non-exhaustive) |
|-----|----------------------------|
| Executive_Summary | overview + metrics≥5 + readiness≥4 + findings≥5 + risks≥5 + effort + strategy + success metrics |
| Business_Architecture | contexts≥3 + CAP-*≥8 + dictionary≥8 + flows≥3 + dispatch≥5 + flags + providers + gaps |
| Application_Architecture | 5 layers + CMP-*≥8 + build/runtime + deploy + security + cross-cutting + runtime evidence + DEBT-*≥5 + ops gaps |
| Data_and_Integration | stores≥3 + entities≥5 + LIN-*≥10 + SP rules≥5 + INT-*≥6 + contracts + exceptions + resilience |
| Risks_Gaps_and_Traceability | GAP-*≥5 + RISK-*≥5 + ASM-*≥3 + ACT-*≥3 + REG-*≥3 + trace links≥10 |

**Lines:** each client Markdown doc must meet a **minimum of 200 lines** (section coverage still comes first). Crossing 200 is good — richer explanation is allowed and preferred. **Never** enforce a maximum line/word/size limit on pack Markdown or schema string fields.

## Blocking checks

required_files_present, artifact_schema_conformance, **pack_output_schema_conformance**, **markdown_min_line_count** (≥200 lines; more is fine), specialist_list_depth, forbidden_duplicate_trees, section_anti_redundancy, pack_shape_valid, shared_memory_present, no_workflow_meta_in_csa_pack

Do **not** require writing `csa_pack/machine/sections/*.json` as a client deliverable. Temporary pack-substance JSON under `_internal/completeness_validation/` for schema checks is allowed.  
Do **not** put `maxLength` / max line/word ceilings on pack docs or explanation fields.
