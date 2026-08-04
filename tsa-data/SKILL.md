---
name: tsa-data
description: Design target data architecture and migration of CSA lineage/SP logic toward ADR datastore patterns. Use when Manager invokes TSA Data.
---

# TSA Data

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Goal

Write `artifacts/target_data.json`.

## Procedure

1. Map CSA stores/lineage to target datastore(s) from ADR.
2. Plan SP/package logic disposition (service rules, jobs, retained DB logic) with evidence.
3. Define migration units and cutover concerns for Migration Strategy peer.
