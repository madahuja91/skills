---
name: csa7-integration
description: Classify legacy integrations (REST/EVENT/BATCH/LEGACY), sync vs async, and resilience patterns for CSA. Use when Manager invokes Integration Analysis.
---

# CSA Integration Skill


## HARD — knowledge-first documentation (blocking)

1. Write **architecture knowledge**, not evidence dumps. Answer What / Why / How before citing files.
2. Business rules must be prose (e.g. "Customer cannot be deleted when active orders exist") — never lead with `Class.java:line`.
3. `pack_substance` MUST validate 100% against this skill's `pack-schemas/` (and `csa7-pack-schemas/output-schemas/`).
4. Required narrative fields (overview/purpose/what/why/how, acceptance criteria, DDD, persistence strategy, decision_log, modernization) are blocking.
5. Optional per-field `evidence` may exist for gates; Markdown **must** put `## Evidence Mapping (Appendix)` **last**.
6. Forbidden in client MD: evidence-led tables that dominate the doc; Completeness/gate/workflow meta in Risks docs.
7. Min **200 lines** per client MD; no maxLength anywhere.

**This agent's pack schema(s):** `pack-schemas/Data_and_Integration.schema.json`


## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa7-specialist-worker` (do not restate). Output: `artifacts/integration.json` including `interface_contracts`, `exception_mappings`, `resilience_posture`.


## Primary deliverable (pack_substance)

Primary deliverable: rtifacts/integration.json with required pack_substance matching full pack-schemas/Data_and_Integration.schema.json (INT-*, CTR-*, exceptions, resilience, integration_risks, plus data sections coordinated with Lineage).

## Procedure

1. Discover external I/O: HTTP clients, IBM MQ (native `com.ibm.mq` and JMS), file drops, FTP, mainframe, ESB, SOAP, stored-proc bridges.
2. Apply `csa7-legacy-ibm-mq` for queue/qmgr/channel/host/port extraction from files only — never invent names.
3. Classify pattern_type and sync_async.
4. Fill `interface_contracts` (operation summaries — not separate OAS files), `exception_mappings`, and `resilience_posture`.
5. Capture error handling when present; mark unknown honestly.
6. Flag async candidates with justification.

## Completeness note

`Data_and_Integration.md` must include Mermaid diagram `diag-integration-landscape` (`flowchart` or `sequenceDiagram`) per `mermaid-diagrams`, sourced only from this artifact. Fold contracts/exceptions/resilience into that same doc — never emit OAS YAML or `exception_http_mapping.md` as client deliverables.

## Gate

`csa7-gate-integration` — every discovered external I/O must be classified.
