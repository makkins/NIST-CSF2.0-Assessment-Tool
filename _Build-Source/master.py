# -*- coding: utf-8 -*-
"""Build 00_Master: register/traceability xlsx, data.json for HTML, Tailoring Guide and Framework Summary (EN, TH)."""
import os, re, json, glob
from collections import Counter, defaultdict
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from docx import Document
from docx.shared import Pt, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

from subcats_th import SUBCATS_TH
from meta import DOCS, DOC, SUBCATS, CATEGORIES, FUNCTIONS, TYPES, TIERS, PPT, ROLES, LEVEL_TH, TRIGGER_TH, cmc_level
from build import (load_content, slug, folder_for, pkg_of, ESSENTIAL, th_basis, R, heading, para, table, bullet, kv_table, box, add_page_number, OUT)

MASTER = os.path.join(OUT, "00_Master")
os.makedirs(MASTER, exist_ok=True)
C = load_content()

def relpath(d, setname):
    fn = d["fn"]; order = ["GV", "ID", "PR", "DE", "RS", "RC"].index(fn) + 1
    return f"{setname}/{order:02d}_{fn}_{FUNCTIONS[fn][0]}/{d['cat']}_{slug(CATEGORIES[d['cat']][0])}/{d['id']}_{slug(d['en'])}.docx"

# VERIFY scan
verify = defaultdict(int)
for d in DOCS:
    s = json.dumps(C[d["id"]], ensure_ascii=False) + d["basis"]
    n = s.count("[VERIFY")
    if n: verify[d["id"]] = n

# ------------------------------------------------------------ XLSX
from enrich import ENRICH, ORDER, WAVES, TRACKS, CAPS, REASONS, SOURCING, THEMES, TAGS, FLOWS
from enrich_activities import ACTIVITIES

def build_xlsx():
    wb = Workbook()
    F = Font(name="Arial", size=10); FB = Font(name="Arial", size=10, bold=True); FH = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    HF = PatternFill("solid", fgColor="1F3864"); thin = Side(style="thin", color="BFBFBF"); BD = Border(left=thin, right=thin, top=thin, bottom=thin)
    WR = Alignment(wrap_text=True, vertical="top")
    def sheet(ws, headers, rows, widths):
        ws.append(headers)
        for c in ws[1]:
            c.font = FH; c.fill = HF; c.alignment = WR; c.border = BD
        for r in rows:
            ws.append(r)
        for row in ws.iter_rows(min_row=2):
            for c in row:
                c.font = F; c.alignment = WR; c.border = BD
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
        ws.freeze_panes = "B2"
        ws.auto_filter.ref = ws.dimensions

    ws = wb.active; ws.title = "README"
    lines = [("NIST CSF 2.0 Document Framework: Document Register and Traceability", FB),
             ("Purpose: one list of every controlled document, its classification, ownership, and mapping to NIST CSF 2.0, ISO/IEC 27001:2022, NIST SP 800-53 Rev. 5, and Thai law.", F),
             ("Sheets: Summary (counts by formula), Document Register (one row per document), Implementation Roadmap (recommended build order), Prerequisite Activities (meetings and workshops with agendas), Process Flows (operating chains), CSF Traceability (one row per CSF 2.0 subcategory), Hierarchy (parent to child links), Verify List (items to confirm with current Thai regulations).", F),
             ("ISO 27002 Theme: the theme of the first ISO/IEC 27001:2022 Annex A control mapped to the document (A.5 Organizational, A.6 People, A.7 Physical, A.8 Technological); documents mapped only to management system clauses count as Organizational. NIST does not publish a theme grouping.", F),
             ("Build Order, Wave, Track: practitioner guidance for an organization starting from scratch. Track A builds governance in overlapping waves (W0 Mandate to W5 Optimize). Track B runs threat-driven quick wins in parallel from day one.", F),
             ("Capability: IT-ready = in-house IT can produce it from the template; Specialist-guided = IT drafts, a cybersecurity specialist facilitates or reviews; Specialist-required = needs a security FTE, consultant, or managed service.", F),
             ("Level: Required = mandated by law or a certifiable standard when the Trigger applies; Expected = auditors, regulators, or customers expect it; Optional = adds value at higher maturity.", F),
             ("Trigger: All, PDPA, ISO 27001 (certification), CII (Critical Information Infrastructure), CCA (service provider under the Computer Crime Act B.E. 2550 s.26).", F),
             ("Package (cumulative): Essential = the smallest self-contained starter set every organization should have; Core = the rest of the full baseline, built on Essential (every Core document sits under an Essential document); Extended = higher maturity or specific contexts. Level answers whether a document is mandated; Package answers how much to adopt for the organization's size. A Required document applies whenever its trigger applies, whatever its package.", F),
             ("Edit cells in the Document Register to track your own status; the Summary sheet recalculates.", F),
             ("References as of October 2026. Items marked [VERIFY] must be confirmed against current Thai regulations before use. This pack is a sample and is not legal advice.", F)]
    for i, (t, f) in enumerate(lines, 1):
        ws.cell(row=i, column=1, value=t).font = f
        ws.cell(row=i, column=1).alignment = Alignment(wrap_text=True, vertical="top")
    ws.column_dimensions["A"].width = 140

    # Document Register
    reg = wb.create_sheet("Document Register")
    hdr = ["Document ID", "Title (EN)", "Title (TH)", "Function", "Category", "Tier", "Type", "ISO 27002 Theme", "Package", "Level", "Trigger", "Basis",
           "Level for CMC", "CSF 2.0 Subcategories", "ISO/IEC 27001:2022", "NIST SP 800-53 Rev. 5", "Owner (role)", "Approver (role)", "Review Cycle",
           "Parent Documents", "Child Documents", "Tags", "Build Order", "Wave", "Track", "Capability", "Sourcing Options", "Prerequisite Activities",
           "Depends On", "File (Template EN)", "Status (your organization)"]
    E = ENRICH
    rows = []
    for d in DOCS:
        rows.append([d["id"], d["en"], d["th"], f"{FUNCTIONS[d['fn']][0]} ({d['fn']})", f"{CATEGORIES[d['cat']][0]} ({d['cat']})", d["tier"], TYPES[d["type"]][0],
                     E[d["id"]]["theme"], pkg_of(d), d["level"], ", ".join(d["trigger"]), d["basis"], cmc_level(d), ", ".join(d["csf"]),
                     ", ".join(d["iso"]), ", ".join(d["nist"]), ROLES[d["owner"]][0], ROLES[d["approver"]][0], d["review"],
                     ", ".join(d["parents"]), ", ".join(d["children"]), ", ".join(TAGS[t][0] for t in E[d["id"]]["tags"]), E[d["id"]]["seq"],
                     f'{E[d["id"]]["wave"]} {WAVES[E[d["id"]]["wave"]][0]}', TRACKS[E[d["id"]]["track"]][0].split(":")[0], CAPS[E[d["id"]]["cap"]][0],
                     " / ".join(SOURCING[x][0] for x in E[d["id"]]["src"]), "; ".join(f'{a} {ACTIVITIES[a]["en"]}' for a in E[d["id"]]["acts"]),
                     ", ".join(E[d["id"]]["deps"]), relpath(d, "02_Template_EN"), "Not started"])
    sheet(reg, hdr, rows, [12, 38, 38, 14, 30, 6, 11, 14, 10, 10, 16, 45, 22, 30, 22, 22, 26, 26, 16, 22, 30, 30, 8, 22, 9, 18, 36, 50, 24, 60, 16])
    from openpyxl.worksheet.datavalidation import DataValidation
    dv = DataValidation(type="list", formula1='"Not started,Drafting,In review,Approved,Not applicable"', allow_blank=True)
    SC = get_column_letter(len(hdr))
    reg.add_data_validation(dv); dv.add(f"{SC}2:{SC}{len(DOCS)+1}")
    n = len(DOCS) + 1

    # Implementation roadmap
    rm = wb.create_sheet("Implementation Roadmap")
    rows = []
    for did in ORDER:
        d, e = DOC[did], ENRICH[did]
        w = WAVES[e["wave"]]
        rows.append([e["seq"], e["wave"], w[0], w[2], TRACKS[e["track"]][0], did, d["en"], d["level"], CAPS[e["cap"]][0],
                     " ".join(REASONS[x][0] for x in e["reasons"]), " / ".join(SOURCING[x][0] for x in e["src"]),
                     "; ".join(f'{a} {ACTIVITIES[a]["en"]}' for a in e["acts"]), ", ".join(e["deps"]), ", ".join(e["unlocks"]),
                     ", ".join(e["align"]), (e["note"] or ("", ""))[0]])
    sheet(rm, ["Build Order", "Wave", "Wave Name", "Timing", "Track", "Document ID", "Title", "Level", "Capability", "Why", "Sourcing Options",
               "Prerequisite Activities", "Depends On", "Unlocks", "Interim: Align Later To", "Advice"], rows,
          [7, 6, 18, 16, 30, 12, 40, 10, 18, 45, 34, 50, 24, 24, 18, 50])

    # Activities
    ac = wb.create_sheet("Prerequisite Activities")
    rows = []
    for k, a in ACTIVITIES.items():
        outs = [d["id"] for d in DOCS if k in ENRICH[d["id"]]["acts"]]
        rows.append([k, a["en"], a["th"], a["purpose"][0], "\n".join(f"{i+1}. {x}" for i, x in enumerate(a["agenda"][0])),
                     ", ".join(ROLES[r][0] for r in a["roles"]), a["inputs"][0], a["duration"][0], a["freq"][0], CAPS[a["cap"]][0], a["first"][0], ", ".join(outs)])
    sheet(ac, ["Activity ID", "Activity (EN)", "Activity (TH)", "Purpose", "Agenda", "Participants", "Inputs", "Duration", "Frequency",
               "Facilitator Capability", "First Time in This Organization", "Feeds Documents"], rows,
          [9, 34, 34, 45, 60, 40, 30, 22, 20, 18, 55, 40])

    # Process flows
    pf = wb.create_sheet("Process Flows")
    rows = []
    for f in FLOWS:
        for i, st in enumerate(f[5], 1):
            rows.append([f[1], i, st[1], st[0], DOC[st[0]]["en"], f[3]])
    sheet(pf, ["Process Flow", "Step", "Step Label", "Document ID", "Title", "Flow Description"], rows, [32, 6, 24, 12, 45, 60])

    # CSF traceability
    tr = wb.create_sheet("CSF Traceability")
    rows = []
    for sc, desc in SUBCATS.items():
        ds = [d for d in DOCS if sc in d["csf"]]
        cat = sc.split("-")[0]
        by_tier = defaultdict(list)
        for d in ds: by_tier[d["tier"]].append(d["id"])
        rows.append([sc, FUNCTIONS[sc[:2]][0], CATEGORIES[cat][0], desc, SUBCATS_TH[sc], len(ds), ", ".join(by_tier["T0"] + by_tier["T1"]), ", ".join(by_tier["T2"]), ", ".join(by_tier["T3"]), ", ".join(by_tier["T4"])])
    sheet(tr, ["Subcategory", "Function", "Category", "Outcome (paraphrased)", "Outcome (TH, unofficial)", "Document Count", "T0 and T1 (Direction)", "T2 (Standards)", "T3 (Procedures and Plans)", "T4 (Evidence)"], rows, [12, 11, 30, 55, 55, 10, 26, 26, 30, 30])

    # Hierarchy edges
    hi = wb.create_sheet("Hierarchy")
    rows = []
    for d in DOCS:
        for p in d["parents"]:
            rows.append([p, DOC[p]["en"], DOC[p]["tier"], d["id"], d["en"], d["tier"]])
    sheet(hi, ["Parent ID", "Parent Title", "Parent Tier", "Child ID", "Child Title", "Child Tier"], rows, [12, 45, 8, 12, 45, 8])

    # Verify list
    vl = wb.create_sheet("Verify List")
    rows = [[k, DOC[k]["en"], v, DOC[k]["basis"]] for k, v in sorted(verify.items())]
    sheet(vl, ["Document ID", "Title", "Items Marked [VERIFY]", "Basis"], rows, [12, 45, 12, 80])

    # Summary with formulas
    sm = wb.create_sheet("Summary", 1)
    sm["A1"] = "Summary (formulas reference the Document Register sheet)"; sm["A1"].font = FB
    r0 = 3
    def block(title, col_letter, values, start):
        sm.cell(row=start, column=1, value=title).font = FB
        sm.cell(row=start, column=2, value="Count").font = FB
        for i, v in enumerate(values, 1):
            sm.cell(row=start + i, column=1, value=v).font = F
            sm.cell(row=start + i, column=2, value=f"=COUNTIF('Document Register'!${col_letter}$2:${col_letter}${n},\"{v}*\")").font = F
        sm.cell(row=start + len(values) + 1, column=1, value="Total").font = FB
        sm.cell(row=start + len(values) + 1, column=2, value=f"=SUM(B{start+1}:B{start+len(values)})").font = FB
        return start + len(values) + 3
    r = block("By Function", "D", [FUNCTIONS[f][0] for f in ["GV", "ID", "PR", "DE", "RS", "RC"]], r0)
    r = block("By Tier", "F", ["T0", "T1", "T2", "T3", "T4"], r)
    r = block("By ISO/IEC 27002 Theme", "H", list(THEMES), r)
    r = block("By Wave (recommended build order)", "X", [f"{k} {v[0]}" for k, v in WAVES.items()], r)
    r = block("By Capability", "Z", [v[0] for v in CAPS.values()], r)
    r = block("By Package", "I", ["Essential", "Core", "Extended"], r)
    r = block("By Level", "J", ["Required", "Expected", "Optional"], r)
    r = block("By Status (your organization)", SC, ["Not started", "Drafting", "In review", "Approved", "Not applicable"], r)
    sm.cell(row=r, column=1, value="CSF 2.0 subcategories covered").font = FB
    sm.cell(row=r, column=2, value=f"=COUNTIF('CSF Traceability'!$F$2:$F${len(SUBCATS)+1},\">0\")").font = FB
    sm.cell(row=r + 1, column=1, value="CSF 2.0 subcategories in total").font = F
    sm.cell(row=r + 1, column=2, value=f"=COUNTA('CSF Traceability'!$A$2:$A${len(SUBCATS)+1})").font = F
    sm.column_dimensions["A"].width = 40; sm.column_dimensions["B"].width = 12
    p = os.path.join(MASTER, "Document-Register-and-CSF-Traceability.xlsx")
    wb.save(p)
    return p

# ------------------------------------------------------------ data.json for HTML
def build_json():
    data = []
    for d in DOCS:
        c = C[d["id"]]
        data.append(dict(id=d["id"], en=d["en"], th=d["th"], fn=d["fn"], cat=d["cat"], tier=d["tier"], type=d["type"], ppt=d["ppt"], pkg=pkg_of(d),
                         level=d["level"], trigger=d["trigger"], basis=d["basis"], basis_th=th_basis(d["basis"]), cmc=cmc_level(d), csf=d["csf"], iso=d["iso"], nist=d["nist"],
                         owner=[ROLES[d["owner"]][0], ROLES[d["owner"]][1]], approver=[ROLES[d["approver"]][0], ROLES[d["approver"]][1]], review=d["review"],
                         parents=d["parents"], children=d["children"], purpose=[c["purpose"][0], c["purpose"][1]], verify=verify.get(d["id"], 0),
                         path=relpath(d, "02_Template_EN")))
    meta = dict(functions={k: list(v) for k, v in FUNCTIONS.items()}, categories={k: list(v) for k, v in CATEGORIES.items()}, subcats=SUBCATS,
                types={k: list(v) for k, v in TYPES.items()}, tiers={k: list(v) for k, v in TIERS.items()}, ppt=PPT)
    p = "html_data.json"
    json.dump(dict(docs=data, meta=meta), open(p, "w", encoding="utf-8"), ensure_ascii=False)
    return p

# ------------------------------------------------------------ guide docx helpers
def new_doc(lang, title, subtitle):
    r = R(lang)
    doc = Document()
    sec = doc.sections[0]
    sec.page_height, sec.page_width = Cm(29.7), Cm(21.0)
    sec.left_margin = sec.right_margin = Cm(2.2)
    st = doc.styles["Normal"]; st.font.name = r.font; st.font.size = Pt(r.size)
    rpr = st.element.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rpr.insert(0, rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"): rf.set(qn(a), r.font)
    add_page_number(sec.footer.paragraphs[0], r, ("Page " if lang == "EN" else "หน้า "))
    heading(doc, title, 0, r)
    para(doc, subtitle, r, size=r.small)
    return doc, r

def tree_lines(root, lang, depth=0, seen=None):
    seen = seen or set()
    out = []
    d = DOC[root]
    name = d["th"] if lang == "TH" else d["en"]
    out.append((depth, f"{d['id']}  {name}  [{d['tier']}, {d['ppt']}]"))
    seen.add(root)
    for ch in d["children"]:
        if ch not in seen:
            out += tree_lines(ch, lang, depth + 1, seen)
    return out

# ------------------------------------------------------------ Framework Summary
def build_summary(lang):
    L = lang == "TH"
    title = "สรุปกรอบเอกสารตาม NIST CSF 2.0" if L else "NIST CSF 2.0 Document Framework Summary"
    sub = ("เอกสารสรุปสิ่งที่จัดทำ ลำดับชั้นเอกสาร การจัดกลุ่มตาม ISO/IEC 27002 themes และลำดับการจัดทำที่แนะนำ | ข้อมูลอ้างอิง ณ ตุลาคม 2569 (2026)" if L
           else "What was built, how the documents cascade, how they group by ISO/IEC 27002 theme, and the recommended build order | References as of October 2026")
    doc, r = new_doc(lang, title, sub)
    tc = Counter(d["tier"] for d in DOCS); fc = Counter(d["fn"] for d in DOCS); pc = Counter(d["ppt"] for d in DOCS)
    lc = Counter(d["level"] for d in DOCS); kc = Counter(pkg_of(d) for d in DOCS)
    heading(doc, "1. ข้อสรุปสำคัญ" if L else "1. Key Message", 1, r)
    if L:
        box(doc, "ข้อสรุป:", f"องค์กรหนึ่งแห่งควรมีเอกสารควบคุม {len(DOCS)} ฉบับใน 5 ชั้น ครอบคลุม 6 Function, 22 Category และ 106 Subcategory ของ NIST CSF 2.0 ครบ 100% แต่ไม่จำเป็นต้องเริ่มพร้อมกันทั้งหมด ชุด Essential {kc['Essential']} ฉบับเพียงพอสำหรับองค์กรขนาดกลางในปีแรก", r)
    else:
        box(doc, "Key message:", f"A complete organization needs {len(DOCS)} controlled documents in five tiers, covering all 6 Functions, 22 Categories, and 106 Subcategories of NIST CSF 2.0 (100%). It does not need all of them at once: the Essential set of {kc['Essential']} documents is enough for a mid-sized organization in year one.", r)
    rows = [["Govern (GV)" if not L else "กำกับดูแล (GV)", fc["GV"]], ["Identify (ID)" if not L else "ระบุ (ID)", fc["ID"]], ["Protect (PR)" if not L else "ป้องกัน (PR)", fc["PR"]],
            ["Detect (DE)" if not L else "ตรวจจับ (DE)", fc["DE"]], ["Respond (RS)" if not L else "ตอบสนอง (RS)", fc["RS"]], ["Recover (RC)" if not L else "กู้คืน (RC)", fc["RC"]], ["Total" if not L else "รวม", len(DOCS)]]
    table(doc, ["Function", "จำนวนเอกสาร" if L else "Documents"], rows, r, widths=[10, 6.5])

    heading(doc, "2. สิ่งที่จัดทำ" if L else "2. What Was Done", 1, r)
    steps = ([("ตรวจสอบแหล่งอ้างอิง", "ยืนยันมาตราของ พ.ร.บ.ไซเบอร์ฯ (มาตรา 44, 46, 52, 54, 56, 57, 58) PDPA และประกาศที่เกี่ยวข้อง และ NIST SP 800-61 Rev. 3 ส่วนที่ยืนยันไม่ได้ติด [VERIFY]"),
              ("ออกแบบรายการเอกสาร", f"กำหนดเอกสาร {len(DOCS)} ฉบับ แบ่งตาม 22 Category พร้อมรหัส ชั้น ประเภท เอกสารแม่และลูก และตรวจด้วย script ว่าครอบคลุม Subcategory ครบ 106 ข้อ"),
              ("จัดประเภทความจำเป็น", "กำหนด Level + Trigger + Basis ให้ทุกฉบับ และคำนวณ Level สำหรับ CMC จากเงื่อนไขของ CMC (PDPA, CII, ผู้ให้บริการตาม พ.ร.บ.คอมพิวเตอร์ฯ)"),
              ("เขียนเนื้อหา", "ทุกฉบับมีส่วน A (ข้อกำหนดขั้นต่ำพร้อมตัวอย่างเนื้อหา) และส่วน B (แนวปฏิบัติที่ดีและข้อผิดพลาดที่พบบ่อย) ความลึกตามชั้นเอกสาร"),
              ("สร้าง 3 ชุด", "สร้างไฟล์ .docx จากข้อมูลชุดเดียว ได้แม่แบบภาษาไทย แม่แบบภาษาอังกฤษ และตัวอย่าง CMC ภาษาอังกฤษ ชุดละ 142 ฉบับ รวม 426 ไฟล์ CMC มีประวัติการแก้ไขจำลอง"),
              ("ตรวจสอบคุณภาพ", "script ตรวจทุกไฟล์: ไม่มี em dash ไม่มีคำต้องห้าม สะกดแบบอเมริกัน การอ้างอิงรหัสเอกสารถูกต้อง ไม่มี placeholder ค้างในชุด CMC และตรวจภาพตัวอย่าง")]
             if L else
             [("Verify references", "Confirmed Cybersecurity Act sections (s.44, 46, 52, 54, 56, 57, 58), PDPA sections and notifications, and NIST SP 800-61 Rev. 3. Items that could not be confirmed carry [VERIFY]."),
              ("Design the document list", f"Defined {len(DOCS)} documents across the 22 Categories with ID, tier, type, parents, and children; a script confirmed all 106 Subcategories are covered."),
              ("Classify necessity", "Assigned Level + Trigger + Basis to every document and resolved the CMC level from CMC's triggers (PDPA, CII, Computer Crime Act service provider)."),
              ("Write content", "Every document has Part A (minimum requirement fields with sample content) and Part B (best practice and common mistakes), with depth set by tier."),
              ("Generate three sets", "Generated .docx files from a single source: Template TH, Template EN, and CMC EN, 142 documents each (426 files). CMC documents carry a simulated revision history."),
              ("Check quality", "A script checked every file for em dashes, banned words, American spelling, valid document references, and leftover placeholders in the CMC set; sample pages were checked visually.")])
    table(doc, ["ขั้นตอน" if L else "Step", "รายละเอียด" if L else "Detail"], [[a, b] for a, b in steps], r, widths=[4.5, 12.0])

    heading(doc, "3. ลำดับชั้นเอกสาร" if L else "3. Document Hierarchy", 1, r)
    rows = [[TIERS[t][1 if L else 0], tc[t], ({"T0": "คณะกรรมการ", "T1": "CEO", "T2": "CIO หลัง ISSC เห็นชอบ", "T3": "CIO", "T4": "เจ้าของกระบวนการ"} if L else
             {"T0": "Board", "T1": "CEO", "T2": "CIO after ISSC endorsement", "T3": "CIO", "T4": "Process owner"})[t]] for t in ["T0", "T1", "T2", "T3", "T4"]]
    table(doc, ["ชั้น" if L else "Tier", "จำนวน" if L else "Count", "ผู้อนุมัติโดยทั่วไป" if L else "Default approver"], rows, r, widths=[8.5, 2.5, 5.5])
    para(doc, ("ข้อยกเว้น เช่น แผนระดับองค์กรที่ CEO อนุมัติ หรือแผนการตรวจสอบที่คณะกรรมการตรวจสอบอนุมัติ ระบุไว้ในตารางอำนาจอนุมัติของ GV-PRC-002 และในทะเบียนเอกสาร" if L else
               "Exceptions, such as organization-wide plans approved by the CEO or the audit program approved by the Audit Committee, are listed in the approval matrix of GV-PRC-002 and in the document register."), r, size=r.small)
    para(doc, ("การถ่ายทอดจากบนลงล่าง (เริ่มจากกฎบัตรการกำกับดูแล GV-CHR-001):" if L else "Top-down cascade, starting from the Cybersecurity Governance Charter (GV-CHR-001):"), r, bold=True)
    for depth, line in tree_lines("GV-CHR-001", lang):
        p = para(doc, ("    " * depth) + ("- " if depth else "") + line, r, size=r.tiny, space_after=0)
    para(doc, "", r)
    others = [d["id"] for d in DOCS if not d["parents"] and d["id"] != "GV-CHR-001"]
    if others:
        para(doc, ("เอกสารที่ไม่มีเอกสารแม่: " if L else "Documents without a parent: ") + ", ".join(others), r, size=r.small)

    heading(doc, "4. การจัดกลุ่มตาม ISO/IEC 27002:2022 themes และ Tag" if L else "4. Classification by ISO/IEC 27002:2022 Theme and Tag", 1, r)
    para(doc, ("กลุ่มหลักใช้ 4 control themes ของ ISO/IEC 27002:2022 โดยดูจาก control ใน Annex A ตัวแรกที่จับคู่กับเอกสาร เอกสารที่จับคู่เฉพาะข้อกำหนดระบบบริหาร (Clause 4 ถึง 10) นับเป็น Organizational ทั้งนี้ NIST ไม่ได้กำหนดการจัดกลุ่มแบบนี้ โดย control class ของ SP 800-53 Rev. 3 (Management, Operational, Technical) ถูกยกเลิกตั้งแต่ Rev. 4" if L else
               "The primary grouping uses the four control themes of ISO/IEC 27002:2022, taken from the first Annex A control mapped to each document. Documents mapped only to management system clauses (Clauses 4 to 10) count as Organizational. NIST does not publish this kind of grouping; the SP 800-53 Rev. 3 control classes (Management, Operational, Technical) were retired in Rev. 4."), r)
    rows = []
    for k, v in THEMES.items():
        ids = [d["id"] for d in DOCS if ENRICH[d["id"]]["theme"] == k]
        rows.append([f"{v[1]} ({k})" if L else k, v[2], len(ids), ", ".join(ids)])
    table(doc, ["Theme", "Annex A", "จำนวน" if L else "Count", "เอกสาร" if L else "Documents"], rows, r, widths=[3.2, 1.6, 1.6, 10.1])
    para(doc, ("Tag รองใช้ดูข้ามหมวด เอกสารหนึ่งฉบับมีได้หลาย Tag" if L else "Secondary tags give cross-cutting views; one document can carry several tags."), r, size=r.small)
    rows = [[f"{v[1]} ({v[0]})" if L else v[0], sum(1 for d in DOCS if k in ENRICH[d["id"]]["tags"])] for k, v in TAGS.items()]
    table(doc, ["Tag", "จำนวน" if L else "Count"], rows, r, widths=[10, 6.5])

    heading(doc, "5. ระดับความจำเป็นและชุดเอกสาร" if L else "5. Necessity Level and Package", 1, r)
    rows = [[LEVEL_TH[k] if L else k, lc[k]] for k in ["Required", "Expected", "Optional"]] + [[("ชุด " if L else "Package: ") + k, kc[k]] for k in ["Essential", "Core", "Extended"]]
    table(doc, ["หมวด" if L else "Group", "จำนวน" if L else "Count"], rows, r, widths=[10, 6.5])
    para(doc, ("หมายเหตุ: Level เป็นเกณฑ์ทั่วไป ส่วน Required ขึ้นกับ Trigger ขององค์กร ดูรายละเอียดในคู่มือการปรับใช้ (Tailoring Guide)" if L else
               "Note: Level is the general rule. Whether a Required document applies depends on the organization's Trigger; see the Tailoring Guide."), r, size=r.small)

    heading(doc, "6. ลำดับการจัดทำและขีดความสามารถที่ต้องใช้" if L else "6. Build Order and Required Capability", 1, r)
    para(doc, ("สำหรับองค์กรที่เริ่มจากศูนย์หรือมีเพียงนโยบาย IT งานเดินเป็น 2 แนวขนานกัน Track A สร้างระบบกำกับดูแลเป็น 6 ระลอกที่ทับซ้อนกันได้ Track B ทำงานเร่งด่วนตามภัยคุกคามตั้งแต่วันแรกในรูปเอกสารชั่วคราว รายละเอียดรายฉบับอยู่ในชีต Implementation Roadmap และมุมมองลำดับที่แนะนำของ Document-Hierarchy.html" if L else
               "For an organization starting from scratch or with IT policies only, the work runs as two parallel tracks. Track A builds governance in six overlapping waves. Track B runs threat-driven quick wins from day one as interim documents. Per-document detail is in the Implementation Roadmap sheet and the Recommended order view of Document-Hierarchy.html."), r)
    rows = []
    for k, v in WAVES.items():
        ds = [d for d in DOCS if ENRICH[d["id"]]["wave"] == k]
        cc = Counter(ENRICH[d["id"]]["cap"] for d in ds)
        rows.append([f"{k} {v[1] if L else v[0]}", v[3] if L else v[2], v[5] if L else v[4], len(ds), f'{cc["IT"]} / {cc["GUIDED"]} / {cc["SPEC"]}'])
    table(doc, ["ระลอก" if L else "Wave", "ช่วงเวลา" if L else "Timing", "เป้าหมาย" if L else "Goal", "จำนวน" if L else "Docs", "IT / G / S"], rows, r, widths=[3.4, 2.6, 6.8, 1.4, 2.3])
    tb = [d["id"] for d in sorted(DOCS, key=lambda x: ENRICH[x["id"]]["seq"]) if ENRICH[d["id"]]["track"] == "B"]
    para(doc, ("Track B (วันที่ 0 ถึง 90): " if L else "Track B (Day 0 to 90): ") + ", ".join(tb), r, size=r.small)
    cc = Counter(e["cap"] for e in ENRICH.values())
    rows = [[CAPS[k][1] if L else CAPS[k][0], cc[k], CAPS[k][3] if L else CAPS[k][2]] for k in ["IT", "GUIDED", "SPEC"]]
    table(doc, ["ขีดความสามารถ" if L else "Capability", "จำนวน" if L else "Count", "ความหมาย" if L else "Meaning"], rows, r, widths=[4.0, 1.8, 10.7])
    box(doc, "ข้อสรุปสำหรับลูกค้า:" if L else "Message for clients:",
        (f"มีเอกสาร {cc['SPEC']} ฉบับที่ทีม IT ทั่วไปจัดทำเองไม่ได้ และอีก {cc['GUIDED']} ฉบับที่ต้องมีผู้เชี่ยวชาญแนะนำ องค์กรที่ไม่มีผู้เชี่ยวชาญด้านไซเบอร์จึงต้องเลือกระหว่างการจ้างพนักงานประจำหรือการใช้ที่ปรึกษาหรือบริการ managed service สำหรับงานส่วนนี้ นอกจากนี้ยังมีกิจกรรมที่ต้องทำก่อน {len(ACTIVITIES)} กิจกรรม เช่น BIA และ Workshop ระดับความเสี่ยงที่ยอมรับได้ ซึ่งต้องจัดจริงก่อนจะเขียนเอกสารได้" if L else
         f"{cc['SPEC']} documents cannot be produced by an IT generalist team, and {cc['GUIDED']} more need specialist guidance. An organization without a cybersecurity specialist must choose between a security hire and a consultant or managed service for this work. The pack also lists {len(ACTIVITIES)} prerequisite activities, such as the BIA and the risk appetite workshop, that must actually take place before the documents can be written."), r)

    heading(doc, "7. รายการที่ต้องตรวจสอบเพิ่มเติม" if L else "7. Items to Verify", 1, r)
    para(doc, (f"มี {len(verify)} ฉบับที่มีรายการ [VERIFY] ซึ่งต้องตรวจสอบกับกฎระเบียบไทยฉบับปัจจุบันก่อนส่งให้ลูกค้า รายการทั้งหมดอยู่ในชีต Verify List ของไฟล์ Excel" if L else
               f"{len(verify)} documents contain [VERIFY] items that must be checked against current Thai regulations before client use. The full list is in the Verify List sheet of the Excel file."), r)
    heading(doc, "8. ไฟล์ในโฟลเดอร์ 00_Master" if L else "8. Files in 00_Master", 1, r)
    files = ([["Document-Register-and-CSF-Traceability.xlsx", "ทะเบียนเอกสาร แผนการจัดทำ กิจกรรมที่ต้องทำก่อน ลำดับกระบวนการ การเชื่อมโยง CSF ลำดับชั้น และรายการ VERIFY"], ["Document-Hierarchy.html", "แผนที่เอกสารแบบโต้ตอบ 7 มุมมอง รวมแผนภาพต้นไม้ ลำดับที่แนะนำ และลำดับกระบวนการ สลับภาษาไทยและอังกฤษได้"], ["Document-Audit-Tracker.html", "เครื่องมือตรวจประเมินเอกสารแบบ offline พร้อมแดชบอร์ดช่องว่างและส่งออก Excel"],
              ["Tailoring-Guide_TH.docx / _EN.docx", "คู่มือการเลือกและปรับใช้เอกสาร"], ["Framework-Summary_TH.docx / _EN.docx", "เอกสารนี้"]] if L else
             [["Document-Register-and-CSF-Traceability.xlsx", "Document register, implementation roadmap, prerequisite activities, process flows, CSF traceability, hierarchy, verify list"], ["Document-Hierarchy.html", "Interactive document map with seven views, including the tree diagram, recommended order, and process flows, with a TH/EN switch"], ["Document-Audit-Tracker.html", "Offline document audit tool with a gap dashboard and Excel export"],
              ["Tailoring-Guide_EN.docx / _TH.docx", "How to select and adapt documents"], ["Framework-Summary_EN.docx / _TH.docx", "This document"]])
    table(doc, ["ไฟล์" if L else "File", "เนื้อหา" if L else "Content"], files, r, widths=[7.5, 9.0])
    p = os.path.join(MASTER, f"Framework-Summary_{lang}.docx"); doc.save(p); return p

# ------------------------------------------------------------ Tailoring Guide
COMBINE = [
 (["GV-CHR-001", "GV-CHR-002"], "One governance charter with the committee terms of reference as an annex.", "รวมเป็นกฎบัตรฉบับเดียว โดยแนบขอบเขตอำนาจหน้าที่ของคณะกรรมการเป็นภาคผนวก"),
 (["PR-POL-001", "PR-STD-001", "PR-STD-002", "PR-STD-003"], "One Access Control Policy and Standard.", "รวมเป็นนโยบายและมาตรฐานการควบคุมการเข้าถึงฉบับเดียว"),
 (["ID-REG-001", "ID-REG-002", "ID-REG-004"], "One asset inventory with sheets for hardware, software, and devices.", "รวมเป็นทะเบียนทรัพย์สินเดียว แยกชีตฮาร์ดแวร์ ซอฟต์แวร์ และอุปกรณ์"),
 (["PR-STD-006", "PR-PRC-005"], "One Backup Standard and Procedure.", "รวมเป็นมาตรฐานและระเบียบปฏิบัติการสำรองข้อมูลฉบับเดียว"),
 (["GV-PRC-006", "GV-REC-001"], "Management review procedure with the minutes template as an annex.", "รวมระเบียบปฏิบัติการทบทวนโดยฝ่ายบริหารกับแม่แบบบันทึกการประชุม"),
 (["RS-PLB-001", "RS-PLB-002", "RS-PLB-003", "RS-PLB-004"], "Playbooks as annexes of the Incident Response Plan (RS-PLN-001).", "รวมคู่มือรับมือเป็นภาคผนวกของแผนรับมือเหตุการณ์ (RS-PLN-001)"),
 (["RC-PLN-003", "RC-PRC-002", "RC-TPL-001"], "One Crisis Management and Communication Plan.", "รวมเป็นแผนบริหารภาวะวิกฤตและการสื่อสารฉบับเดียว"),
 (["GV-STD-002", "GV-TPL-004", "GV-FRM-002"], "One standard contract security schedule with DPA and NDA annexes.", "รวมเป็นภาคผนวกด้านความมั่นคงปลอดภัยในสัญญามาตรฐาน พร้อม DPA และ NDA"),
 (["PR-STD-010", "PR-STD-012", "PR-STD-016"], "One Platform and Network Security Standard for small IT teams.", "รวมเป็นมาตรฐานความมั่นคงปลอดภัยของแพลตฟอร์มและเครือข่ายฉบับเดียวสำหรับทีม IT ขนาดเล็ก"),
 (["ID-PRC-006", "ID-REG-007", "ID-TPL-001"], "One Continual Improvement Procedure with register and lessons template.", "รวมเป็นระเบียบปฏิบัติการปรับปรุงอย่างต่อเนื่อง พร้อมทะเบียนและแม่แบบบทเรียน"),
]

SEQ = {
 "90": ["RS-PLN-001", "RS-PLB-001", "RS-REG-002", "PR-STD-006", "PR-PRC-005", "PR-REC-003", "PR-STD-001", "PR-STD-002", "ID-REG-001", "ID-REG-002", "GV-POL-001", "GV-REG-003"],
 "Y1": ["GV-CHR-001", "GV-STM-001", "GV-POL-002", "GV-PRC-001", "ID-REG-005", "ID-PLN-001", "ID-RPT-002", "GV-POL-004", "GV-REG-007", "GV-TPL-002", "GV-TPL-004", "GV-POL-006", "GV-PRC-008", "GV-REG-009", "PR-PLN-001", "PR-PRC-001", "PR-PRC-002", "PR-PRC-007", "ID-STD-002", "DE-STD-001", "RC-PLN-001", "RC-PLN-002"],
 "Y2": ["GV-PRC-006", "GV-REG-008", "GV-PRC-007", "GV-PLN-002", "ID-PRC-006", "ID-REG-007", "ID-PLN-002", "GV-REG-005", "DE-REG-002", "PR-STD-013", "PR-STD-015", "GV-POL-005", "PR-STD-008"],
}

def ess_combined():
    E = {d["id"] for d in DOCS if pkg_of(d) == "Essential"}
    n = len(E)
    for g, _, _ in COMBINE:
        k = len([x for x in g if x in E])
        if k > 1:
            n -= k - 1
    return n

def build_tailoring(lang):
    L = lang == "TH"
    title = "คู่มือการเลือกและปรับใช้เอกสาร (Tailoring Guide)" if L else "Tailoring Guide"
    sub = ("วิธีเลือกเอกสารที่เหมาะกับขนาดและเงื่อนไขขององค์กร และลำดับการจัดทำ | ข้อมูลอ้างอิง ณ ตุลาคม 2569 (2026)" if L else
           "How to select the documents that fit an organization's size and obligations, and in what order to build them | References as of October 2026")
    doc, r = new_doc(lang, title, sub)
    kc = Counter(pkg_of(d) for d in DOCS)
    heading(doc, "1. ข้อสรุปสำคัญ" if L else "1. Key Message", 1, r)
    box(doc, "ข้อสรุป:" if L else "Key message:",
        ("ไม่ต้องใช้ทั้ง 142 ฉบับ ให้เลือกตาม 3 ขั้น: (1) เลือกชุดตามขนาดองค์กร (2) เพิ่มเอกสารที่บังคับตาม Trigger ขององค์กร (3) รวมเอกสารที่ซ้ำซ้อนเมื่อทีมมีขนาดเล็ก (4) ตรวจว่าเอกสารใดต้องใช้ผู้เชี่ยวชาญ แล้วจัดทำตามระลอกที่แนะนำ โดยทำงานเร่งด่วน (Track B) คู่ขนานตั้งแต่วันแรก" if L else
         "Do not adopt all 142 documents. Select in three steps: (1) pick a package by organization size, (2) add documents made mandatory by the organization's triggers, (3) combine overlapping documents when the team is small, (4) check which documents need a specialist. Then build them in the recommended waves, with threat-driven quick wins (Track B) running in parallel from day one."), r)

    heading(doc, "2. ขั้นที่ 1: เลือกชุดตามขนาดองค์กร" if L else "2. Step 1: Choose a Package by Size", 1, r)
    rows = ([["ขนาดเล็ก (ต่ำกว่า 200 คน ไม่มีทีมความมั่นคงปลอดภัย)", "Essential", f"{kc['Essential']} ฉบับ และเมื่อรวมเอกสารตามหัวข้อ 4 จะเหลือประมาณ {ess_combined()} ฉบับ"],
             ["ขนาดกลาง (200 ถึง 2,000 คน)", "Essential + Core", f"{kc['Essential'] + kc['Core']} ฉบับ ทยอยจัดทำภายใน 2 ปี"],
             ["ขนาดใหญ่หรือมีการกำกับเข้มงวด", "ทุกชุด + ข้อกำหนดเฉพาะภาคส่วน", f"{len(DOCS)} ฉบับ พร้อมเอกสารเพิ่มเติมตามหน่วยงานกำกับ"]] if L else
            [["Small (under 200 staff, no security team)", "Essential", f"{kc['Essential']} documents; about {ess_combined()} after combining (Section 4)"],
             ["Mid-sized (200 to 2,000 staff)", "Essential + Core", f"{kc['Essential'] + kc['Core']} documents, built over two years"],
             ["Large or heavily regulated", "All packages + sector requirements", f"{len(DOCS)} documents plus regulator-specific additions"]])
    table(doc, ["ขนาดองค์กร" if L else "Organization", "ชุดเอกสาร" if L else "Package", "จำนวนโดยประมาณ" if L else "Approximate count"], rows, r, widths=[6.0, 4.5, 6.0])
    para(doc, ("ชุด Essential: " if L else "Essential set: ") + ", ".join(sorted(ESSENTIAL)), r, size=r.tiny)
    para(doc, ("Level, Package และ Wave ตอบคำถามคนละข้อ" if L else "Level, Package, and Wave answer different questions"), r, bold=True, space_after=2)
    rows = ([["Level (ระดับ)", "ต้องมีเอกสารนี้หรือไม่", "กฎหมาย หน่วยงานกำกับ หรือมาตรฐานที่ขอรับรองได้ และองค์กรเข้าเงื่อนไข Trigger หรือไม่"],
             ["Package (ชุด)", "ควรมีมากแค่ไหนตามขนาดองค์กร", "ขนาดและความพร้อมขององค์กร ชุดสะสมต่อกัน: Essential แล้วจึง Core แล้วจึง Extended"],
             ["Wave (ระลอก)", "ควรเขียนเมื่อใด", "ความเชื่อมโยงระหว่างเอกสารและแรงกดดันจากภัยคุกคาม (หัวข้อ 6)"]] if L else
            [["Level", "Must we have this document?", "A law, a regulator, or a certifiable standard, and whether its trigger applies"],
             ["Package", "How much should we adopt for our size?", "Organization size and maturity. Packages are cumulative: Essential, then Core, then Extended"],
             ["Wave", "When should we write it?", "Dependencies between documents and threat pressure (Section 6)"]])
    table(doc, ["มิติ" if L else "Dimension", "คำถามที่ตอบ" if L else "Question it answers", "ตัดสินจาก" if L else "Decided by"], rows, r, widths=[3.0, 5.0, 8.5])
    rules = (["Required และเข้าเงื่อนไข Trigger: ต้องมี ไม่ว่าอยู่ในชุดใด เช่น SoA อยู่ในชุด Extended แต่เป็น Required เมื่อขอรับรอง ISO/IEC 27001",
              "Essential: ต้องมี เริ่มทันที ชุดนี้ใช้งานได้ด้วยตัวเองโดยไม่ต้องพึ่งเอกสาร Core",
              "Core: ควรมีสำหรับองค์กรขนาดกลางขึ้นไป เอกสาร Core ทุกฉบับอยู่ใต้เอกสาร Essential จึงทำ Core โดยไม่มี Essential ไม่ได้",
              "Extended: ทำเมื่อลักษณะองค์กร หน่วยงานกำกับ หรือลูกค้ากำหนดเท่านั้น"] if L else
             ["Required and its trigger applies: must have it, whatever the package. Example: the SoA is Extended but Required for ISO/IEC 27001 certification.",
              "Essential: yes, start now. The set is self-contained and needs no Core document.",
              "Core: yes for mid-sized and larger organizations. Every Core document sits under an Essential document, so Core cannot stand without Essential.",
              "Extended: only when the profile, a regulator, or a customer calls for it."])
    for x in rules:
        bullet(doc, x, r, size=r.small)

    heading(doc, "3. ขั้นที่ 2: เพิ่มเอกสารตาม Trigger" if L else "3. Step 2: Add Documents by Trigger", 1, r)
    para(doc, ("เอกสารต่อไปนี้มี Level เป็น Required เมื่อองค์กรเข้าเงื่อนไข ให้เพิ่มแม้ไม่อยู่ในชุดที่เลือก" if L else
               "These documents become Required when the trigger applies. Add them even if they are outside the chosen package."), r)
    rows = []
    for t, (en, th) in {"PDPA": ("Processes personal data (almost every organization)", "ประมวลผลข้อมูลส่วนบุคคล (เกือบทุกองค์กร)"),
                         "CII": ("Designated Critical Information Infrastructure", "ได้รับการกำหนดเป็นหน่วยงานโครงสร้างพื้นฐานสำคัญทางสารสนเทศ"),
                         "ISO 27001": ("Seeking ISO/IEC 27001 certification", "ต้องการขอรับรอง ISO/IEC 27001"),
                         "CCA": ("Provides internet or computer services to others, such as guest Wi-Fi (confirm with Legal)", "ให้บริการอินเทอร์เน็ตหรือคอมพิวเตอร์แก่ผู้อื่น เช่น Wi-Fi ผู้มาติดต่อ (ยืนยันกับฝ่ายกฎหมาย)")}.items():
        ids = [d["id"] for d in DOCS if d["level"] == "Required" and t in d["trigger"]]
        if not ids and t == "CCA":
            txt = ("ไม่มีเอกสารที่กฎหมายบังคับ แต่ต้องเก็บข้อมูลจราจรทางคอมพิวเตอร์อย่างน้อย 90 วัน (มาตรา 26) ให้ใช้ PR-STD-011 เป็นหลักฐาน" if L else
                   "No document is mandated, but traffic data must be kept for at least 90 days (s.26); use PR-STD-011 as evidence")
        else:
            txt = ", ".join(ids)
        rows.append([TRIGGER_TH.get(t, t) if L else t, th if L else en, txt])
    table(doc, ["Trigger", "เงื่อนไข" if L else "Condition", "เอกสาร Required" if L else "Required documents"], rows, r, widths=[2.8, 6.2, 7.5])

    heading(doc, "4. ขั้นที่ 3: รวมเอกสารเมื่อทีมมีขนาดเล็ก" if L else "4. Step 3: Combine Documents for Small Teams", 1, r)
    para(doc, ("ISO/IEC 27001 กำหนดให้มีข้อมูลที่เป็นเอกสาร ไม่ได้กำหนดจำนวนฉบับ การรวมเอกสารจึงทำได้ หากคงข้อกำหนดในส่วน A ไว้ครบ" if L else
               "ISO/IEC 27001 requires documented information, not a set number of documents. Combining is acceptable when every Part A requirement is kept."), r)
    table(doc, ["เอกสารที่รวมได้" if L else "Documents", "ผลลัพธ์" if L else "Result"], [[", ".join(a), th if L else en] for a, en, th in COMBINE], r, widths=[6.5, 10.0])

    heading(doc, "5. ขั้นที่ 4: ตรวจขีดความสามารถและแหล่งบุคลากร" if L else "5. Step 4: Check Capability and Sourcing", 1, r)
    para(doc, ("ทุกเอกสารมีป้ายขีดความสามารถ นับเอกสาร S ในขอบเขตที่เลือก หากองค์กรไม่มีผู้เชี่ยวชาญด้านไซเบอร์ ให้วางแผนจ้างพนักงานประจำ หรือใช้ที่ปรึกษาหรือบริการ managed service ตั้งแต่ต้น ไม่ใช่หลังจากเอกสารล่าช้าแล้ว" if L else
               "Every document carries a capability flag. Count the S documents in the chosen scope. If the organization has no cybersecurity specialist, plan a security hire or a consultant or managed service from the start, not after the documents stall."), r)
    cc = Counter(ENRICH[d["id"]]["cap"] for d in DOCS)
    rows = [[CAPS[k][1] if L else CAPS[k][0], cc[k], CAPS[k][3] if L else CAPS[k][2]] for k in ["IT", "GUIDED", "SPEC"]]
    table(doc, ["ขีดความสามารถ" if L else "Capability", "จำนวน" if L else "Count", "ความหมาย" if L else "Meaning"], rows, r, widths=[4.0, 1.8, 10.7])
    spec = [d["id"] for d in sorted(DOCS, key=lambda x: ENRICH[x["id"]]["seq"]) if ENRICH[d["id"]]["cap"] == "SPEC"]
    para(doc, ("เอกสารที่ต้องใช้ผู้เชี่ยวชาญ: " if L else "Specialist-required documents: ") + ", ".join(spec), r, size=r.tiny)

    heading(doc, "6. ลำดับการจัดทำ" if L else "6. Build Sequence", 1, r)
    para(doc, ("ระลอกทับซ้อนกันได้ เริ่มระลอกถัดไปเมื่อข้อมูลนำเข้าพร้อม ตัวเลขหน้ารหัสคือลำดับการจัดทำ รหัส A คือกิจกรรมที่ต้องทำก่อน (รายละเอียดในชีต Prerequisite Activities)" if L else
               "Waves overlap; start the next wave when its inputs exist. The number before each ID is the build order. A codes are prerequisite activities (detail in the Prerequisite Activities sheet)."), r, size=r.small)
    for k, v in WAVES.items():
        para(doc, f"{k} {v[1] if L else v[0]} ({v[3] if L else v[2]}): {v[5] if L else v[4]}", r, bold=True, space_after=2)
        hasB = any(ENRICH[d["id"]]["wave"] == k and ENRICH[d["id"]]["track"] == "B" for d in DOCS)
        for tr in ["A", "B"]:
            ds = [d for d in sorted(DOCS, key=lambda x: ENRICH[x["id"]]["seq"]) if ENRICH[d["id"]]["wave"] == k and ENRICH[d["id"]]["track"] == tr]
            if not ds:
                continue
            if hasB:
                para(doc, TRACKS[tr][1] if L else TRACKS[tr][0], r, size=r.small, italic=True, space_after=0)
            for d in ds:
                e = ENRICH[d["id"]]
                acts = (" | " + ", ".join(a.replace("ACT-", "A") for a in e["acts"])) if e["acts"] else ""
                bullet(doc, f"{e['seq']}. {d['id']}  {d['th'] if L else d['en']}  [{CAPS[e['cap']][1 if L else 0]}]{acts}", r, size=r.tiny)
    para(doc, ("หลักการ: ดำเนินงานเป็นหลายแนวขนานกัน ไม่ต้องรอให้นโยบายครบก่อนเริ่มงานด้านการสำรองข้อมูล MFA และความพร้อมรับมือเหตุการณ์" if L else
               "Principle: run parallel tracks. Do not wait for the full policy set before starting backup, MFA, and incident readiness work."), r, size=r.small)

    heading(doc, "7. ขั้นตอนการปรับเอกสารแต่ละฉบับ" if L else "7. Steps to Tailor Each Document", 1, r)
    steps = (["แทนที่ข้อความในวงเล็บเหลี่ยม เช่น [ชื่อองค์กร] และบทบาท", "ปรับค่าที่แนะนำในมาตรฐาน (เช่น กรอบเวลาแก้ไขช่องโหว่) ให้สอดคล้องกับความเสี่ยงและทรัพยากร",
              "ตรวจสอบรายการ [VERIFY] กับกฎระเบียบฉบับปัจจุบันร่วมกับฝ่ายกฎหมาย", "ลบกล่องข้อกำหนดและหมายเหตุวิธีใช้ก่อนประกาศใช้", "อนุมัติตามตารางอำนาจอนุมัติใน GV-PRC-002 และบันทึกในทะเบียนเอกสาร",
              "สื่อสารและอบรมผู้ที่ได้รับผลกระทบ และเก็บหลักฐาน"] if L else
             ["Replace text in square brackets, such as [Organization Name] and role names.", "Adjust recommended values in standards (for example, remediation timelines) to match risk and resources.",
              "Check every [VERIFY] item against current regulations with Legal Counsel.", "Delete the requirement boxes and the how-to note before issue.", "Approve according to the matrix in GV-PRC-002 and record in the document register.",
              "Communicate and train affected staff, and keep evidence."])
    for s in steps:
        bullet(doc, s, r, numbered=True)

    heading(doc, "8. ข้อแตกต่างตามภาคอุตสาหกรรม" if L else "8. Sector Notes", 1, r)
    rows = ([["สาธารณสุข", "มาตรฐาน HA กระทรวงสาธารณสุขในฐานะหน่วยงานกำกับ CII [VERIFY] อุปกรณ์การแพทย์ (ID-REG-004, PR-STD-015) และข้อมูลสุขภาพตาม PDPA มาตรา 26"],
             ["สถาบันการเงิน", "ประกาศธนาคารแห่งประเทศไทยด้านการบริหารความเสี่ยงเทคโนโลยีสารสนเทศ และประกาศ ก.ล.ต. ด้านมาตรฐานระบบ IT [VERIFY ฉบับปัจจุบัน] มักต้องเพิ่มการทดสอบความต่อเนื่องและการรายงานที่เข้มขึ้น"],
             ["อุตสาหกรรมการผลิต", "ความมั่นคงปลอดภัยของ OT ตาม IEC 62443 และ NIST SP 800-82 Rev. 3 การแยกเครือข่าย IT และ OT และความปลอดภัยในการปฏิบัติงาน"]] if L else
            [["Healthcare", "Hospital Accreditation (HA), the Ministry of Public Health as CII regulator [VERIFY], medical devices (ID-REG-004, PR-STD-015), and health data under PDPA s.26."],
             ["Financial services", "Bank of Thailand IT risk management notifications and SEC IT system standards [VERIFY current versions]; usually stricter continuity testing and reporting."],
             ["Manufacturing", "OT security under IEC 62443 and NIST SP 800-82 Rev. 3, IT and OT network separation, and operational safety."]])
    table(doc, ["ภาคส่วน" if L else "Sector", "ประเด็นเพิ่มเติม" if L else "Additional considerations"], rows, r, widths=[3.5, 13.0])
    heading(doc, "9. ข้อจำกัดความรับผิดชอบ" if L else "9. Disclaimer", 1, r)
    para(doc, ("เอกสารชุดนี้เป็นตัวอย่างเพื่อการเรียนรู้และการให้คำปรึกษา ไม่ใช่คำปรึกษาทางกฎหมาย ต้องปรับให้เหมาะกับองค์กรและตรวจสอบกฎระเบียบฉบับปัจจุบันก่อนใช้งาน เนื้อหาไม่ได้คัดลอกข้อความจากมาตรฐาน ISO และอ้างอิงเฉพาะเลขข้อ ส่วน CMC เป็นองค์กรสมมติ" if L else
               "This pack is a sample for learning and advisory use and is not legal advice. Tailor it to the organization and confirm current regulations before use. It cites ISO clause numbers only and does not reproduce ISO text. CMC is a fictional organization."), r)
    p = os.path.join(MASTER, f"Tailoring-Guide_{lang}.docx"); doc.save(p); return p

if __name__ == "__main__":
    print(build_xlsx()); print(build_json())
    for lg in ("EN", "TH"):
        print(build_summary(lg)); print(build_tailoring(lg))
    print("verify docs:", len(verify))
