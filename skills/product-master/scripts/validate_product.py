#!/usr/bin/env python3
from pathlib import Path
import argparse, json, sys

REQUIRED_FILES = [
    "work/SOURCE_INVENTORY.md",
    "work/SOURCE_AUDIT.md",
    "work/PRODUCT_MASTER.md",
    "work/PRODUCT_PRD.md",
    "work/CLAIMS_MATRIX.md",
    "work/ASSET_INDEX.md",
    "work/LAUNCH_READINESS.md",
    "work/CHANGELOG.md",
    "work/product_master.json",
]

VALID_FACT_STATUS = {
    "LOCKED", "VISUAL_ONLY", "DERIVED", "UNVERIFIED",
    "CONFLICT", "PROHIBITED", "SUPERSEDED"
}
READY_STATUSES = {"MASTER_COMPLETE", "PRD_COMPLETE", "READY_FOR_DOWNSTREAM"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project_dir")
    args = ap.parse_args()
    root = Path(args.project_dir).resolve()

    errors, warnings = [], []

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            errors.append(f"Missing required file: {rel}")

    master_path = root / "work/product_master.json"
    if master_path.exists():
        try:
            data = json.loads(master_path.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"Invalid JSON: {e}")
            data = None

        if data:
            doc = data.get("document", {})
            if not doc.get("brand"):
                warnings.append("document.brand is empty")
            if not doc.get("product_name"):
                errors.append("document.product_name is empty")
            if not doc.get("master_version"):
                errors.append("document.master_version is empty")

            facts = data.get("facts", [])
            if not facts:
                errors.append("No facts found.")

            ids = set()
            conflict_ids = []

            for idx, fact in enumerate(facts):
                fid = fact.get("fact_id")
                if not fid:
                    errors.append(f"facts[{idx}] missing fact_id")
                    continue
                if fid in ids:
                    errors.append(f"Duplicate fact_id: {fid}")
                ids.add(fid)

                status = fact.get("status")
                if status not in VALID_FACT_STATUS:
                    errors.append(f"{fid}: invalid status {status!r}")

                if status == "LOCKED" and not fact.get("source_refs"):
                    errors.append(f"{fid}: LOCKED fact has no source_refs")

                if status == "DERIVED" and not fact.get("derivation"):
                    errors.append(f"{fid}: DERIVED fact missing derivation")

                if status == "CONFLICT":
                    conflict_ids.append(fid)

            if doc.get("status") in READY_STATUSES and conflict_ids:
                errors.append(
                    "Project marked ready while unresolved CONFLICT facts remain: "
                    + ", ".join(conflict_ids)
                )

            if doc.get("status") == "READY_FOR_DOWNSTREAM":
                if not (root / "work/downstream_handoff.json").exists():
                    errors.append("READY_FOR_DOWNSTREAM but handoff is missing")

    for w in warnings:
        print("WARNING:", w)

    if errors:
        for e in errors:
            print("ERROR:", e)
        sys.exit(1)

    print("Product master validation passed.")

if __name__ == "__main__":
    main()
