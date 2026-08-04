# Discover Quality Rubric

| Metric | Pass threshold | Blocking if fail |
|--------|----------------|------------------|
| Schema conformance | 100% required fields valid | yes |
| Artifact classification coverage | ≥90% of sampled files classified | yes |
| Primary language identified | ≥1 language with evidence | yes |
| Framework detection | framework listed OR explicit unknown with descriptor search evidence | yes |
| Module map | ≥1 module when codebase has >1 package/root | warn |
| Average confidence on stack items | ≥60 | warn if 40–59; fail if &lt;40 with invented values |
| Evidence coverage on stack items | ≥70% non-inferred | yes |

## Critical gaps (examples)

- `DISC-001`: No programming language detected
- `DISC-014`: Descriptors present but no framework classification
- `DISC-020`: Missing DDL/config called out as critical but not listed in `missing_artifacts`
