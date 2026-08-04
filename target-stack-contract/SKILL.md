---
name: target-stack-contract
description: Normalizes ADR/target architecture spec into a machine stack decisions object (language, DB, messaging, API, runtime). Use during TSA Intake.
---

# Target Stack Contract

## Schema

Authoritative contract: [`schema.json`](schema.json)


## Goal

Produce `artifacts/stack_decisions.json` from ADR/target spec only.

## Required decisions (when present in ADR)

- language_runtime (e.g. Java 21 / Spring Boot)
- datastore (e.g. PostgreSQL, Oracle)
- messaging (e.g. Kafka, Azure Service Bus, IBM MQ retained)
- api_style (REST/events/GraphQL…)
- deployment_target (cloud/on-prem/hybrid)
- constraints[] / non_goals[]

If ADR omits a decision, mark `status: unresolved` — do not invent.
