"""Validate CSA example artifacts (JSON + Markdown/HTML deliverable formats)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

JSON_CHECKS = [
    (ROOT / "agents/csa-discover/examples/pass-minimal.json", ["artifact_id", "agent_id", "technology_stack"]),
    (ROOT / "agents/csa-business-domain/examples/pass-minimal.json", ["business_domains", "business_capabilities"]),
    (ROOT / "agents/csa-tech-architecture/examples/pass-minimal.json", ["architecture_layers", "c4_views"]),
    (ROOT / "agents/csa-data-lineage/examples/pass-minimal.json", ["data_sources", "field_lineage"]),
    (ROOT / "agents/csa-integration/examples/pass-minimal.json", ["integrations"]),
    (ROOT / "agents/csa-completeness-validator/examples/fail-gate-report.json", ["gate_id", "result", "blocking_gaps"]),
    (ROOT / "shared/quality-gate-framework/schema.json", ["$id", "properties"]),
    (ROOT / "agents/csa-document-assembler/examples/pack-manifest.pass.json", ["sections", "arc42_c4_html", "epic_story_seeds"]),
]

MD_CHECKS = [
    (ROOT / "standards/epic-story-mapping/examples/functions.pass.md", ["# Functions", "FN-"]),
    (ROOT / "standards/epic-story-mapping/examples/epics.pass.md", ["# Epics", "EP-"]),
    (ROOT / "standards/epic-story-mapping/examples/stories.pass.md", ["# Stories", "US-"]),
]

HTML_CHECKS = [
    (ROOT / "standards/arc42-c4-views/examples/index.html", ["<!DOCTYPE html>", "context.html", "containers.html", "components.html"]),
]


def main() -> int:
    failed = 0
    passed = 0

    for path, keys in JSON_CHECKS:
        if not path.exists():
            print(f"MISSING {path}")
            failed += 1
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            print(f"INVALID_JSON {path}: {exc}")
            failed += 1
            continue
        missing = [k for k in keys if k not in data]
        if missing:
            print(f"FAIL {path.name}: missing {missing}")
            failed += 1
        else:
            print(f"OK   {path.relative_to(ROOT)}")
            passed += 1

    for path, needles in MD_CHECKS + HTML_CHECKS:
        if not path.exists():
            print(f"MISSING {path}")
            failed += 1
            continue
        text = path.read_text(encoding="utf-8")
        missing = [n for n in needles if n not in text]
        if missing:
            print(f"FAIL {path.name}: missing {missing}")
            failed += 1
        else:
            print(f"OK   {path.relative_to(ROOT)}")
            passed += 1

    bad = ROOT / "agents/csa-discover/examples/fail-invented-stack.json"
    bad_data = json.loads(bad.read_text(encoding="utf-8"))
    frameworks = bad_data.get("technology_stack", {}).get("frameworks", [])
    if not any(f.get("framework_name") == "Spring Boot" for f in frameworks):
        print("FAIL fail-invented-stack.json does not contain Spring Boot fixture")
        failed += 1
    else:
        print("OK   fail-invented-stack.json (negative fixture)")
        passed += 1

    # Manifest format invariants
    manifest = json.loads(
        (ROOT / "agents/csa-document-assembler/examples/pack-manifest.pass.json").read_text(encoding="utf-8")
    )
    if manifest.get("arc42_c4_html", {}).get("format") != "html":
        print("FAIL pack-manifest arc42_c4_html.format must be html")
        failed += 1
    elif any(not s.endswith(".md") for s in manifest.get("epic_story_seeds", [])):
        print("FAIL pack-manifest epic_story_seeds must be .md")
        failed += 1
    elif any(s.get("format") != "markdown" for s in manifest.get("sections", [])):
        print("FAIL pack-manifest sections must be markdown")
        failed += 1
    else:
        print("OK   pack-manifest format invariants")
        passed += 1

    # Every skill must have schema.json and ## Schema section
    skills_root = ROOT
    for skill_md in sorted(skills_root.rglob("SKILL.md")):
        rel = skill_md.parent.relative_to(skills_root).as_posix()
        if not (skill_md.parent / "schema.json").exists():
            print(f"FAIL missing schema.json for {rel}")
            failed += 1
        elif "## Schema" not in skill_md.read_text(encoding="utf-8"):
            print(f"FAIL missing ## Schema section in {rel}/SKILL.md")
            failed += 1
        else:
            print(f"OK   schema+section {rel}")
            passed += 1

    catalog = json.loads((skills_root / "catalog.json").read_text(encoding="utf-8"))
    if catalog.get("missing_schemas"):
        print(f"FAIL catalog missing_schemas={catalog['missing_schemas']}")
        failed += 1
    else:
        print(f"OK   catalog.json ({catalog.get('skill_count')} skills)")
        passed += 1

    print(f"\n{passed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
