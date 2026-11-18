#!/usr/bin/env python3
"""Static structural verification only; does not replace live Figma/browser QA."""
from pathlib import Path
import re, sys, json
root=Path(__file__).resolve().parents[1]
required={
'visual-art-director':[
 'SKILL.md','agents/openai.yaml',
 'references/brief-and-intents.md','references/research-protocol.md',
 'references/creative-method.md','references/scene-blueprint.md',
 'references/spatial-motion-playbook.md','references/experimental-prototyping.md',
 'references/typography-lab.md','references/imagegen-playbook.md',
 'references/figma-mcp-production.md','references/qa-and-acceptance.md',
 'references/ecommerce-ux-benchmarks.md','references/ux-flow-protocol.md',
 'references/hypothesis-voting-testing.md','references/creative-signatures.md',
 'references/figma-review-gates.md','references/handoff-contract.md',
 'references/design-handoff.template.json','references/UX-FLOW.template.md','references/MOTION-SPEC.template.md',
 'references/fresska-v3-brief.md','references/fresska-example-brief.md','references/ready-prompts-v3.md',
 'references/creative-quality-gate.md','references/fresska-promo-case.md',
 'references/motion-reference-decoder.md','references/asset-led-concept-production.md',
 'references/figma-motion-storyboard.md','references/concept-decision-board.md',
 'references/living-research-loop.md','references/source-quality-and-figma.md','references/regression-scenarios.md',
 'references/claude-frontend-design-advisor.md','references/github-research-workflow.md',
 'references/design-system-lock.md',
],
'creative-frontend-engineer':[
 'SKILL.md','agents/openai.yaml','references/frontend-architecture.md',
 'references/interaction-contract.md','references/motion-3d-engineering.md',
 'references/commerce-frontend.md','references/visual-qa-and-performance.md',
 'references/delivery-checklist.md',
]}
errors=[]
for skill,rels in required.items():
 s=root/'skills'/skill
 for rel in rels:
  p=s/rel
  if not p.exists() or not p.read_text(encoding='utf-8').strip():errors.append(f'missing/empty {skill}/{rel}')
 path=s/'SKILL.md'
 if path.exists():
  content=path.read_text(encoding='utf-8')
  front=re.match(r'^---\n(.*?)\n---\n',content,re.S)
  if not front:errors.append(f'invalid frontmatter {skill}')
  else:
   if not re.search(r'^name:\s*'+re.escape(skill)+r'\s*$',front.group(1),re.M):errors.append(f'wrong slug for {skill}')
   if not re.search(r'^description:',front.group(1),re.M):errors.append(f'no description for {skill}')
  for ref in set(re.findall(r'`(references/[a-z0-9-]+\.md)`',content)):
   if not (s/ref).is_file(): errors.append(f'broken {skill}/{ref}')
  if f'${skill}' not in (s/'agents/openai.yaml').read_text(encoding='utf-8'):
   errors.append(f'agent prompt missing ${skill}')
for rel in ['README.md','INSTALL.md','CHANGELOG.md','install.sh','install.ps1','handoff/design-handoff.template.json','handoff/UX-FLOW.template.md','handoff/MOTION-SPEC.template.md','examples/READY-PROMPTS-V3.md','examples/FIGMA-FIRST-MOTION-CONCEPTS.md','examples/fresska-v3-brief.md','scripts/validate_handoff.py','scripts/doctor_skills.py','scripts/validate_research.py','examples/DAILY-RESEARCH-BRIEF.md','research/ideas.json']:
 if not (root/rel).exists():errors.append('missing '+rel)
a=(root/'skills/visual-art-director/SKILL.md').read_text(encoding='utf-8')
b=(root/'skills/creative-frontend-engineer/SKILL.md').read_text(encoding='utf-8')
for needle in ['UX','Figma','hypotheses','approved','HANDOFF','дизайн','голосование','creative-quality-gate','Figma-first','motion-reference-decoder','figma-motion-storyboard','design-system-lock','DS_LOCKED']:
 if needle.lower() not in a.lower():errors.append(f'designer missing {needle}')
for needle in ['frontend','backend','GSAP','Three.js','reduced motion','Figma','browser','approved']:
 if needle.lower() not in b.lower():errors.append(f'engineer missing {needle}')
try:json.loads((root/'handoff/design-handoff.template.json').read_text(encoding='utf-8'))
except Exception as e:errors.append('invalid handoff json '+str(e))
try:
 ledger=json.loads((root/'research/ideas.json').read_text(encoding='utf-8'))
 assert isinstance(ledger.get('records'),list)
 required_keys={'id','title','source_url','source_type','observed','proposal','status','test_scenario'}
 assert all(required_keys.issubset(rec) and rec['status'] in {'candidate','tested','accepted','rejected','superseded'} for rec in ledger['records'])
except Exception as e: errors.append('bad research ledger '+str(e))
if errors:
 print('FAILED:\n'+'\n'.join('- '+e for e in errors));sys.exit(1)
print('OK: two independent skills,',sum(map(len,required.values())),'skill files + package/contract files, reference paths, basic policies.')
print('STATIC ONLY: live Figma MCP, browser and code build were not executed.')
