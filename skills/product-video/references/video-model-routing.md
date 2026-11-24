# Video Model Routing

The skill is model-agnostic.

## Goal

Turn `render_manifest.json` jobs into actual clips using whatever renderer is available in the current Codex environment.

## Routing order

### A. Native video tool
Use when the current agent exposes a video generation function.

Map:
- prompt;
- duration;
- aspect ratio;
- start frame;
- end frame;
- reference images;
- seed;
- output.

Record the real model/tool name and returned asset path.

### B. MCP / plugin renderer
If a connected app exposes text-to-video, image-to-video, or start/end-frame video generation, inspect its schema and map the manifest fields exactly.

Do not assume unsupported parameters.

### C. Repository CLI / SDK
Use a renderer already present in the user's repository when:
- the command is documented;
- credentials are already configured in environment variables;
- executing it will not expose secrets.

### D. API adapter
Only create or use an API adapter when the project already has an approved provider and environment-variable configuration.

Never place raw API keys in:
- `SKILL.md`;
- prompt files;
- JSON manifests;
- shell history committed to git.

### E. No renderer
If no valid renderer exists:
- create all keyframe prompts;
- create all video prompts;
- create `render_manifest.json`;
- set each eligible job to `READY_FOR_RENDER`;
- report which renderer capability is missing.

This is still a successful planning handoff, but not a successful render.

## Capability matching

Choose the lowest-risk mode that preserves product consistency:

1. start+end-frame video, when available and precise landing matters;
2. image-to-video with a verified product keyframe;
3. multi-reference video when product references are supported;
4. text-to-video only for low-risk atmosphere/B-roll shots.

Avoid pure text-to-video for hero product identity shots when accurate reference conditioning is available.

## Retry strategy

For a failed shot:
1. determine whether failure is identity, geometry, motion, camera, or temporal;
2. change only the relevant prompt/control;
3. keep approved keyframes;
4. preserve seed when the model supports deterministic refinement and the visual base is useful;
5. increment version number;
6. record the retry reason.

Do not regenerate the entire film because one shot failed.
