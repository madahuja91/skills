# Skills Catalog (runtime)

Procedures are loaded from GitHub at workflow start.

| | |
|--|--|
| **Source** | https://github.com/madahuja91/skills (public) |
| **Destination** | `.agents/skills/` |
| **PAT required?** | **No** (repo is public). Optional `GITHUB_PAT` / `githubPat` only if the repo later becomes private. |

## Sync Skills node
Runs `git clone --depth 1` (or `git fetch` + reset if already cloned) from that URL into `.agents/skills/`.

Agents then `read_file` paths like `.agents/skills/SK-SWARM/SKILL.md`.

## Local `skills/` folder
This repo may still keep a local `skills/` mirror for editing/docs. Runtime Sync Skills uses **GitHub**, not the local folder.
