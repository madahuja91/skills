---
name: tsa-domain
description: Map CSA domains/capabilities to target bounded contexts using ADR constraints. Use when Manager invokes TSA Domain.
---

# TSA Domain

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Goal

Write `artifacts/target_domain.json` and contribute to `04_target_domain_model.md` content via Assembler.

## Procedure

1. Read accepted intake + CSA domain.
2. Propose target bounded contexts / capabilities aligned to ADR.
3. Map CSA `DOM-*` / capabilities → target IDs with traceability.
4. Required Mermaid later in Assembler: `diag-tsa-domain-context-map`.
