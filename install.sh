#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_ROOT="${CODEX_SKILLS_DIR:-$HOME/.agents/skills}"
# Important: backups must not sit inside a skills discovery directory.
BACKUP_ROOT="${CODEX_SKILLS_BACKUPS_DIR:-$(dirname "$TARGET_ROOT")/$(basename "$TARGET_ROOT")-backups}"
MODE="${1:-both}"
case "$MODE" in both) SKILLS=(visual-art-director creative-frontend-engineer);; designer) SKILLS=(visual-art-director);; frontend) SKILLS=(creative-frontend-engineer);; *) echo "Usage: bash install.sh [both|designer|frontend]" >&2; exit 2;; esac
mkdir -p "$TARGET_ROOT"
for skill in "${SKILLS[@]}"; do
  src="$ROOT/skills/$skill"
  dest="$TARGET_ROOT/$skill"
  [[ -f "$src/SKILL.md" ]] || { echo "Missing $src/SKILL.md" >&2; exit 1; }
  stamp="$(date +%Y%m%d-%H%M%S)-$$"
  if [[ -e "$dest" || -L "$dest" ]]; then
    mkdir -p "$BACKUP_ROOT"
    backup="$BACKUP_ROOT/$skill.backup-$stamp"
    mv "$dest" "$backup"
    echo "Backup (outside skills): $backup"
  fi
  cp -R "$src" "$dest"
  echo "Installed: $dest"
done
printf '\nAvailable in Codex: $visual-art-director and $creative-frontend-engineer. Restart Codex if needed.\n'
if command -v python3 >/dev/null 2>&1; then
  python3 "$ROOT/scripts/doctor_skills.py" --root "$TARGET_ROOT" || true
fi
