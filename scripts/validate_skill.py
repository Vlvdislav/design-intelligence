#!/usr/bin/env python3
"""Static skill structure and design-only contract checks."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
required = {
    "visual-art-director": [
        "SKILL.md", "agents/openai.yaml", "references/creative-mechanics.md",
    ],
    "creative-frontend-engineer": [
        "SKILL.md", "agents/openai.yaml",
        "references/frontend-architecture.md",
        "references/interaction-contract.md",
        "references/motion-3d-engineering.md",
        "references/commerce-frontend.md",
        "references/visual-qa-and-performance.md",
        "references/delivery-checklist.md",
    ],
}
errors = []
for name, paths in required.items():
    folder = root / "skills" / name
    for rel in paths:
        path = folder / rel
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"missing/empty: {name}/{rel}")
    primary = folder / "SKILL.md"
    if not primary.is_file():
        continue
    content = primary.read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---\n", content, re.S)
    if not front or not re.search(r"^name:\s*" + re.escape(name) + r"\s*$", front.group(1), re.M):
        errors.append(f"bad frontmatter: {name}")
    for rel in set(re.findall(r"`(references/[a-z0-9-]+\.md)`", content)):
        if not (folder / rel).is_file():
            errors.append(f"broken reference: {name}/{rel}")
    agent = folder / "agents/openai.yaml"
    if agent.is_file() and f"${name}" not in agent.read_text(encoding="utf-8"):
        errors.append(f"missing invocation: ${name}")
designer_dir = root / "skills" / "visual-art-director"
skill = (designer_dir / "SKILL.md").read_text(encoding="utf-8")
agent = (designer_dir / "agents/openai.yaml").read_text(encoding="utf-8")
for clause in ("DESIGN ONLY", "one finished visual direction", "Exact recreation", "Figma-first", "Do the design"):
    if clause.lower() not in skill.lower():
        errors.append(f"missing design-only contract: {clause}")
if "invoke any frontend engineer" not in agent or "Do not write code" not in agent:
    errors.append("agent must explicitly refuse automatic frontend delegation")
refs = designer_dir / "references"
if refs.is_dir():
    extra = [p.name for p in refs.iterdir() if p.is_file() and p.name != "creative-mechanics.md"]
    if extra:
        errors.append("legacy designer references: " + ", ".join(extra))
for rel in ("install.sh", "install.ps1", "README.md", "INSTALL.md"):
    if not (root / rel).is_file():
        errors.append(f"missing: {rel}")
if errors:
    print("FAILED\n" + "\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print("OK: design-only Figma director, single-default-concept, precise scene specification, editable/QA contract.")
print("STATIC ONLY: no live Figma run was performed.")
