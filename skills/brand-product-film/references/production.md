# Production and delivery

## Timing and rendering

Choose an exact frame rate and calculate each shot's frame count from its duration. The sum must match the intended running time. Treat the frame rate as part of the asset contract.

Save an editable scene with named cameras or scenes, then render a separate numbered sequence for each shot. Track the frame count per shot. On a retry, verify existing images and render the missing or damaged frames. An existing filename alone is insufficient evidence of completion.

Changing geometry, materials, lights, cameras or render settings invalidates the corresponding old frames even if those files decode correctly. Use a separate output revision or force those shots to render again.

Use a continuous motion proxy to inspect camera easing, focus changes and transitions. Label its actual resolution and frame rate. A sequence of held keyframes is useful for storyboarding but does not verify continuous camera movement. Evaluate fine grooves and metal reflections at the intended final resolution before interpreting aliasing in a small proxy.

Keep cut boundaries independent when generating effects, interpolation or retiming. Encode each shot over its exact frame range so frames from adjacent cameras are never blended across a cut.

Measure scene performance on the real render device. CPU Cycles, GPU Cycles and Eevee are options. Check metal reflections, fine geometry, transparency, depth of field, noise and temporal stability in the chosen engine. Record any tradeoff that affects delivered resolution or motion.

## Copy and audio

Use evidence-backed feature language. Treat product dimensions, capacities, coverage, noise, runtime and compatibility as factual claims requiring product evidence. Descriptive aesthetic copy can support the visuals.

Render small text and logos from clean source assets. Keep final typography in a separate editable layer or reproducible compositor. Inspect it at the actual delivery size. Preserve the official mark's geometry when adapting its color to the scene.

Check text against the moving background throughout its visible range. A color that works over a dark studio may disappear over a light shell or interior. Reposition or recolor the text to preserve readability without covering the product.

Use licensed or original audio and retain its provenance. Place impacts at intentional cuts and reveals, preserve headroom, and fade the ending. Listen to both the master and standalone clips.

Let the soundtrack follow the story: quieter reveal, articulated detail rhythm, a more spacious lifestyle section and a deliberate brand resolution. Preserve separate music and sound-design stems when generating or editing the score. Report automated loudness and clipping checks separately from an actual listening review.

The included score generator creates a simple original electronic bed from oscillators and shaped noise. It is optional and should suit the visual brief. Run it with a JSON settings file containing duration, optional impact times and a seed.

```powershell
python scripts/synthesize_score.py music.json score.wav
```

## Encoding manifest

The encoder accepts a JSON file with paths relative to the manifest. Example values are illustrative.

```json
{
  "fps": 24,
  "width": 1920,
  "height": 1080,
  "audio": "assets/score.wav",
  "font": "assets/title.ttf",
  "logo": "assets/logo.png",
  "shots": [
    {
      "name": "01_Reveal",
      "seconds": 4,
      "frames": 96,
      "directory": "Frames/01_Reveal",
      "titles": [
        {"text": "INTRODUCING", "x": 140, "y": 840, "size": 30}
      ]
    },
    {
      "name": "02_Product",
      "seconds": 4,
      "frames": 96,
      "directory": "Frames/02_Product",
      "titles": [
        {"text": "Product Name", "x": 140, "y": 440, "size": 110}
      ],
      "show_logo": true
    }
  ]
}
```

Every sequence starts at 0001.png. Each shot name is a simple filename stem. The final master joins the shots and uses the continuous score to avoid audio discontinuities at encoded segment boundaries. Each standalone clip also includes its corresponding portion of the soundtrack.

```powershell
python scripts/encode_sequence.py manifest.json --ffmpeg path/to/ffmpeg.exe --output Delivery
python scripts/encode_sequence.py manifest.json --ffmpeg path/to/ffmpeg.exe --output Delivery --dry-run
```

## Final inspection

Check representative moving frames, both endpoints of each shot, the complete duration and transitions. Decode the entire master to detect corruption. Inspect fine patterned surfaces for moire, ghosting and flashing. Confirm that text, product and mark fit the target aspect ratio.

For another aspect ratio, reframe the scene and titles as needed. A crop may be sufficient for some shots, while others need a separate camera. Record any omitted deliverable or unresolved limitation.

Copy the accepted deliverables to the requested location and verify hashes. Keep a manifest of the delivered files and render settings. If uploading a reusable workflow, use generic paths and parameterized examples.

