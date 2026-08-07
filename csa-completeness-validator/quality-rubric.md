# Completeness Validator Quality Rubric

| Metric | Pass |
|--------|------|
| Report schema valid | 100% |
| Gaps actionable (`required_action` non-empty) | 100% |
| `target_agent_id` set on every fail | required |
| `remediation_brief.schema_fields_missing` present on schema fails | required |
| remediation_brief present on fail | required |
| No false pass on critical schema errors | required |
| Lane mode never writes `csa_pack/` | required |
| FINAL renders lean 5 MD + README + arc42 HTML | required |
| FINAL validates pack against output-schemas + gate-csa-document | required |
| FINAL proves every required pack-schema field is in MD (not stub) | required |
| No PASS on specialist-artifact-only checks without pack substance | required |
| No epic-story / numbered 00-10 / machine sections required | required |
| No false pass on stub Markdown/HTML (`csa-rich-content`) | required |
