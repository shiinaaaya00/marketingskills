#!/usr/bin/env python3
from pathlib import Path
import argparse

EXPECTED_INPUT_DIRS = [
    "inputs/brand",
    "inputs/product",
    "inputs/reference-videos",
    "inputs/product-images",
]
EXPECTED_WORK_FILES = [
    "work/PROJECT_BRIEF.md",
    "work/BRAND_PROFILE.md",
    "work/PRODUCT_PROFILE.md",
    "work/SOURCE_AUDIT.md",
    "work/REFERENCE_ANALYSIS.md",
    "work/STORYBOARD.md",
    "work/VIDEO_PROMPTS.md",
    "work/render_manifest.json",
]

def count_files(path):
    return sum(1 for p in path.rglob("*") if p.is_file()) if path.exists() else 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project_dir")
    args = ap.parse_args()
    root = Path(args.project_dir).resolve()

    print(f"Project: {root}")
    print("\nInputs:")
    for rel in EXPECTED_INPUT_DIRS:
        p = root / rel
        print(f"- {rel}: {count_files(p)} file(s)")

    print("\nWork files:")
    missing = []
    for rel in EXPECTED_WORK_FILES:
        ok = (root / rel).exists()
        print(f"- {'OK' if ok else 'MISSING'} {rel}")
        if not ok:
            missing.append(rel)

    if missing:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
