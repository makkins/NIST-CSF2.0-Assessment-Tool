# -*- coding: utf-8 -*-
"""Data Dictionary (plan W1-1). The only place that defines enums, ID formats, field names, and EN/TH labels.
Every build script imports from here. `python dictionary.py` writes dictionary.json (copied into the method pack
tools folder) so the HTML tools, validate.py, and check_enums.py read the same values.
Rule: a renamed or removed value needs a new schema ID (method pack Section 9)."""
import json, pathlib, re

# ---- Register labels (moved unchanged from meta.py, enrich.py, build.py) ----
TYPES = {
 # code: (EN, TH, tier)
 "CHR": ("Charter", "กฎบัตร", "T0"),
 "STR": ("Strategy", "ยุทธศาสตร์", "T0"),
 "STM": ("Statement", "แถลงการณ์", "T0"),
 "POL": ("Policy", "นโยบาย", "T1"),
 "STD": ("Standard", "มาตรฐาน", "T2"),
 "PRC": ("Procedure", "ระเบียบปฏิบัติ", "T3"),
 "PLN": ("Plan", "แผน", "T3"),
 "PLB": ("Playbook", "คู่มือรับมือ (Playbook)", "T3"),
 "GDL": ("Guideline", "แนวทาง", "T3"),
 "FRM": ("Form", "แบบฟอร์ม", "T4"),
 "REG": ("Register", "ทะเบียน", "T4"),
 "REC": ("Record", "บันทึก", "T4"),
 "RPT": ("Report", "รายงาน", "T4"),
 "TPL": ("Template", "แม่แบบ", "T4"),
}

TIERS = {
 "T0": ("Tier 0: Charter, Strategy, and Statement", "ชั้นที่ 0: กฎบัตร ยุทธศาสตร์ และแถลงการณ์"),
 "T1": ("Tier 1: Policy", "ชั้นที่ 1: นโยบาย"),
 "T2": ("Tier 2: Standard", "ชั้นที่ 2: มาตรฐาน"),
 "T3": ("Tier 3: Procedure, Plan, Playbook, and Guideline", "ชั้นที่ 3: ระเบียบปฏิบัติ แผน คู่มือ และแนวทาง"),
 "T4": ("Tier 4: Form, Register, Record, Report, and Template", "ชั้นที่ 4: แบบฟอร์ม ทะเบียน บันทึก รายงาน และแม่แบบ"),
}

PPT = {
 "Governance": "การกำกับดูแล (Governance)", "People": "บุคลากร (People)", "Process": "กระบวนการ (Process)",
 "Technology": "เทคโนโลยี (Technology)", "Physical": "กายภาพ (Physical)",
}

LEVEL_TH = {"Required": "บังคับ (Required)", "Expected": "คาดหวัง (Expected)", "Optional": "ทางเลือก (Optional)"}

TRIGGER_TH = {"All": "ทุกองค์กร", "PDPA": "PDPA", "ISO 27001": "ISO 27001 (กรณีขอรับรอง)", "CII": "CII", "CCA": "ผู้ให้บริการตาม พ.ร.บ.คอมพิวเตอร์ฯ"}

WAVES = {
 "W0": ("Mandate and Mobilize", "มอบอำนาจและเตรียมการ", "Month 0 to 2", "เดือนที่ 0 ถึง 2",
        "Get a sponsor, a structure, and one umbrella policy so later documents have authority.",
        "ได้ผู้สนับสนุน โครงสร้าง และนโยบายหลักหนึ่งฉบับ เพื่อให้เอกสารฉบับต่อไปมีอำนาจรองรับ"),
 "W1": ("Understand", "ทำความเข้าใจองค์กร", "Month 1 to 4", "เดือนที่ 1 ถึง 4",
        "Know what you have, what matters most, and what could go wrong before writing detailed rules.",
        "รู้ว่ามีอะไร อะไรสำคัญที่สุด และอะไรอาจผิดพลาด ก่อนเขียนกฎโดยละเอียด"),
 "W2": ("Direct", "กำหนดทิศทาง", "Month 3 to 7", "เดือนที่ 3 ถึง 7",
        "Set strategy, budget, and the topic policies that the risk picture shows you need.",
        "กำหนดยุทธศาสตร์ งบประมาณ และนโยบายรายเรื่องที่ผลการประเมินความเสี่ยงชี้ว่าจำเป็น"),
 "W3": ("Standardize", "กำหนดมาตรฐานและวิธีปฏิบัติ", "Month 6 to 12", "เดือนที่ 6 ถึง 12",
        "Turn policies into measurable standards and repeatable procedures.",
        "แปลงนโยบายเป็นมาตรฐานที่วัดผลได้และระเบียบปฏิบัติที่ทำซ้ำได้"),
 "W4": ("Operate and Prove", "ปฏิบัติและพิสูจน์ผล", "Month 9 to 18", "เดือนที่ 9 ถึง 18",
        "Run the processes, keep records, and test them through reviews, audits, and exercises.",
        "ดำเนินกระบวนการ เก็บบันทึก และทดสอบผ่านการทบทวน การตรวจสอบ และการฝึกซ้อม"),
 "W5": ("Optimize", "ยกระดับ", "Month 18 onward", "เดือนที่ 18 เป็นต้นไป",
        "Add advanced capabilities once the basics run reliably.",
        "เพิ่มขีดความสามารถขั้นสูงเมื่อพื้นฐานทำงานได้อย่างสม่ำเสมอ"),
}

TRACKS = {
 "A": ("Track A: Governance build", "Track A: สร้างระบบกำกับดูแล",
       "The structured path from mandate to evidence.", "เส้นทางตามลำดับจากการมอบอำนาจไปจนถึงหลักฐาน"),
 "B": ("Track B: Threat-driven quick wins (Day 0 to 90)", "Track B: งานเร่งด่วนตามภัยคุกคาม (วันที่ 0 ถึง 90)",
       "Run in parallel from day one. Issue these as interim documents and align them to their parent policy when it is approved.",
       "ดำเนินคู่ขนานตั้งแต่วันแรก ออกเป็นเอกสารฉบับชั่วคราว แล้วปรับให้สอดคล้องกับนโยบายแม่เมื่อได้รับอนุมัติ"),
}

CAPS = {
 "IT": ("IT-ready", "ทีม IT ทำได้เอง", "In-house IT can produce it from the template with management input.",
        "ทีม IT จัดทำได้จากแม่แบบโดยมีข้อมูลจากผู้บริหาร"),
 "GUIDED": ("Specialist-guided", "ต้องมีผู้เชี่ยวชาญแนะนำ", "IT can draft it, but a cybersecurity specialist must facilitate or review it.",
            "ทีม IT ร่างได้ แต่ต้องมีผู้เชี่ยวชาญด้านไซเบอร์ช่วยดำเนินการหรือทบทวน"),
 "SPEC": ("Specialist-required", "ต้องใช้ผู้เชี่ยวชาญ", "Needs cybersecurity expertise that IT generalists do not have. Hire a full-time employee (FTE) or engage a consultant or managed service.",
          "ต้องใช้ความเชี่ยวชาญด้านไซเบอร์ที่ทีม IT ทั่วไปไม่มี ต้องจ้างพนักงานประจำ (FTE) หรือใช้ที่ปรึกษาหรือบริการแบบ managed service"),
}

PKG_TH = {"Essential": "จำเป็นขั้นต้น (Essential)", "Core": "หลัก (Core)", "Extended": "ขยาย (Extended)"}

# ---- Frozen enums used by the Gap Analysis toolchain ----
STAGES = ["Fix", "Find", "Prevent", "Handle exceptions", "Validate", "Sustain"]
STAGE_KEYS = ["fix", "find", "prevent", "exceptions", "validate", "sustain"]
STAGE_STATUS = ["Required", "In place", "Not applicable", "Beyond Target Tier"]
LEVELS = ["Required", "Expected", "Optional"]
PACKAGES = ["Essential", "Core", "Extended"]
TRIGGERS = ["All", "PDPA", "ISO 27001", "CII", "CCA"]
CSF_FUNCTIONS = ["GV", "ID", "PR", "DE", "RS", "RC"]
TIER_NAMES = ["Partial", "Risk Informed", "Repeatable", "Adaptive"]

# ---- ID formats ----
ID_FORMATS = {
    "document": r"^(GV|ID|PR|DE|RS|RC)-(CHR|STR|STM|POL|STD|PRC|PLN|PLB|GDL|FRM|REG|REC|RPT|TPL)-\d{3}$",
    "category": r"^(GV|ID|PR|DE|RS|RC)\.[A-Z]{2}$",
    "subcategory": r"^(GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}$",
}

# ---- Field names shared across tools (Register core fields) ----
REGISTER_FIELDS = ["title", "th", "hierarchy", "type", "category", "level", "trigger", "package", "wave", "track", "cap"]

def as_dict():
    return dict(
        version="1.0",
        enums=dict(stages=STAGES, stageKeys=STAGE_KEYS, stageStatus=STAGE_STATUS, levels=LEVELS, packages=PACKAGES,
                   triggers=TRIGGERS, functions=CSF_FUNCTIONS, tierNames=TIER_NAMES, types=list(TYPES), hierarchy=list(TIERS),
                   waves=list(WAVES), tracks=list(TRACKS), caps=list(CAPS)),
        idFormats=ID_FORMATS, registerFields=REGISTER_FIELDS,
        labels=dict(type={k: dict(en=v[0], th=v[1], hierarchy=v[2]) for k, v in TYPES.items()},
                    hierarchy={k: dict(en=v[0], th=v[1]) for k, v in TIERS.items()},
                    level=LEVEL_TH, trigger=TRIGGER_TH, ppt=PPT, package=PKG_TH,
                    wave={k: dict(en=v[0], th=v[1]) for k, v in WAVES.items()},
                    track={k: dict(en=v[0], th=v[1]) for k, v in TRACKS.items()},
                    cap={k: dict(en=v[0], th=v[1]) for k, v in CAPS.items()}))

def write(path):
    json.dump(as_dict(), open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return path

if __name__ == "__main__":
    d = pathlib.Path(__file__).resolve().parent
    print(write(d.parent / "00_Master" / "Gap-Analysis-Method" / "tools" / "dictionary.json"))
