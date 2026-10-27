# -*- coding: utf-8 -*-
"""Builds the CSF Interview Assessment HTML.
Data: site_data.json (from build_data.py) when present, otherwise the data embedded in 00_Master/Document-Audit-Tracker.html.
Questions: iq_gv.py, iq_idpr.py, iq_dersrc.py (106 CSF 2.0 Subcategories); scene and scenario: iq_frame.py; technical checks: tc.py; interview sequence and system controls: sessions.py; system and vendor profiles: sysprofile.py; environment profile: envprofile.py; department interviews: deptprofile.py; Tier rubric and coverage list: rubric.py.
Usage: python build_interview.py [path/to/Document-Audit-Tracker.html] [output.html]"""
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

SCHEMA = "csf-interview/3"

def load_data(tracker):
    if os.path.exists("site_data.json"):
        return json.load(open("site_data.json", encoding="utf-8"))
    s = open(tracker, encoding="utf-8").read()
    i = s.index("const DATA = ") + len("const DATA = ")
    j = s.index(";\nconst D=DATA.docs", i)
    return json.loads(s[i:j].replace("<\\/", "</"))

def main():
    tracker = sys.argv[1] if len(sys.argv) > 1 else "../00_Master/Document-Audit-Tracker.html"
    out = sys.argv[2] if len(sys.argv) > 2 else "../00_Master/Interview-Assessment.html"
    d = load_data(tracker)
    m = d["meta"]
    assert set(Q) == set(m["subcats"]) == set(F), "question bank and framing must cover every Subcategory"
    q = {k: dict(v, **F[k]) for k, v in Q.items()}
    assert all(s in m["subcats"] for c in TC for s in c["s"])
    assert set(RUBRIC) == set(m["categories"]), "rubric must cover every Category"
    assert all(s in m["subcats"] for s in COVERAGE), "coverage list must use valid Subcategories"
    assert all(s in m["subcats"] for f in PROFILE + VENDOR for s in f["s"]), "profile feeds must use valid Subcategories"
    assert {f["samp"] for f in PROFILE if f["samp"]} == {c["k"] for c in SYSCTL}, "every sampling control needs a profile field"
    assert all(s in m["subcats"] for f in ENV_FIELDS for s in f["s"]), "environment feeds must use valid Subcategories"
    assert all(s in m["subcats"] for f in DEPT_FIELDS for s in f["s"]), "department feeds must use valid Subcategories"
    roles = dict(m["roles"], DEPT=["Department head and key users", "หัวหน้าแผนกและผู้ใช้งานหลัก"])
    assert all(r in roles for z in SESSIONS for r in z["r"]), "every session role must exist"
    sess_ids = {z["id"] for z in SESSIONS}
    assert all(f["sess"] in sess_ids for f in ENV_FIELDS + ENV_TABLES), "environment items must name a valid session"
    assert len({f["k"] for f in ENV_FIELDS}) == len(ENV_FIELDS) and len({t["prefix"] for t in ENV_TABLES}) == len(ENV_TABLES), "environment keys and prefixes must be unique"
    seq = [x for z in SESSIONS for x in z["subs"]]
    assert sorted(seq) == sorted(m["subcats"]), "every Subcategory must sit in exactly one session"
    data = dict(meta=dict(functions=m["functions"], categories=m["categories"], subcats=m["subcats"], subcats_th=m["subcats_th"], roles=roles),
                docs=[dict(id=x["id"], en=x["en"], th=x["th"], csf=x["csf"], level=x["level"]) for x in d["docs"]], q=q,
                tc=TC, domains={k: dict(n=v[0], r=v[1].split()) for k, v in DOMAINS.items()},
                sessions=SESSIONS, sysctl=SYSCTL, principles=PRINCIPLES,
                profile=PROFILE, vendor=VENDOR, devOrigins=DEV_ORIGINS, rubric=RUBRIC, rubricVersion=RUBRIC_VERSION, coverage=COVERAGE, schema=SCHEMA,
                envFields=ENV_FIELDS, envTables=ENV_TABLES, deptFields=DEPT_FIELDS)
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = open("interview_template.html", encoding="utf-8").read()
    assert "__DATA__" in tpl
    body = tpl.replace("__DATA__", js)
    open("artifact_interview.html", "w", encoding="utf-8").write(body)
    open(out, "w", encoding="utf-8").write(apply_viewmode(SKEL.replace("{body}", body), ["score", "dash"]))
    print("interview", len(body), "->", out)

if __name__ == "__main__":
    main()
