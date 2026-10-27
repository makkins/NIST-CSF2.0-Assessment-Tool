# -*- coding: utf-8 -*-
# RS Respond
C = {}

C["RS-PLN-001"] = dict(
 purpose=("This plan defines how [Organization Name] prepares for, responds to, and coordinates cybersecurity incidents, including roles, decision authority, communication, third-party coordination, and the hand-off to recovery (RS.MA, RS.CO; NIST SP 800-61 Rev. 3; CSA s.44).",
          "แผนนี้กำหนดวิธีที่ [ชื่อองค์กร] เตรียมพร้อม รับมือ และประสานงานเมื่อเกิดเหตุการณ์ภัยคุกคามทางไซเบอร์ รวมถึงบทบาท อำนาจตัดสินใจ การสื่อสาร การประสานกับบุคคลภายนอก และการส่งต่อไปยังการกู้คืน (RS.MA, RS.CO; NIST SP 800-61 Rev. 3; พ.ร.บ.ไซเบอร์ฯ มาตรา 44)"),
 sections=[
  ("Incident Response Team and Authority", "ทีมรับมือเหตุการณ์และอำนาจตัดสินใจ", "Define team roles and who decides what during an incident.", "กำหนดบทบาทของทีมและผู้มีอำนาจตัดสินใจในแต่ละเรื่องระหว่างเหตุการณ์",
   {"t": ["Role", "Who", "Authority and responsibility"], "r": [
     ["Incident Commander", "[CISO]", "Leads response; may isolate systems and disable accounts"], ["Executive sponsor", "[CEO] or delegate", "Decides on business shutdown, ransom questions, external statements"],
     ["Technical lead", "[ITM]", "Containment, eradication, recovery actions"], ["Privacy lead", "[DPO]", "Breach assessment and PDPC notification"],
     ["Legal", "[LEGAL]", "Legal privilege, law enforcement, contracts"], ["Communications", "[COMMS]", "Internal and external messages"],
     ["MSSP and IR retainer", "External", "Monitoring, forensics, surge support"], ["Business liaisons", "Affected business heads", "Business impact and workarounds"]], "w": [3.5, 3.5, 9.5]},
   {"t": ["บทบาท", "ผู้รับผิดชอบ", "อำนาจและความรับผิดชอบ"], "r": [
     ["ผู้บัญชาการเหตุการณ์", "[CISO]", "นำการรับมือ มีอำนาจแยกระบบและปิดบัญชี"], ["ผู้บริหารที่รับผิดชอบ", "[CEO] หรือผู้ได้รับมอบหมาย", "ตัดสินใจหยุดการดำเนินธุรกิจ ประเด็นค่าไถ่ และการแถลงต่อภายนอก"],
     ["หัวหน้าด้านเทคนิค", "[ITM]", "การควบคุม การกำจัด และการกู้คืน"], ["หัวหน้าด้านความเป็นส่วนตัว", "[DPO]", "การประเมินเหตุละเมิดและการแจ้ง สคส."],
     ["ฝ่ายกฎหมาย", "[LEGAL]", "เอกสิทธิ์ทางกฎหมาย การประสานเจ้าหน้าที่ สัญญา"], ["ฝ่ายสื่อสาร", "[COMMS]", "การสื่อสารภายในและภายนอก"],
     ["MSSP และผู้ให้บริการรับมือเหตุตามสัญญา", "ภายนอก", "การเฝ้าระวัง นิติวิทยาศาสตร์ดิจิทัล และการสนับสนุนเพิ่มเติม"], ["ผู้ประสานงานฝ่ายธุรกิจ", "หัวหน้าหน่วยธุรกิจที่ได้รับผลกระทบ", "ผลกระทบทางธุรกิจและทางเลือกทดแทน"]], "w": [3.5, 3.5, 9.5]},
   {"t": ["Role", "Who at CMC", "Authority and responsibility"], "r": [
     ["Incident Commander", "Security Manager (deputy: IT Infrastructure Manager)", "Leads response; may isolate systems and disable accounts at any hour"],
     ["Executive sponsor", "CEO (deputy: CIO)", "Decides on clinical system shutdown with the Medical Director; approves external statements"],
     ["Clinical liaison", "Medical Director and nursing supervisor on duty", "Activates downtime procedures and patient safety measures"],
     ["Technical lead", "IT Infrastructure Manager", "Containment, eradication, recovery"], ["Privacy lead", "DPO", "Breach assessment; PDPC notification within 72 hours"],
     ["Legal", "Legal Counsel", "Police reports, legal privilege, vendor contracts"], ["Communications", "Corporate Communications Manager", "Staff, patient, and media messages"],
     ["MSSP and IR retainer", "MSSP Vendor E", "24x7 monitoring, forensics, surge support within 4 hours on site"]], "w": [3.5, 4.0, 9.0]}),
  ("Response Phases", "ระยะการรับมือ", "Describe response phases aligned with NIST SP 800-61 Rev. 3 and CSF 2.0 functions.", "อธิบายระยะการรับมือตาม NIST SP 800-61 Rev. 3 และ Function ของ CSF 2.0",
   {"t": ["Phase", "Key activities", "Document"], "r": [
     ["Prepare (GV, ID, PR)", "Plans, contacts, tools, training, exercises", "This plan, RS-REG-002, ID-PLN-002"], ["Detect and analyze (DE)", "Triage, declare, classify severity", "DE-PRC-002, DE-STD-002"],
     ["Respond (RS)", "Contain, eradicate, investigate, notify", "RS-PRC-001, playbooks, RS-PRC-002, RS-PRC-003"], ["Recover (RC)", "Restore, validate, declare end of recovery", "RC-PLN-002, RC-FRM-001"],
     ["Improve (ID.IM)", "Lessons learned, plan updates", "ID-TPL-001, ID-REG-007"]], "w": [3.5, 7.0, 6.0]},
   {"t": ["ระยะ", "กิจกรรมหลัก", "เอกสาร"], "r": [
     ["เตรียมพร้อม (GV, ID, PR)", "แผน รายชื่อผู้ติดต่อ เครื่องมือ การอบรม การฝึกซ้อม", "แผนนี้ RS-REG-002 ID-PLN-002"], ["ตรวจจับและวิเคราะห์ (DE)", "คัดกรอง ประกาศ จัดระดับความรุนแรง", "DE-PRC-002, DE-STD-002"],
     ["ตอบสนอง (RS)", "ควบคุม กำจัด สอบสวน แจ้งเหตุ", "RS-PRC-001 คู่มือรับมือ RS-PRC-002 RS-PRC-003"], ["กู้คืน (RC)", "กู้คืน ตรวจสอบ ประกาศสิ้นสุดการกู้คืน", "RC-PLN-002, RC-FRM-001"],
     ["ปรับปรุง (ID.IM)", "บทเรียนที่ได้รับ ปรับปรุงแผน", "ID-TPL-001, ID-REG-007"]], "w": [3.5, 7.0, 6.0]}),
  ("Escalation and Recovery Criteria", "เกณฑ์การยกระดับและการเริ่มกู้คืน", "Define escalation triggers and the criteria to start recovery (RS.MA-04, RS.MA-05).", "กำหนดเงื่อนไขการยกระดับและเกณฑ์การเริ่มกู้คืน (RS.MA-04, RS.MA-05)",
   ["Escalate to the executive sponsor for any SEV-1, any incident needing regulatory notification, or any decision to shut down a critical service.", "Activate the Crisis Management Plan (RC-PLN-003) when impact spreads beyond IT.",
    "Start recovery only when the threat is contained, the root access path is closed, and clean restore points are confirmed."],
   ["ยกระดับต่อผู้บริหารที่รับผิดชอบสำหรับเหตุการณ์ SEV-1 ทุกกรณี เหตุการณ์ที่ต้องแจ้งหน่วยงานกำกับ หรือการตัดสินใจหยุดบริการสำคัญ", "เปิดใช้แผนบริหารภาวะวิกฤต (RC-PLN-003) เมื่อผลกระทบขยายเกินฝ่าย IT",
    "เริ่มกู้คืนเมื่อควบคุมภัยคุกคามได้แล้ว ปิดช่องทางการเข้าถึงต้นเหตุแล้ว และยืนยันจุดกู้คืนที่สะอาดแล้วเท่านั้น"]),
  ("Third-Party Coordination", "การประสานงานกับบุคคลภายนอก", "Describe coordination with suppliers, law enforcement, regulators, and peers (RS.MA-01, GV.SC-08).", "อธิบายการประสานงานกับผู้ให้บริการ เจ้าหน้าที่ตามกฎหมาย หน่วยงานกำกับ และองค์กรในภาคส่วนเดียวกัน (RS.MA-01, GV.SC-08)",
   ["Engage critical suppliers named in RS-REG-002 according to contract clause SC-07 (GV-STD-002).", "Report crimes to the police or the Technology Crime Suppression Division as advised by Legal.", "Notify NCSA, the sector regulator, and the PDPC according to RS-PRC-003.", "Share indicators with ThaiCERT and sector peers where helpful."],
   ["ประสานผู้ให้บริการสำคัญที่ระบุใน RS-REG-002 ตามข้อสัญญา SC-07 (GV-STD-002)", "แจ้งความต่อตำรวจหรือกองบังคับการปราบปรามการกระทำความผิดเกี่ยวกับอาชญากรรมทางเทคโนโลยีตามคำแนะนำของฝ่ายกฎหมาย", "แจ้ง สกมช. หน่วยงานกำกับ และ สคส. ตาม RS-PRC-003", "แบ่งปันตัวบ่งชี้กับ ThaiCERT และองค์กรในภาคส่วนเดียวกันเมื่อเป็นประโยชน์"]),
 ],
 bp=[("Decide ransom payment policy, decision authority, and legal checks before an incident, not during it.", "กำหนดนโยบายเรื่องการจ่ายค่าไถ่ ผู้มีอำนาจตัดสินใจ และการตรวจสอบทางกฎหมายก่อนเกิดเหตุการณ์ ไม่ใช่ระหว่างเหตุการณ์"),
     ("Keep a printed copy and an offline copy of the plan and contacts; systems may be down.", "เก็บสำเนาแผนและรายชื่อผู้ติดต่อแบบพิมพ์และแบบออฟไลน์ เพราะระบบอาจใช้งานไม่ได้"),
     ("Use out-of-band communication (for example, a separate messaging group) if email may be compromised.", "ใช้ช่องทางสื่อสารสำรอง (เช่น กลุ่มส่งข้อความแยก) หากอีเมลอาจถูกโจมตี"),
     ("Exercise the plan at least once a year with executives.", "ฝึกซ้อมแผนร่วมกับผู้บริหารอย่างน้อยปีละครั้ง")],
 mistakes=[("Plan lists roles but not who can make decisions at 2 a.m.", "แผนระบุบทบาทแต่ไม่ระบุผู้มีอำนาจตัดสินใจในเวลากลางคืน"),
           ("Plan stored only on the file server that ransomware encrypts.", "จัดเก็บแผนไว้บนไฟล์เซิร์ฟเวอร์เท่านั้น ซึ่งอาจถูกแรนซัมแวร์เข้ารหัส")],
 rev="Updated in March 2026 after EX-2026-01 to name night-time decision authority for notifications and to add the clinical liaison role.",
)

C["RS-PRC-001"] = dict(
 purpose=("This procedure gives the step-by-step actions for handling a declared incident: triage, categorization, containment, eradication, escalation, and hand-off to recovery (RS.MA-02 to RS.MA-05, RS.MI-01, RS.MI-02).",
          "ระเบียบปฏิบัตินี้กำหนดการดำเนินการทีละขั้นตอนในการจัดการเหตุการณ์ที่ประกาศแล้ว ได้แก่ การคัดกรอง การจัดประเภท การควบคุม การกำจัด การยกระดับ และการส่งต่อไปยังการกู้คืน (RS.MA-02 ถึง RS.MA-05, RS.MI-01, RS.MI-02)"),
 sections=[
  ("Handling Steps", "ขั้นตอนการจัดการ", "Describe actions, owners, and time targets for each step.", "อธิบายการดำเนินการ ผู้รับผิดชอบ และเป้าหมายเวลาในแต่ละขั้นตอน",
   {"t": ["Step", "Action", "Owner", "Target"], "r": [
     ["1 Validate", "Confirm the report is a real incident; open the record in RS-REG-001", "[SOC] or security engineer", "Within 30 minutes for High alerts"],
     ["2 Categorize", "Assign category and severity per DE-STD-002", "[CISO]", "Within 1 hour"],
     ["3 Escalate", "Notify per severity; assemble the response team", "[CISO]", "Per DE-STD-002"],
     ["4 Contain", "Isolate hosts, disable accounts, block indicators, preserve evidence first where possible", "Technical lead", "SEV-1 within 1 hour of declaration"],
     ["5 Investigate", "Determine scope, root cause, and data affected (RS-PRC-002)", "Security team, IR retainer", "Ongoing"],
     ["6 Eradicate", "Remove malware and persistence, reset credentials, patch the entry point", "Technical lead", "Before recovery"],
     ["7 Hand off to recovery", "Apply recovery criteria (RS-PLN-001) and start RC-PLN-002", "Incident Commander", "When criteria met"],
     ["8 Close", "Complete the investigation report, lessons learned, and register entry", "[CISO]", "Within 10 working days of recovery"]], "w": [2.8, 7.2, 3.3, 3.2]},
   {"t": ["ขั้นตอน", "การดำเนินการ", "ผู้รับผิดชอบ", "เป้าหมาย"], "r": [
     ["1 ยืนยัน", "ยืนยันว่าเป็นเหตุการณ์จริง และเปิดบันทึกใน RS-REG-001", "[SOC] หรือวิศวกรความมั่นคงปลอดภัย", "ภายใน 30 นาทีสำหรับการแจ้งเตือนระดับสูง"],
     ["2 จัดประเภท", "กำหนดประเภทและระดับความรุนแรงตาม DE-STD-002", "[CISO]", "ภายใน 1 ชั่วโมง"],
     ["3 ยกระดับ", "แจ้งตามระดับความรุนแรง และจัดตั้งทีมรับมือ", "[CISO]", "ตาม DE-STD-002"],
     ["4 ควบคุม", "แยกเครื่อง ปิดบัญชี บล็อกตัวบ่งชี้ และเก็บรักษาพยานหลักฐานก่อนเมื่อทำได้", "หัวหน้าด้านเทคนิค", "SEV-1 ภายใน 1 ชั่วโมงหลังประกาศ"],
     ["5 สอบสวน", "ระบุขอบเขต สาเหตุที่แท้จริง และข้อมูลที่ได้รับผลกระทบ (RS-PRC-002)", "ทีมความมั่นคงปลอดภัย ผู้ให้บริการรับมือเหตุ", "ต่อเนื่อง"],
     ["6 กำจัด", "ลบมัลแวร์และกลไกคงการเข้าถึง รีเซ็ตข้อมูลยืนยันตัวตน และแก้ไขช่องทางที่ถูกใช้เข้ามา", "หัวหน้าด้านเทคนิค", "ก่อนการกู้คืน"],
     ["7 ส่งต่อการกู้คืน", "ใช้เกณฑ์การเริ่มกู้คืน (RS-PLN-001) และเริ่ม RC-PLN-002", "ผู้บัญชาการเหตุการณ์", "เมื่อเป็นไปตามเกณฑ์"],
     ["8 ปิด", "จัดทำรายงานการสอบสวน บทเรียนที่ได้รับ และปรับปรุงทะเบียน", "[CISO]", "ภายใน 10 วันทำการหลังการกู้คืน"]], "w": [2.8, 7.2, 3.3, 3.2]}),
 ],
 bp=[("Contain fast but capture volatile evidence (memory, logs) on key hosts before reimaging.", "ควบคุมเหตุการณ์อย่างรวดเร็ว แต่เก็บพยานหลักฐานที่สูญหายง่าย (หน่วยความจำ Log) จากเครื่องสำคัญก่อนติดตั้งระบบใหม่"),
     ("Keep a time-stamped action log from the first minute.", "บันทึกการดำเนินการพร้อมเวลาตั้งแต่นาทีแรก")],
 mistakes=[("Reimaging infected machines immediately, destroying evidence of how the attacker got in.", "ติดตั้งระบบใหม่ให้เครื่องที่ติดมัลแวร์ทันที ทำให้พยานหลักฐานว่าผู้โจมตีเข้ามาได้อย่างไรสูญหาย")],
)

C["RS-PLB-001"] = dict(
 purpose=("This playbook gives specific actions for responding to ransomware, from first alert to safe recovery, including decisions that must be made by executives (RS.MI-01, RS.MI-02, RC.RP-03).",
          "คู่มือนี้กำหนดการดำเนินการเฉพาะในการรับมือแรนซัมแวร์ ตั้งแต่การแจ้งเตือนแรกจนถึงการกู้คืนอย่างปลอดภัย รวมถึงการตัดสินใจที่ผู้บริหารต้องเป็นผู้ตัดสิน (RS.MI-01, RS.MI-02, RC.RP-03)"),
 sections=[
  ("First Hour Actions", "การดำเนินการในชั่วโมงแรก", "List immediate actions in order.", "ระบุการดำเนินการเร่งด่วนตามลำดับ",
   {"n": ["Declare SEV-1 and notify the Incident Commander and executive sponsor.", "Isolate affected hosts with EDR; do not power off unless instructed (preserve memory).", "Disable compromised accounts and revoke active sessions; reset privileged credentials from a clean device.",
          "Block known indicators at firewall, DNS, and email gateway.", "Protect backups: confirm immutable copies are intact; disconnect backup systems from the network if at risk.", "Activate business downtime procedures.", "Engage the IR retainer and start the evidence log."]},
   {"n": ["ประกาศ SEV-1 และแจ้งผู้บัญชาการเหตุการณ์และผู้บริหารที่รับผิดชอบ", "แยกเครื่องที่ได้รับผลกระทบด้วย EDR และห้ามปิดเครื่องเว้นแต่ได้รับคำสั่ง (เพื่อเก็บหน่วยความจำ)", "ปิดบัญชีที่ถูกยึดและยกเลิกเซสชันที่ใช้งานอยู่ และรีเซ็ตข้อมูลยืนยันตัวตนสิทธิ์ระดับสูงจากเครื่องที่สะอาด",
          "บล็อกตัวบ่งชี้ที่ทราบที่ไฟร์วอลล์ DNS และเกตเวย์อีเมล", "ปกป้องข้อมูลสำรอง: ยืนยันว่าสำเนาที่แก้ไขไม่ได้ยังสมบูรณ์ และตัดระบบสำรองข้อมูลออกจากเครือข่ายหากมีความเสี่ยง", "เปิดใช้ขั้นตอนการทำงานแบบไม่มีระบบ", "ประสานผู้ให้บริการรับมือเหตุตามสัญญาและเริ่มบันทึกพยานหลักฐาน"]},
   {"n": ["MSSP calls the Security Manager; Security Manager declares SEV-1 and calls the CEO and Medical Director.", "MSSP isolates affected servers through EDR; HIS database servers are isolated only after the Medical Director confirms downtime procedures are active.",
          "IT disables affected accounts and resets domain admin credentials from the PAM jump host.", "Network team blocks indicators; internet access restricted to essential clinical services.",
          "IT Infrastructure Manager confirms immutable HIS, PACS, and LIS backups are intact.", "Nursing supervisors activate paper downtime kits on all wards; Emergency Department considers ambulance diversion with the CEO.", "IR retainer engaged; on site within 4 hours."]}),
  ("Executive Decisions", "การตัดสินใจของผู้บริหาร", "List decisions reserved for executives with the criteria.", "ระบุการตัดสินใจที่สงวนไว้สำหรับผู้บริหารพร้อมเกณฑ์",
   {"t": ["Decision", "Decision maker", "Inputs"], "r": [
     ["Shut down a critical service or the whole network", "[CEO]", "Spread risk, safety, business impact"], ["Notify regulators and affected individuals", "[CEO] on advice of [DPO] and [LEGAL]", "RS-PRC-003 criteria"],
     ["Engage with threat actors or consider payment", "[CEO] and [BOARD] with [LEGAL]", "Legal and sanctions checks, backup status, law enforcement advice; payment does not guarantee recovery"],
     ["Public statement", "[CEO]", "Prepared by [COMMS] using RC-TPL-001"]], "w": [5.5, 4.5, 6.5]},
   {"t": ["การตัดสินใจ", "ผู้ตัดสินใจ", "ข้อมูลประกอบ"], "r": [
     ["หยุดบริการสำคัญหรือเครือข่ายทั้งหมด", "[CEO]", "ความเสี่ยงการแพร่กระจาย ความปลอดภัย ผลกระทบทางธุรกิจ"], ["แจ้งหน่วยงานกำกับและบุคคลที่ได้รับผลกระทบ", "[CEO] ตามคำแนะนำของ [DPO] และ [LEGAL]", "เกณฑ์ใน RS-PRC-003"],
     ["การติดต่อกับผู้โจมตีหรือการพิจารณาจ่ายค่าไถ่", "[CEO] และ [BOARD] ร่วมกับ [LEGAL]", "การตรวจสอบทางกฎหมายและมาตรการคว่ำบาตร สถานะข้อมูลสำรอง คำแนะนำของเจ้าหน้าที่ การจ่ายไม่รับประกันการกู้คืน"],
     ["การแถลงต่อสาธารณะ", "[CEO]", "จัดทำโดย [COMMS] ตาม RC-TPL-001"]], "w": [5.5, 4.5, 6.5]}),
  ("Recovery Conditions", "เงื่อนไขการกู้คืน", "State conditions before restoring systems.", "ระบุเงื่อนไขก่อนการกู้คืนระบบ",
   ["Initial access vector identified and closed.", "All privileged credentials reset, including service and backup accounts.", "Restore points verified clean in an isolated environment (PR-PRC-005).", "Recovery order follows the BIA priorities (RC-PLN-002)."],
   ["ระบุและปิดช่องทางการเข้าถึงครั้งแรกแล้ว", "รีเซ็ตข้อมูลยืนยันตัวตนสิทธิ์ระดับสูงทั้งหมด รวมถึงบัญชีบริการและบัญชีระบบสำรองข้อมูล", "ยืนยันว่าจุดกู้คืนสะอาดในสภาพแวดล้อมที่แยกไว้ (PR-PRC-005)", "ลำดับการกู้คืนเป็นไปตามลำดับความสำคัญใน BIA (RC-PLN-002)"]),
 ],
 bp=[("Rebuild identity infrastructure (domain controllers) from known-good media if compromise is suspected.", "สร้างโครงสร้างพื้นฐานด้านตัวตน (Domain controller) ใหม่จากสื่อที่ทราบว่าสะอาด หากสงสัยว่าถูกโจมตี"),
     ("Assume data was stolen before encryption; start breach assessment early.", "สันนิษฐานว่าข้อมูลถูกขโมยก่อนถูกเข้ารหัส และเริ่มประเมินเหตุละเมิดตั้งแต่เนิ่น ๆ")],
 mistakes=[("Restoring from backups before closing the entry point, leading to re-infection.", "กู้คืนจากข้อมูลสำรองก่อนปิดช่องทางเข้า ทำให้ติดมัลแวร์ซ้ำ")],
)

C["RS-PLB-002"] = dict(
 purpose=("This playbook gives specific actions for responding to phishing and business email compromise (BEC), including payment fraud attempts (RS.MI-01, RS.MI-02).",
          "คู่มือนี้กำหนดการดำเนินการเฉพาะในการรับมือฟิชชิ่งและการหลอกลวงทางอีเมลธุรกิจ (BEC) รวมถึงความพยายามฉ้อโกงการชำระเงิน (RS.MI-01, RS.MI-02)"),
 sections=[
  ("Response Steps", "ขั้นตอนการรับมือ", "List actions by scenario.", "ระบุการดำเนินการตามสถานการณ์",
   {"t": ["Scenario", "Actions"], "r": [
     ["Phishing reported, no click", "Search and remove the message from all mailboxes; block sender and URLs; thank the reporter"],
     ["User clicked or entered credentials", "Reset password, revoke sessions, review MFA methods, check sign-ins and mailbox rules for 30 days; scan the device"],
     ["Mailbox compromised (BEC)", "Contain the account; remove malicious forwarding rules; identify emails sent; warn recipients; check for data access"],
     ["Payment fraud attempt", "Contact the bank immediately to stop or recall the transfer; verify vendor details by phone; report to police; preserve evidence"]], "w": [4.5, 12.0]},
   {"t": ["สถานการณ์", "การดำเนินการ"], "r": [
     ["มีการรายงานฟิชชิ่ง แต่ไม่มีการคลิก", "ค้นหาและลบข้อความออกจากทุกกล่องจดหมาย บล็อกผู้ส่งและ URL และขอบคุณผู้รายงาน"],
     ["ผู้ใช้คลิกหรือกรอกรหัสผ่าน", "รีเซ็ตรหัสผ่าน ยกเลิกเซสชัน ตรวจสอบวิธี MFA ตรวจสอบการเข้าสู่ระบบและกฎกล่องจดหมายย้อนหลัง 30 วัน และสแกนเครื่อง"],
     ["กล่องจดหมายถูกยึด (BEC)", "ควบคุมบัญชี ลบกฎส่งต่ออีเมลที่เป็นอันตราย ระบุอีเมลที่ถูกส่งออก แจ้งเตือนผู้รับ และตรวจสอบการเข้าถึงข้อมูล"],
     ["ความพยายามฉ้อโกงการชำระเงิน", "ติดต่อธนาคารทันทีเพื่อระงับหรือเรียกคืนการโอน ตรวจสอบข้อมูลผู้ขายทางโทรศัพท์ แจ้งความ และเก็บรักษาพยานหลักฐาน"]], "w": [4.5, 12.0]},
   {"t": ["Scenario", "CMC actions (from INC-2026-014)"], "r": [
     ["Phishing reported, no click", "MSSP purges the message tenant-wide within 30 minutes; sender blocked"],
     ["User clicked or entered credentials", "Account reset, sessions revoked, MFA re-registered; MSSP reviews 30 days of sign-ins"],
     ["Mailbox compromised (BEC)", "June 2026: a procurement mailbox was accessed; forwarding rule to an external address removed within 2 hours; 14 vendors warned"],
     ["Payment fraud attempt", "Fake bank detail change request stopped by call-back verification (CAR-2026-011); bank and police informed"]], "w": [4.5, 12.0]}),
 ],
 bp=[("Enable a one-click report button and measure time from report to removal.", "เปิดใช้ปุ่มรายงานแบบคลิกเดียว และวัดระยะเวลาตั้งแต่รายงานจนถึงการลบข้อความ"),
     ("Require call-back verification for any change of bank details.", "กำหนดให้ยืนยันทางโทรศัพท์ทุกครั้งที่มีการเปลี่ยนข้อมูลบัญชีธนาคาร")],
 mistakes=[("Only resetting the password without checking mailbox rules and MFA registrations added by the attacker.", "รีเซ็ตรหัสผ่านอย่างเดียวโดยไม่ตรวจสอบกฎกล่องจดหมายและการลงทะเบียน MFA ที่ผู้โจมตีเพิ่มไว้")],
)

C["RS-PLB-003"] = dict(
 purpose=("This playbook guides the assessment and handling of personal data breaches, including the decision and timeline to notify the Personal Data Protection Committee (PDPC) and data subjects under PDPA s.37(4).",
          "คู่มือนี้เป็นแนวทางการประเมินและจัดการเหตุละเมิดข้อมูลส่วนบุคคล รวมถึงการตัดสินใจและกรอบเวลาในการแจ้งคณะกรรมการคุ้มครองข้อมูลส่วนบุคคล (สคส.) และเจ้าของข้อมูลตาม PDPA มาตรา 37(4)"),
 sections=[
  ("Breach Assessment", "การประเมินเหตุละเมิด", "Define how to assess whether a breach is notifiable.", "กำหนดวิธีประเมินว่าเหตุละเมิดต้องแจ้งหรือไม่",
   {"t": ["Question", "Consideration"], "r": [
     ["Is personal data involved?", "Any information that identifies a person directly or indirectly"], ["What type of breach?", "Confidentiality (disclosure), integrity (alteration), availability (loss or destruction)"],
     ["What data and how many people?", "Sensitive data under PDPA s.26 increases risk"], ["Is there risk to rights and freedoms?", "If no risk, notification to the PDPC is not required, but record the decision"],
     ["Is the risk high?", "If high, notify affected data subjects without delay together with remedies"]], "w": [5.5, 11.0]},
   {"t": ["คำถาม", "ข้อพิจารณา"], "r": [
     ["มีข้อมูลส่วนบุคคลเกี่ยวข้องหรือไม่", "ข้อมูลใดที่ระบุตัวบุคคลได้ทั้งทางตรงและทางอ้อม"], ["เป็นการละเมิดประเภทใด", "ความลับ (การเปิดเผย) ความถูกต้อง (การแก้ไข) ความพร้อมใช้งาน (การสูญหายหรือถูกทำลาย)"],
     ["ข้อมูลประเภทใดและกี่คน", "ข้อมูลอ่อนไหวตาม PDPA มาตรา 26 เพิ่มระดับความเสี่ยง"], ["มีความเสี่ยงต่อสิทธิและเสรีภาพหรือไม่", "หากไม่มีความเสี่ยง ไม่ต้องแจ้ง สคส. แต่ต้องบันทึกการตัดสินใจ"],
     ["ความเสี่ยงสูงหรือไม่", "หากสูง ต้องแจ้งเจ้าของข้อมูลที่ได้รับผลกระทบโดยไม่ชักช้า พร้อมแนวทางเยียวยา"]], "w": [5.5, 11.0]}),
  ("Notification Timeline", "กรอบเวลาการแจ้ง", "State the legal deadlines and internal targets.", "ระบุกำหนดเวลาตามกฎหมายและเป้าหมายภายใน",
   {"t": ["Milestone", "Target"], "r": [
     ["Breach detected and reported to [DPO]", "Immediately"], ["Initial assessment and containment", "Within 24 hours"],
     ["Notify the PDPC (if risk to rights and freedoms)", "Without delay and within 72 hours of becoming aware, where feasible (PDPA s.37(4))"],
     ["Notify data subjects (if high risk)", "Without delay"], ["Record the breach and decision", "In all cases, in RS-REG-001"]], "w": [8.0, 8.5]},
   {"t": ["จุดสำคัญ", "เป้าหมาย"], "r": [
     ["ตรวจพบเหตุละเมิดและรายงาน [DPO]", "ทันที"], ["ประเมินเบื้องต้นและควบคุมเหตุ", "ภายใน 24 ชั่วโมง"],
     ["แจ้ง สคส. (หากมีความเสี่ยงต่อสิทธิและเสรีภาพ)", "โดยไม่ชักช้าและภายใน 72 ชั่วโมงนับแต่ทราบเหตุเท่าที่จะทำได้ (PDPA มาตรา 37(4))"],
     ["แจ้งเจ้าของข้อมูล (หากมีความเสี่ยงสูง)", "โดยไม่ชักช้า"], ["บันทึกเหตุละเมิดและการตัดสินใจ", "ทุกกรณี ใน RS-REG-001"]], "w": [8.0, 8.5]}),
  ("Notification Content", "เนื้อหาการแจ้ง", "List the minimum content of notifications. [VERIFY against the current PDPC notification on breach notification criteria.]", "ระบุเนื้อหาขั้นต่ำของการแจ้ง [VERIFY กับประกาศ สคส. เรื่องหลักเกณฑ์การแจ้งเหตุละเมิดฉบับปัจจุบัน]",
   ["Nature of the breach and categories and approximate number of data subjects and records.", "Contact details of the DPO or contact person.", "Likely consequences.", "Measures taken or proposed to address the breach and reduce harm.", "Use the templates in RS-TPL-002."],
   ["ลักษณะของเหตุละเมิด ประเภทและจำนวนโดยประมาณของเจ้าของข้อมูลและรายการข้อมูล", "ข้อมูลติดต่อของ DPO หรือผู้ประสานงาน", "ผลกระทบที่อาจเกิดขึ้น", "มาตรการที่ดำเนินการแล้วหรือจะดำเนินการเพื่อแก้ไขและลดความเสียหาย", "ใช้แม่แบบใน RS-TPL-002"]),
 ],
 bp=[("Start the 72-hour clock at awareness and document when awareness occurred.", "เริ่มนับ 72 ชั่วโมงตั้งแต่ทราบเหตุ และบันทึกเวลาที่ทราบเหตุ"),
     ("Notify in phases if full facts are not yet available, rather than waiting.", "แจ้งเป็นระยะหากยังไม่มีข้อเท็จจริงครบถ้วน แทนการรอ"),
     ("Coordinate PDPA notification with CII reporting so messages are consistent.", "ประสานการแจ้งตาม PDPA กับการรายงานของ CII ให้ข้อความสอดคล้องกัน")],
 mistakes=[("Waiting for the forensic report before assessing notification, missing the 72-hour window.", "รอรายงานนิติวิทยาศาสตร์ดิจิทัลก่อนประเมินการแจ้ง ทำให้เกินกรอบ 72 ชั่วโมง")],
)

C["RS-PLB-004"] = dict(
 purpose=("This playbook gives specific actions for responding to a compromised user, privileged, service, or cloud account (RS.MI-01, RS.MI-02).",
          "คู่มือนี้กำหนดการดำเนินการเฉพาะในการรับมือเมื่อบัญชีผู้ใช้ บัญชีสิทธิ์ระดับสูง บัญชีบริการ หรือบัญชีคลาวด์ถูกยึด (RS.MI-01, RS.MI-02)"),
 sections=[
  ("Response Steps", "ขั้นตอนการรับมือ", "List actions in order.", "ระบุการดำเนินการตามลำดับ",
   {"n": ["Confirm compromise signals (impossible travel, MFA fatigue approvals, unusual access).", "Disable the account or force sign-out and revoke tokens.", "Reset the password and re-register MFA after verifying the user's identity out of band.",
          "Review activity: sign-ins, mailbox rules, file access, privilege changes, new devices or app consents.", "For privileged accounts: escalate to SEV-2 or higher; review all systems the account touched.",
          "For service accounts: rotate secrets and update dependent systems through emergency change.", "Restore access after the device and account are confirmed clean."]},
   {"n": ["ยืนยันสัญญาณการถูกยึดบัญชี (การเข้าสู่ระบบจากตำแหน่งที่เป็นไปไม่ได้ การกดอนุมัติ MFA ที่ผิดปกติ การเข้าถึงที่ผิดปกติ)", "ปิดบัญชีหรือบังคับออกจากระบบและยกเลิก Token", "รีเซ็ตรหัสผ่านและลงทะเบียน MFA ใหม่หลังยืนยันตัวตนผู้ใช้ผ่านช่องทางอื่น",
          "ตรวจสอบกิจกรรม ได้แก่ การเข้าสู่ระบบ กฎกล่องจดหมาย การเข้าถึงไฟล์ การเปลี่ยนแปลงสิทธิ์ อุปกรณ์ใหม่ หรือการให้สิทธิ์แอปพลิเคชัน", "สำหรับบัญชีสิทธิ์ระดับสูง: ยกระดับเป็น SEV-2 ขึ้นไป และตรวจสอบทุกระบบที่บัญชีเข้าถึง",
          "สำหรับบัญชีบริการ: เปลี่ยนรหัสลับและปรับปรุงระบบที่เกี่ยวข้องผ่านการเปลี่ยนแปลงฉุกเฉิน", "คืนสิทธิ์การเข้าถึงหลังยืนยันว่าเครื่องและบัญชีสะอาดแล้ว"]}),
 ],
 bp=[("Investigate how credentials were stolen (phishing, malware, reuse) and fix the cause.", "สอบสวนว่าข้อมูลยืนยันตัวตนถูกขโมยอย่างไร (ฟิชชิ่ง มัลแวร์ การใช้รหัสผ่านซ้ำ) และแก้ไขที่ต้นเหตุ")],
 mistakes=[("Resetting the password but leaving attacker-registered MFA methods in place.", "รีเซ็ตรหัสผ่านแต่ยังคงวิธี MFA ที่ผู้โจมตีลงทะเบียนไว้")],
)

C["RS-FRM-001"] = dict(
 purpose=("This form captures the initial report of a suspected security incident from staff or monitoring, so it can be triaged quickly (RS.MA-02).",
          "แบบฟอร์มนี้ใช้รับรายงานเบื้องต้นของเหตุการณ์ที่สงสัยว่าเป็นเหตุการณ์ด้านความมั่นคงปลอดภัยจากบุคลากรหรือระบบเฝ้าระวัง เพื่อให้คัดกรองได้อย่างรวดเร็ว (RS.MA-02)"),
 fields=[
  ("Reporter name and contact", "ชื่อและช่องทางติดต่อผู้รายงาน", "Who is reporting.", "ผู้รายงาน", ""),
  ("Date and time noticed", "วันและเวลาที่พบ", "When it was first seen.", "เวลาที่พบครั้งแรก", ""),
  ("What happened", "สิ่งที่เกิดขึ้น", "Plain description.", "คำอธิบายง่าย ๆ", ""),
  ("Systems, devices, or accounts involved", "ระบบ อุปกรณ์ หรือบัญชีที่เกี่ยวข้อง", "Names or IDs.", "ชื่อหรือรหัส", ""),
  ("Data possibly affected", "ข้อมูลที่อาจได้รับผลกระทบ", "Type of data, personal data involved?", "ประเภทข้อมูล มีข้อมูลส่วนบุคคลหรือไม่", ""),
  ("Actions already taken", "การดำเนินการที่ทำไปแล้ว", "For example, disconnected cable.", "เช่น ถอดสายเครือข่าย", ""),
  ("Business impact", "ผลกระทบทางธุรกิจ", "Services affected.", "บริการที่ได้รับผลกระทบ", ""),
  ("Received by and incident number", "ผู้รับเรื่องและเลขที่เหตุการณ์", "Completed by security team.", "กรอกโดยทีมความมั่นคงปลอดภัย", ""),
 ],
 cmc_vals=["Ward 6B nurse (name withheld in sample), ext. 6612", "18 June 2026, 10:05", "A pop-up asked to enter Microsoft 365 password again after opening an email about a shift swap; nurse entered the password",
           "Nurse account; Ward 6B workstation WS-W6B-03", "Possibly email containing patient handover notes", "Reported to the service desk; did not unplug the workstation",
           "None observed", "Service desk; INC-2026-016 (linked to phishing campaign INC-2026-014)"],
 approvals=["Reviewer"],
 bp=[("Accept reports by phone, email, and form; speed matters more than format.", "รับรายงานทางโทรศัพท์ อีเมล และแบบฟอร์ม เพราะความเร็วสำคัญกว่ารูปแบบ")],
 mistakes=[("Requiring a complete form before acting on an urgent report.", "บังคับให้กรอกแบบฟอร์มครบถ้วนก่อนดำเนินการกับรายงานเร่งด่วน")],
)

C["RS-REG-001"] = dict(
 purpose=("This register records every security incident, its category, severity, timeline, impact, notifications, root cause, and status, for tracking, reporting, and trend analysis (RS.MA, RS.AN).",
          "ทะเบียนนี้บันทึกเหตุการณ์ด้านความมั่นคงปลอดภัยทุกรายการ พร้อมประเภท ระดับความรุนแรง ลำดับเวลา ผลกระทบ การแจ้งเหตุ สาเหตุที่แท้จริง และสถานะ เพื่อการติดตาม การรายงาน และการวิเคราะห์แนวโน้ม (RS.MA, RS.AN)"),
 fields=[
  ("Incident ID", "รหัสเหตุการณ์", "Unique reference.", "รหัสอ้างอิง", "INC-2026-001"),
  ("Detected and declared", "เวลาที่ตรวจพบและประกาศ", "Date and time.", "วันและเวลา", ""),
  ("Category and severity", "ประเภทและระดับความรุนแรง", "Per DE-STD-002.", "ตาม DE-STD-002", ""),
  ("Summary", "สรุป", "What happened.", "สิ่งที่เกิดขึ้น", ""),
  ("Impact and data affected", "ผลกระทบและข้อมูลที่ได้รับผลกระทบ", "Services, records, people.", "บริการ รายการข้อมูล บุคคล", ""),
  ("Notifications", "การแจ้งเหตุ", "PDPC, NCSA, regulator, data subjects, with dates.", "สคส. สกมช. หน่วยงานกำกับ เจ้าของข้อมูล พร้อมวันที่", ""),
  ("Root cause", "สาเหตุที่แท้จริง", "From investigation.", "จากการสอบสวน", ""),
  ("Status and closed date", "สถานะและวันที่ปิด", "Open, Recovering, Closed.", "เปิด อยู่ระหว่างกู้คืน ปิด", ""),
 ],
 rows=[
  ["INC-2026-014", "16/06/2026 14:20; declared 14:35", "BEC, SEV-2", "Procurement mailbox accessed via phished credentials; forwarding rule created; fake bank change request sent to finance", "One mailbox; no payment made; vendor contact data exposed", "PDPC: not notified (assessed no risk to rights; record kept); NCSA: not significant", "Phishing with MFA fatigue approval", "Closed 30/06/2026"],
  ["INC-2026-016", "18/06/2026 10:05", "Phishing, SEV-3", "Nurse entered password on phishing page from same campaign", "One account; no access found", "None required", "Phishing", "Closed 19/06/2026"],
  ["INC-2026-021", "12/08/2026 09:40", "Third-party access, SEV-2", "Unapproved vendor remote support agent found active on two modality workstations", "No malicious use found", "None required", "Vendor installed tool outside contract", "Closed 22/08/2026"],
  ["INC-2026-027", "03/09/2026 23:10", "Malware, SEV-3", "EDR blocked info-stealer on an office laptop", "None", "None required", "Malicious download", "Closed 04/09/2026"],
 ],
 bp=[("Record near misses and SEV-4 events as well; trends show where controls need work.", "บันทึกเหตุการณ์เกือบเกิดและเหตุการณ์ SEV-4 ด้วย เพราะแนวโน้มแสดงจุดที่มาตรการต้องปรับปรุง"),
     ("Record the reasoning for each notification decision, including decisions not to notify.", "บันทึกเหตุผลของการตัดสินใจแจ้งเหตุทุกครั้ง รวมถึงการตัดสินใจไม่แจ้ง")],
 mistakes=[("Incidents tracked only in chat messages with no central record.", "ติดตามเหตุการณ์ผ่านข้อความแชตเท่านั้นโดยไม่มีบันทึกกลาง")],
)

C["RS-REG-002"] = dict(
 purpose=("This list holds the contact details of everyone needed during an incident, internal and external, including regulator and supplier contacts, so the team can reach them at any time (RS.MA-01, RS.CO-02; CSA s.46 and s.52).",
          "รายชื่อนี้เก็บข้อมูลติดต่อของทุกคนที่จำเป็นระหว่างเหตุการณ์ ทั้งภายในและภายนอก รวมถึงหน่วยงานกำกับและผู้ให้บริการ เพื่อให้ทีมติดต่อได้ตลอดเวลา (RS.MA-01, RS.CO-02; พ.ร.บ.ไซเบอร์ฯ มาตรา 46 และ 52)"),
 fields=[
  ("Role", "บทบาท", "Response role.", "บทบาทในการรับมือ", ""),
  ("Name and position", "ชื่อและตำแหน่ง", "Primary contact.", "ผู้ติดต่อหลัก", ""),
  ("Primary phone", "โทรศัพท์หลัก", "24x7 number.", "หมายเลข 24 ชั่วโมง", ""),
  ("Alternate contact", "ผู้ติดต่อสำรอง", "Deputy.", "ผู้แทน", ""),
  ("Out-of-band channel", "ช่องทางสำรอง", "Messaging group or personal email.", "กลุ่มส่งข้อความหรืออีเมลส่วนตัว", ""),
  ("Last verified", "ตรวจสอบล่าสุด", "Date tested.", "วันที่ทดสอบ", ""),
 ],
 rows=[
  ["Incident Commander", "Security Manager", "08x-xxx-xxxx", "IT Infrastructure Manager", "CMC IR Signal group", "01/10/2026"],
  ["Executive sponsor", "CEO", "08x-xxx-xxxx", "CIO", "CMC IR Signal group", "01/10/2026"],
  ["Clinical liaison", "Medical Director", "08x-xxx-xxxx", "Nursing supervisor on duty (switchboard)", "Switchboard", "01/10/2026"],
  ["Privacy lead", "DPO", "08x-xxx-xxxx", "Legal Counsel", "CMC IR Signal group", "01/10/2026"],
  ["MSSP SOC", "MSSP Vendor E duty manager", "02-xxx-xxxx (24x7)", "MSSP account manager", "Portal and phone", "01/10/2026"],
  ["HIS Vendor A", "Critical support line", "02-xxx-xxxx (24x7)", "Account manager", "Email", "01/10/2026"],
  ["NCSA", "Incident reporting channel [VERIFY current channel]", "As published by NCSA", "ThaiCERT", "Official portal", "01/10/2026"],
  ["PDPC Office", "Breach notification channel [VERIFY current channel]", "As published by PDPC", "Not applicable", "Official e-service", "01/10/2026"],
 ],
 cmc_note="Phone numbers are masked in this sample. The live list is kept in the incident response binder (printed), the out-of-band channel, and the Security Manager's offline device.",
 bp=[("Test contacts quarterly with a short call-tree exercise.", "ทดสอบรายชื่อผู้ติดต่อทุกไตรมาสด้วยการซ้อมโทรต่อเนื่องแบบสั้น"),
     ("Keep printed and offline copies; the directory may be down during an incident.", "เก็บสำเนาแบบพิมพ์และแบบออฟไลน์ เพราะระบบรายชื่ออาจใช้งานไม่ได้ระหว่างเหตุการณ์")],
 mistakes=[("Contact list contains former staff and switchboard numbers that do not work after hours.", "รายชื่อมีบุคลากรที่ลาออกแล้วและหมายเลขโอเปอเรเตอร์ที่ใช้ไม่ได้นอกเวลาทำการ")],
)

C["RS-PRC-002"] = dict(
 purpose=("This procedure defines how digital evidence is identified, collected, preserved, analyzed, and documented so that findings are reliable and usable for legal, regulatory, or disciplinary purposes (RS.AN-03, RS.AN-06, RS.AN-07, RS.AN-08; ISO/IEC 27037).",
          "ระเบียบปฏิบัตินี้กำหนดวิธีระบุ เก็บรวบรวม เก็บรักษา วิเคราะห์ และบันทึกพยานหลักฐานดิจิทัล เพื่อให้ผลการตรวจสอบน่าเชื่อถือและใช้ได้ในทางกฎหมาย การกำกับดูแล หรือการลงโทษทางวินัย (RS.AN-03, RS.AN-06, RS.AN-07, RS.AN-08; ISO/IEC 27037)"),
 sections=[
  ("Evidence Handling Principles", "หลักการจัดการพยานหลักฐาน", "State core principles.", "ระบุหลักการสำคัญ",
   ["Collect the most volatile evidence first (memory, network connections, running processes), then disks and logs.", "Work on forensic copies; record hash values (SHA-256) of originals and copies.",
    "Record every action with time, person, and tool (RS.AN-06).", "Maintain chain of custody for physical and digital evidence (RS-FRM-002).", "Store evidence in a secure location with restricted access.", "Engage qualified forensic specialists for incidents likely to involve legal action."],
   ["เก็บพยานหลักฐานที่สูญหายง่ายที่สุดก่อน (หน่วยความจำ การเชื่อมต่อเครือข่าย Process ที่ทำงานอยู่) แล้วจึงเก็บดิสก์และ Log", "ทำงานกับสำเนาทางนิติวิทยาศาสตร์ และบันทึกค่าแฮช (SHA-256) ของต้นฉบับและสำเนา",
    "บันทึกทุกการดำเนินการพร้อมเวลา ผู้ดำเนินการ และเครื่องมือ (RS.AN-06)", "รักษาสายการครอบครองพยานหลักฐานทั้งทางกายภาพและดิจิทัล (RS-FRM-002)", "จัดเก็บพยานหลักฐานในสถานที่ปลอดภัยที่จำกัดการเข้าถึง", "ใช้ผู้เชี่ยวชาญด้านนิติวิทยาศาสตร์ดิจิทัลที่มีคุณสมบัติสำหรับเหตุการณ์ที่อาจมีการดำเนินคดี"]),
  ("Analysis Outputs", "ผลลัพธ์จากการวิเคราะห์", "Define what the investigation must establish.", "กำหนดสิ่งที่การสอบสวนต้องระบุให้ได้",
   ["Timeline of attacker activity.", "Initial access vector and root cause (RS.AN-03).", "Systems, accounts, and data affected; magnitude estimate validated (RS.AN-08).", "Indicators of compromise for detection and sharing.", "Report using RS-TPL-001."],
   ["ลำดับเวลากิจกรรมของผู้โจมตี", "ช่องทางการเข้าถึงครั้งแรกและสาเหตุที่แท้จริง (RS.AN-03)", "ระบบ บัญชี และข้อมูลที่ได้รับผลกระทบ และการยืนยันขนาดของผลกระทบ (RS.AN-08)", "ตัวบ่งชี้การถูกโจมตีเพื่อใช้ตรวจจับและแบ่งปัน", "รายงานโดยใช้ RS-TPL-001"]),
 ],
 bp=[("Prepare a forensic toolkit and evidence storage before incidents happen.", "จัดเตรียมชุดเครื่องมือนิติวิทยาศาสตร์ดิจิทัลและพื้นที่จัดเก็บพยานหลักฐานก่อนเกิดเหตุการณ์"),
     ("Agree with the IR retainer how evidence will be handed over and stored.", "ตกลงกับผู้ให้บริการรับมือเหตุตามสัญญาเรื่องวิธีส่งมอบและจัดเก็บพยานหลักฐาน")],
 mistakes=[("Administrators browse an infected server to 'have a look', overwriting evidence.", "ผู้ดูแลระบบเข้าไปตรวจดูเซิร์ฟเวอร์ที่ติดมัลแวร์เอง ทำให้พยานหลักฐานถูกเขียนทับ")],
)

C["RS-FRM-002"] = dict(
 purpose=("This form records every transfer of evidence, preserving its integrity and provenance (RS.AN-06, RS.AN-07).",
          "แบบฟอร์มนี้บันทึกการส่งมอบพยานหลักฐานทุกครั้ง เพื่อรักษาความถูกต้องครบถ้วนและแหล่งที่มาของพยานหลักฐาน (RS.AN-06, RS.AN-07)"),
 fields=[
  ("Evidence ID and incident ID", "รหัสพยานหลักฐานและรหัสเหตุการณ์", "Unique references.", "รหัสอ้างอิง", "EV-2026-001 / INC-2026-001"),
  ("Description", "คำอธิบาย", "Item, serial number, or image file.", "รายการ หมายเลขเครื่อง หรือไฟล์อิมเมจ", ""),
  ("Collected by, date, time, location", "ผู้เก็บ วัน เวลา สถานที่", "Collection details.", "รายละเอียดการเก็บ", ""),
  ("Collection method and tool", "วิธีการและเครื่องมือที่ใช้เก็บ", "For example, write blocker, memory capture tool.", "เช่น Write blocker เครื่องมือเก็บหน่วยความจำ", ""),
  ("Hash value (SHA-256)", "ค่าแฮช (SHA-256)", "Of original or image.", "ของต้นฉบับหรืออิมเมจ", ""),
  ("Transfer log", "บันทึกการส่งมอบ", "Released by, received by, date, time, purpose for each transfer.", "ผู้ส่ง ผู้รับ วัน เวลา วัตถุประสงค์ของการส่งมอบแต่ละครั้ง", ""),
  ("Storage location", "สถานที่จัดเก็บ", "Secure storage.", "พื้นที่จัดเก็บที่ปลอดภัย", ""),
 ],
 cmc_vals=["EV-2026-009 / INC-2026-021", "Disk image of modality workstation MED-IMG-002 (CT-02) and remote support agent logs", "Security Engineer, 12 August 2026, 14:30, Riverside Radiology",
           "Forensic imaging tool with hardware write blocker; workstation taken offline with Radiology approval", "SHA-256 recorded in case file (value withheld in sample)",
           "Released by Security Engineer to IR retainer analyst, 13 August 2026 09:00, for analysis; returned 20 August 2026 16:00", "Locked evidence cabinet, Security Office, Riverside"],
 approvals=["Reviewer", "CISO"],
 bp=[("Verify hash values at every transfer.", "ตรวจสอบค่าแฮชทุกครั้งที่ส่งมอบ")],
 mistakes=[("Gaps in the transfer log, which weakens evidence in legal proceedings.", "บันทึกการส่งมอบไม่ต่อเนื่อง ทำให้พยานหลักฐานมีน้ำหนักน้อยลงในการดำเนินคดี")],
)

C["RS-TPL-001"] = dict(
 purpose=("This template structures the final report of an incident investigation, including timeline, root cause, impact, actions, and lessons, for management and regulators (RS.AN-03, RS.AN-08).",
          "แม่แบบนี้กำหนดโครงสร้างรายงานผลการสอบสวนเหตุการณ์ ได้แก่ ลำดับเวลา สาเหตุที่แท้จริง ผลกระทบ การดำเนินการ และบทเรียน สำหรับผู้บริหารและหน่วยงานกำกับดูแล (RS.AN-03, RS.AN-08)"),
 sections=[
  ("Report Structure", "โครงสร้างรายงาน", "Include the minimum report sections.", "ระบุหัวข้อขั้นต่ำของรายงาน",
   {"t": ["Section", "Content"], "r": [
     ["1. Executive summary", "What happened, impact, current status, key decisions (half a page)"], ["2. Timeline", "Detection, declaration, containment, eradication, recovery, notifications"],
     ["3. Root cause and attack path", "Initial access, actions on systems, why controls did not stop it"], ["4. Impact", "Systems, downtime, data and people affected, cost estimate"],
     ["5. Notifications", "Regulators and individuals notified, with dates and references"], ["6. Actions taken", "Containment, eradication, recovery steps"],
     ["7. Recommendations", "Control improvements with owners, linked to ID-REG-007"], ["8. Evidence references", "Evidence IDs and analyst notes"]], "w": [5.0, 11.5]},
   {"t": ["หัวข้อ", "เนื้อหา"], "r": [
     ["1. บทสรุปผู้บริหาร", "สิ่งที่เกิดขึ้น ผลกระทบ สถานะปัจจุบัน การตัดสินใจสำคัญ (ครึ่งหน้า)"], ["2. ลำดับเวลา", "การตรวจพบ การประกาศ การควบคุม การกำจัด การกู้คืน การแจ้งเหตุ"],
     ["3. สาเหตุที่แท้จริงและเส้นทางการโจมตี", "การเข้าถึงครั้งแรก การดำเนินการบนระบบ และเหตุผลที่มาตรการควบคุมหยุดไม่ได้"], ["4. ผลกระทบ", "ระบบ ระยะเวลาหยุดชะงัก ข้อมูลและบุคคลที่ได้รับผลกระทบ ประมาณการต้นทุน"],
     ["5. การแจ้งเหตุ", "หน่วยงานกำกับและบุคคลที่ได้รับแจ้ง พร้อมวันที่และเลขอ้างอิง"], ["6. การดำเนินการที่ทำไปแล้ว", "ขั้นตอนการควบคุม การกำจัด และการกู้คืน"],
     ["7. ข้อเสนอแนะ", "การปรับปรุงมาตรการพร้อมผู้รับผิดชอบ เชื่อมโยงกับ ID-REG-007"], ["8. การอ้างอิงพยานหลักฐาน", "รหัสพยานหลักฐานและบันทึกของนักวิเคราะห์"]], "w": [5.0, 11.5]},
   {"t": ["Section", "Example from INC-2026-014"], "r": [
     ["1. Executive summary", "A procurement mailbox was compromised for 2 hours via phishing and MFA fatigue; a fraudulent bank change request was stopped; no payment loss; no notifiable breach."],
     ["2. Timeline", "16 June 13:58 phishing click; 14:05 MFA approved; 14:20 MSSP alert; 14:35 declared SEV-2; 16:10 contained; 30 June closed."],
     ["3. Root cause", "User approved an unexpected MFA prompt; push-notification MFA without number matching."],
     ["4. Impact", "One mailbox; vendor contact details viewed; 14 vendors warned."],
     ["5. Notifications", "PDPC: assessed not required (no risk to rights); decision recorded. NCSA: not significant."],
     ["6. Actions taken", "Account reset, rule removed, sessions revoked, tenant-wide purge."],
     ["7. Recommendations", "Number matching for MFA (done 07/2026); call-back verification for bank changes (CAR-2026-011)."],
     ["8. Evidence references", "EV-2026-006 (mailbox audit export)"]], "w": [5.0, 11.5]}),
 ],
 bp=[("Write the executive summary for a non-technical reader and put technical detail in annexes.", "เขียนบทสรุปผู้บริหารสำหรับผู้อ่านที่ไม่ใช่สายเทคนิค และใส่รายละเอียดทางเทคนิคในภาคผนวก")],
 mistakes=[("Reports blame individuals instead of explaining control failures.", "รายงานกล่าวโทษบุคคลแทนการอธิบายความล้มเหลวของมาตรการควบคุม")],
)

C["RS-PRC-003"] = dict(
 purpose=("This procedure defines who must be notified about an incident, by whom, within what timeframe, and through which channel, covering internal stakeholders, the PDPC, NCSA, sector regulators, data subjects, and partners (RS.CO-02, RS.CO-03).",
          "ระเบียบปฏิบัตินี้กำหนดผู้ที่ต้องได้รับแจ้งเกี่ยวกับเหตุการณ์ ผู้แจ้ง กรอบเวลา และช่องทาง ครอบคลุมผู้มีส่วนได้ส่วนเสียภายใน สคส. สกมช. หน่วยงานกำกับดูแลภาคส่วน เจ้าของข้อมูล และคู่ค้า (RS.CO-02, RS.CO-03)"),
 sections=[
  ("Notification Matrix", "ตารางการแจ้งเหตุ", "List each audience with trigger, deadline, owner, and channel.", "ระบุผู้รับแจ้งแต่ละกลุ่มพร้อมเงื่อนไข กำหนดเวลา ผู้รับผิดชอบ และช่องทาง",
   {"t": ["Audience", "Trigger", "Deadline", "Owner", "Channel"], "r": [
     ["[CEO] and executives", "SEV-1 or SEV-2", "1 to 2 hours", "[CISO]", "Phone"],
     ["PDPC", "Personal data breach with risk to rights and freedoms", "Within 72 hours of awareness (PDPA s.37(4))", "[DPO]", "PDPC e-service [VERIFY]"],
     ["Affected data subjects", "High risk to rights and freedoms", "Without delay", "[DPO]", "Letter, email, SMS"],
     ["NCSA and sector regulator", "Significant cyber incident at a CII organization", "Per CRC Notification 2024, reported as 24 hours [VERIFY]", "[CISO]", "NCSA channel [VERIFY]"],
     ["Customers and partners", "Their data or services affected, or contract requires", "Per contract", "Business owner, [LEGAL]", "Formal letter"],
     ["Insurer", "Policy notice condition", "Per policy", "[CFO]", "Per policy"],
     ["Police", "Crime suspected", "As advised by [LEGAL]", "[LEGAL]", "Police report"]]},
   {"t": ["ผู้รับแจ้ง", "เงื่อนไข", "กำหนดเวลา", "ผู้รับผิดชอบ", "ช่องทาง"], "r": [
     ["[CEO] และผู้บริหาร", "SEV-1 หรือ SEV-2", "1 ถึง 2 ชั่วโมง", "[CISO]", "โทรศัพท์"],
     ["สคส.", "เหตุละเมิดข้อมูลส่วนบุคคลที่มีความเสี่ยงต่อสิทธิและเสรีภาพ", "ภายใน 72 ชั่วโมงนับแต่ทราบเหตุ (PDPA มาตรา 37(4))", "[DPO]", "ระบบ e-service ของ สคส. [VERIFY]"],
     ["เจ้าของข้อมูลที่ได้รับผลกระทบ", "มีความเสี่ยงสูงต่อสิทธิและเสรีภาพ", "โดยไม่ชักช้า", "[DPO]", "จดหมาย อีเมล SMS"],
     ["สกมช. และหน่วยงานกำกับดูแล", "เหตุการณ์ไซเบอร์ที่มีนัยสำคัญของ CII", "ตามประกาศ กกม. 2567 ซึ่งกำหนดไว้ 24 ชั่วโมง [VERIFY]", "[CISO]", "ช่องทางของ สกมช. [VERIFY]"],
     ["ลูกค้าและคู่ค้า", "ข้อมูลหรือบริการของคู่ค้าได้รับผลกระทบ หรือสัญญากำหนด", "ตามสัญญา", "เจ้าของธุรกิจ [LEGAL]", "หนังสือแจ้งอย่างเป็นทางการ"],
     ["บริษัทประกันภัย", "เงื่อนไขการแจ้งตามกรมธรรม์", "ตามกรมธรรม์", "[CFO]", "ตามกรมธรรม์"],
     ["ตำรวจ", "สงสัยว่ามีการกระทำความผิด", "ตามคำแนะนำของ [LEGAL]", "[LEGAL]", "แจ้งความ"]]}),
  ("Approval of External Messages", "การอนุมัติข้อความที่สื่อสารภายนอก", "Define who approves external messages.", "กำหนดผู้อนุมัติข้อความที่สื่อสารภายนอก",
   "Regulatory notifications are prepared by the [DPO] or [CISO], reviewed by [LEGAL], and approved by the [CEO] or delegate. Public statements follow the Crisis Communication Procedure (RC-PRC-002). Night and weekend approval follows the delegation in RS-PLN-001.",
   "การแจ้งหน่วยงานกำกับจัดทำโดย [DPO] หรือ [CISO] ทบทวนโดย [LEGAL] และอนุมัติโดย [CEO] หรือผู้ได้รับมอบหมาย การแถลงต่อสาธารณะเป็นไปตามระเบียบปฏิบัติการสื่อสารในภาวะวิกฤต (RC-PRC-002) การอนุมัตินอกเวลาทำการเป็นไปตามการมอบอำนาจใน RS-PLN-001"),
 ],
 bp=[("Pre-register with regulator portals and keep credentials available offline.", "ลงทะเบียนระบบของหน่วยงานกำกับไว้ล่วงหน้า และเก็บข้อมูลเข้าสู่ระบบไว้แบบออฟไลน์"),
     ("Keep notifications factual and update them as the investigation progresses.", "แจ้งเฉพาะข้อเท็จจริง และปรับปรุงข้อมูลตามความคืบหน้าของการสอบสวน")],
 mistakes=[("Different teams send inconsistent messages to the PDPC and NCSA.", "ทีมต่างกันส่งข้อความที่ไม่สอดคล้องกันไปยัง สคส. และ สกมช.")],
 rev="Updated in March 2026 after EX-2026-01 to add night-time approval delegation; regulator portal access for the CII channel pending (GV-REG-006, CII-05).",
)

C["RS-TPL-002"] = dict(
 purpose=("These templates provide pre-approved text for notifying the PDPC, NCSA or sector regulators, and affected individuals, so notifications are complete and fast.",
          "แม่แบบนี้มีข้อความที่อนุมัติไว้ล่วงหน้าสำหรับการแจ้ง สคส. สกมช. หรือหน่วยงานกำกับดูแลภาคส่วน และบุคคลที่ได้รับผลกระทบ เพื่อให้การแจ้งครบถ้วนและรวดเร็ว"),
 sections=[
  ("PDPC Breach Notification", "การแจ้งเหตุละเมิดต่อ สคส.", "Provide fields required for PDPC notification. [VERIFY against the current PDPC notification and e-service form.]", "ระบุข้อมูลที่ต้องใช้ในการแจ้ง สคส. [VERIFY กับประกาศและแบบฟอร์ม e-service ของ สคส. ฉบับปัจจุบัน]",
   {"t": ["Field", "Content"], "r": [["Controller and DPO contact", ""], ["Date and time of breach and of awareness", ""], ["Nature of breach", ""], ["Categories and approximate number of data subjects and records", ""], ["Likely consequences", ""], ["Measures taken and planned", ""], ["Whether data subjects were or will be notified", ""]], "w": [7.0, 9.5]},
   {"t": ["หัวข้อ", "เนื้อหา"], "r": [["ผู้ควบคุมข้อมูลและข้อมูลติดต่อ DPO", ""], ["วันเวลาที่เกิดเหตุและที่ทราบเหตุ", ""], ["ลักษณะของเหตุละเมิด", ""], ["ประเภทและจำนวนโดยประมาณของเจ้าของข้อมูลและรายการข้อมูล", ""], ["ผลกระทบที่อาจเกิดขึ้น", ""], ["มาตรการที่ดำเนินการแล้วและที่จะดำเนินการ", ""], ["ได้แจ้งหรือจะแจ้งเจ้าของข้อมูลหรือไม่", ""]], "w": [7.0, 9.5]}),
  ("Notice to Affected Individuals", "หนังสือแจ้งบุคคลที่ได้รับผลกระทบ", "Provide a plain-language notice template.", "จัดทำแม่แบบหนังสือแจ้งด้วยภาษาที่เข้าใจง่าย",
   "Dear [Name],\nWe are writing to inform you of an incident that affected your personal information. On [date], we discovered that [brief description]. The information involved includes [data types]. We have [actions taken]. We recommend that you [protective steps]. If you have questions, please contact our Data Protection Officer at [contact]. We sincerely apologize for this incident.\n[Name, position], [Organization Name]",
   "เรียน [ชื่อ]\n[ชื่อองค์กร] ขอแจ้งให้ท่านทราบถึงเหตุการณ์ที่กระทบต่อข้อมูลส่วนบุคคลของท่าน เมื่อวันที่ [วันที่] องค์กรตรวจพบว่า [คำอธิบายโดยย่อ] ข้อมูลที่เกี่ยวข้อง ได้แก่ [ประเภทข้อมูล] องค์กรได้ [การดำเนินการ] และขอแนะนำให้ท่าน [ขั้นตอนป้องกัน] หากมีข้อสงสัย โปรดติดต่อเจ้าหน้าที่คุ้มครองข้อมูลส่วนบุคคลที่ [ช่องทางติดต่อ] องค์กรขออภัยต่อเหตุการณ์ที่เกิดขึ้น\n[ชื่อ ตำแหน่ง] [ชื่อองค์กร]",
   "Dear Patient,\nWe are writing to inform you of an incident that affected your personal information. On [date], CMC discovered that [brief description]. The information involved includes [data types]. CMC has [actions taken]. We recommend that you [protective steps]. If you have questions, please contact the CMC Data Protection Officer at dpo@cmc.example or 02-000-0000 ext. 1234. We sincerely apologize.\nChief Executive Officer, Chaophraya Medical Center"),
  ("NCSA and Regulator Incident Report", "รายงานเหตุการณ์ต่อ สกมช. และหน่วยงานกำกับดูแล", "Provide fields for CII incident reports. [VERIFY current NCSA form.]", "ระบุข้อมูลสำหรับรายงานเหตุการณ์ของ CII [VERIFY แบบฟอร์มของ สกมช. ฉบับปัจจุบัน]",
   ["Organization, CII sector, and contact officer.", "Date and time of detection.", "Type of threat and affected systems.", "Impact on critical services.", "Actions taken and assistance requested.", "Next update time."],
   ["องค์กร ภาคส่วน CII และผู้ประสานงาน", "วันและเวลาที่ตรวจพบ", "ประเภทภัยคุกคามและระบบที่ได้รับผลกระทบ", "ผลกระทบต่อบริการสำคัญ", "การดำเนินการและความช่วยเหลือที่ต้องการ", "เวลาที่จะรายงานความคืบหน้าครั้งถัดไป"]),
 ],
 bp=[("Pre-approve templates with Legal so only incident facts need to be added under time pressure.", "ให้ฝ่ายกฎหมายอนุมัติแม่แบบล่วงหน้า เพื่อให้เติมเฉพาะข้อเท็จจริงของเหตุการณ์ภายใต้ความกดดันด้านเวลา"),
     ("Prepare Thai and English versions.", "จัดทำฉบับภาษาไทยและภาษาอังกฤษ")],
 mistakes=[("Speculating about causes or attackers in regulatory notices before facts are confirmed.", "คาดเดาสาเหตุหรือผู้โจมตีในการแจ้งหน่วยงานกำกับก่อนยืนยันข้อเท็จจริง")],
)
