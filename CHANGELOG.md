## 4.0 — Creative Art Director clean rewrite (2026-11-18)

- Rebuilt `visual-art-director` from scratch for **brief → original visual concept → scene specification → visual check**.
- Reduced designer skill from dozens of references to one compact creative-mechanics note.
- Kept Figma concept mode, existing brand systems, mobile/reduced motion and direct-build handoff to independent frontend skill.
- Simplified structural validator and installation documentation; previous content remains in Git history.
- Static integrity checked through the repository. Live Figma/browser QA not run.

## 3.5.2 — Adaptive UX Interview (2026-11-18, draft PR)

- Added design-brief interviewing: default AUTO, collaborative WORKSHOP, minimal-question FAST.
- One prioritized question when materially useful, grounded in prior answers/Design.md, with concise options, design tradeoffs and a senior recommendation.
- Optional native Codex `request_user_input` only when it is actually available in the active mode; plain-text fallback, separate approval handling and skip resilience.
- Decision Ledger and regressions R15–R18. No frontend generated.
- GitHub structural checks only; a live Codex question-card run and Figma testing remain unverified.

## 3.5.1 — Design.md source-of-truth support (2026-11-18, draft PR)

- Read actual project `Design.md` before concept ideation and Figma writing; inspect related assets, record source headings and provenance.
- Markdown-defined design systems work without a published Figma library: author native reusable components directly from source specs, and reuse library instances if available.
- Keep document verification separate from Figma render/read-back verification, and flag `DS_CONFLICT` where documentation and Figma diverge.
- Added protocol, starter template, R13/R14 regression and frontend handoff requirement.
- Validation limited to GitHub static file/reference checks; no actual project Design.md was provided or live Codex/Figma tested.

## 3.5 — Design System Lock (2026-11-18; candidate PR)

- Enforced `DS_LOCKED` for any existing product/Figma design: user-approved sources and actual component/token libraries outrank creative references.
- Mandatory read-only Figma/Code Connect/library discovery and source-backed Design System Inventory before mutating Figma.
- Required reuse of library component instances, variants, styles, variables and modes; no invented colors, fonts, widgets, icon styles, radii or responsive rules.
- Three creative concepts stay within the **same design system**; new identity/tokens only as separately labeled `PROPOSED EXTENSION` pending approval.
- Added structural DS Diff QA alongside visual screenshots, with `DS_VERIFIED | DS_UNVERIFIED | DS_BLOCKED` and regression cases R11/R12.
- **Status: source patch authored and checked structurally; real Codex/Figma read-back not run.**

## 3.4 — GitHub source-of-truth and design-only Anthropic advisor (2026-11-18)

- Read-only design-critique rubric distilled from public Anthropic `frontend-design` guidance without vendoring its original file or asking for frontend.
- Transparent labeling: local design review != real independent Claude review; external second opinion only when tool is genuinely connected.
- GitHub PR release protocol and safe repo publishing helper that does not overwrite the existing design-intelligence root skill.
- R09/R10 regression checks; v3.4 source archive. Live Figma / external Claude / GitHub full push tests NOT RUN.

## 3.3 — Living Research & Evidence Gates (2026-11-17)

- Added a research-to-release method: credible sources → candidate rule → counterexample → regression check → approval/release, without pretending LLM weights self-train.
- Added curated versioned `research/ideas.json` with provenance/status (initial entries are candidates until live regression); daily research prompt and R01–R08 regression bench.
- Refined Figma-native / Code-to-Canvas capability limits from official Figma sources and sharpened distinction between motion demos and validated commerce UX.
- Retained strict Figma-first / no frontend code by default, split skills and safe backups outside installed-skills directory.
- Ran only static checks for package; live Figma/design quality not certified.

## 3.2 — Figma-first cinematic concepts (2026-11-17)

- Reframed motion-site recreation prompts as source **specimens** for art direction, not requests to build coded sites.
- Added KAIRN/VELL design grammar decoder, hero plate and asset-led art direction, original scene production, Figma motion storyboard, and decision board.
- Added strict no-frontend-by-default guard: temporary coding only if explicitly requested; engineer skill unchanged.
- Added examples and regression checks for media-led campaigns, stateful configurators and Fresska mascot-driven marketplace promo.
- Retained installer compatibility and existing two-skill architecture.

## 3.1 — Concept quality correction / installer doctor

- Added mandatory Concept DNA and creative-quality-gate for promo/landing.
- Added Fresska mascot anti-kids regression case; stop generic hero + three cards.
- Added design screenshot critique/re-render and whole-page narrative proof.
- Fixed installer backups to live outside skills discovery root.
- Added reversible duplicate-skill doctor script (dry-run by default).

# Changelog

## 3.0 / 2026-11-17
- Split architecture: UX/design/Figma `visual-art-director` versus frontend-only `creative-frontend-engineer`.
- Preserved visual-art-director 2.0's scene blueprint, spatial and experimental studies, Figma guidance, typography, assets and QA.
- Added commerce benchmark, UX flow protocol, hypothesis preference vs usability vs A/B and three-concept diversity gates.
- Added user selection/explicit approval states and JSON+MD handoff contract.
- New frontend skill: stack choice, real interactions, 3D/cursor-follow, GSAP, WebGL fallback, reduced motion, visual QA, mock-only commerce.
- Safe installer for both, validator, realistic prompts, Fresska scoped example.

## From 2.0
- Concept exploration, local optional motion study, Code to Canvas and Figma-native routes.
