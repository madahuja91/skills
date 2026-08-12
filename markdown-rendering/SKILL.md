---
name: markdown-rendering
description: >-
  Render human-readable Markdown from the validated technical backlog JSON.
---

## Schema

Authoritative contract: [`schema.json`](schema.json)

# Markdown Rendering

Version `2.0.0`.

## Purpose

Render human-readable Markdown from the validated technical backlog JSON.

## Workflow binding

- Markdown Renderer

## Rules

- JSON is authoritative.
- Preserve Epic -> Feature -> Story hierarchy.
- Display FAC/AAC at Feature level.
- Display full technical LLD sections at Story level.
- Display SAC at Story level.
- Preserve exact Story area names.
- Do not add content not present in JSON.

## ACTIVE_ROOT

Write only under the single workspace ACTIVE_ROOT (`src`). See `active-root-hygiene`.

## Must not

- Invent architecture decisions unsupported by `architecture_blueprint`.
- Change Feature business boundaries from a technical Story.
- Use Story area names other than UI, BFF/API, Domain, Persistence, Messaging, Testing.
