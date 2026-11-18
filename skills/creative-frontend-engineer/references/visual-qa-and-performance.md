# Browser QA / performance

First screenshot static layout against approved desktop/mobile Figma. Compare: hero focal subject, ratio, crop, heading wraps, card geometry, whitespace rhythm, panel depth, overlay and CTA visibility. Record differences by severity P0/P1/P2 and fix P0/P1.

Test viewport widths 390, 768, 1440 unless handoff specifies more; real browser and DPR variation when feasible. Verify no horizontal overflow, drawer overlays or hidden tap targets. Check UI on no hover and reduced-motion.

Run available `npm run build`, lint/typecheck and tests; do not invent results. For complex scene, inspect CPU/GPU, asset waterfall, device DPR, frame drops and context failures with measured tools if possible. Prefer LCP hero imagery as optimized visible image and lazy-load 3D below fold. No universal threshold guessed as measured performance.

Critical smoke flow: home → browse/search → filter → PDP → variant → cart demo → checkout mock. Landing: CTA → form validation → success demo. If user requested only a hero, test hero's specified interactions rather than inventing checkout.

Keep console/network issue log with actual reproduction and screenshots; report limitations.
