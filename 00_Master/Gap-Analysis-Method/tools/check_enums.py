# -*- coding: utf-8 -*-
"""Consistency check for frozen enums (plan W0-4). Fails when the schemas, the Analyst prompt, validate.py,
or the Gap Analysis templates disagree on the four stage status values or the six stage names.
Usage: python check_enums.py [path to _Build-Source]   (default ../../../_Build-Source)
Display-only fallback 'Not assessed' in the HTML is allowed: it labels outputs from before six stages and is never written to data."""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
M = HERE.parent
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else M.parent.parent / "_Build-Source"
DICT = json.load(open(HERE / "dictionary.json", encoding="utf-8"))   # Data Dictionary export (plan W1-1)
STATUS = DICT["enums"]["stageStatus"]
STAGES = DICT["enums"]["stages"]
bad = []

# Register (plan W1-2): every core value must be a Dictionary value and every ID must match its format
REG = json.load(open(HERE / "register-ids.json", encoding="utf-8"))
E = DICT["enums"]
if REG["count"] != len(REG["documents"]):
    bad.append("register-ids.json count does not match the documents")
for did, r in REG["documents"].items():
    if not re.match(DICT["idFormats"]["document"], did):
        bad.append(f"register: bad ID {did}")
    if not re.match(DICT["idFormats"]["category"], r["category"]):
        bad.append(f"register: {did} bad category {r['category']}")
    for key, enum in (("type", "types"), ("hierarchy", "hierarchy"), ("level", "levels"), ("package", "packages"),
                      ("wave", "waves"), ("track", "tracks"), ("cap", "caps")):
        if r.get(key) not in E[enum]:
            bad.append(f"register: {did} {key}={r.get(key)!r} is not in the Dictionary")
    for t in r["trigger"]:
        if t not in E["triggers"]:
            bad.append(f"register: {did} trigger {t!r} is not in the Dictionary")
    if did[:2] not in E["functions"] or did.split("-")[1] != r["type"]:
        bad.append(f"register: {did} ID does not match its function or type")

for n in (4, 5):
    s = json.load(open(M / "schemas" / f"csf-gap-analyst-{n}.schema.json", encoding="utf-8"))
    ss = s["$defs"]["gapFinding"]["properties"]["responses"]["properties"]["stageStatus"]["properties"]
    for k, v in ss.items():
        if v["enum"] != STATUS:
            bad.append(f"schema /{n}: stageStatus.{k} is {v['enum']}")
    key = "stage" if n == 5 else "angle"
    if s["$defs"]["imp"]["properties"][key]["enum"] != STAGES:
        bad.append(f"schema /{n}: IMP {key} enum differs from the six stages")

p = open(M / "prompts" / "01-analyst-prompt.md", encoding="utf-8").read()
tbl = p[p.index("**Status per stage**"):p.index("**Depth follows")]
rows = [r.split("|")[1].strip() for r in tbl.splitlines() if r.startswith("|") and not r.startswith("|---") and "Status" not in r.split("|")[1]]
if rows != STATUS:
    bad.append(f"Analyst prompt status table is {rows}")

v = open(HERE / "validate.py", encoding="utf-8").read()
if "Beyond Target Tier" not in v:
    bad.append("validate.py does not check Beyond Target Tier")
if re.search(r"Not required", v):
    bad.append("validate.py mentions 'Not required'")

for t in ("gap_template.html",):
    h = open(SRC / t, encoding="utf-8").read()
    if "Not required" in h:
        bad.append(f"{t}: contains 'Not required'")
    for m in re.finditer(r'stN:\{(Required.*?)\}', h):
        keys = re.findall(r'"?([A-Za-z ]+)"?:"', m.group(1))
        keys = [k.strip() for k in keys if k.strip() != "Not assessed"]
        if keys != STATUS:
            bad.append(f"{t}: stN keys are {keys}")

print("FAIL" if bad else "PASS", "Dictionary enums (stage status 4, stages 6), Register v2 values, schemas, prompt, validate.py, templates")
for b in bad:
    print(" -", b)
sys.exit(1 if bad else 0)
