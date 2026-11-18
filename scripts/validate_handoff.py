#!/usr/bin/env python3
"""Check handoff shape, approval gating; demo template is allowed to be exploring."""
import json,sys
from pathlib import Path
p=Path(sys.argv[1] if len(sys.argv)>1 else 'handoff/design-handoff.template.json')
d=json.loads(p.read_text(encoding='utf-8'))
req=['schema_version','project','project_type','status','scope','user_tasks','figma','visual_dna','responsive','tokens','states','interaction_specs','assets','hypotheses','acceptance','constraints','open_questions','evidence']
errors=[f'missing {key}' for key in req if key not in d]
if d.get('status') not in {'exploring','selected','approved','blocked'}:errors.append('invalid status')
if not isinstance(d.get('user_tasks'),list):errors.append('user_tasks must be a list')
if not isinstance(d.get('figma'),dict) or 'frames' not in d.get('figma',{}):errors.append('figma.frames missing')
if d.get('status')=='approved':
 if not d.get('approved_by'):errors.append('approved_by needed for approved status')
 if not d.get('figma',{}).get('file_url') and not d.get('evidence',{}).get('selected_visual_proof'):
  errors.append('approved status requires real Figma file URL or selected_visual_proof')
if errors:
 print('FAILED: '+'; '.join(errors));sys.exit(1)
print(f'OK handoff schema: {p} (status={d["status"]}; no live content verified)')
