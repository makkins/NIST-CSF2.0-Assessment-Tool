# -*- coding: utf-8 -*-
"""Builds the CSF Information Gathering HTML (spec v2.0, schema csf-ig/4).
Merges the Interview Assessment and the document review part of the Document Audit Tracker into one tool.
Data: site_data.json (from build_data.py) when present, otherwise the data embedded in 00_Master/Document-Audit-Tracker.html.
Sources: question bank, framing, technical checks, sessions, profiles, rubric, environment and department profiles, plus packs.py (industry packs and mandate tags) and screening.py (Category screening questions).
Usage: python build_ig.py [path/to/Document-Audit-Tracker.html] [output.html]"""
import json, os, sys
from iq_dersrc import Q
from iq_frame import F
from tc import TC, DOMAINS
from sessions import SESSIONS, SYSCTL, PRINCIPLES
from build_html import SKEL
from viewmode import apply_viewmode
from sysprofile import PROFILE, VENDOR, DEV_ORIGINS
from rubric import RUBRIC, RUBRIC_VERSION, COVERAGE
from envprofile import ENV_FIELDS, ENV_TABLES
from deptprofile import DEPT_FIELDS
from packs import PACKS, MANDATES, VERIFY_LOG
from screening import SCREEN
from techev import TECHEV
from comms import COMMS
from prompts import PROMPTS, RULES

SCHEMA = "csf-ig/4"
APP_VERSION = "2.0.0"


def load_data(tracker):
    """Register, meta, and Thai text: site_data.json when present, otherwise the DATA block of the Audit Tracker."""
    if os.path.exists("site_data.json"):
        return json.load(open("site_data.json", encoding="utf-8"))
    s = open(tracker, encoding="utf-8").read()
    i = s.index("const DATA = ") + len("const DATA = ")
    j = s.index(";\nconst D=DATA.docs", i)
    return json.loads(s[i:j].replace("<\\/", "</"))
DOC_KEYS = ["id", "en", "th", "fn", "cat", "level", "pkg", "trigger", "type", "owner_k", "approver_k", "review", "review_th",
            "csf", "purpose", "ctrl", "content", "seq", "wave", "cap"]

def main():
    tracker = sys.argv[1] if len(sys.argv) > 1 else "../00_Master/Document-Audit-Tracker.html"
    out = sys.argv[2] if len(sys.argv) > 2 else "../00_Master/Information-Gathering.html"
    d = load_data(tracker)
    m = d["meta"]
    assert set(Q) == set(m["subcats"]) == set(F), "question bank and framing must cover every Subcategory"
    q = {k: dict(v, **F[k]) for k, v in Q.items()}
    assert all(s in m["subcats"] for c in TC for s in c["s"])
    assert set(RUBRIC) == set(m["categories"]), "rubric must cover every Category"
    assert all(s in m["subcats"] for s in COVERAGE)
    assert all(s in m["subcats"] for f in PROFILE + VENDOR for s in f["s"])
    assert {f["samp"] for f in PROFILE if f["samp"]} == {c["k"] for c in SYSCTL}
    assert all(s in m["subcats"] for f in ENV_FIELDS for s in f["s"])
    assert all(s in m["subcats"] for f in DEPT_FIELDS for s in f["s"])
    roles = dict(m["roles"], DEPT=["Department head and key users", "หัวหน้าแผนกและผู้ใช้งานหลัก"])
    assert all(r in roles for z in SESSIONS for r in z["r"])
    seq = [x for z in SESSIONS for x in z["subs"]]
    assert sorted(seq) == sorted(m["subcats"]), "every Subcategory must sit in exactly one session"
    tcids = {c["id"] for c in TC}
    assert all(c in tcids for e in TECHEV for c in e["tcs"]), "technical evidence must link to known checks"
    assert all(e["r"] in roles for e in TECHEV), "technical evidence owner must be a known role"
    import re
    ctx = set("client assessor ref scope cutoff reqDue saDue schedule requestSummary session sessionDate sessionTime sessionLoc attendees objective duration prepare facts newRequests openByOwner openCount landscape".split())
    for c in COMMS:
        used = set(re.findall(r"\{\{(\w+)\}\}", "".join(c["subj"] + c["body"])))
        assert used <= ctx, (c["id"], used - ctx)
    assert all(p["id"] for p in PROMPTS) and len(PROMPTS) == 5
    assert len({p["id"] for p in PACKS}) == len(PACKS) and PACKS[0]["id"] == "gen"
    assert set(SCREEN) == set(m["categories"]), "one screening question per Category"
    pk = {p["id"]: p for p in PACKS}
    assert all(t["pack"] in pk for t in TC if "pack" in t), "pack checks must name a pack"
    assert all(s in m["subcats"] for p in PACKS for s in p["probes"]), "pack probes must use valid Subcategories"
    assert all(s in m["subcats"] for x in MANDATES for s in x["s"]), "mandate tags must use valid Subcategories"
    for x in MANDATES:
        a, *b = x["src"].split(":")
        assert (a == "flag" and b[0] in ("cii", "pdpa", "cca", "iso")) or (a == "pack" and b[0] in pk) or \
               (a == "opt" and b[0] in pk and b[1] in {o["k"] for o in pk[b[0]]["opts"]}), x["id"]
    docs = [{k: x[k] for k in DOC_KEYS} for x in d["docs"]]
    assert all(s in m["subcats"] for x in docs for s in x["csf"]), "Register CSF mapping must use valid Subcategories"
    data = dict(meta=dict(functions=m["functions"], categories=m["categories"], subcats=m["subcats"], subcats_th=m["subcats_th"],
                          roles=roles, caps=m["caps"], waves=m["waves"]),
                adocs=docs, q=q, tc=TC, domains={k: dict(n=v[0], r=v[1].split()) for k, v in DOMAINS.items()},
                sessions=SESSIONS, sysctl=SYSCTL, principles=PRINCIPLES,
                profile=PROFILE, vendor=VENDOR, devOrigins=DEV_ORIGINS, rubric=RUBRIC, rubricVersion=RUBRIC_VERSION, coverage=COVERAGE,
                schema=SCHEMA, appVersion=APP_VERSION, envFields=ENV_FIELDS, envTables=ENV_TABLES, deptFields=DEPT_FIELDS, packs=PACKS,
                screen=SCREEN, mandates=MANDATES, verifyLog=VERIFY_LOG,
                techev=TECHEV, comms=COMMS, prompts=PROMPTS, promptRules=RULES)
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = open("ig_template.html", encoding="utf-8").read()
    assert "__DATA__" in tpl
    body = tpl.replace("__DATA__", js)
    open("artifact_ig.html", "w", encoding="utf-8").write(body)
    open(out, "w", encoding="utf-8").write(apply_viewmode(SKEL.replace("{body}", body), ["score", "dash"]))
    print("information gathering", len(body), "->", out)

if __name__ == "__main__":
    main()
