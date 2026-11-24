#!/usr/bin/env python3
"""
Extract metadata + evenly spaced reference frames with ffprobe/ffmpeg.
Requires ffmpeg and ffprobe on PATH.
No OCR is performed.
"""
from pathlib import Path
import argparse, json, math, subprocess, sys

def run(cmd):
    return subprocess.run(cmd, check=True, text=True, capture_output=True)

def probe(video: Path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration:stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate",
        "-of", "json", str(video)
    ]
    return json.loads(run(cmd).stdout)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("output_dir")
    ap.add_argument("--frames", type=int, default=12,
                    help="Number of evenly spaced frames (default: 12)")
    args = ap.parse_args()

    video = Path(args.video).resolve()
    out = Path(args.output_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)

    if not video.exists():
        sys.exit(f"Video not found: {video}")

    try:
        meta = probe(video)
    except FileNotFoundError:
        sys.exit("ffprobe/ffmpeg not found on PATH.")
    (out / "metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    duration = float(meta.get("format", {}).get("duration", 0) or 0)
    if duration <= 0:
        sys.exit("Could not determine video duration.")

    n = max(2, args.frames)
    times = [(duration * (i + 1) / (n + 1)) for i in range(n)]

    frame_dir = out / "frames"
    frame_dir.mkdir(exist_ok=True)

    for i, t in enumerate(times, 1):
        dest = frame_dir / f"frame_{i:02d}_{t:07.2f}s.jpg"
        cmd = [
            "ffmpeg", "-hide_banner", "-loglevel", "error",
            "-ss", f"{t:.3f}", "-i", str(video),
            "-frames:v", "1", "-q:v", "2", "-y", str(dest)
        ]
        subprocess.run(cmd, check=True)

    notes = out / "analysis-notes.md"
    if not notes.exists():
        notes.write_text(
            f"# Reference Analysis Notes\n\n"
            f"- File: {video.name}\n"
            f"- Duration: {duration:.2f}s\n"
            f"- Extracted frames: {n}\n\n"
            "## Shot analysis\n"
            "| Time | Purpose | Camera | Lighting | Transition | Transferable principle |\n"
            "|---|---|---|---|---|---|\n",
            encoding="utf-8"
        )

    print(f"Wrote metadata and {n} frames to: {out}")

if __name__ == "__main__":
    main()
