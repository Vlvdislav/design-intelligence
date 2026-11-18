#!/usr/bin/env python3
"""Static structure checks for reference-first, design-only skill."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
required = {
    "visual-art-director": ["SKILL.md", "agents/openai.yaml", "references/reference-decoder.md"],
    "creative-frontend-engineer": [
        "SKILL.md", "agents/openai.yaml", "references/frontend-architecture.md",
        "references/interaction-contract.md", "references/motion-3d-engineering.md",
        "references/commerce-frontend.md", "references/visual-qa-and-performance.md",
        "references/delivery-checklist.md",
    ],
}
errors = []
for name, paths in required.items():
    folder = root / "skills" / name
    for rel in paths:
        file = folder / rel
        if not file.is_file() or not file.read_text(encoding="utf-8").strip():
            errors.append(f"missing: {name}/{rel}")
    file = folder / "SKILL.md"
    if not file.is_file():
        continue
    text = file.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match or not re.search(r"^name:\s*" + re.escape(name) + r"\s*$", match.group(1), re.M):
        errors.append(f"bad frontmatter: {name}")
    for ref in set(re.findall(r"`(references/[a-z0-9-]+\.md)`", text)):
        if not (folder / ref).is_file():
            errors.append(f"broken ref: {name}/{ref}")
    agent = folder / "agents/openai.yaml"
    if agent.is_file() and f"${name}" not in agent.read_text(encoding="utf-8"):
        errors.append(f"missing invocation: ${name}")
designer = (root / "skills" / "visual-art-director" / "SKILL.md").read_text(encoding="utf-8")
agent = (root / "skills" / "visual-art-director" / "agents" / "openai.yaml").read_text(encoding="utf-8")
for phrase in ("REFERENCE FIRST", "DESIGN ONLY", "design system", "Reference map", "EXACT", "ADAPT", "DESIGN-SYSTEM", "NO REFERENCE", "Compare and correct"):
    if phrase.lower() not in designer.lower():
        errors.append("missing ref-first contract: " + phrase)
if "$creative-frontend-engineer" in designer or "frontend code or engineer handoff" not in agent:
    errors.append("design skill must not invoke frontend")
refdir = root / "skills" / "visual-art-director" / "references"
if refdir.is_dir():
    extras = [p.name for p in refdir.iterdir() if p.is_file() and p.name != "reference-decoder.md"]
    if extras: errors.append("legacy references present: " + ", ".join(extras))
for rel in ("install.sh", "install.ps1", "README.md", "INSTALL.md"):
    if not (root / rel).is_file():
        errors.append("missing: " + rel)
if errors:
    print("FAILED\n" + "\n".join("- " + e for e in errors))
    sys.exit(1)
print("OK: reference-first designer, strict source mapping, Figma-only, independent engineer.")
print("STATIC ONLY: no live Figma comparison was run.")
