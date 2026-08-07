---
name: csa5-integration
description: Classify legacy integrations (REST/EVENT/BATCH/LEGACY), sync vs async, and resilience patterns for CSA. Use when Manager invokes Integration Analysis.
---

# CSA Integration Skill

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)

## Shared worker rules

Obey `csa5-specialist-worker` (do not restate). Output: `artifacts/integration.json` including `interface_contracts`, `exception_mappings`, `resilience_posture`.

## Procedure

1. Discover external I/O: HTTP clients, IBM MQ (native `com.ibm.mq` and JMS), file drops, FTP, mainframe, ESB, SOAP, stored-proc bridges.
2. Apply `csa5-legacy-ibm-mq` for queue/qmgr/channel/host/port extraction from files only — never invent names.
3. Classify pattern_type and sync_async.
4. Fill `interface_contracts` (operation summaries — not separate OAS files), `exception_mappings`, and `resilience_posture`.
5. Capture error handling when present; mark unknown honestly.
6. Flag async candidates with justification.

## Completeness note

`Data_and_Integration.md` must include Mermaid diagram `diag-integration-landscape` (`flowchart` or `sequenceDiagram`) per `mermaid-diagrams`, sourced only from this artifact. Fold contracts/exceptions/resilience into that same doc — never emit OAS YAML or `exception_http_mapping.md` as client deliverables.

## Gate

`csa5-gate-integration` — every discovered external I/O must be classified.
