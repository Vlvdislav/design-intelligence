# Contract for actually interactive UI

For each user action, specify `element | pointer | keyboard | touch | state change | visible feedback | undo/cancel | fallback | verification`.

Examples:
- Search: type query → filtered fixture results; Escape clears suggestion overlay; clear button works; empty state and reset.
- Filter: selectable facets, count/range derived from mock catalog; clear all, proper focus.
- Product variants: selected option changes state and relevant imagery/pricing if supplied; no false visual change if assets absent.
- Cart demo: add/remove/update quantity, subtotal calculation from fixture, cart count update; clearly no real order.
- Mobile drawers: trap focus properly while open, Escape/overlay close, restore focus; underlying page not scrollable.
- Spatial orbit: drag + arrow keys + buttons + accessible item list; no invisible-only gestures.
- Cursor follower: decorative only, no click obstruction; coarse pointer disabled/static; reduced motion supported.

Telemetry events only proposed (e.g. `product_view`, `variant_select`, `add_to_cart_demo`); no undeclared external analytics calls.
