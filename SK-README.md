# Skills Catalog (runtime)

Procedures live here — **not** in agent prompts.

Agents use `model: gpt-5.5`, keep thin identity prompts, and `read_file` these skills from `.agents/skills/<ID>/SKILL.md` (synced from `skills/` at workflow start).

| Skill | Used by |
|-------|---------|
| SK-SWARM | All swarm peers |
| SK-SWARM-RELAY | Phase + Master orchestrators |
| SK-LEGACY | Legacy Code Analyzer |
| SK-ARCH | CSA Analyzer, TSA Analyzer |
| SK-CAP | Business Capability Extractor |
| SK-REQ | Functional Requirement Extractor |
| SK-RULE | Business Rule Extractor |
| SK-STORY | Current State Story Generator |
| SK-EPIC | CS/TS Story Generators |
| SK-ADR | ADR Analyzer |
| SK-GAP | Gap & Impact Analyzer |
| SK-TARGET | Target Story Generator |
| SK-AC | Acceptance Criteria Generator |
| SK-TEST | Test Scenario Generator |
| SK-TRACE | Traceability Validator |
| SK-QUALITY | Quality Reviewer |
| SK-PACKAGE | Master / packagers |

Source of truth: `skills/`. Runtime mirror: `.agents/skills/` (created by Sync Skills script node).
