# Completeness Validator Quality Rubric

| Metric | Pass |
|--------|------|
| Report schema valid | 100% |
| Gaps actionable (required_action non-empty) | 100% |
| remediation_brief present on fail | required |
| No false pass on critical schema errors | required |
| No false pass on stub Markdown/HTML (must enforce `csa-rich-content`) | required |
| Document-gate reports include observed word counts when depth fails | required |
