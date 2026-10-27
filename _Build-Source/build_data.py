# -*- coding: utf-8 -*-
"""Builds site_data.json: documents + enrichment + audit checklists + catalogs, shared by the Document Map and Audit Tracker."""
import json
from meta import DOCS, ROLES, FUNCTIONS, CATEGORIES, SUBCATS, TYPES, TIERS, cmc_level
import build
from build import load_content, transform, AUTO_REQ, L, pkg_of, th_basis
from enrich import ENRICH, ORDER, WAVES, TRACKS, CAPS, REASONS, SOURCING, THEMES, TAGS, FLOWS
from enrich_activities import ACTIVITIES

C = load_content()
OUT = "site_data.json"

def T2(en, th):
    return [transform(en, "EN", "tpl"), transform(th, "TH", "tpl")]

CTRL = [
 ("ctl-owner", "Owner is assigned and named: {owner}", "มีการกำหนดเจ้าของเอกสาร: {owner}"),
 ("ctl-approve", "Approved by the designated approver ({approver}), with evidence of approval", "ได้รับอนุมัติจากผู้อนุมัติที่กำหนด ({approver}) และมีหลักฐานการอนุมัติ"),
 ("ctl-version", "Document ID, version, effective date, and revision history are recorded", "มีรหัสเอกสาร เวอร์ชัน วันที่มีผล และประวัติการแก้ไข"),
 ("ctl-review", "Reviewed within the defined cycle ({review})", "ได้รับการทบทวนตามรอบที่กำหนด ({review})"),
]
CTRL_COMM = ("ctl-comm", "Published and communicated to the intended audience, with acknowledgment where required", "เผยแพร่และสื่อสารถึงกลุ่มเป้าหมาย และมีการรับทราบเมื่อจำเป็น")
CTRL_REC = ("ctl-rec", "Entries are complete, current, and retained according to the retention rules", "รายการครบถ้วน เป็นปัจจุบัน และเก็บรักษาตามหลักเกณฑ์การเก็บรักษา")
def review_th(rv):
    rv2 = {"Annual": "ทุกปี", "Quarterly": "ทุกไตรมาส", "Semi-annual": "ทุก 6 เดือน", "Continuous": "ต่อเนื่อง", "Each meeting": "ทุกครั้งที่ประชุม",
           "Each test": "ทุกครั้งที่ทดสอบ", "Each exercise": "ทุกครั้งที่ฝึกซ้อม", "Each review cycle": "ทุกรอบการทบทวน"}.get(rv, rv)
    for a, b in [("Continuous; reconcile quarterly", "ต่อเนื่อง และกระทบยอดทุกไตรมาส"), ("Continuous; review monthly", "ต่อเนื่อง และทบทวนทุกเดือน"),
                 ("Continuous; report monthly", "ต่อเนื่อง และรายงานทุกเดือน"), ("Annual and on legal change", "ทุกปี และเมื่อกฎหมายเปลี่ยนแปลง"),
                 ("Annual and on major change", "ทุกปี และเมื่อมีการเปลี่ยนแปลงสำคัญ"), ("Annual and on change", "ทุกปี และเมื่อมีการเปลี่ยนแปลง"),
                 ("Annual and after each test", "ทุกปี และหลังการทดสอบทุกครั้ง")]:
        rv2 = rv2.replace(a, b)
    return rv2

def checks_for(d):
    c = C[d["id"]]
    own, apr = ROLES[d["owner"]], ROLES[d["approver"]]
    rv = d["review"]
    fmt = lambda s, li: s.format(owner=own[li], approver=apr[li], review=(review_th(rv) if li else rv))
    ctrl = [dict(id=k, g="ctl", t=[fmt(en, 0), fmt(th, 1)]) for k, en, th in CTRL]
    k, en, th = CTRL_REC if d["tier"] == "T4" else CTRL_COMM
    ctrl.append(dict(id=k, g="ctl", t=[en, th]))
    content = []
    lbE, lbT = L["EN"], L["TH"]
    content.append(dict(id="c-purpose", g="content", t=[lbE["purpose"], lbT["purpose"]], r=list(AUTO_REQ["purpose"])))
    content.append(dict(id="c-scope", g="content", t=[lbE["scope"], lbT["scope"]], r=list(AUTO_REQ["scope"])))
    for i, s in enumerate(c.get("sections", [])):
        content.append(dict(id=f"c-s{i+1}", g="content", t=T2(s[0], s[1]), r=T2(s[2], s[3])))
    if c.get("fields") and d["type"] in ("FRM", "REG", "REC"):
        for i, f in enumerate(c["fields"]):
            content.append(dict(id=f"c-f{i+1}", g="field", t=T2(f[0], f[1]), r=T2(f[2], f[3])))
        if d["type"] == "FRM":
            content.append(dict(id="c-approval", g="content", t=[lbE["approval"], lbT["approval"]], r=list(AUTO_REQ["approval"])))
        if d["type"] == "REG":
            content.append(dict(id="c-changelog", g="content", t=[lbE["changelog"], lbT["changelog"]], r=list(AUTO_REQ["changelog"])))
    if d["type"] in ("POL", "STD"):
        content.append(dict(id="c-compliance", g="content", t=[lbE["compliance"], lbT["compliance"]], r=list(AUTO_REQ["compliance"])))
    if d["type"] in ("PRC", "PLN", "PLB"):
        content.append(dict(id="c-records", g="content", t=[lbE["records"], lbT["records"]], r=list(AUTO_REQ["records"])))
    return ctrl, content

def main():
    import master
    verify = master.verify if hasattr(master, "verify") else {}
    docs = []
    for d in DOCS:
        c = C[d["id"]]
        e = ENRICH[d["id"]]
        ctrl, content = checks_for(d)
        docs.append(dict(
            id=d["id"], en=d["en"], th=d["th"], fn=d["fn"], cat=d["cat"], tier=d["tier"], type=d["type"], ppt=d["ppt"], pkg=pkg_of(d),
            level=d["level"], trigger=d["trigger"], basis=d["basis"], basis_th=th_basis(d["basis"]), cmc=cmc_level(d), csf=d["csf"], iso=d["iso"], nist=d["nist"],
            owner_k=d["owner"], approver_k=d["approver"], review=d["review"], review_th=review_th(d["review"]), parents=d["parents"], children=d["children"],
            purpose=[transform(c["purpose"][0], "EN", "tpl"), transform(c["purpose"][1], "TH", "tpl")],
            mistakes=[T2(m[0], m[1]) for m in c.get("mistakes", [])],
            path=master.relpath(d, "02_Template_EN"), verify=verify.get(d["id"], 0),
            ctrl=ctrl, content=content, **e))
    roles = {k: [v[0], v[1]] for k, v in ROLES.items()}
    acts = {}
    for k, a in ACTIVITIES.items():
        acts[k] = dict(en=a["en"], th=a["th"], purpose=list(a["purpose"]), agenda=[a["agenda"][0], a["agenda"][1]], roles=a["roles"],
                       inputs=list(a["inputs"]), duration=list(a["duration"]), cap=a["cap"], freq=list(a["freq"]), first=list(a["first"]),
                       outputs=[d["id"] for d in DOCS if k in ENRICH[d["id"]]["acts"]])
    meta = dict(functions={k: list(v) for k, v in FUNCTIONS.items()}, categories={k: list(v) for k, v in CATEGORIES.items()}, subcats=SUBCATS, subcats_th=__import__('subcats_th').SUBCATS_TH,
                types={k: list(v) for k, v in TYPES.items()}, tiers={k: list(v) for k, v in TIERS.items()},
                waves={k: list(v) for k, v in WAVES.items()}, tracks={k: list(v) for k, v in TRACKS.items()}, caps={k: list(v) for k, v in CAPS.items()},
                reasons={k: list(v) for k, v in REASONS.items()}, sourcing={k: list(v) for k, v in SOURCING.items()},
                themes={k: list(v) for k, v in THEMES.items()}, tags={k: list(v) for k, v in TAGS.items()}, roles=roles,
                flows=[dict(id=f[0], en=f[1], th=f[2], d_en=f[3], d_th=f[4], steps=[list(s) for s in f[5]]) for f in FLOWS],
                order=ORDER)
    json.dump(dict(docs=docs, meta=meta, acts=acts), open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    print("wrote", OUT, len(docs), sum(len(x["content"]) for x in docs), "content checks")

if __name__ == "__main__":
    main()
