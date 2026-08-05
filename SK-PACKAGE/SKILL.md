---
name: SK-PACKAGE
description: >-
  Assemble phase or final package manifests without inventing story content.
---

# SK-PACKAGE — Packaging

## Outputs
- `artifacts/package/cs_manifest.json` and/or `ts_manifest.json`
- `artifacts/package/final_manifest.json` (master)
- Copy indexes of epics/stories/gates/trace/approvals
- Ensure package lists **both** JSON and MD paths for epics/stories

## Procedure
1. Collect existing artifact paths only (JSON + MD)
2. Record template_version, skill versions, approvals, gate results
3. Fail packaging if stories exist as JSON without matching MD (or vice versa)
4. Do not modify story substance

## Must not
Invent missing stories to make the package look complete.
