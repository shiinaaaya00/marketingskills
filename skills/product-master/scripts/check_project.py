#!/usr/bin/env python3
from pathlib import Path
import argparse

INPUT_DIRS = [
    "inputs/brand","inputs/specs","inputs/product-images","inputs/packaging",
    "inputs/bom-cost","inputs/sku-inventory","inputs/listings",
    "inputs/copy-marketing","inputs/compliance","inputs/research","inputs/notes"
]

WORK_FILES = [
    "work/SOURCE_INVENTORY.md","work/SOURCE_AUDIT.md","work/PRODUCT_MASTER.md",
    "work/product_master.json","work/PRODUCT_PRD.md","work/CLAIMS_MATRIX.md",
    "work/ASSET_INDEX.md","work/LAUNCH_READINESS.md","work/CHANGELOG.md"
]

def count_files(p):
    return sum(1 for x in p.rglob("*") if x.is_file()) if p.exists() else 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project_dir")
    args = ap.parse_args()
    root = Path(args.project_dir).resolve()

    print(f"Project: {root}\n")
    print("Inputs")
    for rel in INPUT_DIRS:
        print(f"- {rel}: {count_files(root/rel)} file(s)")

    print("\nWork files")
    missing = []
    for rel in WORK_FILES:
        ok = (root/rel).exists()
        print(f"- {'OK' if ok else 'MISSING'} {rel}")
        if not ok:
            missing.append(rel)

    if missing:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
