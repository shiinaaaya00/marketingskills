#!/usr/bin/env python3
from pathlib import Path
import argparse
import shutil

HERE = Path(__file__).resolve().parent
SKILL_ROOT = HERE.parent
TEMPLATES = SKILL_ROOT / "templates"

DIRS = [
    "inputs/brand",
    "inputs/product",
    "inputs/reference-videos",
    "inputs/product-images",
    "inputs/3d-cad",
    "inputs/audio",
    "work/keyframes/prompts",
    "work/keyframes/start",
    "work/keyframes/end",
    "work/reference-analysis",
    "work/video-clips",
    "exports/master",
    "exports/homepage",
    "exports/pdp",
    "exports/social",
]

TEMPLATE_MAP = {
    "PROJECT_BRIEF.md": "work/PROJECT_BRIEF.md",
    "BRAND_PROFILE.md": "work/BRAND_PROFILE.md",
    "PRODUCT_PROFILE.md": "work/PRODUCT_PROFILE.md",
    "REFERENCE_ANALYSIS.md": "work/REFERENCE_ANALYSIS.md",
    "STORYBOARD.md": "work/STORYBOARD.md",
    "VIDEO_PROMPTS.md": "work/VIDEO_PROMPTS.md",
    "render_manifest.template.json": "work/render_manifest.json",
    "QA_REPORT.md": "work/QA_REPORT.md",
    "DELIVERY_REPORT.md": "work/DELIVERY_REPORT.md",
}

def main():
    ap = argparse.ArgumentParser(description="Initialize a product-video project.")
    ap.add_argument("project_dir")
    args = ap.parse_args()

    root = Path(args.project_dir).resolve()
    root.mkdir(parents=True, exist_ok=True)

    for rel in DIRS:
        (root / rel).mkdir(parents=True, exist_ok=True)

    for src_name, dest_rel in TEMPLATE_MAP.items():
        src = TEMPLATES / src_name
        dest = root / dest_rel
        if not dest.exists():
            shutil.copy2(src, dest)

    source_audit = root / "work/SOURCE_AUDIT.md"
    if not source_audit.exists():
        source_audit.write_text(
            "# SOURCE AUDIT\n\n"
            "## Inputs found\n-\n\n"
            "## Missing inputs\n-\n\n"
            "## Conflicts\n"
            "| Field | Source A | Source B | Safe action |\n"
            "|---|---|---|---|\n\n"
            "## Status\n`UNVERIFIED`\n",
            encoding="utf-8"
        )

    print(f"Initialized product-video project at: {root}")

if __name__ == "__main__":
    main()
