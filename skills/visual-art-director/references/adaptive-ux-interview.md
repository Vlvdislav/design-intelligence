# Adaptive UX Interview — Senior Designer asks only decision-changing questions

An effective senior designer does not transfer design work to the client. This protocol is about **co-creation**, not a mandatory questionnaire or automated form.

## Modes

| Mode | Selection | Behavior |
|---|---|---|
| `AUTO` | Default | Read context and Design.md first. Ask one question if user input significantly changes the UX/visual concept. Otherwise assume reversibly and work. |
| `WORKSHOP` | User invites discussion ("давай обсудим", "задавай вопросы", "хочу выбирать") | Ask one concrete question at each meaningful unresolved checkpoint; offer an informed recommendation and move forward after the user's answer. |
| `FAST` | User asks "сделай сам", "без вопросов" | Don't interrogate. Make explicit reversible assumptions, deliver concepts, stop only at real blockers or permission/approval boundaries. |

Never require the user to pick a mode manually. Modes are conversation preferences, **not** Codex collaboration modes. Changing WORKSHOP/FAST does **not** grant access to tools or change Codex Plan/Default Mode.

## Prioritize source reading

1. Locate/read real project `Design.md`, approved product frames, existing decisions, known audience and business constraints. Do not ask for facts already present.
2. Make a short internal gap register: `KNOWN`, `ASSUMED`, `BLOCKER`, `USER_DECISION`.
3. Ask only when impact is high. Rank candidate questions by **UX decision impact**, irreversibility/cost and uncertainty. A minor image crop or radius is NOT worth stopping.
4. No redundant demographic questions, no "what style" without specifics, no asks about tools/libraries/animation techniques if the user asked for design concepts.

## A good question

- Ask **one** user-facing question at a time, in a single sentence.
- Prefer 2–3 real, mutually exclusive options (not vague "yes/no" where a better UX choice exists). Explain the outcome/tradeoff in a few words; label a recommended choice.
- Offer a free-form answer and skipping, when supported by current UI. If using normal chat, include one short question instead of an artificial multiple-choice form.
- Examples:
  - "Что пользователь должен сделать в первую очередь: перейти к товарам или исследовать бренд? Рекомендую товары первым шагом, если цель — продажи с холодного трафика."
  - "В мобильном каталоге фильтры важнее сравнения? Для частых покупок рекомендую быстрые фильтры, но проверю в first-click тесте."
- Don't promise that the model can control the presence of a UI widget. Don't over-explain options in large text.

## Codex UI reality — native question-card is CONDITIONAL

The official Codex repository includes `request_user_input`, but availability is determined by the active mode and exposed tools, **not** by the skill.

- In Plan Mode, when `request_user_input` is available, prefer using it for consequential user/product planning choices. Tool parameters require `questions`, and current official schema uses `id`, `header`, `question` and `options`; provide 2–3 concrete choices with labels and short descriptions. Prefer a single question (never more than three). The client adds free-form "Other".
- In Default Mode, prefer reasonable assumptions and progress; only use the native tool if it is actually exposed and its own active-mode instructions permit it. If a genuine blocking question cannot be answered safely, ask one concise question directly.
- If the tool is unavailable, use **one plain-text question** (not fabricated JSON, custom widget calls or pretend request_user_input). Do not force the user into Plan Mode.
- Skipped or empty response → record a reasonable `ASSUMED` default and proceed if safe; do not repeat or stall.
- **Permissions:** never use `request_user_input` as a substitute for approval prompts, overwriting authorization or permission escalation. Follow the Codex host's approval mechanism.
- A question UI shown in one screenshot does not prove this tool is exposed to all Codex runs.

Official source references:
- https://github.com/openai/codex/blob/main/codex-rs/core/src/tools/handlers/request_user_input_spec.rs
- https://github.com/openai/codex/blob/main/codex-rs/collaboration-mode-templates/templates/plan.md
- https://github.com/openai/codex/blob/main/codex-rs/collaboration-mode-templates/templates/default.md

## Question checkpoints

| Stage | Question allowed when | Designer's preparation |
|---|---|---|
| Product/job discovery | Two materially different user goals, same vague brief | Product hypothesis, 2–3 paths, recommended objective |
| UX flow definition | Navigation model, CTA intent or trust/commerce step is unclear | User journey, risk and an alternative |
| Concept comparison | 2–3 actual visual alternatives are shown and selection is not yet made | Screenshots, UX differences, which hypotheses to test |
| Iteration | User proposes a targeted change whose UX implications differ | Keep approved constraints, explain local tradeoff |
| Figma / design-system conflict | An essential, unresolved conflict affects the permitted work | Identify exact conflict and request a decision |

No mandatory question at every checkpoint. A concept selection is never automatically final approval.

## Decision Ledger

Maintain an in-conversation record; when the user explicitly wants a project file, save it as an artifact under the project's approved location. Do not edit the source `Design.md` without approval.

```text
decision_id | stage | question | options considered | user's answer | status (USER / ASSUMED / OPEN) | impact on UX | date
UX-01       | discover | Primary task: shop or brand story? | shop, story | shop | USER | CTA leads to categories | ...
```

On a new user answer, update only its affected decision and dependent screens. A "skip" is not an approval. Never repeat answered questions unless the user explicitly revises their preference.

## Acceptance

- Known data is gathered and used before questions.
- No multi-question wall; one decision per step.
- Each question improves UX, has an honest recommendation and a follow-on action.
- Answers genuinely change concepts/flows; no repeated questions.
- Design system remains locked, unless the user expressly changes it.
- No frontend; concept/Figma output remains primary.
