# Frontend architecture for design-driven sites

1. Inspect existing repo; preserve framework, package manager, config and routes. Only new repo: suggest Vite + React + TypeScript; small microsite may stay vanilla JS. No dependency explosion.
2. Organize by cohesive feature: `app/`, `pages/`, `features/catalog/`, `features/product/`, `components/ui/`, `components/scene/`, `assets/`, `styles/tokens.css`, `data/mock/`. Adapt to existing conventions.
3. Strict boundary: UI view + state & mock service; do not implement backend. Types/model consistent: `Product`, `Variant`, `Price`, `Offer`, `Filter`, `DeliveryOption` only if specified.
4. Design tokens mirror approved Figma or documented derived values; name semantic tokens instead of random hex values.
5. Content, interactive state and layout separate. Avoid huge single-file React components, ad-hoc DOM mutations of React-managed nodes, and per-frame rerenders.
6. Assets: avoid hotlink-only if licensing/availability unknown. Prefer provided assets; add attribution/license manifest if third-party source.
7. Make demo state deterministic and resettable. Expose a visible Demo label where interactions simulate real commerce.
