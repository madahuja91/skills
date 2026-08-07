---
name: csa6-integration
description: Classify legacy integrations (REST/EVENT/BATCH/LEGACY), sync vs async, and resilience patterns for CSA. Use when Manager invokes Integration Analysis.
---

# CSA Integration Skill


## HARD — pack schema is the artifact contract (blocking)

1. Your `artifacts/*.json` **MUST** include a top-level `pack_substance` object.
2. `pack_substance` **MUST** validate 100% against the pack schema(s) in this skill's `pack-schemas/` folder (same as `csa6-pack-schemas/output-schemas/`).
3. Cover **every** `required[]` field, every `minItems` floor, and every ID pattern (`CAP-*`, `CMP-*`, `LIN-*`, `INT-*`, `CTR-*`, `DEBT-*`, `RISK-*`, `GAP-*`, `ASM-*`, `ACT-*`, `REG-*`, `WF-*`, etc.).
4. Do **not** mark done if analysis-only fields are filled but `pack_substance` is missing, thin, or schema-invalid.
5. Markdown rendered later must expose the **same** sections/IDs — if it is not in `pack_substance`, it will not appear in the client MD.
6. Inventing empty placeholders to “pass” is forbidden; use evidenced content or explicit gap rows that still satisfy schema shape/floors where the schema allows gap documentation.

**This agent's pack schema(s):** `pack-schemas/Data_and_Integration.schema.json`

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa6-specialist-worker` (do not restate). Output: `artifacts/integration.json` including `interface_contracts`, `exception_mappings`, `resilience_posture`.


## Primary deliverable (pack_substance)

Primary deliverable: rtifacts/integration.json with required pack_substance matching full pack-schemas/Data_and_Integration.schema.json (INT-*, CTR-*, exceptions, resilience, integration_risks, plus data sections coordinated with Lineage).

## Procedure

1. Discover external I/O: HTTP clients, IBM MQ (native `com.ibm.mq` and JMS), file drops, FTP, mainframe, ESB, SOAP, stored-proc bridges.
2. Apply `csa6-legacy-ibm-mq` for queue/qmgr/channel/host/port extraction from files only — never invent names.
3. Classify pattern_type and sync_async.
4. Fill `interface_contracts` (operation summaries — not separate OAS files), `exception_mappings`, and `resilience_posture`.
5. Capture error handling when present; mark unknown honestly.
6. Flag async candidates with justification.

## Completeness note

`Data_and_Integration.md` must include Mermaid diagram `diag-integration-landscape` (`flowchart` or `sequenceDiagram`) per `mermaid-diagrams`, sourced only from this artifact. Fold contracts/exceptions/resilience into that same doc — never emit OAS YAML or `exception_http_mapping.md` as client deliverables.

## Gate

`csa6-gate-integration` — every discovered external I/O must be classified.
