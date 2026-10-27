# -*- coding: utf-8 -*-
# RC Recover
C = {}

C["RC-POL-001"] = dict(
 purpose=("This policy commits [Organization Name] to maintaining critical services during disruption and recovering them within approved objectives, through a business continuity management (BCM) program (RC.RP, GV.OC-04).",
          "นโยบายนี้แสดงความมุ่งมั่นของ [ชื่อองค์กร] ในการรักษาบริการสำคัญระหว่างการหยุดชะงัก และกู้คืนภายในเป้าหมายที่อนุมัติ ผ่านแผนงานบริหารความต่อเนื่องทางธุรกิจ (BCM) (RC.RP, GV.OC-04)"),
 sections=[
  ("Policy Statements", "ข้อความนโยบาย", "State mandatory BCM principles (ISO 22301:2019 Clause 5.2).", "ระบุหลักการ BCM ที่บังคับ (ISO 22301:2019 ข้อ 5.2)",
   ["A Business Impact Analysis (ID-RPT-002) identifies critical services and recovery objectives at least once a year.", "Each critical service has a continuity plan, and each critical system has a tested recovery plan (RC-PLN-001, RC-PLN-002).",
    "Cyber scenarios, including ransomware and loss of IT, are included in continuity planning.", "Plans are exercised at least once a year and updated after exercises, incidents, and major changes (ID-PLN-002).",
    "Information security is maintained during disruption (ISO/IEC 27001:2022 Annex A 5.29).", "Critical suppliers have continuity arrangements that meet our objectives."],
   ["จัดทำการวิเคราะห์ผลกระทบทางธุรกิจ (ID-RPT-002) เพื่อระบุบริการสำคัญและเป้าหมายการกู้คืนอย่างน้อยปีละครั้ง", "บริการสำคัญแต่ละบริการมีแผนความต่อเนื่อง และระบบสำคัญแต่ละระบบมีแผนกู้คืนที่ผ่านการทดสอบ (RC-PLN-001, RC-PLN-002)",
    "รวมสถานการณ์ภัยไซเบอร์ รวมถึงแรนซัมแวร์และการสูญเสียระบบ IT ไว้ในการวางแผนความต่อเนื่อง", "ฝึกซ้อมแผนอย่างน้อยปีละครั้ง และปรับปรุงหลังการฝึกซ้อม เหตุการณ์ และการเปลี่ยนแปลงสำคัญ (ID-PLN-002)",
    "รักษาความมั่นคงปลอดภัยสารสนเทศระหว่างการหยุดชะงัก (ISO/IEC 27001:2022 Annex A 5.29)", "ผู้ให้บริการสำคัญต้องมีการจัดการด้านความต่อเนื่องที่เป็นไปตามเป้าหมายขององค์กร"],
   ["The BIA covers both hospitals and is reviewed every January by the ISSC.", "Each clinical department has a downtime procedure; HIS, PACS, LIS, and ERP have DR plans tested yearly.",
    "Ransomware and prolonged HIS outage are mandatory BCP scenarios.", "CMC exercises the BCP at least once a year, as CII duties require [VERIFY], and after major incidents.",
    "Paper downtime records containing patient data are stored and later scanned or destroyed securely.", "HIS Vendor A and the MSSP have contractual recovery commitments aligned with the BIA."]),
 ],
 bp=[("Integrate IT disaster recovery, cyber incident response, and business continuity so they hand off cleanly.", "บูรณาการการกู้คืนระบบ IT การรับมือเหตุการณ์ไซเบอร์ และความต่อเนื่องทางธุรกิจ เพื่อให้ส่งต่อกันได้อย่างราบรื่น"),
     ("Make business units own their continuity plans; IT owns technology recovery.", "ให้หน่วยธุรกิจเป็นเจ้าของแผนความต่อเนื่องของตน และฝ่าย IT เป็นเจ้าของการกู้คืนเทคโนโลยี")],
 mistakes=[("Treating BCP as an IT document only, with no business workarounds.", "ถือว่า BCP เป็นเอกสารของฝ่าย IT เท่านั้น โดยไม่มีทางเลือกทดแทนของฝ่ายธุรกิจ")],
)

C["RC-PLN-001"] = dict(
 purpose=("This plan describes how [Organization Name] continues critical services during a disruption, including activation, roles, workarounds, communication, and return to normal operations (RC.RP-01, RC.RP-02, RC.RP-04, RC.RP-06).",
          "แผนนี้อธิบายวิธีที่ [ชื่อองค์กร] รักษาบริการสำคัญระหว่างการหยุดชะงัก ได้แก่ การเปิดใช้แผน บทบาท ทางเลือกทดแทน การสื่อสาร และการกลับสู่การดำเนินงานปกติ (RC.RP-01, RC.RP-02, RC.RP-04, RC.RP-06)"),
 sections=[
  ("Activation Criteria", "เกณฑ์การเปิดใช้แผน", "Define when and by whom the plan is activated.", "กำหนดเวลาและผู้มีอำนาจเปิดใช้แผน",
   ["A critical service is or will be disrupted beyond its RTO.", "A SEV-1 cyber incident affects critical systems.", "Loss of a site, utility, or key supplier.", "Activation authority: [CEO] or delegate on advice of the [BCM] Coordinator and Incident Commander."],
   ["บริการสำคัญหยุดชะงักหรือจะหยุดชะงักเกิน RTO", "เหตุการณ์ไซเบอร์ SEV-1 กระทบระบบสำคัญ", "สูญเสียสถานที่ สาธารณูปโภค หรือผู้ให้บริการหลัก", "ผู้มีอำนาจเปิดใช้แผน: [CEO] หรือผู้ได้รับมอบหมาย ตามคำแนะนำของผู้ประสานงาน [BCM] และผู้บัญชาการเหตุการณ์"]),
  ("Continuity Strategies by Service", "กลยุทธ์ความต่อเนื่องตามบริการ", "Describe workarounds and resources for each critical service.", "อธิบายทางเลือกทดแทนและทรัพยากรของบริการสำคัญแต่ละบริการ",
   {"t": ["Critical service", "RTO", "Workaround", "Resources needed", "Owner"], "r": [["[Service]", "", "", "", ""], ["[Service]", "", "", "", ""]]},
   {"t": ["บริการสำคัญ", "RTO", "ทางเลือกทดแทน", "ทรัพยากรที่ต้องใช้", "เจ้าของ"], "r": [["[บริการ]", "", "", "", ""], ["[บริการ]", "", "", "", ""]]},
   {"t": ["Critical service", "RTO", "Workaround during IT outage", "Resources needed", "Owner"], "r": [
     ["Emergency care", "4 hours", "Paper triage and order forms; read-only HIS replica for history; ambulance diversion if needed", "Downtime kits, printed patient lists every 4 hours", "Head of Emergency"],
     ["Inpatient medication", "4 hours", "Printed medication administration records (MAR) generated every 4 hours; pharmacy manual verification", "MAR printouts, pharmacist on site", "Director of Pharmacy"],
     ["Diagnostic imaging", "8 hours", "Modalities store images locally; reports by phone for urgent cases", "Modality local storage", "Director of Radiology"],
     ["Laboratory", "8 hours", "Analyzer printouts; results phoned for critical values", "Paper requisitions", "Laboratory Director"],
     ["Billing", "24 hours", "Record charges on paper; enter after recovery", "Charge sheets", "CFO"]]}),
  ("Roles and Communication", "บทบาทและการสื่อสาร", "Define continuity roles and communication flow.", "กำหนดบทบาทด้านความต่อเนื่องและลำดับการสื่อสาร",
   ["Crisis Management Team (RC-PLN-003) sets priorities and approves communications.", "Department continuity leads run workarounds and report status every [4] hours.",
    "IT recovery follows RC-PLN-002 and reports progress to the Crisis Management Team (RC.CO-03).", "Staff updates follow RC-PRC-002."],
   ["ทีมบริหารภาวะวิกฤต (RC-PLN-003) กำหนดลำดับความสำคัญและอนุมัติการสื่อสาร", "ผู้นำความต่อเนื่องของแต่ละหน่วยงานดำเนินการตามทางเลือกทดแทน และรายงานสถานะทุก [4] ชั่วโมง",
    "การกู้คืนระบบ IT เป็นไปตาม RC-PLN-002 และรายงานความคืบหน้าต่อทีมบริหารภาวะวิกฤต (RC.CO-03)", "การแจ้งบุคลากรเป็นไปตาม RC-PRC-002"],
   ["The Crisis Management Team, chaired by the CEO, meets in the Riverside command room or by phone bridge.", "Ward and department heads report status every 4 hours to the nursing supervisor on duty.",
    "IT reports recovery progress against the restoration order every 2 hours.", "Staff receive updates by overhead announcement, SMS, and printed bulletins."]),
  ("Return to Normal and Deactivation", "การกลับสู่ภาวะปกติและการยุติแผน", "Define how normal operations resume and the plan is closed (RC.RP-04, RC.RP-06).", "กำหนดวิธีกลับสู่การดำเนินงานปกติและการปิดแผน (RC.RP-04, RC.RP-06)",
   ["Confirm systems are restored and validated (RC-FRM-001).", "Back-enter paper records into systems and reconcile.", "Declare the end of the continuity event and record the decision.", "Hold a lessons-learned review (ID-TPL-001)."],
   ["ยืนยันว่ากู้คืนระบบและตรวจสอบแล้ว (RC-FRM-001)", "บันทึกข้อมูลจากเอกสารกระดาษเข้าสู่ระบบและกระทบยอด", "ประกาศสิ้นสุดเหตุการณ์ด้านความต่อเนื่องและบันทึกการตัดสินใจ", "จัดทบทวนบทเรียนที่ได้รับ (ID-TPL-001)"]),
 ],
 bp=[("Test workarounds with the people who will use them, not only the plan authors.", "ทดสอบทางเลือกทดแทนกับผู้ที่จะใช้งานจริง ไม่ใช่เฉพาะผู้เขียนแผน"),
     ("Pre-print or regularly export critical lists (patients, customers, orders) for outage periods.", "พิมพ์หรือส่งออกรายการสำคัญ (ผู้ป่วย ลูกค้า คำสั่งซื้อ) ไว้ล่วงหน้าอย่างสม่ำเสมอสำหรับช่วงที่ระบบหยุด")],
 mistakes=[("Workarounds depend on the same systems that are down (for example, forms stored on the file server).", "ทางเลือกทดแทนต้องพึ่งพาระบบเดียวกับที่หยุดทำงาน (เช่น แบบฟอร์มเก็บไว้บนไฟล์เซิร์ฟเวอร์)")],
 rev="Updated in March 2026 after EX-2026-01 to add downtime kits to ward checklists and 4-hourly MAR printing.",
)

C["RC-PLN-002"] = dict(
 purpose=("This plan sets how IT restores critical systems after a disaster or cyber incident: recovery order, strategies, teams, and verification, so systems return within RTO and RPO (RC.RP-01 to RC.RP-05).",
          "แผนนี้กำหนดวิธีที่ฝ่าย IT กู้คืนระบบสำคัญหลังภัยพิบัติหรือเหตุการณ์ไซเบอร์ ได้แก่ ลำดับการกู้คืน กลยุทธ์ ทีม และการตรวจสอบ เพื่อให้ระบบกลับมาภายใน RTO และ RPO (RC.RP-01 ถึง RC.RP-05)"),
 sections=[
  ("Recovery Order and Strategy", "ลำดับและกลยุทธ์การกู้คืน", "List systems in recovery order with strategy, RTO, and RPO.", "ระบุระบบตามลำดับการกู้คืนพร้อมกลยุทธ์ RTO และ RPO",
   {"t": ["Order", "System or layer", "Strategy", "RTO", "RPO"], "r": [
     ["1", "Network core, firewalls, DNS", "Redundant hardware; configuration backups", "[2] hours", "Not applicable"], ["2", "Identity (directory, MFA)", "Rebuild or restore from clean backup", "[4] hours", "[24] hours"],
     ["3", "Critical business applications", "Fail over to DR site or restore from immutable backup", "Per BIA", "Per BIA"], ["4", "Email and collaboration", "Cloud service; restore mailboxes if needed", "[8] hours", "[24] hours"],
     ["5", "Other applications", "Restore from backup", "Per BIA", "Per BIA"]], "w": [1.4, 4.0, 6.0, 2.5, 2.6]},
   {"t": ["ลำดับ", "ระบบหรือชั้น", "กลยุทธ์", "RTO", "RPO"], "r": [
     ["1", "แกนหลักเครือข่าย ไฟร์วอลล์ DNS", "อุปกรณ์สำรองและการสำรองการตั้งค่า", "[2] ชั่วโมง", "ไม่เกี่ยวข้อง"], ["2", "ระบบตัวตน (ไดเรกทอรี MFA)", "สร้างใหม่หรือกู้คืนจากข้อมูลสำรองที่สะอาด", "[4] ชั่วโมง", "[24] ชั่วโมง"],
     ["3", "แอปพลิเคชันทางธุรกิจที่สำคัญ", "สลับไปยังศูนย์สำรองหรือกู้คืนจากข้อมูลสำรองที่แก้ไขไม่ได้", "ตาม BIA", "ตาม BIA"], ["4", "อีเมลและระบบทำงานร่วมกัน", "บริการคลาวด์ และกู้คืนกล่องจดหมายเมื่อจำเป็น", "[8] ชั่วโมง", "[24] ชั่วโมง"],
     ["5", "แอปพลิเคชันอื่น", "กู้คืนจากข้อมูลสำรอง", "ตาม BIA", "ตาม BIA"]], "w": [1.4, 4.0, 6.0, 2.5, 2.6]},
   {"t": ["Order", "System", "Strategy", "RTO", "RPO"], "r": [
     ["1", "Core network and firewalls (both hospitals)", "Redundant pairs; configs in offline vault", "2 hours", "Not applicable"],
     ["2", "Active Directory and Entra ID", "Restore domain controller from immutable backup; clean rebuild if compromised", "4 hours", "24 hours"],
     ["3", "HIS", "Fail over to Nonthaburi DR site (replicated) or restore from immutable backup", "4 hours", "15 minutes"],
     ["4", "LIS and PACS", "Restore at DR site; modalities buffer locally", "8 hours", "1 hour"],
     ["5", "ERP (private cloud)", "Provider recovery per contract", "24 hours", "4 hours"], ["6", "Microsoft 365", "Cloud service; third-party backup for mailboxes", "8 hours", "24 hours"]], "w": [1.4, 4.0, 6.0, 2.5, 2.6]}),
  ("Recovery Steps and Verification", "ขั้นตอนและการตรวจสอบการกู้คืน", "Describe the recovery sequence and checks (RC.RP-03, RC.RP-05).", "อธิบายลำดับการกู้คืนและการตรวจสอบ (RC.RP-03, RC.RP-05)",
   {"n": ["Confirm recovery is authorized and criteria in RS-PLN-001 are met (for cyber incidents).", "Select restore points and verify backup integrity before use (RC.RP-03).", "Restore systems in order using runbooks (RC-PRC-001).",
          "Verify integrity: malware scan, configuration check against baseline, monitoring re-enabled.", "System owner validates function and data; sign RC-FRM-001 (RC.RP-05).", "Return users in a controlled way and monitor closely for re-compromise."]},
   {"n": ["ยืนยันว่าได้รับอนุมัติให้กู้คืน และเป็นไปตามเกณฑ์ใน RS-PLN-001 (กรณีเหตุการณ์ไซเบอร์)", "เลือกจุดกู้คืนและตรวจสอบความถูกต้องของข้อมูลสำรองก่อนใช้ (RC.RP-03)", "กู้คืนระบบตามลำดับโดยใช้คู่มือการกู้คืน (RC-PRC-001)",
          "ตรวจสอบความถูกต้อง ได้แก่ สแกนมัลแวร์ ตรวจสอบการตั้งค่าเทียบกับมาตรฐาน และเปิดการเฝ้าระวังอีกครั้ง", "เจ้าของระบบตรวจสอบการทำงานและข้อมูล และลงนามใน RC-FRM-001 (RC.RP-05)", "ให้ผู้ใช้กลับมาใช้งานอย่างมีการควบคุม และเฝ้าระวังใกล้ชิดเพื่อป้องกันการถูกโจมตีซ้ำ"]}),
 ],
 bp=[("Recover identity and network first; nothing else works without them.", "กู้คืนระบบตัวตนและเครือข่ายก่อน เพราะระบบอื่นใช้งานไม่ได้หากไม่มีสองส่วนนี้"),
     ("Keep DR documentation and credentials available offline.", "เก็บเอกสาร DR และข้อมูลเข้าสู่ระบบไว้แบบออฟไลน์")],
 mistakes=[("DR plan assumes a clean environment and has no steps for ransomware where backups and identity may be compromised.", "แผน DR สันนิษฐานว่าสภาพแวดล้อมสะอาด และไม่มีขั้นตอนสำหรับแรนซัมแวร์ซึ่งข้อมูลสำรองและระบบตัวตนอาจถูกโจมตี")],
 rev="Updated in May 2026 after DR-2026-01; HIS failover measured at 2 hours 50 minutes and the LIS license server step added.",
)

C["RC-PRC-001"] = dict(
 purpose=("This runbook template gives system-specific, step-by-step recovery instructions that a trained engineer can follow under pressure (RC.RP-02, RC.RP-03, RC.RP-05).",
          "แม่แบบคู่มือนี้ให้ขั้นตอนการกู้คืนเฉพาะระบบทีละขั้นตอน ที่วิศวกรที่ผ่านการอบรมสามารถปฏิบัติตามได้ภายใต้ความกดดัน (RC.RP-02, RC.RP-03, RC.RP-05)"),
 sections=[
  ("Runbook Header", "ข้อมูลส่วนหัวของคู่มือ", "Record the system, dependencies, and objectives.", "บันทึกระบบ การพึ่งพา และเป้าหมาย",
   {"t": ["Item", "Content"], "r": [["System and owner", ""], ["RTO and RPO", ""], ["Dependencies (must be up first)", ""], ["Backup location and copy types", ""], ["Credentials location (vault reference)", ""], ["Vendor support contact", ""]], "w": [6.0, 10.5]},
   {"t": ["หัวข้อ", "เนื้อหา"], "r": [["ระบบและเจ้าของ", ""], ["RTO และ RPO", ""], ["การพึ่งพา (ต้องทำงานก่อน)", ""], ["ที่ตั้งข้อมูลสำรองและประเภทสำเนา", ""], ["ที่เก็บข้อมูลเข้าสู่ระบบ (อ้างอิง Vault)", ""], ["ช่องทางติดต่อผู้ขาย", ""]], "w": [6.0, 10.5]},
   {"t": ["Item", "Content (HIS runbook)"], "r": [["System and owner", "HIS; CIO with Medical Director"], ["RTO and RPO", "4 hours; 15 minutes"], ["Dependencies", "Core network, Active Directory, DNS, database cluster, interface engine"], ["Backup location", "Immutable repository at Riverside; replica at Nonthaburi DR site; weekly offline copy"], ["Credentials", "PAM vault entries HIS-DB-ADM and HIS-APP-ADM; sealed break-glass envelope"], ["Vendor support", "HIS Vendor A critical line (RS-REG-002)"]], "w": [6.0, 10.5]}),
  ("Recovery Steps", "ขั้นตอนการกู้คืน", "Write numbered steps with expected results and checks.", "เขียนขั้นตอนเป็นลำดับพร้อมผลที่คาดหวังและการตรวจสอบ",
   {"t": ["Step", "Action", "Expected result", "Check"], "r": [["1", "[Action]", "", ""], ["2", "[Action]", "", ""], ["3", "[Action]", "", ""]]},
   {"t": ["ขั้นตอน", "การดำเนินการ", "ผลที่คาดหวัง", "การตรวจสอบ"], "r": [["1", "[การดำเนินการ]", "", ""], ["2", "[การดำเนินการ]", "", ""], ["3", "[การดำเนินการ]", "", ""]]},
   {"t": ["Step", "Action", "Expected result", "Check"], "r": [
     ["1", "Confirm network, AD, and DNS are up at the DR site", "Domain logon works", "Test account logon"],
     ["2", "Select restore point; verify checksum and scan in isolated network", "Clean restore point", "Security Engineer sign-off"],
     ["3", "Restore or promote the HIS database replica", "Database online, consistent", "Database integrity check"],
     ["4", "Start HIS application servers; update DNS alias", "Application responds", "Login page loads"],
     ["5", "Start the interface engine; replay queued messages", "PACS and LIS orders flow", "Test order end to end"],
     ["6", "Clinical validation with super-users on two wards", "Patient records correct", "HIS analyst checklist"],
     ["7", "Release to users; monitor for 24 hours", "Normal operation", "MSSP heightened monitoring"]], "w": [1.2, 6.8, 4.5, 4.0]}),
 ],
 bp=[("Have someone other than the author run the runbook in tests.", "ให้ผู้อื่นที่ไม่ใช่ผู้เขียนเป็นผู้ปฏิบัติตามคู่มือในการทดสอบ"), ("Include screenshots and exact commands for complex steps.", "ใส่ภาพหน้าจอและคำสั่งที่ถูกต้องสำหรับขั้นตอนที่ซับซ้อน")],
 mistakes=[("Runbooks that say 'restore the server' without the steps, credentials, or order.", "คู่มือที่ระบุเพียงให้กู้คืนเซิร์ฟเวอร์ โดยไม่มีขั้นตอน ข้อมูลเข้าสู่ระบบ หรือลำดับ")],
)

C["RC-REC-001"] = dict(
 purpose=("This report records the objectives, scenario, results, gaps, and actions from each business continuity and disaster recovery exercise, as evidence of tested capability (RC.RP, ID.IM-02).",
          "รายงานนี้บันทึกวัตถุประสงค์ สถานการณ์ ผลลัพธ์ ช่องว่าง และการดำเนินการจากการฝึกซ้อมความต่อเนื่องทางธุรกิจและการกู้คืนระบบแต่ละครั้ง เป็นหลักฐานของความสามารถที่ผ่านการทดสอบ (RC.RP, ID.IM-02)"),
 sections=[
  ("Exercise Summary", "สรุปการฝึกซ้อม", "Record objectives, scope, participants, and scenario.", "บันทึกวัตถุประสงค์ ขอบเขต ผู้เข้าร่วม และสถานการณ์",
   {"t": ["Item", "Content"], "r": [["Exercise ID and type", ""], ["Date and duration", ""], ["Objectives", ""], ["Scenario", ""], ["Participants", ""]], "w": [5.0, 11.5]},
   {"t": ["หัวข้อ", "เนื้อหา"], "r": [["รหัสและประเภทการฝึกซ้อม", ""], ["วันที่และระยะเวลา", ""], ["วัตถุประสงค์", ""], ["สถานการณ์", ""], ["ผู้เข้าร่วม", ""]], "w": [5.0, 11.5]},
   {"t": ["Item", "Content"], "r": [["Exercise ID and type", "DR-2026-01, partial failover"], ["Date and duration", "16 May 2026, 22:00 to 06:00"], ["Objectives", "Fail over HIS and PACS to Nonthaburi within RTO; validate clinical function"], ["Scenario", "Riverside data center unavailable after ransomware isolation"], ["Participants", "IT team, HIS Vendor A, PACS Vendor B, two ward super-users, Security Manager"]], "w": [5.0, 11.5]}),
  ("Results Against Objectives", "ผลลัพธ์เทียบกับวัตถุประสงค์", "Compare actual results to objectives.", "เปรียบเทียบผลจริงกับวัตถุประสงค์",
   {"t": ["Objective", "Target", "Actual", "Met"], "r": [["[Objective]", "", "", ""]]},
   {"t": ["วัตถุประสงค์", "เป้าหมาย", "ผลจริง", "บรรลุ"], "r": [["[วัตถุประสงค์]", "", "", ""]]},
   {"t": ["Objective", "Target", "Actual", "Met"], "r": [["HIS failover", "4 hours", "2 h 50 min", "Yes"], ["PACS restore at DR", "8 hours", "5 h 30 min", "Yes"], ["LIS restore at DR", "8 hours", "Not in scope (tested 09/2026: 6 h 20 min)", "Yes (separate test)"], ["Data loss (HIS)", "15 minutes", "4 minutes", "Yes"]]}),
  ("Gaps and Actions", "ช่องว่างและการดำเนินการ", "Record gaps and assign actions.", "บันทึกช่องว่างและมอบหมายการดำเนินการ",
   {"t": ["Gap", "Action", "Owner", "Due"], "r": [["[Gap]", "", "", ""]]},
   {"t": ["ช่องว่าง", "การดำเนินการ", "ผู้รับผิดชอบ", "กำหนดเสร็จ"], "r": [["[ช่องว่าง]", "", "", ""]]},
   {"t": ["Gap", "Action", "Owner", "Due"], "r": [["DNS alias change took 40 minutes (manual)", "Script DNS failover", "IT Infrastructure Manager", "08/2026 (done)"], ["PACS vendor engineer needed VPN that was blocked by isolation", "Pre-stage vendor access at DR jump host", "Security Manager", "09/2026 (done)"]]}),
 ],
 bp=[("Measure actual recovery times and compare with RTO; report gaps to the ISSC.", "วัดเวลาการกู้คืนจริงเทียบกับ RTO และรายงานช่องว่างต่อ ISSC"), ("Keep reports as evidence for CII and audit.", "เก็บรายงานไว้เป็นหลักฐานสำหรับ CII และการตรวจสอบ")],
 mistakes=[("Declaring an exercise 'successful' without measuring against objectives.", "ประกาศว่าการฝึกซ้อมสำเร็จโดยไม่วัดผลเทียบกับวัตถุประสงค์")],
)

C["RC-FRM-001"] = dict(
 purpose=("This form confirms that a system has been restored, its integrity verified, and that it is approved for return to normal operation, and records the end of recovery (RC.RP-04 to RC.RP-06).",
          "แบบฟอร์มนี้ใช้ยืนยันว่ากู้คืนระบบแล้ว ตรวจสอบความถูกต้องแล้ว และอนุมัติให้กลับสู่การใช้งานปกติ รวมถึงบันทึกการสิ้นสุดการกู้คืน (RC.RP-04 ถึง RC.RP-06)"),
 fields=[
  ("Incident or test reference", "เลขอ้างอิงเหตุการณ์หรือการทดสอบ", "INC or DR ID.", "รหัส INC หรือ DR", ""),
  ("System restored", "ระบบที่กู้คืน", "System and environment.", "ระบบและสภาพแวดล้อม", ""),
  ("Restore point used", "จุดกู้คืนที่ใช้", "Date, time, copy type.", "วัน เวลา ประเภทสำเนา", ""),
  ("Integrity checks completed", "การตรวจสอบความถูกต้องที่ทำแล้ว", "Malware scan, baseline, monitoring enabled.", "สแกนมัลแวร์ ตรวจสอบการตั้งค่า เปิดการเฝ้าระวัง", ""),
  ("Functional validation by owner", "การตรวจสอบการทำงานโดยเจ้าของระบบ", "Tests performed and result.", "การทดสอบที่ทำและผล", ""),
  ("Data loss (actual vs RPO)", "ข้อมูลที่สูญหาย (จริงเทียบกับ RPO)", "Measured gap.", "ช่องว่างที่วัดได้", ""),
  ("Residual issues", "ปัญหาที่ยังเหลือ", "Known issues and owners.", "ปัญหาที่ทราบและผู้รับผิดชอบ", ""),
  ("End of recovery declared", "ประกาศสิ้นสุดการกู้คืน", "Date, time, by whom.", "วัน เวลา ผู้ประกาศ", ""),
 ],
 cmc_vals=["DR-2026-01", "HIS production at Nonthaburi DR site", "16 May 2026 23:56, replicated copy", "EDR scan clean; configuration compliance 100%; logs flowing to MSSP",
           "Ward 5A and 6B super-users completed admission, order, and medication checks; passed", "4 minutes vs RPO 15 minutes", "DNS alias change manual (action raised)",
           "17 May 2026 05:40 by IT Infrastructure Manager; failback completed 18 May"],
 approvals=["SYSOWN", "CISO", "ITM"],
 bp=[("Require security sign-off before returning systems after a cyber incident.", "กำหนดให้หน่วยงานความมั่นคงปลอดภัยลงนามก่อนนำระบบกลับมาใช้งานหลังเหตุการณ์ไซเบอร์")],
 mistakes=[("Users are reconnected before integrity checks, allowing re-infection.", "ให้ผู้ใช้กลับมาเชื่อมต่อก่อนตรวจสอบความถูกต้อง ทำให้ติดมัลแวร์ซ้ำ")],
)

C["RC-PLN-003"] = dict(
 purpose=("This plan sets how senior leaders manage a crisis that threatens people, operations, reputation, or legal standing, including team structure, decision-making, and stakeholder communication (RC.CO-03, RC.CO-04).",
          "แผนนี้กำหนดวิธีที่ผู้บริหารระดับสูงบริหารภาวะวิกฤตที่คุกคามบุคคล การดำเนินงาน ชื่อเสียง หรือสถานะทางกฎหมาย ได้แก่ โครงสร้างทีม การตัดสินใจ และการสื่อสารกับผู้มีส่วนได้ส่วนเสีย (RC.CO-03, RC.CO-04)"),
 sections=[
  ("Crisis Management Team", "ทีมบริหารภาวะวิกฤต", "Define membership, roles, and meeting rhythm.", "กำหนดองค์ประกอบ บทบาท และรอบการประชุม",
   {"t": ["Role", "Member", "Responsibility"], "r": [
     ["Chair", "[CEO]", "Final decisions, external spokesperson or delegate"], ["Operations", "Business heads", "Service continuity and workarounds"], ["Technology", "[CIO], [CISO]", "Incident status, recovery timeline"],
     ["Legal and compliance", "[LEGAL], [DPO]", "Notifications, legal exposure"], ["Communications", "[COMMS]", "Messages to staff, customers, media"], ["Finance", "[CFO]", "Costs, insurance, payments"], ["Coordinator", "[BCM]", "Logs decisions and actions"]], "w": [3.5, 4.5, 8.5]},
   {"t": ["บทบาท", "สมาชิก", "ความรับผิดชอบ"], "r": [
     ["ประธาน", "[CEO]", "ตัดสินใจขั้นสุดท้าย และเป็นโฆษกหรือมอบหมายผู้แทน"], ["ปฏิบัติการ", "หัวหน้าหน่วยธุรกิจ", "ความต่อเนื่องของบริการและทางเลือกทดแทน"], ["เทคโนโลยี", "[CIO] [CISO]", "สถานะเหตุการณ์และกรอบเวลาการกู้คืน"],
     ["กฎหมายและการปฏิบัติตามกฎเกณฑ์", "[LEGAL] [DPO]", "การแจ้งเหตุและความเสี่ยงทางกฎหมาย"], ["การสื่อสาร", "[COMMS]", "การสื่อสารกับบุคลากร ลูกค้า และสื่อมวลชน"], ["การเงิน", "[CFO]", "ค่าใช้จ่าย ประกันภัย การชำระเงิน"], ["ผู้ประสานงาน", "[BCM]", "บันทึกการตัดสินใจและการดำเนินการ"]], "w": [3.5, 4.5, 8.5]}),
  ("Crisis Rhythm", "จังหวะการบริหารภาวะวิกฤต", "Define the cycle of meetings, decisions, and updates.", "กำหนดรอบการประชุม การตัดสินใจ และการแจ้งความคืบหน้า",
   ["Initial meeting within 1 hour of activation.", "Situation updates every 2 to 4 hours: facts, impact, decisions needed, next update time.", "Decision log maintained by the [BCM] Coordinator.", "Stakeholder updates issued after each cycle (RC-PRC-002)."],
   ["ประชุมครั้งแรกภายใน 1 ชั่วโมงหลังเปิดใช้แผน", "รายงานสถานการณ์ทุก 2 ถึง 4 ชั่วโมง ได้แก่ ข้อเท็จจริง ผลกระทบ เรื่องที่ต้องตัดสินใจ และเวลาการรายงานครั้งถัดไป", "ผู้ประสานงาน [BCM] บันทึกการตัดสินใจ", "แจ้งความคืบหน้าต่อผู้มีส่วนได้ส่วนเสียหลังแต่ละรอบ (RC-PRC-002)"]),
 ],
 bp=[("Separate the crisis team (strategic) from the incident response team (technical) to avoid micromanagement.", "แยกทีมบริหารภาวะวิกฤต (เชิงกลยุทธ์) ออกจากทีมรับมือเหตุการณ์ (เชิงเทคนิค) เพื่อหลีกเลี่ยงการก้าวก่ายงาน"),
     ("Prepare a crisis room and phone bridge that do not depend on corporate IT.", "เตรียมห้องบริหารภาวะวิกฤตและสายประชุมทางโทรศัพท์ที่ไม่ต้องพึ่งพาระบบ IT ขององค์กร")],
 mistakes=[("Executives join technical calls and slow the response.", "ผู้บริหารเข้าร่วมการประชุมทางเทคนิคและทำให้การรับมือล่าช้า")],
)

C["RC-PRC-002"] = dict(
 purpose=("This procedure defines how recovery progress and incident information are communicated to staff, customers, partners, media, and the public through approved channels and messages (RC.CO-03, RC.CO-04).",
          "ระเบียบปฏิบัตินี้กำหนดวิธีสื่อสารความคืบหน้าการกู้คืนและข้อมูลเหตุการณ์แก่บุคลากร ลูกค้า คู่ค้า สื่อมวลชน และสาธารณะ ผ่านช่องทางและข้อความที่ได้รับอนุมัติ (RC.CO-03, RC.CO-04)"),
 sections=[
  ("Communication Matrix", "ตารางการสื่อสาร", "Define audience, owner, channel, and frequency.", "กำหนดกลุ่มเป้าหมาย ผู้รับผิดชอบ ช่องทาง และความถี่",
   {"t": ["Audience", "Owner", "Channel", "Frequency"], "r": [
     ["Staff", "[COMMS] with [HR]", "SMS, intranet, managers' briefings", "Each crisis cycle"], ["Customers", "[COMMS] and business heads", "Website, call center script, email", "As needed"],
     ["Media", "[CEO] or spokesperson", "Statements, press briefing", "Only approved statements"], ["Regulators", "[CISO], [DPO]", "Formal channels (RS-PRC-003)", "Per legal requirements"],
     ["Partners and suppliers", "Business owners", "Direct contact", "As needed"]], "w": [3.5, 4.5, 5.0, 3.5]},
   {"t": ["กลุ่มเป้าหมาย", "ผู้รับผิดชอบ", "ช่องทาง", "ความถี่"], "r": [
     ["บุคลากร", "[COMMS] ร่วมกับ [HR]", "SMS อินทราเน็ต การบรรยายสรุปโดยหัวหน้างาน", "ทุกรอบการบริหารภาวะวิกฤต"], ["ลูกค้า", "[COMMS] และหัวหน้าหน่วยธุรกิจ", "เว็บไซต์ สคริปต์ศูนย์บริการลูกค้า อีเมล", "ตามความจำเป็น"],
     ["สื่อมวลชน", "[CEO] หรือโฆษก", "แถลงการณ์ การแถลงข่าว", "เฉพาะแถลงการณ์ที่อนุมัติ"], ["หน่วยงานกำกับ", "[CISO] [DPO]", "ช่องทางทางการ (RS-PRC-003)", "ตามข้อกำหนดทางกฎหมาย"],
     ["คู่ค้าและผู้ให้บริการ", "เจ้าของธุรกิจ", "ติดต่อโดยตรง", "ตามความจำเป็น"]], "w": [3.5, 4.5, 5.0, 3.5]},
   {"t": ["Audience", "Owner", "Channel", "Frequency"], "r": [
     ["Staff", "Corporate Communications with HR", "SMS broadcast, overhead announcement, printed bulletins at nursing stations", "Every 4 hours during SEV-1"], ["Patients and families", "Corporate Communications and Director of Patient Experience", "Signage, front-desk script, website, call center", "As needed"],
     ["Media", "CEO or designated spokesperson", "Approved statements only", "As approved"], ["Regulators (PDPC, NCSA, MOPH)", "Security Manager, DPO", "Formal channels per RS-PRC-003", "Per legal requirements"],
     ["Referral hospitals and insurers", "Medical Director, CFO", "Direct phone and letter", "As needed"]], "w": [3.5, 4.5, 5.0, 3.5]}),
  ("Message Principles", "หลักการของข้อความ", "State rules for content of messages.", "ระบุกฎสำหรับเนื้อหาของข้อความ",
   ["State facts only; do not speculate on cause or attacker.", "Say what people should do and when the next update will come.", "Use pre-approved templates (RC-TPL-001).", "Staff must not speak to media or post on social media about the incident."],
   ["ระบุเฉพาะข้อเท็จจริง และไม่คาดเดาสาเหตุหรือผู้โจมตี", "ระบุสิ่งที่ผู้รับสารควรทำ และเวลาที่จะแจ้งความคืบหน้าครั้งถัดไป", "ใช้แม่แบบที่อนุมัติล่วงหน้า (RC-TPL-001)", "บุคลากรต้องไม่ให้ข้อมูลแก่สื่อมวลชนหรือโพสต์บนสื่อสังคมออนไลน์เกี่ยวกับเหตุการณ์"]),
 ],
 bp=[("Prepare holding statements in advance so the first message goes out within the first hour.", "เตรียมแถลงการณ์เบื้องต้นไว้ล่วงหน้า เพื่อให้ข้อความแรกออกได้ภายในชั่วโมงแรก"), ("Use channels that work when corporate email is down.", "ใช้ช่องทางที่ยังใช้ได้เมื่ออีเมลขององค์กรใช้งานไม่ได้")],
 mistakes=[("Silence for days, which lets rumors fill the gap.", "เงียบหลายวัน ทำให้ข่าวลือเข้ามาแทนที่")],
)

C["RC-TPL-001"] = dict(
 purpose=("These templates provide pre-approved messages for staff, customers, and the public at each stage of a cyber incident and recovery (RC.CO-04).",
          "แม่แบบนี้มีข้อความที่อนุมัติไว้ล่วงหน้าสำหรับบุคลากร ลูกค้า และสาธารณะ ในแต่ละช่วงของเหตุการณ์ไซเบอร์และการกู้คืน (RC.CO-04)"),
 sections=[
  ("Holding Statement (First Hours)", "แถลงการณ์เบื้องต้น (ช่วงชั่วโมงแรก)", "Provide a short statement for the first public response.", "จัดทำแถลงการณ์สั้นสำหรับการตอบสนองต่อสาธารณะครั้งแรก",
   "[Organization Name] is responding to an IT incident affecting some of our systems. We have activated our response plans and are working with specialists to restore services safely. [Critical service] continues through alternative procedures. We will provide an update by [time].",
   "[ชื่อองค์กร] กำลังดำเนินการรับมือเหตุการณ์ด้านระบบสารสนเทศที่กระทบระบบบางส่วน องค์กรได้เปิดใช้แผนรับมือและทำงานร่วมกับผู้เชี่ยวชาญเพื่อกู้คืนบริการอย่างปลอดภัย [บริการสำคัญ] ยังคงให้บริการได้ผ่านขั้นตอนทดแทน องค์กรจะแจ้งความคืบหน้าภายใน [เวลา]",
   "Chaophraya Medical Center is responding to an IT incident affecting some hospital systems. Patient care continues safely using our established downtime procedures, and emergency services remain open. We have activated our response plans and are working with specialists to restore systems. We will provide an update by [time]."),
  ("Staff Update", "การแจ้งบุคลากร", "Provide a template for internal updates.", "จัดทำแม่แบบสำหรับการแจ้งภายใน",
   "Update [number], [time]: Systems affected: [list]. What to do: [instructions, for example, use downtime forms, do not connect devices]. What not to do: do not discuss the incident externally. Next update: [time]. Questions: [contact].",
   "การแจ้งครั้งที่ [ลำดับ] เวลา [เวลา]: ระบบที่ได้รับผลกระทบ: [รายการ] สิ่งที่ต้องทำ: [คำแนะนำ เช่น ใช้แบบฟอร์มทดแทน ห้ามเชื่อมต่ออุปกรณ์] สิ่งที่ห้ามทำ: ห้ามเปิดเผยเรื่องเหตุการณ์ต่อภายนอก การแจ้งครั้งถัดไป: [เวลา] สอบถาม: [ช่องทางติดต่อ]",
   "Update [number], [time]: HIS, PACS, and LIS are unavailable. What to do: use downtime kits; phone critical results; do not reconnect any computer that IT has disconnected. Do not discuss the incident with patients' relatives or on social media; refer questions to the nursing supervisor. Next update: [time]. Questions: nursing supervisor on duty or the command room at ext. 1000."),
  ("Recovery Update", "การแจ้งความคืบหน้าการกู้คืน", "Provide a template for public recovery updates.", "จัดทำแม่แบบสำหรับการแจ้งความคืบหน้าการกู้คืนต่อสาธารณะ",
   "[Organization Name] has restored [services]. We are completing checks on remaining systems and expect [timeline]. [If personal data affected: We are contacting affected individuals directly.] We thank our customers for their patience.",
   "[ชื่อองค์กร] ได้กู้คืน [บริการ] แล้ว และกำลังตรวจสอบระบบที่เหลือ คาดว่าจะแล้วเสร็จภายใน [กรอบเวลา] [กรณีข้อมูลส่วนบุคคลได้รับผลกระทบ: องค์กรกำลังติดต่อบุคคลที่ได้รับผลกระทบโดยตรง] องค์กรขอขอบคุณผู้รับบริการสำหรับความอดทน"),
 ],
 bp=[("Have Legal and Communications approve templates annually.", "ให้ฝ่ายกฎหมายและฝ่ายสื่อสารอนุมัติแม่แบบทุกปี"), ("Prepare Thai and English versions.", "จัดทำฉบับภาษาไทยและภาษาอังกฤษ")],
 mistakes=[("Using 'no evidence of data theft' before the investigation can support it.", "ใช้ข้อความว่าไม่พบหลักฐานการขโมยข้อมูลก่อนที่ผลการสอบสวนจะยืนยันได้")],
)
