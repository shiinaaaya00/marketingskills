---
name: brand-product-film
description: Create a rendered brand or product launch film from photos, CAD or Blender scenes, including material matching, storyboard, camera and light animation, segmented delivery, sound and export. Use when a user wants a finished product film or a reusable production workflow.
metadata:
  version: 1.0.0
---

# Brand product film

Produce the requested playable video together with the editable scene and reproducible source. Use the user's product, accepted visual corrections, language, output location and distribution formats. Resolve ordinary production choices from the conversation and available assets.

## Establish the source of truth

Inspect the provided photos, dimensions, logos, scene files and CAD. Record which assets actually exist and which conclusions came from an earlier chat. Identify the product and revision before transferring features between models. A filename, matching hash or importable Python package alone does not establish geometric validity or a match to the physical product.

Keep these meanings explicit when needed.

- A storyboard specifies shots, action, copy and timing.
- A Python script implements scene creation or automation.
- A Blender scene stores geometry, materials, lights, cameras and animation.
- CAD supplies structural geometry. Photos and product evidence guide appearance and claims.

When CAD is available, measure its units and assembled bounds, inspect parts and geometric validity, then inspect the tessellated mesh. Retain its original dimensions in the validation record. If the production dimensions differ, identify the affected parts using the photos and specifications. Read [CAD and appearance checks](references/cad-and-appearance.md) when processing STEP or correcting an inaccurate model.

An existing usable scene can be the starting point. Request missing CAD, measurements or production information only when it affects a shot that the user actually needs.

## Build the film

Write a concise timed shot list with the audience-facing copy. Develop the rhythm around the requested style and verified product features. Choose close-ups, light sweeps, assembly, hero views or lifestyle shots to support that story. Use a real part breakdown and verified sequence for assembly claims.

Match material color, roughness, microscopic finish and reflection direction against the user's reference. Use neutral test lighting to inspect appearance before introducing dramatic lighting. Carry accepted material changes into the generation script and regenerate the scene.

Test representative frames at each cut, including the first and last frame of tight shots. Evaluate the available render devices and benchmark a representative frame before choosing resolution and samples. Use a render method that preserves the requested product and movement. Disclose resolution scaling or frame interpolation if used.

Read [Production and delivery](references/production.md) for resumable rendering, typography, audio and final checks.

## Deliver and verify

Deliver the complete film and standalone clips when requested. Include the editable scene, scripts, a shot manifest and the assets needed to reproduce the edit. Pack required scene dependencies or use portable relative paths. Keep intermediate frames out of a compact delivery unless the user requests them.

Use [the sequence encoder](scripts/encode_sequence.py) to validate frame ranges, title and encode a manifest-driven edit. Use [the procedural score generator](scripts/synthesize_score.py) when an original synthetic soundtrack fits the brief. Follow the manifest format documented in the production reference.

Before declaring completion, decode the full master, check duration and frame count, inspect a contact sheet and verify copied deliverables by hashes. Save the verified output locations and any unresolved accuracy limits.

If the user requests a repository upload or Notion workflow page, use the specified destination and actual connected account. Follow the repository's instructions and versioning. Keep product photos, CAD, credentials and private business information out of a public reusable skill. Report the saved URLs and any pending merge or publication step.

