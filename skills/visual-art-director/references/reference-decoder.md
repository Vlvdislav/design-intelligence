# Reference Decoder — inspect, measure, reproduce

**Use before creating Figma frames.** A reference is a design specification, not vague inspiration.

## 1. Inspect the source

For each screenshot, prompt, Figma frame or web page capture:

- **Identity:** logo, colors, fonts (verified or estimated), tone, text, imagery.
- **Geometry:** artboard size, safe areas, column count, content width, gutters, vertical rhythm, alignments, overlaps, negative space.
- **Components:** button dimensions, corner shape, outlines, tabs, cards, image borders, states.
- **Scene layers:** background → typography → hero assets → foreground → UI; cropping, blur, shadows and depth.
- **Motion:** trigger, entering/leaving layers, direction, distance, timing, easing, start/end keyframes, reduced-motion state.
- **Responsive:** whether mobile changes composition, hides decoration, reorders content, resizes text or moves navigation.
- **Evidence:** user-supplied exact number = `EXACT`; measured in visible source = `OBSERVED`; estimated by visual analysis = `ESTIMATED`; source unavailable = `MISSING`.

A screenshot does **not** reveal hidden implementation, exact fonts, animation timing or real functionality. Never invent certainty.

## 2. Token sheet and source map (internal)

```text
SOURCE: reference name/link
ROLE: grid / typography / palette / motion / image / exact layout
CANVAS: W × H
GRID: columns, outer margins, gaps, alignment
TYPE: family? weights, sizes, line height, tracking
COLOR: base, surface, text, accent
IMAGES: named assets, crop/placement, layer order
COMPONENTS: buttons, cards, nav, their variants
SCENE: element -> x / y / w / h / z-order
MOTION: state A -> state B, trigger, keyframe, duration
MATCH: which Figma frame/element recreates which source element
UNKNOWN: what could not be confirmed
```

Prioritize **geometry + imagery + typography** before micro-decoration. Don't swap in a familiar card grid because it is easier to build.

## 3. Multiple-reference discipline

If the user says "use reference A for grid and B for typography", never use B's layout or A's palette by accident. Do not blend whole pages indiscriminately. Keep brand identity distinct from borrowed compositional language unless exact recreation was explicitly requested. Map only approved transformations.

## 4. Visual verification

Render at the reference viewport first. Compare source and Figma in the same crop:
1. Focal object location, proportion and image treatment.
2. Large type scale/line breaks.
3. Outer margins, columns, whitespace, section heights.
4. Colors and component details.
5. Mobile frame and named interaction states.

If one fails, revise it **before** adding extra sections. Report screenshot/Figma availability honestly. 
