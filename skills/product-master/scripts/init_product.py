#!/usr/bin/env python3
from pathlib import Path
import argparse, shutil

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
TEMPLATES = ROOT / "templates"

DIRS = [
    "inputs/brand",
    "inputs/specs",
    "inputs/product-images",
    "inputs/packaging",
    "inputs/bom-cost",
    "inputs/sku-inventory",
    "inputs/listings",
    "inputs/copy-marketing",
    "inputs/compliance",
    "inputs/research",
    "inputs/notes",
    "work",
    "exports/archive",
]

COPY = {
    "SOURCE_INVENTORY.md": "work/SOURCE_INVENTORY.md",
    "SOURCE_AUDIT.md": "work/SOURCE_AUDIT.md",
    "PRODUCT_MASTER.md": "work/PRODUCT_MASTER.md",
    "PRODUCT_PRD.md": "work/PRODUCT_PRD.md",
    "CLAIMS_MATRIX.md": "work/CLAIMS_MATRIX.md",
    "ASSET_INDEX.md": "work/ASSET_INDEX.md",
    "LAUNCH_READINESS.md": "work/LAUNCH_READINESS.md",
    "CHANGELOG.md": "work/CHANGELOG.md",
    "product_master.template.json": "work/product_master.json",
    "downstream_handoff.template.json": "work/downstream_handoff.json",
}

def main():
    ap = argparse.ArgumentParser(description="Initialize a product-master project.")
    ap.add_argument("project_dir")
    args = ap.parse_args()

    project = Path(args.project_dir).resolve()
    project.mkdir(parents=True, exist_ok=True)

    for rel in DIRS:
        (project / rel).mkdir(parents=True, exist_ok=True)

    for src_name, dest_rel in COPY.items():
        src = TEMPLATES / src_name
        dest = project / dest_rel
        if not dest.exists():
            shutil.copy2(src, dest)

    print(f"Initialized product-master project at: {project}")

if __name__ == "__main__":
    main()
