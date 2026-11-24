#!/usr/bin/env python3
from pathlib import Path
import argparse, json

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def index(data):
    return {f["fact_id"]: f for f in data.get("facts", []) if f.get("fact_id")}

def main():
    ap = argparse.ArgumentParser(description="Compare two product master JSON versions.")
    ap.add_argument("old")
    ap.add_argument("new")
    args = ap.parse_args()

    a = index(load(args.old))
    b = index(load(args.new))

    print("# PRODUCT MASTER VERSION DIFF\n")
    print("## Added")
    for k in sorted(set(b) - set(a)):
        print("-", k)

    print("\n## Removed")
    for k in sorted(set(a) - set(b)):
        print("-", k)

    print("\n## Changed")
    for k in sorted(set(a) & set(b)):
        fields = ["value", "unit", "status", "scope", "source_refs"]
        diffs = {f:(a[k].get(f), b[k].get(f)) for f in fields if a[k].get(f) != b[k].get(f)}
        if diffs:
            print("-", k)
            for f,(x,y) in diffs.items():
                print(f"  - {f}: {x!r} -> {y!r}")

if __name__ == "__main__":
    main()
