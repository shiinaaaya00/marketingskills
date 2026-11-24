# Keyframe Rules

Keyframes are the visual anchors for stable image-to-video generation.

## Start frame

Must define:
- exact product variant;
- correct geometry;
- correct materials;
- correct logo/label;
- exact background;
- lighting direction;
- camera angle;
- product scale;
- negative space;
- beginning physical state.

## End frame

Use an end frame when:
- the product must land at a precise pose;
- a camera orbit must finish at a known angle;
- a hand interaction must end at a known state;
- a loop must bridge back cleanly;
- typography or packaging alignment matters.

## Product references

Use official product images as image references whenever supported.

Prefer:
1. clean front/three-quarter packshot;
2. close-up of critical details;
3. rear/control image;
4. included accessory image;
5. color swatch/variant image.

## Prompt discipline

A keyframe prompt should describe a still image, not a full motion sequence.

Include:
- product identity;
- composition;
- environment;
- materials;
- lighting;
- camera/lens character;
- brand mood;
- exact no-change constraints.

## Negative constraints

Common constraints:
- no altered product proportions;
- no extra buttons;
- no missing ports;
- no warped logo;
- no duplicated accessories;
- no incorrect label;
- no added text;
- no fantasy glow unless specified;
- no extra mist outlet;
- no floating parts unless storyboard requires it.

## File naming

`KF_<shot-id>_<variant>_START_v01.png`
`KF_<shot-id>_<variant>_END_v01.png`

Keep superseded versions; do not overwrite without a reason.
