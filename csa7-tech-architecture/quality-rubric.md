# Tech Architecture Quality Rubric

| Metric | Pass threshold | Blocking |
|--------|----------------|----------|
| Schema conformance | 100% | yes |
| Layers with components | ≥3 layers or documented monolith single-deployable with justification | yes |
| Components have evidence | ≥70% | yes |
| analysis_scope honest | runtime/combined only if runtime evidence exists | yes |
| Tech debt overall score present | required | yes |
| Dead/orphan list | present (may be empty array) | warn if omitted |
| c4_views.containers | ≥1 | warn |
