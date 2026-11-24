#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import argparse, json, sys

def compact(f):
    return {
        "fact_id": f.get("fact_id"),
        "name": f.get("name"),
        "value": f.get("value"),
        "unit": f.get("unit"),
        "scope": f.get("scope"),
        "status": f.get("status"),
        "source_refs": f.get("source_refs", []),
        "notes": f.get("notes", "")
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project_dir")
    args = ap.parse_args()
    root = Path(args.project_dir).resolve()

    path = root / "work/product_master.json"
    if not path.exists():
        sys.exit("Missing work/product_master.json")

    data = json.loads(path.read_text(encoding="utf-8"))
    doc = data.get("document", {})
    facts = data.get("facts", [])

    conflicts = [compact(f) for f in facts if f.get("status") == "CONFLICT"]
    open_questions = data.get("open_questions", [])
    blockers = conflicts + [{"question": q} for q in open_questions]

    identity = {
        f.get("fact_id"): f.get("value")
        for f in facts
        if f.get("category") == "IDENTITY"
        and f.get("status") in {"LOCKED","DERIVED"}
    }

    allowed = {"LOCKED","DERIVED"}
    handoff = {
        "schema_version": "1.0",
        "product_master_version": doc.get("master_version", ""),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "READY_FOR_DOWNSTREAM"
            if not blockers and doc.get("status") in {"MASTER_COMPLETE","PRD_COMPLETE","READY_FOR_DOWNSTREAM"}
            else "BLOCKED",
        "identity": identity,
        "variants": [compact(f) for f in facts if f.get("category")=="VARIANT" and f.get("status") in allowed],
        "skus": [compact(f) for f in facts if f.get("category")=="SKU" and f.get("status") in allowed],
        "pricing": [compact(f) for f in facts if f.get("category")=="PRICE" and f.get("status") in allowed],
        "dimensions": [compact(f) for f in facts if f.get("category")=="DIMENSION" and f.get("status") in allowed],
        "physical_identity": [
            compact(f) for f in facts
            if f.get("category") in {"MATERIAL","FINISH","COLOR","CONTROL","LIGHT","OUTPUT"}
            and f.get("status") in {"LOCKED","VISUAL_ONLY","DERIVED"}
        ],
        "verified_features": [
            compact(f) for f in facts
            if f.get("category") in {"PERFORMANCE","TIMER","NOISE","CAPACITY","COMPATIBILITY","POWER","BATTERY","CARE"}
            and f.get("status") in allowed
        ],
        "included_items": [compact(f) for f in facts if f.get("category")=="INCLUDED_ITEM" and f.get("status") in allowed],
        "approved_claims": [],
        "prohibited_claims": [],
        "approved_assets": [],
        "prd_decisions": [],
        "open_issues": blockers,
        "source_audit_status": doc.get("source_audit_status", ""),
        "downstream_notes": {
            "claims_and_assets": "Populate approved/prohibited claims and approved assets from reviewed matrices.",
            "preferred_consumers": [
                "product-video","product-images","PDP","SEO/GEO",
                "EDM","Ads","Affiliate","Influencer","Marketplace"
            ]
        }
    }

    out = root / "work/downstream_handoff.json"
    out.write_text(json.dumps(handoff, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote: {out}")
    print(f"Status: {handoff['status']}")

if __name__ == "__main__":
    main()
