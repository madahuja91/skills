---
name: csa-integration
description: Classify legacy integrations (REST/EVENT/BATCH/LEGACY), sync vs async, and resilience patterns for CSA. Use when Manager invokes Integration Analysis.
---

# CSA Integration Skill

## Schema

Authoritative output/invocation contract: [schema.json](schema.json)


## Goal

Write `artifacts/integration.json` per `schema.json`.

## Procedure

1. Discover external I/O: HTTP clients, IBM MQ (native `com.ibm.mq` and JMS), file drops, FTP, mainframe, ESB, SOAP, stored-proc bridges.
2. Apply `legacy-ibm-mq` for queue/qmgr/channel/host/port extraction from files only — never invent names.
3. Classify pattern_type and sync_async.
4. Capture error handling when present; mark unknown honestly.
5. Flag async candidates with justification.
6. Sync outputs through `csa-swarm-shared-memory`.

## HARD: Depth (`csa-rich-content`)

Classify **all** evidenced external I/O with rich descriptions (endpoints/queues/adapters, direction, reliability). Do not stop after 3–5 sample integrations when discovery shows more.

## Assembler note

Section `07_integration_landscape.md` must include Mermaid diagram **`diag-integration-landscape`** (`flowchart` or `sequenceDiagram`) per `mermaid-diagrams`, sourced only from this artifact.

## Gate

`gate-integration` — every discovered external I/O must be classified.
