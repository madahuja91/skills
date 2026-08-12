---
name: jira-projection
description: >-
  Project the validated technical backlog into Jira-import-oriented JSON.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Jira Projection

Version `2.0.0`.

## Purpose

Project the validated technical backlog into Jira-import-oriented JSON.

## Workflow binding

- Jira Projection Agent

## Rules

- Canonical backlog remains the source of truth.
- Preserve REQ/EPIC/FEAT/ST IDs as external IDs.
- Preserve parent relationships.
- Preserve FAC/AAC/SAC content in the configured Jira description/acceptance representation.
- Do not flatten technical Story LLD information.
- Do not generate or modify canonical content.

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
