# Motion & 3D — tech decision and implementation bar

## When to pick what

- CSS / Web Animations: hover/focus, mild parallax, image reveals, button states, inexpensive 2.5D product cards.
- GSAP (optionally ScrollTrigger): complex choreography, scrub narrative, synchronized layers; cleanup with contexts/revert; `gsap.matchMedia()` for breakpoints and reduced motion.
- Motion: framework-friendly gestures and transition choreography, but don't combine several animation engines on the same properties without a reason.
- Three.js/R3F: true orbit camera, 3D object, depth/raycasting, shaders, particles, physically meaningful lighting. Use loading placeholder and static fallback.
- Lenis / custom smooth scroll: only if asked and benchmarked; never break native accessibility, anchor navigation or browser scroll behavior.

## Cursor-follow hero spec

Track normalized pointer in [-1,1], smooth target with dt-dependent interpolation (not raw frame-rate constants). Map to small controlled rotation around neutral pose, clamp bounds, preserve object center. Use `pointermove` passive where possible; do not block clicks. For touch disable mouse-follow and allow scroll/optional direct rotation. On reduced motion display neutral image/pose; if object missing render a product photo. Test at 60/120Hz, resize and 390px viewport.

## Three.js lifecycle

Limit pixel ratio on mobile, test shader compile/WebGL failure, pause when offscreen via IntersectionObserver when available, handle visibilitychange, use renderer `setAnimationLoop` as recommended by official docs, dispose geometries/materials/textures/render targets and remove event listeners. Avoid multiple active render loops and full-screen shaders on every product tile.

## Scroll and time

Define per effect: trigger, start/end, user input, duration, easing, cancel, keyboard equivalent, reduced-motion equivalent. Do not pin entire catalog, trap scrolling, or delay purchase CTA. Animate transform/opacity where possible, beware layout jank. Don't claim measured FPS without profiling.

## Motion test

1. With mouse: move, click, drag, flick, wheel. 2. Keyboard: tab, enter, arrows, escape. 3. Touch: swipe, scroll, tap. 4. Reduced motion. 5. Slow device/network or no WebGL. 6. Resize/orientation. Every effect should degrade rather than disappear with missing core functionality.

Official docs to consult when coding: https://gsap.com/docs/v3/Plugins/ScrollTrigger/ ; https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/ ; https://threejs.org/docs/pages/WebGLRenderer ; https://motion.dev/docs .
