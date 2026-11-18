#!/usr/bin/env python3
"""Safely detect and optionally archive duplicate Visual Art Director skills.
Dry run by default. Never touches canonical skill dirs. Archives outside skill root.
"""
import argparse
from pathlib import Path
import re, shutil, sys
from datetime import datetime, timezone

CANONICAL = {'visual-art-director', 'creative-frontend-engineer'}

def skill_name(folder: Path):
    p=folder/'SKILL.md'
    if not p.is_file(): return None
    try:
        first=p.read_text(encoding='utf-8')[:1500]
    except (OSError, UnicodeError): return None
    fm=re.search(r'\A---\s*\n(.*?)\n---', first, re.S)
    if not fm: return None
    found=re.search(r'^name:\s*["\']?([^\n"\']+)', fm.group(1), re.M)
    return found.group(1).strip() if found else None

def is_legacy_name(value):
    slug=value.lower().strip().replace('_','-').replace(' ','-')
    return bool(re.match(r'^(visual-art-director|visual-artdirector)(?:[.-](?:v?[0-9]+.*|backup.*|old.*|copy.*|figma.*|ux.*))?$',slug))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=Path.home()/'.agents'/'skills',help='Codex skills discovery directory')
    ap.add_argument('--apply',action='store_true',help='Move detected duplicate dirs into archive outside discovery root')
    a=ap.parse_args(); root=a.root.expanduser().resolve()
    if not root.is_dir(): print(f'No skills dir: {root}'); return 0
    canonical=root/'visual-art-director'
    if not canonical.is_dir() or skill_name(canonical)!='visual-art-director':
        print(f'SKIP: canonical visual-art-director missing or invalid: {canonical}. No changes.'); return 1
    duplicates=[]
    for folder in sorted(root.iterdir()):
        if not folder.is_dir() or folder.is_symlink() or folder.name in CANONICAL:
            continue
        n=skill_name(folder)
        # Candidate only if path or exact frontmatter indicates the Visual Art Director family.
        if n and (n=='visual-art-director' or is_legacy_name(n) or is_legacy_name(folder.name)):
            duplicates.append((folder,n))
    print(f'Canonical: {canonical}')
    if not duplicates:
        print('No detected duplicates. For other roots, pass --root /path/to/skills')
        return 0
    print('Duplicate candidates (not deleting):')
    for d,n in duplicates: print(f'  {d} [frontmatter name={n}]')
    if not a.apply:
        print('DRY RUN: no changes. To archive: python3 scripts/doctor_skills.py --apply')
        return 0
    backup_root = root.parent / (root.name + '-backups') / ('legacy-' + datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S'))
    backup_root.mkdir(parents=True,exist_ok=False)
    for d,n in duplicates:
        dest=backup_root/d.name
        shutil.move(str(d),str(dest))
        print(f'Archived: {dest}')
    print('Restart Codex. To undo, move an archived directory back into the skills root.')
    return 0

if __name__=='__main__': sys.exit(main())
