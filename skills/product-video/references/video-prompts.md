# AI Video Prompt Rules

Write one prompt per shot.

## Prompt order

1. Product identity and source-lock.
2. Scene/environment.
3. Composition.
4. Camera motion.
5. Product/hand/object motion.
6. Lighting.
7. Material behavior.
8. Temporal pacing.
9. Ending state.
10. Hard consistency constraints.

## Prompt template

`[PRODUCT] appears exactly as in the supplied product reference images: [variant/material/geometry lock].`

`Scene: [environment/background/props].`

`Composition: [framing, product placement, frame occupancy, negative space].`

`Camera: [movement, speed, lens impression, focus behavior].`

`Action: [one primary action].`

`Lighting: [direction, softness, color temperature, highlight behavior].`

`Motion quality: [slow/controlled/realistic; no sudden acceleration].`

`End state: [precise landing pose or loop state].`

`Consistency: preserve [buttons/ports/logo/proportions/materials/accessory count]; do not add or remove product parts.`

## Negative prompt template

- no product redesign;
- no geometry morphing;
- no extra controls;
- no extra openings;
- no warped labels/logos;
- no duplicated accessories;
- no incorrect color;
- no flicker;
- no frame-to-frame texture crawling;
- no camera jitter;
- no impossible hand anatomy;
- no unverified visual claim;
- no text artifacts.

## Text

Prefer adding marketing copy in editing/web layout rather than asking the video model to render critical text.

If on-screen text must be generated, keep it minimal and expect a separate typography/compositing pass.

## Product claims

Translate verified features into visual behavior only when physically justified.

Example:
Verified: warm ambient light.
Safe visualization: visible glow from the documented light area.
Unsafe: inventing a projected light ring from a non-light-emitting base.

## Reference influence

Describe the principle, not the competitor:
- "restrained premium studio reveal with a narrow rim light"
instead of
- "make it exactly like Brand X's ad."
