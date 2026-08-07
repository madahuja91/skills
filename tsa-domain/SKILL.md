---
name: tsa-domain
description: Produce enterprise ADR blueprint for TSA decisions and trade-offs.
---

# TSA ADR Blueprint

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Goal

Write `artifacts/adr_blueprint.json` using enterprise ADR schema.

## Procedure

1. Read accepted `tsa_specification.json` and CSA risk/debt evidence.
2. Produce ADR decisions with context, drivers, options, chosen rationale.
3. Include governance metadata, compliance/enforcement, and ADR relationships.
4. Ensure each ADR traces to CSA baseline concerns and target-service outcomes.
