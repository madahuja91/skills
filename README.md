# Skills Catalog (runtime)

Procedures live in local `skills/` folders (`SKILL.md` + `schema.json`). Agents load them via the **skills** tool and `input.skills` attachments — not by hardcoding skill bodies in prompts.

| | |
|--|--|
| **Primary source** | Local `skills/` (mirrored to `.agents/skills/`) |
| **Fallback** | https://github.com/madahuja91/skills (public) if local skills missing |
| **Destination** | `.agents/skills/` |
| **PAT required?** | **No** for public fallback |

## Sync Skills node
1. Prefer copying **all** local `skills/*` → `.agents/skills/`
2. If local empty, `git clone --depth 1` from GitHub (keep all skills)
3. Bootstrap ACTIVE_ROOT = workspace-relative `src` (or `.` if already in `src`) + `active_root.txt` (never `src/src`)
4. Preflight: FAIL early if any workflow-required skill is missing/invalid; write `ACTIVE_ROOT/artifacts/gates/skills_preflight.json`

## ACTIVE_ROOT
Manager/Orchestrator creates **one** ACTIVE_ROOT (`src`). All agents write only under it. See `active-root-hygiene`.

## Local skill folders
Each skill has:
- `SKILL.md` — procedure
- `schema.json` — output contract
