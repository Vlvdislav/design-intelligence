#!/usr/bin/env python3
"""Checks research ledger integrity. Does not prove claims or the visual quality."""
import json, pathlib, sys
p=pathlib.Path(__file__).resolve().parents[1]/'research'/'ideas.json'
a=json.loads(p.read_text(encoding='utf-8'))
ids=set(); errs=[]
for x in a.get('records',[]):
 id=x.get('id'); url=x.get('source_url','');status=x.get('status','')
 if not id or id in ids:errs.append(f'duplicate/missing id: {id}')
 ids.add(id)
 if not url.startswith('https://'):errs.append(f'bad source URL: {id}')
 if status not in ('candidate','tested','accepted','rejected','superseded'):errs.append(f'bad status: {id}')
 if not x.get('test_scenario','').startswith('R'):errs.append(f'missing test scenario: {id}')
print('FAILED: '+', '.join(errs) if errs else f'OK: {len(ids)} source records, IDs, statuses and URL formats; source claims NOT independently verified by this script.')
sys.exit(1 if errs else 0)
