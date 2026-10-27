# -*- coding: utf-8 -*-
# DE Detect: DE.CM and DE.AE
C = {}

C["DE-STD-001"] = dict(
 purpose=("This standard sets what must be monitored, by whom, how quickly alerts must be handled, and how monitoring coverage is measured, so that adverse events are detected in time (DE.CM; CSA s.56 for CII).",
          "มาตรฐานนี้กำหนดสิ่งที่ต้องเฝ้าระวัง ผู้รับผิดชอบ ระยะเวลาในการจัดการการแจ้งเตือน และวิธีวัดความครอบคลุมของการเฝ้าระวัง เพื่อให้ตรวจจับเหตุการณ์ไม่พึงประสงค์ได้ทันเวลา (DE.CM; พ.ร.บ.ไซเบอร์ฯ มาตรา 56 สำหรับ CII)"),
 sections=[
  ("Monitoring Scope", "ขอบเขตการเฝ้าระวัง", "Define what is monitored, mapped to CSF subcategories.", "กำหนดสิ่งที่ต้องเฝ้าระวัง โดยเชื่อมโยงกับ CSF Subcategory",
   {"t": ["Area", "Sources", "CSF"], "r": [
     ["Networks and network services", "Firewalls, IPS, DNS, proxy, VPN, network detection", "DE.CM-01"],
     ["Physical environment", "Badge systems, CCTV alerts, environmental sensors for data centers", "DE.CM-02"],
     ["Personnel activity and technology use", "Identity logs, privileged sessions, DLP, application audit logs", "DE.CM-03"],
     ["External service provider activity", "Vendor remote sessions, SaaS admin logs, MSSP actions", "DE.CM-06"],
     ["Computing hardware, software, and data", "EDR, server logs, cloud workloads, file integrity, backup alerts", "DE.CM-09"]], "w": [5.0, 9.0, 2.5]},
   {"t": ["ด้าน", "แหล่งข้อมูล", "CSF"], "r": [
     ["เครือข่ายและบริการเครือข่าย", "ไฟร์วอลล์ IPS DNS Proxy VPN ระบบตรวจจับบนเครือข่าย", "DE.CM-01"],
     ["สภาพแวดล้อมทางกายภาพ", "ระบบบัตรผ่าน การแจ้งเตือนจากกล้องวงจรปิด เซ็นเซอร์สภาพแวดล้อมของศูนย์ข้อมูล", "DE.CM-02"],
     ["กิจกรรมของบุคลากรและการใช้เทคโนโลยี", "Log ระบบตัวตน เซสชันสิทธิ์ระดับสูง DLP Log การตรวจสอบของแอปพลิเคชัน", "DE.CM-03"],
     ["กิจกรรมของผู้ให้บริการภายนอก", "เซสชันระยะไกลของผู้ขาย Log ผู้ดูแล SaaS การดำเนินการของ MSSP", "DE.CM-06"],
     ["ฮาร์ดแวร์ ซอฟต์แวร์ และข้อมูล", "EDR Log เซิร์ฟเวอร์ Workload บนคลาวด์ ความถูกต้องของไฟล์ การแจ้งเตือนการสำรองข้อมูล", "DE.CM-09"]], "w": [5.0, 9.0, 2.5]}),
  ("Service Levels", "ระดับการให้บริการ", "Set triage and escalation times by alert severity.", "กำหนดระยะเวลาการคัดกรองและการยกระดับตามระดับความรุนแรงของการแจ้งเตือน",
   {"t": ["Alert severity", "Triage start", "Escalate to on-call", "Coverage"], "r": [["Critical", "15 minutes", "30 minutes", "24x7"], ["High", "30 minutes", "2 hours", "24x7"], ["Medium", "4 hours", "Next business day", "Business hours or 24x7"], ["Low", "Next business day", "Weekly review", "Business hours"]], "w": [3.5, 4.0, 4.5, 4.5]},
   {"t": ["ระดับการแจ้งเตือน", "เริ่มคัดกรอง", "ยกระดับไปยังผู้รับผิดชอบเวร", "ช่วงเวลาให้บริการ"], "r": [["วิกฤต", "15 นาที", "30 นาที", "24 ชั่วโมง 7 วัน"], ["สูง", "30 นาที", "2 ชั่วโมง", "24 ชั่วโมง 7 วัน"], ["ปานกลาง", "4 ชั่วโมง", "วันทำการถัดไป", "เวลาทำการหรือ 24 ชั่วโมง"], ["ต่ำ", "วันทำการถัดไป", "ทบทวนรายสัปดาห์", "เวลาทำการ"]], "w": [3.5, 4.0, 4.5, 4.5]}),
  ("Coverage Measurement", "การวัดความครอบคลุม", "Define how monitoring coverage and quality are measured.", "กำหนดวิธีวัดความครอบคลุมและคุณภาพของการเฝ้าระวัง",
   ["Maintain the Log Source and Monitoring Coverage Register (DE-REG-001) and the Detection Use Case Catalog (DE-REG-002).", "Report critical log source coverage monthly (target 95%).", "Test detections at least twice a year using simulated attack techniques mapped to MITRE ATT&CK."],
   ["ดูแลทะเบียนแหล่งข้อมูล Log และขอบเขตการเฝ้าระวัง (DE-REG-001) และบัญชีกรณีการตรวจจับ (DE-REG-002)", "รายงานความครอบคลุมของแหล่ง Log สำคัญทุกเดือน (เป้าหมาย 95%)", "ทดสอบการตรวจจับอย่างน้อยปีละ 2 ครั้งด้วยเทคนิคการโจมตีจำลองที่อ้างอิง MITRE ATT&CK"]),
 ],
 bp=[("Decide in-house versus managed SOC based on 24x7 cost; most mid-sized organizations use an MSSP with in-house oversight.", "ตัดสินใจระหว่าง SOC ภายในหรือจ้างภายนอกตามต้นทุนการทำงาน 24 ชั่วโมง องค์กรขนาดกลางส่วนใหญ่ใช้ MSSP โดยมีทีมภายในกำกับดูแล"),
     ("Focus first on detections for ransomware precursors: credential abuse, lateral movement, backup tampering.", "เริ่มจากการตรวจจับสัญญาณเตือนของแรนซัมแวร์ ได้แก่ การใช้ข้อมูลยืนยันตัวตนในทางที่ผิด การเคลื่อนที่ภายในเครือข่าย และการแก้ไขระบบสำรองข้อมูล"),
     ("Measure mean time to detect and mean time to respond.", "วัดระยะเวลาเฉลี่ยในการตรวจจับและระยะเวลาเฉลี่ยในการตอบสนอง")],
 mistakes=[("Buying a SIEM and sending all logs without defined use cases, producing noise and high cost.", "ซื้อ SIEM แล้วส่ง Log ทั้งหมดโดยไม่มีกรณีการตรวจจับที่กำหนด ทำให้เกิดการแจ้งเตือนรบกวนและต้นทุนสูง")],
 rev="Updated in March 2026 when the MSSP began 24x7 monitoring; service levels aligned with the MSSP contract.",
)

C["DE-PRC-001"] = dict(
 purpose=("This procedure describes daily security monitoring operations: alert handling, shift handover, tuning, escalation, and oversight of the managed service provider where used (DE.CM, DE.AE-06).",
          "ระเบียบปฏิบัตินี้อธิบายการปฏิบัติงานเฝ้าระวังความมั่นคงปลอดภัยประจำวัน ได้แก่ การจัดการการแจ้งเตือน การส่งมอบเวร การปรับแต่ง การยกระดับ และการกำกับผู้ให้บริการกรณีจ้างภายนอก (DE.CM, DE.AE-06)"),
 sections=[
  ("Daily Operations", "การปฏิบัติงานประจำวัน", "Describe recurring monitoring activities.", "อธิบายกิจกรรมการเฝ้าระวังที่ทำเป็นประจำ",
   {"t": ["Activity", "Frequency", "Actor"], "r": [
     ["Monitor alert queue and triage per DE-PRC-002", "Continuous", "[SOC] analyst"], ["Check log source health; raise tickets for silent sources", "Daily", "[SOC] analyst"],
     ["Shift handover with open cases and watch items", "Each shift", "[SOC] analysts"], ["Tune noisy rules and document changes", "Weekly", "[SOC] engineer"],
     ["Report alerts, incidents, and coverage to the [CISO]", "Monthly", "[SOC] Lead"], ["Service review with the MSSP (if outsourced)", "Monthly", "[CISO]"]], "w": [9.0, 3.0, 4.5]},
   {"t": ["กิจกรรม", "ความถี่", "ผู้ดำเนินการ"], "r": [
     ["เฝ้าระวังคิวการแจ้งเตือนและคัดกรองตาม DE-PRC-002", "ต่อเนื่อง", "นักวิเคราะห์ [SOC]"], ["ตรวจสอบสถานะแหล่ง Log และเปิดงานสำหรับแหล่งที่หยุดส่ง", "ทุกวัน", "นักวิเคราะห์ [SOC]"],
     ["ส่งมอบเวรพร้อมเคสที่ยังเปิดและรายการที่ต้องเฝ้าดู", "ทุกเวร", "นักวิเคราะห์ [SOC]"], ["ปรับแต่งกฎที่แจ้งเตือนมากเกินไปและบันทึกการเปลี่ยนแปลง", "ทุกสัปดาห์", "วิศวกร [SOC]"],
     ["รายงานการแจ้งเตือน เหตุการณ์ และความครอบคลุมต่อ [CISO]", "ทุกเดือน", "หัวหน้า [SOC]"], ["ทบทวนการให้บริการกับ MSSP (กรณีจ้างภายนอก)", "ทุกเดือน", "[CISO]"]], "w": [9.0, 3.0, 4.5]}),
  ("Escalation Matrix", "ตารางการยกระดับ", "Define who is contacted, how, and when.", "กำหนดผู้ที่ต้องติดต่อ วิธีการ และเวลา",
   {"t": ["Condition", "Contact", "Method"], "r": [["Critical alert or confirmed compromise", "[CISO] and IT on-call", "Phone call, then ticket"], ["Suspected personal data exposure", "[CISO] and [DPO]", "Phone call"], ["Business-impacting outage", "IT on-call and [CIO]", "Phone call"]], "w": [6.5, 5.0, 5.0]},
   {"t": ["เงื่อนไข", "ผู้ติดต่อ", "วิธีการ"], "r": [["การแจ้งเตือนระดับวิกฤตหรือยืนยันว่าถูกโจมตี", "[CISO] และ IT เวร", "โทรศัพท์ แล้วเปิดงาน"], ["สงสัยว่าข้อมูลส่วนบุคคลรั่วไหล", "[CISO] และ [DPO]", "โทรศัพท์"], ["ระบบหยุดชะงักที่กระทบธุรกิจ", "IT เวร และ [CIO]", "โทรศัพท์"]], "w": [6.5, 5.0, 5.0]},
   {"t": ["Condition", "Contact", "Method"], "r": [["Critical alert or confirmed compromise", "Security Manager and IT on-call", "MSSP phone call within 15 minutes, then ticket"], ["Suspected patient data exposure", "Security Manager and DPO", "Phone call"], ["Clinical system outage", "IT on-call, CIO, and nursing supervisor on duty", "Phone call"]], "w": [6.5, 5.0, 5.0]}),
 ],
 bp=[("Give the MSSP clear authority to isolate endpoints for Critical alerts, agreed in advance.", "มอบอำนาจที่ชัดเจนให้ MSSP แยกเครื่องออกจากเครือข่ายเมื่อเกิดการแจ้งเตือนระดับวิกฤต โดยตกลงไว้ล่วงหน้า"),
     ("Keep an internal owner who understands the business context the MSSP lacks.", "มีผู้รับผิดชอบภายในที่เข้าใจบริบททางธุรกิจที่ MSSP ไม่ทราบ")],
 mistakes=[("Outsourcing monitoring and assuming the MSSP will also respond and decide.", "จ้างภายนอกเฝ้าระวังแล้วเข้าใจว่า MSSP จะรับมือและตัดสินใจแทนทั้งหมด")],
)

C["DE-REG-001"] = dict(
 purpose=("This register lists log sources, whether they are collected and monitored, and their coverage status, so that blind spots are visible (DE.CM-01, DE.CM-09, PR.PS-04).",
          "ทะเบียนนี้ระบุแหล่งข้อมูล Log สถานะการรวบรวมและการเฝ้าระวัง และความครอบคลุม เพื่อให้เห็นจุดบอดของการเฝ้าระวัง (DE.CM-01, DE.CM-09, PR.PS-04)"),
 fields=[
  ("Source", "แหล่งข้อมูล", "System or device group.", "ระบบหรือกลุ่มอุปกรณ์", ""),
  ("Criticality", "ความสำคัญ", "Critical, High, Medium.", "วิกฤต สูง ปานกลาง", ""),
  ("Log types", "ประเภท Log", "Events collected.", "เหตุการณ์ที่รวบรวม", ""),
  ("Collected (Yes, Partial, No)", "รวบรวมแล้ว (ใช่ บางส่วน ไม่)", "Status.", "สถานะ", ""),
  ("Monitored use cases", "กรณีการตรวจจับที่เฝ้าระวัง", "From DE-REG-002.", "จาก DE-REG-002", ""),
  ("Retention", "ระยะเวลาเก็บรักษา", "Online and archive.", "ออนไลน์และจัดเก็บถาวร", ""),
  ("Gap and action", "ช่องว่างและการดำเนินการ", "Plan to close gaps.", "แผนปิดช่องว่าง", ""),
 ],
 rows=[
  ["Active Directory and Entra ID", "Critical", "Sign-ins, account and group changes, MFA", "Yes", "UC-01, UC-02, UC-05", "1 year / 2 years", "None"],
  ["EDR (workstations and servers)", "Critical", "Detections, process telemetry", "Yes", "UC-03, UC-04", "90 days in EDR; alerts 1 year", "None"],
  ["Firewalls and VPN", "Critical", "Allow and deny, VPN sessions", "Yes", "UC-06", "1 year", "None"],
  ["HIS application audit log", "Critical", "Record access, exports, admin actions", "Partial", "UC-08", "2 years", "Export to SIEM in Q4 2026"],
  ["Backup platform", "Critical", "Job changes, deletions, admin logins", "Yes", "UC-07", "1 year", "None"],
  ["Medical device VLAN (network detection)", "High", "Network anomalies", "Partial", "UC-09", "90 days", "Phase 2 wards in 2027"],
  ["PACS", "Critical", "Logins, admin actions", "No", "None", "Not applicable", "Vendor log export under discussion"],
 ],
 bp=[("Review coverage quarterly against the asset inventory and new systems.", "ทบทวนความครอบคลุมทุกไตรมาสเทียบกับทะเบียนทรัพย์สินและระบบใหม่")],
 mistakes=[("Assuming a source is monitored because it was onboarded once; sources stop sending silently.", "เข้าใจว่าแหล่งข้อมูลได้รับการเฝ้าระวังเพราะเคยเชื่อมต่อแล้ว ทั้งที่แหล่งข้อมูลอาจหยุดส่งโดยไม่มีใครรู้")],
)

C["DE-GDL-001"] = dict(
 purpose=("This guideline sets out what to require from a managed security service provider (MSSP) for monitoring and response, so the service is measurable and the organization retains control (DE.CM-06, GV.SC-05).",
          "แนวทางนี้กำหนดสิ่งที่ควรกำหนดให้ผู้ให้บริการความมั่นคงปลอดภัยแบบบริหารจัดการ (MSSP) ต้องให้บริการด้านการเฝ้าระวังและรับมือ เพื่อให้วัดผลบริการได้และองค์กรยังคงควบคุมได้ (DE.CM-06, GV.SC-05)"),
 sections=[
  ("Service Requirements", "ข้อกำหนดของบริการ", "List the minimum service elements and measures.", "ระบุองค์ประกอบขั้นต่ำของบริการและตัวชี้วัด",
   {"t": ["Area", "Requirement"], "r": [
     ["Coverage", "24x7 monitoring of agreed log sources; onboarding plan with dates"], ["Service levels", "Triage and notification times matching DE-STD-001; monthly SLA report"],
     ["Response authority", "Defined actions the MSSP may take (for example, isolate endpoint, disable account) and those that need approval"],
     ["Use cases", "Agreed detection catalog, tuned quarterly, mapped to MITRE ATT&CK"], ["Threat intelligence", "Included and applied to detections"],
     ["Incident response", "Retainer hours, on-site option, forensic capability"], ["Data protection", "Log location, retention, access, deletion at exit; DPA where personal data is processed"],
     ["Reporting and governance", "Monthly service review, quarterly executive report"], ["Exit", "Return of logs, rules, and documentation"]], "w": [4.0, 12.5]},
   {"t": ["ด้าน", "ข้อกำหนด"], "r": [
     ["ความครอบคลุม", "เฝ้าระวังแหล่ง Log ที่ตกลงตลอด 24 ชั่วโมง 7 วัน พร้อมแผนการเชื่อมต่อและกำหนดเวลา"], ["ระดับการให้บริการ", "ระยะเวลาคัดกรองและแจ้งเตือนตาม DE-STD-001 และรายงาน SLA รายเดือน"],
     ["อำนาจในการตอบสนอง", "กำหนดการดำเนินการที่ MSSP ทำได้เอง (เช่น แยกเครื่อง ปิดบัญชี) และที่ต้องขออนุมัติ"],
     ["กรณีการตรวจจับ", "บัญชีการตรวจจับที่ตกลง ปรับแต่งทุกไตรมาส และอ้างอิง MITRE ATT&CK"], ["ข้อมูลข่าวกรองภัยคุกคาม", "รวมอยู่ในบริการและนำไปใช้กับการตรวจจับ"],
     ["การรับมือเหตุการณ์", "ชั่วโมงบริการตามสัญญา ทางเลือกการปฏิบัติงานในสถานที่ และความสามารถด้านนิติวิทยาศาสตร์ดิจิทัล"], ["การคุ้มครองข้อมูล", "ที่ตั้ง Log ระยะเวลาเก็บรักษา การเข้าถึง และการลบเมื่อสิ้นสุดสัญญา พร้อม DPA เมื่อมีการประมวลผลข้อมูลส่วนบุคคล"],
     ["การรายงานและการกำกับ", "ทบทวนบริการรายเดือน และรายงานผู้บริหารรายไตรมาส"], ["การยุติบริการ", "ส่งคืน Log กฎการตรวจจับ และเอกสาร"]], "w": [4.0, 12.5]}),
 ],
 bp=[("Run a proof of concept with your own data before signing.", "ทดสอบแนวคิด (PoC) ด้วยข้อมูลขององค์กรก่อนลงนาม"),
     ("Own the detection rules and log platform where possible to avoid lock-in.", "เป็นเจ้าของกฎการตรวจจับและระบบ Log เมื่อทำได้ เพื่อหลีกเลี่ยงการผูกขาดกับผู้ให้บริการ")],
 mistakes=[("Contracts measure ticket counts instead of detection quality and response times.", "สัญญาวัดผลจากจำนวนงาน แทนคุณภาพการตรวจจับและระยะเวลาการตอบสนอง")],
)

C["DE-PRC-002"] = dict(
 purpose=("This procedure describes how security alerts are triaged, enriched, analyzed, correlated, and either closed or declared as incidents (DE.AE-02 to DE.AE-07).",
          "ระเบียบปฏิบัตินี้อธิบายวิธีคัดกรอง เพิ่มข้อมูลประกอบ วิเคราะห์ เชื่อมโยง และปิดหรือประกาศเป็นเหตุการณ์ สำหรับการแจ้งเตือนด้านความมั่นคงปลอดภัย (DE.AE-02 ถึง DE.AE-07)"),
 sections=[
  ("Triage and Analysis Steps", "ขั้นตอนการคัดกรองและวิเคราะห์", "Describe analysis steps from alert to decision.", "อธิบายขั้นตอนการวิเคราะห์ตั้งแต่การแจ้งเตือนจนถึงการตัดสินใจ",
   {"t": ["Step", "Activity", "CSF"], "r": [
     ["1", "Acknowledge the alert and check whether it is a known false positive", "DE.AE-02"], ["2", "Enrich with asset criticality, user role, threat intelligence, and recent changes", "DE.AE-07"],
     ["3", "Correlate with other sources (identity, EDR, network) and related alerts", "DE.AE-03"], ["4", "Estimate scope and impact: systems, data, users affected", "DE.AE-04"],
     ["5", "Decide: close with reason, monitor, or declare an incident per DE-STD-002", "DE.AE-08"], ["6", "Notify authorized staff and record the case", "DE.AE-06"]], "w": [1.2, 12.3, 3.0]},
   {"t": ["ขั้นตอน", "กิจกรรม", "CSF"], "r": [
     ["1", "รับทราบการแจ้งเตือนและตรวจสอบว่าเป็นผลบวกลวงที่ทราบแล้วหรือไม่", "DE.AE-02"], ["2", "เพิ่มข้อมูลประกอบ ได้แก่ ความสำคัญของทรัพย์สิน บทบาทผู้ใช้ ข้อมูลข่าวกรองภัยคุกคาม และการเปลี่ยนแปลงล่าสุด", "DE.AE-07"],
     ["3", "เชื่อมโยงกับแหล่งข้อมูลอื่น (ระบบตัวตน EDR เครือข่าย) และการแจ้งเตือนที่เกี่ยวข้อง", "DE.AE-03"], ["4", "ประเมินขอบเขตและผลกระทบ ได้แก่ ระบบ ข้อมูล และผู้ใช้ที่ได้รับผลกระทบ", "DE.AE-04"],
     ["5", "ตัดสินใจ: ปิดพร้อมเหตุผล เฝ้าดูต่อ หรือประกาศเป็นเหตุการณ์ตาม DE-STD-002", "DE.AE-08"], ["6", "แจ้งบุคลากรที่ได้รับอนุญาต และบันทึกเคส", "DE.AE-06"]], "w": [1.2, 12.3, 3.0]}),
 ],
 bp=[("Document triage decisions so others can learn and auditors can verify.", "บันทึกการตัดสินใจในการคัดกรอง เพื่อให้ผู้อื่นเรียนรู้และผู้ตรวจสอบตรวจสอบได้"),
     ("Automate enrichment (asset owner, user role) to cut triage time.", "เพิ่มข้อมูลประกอบโดยอัตโนมัติ (เจ้าของทรัพย์สิน บทบาทผู้ใช้) เพื่อลดเวลาการคัดกรอง")],
 mistakes=[("Closing alerts as false positives without investigation because volume is high.", "ปิดการแจ้งเตือนว่าเป็นผลบวกลวงโดยไม่สอบสวนเพราะมีปริมาณมาก")],
)

C["DE-STD-002"] = dict(
 purpose=("This standard defines incident categories, severity levels, and declaration criteria, so that incidents are declared consistently and trigger the right response and notifications (DE.AE-08, RS.MA-03).",
          "มาตรฐานนี้กำหนดประเภทเหตุการณ์ ระดับความรุนแรง และเกณฑ์การประกาศเหตุการณ์ เพื่อให้ประกาศเหตุการณ์ได้สม่ำเสมอ และนำไปสู่การรับมือและการแจ้งเหตุที่ถูกต้อง (DE.AE-08, RS.MA-03)"),
 sections=[
  ("Incident Categories", "ประเภทเหตุการณ์", "List incident categories.", "ระบุประเภทเหตุการณ์",
   ["Malware and ransomware", "Account compromise", "Phishing and business email compromise", "Data breach or unauthorized disclosure", "Denial of service", "Insider misuse", "Third-party or supply chain compromise", "Physical security incident affecting information"],
   ["มัลแวร์และแรนซัมแวร์", "บัญชีผู้ใช้ถูกยึด", "ฟิชชิ่งและการหลอกลวงทางอีเมลธุรกิจ", "ข้อมูลรั่วไหลหรือถูกเปิดเผยโดยไม่ได้รับอนุญาต", "การโจมตีแบบปฏิเสธการให้บริการ", "การใช้งานในทางที่ผิดโดยบุคคลภายใน", "การถูกโจมตีผ่านผู้ให้บริการหรือห่วงโซ่อุปทาน", "เหตุการณ์ด้านความมั่นคงปลอดภัยทางกายภาพที่กระทบข้อมูล"]),
  ("Severity Levels", "ระดับความรุนแรง", "Define severity levels with criteria and required actions.", "กำหนดระดับความรุนแรงพร้อมเกณฑ์และการดำเนินการที่ต้องทำ",
   {"t": ["Severity", "Criteria (any)", "Response lead", "Notify"], "r": [
     ["SEV-1 Critical", "Critical service down or at imminent risk; confirmed large-scale data breach; ransomware spreading", "[CISO]; crisis team activated", "[CEO] within 1 hour; regulators per RS-PRC-003"],
     ["SEV-2 High", "Confirmed compromise of a server or privileged account; personal data breach likely notifiable", "[CISO]", "[CIO] within 2 hours; [DPO]"],
     ["SEV-3 Medium", "Compromise contained to one user or endpoint; no sensitive data affected", "Security engineer", "[CISO] same day"],
     ["SEV-4 Low", "Policy violation or blocked attack with no impact", "[SOC] analyst", "Monthly report"]], "w": [2.8, 7.0, 3.5, 3.2]},
   {"t": ["ระดับ", "เกณฑ์ (ข้อใดข้อหนึ่ง)", "ผู้นำการรับมือ", "การแจ้ง"], "r": [
     ["SEV-1 วิกฤต", "บริการสำคัญหยุดหรือมีความเสี่ยงจะหยุดทันที ยืนยันข้อมูลรั่วไหลขนาดใหญ่ แรนซัมแวร์กำลังแพร่กระจาย", "[CISO] และเปิดใช้ทีมบริหารภาวะวิกฤต", "[CEO] ภายใน 1 ชั่วโมง และหน่วยงานกำกับตาม RS-PRC-003"],
     ["SEV-2 สูง", "ยืนยันว่าเซิร์ฟเวอร์หรือบัญชีสิทธิ์ระดับสูงถูกโจมตี มีแนวโน้มเป็นเหตุละเมิดข้อมูลที่ต้องแจ้ง", "[CISO]", "[CIO] ภายใน 2 ชั่วโมง และ [DPO]"],
     ["SEV-3 ปานกลาง", "การถูกโจมตีจำกัดอยู่ที่ผู้ใช้หรือเครื่องเดียว และไม่กระทบข้อมูลอ่อนไหว", "วิศวกรความมั่นคงปลอดภัย", "[CISO] ภายในวันเดียวกัน"],
     ["SEV-4 ต่ำ", "การฝ่าฝืนนโยบายหรือการโจมตีที่ถูกบล็อกโดยไม่มีผลกระทบ", "นักวิเคราะห์ [SOC]", "รายงานรายเดือน"]], "w": [2.8, 7.0, 3.5, 3.2]},
   {"t": ["Severity", "CMC criteria (any)", "Response lead", "Notify"], "r": [
     ["SEV-1 Critical", "HIS, PACS, or LIS down from a cyber event; ransomware on any server; patient data breach over 1,000 records", "Security Manager; Crisis Management Team", "CEO within 1 hour; NCSA and regulator per CII rules; PDPC within 72 hours if notifiable"],
     ["SEV-2 High", "Privileged account or server compromise; vendor access misuse; patient data breach under 1,000 records", "Security Manager", "CIO within 2 hours; DPO"],
     ["SEV-3 Medium", "Single workstation malware contained by EDR; single mailbox compromise without data access", "Security engineer with MSSP", "Security Manager same day"],
     ["SEV-4 Low", "Blocked phishing; policy violation", "MSSP analyst", "Monthly report"]], "w": [2.8, 7.0, 3.5, 3.2]}),
  ("Regulatory Significance Check", "การตรวจสอบนัยสำคัญด้านกฎหมาย", "Require a check of legal notification thresholds for every SEV-1 and SEV-2 incident.", "กำหนดให้ตรวจสอบเกณฑ์การแจ้งเหตุตามกฎหมายสำหรับเหตุการณ์ระดับ SEV-1 และ SEV-2 ทุกครั้ง",
   "For every SEV-1 and SEV-2 incident, the [CISO] and [DPO] assess within 4 hours whether PDPA breach notification (s.37(4)) or CII significant incident reporting (CSA s.57; CRC Notification 2024, reported as 24 hours [VERIFY]) applies, and start RS-PRC-003.",
   "สำหรับเหตุการณ์ระดับ SEV-1 และ SEV-2 ทุกครั้ง [CISO] และ [DPO] ต้องประเมินภายใน 4 ชั่วโมงว่าต้องแจ้งเหตุละเมิดตาม PDPA (มาตรา 37(4)) หรือต้องรายงานเหตุการณ์สำคัญของ CII (พ.ร.บ.ไซเบอร์ฯ มาตรา 57 และประกาศ กกม. 2567 ซึ่งกำหนดไว้ 24 ชั่วโมง [VERIFY]) หรือไม่ และเริ่มดำเนินการตาม RS-PRC-003"),
 ],
 bp=[("Base severity on business impact so non-technical leaders understand it.", "กำหนดระดับความรุนแรงตามผลกระทบทางธุรกิจ เพื่อให้ผู้บริหารที่ไม่ใช่สายเทคนิคเข้าใจ"),
     ("Allow upgrading severity at any time as facts emerge; never downgrade without review.", "อนุญาตให้ปรับระดับความรุนแรงขึ้นได้ตลอดเมื่อมีข้อเท็จจริงใหม่ และห้ามลดระดับโดยไม่มีการทบทวน")],
 mistakes=[("Waiting for certainty before declaring an incident, which wastes the notification window.", "รอให้แน่ใจก่อนประกาศเหตุการณ์ ทำให้เสียเวลาในกรอบเวลาการแจ้งเหตุ")],
)

C["DE-REG-002"] = dict(
 purpose=("This catalog lists detection use cases, the threat each addresses, data sources, logic owner, and test status, so detection capability is managed and measured (DE.AE-02, DE.AE-07).",
          "บัญชีนี้ระบุกรณีการตรวจจับ ภัยคุกคามที่แต่ละกรณีรองรับ แหล่งข้อมูล ผู้รับผิดชอบตรรกะการตรวจจับ และสถานะการทดสอบ เพื่อบริหารและวัดความสามารถในการตรวจจับ (DE.AE-02, DE.AE-07)"),
 fields=[
  ("Use case ID", "รหัสกรณีการตรวจจับ", "Unique reference.", "รหัสอ้างอิง", "UC-01"),
  ("Detection", "การตรวจจับ", "What the rule detects.", "สิ่งที่กฎตรวจจับ", ""),
  ("MITRE ATT&CK technique", "เทคนิค MITRE ATT&CK", "Technique ID.", "รหัสเทคนิค", "T1110"),
  ("Data sources", "แหล่งข้อมูล", "From DE-REG-001.", "จาก DE-REG-001", ""),
  ("Severity", "ระดับความรุนแรง", "Default alert severity.", "ระดับการแจ้งเตือนเริ่มต้น", ""),
  ("Response playbook", "คู่มือการรับมือ", "Linked playbook.", "คู่มือที่เชื่อมโยง", ""),
  ("Last tested", "ทดสอบล่าสุด", "Date and result.", "วันที่และผล", ""),
 ],
 rows=[
  ["UC-01", "Password spraying or brute force against directory or VPN", "T1110", "Entra ID, Active Directory, VPN", "High", "RS-PLB-004", "05/2026 Pass"],
  ["UC-02", "Impossible travel or sign-in from unusual country", "T1078", "Entra ID", "Medium", "RS-PLB-004", "05/2026 Pass"],
  ["UC-03", "Ransomware behavior: mass file encryption or shadow copy deletion", "T1486, T1490", "EDR", "Critical", "RS-PLB-001", "05/2026 Pass"],
  ["UC-04", "Credential dumping tools on servers", "T1003", "EDR", "Critical", "RS-PLB-001", "05/2026 Pass"],
  ["UC-05", "New member added to Domain Admins", "T1098", "Active Directory", "High", "RS-PRC-001", "05/2026 Pass"],
  ["UC-06", "Connection to known malicious IP or domain", "T1071", "Firewall, DNS filter", "High", "RS-PRC-001", "05/2026 Pass"],
  ["UC-07", "Backup job deletion or retention change", "T1490", "Backup platform", "Critical", "RS-PLB-001", "05/2026 Pass"],
  ["UC-08", "Bulk patient record access or export by one user", "T1530", "HIS audit log", "High", "RS-PLB-003", "Pending (HIS log onboarding)"],
  ["UC-09", "New device or unusual protocol on medical device VLAN", "T0846", "Network detection", "Medium", "RS-PRC-001", "09/2026 Pass"],
 ],
 bp=[("Start with 15 to 25 high-value use cases and test each one.", "เริ่มจากกรณีการตรวจจับที่มีคุณค่าสูง 15 ถึง 25 กรณี และทดสอบทุกกรณี"),
     ("Link every use case to a response playbook so analysts know what to do.", "เชื่อมทุกกรณีการตรวจจับกับคู่มือการรับมือ เพื่อให้นักวิเคราะห์รู้ว่าต้องทำอะไร")],
 mistakes=[("Hundreds of vendor default rules enabled, none tested or tuned.", "เปิดใช้กฎค่าเริ่มต้นของผู้ขายหลายร้อยกฎโดยไม่ได้ทดสอบหรือปรับแต่ง")],
)

C["DE-PRC-003"] = dict(
 purpose=("This procedure guides proactive, hypothesis-driven searches for threats that evaded automated detection (DE.AE-02, DE.AE-03, DE.AE-07).",
          "ระเบียบปฏิบัตินี้เป็นแนวทางการค้นหาภัยคุกคามเชิงรุกโดยอิงสมมติฐาน เพื่อค้นหาภัยคุกคามที่หลบเลี่ยงการตรวจจับอัตโนมัติ (DE.AE-02, DE.AE-03, DE.AE-07)"),
 sections=[
  ("Hunt Cycle", "รอบการค้นหา", "Describe the hunt cycle.", "อธิบายรอบการค้นหาภัยคุกคาม",
   {"n": ["Form a hypothesis from threat intelligence or recent incidents (for example, 'attackers use remote management tools for persistence').", "Identify data needed and confirm it is available.",
          "Search, analyze, and pivot across sources.", "Confirm or reject the hypothesis; escalate findings as incidents.", "Turn successful hunts into automated detections (DE-REG-002).", "Record the hunt, data gaps, and outcomes."]},
   {"n": ["ตั้งสมมติฐานจากข้อมูลข่าวกรองภัยคุกคามหรือเหตุการณ์ล่าสุด (เช่น ผู้โจมตีใช้เครื่องมือบริหารระยะไกลเพื่อคงการเข้าถึง)", "ระบุข้อมูลที่ต้องใช้และยืนยันว่ามีข้อมูลพร้อม",
          "ค้นหา วิเคราะห์ และเชื่อมโยงข้อมูลข้ามแหล่ง", "ยืนยันหรือปฏิเสธสมมติฐาน และยกระดับสิ่งที่พบเป็นเหตุการณ์", "แปลงการค้นหาที่สำเร็จเป็นการตรวจจับอัตโนมัติ (DE-REG-002)", "บันทึกการค้นหา ช่องว่างของข้อมูล และผลลัพธ์"]}),
 ],
 bp=[("Run at least one hunt per quarter focused on the top threat to your sector.", "ค้นหาภัยคุกคามอย่างน้อยไตรมาสละครั้ง โดยมุ่งเน้นภัยคุกคามสำคัญของภาคส่วน")],
 mistakes=[("Calling routine alert review 'threat hunting'.", "เรียกการทบทวนการแจ้งเตือนตามปกติว่าเป็นการค้นหาภัยคุกคาม")],
)
