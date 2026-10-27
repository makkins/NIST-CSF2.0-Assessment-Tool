# -*- coding: utf-8 -*-
"""Industry packs and mandate tags for the Information Gathering tool (spec v2.0 Sections 6.3 and 8.1 A2).

PACKS: id, TSIC section, names, description, terminology, options (switches shown in Setup when the pack is chosen),
       and extra probes per Subcategory. Pack technical checks live in tc.py with pack=<id>.
MANDATES: requirement tags that attach to Subcategories. A tag is active when its source is on:
  "flag:<key>"       a Setup regulatory flag (cii, pdpa, iso, cca)
  "opt:<pack>:<key>" a pack option (only while that pack is selected)
  "pack:<pack>"      always on while that pack is selected
  mandate=True  counts as a mandate (forces drill-down and an evidence request from M3).
  mandate=False is a reference only (good practice or guidance, not binding).
  ver: "verified" = the instrument and the obligation were checked against a source on the date in VERIFY_LOG;
       "verify"   = confirm the clause or number before relying on it.
The Subcategory mapping of every tag is practitioner judgment, not regulatory text.
A pack never adds Register documents in v2.0."""

VERIFY_DATE = "2026-10-23"

PACKS = [
 dict(id="gen", tsic="Any", n=["General", "ทั่วไป"],
      d=["Base content only. Use when no other pack fits.", "ใช้เนื้อหาพื้นฐานเท่านั้น เลือกเมื่อไม่มีชุดอุตสาหกรรมอื่นที่ตรง"],
      terms=[], opts=[], probes={}),
 dict(id="hc", tsic="Q", n=["Healthcare", "สุขภาพและโรงพยาบาล"],
      d=["CII public health, PDPA sensitive data, medical devices, Hospital Accreditation, clinical shared workstations, break-glass access.",
         "CII ด้านสาธารณสุข ข้อมูลอ่อนไหวตาม PDPA อุปกรณ์การแพทย์ มาตรฐาน HA เครื่องที่ใช้ร่วมกันในหน่วยบริการ และบัญชีฉุกเฉิน (break-glass)"],
      terms=[["Customer", "Patient", "ลูกค้า", "ผู้ป่วย"], ["Business owner", "Clinical or department head", "เจ้าของงาน", "หัวหน้าหน่วยบริการหรือแผนก"], ["OT device", "Medical device (biomedical engineering)", "อุปกรณ์ OT", "อุปกรณ์การแพทย์ (วิศวกรรมชีวการแพทย์)"]],
      opts=[dict(k="sens", on=True, n=["Processes health data (sensitive personal data)", "ประมวลผลข้อมูลสุขภาพ (ข้อมูลส่วนบุคคลอ่อนไหว)"]),
            dict(k="state", on=False, n=["State hospital", "โรงพยาบาลของรัฐ"])],
      probes={
       "PR.AA-05": [["How do clinicians get emergency access to patient records when normal sign-in fails, and who reviews that access?", "แพทย์และพยาบาลเข้าถึงเวชระเบียนแบบฉุกเฉินอย่างไรเมื่อการล็อกอินปกติใช้ไม่ได้ และใครเป็นผู้ทบทวนการเข้าถึงนั้น"]],
       "ID.AM-01": [["Which medical devices store or send patient data, and who owns each one: biomedical engineering or IT?", "อุปกรณ์การแพทย์ใดจัดเก็บหรือส่งข้อมูลผู้ป่วย และใครเป็นเจ้าของแต่ละเครื่อง ระหว่างวิศวกรรมชีวการแพทย์กับ IT"]],
       "PR.AA-01": [["Do staff share logged-in workstations at nurse stations or service counters?", "เจ้าหน้าที่ใช้เครื่องที่ล็อกอินค้างไว้ร่วมกันที่เคาน์เตอร์พยาบาลหรือจุดบริการหรือไม่"]],
       "GV.SC-05": [["Do medical device contracts cover patching, remote support security, and the end-of-support date?", "สัญญาอุปกรณ์การแพทย์ครอบคลุมการแพตช์ ความมั่นคงปลอดภัยของการสนับสนุนระยะไกล และวันสิ้นสุดการสนับสนุนหรือไม่"]],
       "RC.RP-01": [["What is the downtime procedure for clinical care when the hospital information system is unavailable?", "ขั้นตอนการให้บริการผู้ป่วยระหว่างระบบสารสนเทศโรงพยาบาลใช้งานไม่ได้เป็นอย่างไร"]]}),
 dict(id="mfg", tsic="C", n=["Manufacturing", "การผลิต"],
      d=["OT and industrial control systems, IEC 62443 reference, supplier and plant network.", "ระบบ OT และระบบควบคุมอุตสาหกรรม อ้างอิง IEC 62443 เครือข่ายโรงงานและผู้ส่งมอบ"],
      terms=[["OT device", "Industrial control system (PLC, SCADA, HMI)", "อุปกรณ์ OT", "ระบบควบคุมอุตสาหกรรม (PLC, SCADA, HMI)"], ["Critical service", "Production line", "บริการสำคัญ", "สายการผลิต"]],
      opts=[],
      probes={
       "GV.OC-04": [["Which production lines stop if the plant network or the manufacturing execution system fails, and how long can each stop?", "สายการผลิตใดหยุดเมื่อเครือข่ายโรงงานหรือระบบบริหารการผลิตล่ม และแต่ละสายหยุดได้นานเท่าใด"]],
       "GV.OC-03": [["Do customers require security assessments or certifications, such as TISAX for automotive suppliers?", "ลูกค้ากำหนดให้มีการประเมินหรือการรับรองด้านความมั่นคงปลอดภัยหรือไม่ เช่น TISAX สำหรับผู้ผลิตชิ้นส่วนยานยนต์"]],
       "PR.IR-01": [["Is there a DMZ between the office network and the plant network?", "มี DMZ ระหว่างเครือข่ายสำนักงานกับเครือข่ายโรงงานหรือไม่"]],
       "RC.RP-03": [["Are PLC programs and HMI configurations backed up, and has a restore been tested?", "มีการสำรองโปรแกรม PLC และการตั้งค่า HMI และเคยทดสอบการกู้คืนหรือไม่"]]}),
 dict(id="fin", tsic="K", n=["Financial services", "การเงินและประกันภัย"],
      d=["Bank of Thailand, SEC, and Office of Insurance Commission requirements, third-party and cloud outsourcing, fraud and customer channels.",
         "ข้อกำหนดของ ธปท. ก.ล.ต. และ คปภ. การใช้บริการภายนอกและคลาวด์ การทุจริต และช่องทางบริการลูกค้า"],
      terms=[["Customer", "Customer or policyholder", "ลูกค้า", "ลูกค้าหรือผู้เอาประกันภัย"]],
      opts=[dict(k="bot", on=False, n=["Supervised by the Bank of Thailand", "อยู่ภายใต้การกำกับของ ธปท."]),
            dict(k="sec", on=False, n=["Licensed by the SEC", "ได้รับใบอนุญาตจาก ก.ล.ต."]),
            dict(k="oic", on=False, n=["Supervised by the Office of Insurance Commission", "อยู่ภายใต้การกำกับของ คปภ."])],
      probes={
       "RS.CO-02": [["Which regulator report forms and deadlines apply to a cyber incident, and who submits them?", "แบบรายงานและกำหนดเวลาของหน่วยงานกำกับใดใช้กับเหตุการณ์ไซเบอร์ และใครเป็นผู้ส่ง"]],
       "GV.SC-05": [["Does outsourcing or cloud use need regulator approval or notice, and was it obtained?", "การใช้บริการภายนอกหรือคลาวด์ต้องขออนุญาตหรือแจ้งหน่วยงานกำกับหรือไม่ และได้ดำเนินการแล้วหรือไม่"]],
       "GV.RR-01": [["Which board committee oversees IT and cyber risk, and does it include a director with IT knowledge?", "คณะกรรมการชุดใดกำกับความเสี่ยงด้าน IT และไซเบอร์ และมีกรรมการที่มีความรู้ด้าน IT หรือไม่"]],
       "DE.AE-02": [["Are cyber alerts and fraud alerts analyzed together?", "มีการวิเคราะห์การแจ้งเตือนด้านไซเบอร์และการทุจริตร่วมกันหรือไม่"]]}),
 dict(id="hosp", tsic="I, G", n=["Hospitality and retail", "โรงแรมและค้าปลีก"],
      d=["PCI DSS, point-of-sale and guest networks, customer data, seasonal staff.", "PCI DSS ระบบ POS และเครือข่ายสำหรับแขก ข้อมูลลูกค้า และพนักงานชั่วคราว"],
      terms=[["Customer", "Guest or shopper", "ลูกค้า", "แขกหรือผู้ซื้อ"]],
      opts=[dict(k="card", on=True, n=["Stores, processes, or sends payment card data", "จัดเก็บ ประมวลผล หรือส่งต่อข้อมูลบัตรชำระเงิน"])],
      probes={
       "PR.IR-01": [["Is guest Wi-Fi separated from point-of-sale and property management systems?", "Wi-Fi สำหรับแขกแยกจากระบบ POS และระบบบริหารโรงแรมหรือร้านค้าหรือไม่"]],
       "PR.AA-01": [["Do seasonal or shift staff share point-of-sale or front-desk logins?", "พนักงานชั่วคราวหรือพนักงานกะใช้บัญชี POS หรือเคาน์เตอร์ต้อนรับร่วมกันหรือไม่"]],
       "GV.OC-03": [["Who owns PCI compliance, and which acquirer or assessor validates it each year?", "ใครรับผิดชอบการปฏิบัติตาม PCI และธนาคารผู้รับบัตรหรือผู้ประเมินรายใดตรวจรับรองทุกปี"]]}),
 dict(id="util", tsic="D, E", n=["Energy and utilities", "พลังงานและสาธารณูปโภค"],
      d=["CII energy, OT, safety systems.", "CII ด้านพลังงาน ระบบ OT และระบบความปลอดภัย"],
      terms=[["OT device", "Control system or field device (SCADA, RTU, PLC)", "อุปกรณ์ OT", "ระบบควบคุมหรืออุปกรณ์ภาคสนาม (SCADA, RTU, PLC)"]],
      opts=[],
      probes={
       "GV.OC-04": [["Which control systems could harm public safety or supply if they were manipulated or stopped?", "ระบบควบคุมใดที่หากถูกแทรกแซงหรือหยุดทำงานจะกระทบความปลอดภัยของประชาชนหรือการจ่ายพลังงาน"]],
       "RS.CO-03": [["Do you share threat information with the sector ISAC and the regulator?", "มีการแลกเปลี่ยนข้อมูลภัยคุกคามกับ ISAC ของภาคและหน่วยงานกำกับหรือไม่"]]}),
 dict(id="pub", tsic="O", n=["Public sector", "ภาครัฐ"],
      d=["CII government services, government standards for websites and services.", "CII ด้านบริการภาครัฐ และมาตรฐานภาครัฐสำหรับเว็บไซต์และบริการ"],
      terms=[["Customer", "Citizen or service user", "ลูกค้า", "ประชาชนหรือผู้รับบริการ"]],
      opts=[dict(k="state", on=True, n=["State agency (department, state enterprise, or public university)", "หน่วยงานของรัฐ (ส่วนราชการ รัฐวิสาหกิจ หรือมหาวิทยาลัยของรัฐ)"])],
      probes={
       "ID.AM-05": [["Has each information system been classified low, medium, or high, and when was the classification last reviewed?", "ระบบสารสนเทศแต่ละระบบได้รับการจัดระดับต่ำ กลาง หรือสูงแล้วหรือไม่ และทบทวนครั้งล่าสุดเมื่อใด"]],
       "GV.OC-03": [["Which ministry or parent agency rules apply on top of national standards?", "เกณฑ์ของกระทรวงหรือหน่วยงานต้นสังกัดใดใช้บังคับเพิ่มเติมจากมาตรฐานระดับชาติ"]]}),
]

def M(id, src, kind, mandate, ref, req, subs, ver):
    return dict(id=id, src=src, kind=kind, mandate=mandate, ref=ref, req=req, s=subs.split(), ver=ver)

MANDATES = [
 # ---- Cybersecurity Act B.E. 2562 (CII) ----
 M("CII-44", "flag:cii", "law", True, ["Cybersecurity Act B.E. 2562, Section 44", "พ.ร.บ.การรักษาความมั่นคงปลอดภัยไซเบอร์ พ.ศ. 2562 มาตรา 44"],
   ["Keep a code of practice and a standard framework for cybersecurity.", "จัดทำประมวลแนวทางปฏิบัติและกรอบมาตรฐานด้านการรักษาความมั่นคงปลอดภัยไซเบอร์"], "GV.PO-01 GV.PO-02", "verified"),
 M("CII-54", "flag:cii", "law", True, ["Cybersecurity Act B.E. 2562, Section 54, and the 2024 notification on CII duties", "พ.ร.บ.การรักษาความมั่นคงปลอดภัยไซเบอร์ฯ มาตรา 54 และประกาศปี 2567 เรื่องหน้าที่ของ CII"],
   ["Assess risk and complete an audit at least once a year; report results to the NCSA by 31 January.", "ประเมินความเสี่ยงและตรวจสอบอย่างน้อยปีละครั้ง และรายงานผลต่อ สกมช. ภายใน 31 มกราคม"], "ID.RA-05 ID.IM-02 GV.OV-01", "verified"),
 M("CII-57", "flag:cii", "law", True, ["Cybersecurity Act B.E. 2562, Section 57, and the 2024 notification (effective 20 June 2024)", "พ.ร.บ.การรักษาความมั่นคงปลอดภัยไซเบอร์ฯ มาตรา 57 และประกาศปี 2567 (มีผล 20 มิถุนายน 2567)"],
   ["Report significant cyber threats to the NCSA and the regulator within 24 hours.", "รายงานภัยคุกคามทางไซเบอร์ที่มีนัยสำคัญต่อ สกมช. และหน่วยงานกำกับภายใน 24 ชั่วโมง"], "RS.CO-02 RS.MA-01", "verified"),
 # ---- PDPA B.E. 2562 ----
 M("PDPA-37S", "flag:pdpa", "law", True, ["PDPA B.E. 2562, Section 37(1), and the PDPC notification on security measures", "พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 มาตรา 37(1) และประกาศคณะกรรมการฯ เรื่องมาตรการรักษาความมั่นคงปลอดภัย"],
   ["Apply appropriate security measures to personal data, including access control.", "จัดให้มีมาตรการรักษาความมั่นคงปลอดภัยที่เหมาะสมสำหรับข้อมูลส่วนบุคคล รวมถึงการควบคุมการเข้าถึง"], "PR.DS-01 PR.DS-02 PR.AA-05", "verified"),
 M("PDPA-37B", "flag:pdpa", "law", True, ["PDPA B.E. 2562, Section 37(4), and the PDPC notification on breach notification (2022)", "พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคลฯ มาตรา 37(4) และประกาศคณะกรรมการฯ เรื่องการแจ้งเหตุละเมิด (2565)"],
   ["Notify the PDPC Office of a personal data breach within 72 hours unless it is unlikely to affect individuals; notify data subjects of high-risk breaches.", "แจ้งเหตุละเมิดข้อมูลส่วนบุคคลต่อสำนักงานฯ ภายใน 72 ชั่วโมง เว้นแต่ไม่มีความเสี่ยงต่อบุคคล และแจ้งเจ้าของข้อมูลเมื่อมีความเสี่ยงสูง"], "RS.CO-02 RS.MA-01", "verified"),
 M("PDPA-39", "flag:pdpa", "law", True, ["PDPA B.E. 2562, Section 39", "พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคลฯ มาตรา 39"],
   ["Keep a record of processing activities.", "จัดทำบันทึกรายการกิจกรรมการประมวลผล (ROPA)"], "ID.AM-07", "verified"),
 M("PDPA-40", "flag:pdpa", "law", True, ["PDPA B.E. 2562, Section 40", "พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคลฯ มาตรา 40"],
   ["Bind data processors by agreement to protect personal data and follow the controller's instructions.", "ทำข้อตกลงกับผู้ประมวลผลข้อมูลให้ปกป้องข้อมูลและปฏิบัติตามคำสั่งของผู้ควบคุมข้อมูล"], "GV.SC-05", "verify"),
 # ---- Computer Crime Act ----
 M("CCA-26", "flag:cca", "law", True, ["Computer Crime Act B.E. 2550 (amended B.E. 2560), Section 26, and the MDES notification on traffic data retention", "พ.ร.บ.ว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ฯ มาตรา 26 และประกาศกระทรวงดิจิทัลฯ เรื่องการเก็บรักษาข้อมูลจราจรคอมพิวเตอร์"],
   ["Service providers keep computer traffic data for at least 90 days.", "ผู้ให้บริการเก็บรักษาข้อมูลจราจรคอมพิวเตอร์ไว้อย่างน้อย 90 วัน"], "PR.PS-04", "verify"),
 # ---- ISO/IEC 27001 certification ----
 M("ISO-RA", "flag:iso", "standard", True, ["ISO/IEC 27001:2022, Clauses 6.1.2 and 8.2", "ISO/IEC 27001:2022 ข้อ 6.1.2 และ 8.2"],
   ["Run and record information security risk assessments at planned intervals.", "ประเมินความเสี่ยงด้านความมั่นคงปลอดภัยสารสนเทศตามรอบที่กำหนดและเก็บบันทึก"], "ID.RA-05 GV.RM-01", "verified"),
 M("ISO-AUD", "flag:iso", "standard", True, ["ISO/IEC 27001:2022, Clauses 9.2 and 9.3", "ISO/IEC 27001:2022 ข้อ 9.2 และ 9.3"],
   ["Hold internal audits and management reviews at planned intervals.", "ตรวจสอบภายในและทบทวนโดยผู้บริหารตามรอบที่กำหนด"], "ID.IM-02 GV.OV-01", "verified"),
 # ---- Healthcare ----
 M("HC-PDPA26", "opt:hc:sens", "law", True, ["PDPA B.E. 2562, Section 26 (health data)", "พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคลฯ มาตรา 26 (ข้อมูลสุขภาพ)"],
   ["Process health data only on a Section 26 basis, with stronger protection for sensitive data.", "ประมวลผลข้อมูลสุขภาพได้เฉพาะตามฐานในมาตรา 26 และต้องคุ้มครองข้อมูลอ่อนไหวอย่างเข้มงวดขึ้น"], "GV.OC-03 PR.DS-01 PR.AA-05", "verified"),
 M("HC-NHA7", "pack:hc", "law", True, ["National Health Act B.E. 2550, Section 7", "พ.ร.บ.สุขภาพแห่งชาติ พ.ศ. 2550 มาตรา 7"],
   ["Keep personal health information confidential.", "ข้อมูลด้านสุขภาพของบุคคลเป็นความลับส่วนบุคคล"], "PR.DS-01 PR.AA-05", "verified"),
 M("HC-SHG", "opt:hc:state", "guideline", False, ["NCSA and TMI Cybersecurity Operational Guidelines for State Hospitals B.E. 2567", "แนวทางปฏิบัติด้านการรักษาความมั่นคงปลอดภัยไซเบอร์สำหรับโรงพยาบาลของรัฐ พ.ศ. 2567 (สกมช. และ TMI)"],
   ["Guideline for state hospitals; confirm which parts the parent ministry requires.", "แนวทางสำหรับโรงพยาบาลของรัฐ ตรวจสอบว่ากระทรวงต้นสังกัดกำหนดให้ใช้ส่วนใด"], "GV.PO-01 PR.AA-05 PR.DS-11 RS.MA-01", "verified"),
 M("HC-HA", "pack:hc", "standard", False, ["Hospital Accreditation (HA) standards, information management chapter", "มาตรฐานโรงพยาบาลและบริการสุขภาพ (HA) หมวดการจัดการสารสนเทศ"],
   ["Accreditation surveyors review information security and system continuity; confirm the current edition and section.", "ผู้เยี่ยมสำรวจ HA ทบทวนความมั่นคงปลอดภัยสารสนเทศและความต่อเนื่องของระบบ ตรวจสอบฉบับและหมวดที่ใช้ปัจจุบัน"], "GV.PO-01 RC.RP-01", "verify"),
 # ---- Manufacturing and utilities (references, not law) ----
 M("OT-62443", "pack:mfg", "standard", False, ["IEC 62443-2-1 and 62443-3-3; NIST SP 800-82 Rev. 3", "IEC 62443-2-1 และ 62443-3-3; NIST SP 800-82 Rev. 3"],
   ["Usual reference for OT security; usually a customer or insurer expectation, not law.", "มาตรฐานอ้างอิงทั่วไปด้านความมั่นคงปลอดภัย OT ส่วนใหญ่เป็นความคาดหวังของลูกค้าหรือบริษัทประกัน ไม่ใช่กฎหมาย"], "ID.AM-01 PR.IR-01 PR.PS-01 RC.RP-03", "verified"),
 M("UT-62443", "pack:util", "standard", False, ["IEC 62443 and NIST SP 800-82 Rev. 3; Energy ISAC (NCSA and Ministry of Energy, 2025)", "IEC 62443 และ NIST SP 800-82 Rev. 3; Energy ISAC (สกมช. และกระทรวงพลังงาน 2568)"],
   ["OT security reference and sector information sharing; check the regulator named in any CII designation.", "มาตรฐานอ้างอิงด้าน OT และการแลกเปลี่ยนข้อมูลในภาค ตรวจสอบหน่วยงานกำกับที่ระบุในหนังสือกำหนด CII"], "ID.AM-01 PR.IR-01 RS.CO-03", "verified"),
 # ---- Financial services ----
 M("BOT-21", "opt:fin:bot", "regulation", True, ["Bank of Thailand Notification SorNorSor. 21/2562, IT risk governance of financial institutions", "ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 21/2562 เรื่องหลักเกณฑ์การกำกับดูแลความเสี่ยงด้านเทคโนโลยีสารสนเทศของสถาบันการเงิน"],
   ["Board-level IT risk governance, IT and cyber risk management, and third-party risk management; check the clauses for each control.", "การกำกับดูแลความเสี่ยงด้าน IT ระดับคณะกรรมการ การบริหารความเสี่ยงด้าน IT และไซเบอร์ และการบริหารความเสี่ยงจากบุคคลภายนอก ตรวจสอบข้อที่เกี่ยวข้องรายการควบคุม"], "GV.RR-01 GV.RM-01 GV.OV-01 GV.SC-04 GV.SC-07 PR.AA-05", "verified"),
 M("BOT-19", "opt:fin:bot", "regulation", True, ["Bank of Thailand Notification FPG. 19/2559, IT outsourcing", "ประกาศธนาคารแห่งประเทศไทย ที่ สนส. 19/2559 เรื่องการใช้บริการด้านเทคโนโลยีสารสนเทศจากผู้ให้บริการภายนอก"],
   ["Controls and approvals for IT outsourcing, including cloud.", "การควบคุมและการอนุมัติการใช้บริการ IT จากภายนอก รวมถึงคลาวด์"], "GV.SC-05 GV.SC-06", "verify"),
 M("SEC-37", "opt:fin:sec", "regulation", True, ["SEC Notification Sor Thor. 37/2559 on IT system standards, updated by Sor Thor. 38/2565", "ประกาศ ก.ล.ต. ที่ สธ. 37/2559 เรื่องมาตรฐานการประกอบธุรกิจเกี่ยวกับระบบเทคโนโลยีสารสนเทศ และฉบับแก้ไข สธ. 38/2565"],
   ["IT governance, security, and continuity standards for licensed businesses; check the clauses for each control.", "มาตรฐานการกำกับดูแล ความมั่นคงปลอดภัย และความต่อเนื่องของระบบ IT สำหรับผู้ได้รับใบอนุญาต ตรวจสอบข้อที่เกี่ยวข้อง"], "GV.RM-01 PR.AA-05 PR.DS-11 DE.CM-01 RS.MA-01", "verified"),
 M("OIC-63", "opt:fin:oic", "regulation", True, ["OIC criteria on IT risk management B.E. 2563 (effective 1 January 2021)", "หลักเกณฑ์ คปภ. เรื่องการบริหารความเสี่ยงด้านเทคโนโลยีสารสนเทศ พ.ศ. 2563 (มีผล 1 มกราคม 2564)"],
   ["A director with IT knowledge, outsourcing controls, and a report of critical cyber attacks within 72 hours.", "มีกรรมการที่มีความรู้ด้าน IT การควบคุมการใช้บริการภายนอก และรายงานการโจมตีทางไซเบอร์ที่ร้ายแรงภายใน 72 ชั่วโมง"], "GV.RR-01 GV.SC-05 RS.CO-02", "verified"),
 # ---- Hospitality and retail: PCI DSS (contract) ----
 M("PCI-8.4.2", "opt:hosp:card", "contract", True, ["PCI DSS v4.0.1, Requirement 8.4.2", "PCI DSS v4.0.1 ข้อ 8.4.2"],
   ["Multi-factor authentication for all access into the cardholder data environment.", "ใช้การยืนยันตัวตนหลายปัจจัยสำหรับการเข้าถึงทั้งหมดเข้าสู่ระบบข้อมูลบัตร (CDE)"], "PR.AA-03", "verified"),
 M("PCI-11.3", "opt:hosp:card", "contract", True, ["PCI DSS v4.0.1, Requirements 11.3 and 11.4", "PCI DSS v4.0.1 ข้อ 11.3 และ 11.4"],
   ["Quarterly internal and approved external vulnerability scans; annual penetration test, including segmentation tests.", "สแกนช่องโหว่ภายในและภายนอกทุกไตรมาส และทดสอบเจาะระบบรวมถึงการแบ่งส่วนเครือข่ายทุกปี"], "ID.RA-01 ID.IM-02", "verified"),
 M("PCI-3-4", "opt:hosp:card", "contract", True, ["PCI DSS v4.0.1, Requirements 3 and 4", "PCI DSS v4.0.1 ข้อ 3 และ 4"],
   ["Protect stored account data and encrypt cardholder data sent over open networks.", "ปกป้องข้อมูลบัญชีที่จัดเก็บ และเข้ารหัสข้อมูลผู้ถือบัตรที่ส่งผ่านเครือข่ายสาธารณะ"], "PR.DS-01 PR.DS-02", "verify"),
 M("PCI-6-10", "opt:hosp:card", "contract", True, ["PCI DSS v4.0.1, Requirements 6.3 and 10", "PCI DSS v4.0.1 ข้อ 6.3 และ 10"],
   ["Patch known vulnerabilities on a set timeline and log and review access to cardholder data.", "แก้ไขช่องโหว่ที่ทราบตามกรอบเวลา และบันทึกและทบทวนการเข้าถึงข้อมูลผู้ถือบัตร"], "PR.PS-02 PR.PS-04 DE.CM-09", "verify"),
 M("PCI-12", "opt:hosp:card", "contract", True, ["PCI DSS v4.0.1, Requirements 12.8 and 12.10", "PCI DSS v4.0.1 ข้อ 12.8 และ 12.10"],
   ["Manage service providers that affect card data, and keep an incident response plan ready.", "บริหารผู้ให้บริการที่เกี่ยวข้องกับข้อมูลบัตร และมีแผนรับมือเหตุการณ์ที่พร้อมใช้"], "GV.SC-07 RS.MA-01", "verify"),
 # ---- Public sector ----
 M("NCSC-66", "opt:pub:state", "regulation", True, ["NCSC notifications on security categories and minimum standards for data and information systems B.E. 2566 (effective 18 January 2025)", "ประกาศ กมช. เรื่องการจัดระดับความมั่นคงปลอดภัยและมาตรฐานขั้นต่ำของข้อมูลและระบบสารสนเทศ พ.ศ. 2566 (มีผล 18 มกราคม 2568)"],
   ["Classify each data and information system low, medium, or high; review at least every three years; apply the minimum measures for the category.", "จัดระดับข้อมูลและระบบสารสนเทศเป็นต่ำ กลาง หรือสูง ทบทวนอย่างน้อยทุก 3 ปี และใช้มาตรการขั้นต่ำตามระดับ"], "ID.AM-05 ID.RA-05 GV.PO-01 PR.AA-05 PR.DS-01 PR.PS-02 DE.CM-01 RS.MA-01", "verified"),
]

# Sources checked for the "verified" status (dates are when the instrument was checked, not legal advice).
VERIFY_LOG = [
 ("Cybersecurity Act Sections 44, 54, 57 and the 2024 notification", "ThaiCERT CII page; Tilleke & Gibbins (Workshop verification log, 16 October 2026)"),
 ("PDPA Sections 26, 37 and the PDPC breach notification (2022)", "Tilleke & Gibbins (Workshop verification log, 16 October 2026)"),
 ("PDPA Section 39 record of processing", "Forvis Mazars Thailand, record of processing activities (checked 23 October 2026)"),
 ("BOT SorNorSor. 21/2562 and FPG. 19/2559", "Google Cloud BOT Thailand compliance page (checked 23 October 2026); FPG 19 clause content not checked"),
 ("SEC Sor Thor. 37/2559 and 38/2565; OIC B.E. 2563", "Huawei Cloud compliance page; Tilleke & Gibbins (Workshop verification log, 16 October 2026)"),
 ("National Health Act Section 7; State Hospital Guidelines B.E. 2567", "Act text; MOPH-hosted guideline (Workshop verification log, 16 October 2026)"),
 ("NCSC minimum standards B.E. 2566", "Tilleke & Gibbins (Workshop verification log, 16 October 2026)"),
 ("PCI DSS v4.0.1 Requirements 8.4.2, 11.3, 11.4", "Secondary source summary of v4.0.1 (checked 23 October 2026); confirm against the PCI SSC document library"),
]

assert all(m["src"].split(":")[0] in ("flag", "opt", "pack") for m in MANDATES)
assert len({m["id"] for m in MANDATES}) == len(MANDATES)
