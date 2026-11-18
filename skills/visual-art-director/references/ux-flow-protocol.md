# Senior UX workflow: from job to interaction

For every page, define: user segment / intent / context / entry / decision / successful action / failure / next step. Separate primary vs secondary task. Build an IA outline and a user flow using arrows and state IDs. The design must solve the *decision*, not merely show attractive UI.

## Marketplace example (adapt, don't assume real capabilities)

`ENTRY → Search/Category → Listing → Filters → PDP → Variant/Offer → Cart → Checkout → Confirmation`.
Branches: no results → edit query; invalid filter combo → reset; unavailable item → alternatives; out of stock → status; quantity issue → feedback; offline → retry; unavailable delivery method → alternative; logged-out checkout → guest/auth based on verified policy.

For every node, document: visible information, controls, system feedback, error recovery, accessibility, measurement event (proposed, not implemented).

## Landing example

`Traffic context → relevance in first viewport → evidence + product demonstration → objection handling → CTA → completion state`.
Motion may reinforce the story but cannot delay discovery of product or CTA. Add skip/reduced-motion equivalent.

## Evaluate before rendering

- Five-second test: what is this, whom for, what is the next step?
- First click: can users predict correct control?
- Copy: avoid jargon; proper Russian grammar and numbers, no fake testimonials.
- Multi-device: keyboard focus, 390px touch target, dynamic content, long strings.
- Reachability: no essential hover-only interaction on mobile.

## Deliverable wireflow format

`screen_id | goal | entry state | content hierarchy | actions | next screens | edge/error states | hypothesis | evidence level`.
