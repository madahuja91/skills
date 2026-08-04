# Business Domain Quality Rubric

| Metric | Pass threshold | Blocking |
|--------|----------------|----------|
| Schema conformance | 100% | yes |
| Domains present | ≥1 | yes |
| Critical/high rules with implementation_location OR explicit missing flag | 100% | yes |
| Entities with extraction_source | 100% | yes |
| Capability → domain mapping | ≥80% capabilities have supporting_domains | warn |
| Avg confidence critical rules | ≥70 | warn |
| Evidence on code-sourced rules | ≥70% | yes |
