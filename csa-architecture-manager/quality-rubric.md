# Manager Quality Rubric

| Metric | Pass |
|--------|------|
| Completeness Validator invoked after every specialist | required |
| No accepted artifact with critical schema gaps | required |
| On Completeness fail: re-run named `target_agent_id` owner (≤2) | required |
| max_reruns honored (≤2 re-runs per owner) | required |
| execution_plan.json / swarm_state kept current | required |
| FINAL Completeness renders lean 5-doc pack + arc42 HTML | required |
| gate-csa-document pass (or escalated after max re-runs) | required |
| No Document Assembler invoked | required |
| No epic-story readiness / epic_story_seeds | required |
| Done only when `src/csa_pack/` required files exist on disk | required |
