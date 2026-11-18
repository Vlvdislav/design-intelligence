# Commerce UX in frontend-only mode

Priority: search / results / usable facets / PDP / offer clarity / variants / cart / checkout UI. Do not make up payment flows, delivery services, taxes or stock rules. If source specifies no quick-add in listing, respect it.

For demo implementations use typed mock fixtures. Make state changes genuine and deterministic (no inert controls). Label simulation visibly in documentation and interface near checkout where it might be mistaken for purchase. Payment button must NOT imply real charge; use 'Demo confirmation' or disabled behavior with clear explanation.

For every listing/PDP, check: image quality/fallback, name, price, sale marking only if data supports, variant selection, stock, delivery text, trust, clear navigational origin. For mobile: sticky buy bar should not overlap page or safe area; filters drawer; soft keyboard visibility; cart total.

Responsive catalog tests at 390/768/1440; long titles and prices; 0 and 1000 items; empty filter combination; active promotions if supported; product variant differences. Think of Ozon as a dense information benchmark, Yandex Market as an ease-of-use reference, not UI templates to copy.
