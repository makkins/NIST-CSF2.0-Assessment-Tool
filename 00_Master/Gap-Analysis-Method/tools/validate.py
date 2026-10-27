# -*- coding: utf-8 -*-
"""Validate Gap Analysis JSON against the method pack schemas plus the cross-reference rules
that the Gap Analysis HTML applies on import. Usage:
  python validate.py <file.json> [more files] [--input <input pack or landscape facts>]
The schema is chosen from the "schema" field. Exit code 1 when any file fails.
With --input (csf-gap-input/2 or csf-gap-landscape-facts/1), the Landscape cross-checks also run:
row IDs exist, changes in flight and existing tools are linked, landscape evidence exists, and
(across all Analyst files given) every Landscape block is referenced at least once (warning only)."""
import json, re, sys, pathlib
from jsonschema import Draft202012Validator

HERE = pathlib.Path(__file__).resolve().parent.parent / "schemas"
SCHEMAS = {
    "csf-gap-analyst/1": "csf-gap-analyst-1.schema.json",
    "csf-gap-analyst/2": "csf-gap-analyst-2.schema.json",
    "csf-gap-analyst/3": "csf-gap-analyst-3.schema.json",
    "csf-gap-analyst/4": "csf-gap-analyst-4.schema.json",
    "csf-gap-analyst/5": "csf-gap-analyst-5.schema.json",
    "csf-gap-review/2": "csf-gap-review-2.schema.json",
    "csf-gap-input/2": "csf-gap-input-2.schema.json",
    "csf-gap-landscape/1": "csf-gap-landscape-1.schema.json",
    "csf-gap-landscape-facts/1": "csf-gap-landscape-facts-1.schema.json",
    "csf-gap-review/1": "csf-gap-review-1.schema.json",
    "csf-gap-xreview/1": "csf-gap-xreview-1.schema.json",
    "csf-gap-decisions/1": "csf-gap-decisions-1.schema.json",
    "csf-gap-input/1": "csf-gap-input-1.schema.json",
}
BANNED = re.compile(r"\b(estate|posture|uplift|leverag(e|es|ed|ing)|artifacts?|artefacts?|ideate|operationali[sz]e)\b", re.I)
UK = re.compile(r"\b(organis|prioritis|minimis|optimis|analys(e|es|ed|ing)\b|behaviour|colour|centre|licence)", re.I)

def texts(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from texts(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from texts(v, f"{path}[{i}]")
    elif isinstance(o, str):
        yield path, o

def analyst_rules(d):
    err = []
    fn = d["function"]
    imps = {i["id"]: i for i in d["improvementActions"]}
    gaps = {}
    for c in d["categories"]:
        if not c["categoryId"].startswith(fn + "."):
            err.append(f"{c['categoryId']}: Category is outside Function {fn}")
        for s in c["strengths"]:
            if not s["id"].startswith("STR-" + c["categoryId"] + "-"):
                err.append(f"{s['id']}: Strength ID does not match Category {c['categoryId']}")
        for g in c["gapFindings"]:
            gaps[g["id"]] = g
            if not g["id"].startswith("GAP-" + c["categoryId"] + "-"):
                err.append(f"{g['id']}: Gap ID does not match Category {c['categoryId']}")
            if g["basis"] == "Observed" and g["confidence"] is not None:
                err.append(f"{g['id']}: Observed finding must have confidence null")
            if g["basis"] == "Inferred" and g["confidence"] is None:
                err.append(f"{g['id']}: Inferred finding needs a confidence")
            if g["confidence"] == "Low" and g["likelihood"]["value"] is not None:
                err.append(f"{g['id']}: Low confidence must have no Likelihood")
            if g["likelihood"]["value"] is not None and not g["likelihood"]["anchor"]:
                err.append(f"{g['id']}: Likelihood needs an anchor ID")
            if g["likelihood"]["anchor"] and g["likelihood"]["value"] is not None and int(g["likelihood"]["anchor"][1]) != g["likelihood"]["value"]:
                err.append(f"{g['id']}: anchor {g['likelihood']['anchor']} does not match Likelihood {g['likelihood']['value']}")
            for s in g["linkedSubcategories"]:
                if not s.startswith(c["categoryId"] + "-"):
                    err.append(f"{g['id']}: linked Subcategory {s} is outside the Category")
            if "title" in g:
                err += layer_rules(g)
            r = g["responses"]
            v4 = "stageStatus" in r
            for angle in (STAGES if v4 else STAGES[:4]):
                if v4:
                    st = r["stageStatus"][angle]
                    if st == "Required" and not r[angle]:
                        err.append(f"{g['id']}: stage '{angle}' is Required but has no Improvement Action")
                    if st != "Required" and r[angle]:
                        err.append(f"{g['id']}: stage '{angle}' is {st} but lists Improvement Actions")
                    if st != "Required" and not r["notApplicable"].get(angle):
                        err.append(f"{g['id']}: stage '{angle}' is {st} without a reason")
                    if st == "Beyond Target Tier" and angle != "sustain":
                        err.append(f"{g['id']}: only Sustain can be Beyond Target Tier")
                elif not r[angle] and not r["notApplicable"].get(angle):
                    err.append(f"{g['id']}: stage '{angle}' is empty without a reason")
                for i in r[angle]:
                    if i not in imps:
                        err.append(f"{g['id']}: response {i} is not in improvementActions")
                    elif g["id"] not in imps[i]["linkedGaps"]:
                        err.append(f"{g['id']}: {i} does not list this finding in linkedGaps")
                    elif v4 and imp_stage(imps[i]) != STAGE_ANGLE[angle]:
                        err.append(f"{g['id']}: {i} is listed under '{angle}' but its stage is {imp_stage(imps[i])}")
    for i in imps.values():
        for gid in i["linkedGaps"]:
            if gid not in gaps:
                err.append(f"{i['id']}: linked gap {gid} is not in this output")
        for p in i["prerequisites"]:
            if p not in imps:
                err.append(f"{i['id']}: prerequisite {p} is not in improvementActions")
        if not re.match(r"^[A-Z][a-z]+", i["action"]):
            err.append(f"{i['id']}: action must start with a verb")
    seen = {}
    for i in imps.values():
        k = i["action"].strip().lower()
        if k in seen:
            err.append(f"{i['id']}: duplicates {seen[k]}")
        seen[k] = i["id"]
    if d["round"] == 3 and d["verify"]:
        err.append("round 3 still has open verify items, so the Function cannot lock")
    return err

VERDICT = re.compile(r"\b(weak|poor|strong|good|adequate|inadequate|insufficient|immature|mature|lacks?|lacking|fails?|failed|gaps?|risks?|should|must|recommend\w*|needs?)\b")  # lowercase only: profile labels (Good, Weak, Poor) may appear as counts
ANALYST_V = ("csf-gap-analyst/1", "csf-gap-analyst/2", "csf-gap-analyst/3", "csf-gap-analyst/4", "csf-gap-analyst/5")
V3_UP = ("csf-gap-analyst/3", "csf-gap-analyst/4", "csf-gap-analyst/5")
STAGES = ("fix", "find", "prevent", "exceptions", "validate", "sustain")
def imp_stage(i):
    """IMP stage tag: key stage from csf-gap-analyst/5, key angle in /4 and older outputs (plan W0-3)."""
    return i["stage"] if "stage" in i else i.get("angle")

STAGE_ANGLE = {"fix": "Fix", "find": "Find", "prevent": "Prevent", "exceptions": "Handle exceptions", "validate": "Validate", "sustain": "Sustain"}

def load_register():
    f = pathlib.Path(__file__).resolve().parent / "register-ids.json"
    return json.load(open(f, encoding="utf-8"))["documents"] if f.exists() else None

def v4_rules(d, ctx=None):
    """Six stages, Target Tier depth, and Register documents (csf-gap-analyst/4 and /5)."""
    err = []
    reg = load_register()
    imps = {i["id"]: i for i in d["improvementActions"]}
    tgt, rs = {}, {}
    if ctx is not None and ctx.get("schema") == "csf-gap-input/2":
        for c in ctx["categories"]:
            tgt[c["id"]] = c["targetTier"]
            for s in c["subcategories"]:
                for x in s.get("documents", []):
                    if x.get("requestStatus"):
                        rs[x["id"]] = x["requestStatus"]
    for c in d["categories"]:
        t = tgt.get(c["categoryId"])
        for g in c["gapFindings"]:
            r = g["responses"]
            st = r["stageStatus"]
            if t is not None:
                if t >= 3 and st["sustain"] == "Beyond Target Tier":
                    err.append(f"{g['id']}: Target Tier is {t}, so Sustain is within the Target and cannot be Beyond Target Tier")
                if t < 3 and st["sustain"] == "Required":
                    err.append(f"{g['id']}: Target Tier is {t}, so Sustain is beyond the Target. Use Beyond Target Tier with a reason")
                if t >= 3 and st["validate"] != "Required" and st["validate"] != "In place" and not r["notApplicable"].get("validate"):
                    err.append(f"{g['id']}: Validate needs a reason")
            ids = [x["id"] for x in g["documents"]]
            if len(set(ids)) != len(ids):
                err.append(f"{g['id']}: a document is listed twice")
            for x in g["documents"]:
                if reg is not None and x["id"] not in reg:
                    err.append(f"{g['id']}: {x['id']} is not in the document register")
                q = rs.get(x["id"])
                if q == "Received" and x["status"] == "Missing":
                    err.append(f"{g['id']}: {x['id']} was received but is marked Missing")
                if q == "Does not exist" and x["status"] in ("Exists", "Needs update"):
                    err.append(f"{g['id']}: {x['id']} does not exist but is marked {x['status']}")
    for i in imps.values():
        for gid in i["linkedGaps"]:
            gd = next((g for c in d["categories"] for g in c["gapFindings"] if g["id"] == gid), None)
            if gd is None:
                continue
            have = {x["id"] for x in gd["documents"]}
            for doc in i["documents"]:
                if doc not in have:
                    err.append(f"{i['id']}: document {doc} is not in the documents of {gid}")
    return err

def v3_rules(d):
    err = []
    for c in d["categories"]:
        for g in c["gapFindings"]:
            r = g["repeatFinding"]
            if r["value"] and not r["priorRef"]:
                err.append(f"{g['id']}: repeat finding needs a PRIOR ID")
            if not r["value"] and r["priorRef"]:
                err.append(f"{g['id']}: priorRef set but repeatFinding is false")
    return err

def landscape_of(ctx):
    if ctx is None:
        return None
    return ctx["landscape"] if ctx.get("schema") == "csf-gap-input/2" else ctx

def landscape_ids(L):
    ids = set()
    for b in L["blocks"].values():
        for f in b["facts"]:
            ids.update(f["evidence"])
    for k in ("securityTools", "changesInFlight", "priorAssessments", "incidentHistory", "departmentConflicts"):
        ids.update(r["id"] for r in L.get(k, []))
    return ids

def v3_context_rules(d, L):
    err = []
    tools = {t["id"]: t for t in L["securityTools"]}
    chg = {c["id"]: c for c in L["changesInFlight"]}
    prior = {p["id"] for p in L["priorAssessments"]}
    soon = [c for c in L["changesInFlight"] if c["within12Months"]]
    for c in d["categories"]:
        for g in c["gapFindings"]:
            for b in g["landscapeRefs"]:
                if b not in L["blocks"]:
                    err.append(f"{g['id']}: Landscape block {b} is not in the input")
            if g["repeatFinding"]["priorRef"] and g["repeatFinding"]["priorRef"] not in prior:
                err.append(f"{g['id']}: {g['repeatFinding']['priorRef']} is not in priorAssessments")
    for i in d["improvementActions"]:
        hit = [c["id"] for c in soon if set(c["systems"]) & set(i["systems"])]
        cf = i["changeInFlight"]
        if hit and not cf:
            err.append(f"{i['id']}: names a system in {', '.join(hit)} (within 12 months) but changeInFlight is null")
        if cf and cf["ref"] not in chg:
            err.append(f"{i['id']}: {cf['ref']} is not in changesInFlight")
        t = i["existingTool"]
        if t and t not in tools:
            err.append(f"{i['id']}: {t} is not in securityTools")
        elif t and tools[t]["status"] == "Bought, not deployed" and not i["action"].startswith("Deploy"):
            err.append(f"{i['id']}: {t} is bought but not deployed, so the action must start with Deploy")
    return err

def landscape_rules(d, L):
    err = []
    pages = [p["page"] for p in d["pages"]]
    if sorted(pages) != [1, 2, 3, 4]:
        err.append(f"pages must be 1 to 4 once each, found {pages}")
    blocks = [b["block"] for b in d["blockLines"]]
    for b in set(blocks):
        if blocks.count(b) > 1:
            err.append(f"{b}: more than one block line")
    for p in d["pages"]:
        if words(p["title"]) > 12:
            err.append(f"page {p['page']}: title longer than 12 words")
        if words(p["keyMessage"]) > 35:
            err.append(f"page {p['page']}: key message longer than 35 words")
    for b in d["blockLines"]:
        if words(b["text"]) > 30:
            err.append(f"{b['block']}: block line longer than 30 words")
    for path, t in texts({"pages": d["pages"], "blockLines": d["blockLines"]}):
        if path.endswith(".evidence") or "].evidence[" in path or path.endswith("block"):
            continue
        m = VERDICT.search(t)
        if m:
            err.append(f"{path}: judgment word '{m.group(0)}' in a facts-only section")
    if d["round"] == 2 and d["verify"]:
        err.append("round 2 still has open verify items, so the Landscape cannot lock")
    if L is not None:
        ids = landscape_ids(L)
        for path, item in [(f"page {p['page']}", p) for p in d["pages"]] + [(b["block"], b) for b in d["blockLines"]]:
            for e in item["evidence"]:
                if e not in ids:
                    err.append(f"{path}: evidence {e} is not in the Landscape facts")
        empty = {k for k, b in L["blocks"].items() if not b["facts"]}
        for b in blocks:
            if b in empty:
                err.append(f"{b}: block line written for a block with no facts")
        for b in empty:
            if b not in {v["ref"] for v in d["verify"]} and d["round"] == 1:
                err.append(f"{b}: block has no facts and no verify item")
    return err

def words(t):
    return len(t.split())

def layer_rules(g):
    err = []
    if words(g["title"]) > 12:
        err.append(f"{g['id']}: title longer than 12 words")
    if words(g["statement"]) > 35:
        err.append(f"{g['id']}: statement longer than 35 words")
    if words(g["consequence"]) > 35:
        err.append(f"{g['id']}: consequence longer than 35 words")
    for n, f in enumerate(g["supportingFacts"]):
        if words(f["fact"]) > 25:
            err.append(f"{g['id']}: supporting fact {n + 1} longer than 25 words")
        for e in f["evidence"]:
            if e not in g["evidence"]:
                err.append(f"{g['id']}: supporting fact {n + 1} cites {e}, which is not in the finding evidence")
    return err

def style_rules(d):
    err = []
    for path, t in texts(d):
        if "—" in t or "–" in t:
            err.append(f"{path}: dash character")
        if ";" in t:
            err.append(f"{path}: semicolon")
        if "!" in t:
            err.append(f"{path}: exclamation mark")
        m = BANNED.search(t)
        if m:
            err.append(f"{path}: banned word '{m.group(0)}'")
        m = UK.search(t)
        if m:
            err.append(f"{path}: British spelling '{m.group(0)}'")
    return err

def main(argv):
    files, ctx = [], None
    it = iter(argv)
    for a in it:
        if a == "--input":
            ctx = json.load(open(next(it), encoding="utf-8"))
        else:
            files.append(a)
    L = landscape_of(ctx)
    refs = set()
    bad = 0
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        sid = d.get("schema")
        if sid not in SCHEMAS:
            print(f"FAIL {f}: unknown schema {sid!r}"); bad += 1; continue
        schema = json.load(open(HERE / SCHEMAS[sid], encoding="utf-8"))
        errs = [f"{'/'.join(map(str, e.path))}: {e.message}" for e in Draft202012Validator(schema).iter_errors(d)]
        if not errs:
            if sid in ANALYST_V:
                errs += analyst_rules(d)
            if sid in V3_UP:
                errs += v3_rules(d)
                if sid in ("csf-gap-analyst/4", "csf-gap-analyst/5"):
                    errs += v4_rules(d, ctx)
                if L is not None:
                    errs += v3_context_rules(d, L)
                    refs.update(b for c in d["categories"] for g in c["gapFindings"] for b in g["landscapeRefs"])
            if sid == "csf-gap-landscape/1":
                errs += landscape_rules(d, L)
            if sid not in ("csf-gap-input/1", "csf-gap-input/2", "csf-gap-landscape-facts/1"):
                errs += style_rules(d)
        if errs:
            bad += 1
            print(f"FAIL {f} ({sid})")
            for e in errs[:40]:
                print("  -", e)
        else:
            print(f"PASS {f} ({sid})")
    if L is not None and refs:
        missing = [b for b in L["blocks"] if b not in refs]
        if missing:
            print(f"WARN Landscape blocks not referenced by any Gap Finding in these files: {', '.join(missing)}. "
                  "At Stage 3 each needs a reference or an assessor reason (rule L2)")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main(sys.argv[1:])
