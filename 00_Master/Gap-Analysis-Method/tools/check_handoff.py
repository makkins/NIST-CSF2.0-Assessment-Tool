# -*- coding: utf-8 -*-
"""Validate an Information Gathering P1 handoff file (csf-p1-handoff/1) before Gap Analysis uses it.
Usage: python check_handoff.py <handoff.json> [more files]
Checks the JSON Schema, then the rules in Information Gathering Spec v2.0 Section 13.1:
106 unique Subcategories, all rated or N/A; every Documented or Demonstrated rating cites an Evidence ID
that exists in the Evidence Register and is not after the cut-off; Landscape locked; Landscape evidence IDs exist;
22 Categories; no Target value anywhere. Exit code 1 when any file fails."""
import json, re, sys, pathlib
from jsonschema import Draft202012Validator

SCHEMA = pathlib.Path(__file__).resolve().parent.parent / "schemas" / "csf-p1-handoff-1.schema.json"
REC = re.compile(r"^(TOOL|HIST|CHG|PRIOR|SITE|OBS)-\d+$")


def keys(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield path + k, k
            yield from keys(v, path + k + ".")
    elif isinstance(o, list):
        for v in o:
            yield from keys(v, path)


def check(doc):
    errs = [f"schema: {'/'.join(map(str, e.path))}: {e.message[:160]}" for e in Draft202012Validator(json.load(open(SCHEMA, encoding="utf-8"))).iter_errors(doc)]
    if errs:
        return errs
    subs = doc["subcategories"]
    ids = [s["id"] for s in subs]
    if len(set(ids)) != 106:
        errs.append(f"Subcategory IDs are not unique: {len(set(ids))} distinct")
    ev = {e["id"]: e for e in doc["evidence"]}
    for s in subs:
        if s["statedTier"] == "" or s["countedTier"] is None:
            errs.append(f"{s['id']}: not rated")
        if s["evidenceLevel"] in ("D", "O") and s["statedTier"] != "NA":
            good = [i for i in s["evidenceIds"] if i in ev and not ev[i]["afterCutoff"]]
            if not good:
                errs.append(f"{s['id']}: {s['evidenceLevel']} rating without a current Evidence ID")
        for i in s["evidenceIds"]:
            if i not in ev:
                errs.append(f"{s['id']}: Evidence ID {i} is not in the Evidence Register")
    if len({c["id"] for c in doc["categories"]}) != 22:
        errs.append("Categories are not 22 distinct IDs")
    for f in doc["landscape"]["facts"]:
        for i in f["evidence"]:
            if i not in ev and not REC.match(i):
                errs.append(f"{f['id']}: unknown evidence or record ID {i}")
    bad = sorted({p for p, k in keys(doc) if k.lower() in ("tgt", "target", "targettier")})
    if bad:
        errs.append("Target values present: " + ", ".join(bad[:5]))
    return errs


def main():
    files = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not files:
        print(__doc__)
        sys.exit(2)
    fail = 0
    for f in files:
        doc = json.load(open(f, encoding="utf-8"))
        errs = check(doc)
        rated = sum(1 for s in doc.get("subcategories", []) if s.get("statedTier"))
        print(("PASS " if not errs else "FAIL ") + f"{pathlib.Path(f).name}  [{doc.get('engagement', {}).get('scale', '?')} {doc.get('engagement', {}).get('industry', '?')}, {rated} rated, {len(doc.get('evidence', []))} evidence]")
        for e in errs[:15]:
            print("    " + e)
        fail += bool(errs)
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
