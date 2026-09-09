#!/usr/bin/env python3
"""Validate the public Visual Grammar Foundry contract repository."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "LICENSE",
    "docs/CONTRACT.md",
    "schemas/child-skill.schema.json",
    "schemas/release.schema.json",
    "templates/public-child/SKILL.md",
    "templates/public-child/README.md",
    "templates/public-child/CHANGELOG.md",
    "templates/public-child/LICENSE",
    "templates/public-child/ASSET-LICENSE.md",
    "templates/public-child/REFERENCES.md",
    "templates/public-child/.gitignore",
    "templates/public-child/scripts/validate_public.py",
    "templates/public-child/.github/workflows/validate.yml",
)
POLICY_FILES = {
    Path("README.md"),
    Path("docs/CONTRACT.md"),
    Path("templates/public-child/ASSET-LICENSE.md"),
    Path("templates/public-child/REFERENCES.md"),
}
PRIVATE_MARKERS = (
    "private-" + "core/runs",
    "routing " + "weights",
    "prompt " + "compiler",
    "evidence-" + "notes",
    "hidden " + "inventories",
    "discovery " + "implementation",
)


def fail(message: str) -> None:
    print(f"public contract validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


for relative in REQUIRED:
    if not (ROOT / relative).is_file():
        fail(f"missing required file {relative}")

for relative in ("schemas/child-skill.schema.json", "schemas/release.schema.json"):
    try:
        json.loads((ROOT / relative).read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {relative}: {exc}")

for relative in ("README.md", "docs/CONTRACT.md"):
    text = (ROOT / relative).read_text(encoding="utf-8").lower()
    if "visual-grammar-foundry-core" not in text:
        fail(f"{relative} does not identify the private core boundary")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
        continue
    if path.suffix.lower() not in {".md", ".json", ".py", ".yml", ".yaml", ".txt"}:
        continue
    relative = path.relative_to(ROOT)
    if relative == Path("scripts/validate_contract.py"):
        continue
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    for marker in PRIVATE_MARKERS:
        if marker.lower() in text and relative not in POLICY_FILES:
            fail(f"private marker {marker!r} in {relative}")

print("Validated public Visual Grammar Foundry contract repository.")
