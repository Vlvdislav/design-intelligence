param([ValidateSet('both','designer','frontend')][string]$Mode='both')
$ErrorActionPreference='Stop'
$TargetRoot=if ($env:CODEX_SKILLS_DIR) { $env:CODEX_SKILLS_DIR } else { Join-Path $HOME '.agents\skills' }
$BackupRoot=if ($env:CODEX_SKILLS_BACKUPS_DIR) { $env:CODEX_SKILLS_BACKUPS_DIR } else { Join-Path (Split-Path $TargetRoot -Parent) ((Split-Path $TargetRoot -Leaf) + '-backups') }
New-Item -Force -ItemType Directory -Path $TargetRoot | Out-Null
$Skills = switch ($Mode) { 'designer' { @('visual-art-director') } 'frontend' { @('creative-frontend-engineer') } default { @('visual-art-director','creative-frontend-engineer') } }
foreach ($Skill in $Skills) {
  $Source=Join-Path $PSScriptRoot "skills\$Skill"
  $Dest=Join-Path $TargetRoot $Skill
  if (-not (Test-Path (Join-Path $Source 'SKILL.md'))) { throw "Missing $Source\SKILL.md" }
  if (Test-Path $Dest) {
    New-Item -Force -ItemType Directory -Path $BackupRoot | Out-Null
    $Stamp=Get-Date -Format 'yyyyMMdd-HHmmss-ffff'
    $Backup=Join-Path $BackupRoot "$Skill.backup-$Stamp"
    Move-Item $Dest $Backup
    Write-Host "Backup (outside skills): $Backup"
  }
  Copy-Item -Path $Source -Destination $Dest -Recurse
  Write-Host "Installed: $Dest"
}
Write-Host 'Open Codex and invoke $visual-art-director or $creative-frontend-engineer.'
Write-Host 'For stale duplicates, run python3 scripts/doctor_skills.py --root <skills-folder> (dry-run), then --apply.'
