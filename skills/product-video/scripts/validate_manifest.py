#!/usr/bin/env python3
from pathlib import Path
import argparse, json, sys

VALID_MODES = {"image_to_video", "text_to_video", "start_end_frame"}
VALID_STATUS = {
    "PLANNED", "KEYFRAME_READY", "READY_FOR_RENDER", "RENDERING",
    "RENDERED", "PASS", "RETRY", "BLOCKED", "UNVERIFIED"
}

def fail(msg):
    print(f"ERROR: {msg}")
    return 1

def main():
    ap = argparse.ArgumentParser(description="Validate product-video render manifest.")
    ap.add_argument("manifest")
    args = ap.parse_args()

    p = Path(args.manifest)
    if not p.exists():
        sys.exit(f"Manifest not found: {p}")

    data = json.loads(p.read_text(encoding="utf-8"))
    jobs = data.get("jobs")
    if not isinstance(jobs, list) or not jobs:
        sys.exit("Manifest must contain a non-empty jobs array.")

    errors = []
    seen = set()

    for idx, job in enumerate(jobs):
        prefix = f"jobs[{idx}]"
        shot_id = job.get("shot_id")
        if not shot_id:
            errors.append(f"{prefix}: missing shot_id")
        elif shot_id in seen:
            errors.append(f"{prefix}: duplicate shot_id {shot_id}")
        seen.add(shot_id)

        dur = job.get("duration_seconds")
        if not isinstance(dur, (int, float)) or dur <= 0:
            errors.append(f"{prefix}: duration_seconds must be > 0")

        ratio = job.get("aspect_ratio")
        if not isinstance(ratio, str) or ":" not in ratio:
            errors.append(f"{prefix}: invalid aspect_ratio")

        mode = job.get("mode")
        if not isinstance(mode, str) or not mode:
            errors.append(f"{prefix}: missing mode")
        if mode and mode not in VALID_MODES and ":" not in mode:
            errors.append(
                f"{prefix}: custom mode '{mode}' should be namespaced, e.g. provider:mode"
            )

        if not job.get("prompt"):
            errors.append(f"{prefix}: prompt is empty")

        if mode in {"image_to_video", "start_end_frame"} and not job.get("start_frame"):
            errors.append(f"{prefix}: {mode} requires start_frame")

        if mode == "start_end_frame" and not job.get("end_frame"):
            errors.append(f"{prefix}: start_end_frame requires end_frame")

        status = job.get("status")
        if status not in VALID_STATUS:
            errors.append(f"{prefix}: unsupported status {status!r}")

        if not job.get("output_path"):
            errors.append(f"{prefix}: missing output_path")

    if errors:
        print("\n".join("ERROR: " + e for e in errors))
        sys.exit(1)

    print(f"Manifest valid: {len(jobs)} job(s).")

if __name__ == "__main__":
    main()
