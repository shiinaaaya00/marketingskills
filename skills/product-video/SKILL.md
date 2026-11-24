---
name: product-video
description: Create reusable ecommerce product-video plans and production packages from brand guidelines, product资料/images, and reference videos. Use for Homepage hero/product videos, PDP gallery/feature videos, social cutdowns, storyboards, keyframes, AI video prompts, render manifests, video-model handoff, QA, and export planning. Preserve product truth and brand consistency; do not invent features or claim rendering succeeded when no video renderer is available.
---

# Product Video

Build a production-ready ecommerce video package from the user's brand assets, product source-of-truth, product images, and reference videos.

Keep this file procedural. Load detailed rules from `references/` only when needed.

## 1. Required behavior

1. Treat supplied brand files, product specifications, product images, CAD/3D files, packaging files, and approved copy as source-of-truth.
2. Never invent product functions, dimensions, materials, labels, included items, claims, variants, internal structure, UI states, or certifications.
3. When information is missing:
   - continue with unaffected work;
   - mark the missing field `UNVERIFIED`;
   - avoid rendering or claiming the affected detail;
   - use a neutral placeholder only in planning documents.
4. Do not copy a reference video's copyrighted footage, music, exact branded graphics, logos, or distinctive shot-for-shot sequence. Extract transferable visual grammar: pacing, lens language, composition, lighting, transitions, information hierarchy, and function-demonstration logic.
5. Separate planning from rendering. A shot is not "generated" until a real video-generation tool/model returns an output.
6. Prefer multiple controlled 3–10 second shots over one long AI-generated video.
7. Preserve visual continuity across shots: same variant, proportions, materials, control layout, product geometry, packaging, accessories, and lighting logic unless the storyboard explicitly changes them.
8. Design Homepage and PDP versions from a shared master shot library instead of generating unrelated videos independently.

## 2. Project initialization

When starting a new product-video project:

1. Run:
   `python scripts/init_project.py <project-dir>`
2. Put user inputs under:
   - `inputs/brand/`
   - `inputs/product/`
   - `inputs/reference-videos/`
   - `inputs/product-images/`
   - `inputs/3d-cad/` when available
   - `inputs/audio/` when licensed audio is supplied
3. Keep generated work under `work/`.
4. Keep final deliverables under `exports/`.

Do not place user project assets inside the reusable skill directory.

## 3. Source audit

Read `references/source-of-truth.md`.

Create or update:
- `work/PROJECT_BRIEF.md`
- `work/BRAND_PROFILE.md`
- `work/PRODUCT_PROFILE.md`
- `work/SOURCE_AUDIT.md`

Lock the following before detailed prompts:
- exact product name;
- variants/colors;
- visible geometry and proportions;
- material/finish;
- controls, ports, openings, lights, mist/output location;
- included accessories;
- verified specs and claims;
- prohibited/unverified claims;
- brand typography/colors/tone;
- required logo treatment.

If product images disagree with written specs, flag the conflict. Do not silently choose one.

## 4. Analyze reference videos

Read `references/reference-video-analysis.md`.

For local videos, use:
`python scripts/extract_reference_frames.py <reference-video> <output-dir>`

Analyze:
- duration/aspect ratio;
- opening hook;
- shot lengths and rhythm;
- camera motion;
- lens/framing;
- product scale and placement;
- lighting;
- materials/backgrounds;
- transitions;
- typography;
- sound design;
- product/function demonstration;
- closing frame;
- transferable ideas;
- ideas that must NOT be copied.

Write one section per reference in:
`work/REFERENCE_ANALYSIS.md`

Then synthesize a reference strategy:
- `TAKE`: reusable principles.
- `ADAPT`: principles that need brand/product translation.
- `AVOID`: copying, mismatched aesthetics, or unsuitable techniques.

## 5. Define deliverables

Read `references/homepage-pdp-deliverables.md`.

At minimum define:
- master film;
- Homepage desktop hero;
- Homepage mobile hero;
- PDP gallery/main product video;
- PDP feature loops;
- poster/key art;
- optional social cutdowns.

Every deliverable must specify:
- purpose;
- target placement;
- duration;
- aspect ratio;
- loop/non-loop;
- audio policy;
- text policy;
- safe zones;
- maximum practical file-size/performance target;
- source shots used.

## 6. Build shot strategy

Read `references/shot-design.md`.

Create:
`work/STORYBOARD.md`

Map every verified selling point to at least one shot, but do not force all specs into video.

Use a controlled structure:
- hook/reveal;
- hero form;
- material/detail;
- core function;
- operation/use;
- included set/variants;
- lifestyle/context;
- brand/product close.

Each shot must have:
- shot ID;
- objective;
- verified product fact;
- duration;
- aspect-ratio intent;
- visual description;
- camera;
- product action;
- background/lighting;
- continuity constraints;
- text overlay;
- sound;
- reference influence;
- start-frame intent;
- end-frame intent;
- render risk;
- target deliverables.

Prefer 3–8 seconds per AI-generated shot. Extend only when the selected renderer is proven stable.

## 7. Keyframes

Read `references/keyframe-rules.md`.

For each shot, create:
- start-frame brief;
- optional end-frame brief;
- image-generation prompt;
- negative constraints;
- product consistency checklist.

If an image-generation tool/skill is available, generate keyframes using real product images as references whenever possible.

If no image-generation tool is available, create production-ready prompt files in:
`work/keyframes/prompts/`

Do not claim a keyframe exists unless an image file was actually created.

## 8. AI video prompts

Read `references/video-prompts.md`.

Create:
`work/VIDEO_PROMPTS.md`
and
`work/render_manifest.json`

Each render job must contain:
- `shot_id`
- `variant`
- `duration_seconds`
- `aspect_ratio`
- `fps`
- `mode` (`image_to_video`, `text_to_video`, `start_end_frame`, or renderer-specific equivalent)
- `prompt`
- `negative_prompt`
- `start_frame`
- `end_frame`
- `reference_images`
- `seed` when supported
- `continuity_notes`
- `output_path`
- `status`

Write prompts in natural production English unless the user requests another language.

Prompts must describe:
- subject;
- scene;
- composition;
- camera motion;
- product motion;
- lighting;
- texture/material behavior;
- temporal behavior;
- ending state;
- hard consistency constraints.

Do not overload a shot with multiple unrelated actions.

## 9. Video-model handoff

Read `references/video-model-routing.md`.

Detect the available path in this order:

1. native video-generation tool available to the agent;
2. connected MCP/plugin video renderer;
3. repository-provided CLI/SDK renderer;
4. configured API adapter using existing environment variables;
5. no renderer.

If a renderer exists:
- use the closest supported mode to the storyboard;
- send one shot per job unless batch rendering is explicitly reliable;
- save outputs into `work/video-clips/`;
- record tool/model/settings and returned asset path in `render_manifest.json`.

If no renderer exists:
- finish the full render package;
- set jobs to `READY_FOR_RENDER`;
- do not pretend video was generated.

Never hard-code API secrets into the skill, prompts, manifests, or repository.

## 10. QA and iteration

Read `references/qa.md`.

For every generated clip check:
- product identity;
- geometry;
- variant/color;
- controls/ports/openings;
- materials;
- text/logo/labels;
- accessory count;
- physical plausibility;
- temporal consistency;
- camera stability;
- unwanted morphing;
- flicker;
- false feature depiction;
- suitability for intended crop;
- loop quality where required.

Mark each shot:
- `PASS`
- `RETRY`
- `BLOCKED`
- `UNVERIFIED`

Retry only the failing shot; do not regenerate passed shots without a reason.

## 11. Edit and exports

Build the master edit from passed clips.

Create export plans under:
- `exports/master/`
- `exports/homepage/`
- `exports/pdp/`
- `exports/social/`

For web:
- prefer visually loss-minimized compression;
- create poster frames;
- keep autoplay hero versions muted and loop-safe;
- preserve readable safe areas for HTML copy/CTA;
- avoid baking essential CTA text into the only master;
- produce platform-appropriate MP4 and optional WebM when tooling supports it.

Do not make performance claims without measuring actual encoded files.

## 12. Final output

Deliver:
1. `PROJECT_BRIEF.md`
2. `BRAND_PROFILE.md`
3. `PRODUCT_PROFILE.md`
4. `SOURCE_AUDIT.md`
5. `REFERENCE_ANALYSIS.md`
6. `STORYBOARD.md`
7. keyframe files or keyframe prompt package
8. `VIDEO_PROMPTS.md`
9. `render_manifest.json`
10. generated clips when a renderer is available
11. `QA_REPORT.md`
12. Homepage/PDP/social edit plan or rendered exports
13. `DELIVERY_REPORT.md`

Use `python scripts/validate_manifest.py work/render_manifest.json` before completion.

Final status must explicitly state one of:
- `PLANNING_COMPLETE`
- `KEYFRAMES_COMPLETE`
- `READY_FOR_RENDER`
- `RENDER_PARTIAL`
- `RENDER_COMPLETE`
- `EXPORT_COMPLETE`

Never label the project `RENDER_COMPLETE` or `EXPORT_COMPLETE` unless the corresponding files exist.
