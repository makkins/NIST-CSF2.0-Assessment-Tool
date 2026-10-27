# -*- coding: utf-8 -*-
"""Implementation guidance layer: recommendation order (wave, track), capability flag, sourcing,
prerequisite activities, hard dependencies, ISO/IEC 27002:2022 theme, secondary tags, and process flows."""
from meta import DOCS, DOC
from dictionary import WAVES, TRACKS, CAPS
from enrich_activities import ACTIVITIES

REASONS = {
 "TPL": ("Template-driven: content is mostly factual or administrative.", "ใช้แม่แบบได้: เนื้อหาส่วนใหญ่เป็นข้อเท็จจริงหรืองานธุรการ"),
 "OPS": ("Operational: IT runs it day to day once the parent standard exists.", "งานปฏิบัติการ: ทีม IT ดำเนินการประจำวันได้เมื่อมีมาตรฐานแม่แล้ว"),
 "PEOPLE": ("HR process: HR owns it and security supplies the content.", "กระบวนการ HR: ฝ่าย HR เป็นเจ้าของ และฝ่ายความมั่นคงปลอดภัยให้เนื้อหา"),
 "FACIL": ("Needs neutral facilitation of executive or cross-department decisions.", "ต้องมีผู้ดำเนินการที่เป็นกลางเพื่อนำการตัดสินใจของผู้บริหารหรือข้ามหน่วยงาน"),
 "LAW": ("Needs interpretation of Thai cybersecurity, PDPA, or contract obligations.", "ต้องตีความหน้าที่ตามกฎหมายไซเบอร์ไทย PDPA หรือสัญญา"),
 "METHOD": ("Needs risk methodology design and calibration skills.", "ต้องมีทักษะออกแบบและปรับเทียบวิธีการประเมินความเสี่ยง"),
 "ARCH": ("Needs security architecture judgment to set technical requirements.", "ต้องใช้วิจารณญาณด้านสถาปัตยกรรมความมั่นคงปลอดภัยในการกำหนดข้อกำหนดทางเทคนิค"),
 "IR": ("Needs incident handling and digital forensics experience.", "ต้องมีประสบการณ์รับมือเหตุการณ์และนิติวิทยาศาสตร์ดิจิทัล"),
 "DET": ("Needs detection engineering and security monitoring expertise.", "ต้องมีความเชี่ยวชาญด้านการออกแบบการตรวจจับและการเฝ้าระวัง"),
 "TEST": ("Needs experienced offensive security testers, preferably certified.", "ต้องใช้ผู้ทดสอบเจาะระบบที่มีประสบการณ์ และควรมีใบรับรอง"),
 "AUDIT": ("Needs independent audit competence; the security team cannot audit its own work.", "ต้องมีความสามารถด้านการตรวจสอบที่เป็นอิสระ ทีมความมั่นคงปลอดภัยตรวจสอบงานของตนเองไม่ได้"),
 "BCM": ("Needs business continuity methodology (ISO 22301).", "ต้องใช้วิธีการบริหารความต่อเนื่องทางธุรกิจ (ISO 22301)"),
 "PRIV": ("Needs privacy expertise: PDPA lawful basis, DPIA, data subject rights.", "ต้องมีความเชี่ยวชาญด้านความเป็นส่วนตัว: ฐานทางกฎหมายตาม PDPA, DPIA และสิทธิของเจ้าของข้อมูล"),
 "VENDOR": ("Needs vendor security assessment experience.", "ต้องมีประสบการณ์ประเมินความมั่นคงปลอดภัยของผู้ให้บริการ"),
}
SOURCING = {
 "INH": ("In-house IT", "ทีม IT ภายใน"),
 "FTE": ("Security FTE", "พนักงานประจำด้านความมั่นคงปลอดภัย"),
 "CONS": ("Cybersecurity consultant (project)", "ที่ปรึกษาด้านไซเบอร์ (รายโครงการ)"),
 "MSSP": ("Managed Security Service Provider (MSSP)", "ผู้ให้บริการความมั่นคงปลอดภัยแบบ managed service (MSSP)"),
 "IRR": ("Incident response retainer", "บริการรับมือเหตุการณ์แบบ retainer"),
 "LEGAL": ("Legal counsel", "ที่ปรึกษากฎหมาย"),
 "DPOS": ("DPO or privacy counsel service", "DPO หรือบริการที่ปรึกษาด้านความเป็นส่วนตัว"),
 "IAEXT": ("Co-sourced internal audit", "การตรวจสอบภายในร่วมกับผู้ให้บริการภายนอก"),
 "HR": ("Human Resources", "ฝ่ายทรัพยากรบุคคล"),
}

# id | reasons | sourcing | activities | hard dependencies   (wave, track, cap live in register-ids.json)
GUIDE_TABLE = r"""
GV-CHR-001|FACIL|INH,CONS|ACT-01,ACT-02|-
GV-CHR-002|TPL|INH|ACT-02|GV-CHR-001
GV-REG-003|FACIL|INH,CONS|ACT-02|GV-CHR-002
GV-REG-001|LAW|LEGAL,CONS|ACT-03|-
GV-POL-001|FACIL,LAW|CONS,FTE|ACT-03,ACT-13,ACT-14|GV-CHR-001,GV-REG-001
GV-PRC-002|TPL|INH|ACT-14|GV-POL-001
RS-REG-002|TPL|INH|-|-
RS-PLN-001|IR,LAW|IRR,CONS|ACT-17|RS-REG-002
RS-FRM-001|TPL|INH|-|RS-PLN-001
RS-REG-001|TPL|INH|-|RS-PLN-001
PR-STD-006|TPL|INH|ACT-18|-
PR-PRC-005|OPS|INH|ACT-18|PR-STD-006
PR-REC-003|OPS|INH|ACT-18|PR-PRC-005
PR-STD-001|ARCH|INH,CONS|ACT-19|-
PR-REG-001|OPS|INH|ACT-19|-
GV-RPT-001|FACIL|CONS,FTE|ACT-04|GV-CHR-001,GV-REG-001
GV-REG-002|TPL|INH|ACT-04|GV-RPT-001
ID-STD-001|TPL|INH|ACT-13|GV-POL-001
ID-REG-001|TPL,OPS|INH|ACT-05|-
ID-REG-002|TPL,OPS|INH|ACT-05|-
ID-RPT-001|TPL|INH|ACT-05|ID-REG-001
ID-REG-004|TPL|INH|ACT-05|ID-REG-001
ID-REG-003|PRIV|DPOS,INH|ACT-06|ID-REG-002
GV-POL-004|PRIV,LAW|DPOS,LEGAL|ACT-03,ACT-13,ACT-14|GV-REG-001,GV-POL-001
GV-REG-007|PRIV|DPOS|ACT-06|ID-REG-003
GV-TPL-002|PRIV,LAW|DPOS,LEGAL|ACT-06|GV-REG-007
GV-REG-009|TPL|INH|ACT-16|-
ID-RPT-002|BCM,FACIL|CONS|ACT-07|ID-REG-001,ID-REG-002
GV-STM-001|FACIL,METHOD|CONS|ACT-08|ID-RPT-002,GV-CHR-001
GV-POL-002|METHOD|CONS,FTE|ACT-13,ACT-14|GV-POL-001,GV-STM-001
GV-PRC-001|METHOD|CONS,FTE|ACT-09|GV-POL-002
ID-REG-005|METHOD|CONS,FTE|ACT-10|GV-PRC-001,ID-REG-001,ID-RPT-002
ID-RPT-003|METHOD|CONS,FTE|ACT-10,ACT-11|ID-REG-005
RS-PLB-001|IR|IRR,CONS|ACT-17,ACT-20|RS-PLN-001,PR-PRC-005
PR-STD-002|ARCH|INH,CONS|ACT-19|PR-STD-001
PR-STD-003|ARCH|INH,CONS|ACT-19|PR-STD-001
PR-STD-012|ARCH|INH,MSSP|-|ID-REG-001
GV-STR-001|FACIL|CONS,FTE|ACT-11,ACT-12|ID-RPT-003,GV-RPT-001
GV-PLN-001|FACIL|FTE,INH|ACT-12|GV-STR-001
ID-PLN-001|METHOD|FTE,CONS|ACT-10|ID-REG-005
GV-FRM-001|TPL|INH|-|GV-PRC-001
GV-REG-005|METHOD|CONS,FTE|ACT-11|ID-PLN-001,GV-RPT-001
GV-REG-006|LAW|CONS,LEGAL|ACT-03,ACT-11|GV-REG-001
GV-REG-008|METHOD|FTE,CONS|ACT-12|GV-STR-001
GV-POL-003|TPL|INH,HR|ACT-13,ACT-14|GV-POL-001
PR-POL-001|ARCH|FTE,CONS|ACT-13,ACT-14|GV-POL-001
PR-POL-003|PRIV|FTE,DPOS|ACT-13,ACT-14|GV-POL-001,ID-REG-003
GV-POL-006|VENDOR|FTE,CONS|ACT-13,ACT-14|GV-POL-001,GV-REG-009
RC-POL-001|BCM|CONS,INH|ACT-13,ACT-14|GV-CHR-001,ID-RPT-002
PR-POL-002|TPL|INH|ACT-13,ACT-14|GV-POL-001
GV-STD-001|PEOPLE|HR|ACT-13|GV-POL-001
GV-FRM-002|LAW|LEGAL|-|GV-STD-001
GV-FRM-003|PEOPLE|HR,INH|-|GV-STD-001
PR-PLN-001|TPL|INH,HR|ACT-23|GV-POL-003
GV-PRC-003|TPL|INH|-|GV-POL-001
GV-FRM-004|TPL|INH|-|GV-PRC-003
GV-REG-004|TPL|INH|-|GV-PRC-003
GV-TPL-004|PRIV,LAW|LEGAL,DPOS|-|GV-POL-004
GV-PRC-005|PRIV|DPOS|ACT-13|GV-POL-004
GV-FRM-005|TPL|INH|-|GV-PRC-005
GV-PRC-004|PRIV|DPOS|ACT-13|GV-POL-004
GV-TPL-003|PRIV|DPOS|ACT-27|GV-PRC-004
ID-PRC-001|TPL,OPS|INH|-|ID-STD-001
ID-FRM-001|TPL|INH|-|ID-PRC-001
ID-STD-002|ARCH|FTE,CONS|ACT-26|GV-POL-001
ID-PRC-002|ARCH|FTE,MSSP|ACT-26|ID-STD-002
ID-REG-006|OPS|INH|-|ID-PRC-002
ID-PRC-003|TEST|CONS|ACT-26|ID-STD-002
ID-FRM-002|TEST,LAW|CONS,LEGAL|ACT-26|ID-PRC-003
PR-STD-004|PRIV|FTE,DPOS|ACT-13|PR-POL-003
PR-STD-005|ARCH|FTE,CONS|ACT-13|PR-POL-003
PR-STD-007|PRIV,LAW|DPOS,LEGAL|ACT-13|PR-POL-003
PR-STD-009|ARCH|INH,CONS|ACT-13|GV-POL-003
PR-STD-010|ARCH|INH,CONS|ACT-15|ID-REG-001
PR-PRC-006|TPL,OPS|INH|ACT-28|GV-POL-001
PR-FRM-005|TPL|INH|ACT-28|PR-PRC-006
PR-PRC-007|OPS|INH|-|ID-STD-002
PR-STD-011|ARCH,LAW|FTE,CONS|ACT-22|GV-REG-001
PR-REG-003|TPL,OPS|INH|-|PR-STD-012
PR-STD-013|ARCH|CONS,FTE|ACT-13|GV-POL-001
PR-STD-014|ARCH|CONS,FTE|ACT-15|GV-POL-006
PR-STD-016|ARCH|INH,CONS|ACT-15|ID-RPT-001
PR-PRC-008|OPS|INH|ACT-28|PR-STD-016
PR-FRM-006|TPL|INH|-|PR-PRC-008
PR-STD-017|ARCH,BCM|INH,CONS|-|ID-RPT-002
PR-PRC-001|TPL,OPS|INH|-|PR-POL-001
PR-FRM-001|TPL|INH|-|PR-PRC-001
PR-FRM-002|TPL|INH|-|PR-STD-002
PR-FRM-003|TPL|INH|-|PR-STD-003
PR-PRC-002|OPS|INH|-|PR-POL-001
PR-PRC-003|TPL|INH|-|PR-POL-002
PR-FRM-004|TPL|INH|-|PR-PRC-003
PR-REG-002|PEOPLE|INH,HR|ACT-23|PR-PLN-001
GV-PRC-008|VENDOR|FTE,CONS|ACT-16|GV-POL-006
GV-STD-002|VENDOR,LAW|FTE,LEGAL|ACT-16|GV-POL-006
GV-FRM-006|VENDOR|FTE,CONS|ACT-16|GV-PRC-008
GV-STD-003|ARCH,VENDOR|FTE,CONS|-|GV-POL-006
GV-TPL-005|FACIL|FTE,CONS|-|GV-REG-008
DE-STD-001|DET|CONS,MSSP|ACT-22|PR-STD-011,ID-REG-005
DE-PRC-001|DET|MSSP,FTE|ACT-22|DE-STD-001
DE-REG-001|DET|MSSP,FTE|ACT-22|DE-STD-001
DE-GDL-001|VENDOR,DET|CONS|ACT-22|DE-STD-001
DE-STD-002|IR|CONS,FTE|ACT-17|RS-PLN-001
DE-PRC-002|DET,IR|MSSP,FTE|ACT-22|DE-STD-002,DE-PRC-001
RS-PRC-001|IR|CONS,IRR|ACT-17|RS-PLN-001,DE-STD-002
RS-PLB-002|IR|CONS,IRR|ACT-17|RS-PRC-001
RS-PLB-003|PRIV,IR|DPOS,CONS|ACT-17|RS-PRC-001,GV-POL-004
RS-PLB-004|IR|CONS,IRR|ACT-17|RS-PRC-001
RS-PRC-002|IR|IRR,CONS|ACT-17|RS-PLN-001
RS-FRM-002|IR|IRR,CONS|-|RS-PRC-002
RS-TPL-001|IR|CONS,INH|-|RS-PRC-001
RS-PRC-003|LAW,IR|LEGAL,CONS|ACT-03,ACT-17|RS-PLN-001,GV-REG-001
RS-TPL-002|LAW,PRIV|LEGAL,DPOS|-|RS-PRC-003
RC-PLN-001|BCM|CONS|ACT-07|ID-RPT-002
RC-PLN-002|BCM,ARCH|INH,CONS|ACT-18|RC-PLN-001
RC-PRC-001|OPS|INH|ACT-18|RC-PLN-002
RC-FRM-001|TPL|INH|-|RC-PLN-002
RC-PRC-002|FACIL|INH,CONS|-|RC-PLN-001
RC-TPL-001|TPL|INH|-|RC-PRC-002
PR-REC-001|OPS|INH|ACT-19|PR-PRC-002
PR-REC-002|OPS|HR|ACT-23|PR-PLN-001
GV-PRC-006|FACIL|FTE,CONS|ACT-24|GV-CHR-002
GV-REC-001|TPL|INH|ACT-24|GV-PRC-006
GV-PRC-007|AUDIT|IAEXT|ACT-25|GV-CHR-001
GV-PLN-002|AUDIT|IAEXT|ACT-25|GV-PRC-007
GV-TPL-006|AUDIT|IAEXT|-|GV-PRC-007
ID-PRC-006|TPL|INH|-|GV-POL-001
ID-REG-007|TPL,OPS|INH|-|ID-PRC-006
ID-PLN-002|IR,BCM|CONS,FTE|ACT-20,ACT-21|RS-PLN-001,RC-PLN-001
ID-TPL-001|IR|FTE,CONS|ACT-29|ID-PRC-006
RC-REC-001|BCM|INH,CONS|ACT-21|ID-PLN-002,RC-PLN-002
GV-FRM-007|TPL|INH|-|GV-PRC-008
DE-REG-002|DET|MSSP,FTE|ACT-22|DE-PRC-001
GV-TPL-001|PEOPLE|HR|-|GV-REG-003
GV-POL-005|LAW,ARCH|FTE,CONS|ACT-13,ACT-14|GV-POL-003
PR-PRC-004|TPL|INH,MSSP|ACT-23|PR-PLN-001
PR-STD-008|ARCH,PRIV|CONS|-|PR-STD-004
PR-STD-015|ARCH|CONS|ACT-15|ID-REG-004
ID-PRC-004|DET|MSSP,FTE|-|GV-PRC-001
ID-PRC-005|TEST,LAW|FTE,LEGAL|-|ID-PRC-002
DE-PRC-003|DET|MSSP,FTE|-|DE-REG-002
RC-PLN-003|BCM,FACIL|CONS|ACT-20|RC-PLN-001
"""

# Advice notes for specific documents (EN, TH)
NOTES = {
 "GV-POL-001": ("Issue a short umbrella policy early. Topic policies follow once the risk picture is known.",
                "ออกนโยบายหลักฉบับสั้นตั้งแต่ต้น นโยบายรายเรื่องจะตามมาเมื่อทราบภาพความเสี่ยงแล้ว"),
 "RS-PLN-001": ("Start with a 5 to 10 page interim plan in the first 30 days. Expand it in Wave 3 once severity levels and procedures exist.",
                "เริ่มจากแผนชั่วคราว 5 ถึง 10 หน้าภายใน 30 วันแรก แล้วขยายในระลอกที่ 3 เมื่อมีระดับความรุนแรงและระเบียบปฏิบัติแล้ว"),
 "ID-RPT-002": ("BIA usually runs before the continuity policy is approved. Align it to RC-POL-001 when issued.",
                "BIA มักทำก่อนอนุมัตินโยบายความต่อเนื่อง ให้ปรับให้สอดคล้องกับ RC-POL-001 เมื่อออกแล้ว"),
 "GV-POL-005": ("Move to Wave 2 if staff already use generative AI tools with company data.",
                "เลื่อนมาไว้ระลอกที่ 2 หากพนักงานใช้เครื่องมือ Generative AI กับข้อมูลขององค์กรอยู่แล้ว"),
 "PR-STD-015": ("Move to Wave 3 for hospitals, factories, and utilities where OT or medical devices are on the network.",
                "เลื่อนมาไว้ระลอกที่ 3 สำหรับโรงพยาบาล โรงงาน และสาธารณูปโภคที่มีอุปกรณ์ OT หรืออุปกรณ์การแพทย์ในเครือข่าย"),
 "DE-GDL-001": ("Required in practice if monitoring is outsourced. Prepare it before the MSSP request for proposal.",
                "จำเป็นในทางปฏิบัติหากจ้างบริการเฝ้าระวังภายนอก ให้จัดทำก่อนออกเอกสารเชิญยื่นข้อเสนอ MSSP"),
 "ID-REG-001": ("Do not wait for the asset standard. Build the inventory now and formalize the rules later.",
                "ไม่ต้องรอมาตรฐานทรัพย์สิน ให้จัดทำทะเบียนทันที แล้วค่อยกำหนดกฎอย่างเป็นทางการภายหลัง"),
 "PR-STD-001": ("Multi-factor authentication for remote access, email, and administrators is the first technical control to enforce.",
                "MFA สำหรับการเข้าถึงระยะไกล อีเมล และผู้ดูแลระบบ เป็นมาตรการทางเทคนิคแรกที่ควรบังคับใช้"),
 "GV-REG-005": ("Only needed for ISO/IEC 27001 certification. Otherwise use the CSF Target Profile as the control selection record.",
                "จำเป็นเฉพาะเมื่อขอรับรอง ISO/IEC 27001 หากไม่ขอรับรอง ให้ใช้ CSF Target Profile เป็นบันทึกการเลือกมาตรการ"),
 "GV-PRC-007": ("If internal audit lacks cybersecurity skills, co-source rather than let the security team audit itself.",
                "หากฝ่ายตรวจสอบภายในขาดทักษะด้านไซเบอร์ ให้ใช้บริการร่วมกับภายนอก แทนที่จะให้ทีมความมั่นคงปลอดภัยตรวจสอบตนเอง"),
}

THEMES = {
 "Organizational": ("Organizational", "องค์กร", "A.5"),
 "People": ("People", "บุคลากร", "A.6"),
 "Physical": ("Physical", "กายภาพ", "A.7"),
 "Technological": ("Technological", "เทคโนโลยี", "A.8"),
}
THEME_OVERRIDE = {"PR-STD-001": "Technological", "PR-STD-003": "Technological", "GV-FRM-003": "People", "PR-REG-002": "People"}
THEME_OF = {"5": "Organizational", "6": "People", "7": "Physical", "8": "Technological"}

TAGS = {
 "Governance": ("Governance", "การกำกับดูแล"), "People": ("People", "บุคลากร"), "Process": ("Process", "กระบวนการ"),
 "Technology": ("Technology", "เทคโนโลยี"), "Physical": ("Physical", "กายภาพ"),
 "Legal": ("Legal and Regulatory", "กฎหมายและกฎระเบียบ"), "Privacy": ("Privacy", "ความเป็นส่วนตัว"),
 "ThirdParty": ("Third Party", "บุคคลภายนอก"), "Resilience": ("Resilience", "ความยืดหยุ่น"),
 "Evidence": ("Evidence", "หลักฐาน"), "Cloud": ("Cloud", "คลาวด์"), "AI": ("AI", "AI"), "OT": ("OT and Medical Device", "OT และอุปกรณ์การแพทย์"),
}
EXTRA_TAGS = {
 "PR-STD-014": ["Cloud"], "GV-STD-003": ["Cloud", "ThirdParty"], "GV-POL-005": ["AI"], "ID-REG-004": ["OT"], "PR-STD-015": ["OT"],
 "PR-FRM-003": ["ThirdParty"], "DE-GDL-001": ["ThirdParty"], "GV-TPL-004": ["ThirdParty", "Privacy"], "RS-PLB-003": ["Privacy"],
 "GV-REG-001": ["Legal"], "GV-REG-006": ["Legal"], "RS-PRC-003": ["Legal"], "RS-TPL-002": ["Legal"], "GV-FRM-002": ["Legal"],
 "ID-FRM-002": ["Legal"], "PR-STD-006": ["Resilience"], "PR-PRC-005": ["Resilience"], "PR-REC-003": ["Resilience"],
 "ID-RPT-002": ["Resilience"], "ID-PLN-002": ["Resilience"], "RS-PLB-001": ["Resilience"], "PR-STD-009": ["People"],
}

# Process flows: ordered steps (doc id, step label EN, step label TH)
FLOWS = [
 ("risk", "Risk management cycle", "วงจรการบริหารความเสี่ยง",
  "From appetite to Board reporting: how risk decisions are made and evidenced.", "ตั้งแต่ระดับความเสี่ยงที่ยอมรับได้จนถึงการรายงานคณะกรรมการ: การตัดสินใจเรื่องความเสี่ยงและหลักฐาน",
  [("GV-STM-001","Set appetite","กำหนดระดับที่ยอมรับได้"),("GV-POL-002","Set rules","กำหนดหลักการ"),("GV-PRC-001","Define method","กำหนดวิธีการ"),
   ("ID-REG-005","Record risks","บันทึกความเสี่ยง"),("ID-RPT-003","Report assessment","รายงานผลการประเมิน"),("ID-PLN-001","Plan treatment","วางแผนจัดการ"),
   ("GV-FRM-001","Accept residual risk","ยอมรับความเสี่ยงคงเหลือ"),("GV-REG-008","Measure","วัดผล"),("GV-TPL-005","Report to Board","รายงานคณะกรรมการ")]),
 ("access", "User access lifecycle", "วงจรสิทธิ์การเข้าถึงของผู้ใช้",
  "Request, approve, provision, review, and remove access.", "ขอ อนุมัติ จัดสรร ทบทวน และถอนสิทธิ์",
  [("PR-POL-001","Set rules","กำหนดหลักการ"),("PR-STD-001","Set authentication","กำหนดการยืนยันตัวตน"),("PR-PRC-001","Manage access","บริหารสิทธิ์"),
   ("PR-FRM-001","Request","ยื่นคำขอ"),("PR-PRC-002","Review periodically","ทบทวนตามรอบ"),("PR-REC-001","Record review","บันทึกการทบทวน"),("GV-FRM-003","Remove at exit","ถอนสิทธิ์เมื่อพ้นสภาพ")]),
 ("priv", "Privileged and third-party access", "สิทธิ์ระดับสูงและการเข้าถึงของบุคคลภายนอก",
  "Control the accounts attackers want most.", "ควบคุมบัญชีที่ผู้โจมตีต้องการมากที่สุด",
  [("PR-STD-002","Set PAM rules","กำหนดหลักการ PAM"),("PR-FRM-002","Request privilege","ขอสิทธิ์ระดับสูง"),("PR-REG-001","Register accounts","ขึ้นทะเบียนบัญชี"),
   ("PR-STD-003","Set remote access rules","กำหนดหลักการเข้าถึงระยะไกล"),("PR-FRM-003","Request vendor access","ขอการเข้าถึงของผู้ให้บริการ")]),
 ("vuln", "Vulnerability and patch management", "การบริหารช่องโหว่และแพตช์",
  "Find, prioritize, fix, and verify weaknesses.", "ค้นหา จัดลำดับ แก้ไข และยืนยันจุดอ่อน",
  [("ID-STD-002","Set timelines","กำหนดเวลาแก้ไข"),("ID-PRC-002","Scan and triage","สแกนและคัดกรอง"),("ID-PRC-003","Penetration test","ทดสอบเจาะระบบ"),
   ("ID-FRM-002","Authorize test","อนุญาตการทดสอบ"),("ID-REG-006","Track remediation","ติดตามการแก้ไข"),("PR-PRC-007","Patch","ติดตั้งแพตช์")]),
 ("change", "Change and configuration control", "การควบคุมการเปลี่ยนแปลงและการตั้งค่า",
  "Keep production changes approved, secure, and traceable.", "ให้การเปลี่ยนแปลงระบบได้รับอนุมัติ ปลอดภัย และตรวจสอบย้อนหลังได้",
  [("PR-STD-010","Set baseline","กำหนด Baseline"),("PR-PRC-006","Manage change","บริหารการเปลี่ยนแปลง"),("PR-FRM-005","Request change","ยื่นคำขอเปลี่ยนแปลง"),
   ("PR-PRC-008","Manage firewall rules","บริหารกฎ firewall"),("PR-FRM-006","Request rule","ยื่นคำขอกฎ")]),
 ("incident", "Detect, respond, and learn", "ตรวจจับ ตอบสนอง และเรียนรู้",
  "From the first alert to closure and improvement.", "ตั้งแต่การแจ้งเตือนครั้งแรกจนถึงการปิดเหตุการณ์และการปรับปรุง",
  [("DE-PRC-001","Monitor","เฝ้าระวัง"),("DE-PRC-002","Triage","คัดกรอง"),("DE-STD-002","Classify severity","จัดระดับความรุนแรง"),
   ("RS-FRM-001","Report","รายงาน"),("RS-PRC-001","Handle","จัดการ"),("RS-PLB-001","Apply playbook","ใช้ Playbook"),
   ("RS-PRC-002","Preserve evidence","เก็บรักษาหลักฐาน"),("RS-PRC-003","Notify","แจ้งเหตุ"),("RS-REG-001","Log","บันทึกทะเบียน"),
   ("RS-TPL-001","Investigate","สอบสวน"),("ID-TPL-001","Learn","สรุปบทเรียน"),("ID-REG-007","Track actions","ติดตามการแก้ไข")]),
 ("privacy", "Personal data lifecycle", "วงจรข้อมูลส่วนบุคคล",
  "PDPA duties from mapping to breach notification.", "หน้าที่ตาม PDPA ตั้งแต่การจัดทำแผนผังข้อมูลจนถึงการแจ้งเหตุละเมิด",
  [("GV-POL-004","Set rules","กำหนดหลักการ"),("ID-REG-003","Map data","จัดทำแผนผังข้อมูล"),("GV-REG-007","Record processing","บันทึกกิจกรรมการประมวลผล"),
   ("GV-TPL-002","Inform","แจ้งเจ้าของข้อมูล"),("GV-PRC-004","Assess impact","ประเมินผลกระทบ"),("GV-TPL-004","Bind processors","ผูกพันผู้ประมวลผล"),
   ("GV-PRC-005","Handle requests","จัดการคำขอใช้สิทธิ"),("RS-PLB-003","Respond to breach","รับมือการละเมิด"),("RS-TPL-002","Notify regulator","แจ้งหน่วยงานกำกับ")]),
 ("vendor", "Third-party lifecycle", "วงจรผู้ให้บริการภายนอก",
  "Select, contract, monitor, and exit suppliers.", "คัดเลือก ทำสัญญา ติดตาม และยุติการใช้ผู้ให้บริการ",
  [("GV-POL-006","Set rules","กำหนดหลักการ"),("GV-REG-009","Tier suppliers","จัดระดับผู้ให้บริการ"),("GV-PRC-008","Manage risk","บริหารความเสี่ยง"),
   ("GV-FRM-006","Assess","ประเมิน"),("GV-STD-002","Contract requirements","ข้อกำหนดในสัญญา"),("PR-FRM-003","Grant access","ให้สิทธิ์เข้าถึง"),("GV-FRM-007","Offboard","ยุติการใช้บริการ")]),
 ("people", "Joiner, mover, leaver", "การเข้า โยกย้าย และพ้นสภาพของพนักงาน",
  "Security across the employment lifecycle.", "ความมั่นคงปลอดภัยตลอดวงจรการจ้างงาน",
  [("GV-STD-001","Screen and set terms","คัดกรองและกำหนดเงื่อนไข"),("GV-FRM-002","Sign NDA","ลงนาม NDA"),("GV-POL-003","Accept AUP","รับทราบ AUP"),
   ("PR-FRM-001","Request access","ขอสิทธิ์"),("PR-PLN-001","Train","อบรม"),("PR-REC-002","Record training","บันทึกการอบรม"),("GV-FRM-003","Exit","พ้นสภาพ")]),
 ("continuity", "Continuity and recovery", "ความต่อเนื่องและการกู้คืน",
  "From impact analysis to tested recovery.", "ตั้งแต่การวิเคราะห์ผลกระทบจนถึงการกู้คืนที่ผ่านการทดสอบ",
  [("ID-RPT-002","Analyze impact","วิเคราะห์ผลกระทบ"),("RC-POL-001","Set rules","กำหนดหลักการ"),("PR-STD-006","Back up","สำรองข้อมูล"),
   ("PR-PRC-005","Restore","กู้คืนข้อมูล"),("PR-REC-003","Test restore","ทดสอบการกู้คืน"),("RC-PLN-001","Plan continuity","วางแผนความต่อเนื่อง"),
   ("RC-PLN-002","Plan IT recovery","วางแผนกู้คืนระบบ IT"),("RC-PRC-001","Run recovery","ดำเนินการกู้คืน"),("ID-PLN-002","Exercise","ฝึกซ้อม"),
   ("RC-REC-001","Report exercise","รายงานการฝึกซ้อม"),("RC-FRM-001","Sign off","ลงนามยืนยัน")]),
 ("assurance", "Oversight and assurance", "การกำกับติดตามและการให้ความเชื่อมั่น",
  "How management and auditors confirm the program works.", "วิธีที่ผู้บริหารและผู้ตรวจสอบยืนยันว่าแผนงานได้ผล",
  [("GV-REG-008","Measure","วัดผล"),("GV-PRC-007","Set audit method","กำหนดวิธีการตรวจสอบ"),("GV-PLN-002","Plan and run audits","วางแผนและตรวจสอบ"),("GV-TPL-006","Report findings","รายงานข้อตรวจพบ"),
   ("ID-PRC-006","Correct","แก้ไข"),("ID-REG-007","Track actions","ติดตามการแก้ไข"),("GV-PRC-006","Review","ทบทวน"),("GV-REC-001","Record decisions","บันทึกการตัดสินใจ")]),
 ("policy", "Policy lifecycle and exceptions", "วงจรนโยบายและข้อยกเว้น",
  "Write, approve, publish, and grant controlled exceptions.", "เขียน อนุมัติ เผยแพร่ และให้ข้อยกเว้นอย่างมีการควบคุม",
  [("GV-POL-001","Set direction","กำหนดทิศทาง"),("GV-PRC-002","Control documents","ควบคุมเอกสาร"),("GV-PRC-003","Manage exceptions","บริหารข้อยกเว้น"),
   ("GV-FRM-004","Request exception","ขอข้อยกเว้น"),("GV-REG-004","Register exception","ขึ้นทะเบียนข้อยกเว้น")]),
]


def theme_of(d):
    if d["id"] in THEME_OVERRIDE:
        return THEME_OVERRIDE[d["id"]]
    for x in d["iso"]:
        if x.startswith("A."):
            return THEME_OF[x.split(".")[1]]
    return "Organizational"

def theme_basis(d):
    ctrls = [x for x in d["iso"] if x.startswith("A.")]
    if d["id"] in THEME_OVERRIDE:
        return "override"
    return ctrls[0] if ctrls else "clause"

def tags_of(d):
    t = [d["ppt"]]
    trig = set(d["trigger"])
    if trig & {"CII", "PDPA", "CCA"}:
        t.append("Legal")
    if "PDPA" in trig or d["owner"] == "DPO":
        t.append("Privacy")
    if d["cat"] == "GV.SC":
        t.append("ThirdParty")
    if d["fn"] == "RC" or d["cat"] == "PR.IR":
        t.append("Resilience")
    if d["tier"] == "T4":
        t.append("Evidence")
    t += EXTRA_TAGS.get(d["id"], [])
    out = []
    for x in t:
        if x not in out:
            out.append(x)
    return out

def parse_guide():
    from register import REG
    R = REG["documents"]
    rows = {}
    for line in GUIDE_TABLE.strip().splitlines():
        p = [x.strip() for x in line.split("|")]
        assert len(p) == 5, line
        assert p[0] in DOC, p[0]
        assert p[0] not in rows, ("dup", p[0])
        rows[p[0]] = p
    G = {}
    for did in rows:   # table order is the tie-break order for the sequence
        p, r = rows[did], R[did]
        G[did] = dict(wave=r["wave"], track=r["track"], cap=r["cap"], reasons=p[1].split(","), src=p[2].split(","),
                      acts=[] if p[3] == "-" else p[3].split(","), deps=[] if p[4] == "-" else p[4].split(","))
    return G

GUIDE = parse_guide()
WORDER = list(WAVES)

def build():
    assert set(GUIDE) == set(DOC), sorted(set(DOC) ^ set(GUIDE))
    for did, g in GUIDE.items():
        assert g["wave"] in WAVES and g["track"] in TRACKS and g["cap"] in CAPS, did
        for r in g["reasons"]: assert r in REASONS, (did, r)
        for s in g["src"]: assert s in SOURCING, (did, s)
        for a in g["acts"]: assert a in ACTIVITIES, (did, a)
        for dep in g["deps"]:
            assert dep in DOC, (did, dep)
            assert WORDER.index(GUIDE[dep]["wave"]) <= WORDER.index(g["wave"]), ("dep in later wave", did, dep)
    # topological order: wave, then track A before B within the same wave, then dependencies, then table order
    table_order = {did: i for i, did in enumerate(GUIDE)}
    done, order = set(), []
    remaining = sorted(GUIDE, key=lambda x: (WORDER.index(GUIDE[x]["wave"]), table_order[x]))
    while remaining:
        progressed = False
        for did in list(remaining):
            if all(dep in done for dep in GUIDE[did]["deps"]):
                # do not let a doc jump ahead of an earlier wave still pending
                w = WORDER.index(GUIDE[did]["wave"])
                if any(WORDER.index(GUIDE[x]["wave"]) < w for x in remaining):
                    continue
                order.append(did); done.add(did); remaining.remove(did); progressed = True
                break
        assert progressed, ("cycle", remaining[:5])
    seq = {did: i + 1 for i, did in enumerate(order)}
    unlocks = {did: [] for did in GUIDE}
    for did, g in GUIDE.items():
        for dep in g["deps"]:
            unlocks[dep].append(did)
    flows_of = {did: [] for did in GUIDE}
    for f in FLOWS:
        for step in f[5]:
            assert step[0] in DOC, (f[0], step[0])
            if f[0] not in flows_of[step[0]]:
                flows_of[step[0]].append(f[0])
    out = {}
    for d in DOCS:
        g = GUIDE[d["id"]]
        later_parents = [p for p in d["parents"] if WORDER.index(GUIDE[p]["wave"]) > WORDER.index(g["wave"])]
        out[d["id"]] = dict(wave=g["wave"], track=g["track"], seq=seq[d["id"]], cap=g["cap"], reasons=g["reasons"], src=g["src"],
                            acts=g["acts"], deps=g["deps"], unlocks=sorted(unlocks[d["id"]], key=lambda x: seq[x]),
                            align=later_parents, theme=theme_of(d), theme_basis=theme_basis(d), tags=tags_of(d),
                            flows=flows_of[d["id"]], note=NOTES.get(d["id"]))
    return out, order

ENRICH, ORDER = build()

if __name__ == "__main__":
    from collections import Counter
    print(len(ENRICH), Counter(v["wave"] for v in ENRICH.values()), Counter(v["cap"] for v in ENRICH.values()))
    print(Counter(v["theme"] for v in ENRICH.values()))
    print(Counter(t for v in ENRICH.values() for t in v["tags"]))
    print([ (x, ENRICH[x]["align"]) for x in ORDER if ENRICH[x]["align"]])
    print(ORDER[:20])
    used = {a for v in ENRICH.values() for a in v["acts"]}
    print("unused activities", set(ACTIVITIES) - used)
