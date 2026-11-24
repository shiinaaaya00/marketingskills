#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib

CATEGORIES = [
    "brand", "specs", "product-images", "packaging", "bom-cost",
    "sku-inventory", "listings", "copy-marketing", "compliance",
    "research", "notes"
]

def sha8(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()[:8]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project_dir")
    args = ap.parse_args()
    root = Path(args.project_dir).resolve()

    rows = []
    i = 1
    for cat in CATEGORIES:
        base = root / "inputs" / cat
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if p.is_file():
                rows.append([
                    f"SRC-{i:03d}",
                    str(p.relative_to(root)),
                    cat,
                    p.suffix.lower().lstrip(".") or "file",
                    "",
                    "",
                    "YES",
                    "",
                    f"sha256:{sha8(p)}; {p.stat().st_size} bytes"
                ])
                i += 1

    out = root / "work" / "SOURCE_INVENTORY.md"
    lines = [
        "# SOURCE INVENTORY",
        "",
        "| Source ID | File / Link | Category | Type | Date / Revision | Authority | Current? | Supports | Notes |",
        "|---|---|---|---|---|---|---|---|---|"
    ]
    for r in rows:
        lines.append("| " + " | ".join(str(x).replace("|", "\\|") for x in r) + " |")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Inventoried {len(rows)} source(s) -> {out}")

if __name__ == "__main__":
    main()
