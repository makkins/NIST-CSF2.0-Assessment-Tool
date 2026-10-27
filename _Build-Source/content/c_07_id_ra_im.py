# -*- coding: utf-8 -*-
# ID.RA Risk Assessment and ID.IM Improvement
C = {}

C["ID-REG-005"] = dict(
 purpose=("This register records each identified cybersecurity risk scenario with its inherent and residual rating, treatment decision, owner, and review history, as the single source of truth for cyber risk (ID.RA-03 to ID.RA-06; ISO/IEC 27001:2022 Clause 8.2).",
          "ทะเบียนนี้บันทึกสถานการณ์ความเสี่ยงด้านไซเบอร์แต่ละรายการ พร้อมระดับความเสี่ยงก่อนและหลังมีมาตรการควบคุม การตัดสินใจจัดการ เจ้าของ และประวัติการทบทวน เพื่อเป็นแหล่งข้อมูลหลักของความเสี่ยงด้านไซเบอร์ (ID.RA-03 ถึง ID.RA-06; ISO/IEC 27001:2022 ข้อ 8.2)"),
 fields=[
  ("Risk ID", "รหัสความเสี่ยง", "Unique, never reused.", "รหัสไม่ซ้ำและไม่นำกลับมาใช้", "R-001"),
  ("Risk scenario", "สถานการณ์ความเสี่ยง", "Threat exploits vulnerability in asset, causing impact.", "ภัยคุกคามใช้ประโยชน์จากช่องโหว่ในทรัพย์สิน ก่อให้เกิดผลกระทบ", ("Ransomware encrypts core systems", "แรนซัมแวร์เข้ารหัสระบบหลัก")),
  ("Asset or service", "ทรัพย์สินหรือบริการ", "From inventories or BIA.", "จากทะเบียนทรัพย์สินหรือ BIA", ""),
  ("Existing controls", "มาตรการควบคุมที่มีอยู่", "Controls in place today.", "มาตรการที่มีอยู่ในปัจจุบัน", ""),
  ("Inherent (L x I)", "ความเสี่ยงก่อนมีมาตรการ (L x I)", "Likelihood x impact without controls.", "โอกาสเกิด x ผลกระทบ เมื่อไม่มีมาตรการ", "5 x 5 = 25"),
  ("Residual (L x I) and level", "ความเสี่ยงคงเหลือ (L x I) และระดับ", "Rating with existing controls.", "ระดับเมื่อมีมาตรการปัจจุบัน", "3 x 4 = 12 High"),
  ("Treatment", "การจัดการ", "Mitigate, Avoid, Transfer, Accept.", "ลด หลีกเลี่ยง โอน ยอมรับ", "Mitigate"),
  ("Plan reference and target", "แผนอ้างอิงและเป้าหมาย", "ID-PLN-001 item and target residual.", "รายการใน ID-PLN-001 และระดับเป้าหมาย", "RTP-01, target Medium"),
  ("Risk owner", "เจ้าของความเสี่ยง", "Accountable executive.", "ผู้บริหารที่รับผิดชอบ", ""),
  ("Status", "สถานะ", "Open, In treatment, Accepted, Closed.", "เปิด อยู่ระหว่างจัดการ ยอมรับ ปิด", "In treatment"),
  ("Last reviewed (version)", "ทบทวนล่าสุด (ฉบับ)", "Date and register version.", "วันที่และฉบับของทะเบียน", "30/09/2026 (v2.3)"),
 ],
 rows=[
  ["R-001", "Ransomware enters through phishing or exposed remote access and encrypts HIS, PACS, and LIS, stopping care", "HIS, PACS, LIS; emergency and inpatient care", "EDR, immutable backup (tested monthly), MFA for remote access, MSSP 24x7 monitoring", "5 x 5 = 25", "3 x 4 = 12 High", "Mitigate", "RTP-01 PAM and segmentation; target 2 x 4 = 8 Medium by 06/2027", "CIO", "In treatment", "30/09/2026 (v2.3)"],
  ["R-002", "Attacker uses stolen staff credentials to access patient records in HIS", "HIS; patient data", "MFA for remote and admin access, quarterly access review, audit logs", "4 x 4 = 16", "3 x 4 = 12 High", "Mitigate", "RTP-02 MFA for all HIS access through badge tap plus PIN; target Medium", "Medical Director", "In treatment", "30/09/2026 (v2.3)"],
  ["R-003", "Vendor remote access is misused or compromised to reach PACS and modalities", "PACS, medical devices", "Jump host with session recording since 08/2026, named vendor accounts", "4 x 4 = 16", "2 x 4 = 8 Medium", "Mitigate", "RTP-03 complete for all Tier 1 vendors by 12/2026", "CIO", "In treatment", "30/09/2026 (v2.3)"],
  ["R-007", "Malware on unsupported modality workstations stops imaging", "CT and MRI workstations", "Medical device VLAN, USB disabled, network monitoring", "4 x 4 = 16", "3 x 3 = 9 Medium", "Accept (time-bound)", "EXC-2026-007 until vendor certifies EDR", "Director of Radiology", "Accepted", "30/09/2026 (v2.3)"],
  ["R-011", "Personal data breach through email misdirection or uncontrolled file sharing", "Microsoft 365", "Sensitivity labels (pilot), external sharing restrictions, awareness training", "4 x 3 = 12", "3 x 3 = 9 Medium", "Mitigate", "RTP-06 DLP deferred to 2027 after budget cut", "DPO", "Open", "30/09/2026 (v2.3)"],
  ["R-016", "Unsupported nurse call server compromised, stopping nurse call alerts in one building", "Nurse call system", "Isolated segment, allowlisting, manual rounds procedure", "3 x 4 = 12", "2 x 4 = 8 Medium", "Accept (time-bound)", "GV-FRM-001 acceptance until replacement in 2027", "Director of Nursing", "Accepted", "30/09/2026 (v2.3)"],
 ],
 changelog=[
  ["v2.0", "22 January 2026", "Annual reassessment after IA-2025-04 and MR-2026-01: 18 risks reviewed; R-001 reduced from 16 to 12 after immutable backup; R-016 added.", "Security Manager"],
  ["v2.1", "31 March 2026", "Q1 review: MSSP onboarding reduced R-001 likelihood evidence; R-002 treatment plan approved by ISSC.", "Security Manager"],
  ["v2.2", "30 June 2026", "Q2 review: R-011 updated after email misdirection near miss (INC-2026-014 follow-up); DLP deferred after budget cut.", "Security Manager"],
  ["v2.3", "30 September 2026", "Q3 review: R-003 residual reduced to 8 after vendor jump host rollout; owners confirmed.", "Security Manager"],
 ],
 cmc_note="CMC's register holds 18 risk scenarios. The excerpt shows six. The Security Manager facilitates; each risk owner approves the rating and treatment. The register version increases at each quarterly review.",
 bp=[("Keep 15 to 30 well-written scenarios rather than hundreds of control gaps.", "จัดทำสถานการณ์ความเสี่ยงที่เขียนดี 15 ถึง 30 รายการ แทนช่องว่างของมาตรการควบคุมหลายร้อยรายการ"),
     ("Version the register at each review and keep prior versions, so auditors can see how risks changed.", "กำหนดฉบับของทะเบียนในการทบทวนแต่ละครั้งและเก็บฉบับก่อนหน้า เพื่อให้ผู้ตรวจสอบเห็นการเปลี่ยนแปลงของความเสี่ยง"),
     ("Show inherent and residual ratings to demonstrate control value to management.", "แสดงระดับความเสี่ยงก่อนและหลังมีมาตรการ เพื่อแสดงคุณค่าของมาตรการควบคุมต่อผู้บริหาร"),
     ("Feed the top cyber risks into the enterprise risk register with the same scale.", "ส่งความเสี่ยงด้านไซเบอร์ที่สำคัญเข้าสู่ทะเบียนความเสี่ยงองค์กรด้วยมาตรวัดเดียวกัน")],
 mistakes=[("Risk owners are IT staff rather than business executives.", "เจ้าของความเสี่ยงเป็นเจ้าหน้าที่ IT แทนที่จะเป็นผู้บริหารธุรกิจ"),
           ("Residual risk is lowered for planned controls that are not yet implemented.", "ลดระดับความเสี่ยงคงเหลือจากมาตรการที่ยังอยู่ในแผนและยังไม่ได้ดำเนินการ")],
 rev="Register structure updated in January 2026 to add inherent rating and register version column after the internal audit.",
)

C["ID-PLN-001"] = dict(
 purpose=("This plan sets out the actions chosen to treat each risk, with owners, resources, dates, and target residual risk, and tracks progress (ID.RA-06; ISO/IEC 27001:2022 Clause 6.1.3(e) and 8.3).",
          "แผนนี้กำหนดการดำเนินการที่เลือกเพื่อจัดการความเสี่ยงแต่ละรายการ พร้อมผู้รับผิดชอบ ทรัพยากร กำหนดเวลา และระดับความเสี่ยงคงเหลือเป้าหมาย และใช้ติดตามความคืบหน้า (ID.RA-06; ISO/IEC 27001:2022 ข้อ 6.1.3(e) และ 8.3)"),
 sections=[
  ("Treatment Actions", "การดำเนินการจัดการความเสี่ยง", "List each action with linked risk, owner, resources, dates, and target.", "ระบุการดำเนินการแต่ละรายการพร้อมความเสี่ยงที่เชื่อมโยง ผู้รับผิดชอบ ทรัพยากร กำหนดเวลา และเป้าหมาย",
   {"t": ["Plan ID", "Risk ID", "Action", "Owner", "Budget", "Due", "Target residual", "Status"], "r": [["RTP-01", "[R-xxx]", "", "", "", "", "", ""], ["RTP-02", "[R-xxx]", "", "", "", "", "", ""]]},
   {"t": ["รหัสแผน", "รหัสความเสี่ยง", "การดำเนินการ", "ผู้รับผิดชอบ", "งบประมาณ", "กำหนดเสร็จ", "เป้าหมายคงเหลือ", "สถานะ"], "r": [["RTP-01", "[R-xxx]", "", "", "", "", "", ""], ["RTP-02", "[R-xxx]", "", "", "", "", "", ""]]},
   {"t": ["Plan ID", "Risk ID", "Action", "Owner", "Budget (THB)", "Due", "Target", "Status"], "r": [
     ["RTP-01", "R-001", "Privileged access management for domain and HIS admins; server zone segmentation", "IT Infrastructure Manager", "3,100,000", "06/2027", "8 Medium", "60%"],
     ["RTP-02", "R-002", "Badge tap plus PIN for shared clinical workstations; MFA for all HIS access", "CIO", "1,400,000", "03/2027", "8 Medium", "Pilot done"],
     ["RTP-03", "R-003", "All Tier 1 vendors through jump host with session recording", "Security Manager", "Within existing PAM", "12/2026", "8 Medium", "80%"],
     ["RTP-04", "R-007", "Medical device VLAN phase 2 (remaining wards)", "Facilities and Engineering Manager", "2,100,000 (2027 request)", "12/2027", "6 Medium", "Planned"],
     ["RTP-06", "R-011", "Data loss prevention for Microsoft 365", "DPO", "Deferred", "2027", "6 Medium", "Deferred"]]}),
  ("Progress Reporting", "การรายงานความคืบหน้า", "Define how progress is reviewed and reported.", "กำหนดวิธีทบทวนและรายงานความคืบหน้า",
   "Owners update status monthly. The [CISO] reports progress, delays, and changes in target dates to the [ISSC] each quarter. When an action is complete, the [CISO] re-rates the residual risk and updates ID-REG-005.",
   "ผู้รับผิดชอบปรับปรุงสถานะทุกเดือน [CISO] รายงานความคืบหน้า ความล่าช้า และการเปลี่ยนแปลงกำหนดเวลาต่อ [ISSC] ทุกไตรมาส เมื่อดำเนินการเสร็จ [CISO] ประเมินความเสี่ยงคงเหลือใหม่และปรับปรุง ID-REG-005"),
 ],
 bp=[("Get risk owner approval of the plan and their acceptance of the remaining residual risk (ISO/IEC 27001:2022 Clause 6.1.3(f)).", "ให้เจ้าของความเสี่ยงอนุมัติแผนและยอมรับความเสี่ยงคงเหลือ (ISO/IEC 27001:2022 ข้อ 6.1.3(f))"),
     ("Break large actions into milestones with measurable completion criteria.", "แบ่งการดำเนินการขนาดใหญ่เป็นเป้าหมายย่อยที่มีเกณฑ์ความสำเร็จวัดผลได้")],
 mistakes=[("Plans with no budget or owner, which never progress.", "แผนที่ไม่มีงบประมาณหรือผู้รับผิดชอบ จึงไม่มีความคืบหน้า")],
)

C["ID-RPT-003"] = dict(
 purpose=("This report presents the results of the periodic cybersecurity risk assessment, including scope, method, key risks, and recommendations, and serves as the annual risk assessment for CII under CSA s.54.",
          "รายงานนี้นำเสนอผลการประเมินความเสี่ยงด้านไซเบอร์ตามรอบ ได้แก่ ขอบเขต วิธีการ ความเสี่ยงสำคัญ และข้อเสนอแนะ และใช้เป็นรายงานการประเมินความเสี่ยงประจำปีของ CII ตาม พ.ร.บ.ไซเบอร์ฯ มาตรา 54"),
 sections=[
  ("Executive Summary", "บทสรุปผู้บริหาร", "State the overall risk position and top messages first (Pyramid Principle).", "ระบุภาพรวมความเสี่ยงและข้อความสำคัญก่อน (Pyramid Principle)",
   "Overall cyber risk is [within or above] appetite. [Number] risks are High or Critical. The three priorities are [priority 1], [priority 2], and [priority 3].",
   "ความเสี่ยงด้านไซเบอร์โดยรวม [อยู่ภายใน หรือ เกิน] ระดับที่ยอมรับได้ มีความเสี่ยงระดับสูงหรือวิกฤต [จำนวน] รายการ ลำดับความสำคัญ 3 อันดับแรก ได้แก่ [ลำดับที่ 1] [ลำดับที่ 2] และ [ลำดับที่ 3]",
   "Overall cyber risk is above appetite in two areas: ransomware impact on clinical systems and credential misuse in HIS. Two of 18 risks are High; none are Critical (down from three Critical in 2025). Priorities for 2027: complete privileged access management, extend MFA to all HIS access, and finish medical device network isolation."),
  ("Scope and Method", "ขอบเขตและวิธีการ", "State scope, period, assessor, and method used.", "ระบุขอบเขต ช่วงเวลา ผู้ประเมิน และวิธีการที่ใช้",
   ["Scope: [systems, sites, processes].", "Period: [dates].", "Assessor: [internal team or external assessor].", "Method: GV-PRC-001 based on NIST SP 800-30 Rev. 1; inputs from vulnerability scans, penetration tests, audits, incidents, and threat intelligence."],
   ["ขอบเขต: [ระบบ สถานที่ กระบวนการ]", "ช่วงเวลา: [วันที่]", "ผู้ประเมิน: [ทีมภายในหรือผู้ประเมินภายนอก]", "วิธีการ: GV-PRC-001 ตาม NIST SP 800-30 Rev. 1 โดยใช้ข้อมูลจากการสแกนช่องโหว่ การทดสอบเจาะระบบ การตรวจสอบ เหตุการณ์ และข้อมูลข่าวกรองภัยคุกคาม"],
   ["Scope: all CMC critical information infrastructure systems (HIS, PACS, LIS, network, identity) at both hospitals.", "Period: August to October 2026.", "Assessor: external assessor engaged under CSA s.54, with the Security Manager.", "Method: GV-PRC-001; inputs from the 2026 penetration test, IA-2025-04, MSSP incident data, and ThaiCERT advisories."]),
  ("Key Risks and Recommendations", "ความเสี่ยงสำคัญและข้อเสนอแนะ", "Summarize top risks with rating, trend, and recommendation.", "สรุปความเสี่ยงสำคัญพร้อมระดับ แนวโน้ม และข้อเสนอแนะ",
   {"t": ["Risk", "Residual", "Trend", "Recommendation"], "r": [["[R-xxx]", "", "", ""]]},
   {"t": ["ความเสี่ยง", "ระดับคงเหลือ", "แนวโน้ม", "ข้อเสนอแนะ"], "r": [["[R-xxx]", "", "", ""]]},
   {"t": ["Risk", "Residual", "Trend", "Recommendation"], "r": [
     ["R-001 Ransomware on clinical systems", "12 High", "Improving (16 to 12)", "Complete PAM and server segmentation (RTP-01)"],
     ["R-002 Credential misuse in HIS", "12 High", "Stable", "MFA for all HIS access through badge tap plus PIN (RTP-02)"],
     ["R-003 Vendor remote access", "8 Medium", "Improving (12 to 8)", "Finish jump host onboarding for remaining vendors"],
     ["R-011 Personal data leakage via Microsoft 365", "9 Medium", "Stable", "Fund DLP in 2027"]]}),
  ("Submission", "การส่งรายงาน", "Record submission to NCSA and the regulator where the organization is CII.", "บันทึกการส่งรายงานต่อ สกมช. และหน่วยงานกำกับดูแลกรณีองค์กรเป็น CII",
   "For CII: submit the summary report to NCSA within 30 days of completion (CSA s.54) and to the [Sector Regulator]. Record the submission reference here. [VERIFY current submission deadline and format.]",
   "สำหรับ CII: ส่งรายงานสรุปต่อ สกมช. ภายใน 30 วันนับแต่ประเมินเสร็จ (พ.ร.บ.ไซเบอร์ฯ มาตรา 54) และต่อหน่วยงานกำกับดูแล บันทึกเลขอ้างอิงการส่งไว้ที่นี่ [VERIFY กำหนดเวลาและรูปแบบการส่งฉบับปัจจุบัน]"),
 ],
 bp=[("Lead with business impact and decisions; put technical detail in appendices.", "เริ่มด้วยผลกระทบทางธุรกิจและเรื่องที่ต้องตัดสินใจ และใส่รายละเอียดทางเทคนิคในภาคผนวก"),
     ("Show the trend against the previous assessment.", "แสดงแนวโน้มเทียบกับการประเมินครั้งก่อน")],
 mistakes=[("Delivering a vulnerability scan report and calling it a risk assessment.", "ส่งรายงานผลการสแกนช่องโหว่แล้วเรียกว่าการประเมินความเสี่ยง")],
)

C["ID-STD-002"] = dict(
 purpose=("This standard sets the scope, frequency, and remediation timelines for vulnerability scanning and remediation (ID.RA-01, PR.PS-02).",
          "มาตรฐานนี้กำหนดขอบเขต ความถี่ และกรอบเวลาในการสแกนและแก้ไขช่องโหว่ (ID.RA-01, PR.PS-02)"),
 sections=[
  ("Scanning Requirements", "ข้อกำหนดการสแกน", "Define coverage and frequency.", "กำหนดขอบเขตและความถี่",
   {"t": ["ID", "Scope", "Frequency"], "r": [
     ["VS-01", "Internet-facing systems (external scan)", "Weekly and after changes"], ["VS-02", "Internal servers and network devices (authenticated scan)", "Monthly"],
     ["VS-03", "Endpoints (agent-based)", "Continuous"], ["VS-04", "Web applications (dynamic application security testing)", "Before release and quarterly"],
     ["VS-05", "Cloud configuration (automated configuration checks)", "Continuous"], ["VS-06", "OT and medical devices (passive or vendor-approved method)", "Quarterly"]], "w": [1.8, 9.7, 5.0]},
   {"t": ["รหัส", "ขอบเขต", "ความถี่"], "r": [
     ["VS-01", "ระบบที่เปิดสู่อินเทอร์เน็ต (สแกนจากภายนอก)", "ทุกสัปดาห์และหลังการเปลี่ยนแปลง"], ["VS-02", "เซิร์ฟเวอร์และอุปกรณ์เครือข่ายภายใน (สแกนแบบยืนยันตัวตน)", "ทุกเดือน"],
     ["VS-03", "อุปกรณ์ปลายทาง (ผ่าน Agent)", "ต่อเนื่อง"], ["VS-04", "เว็บแอปพลิเคชัน (การทดสอบความมั่นคงปลอดภัยแบบ Dynamic)", "ก่อนเปิดใช้งานและทุกไตรมาส"],
     ["VS-05", "การตั้งค่าคลาวด์ (ตรวจสอบสถานะการตั้งค่า)", "ต่อเนื่อง"], ["VS-06", "OT และอุปกรณ์การแพทย์ (วิธี Passive หรือวิธีที่ผู้ผลิตอนุมัติ)", "ทุกไตรมาส"]], "w": [1.8, 9.7, 5.0]}),
  ("Remediation Timelines", "กรอบเวลาการแก้ไข", "Set remediation SLAs by severity and exposure.", "กำหนดกรอบเวลาการแก้ไขตามความรุนแรงและการเปิดเผยต่อภายนอก",
   {"t": ["Severity (CVSS and context)", "Internet-facing", "Internal", "Known exploited (for example, CISA KEV listed)"], "r": [
     ["Critical (9.0 to 10.0)", "7 days", "15 days", "Internet-facing 48 hours; internal 7 days"], ["High (7.0 to 8.9)", "15 days", "30 days", "15 days"],
     ["Medium (4.0 to 6.9)", "30 days", "90 days", "30 days"], ["Low (below 4.0)", "Next maintenance cycle", "Next maintenance cycle", "Next maintenance cycle"]], "w": [4.5, 3.5, 3.5, 5.0]},
   {"t": ["ความรุนแรง (CVSS และบริบท)", "ระบบที่เปิดสู่อินเทอร์เน็ต", "ระบบภายใน", "ช่องโหว่ที่ถูกใช้โจมตีจริง (เช่น อยู่ในรายการ CISA KEV)"], "r": [
     ["วิกฤต (9.0 ถึง 10.0)", "7 วัน", "15 วัน", "ระบบที่เปิดสู่อินเทอร์เน็ต 48 ชั่วโมง ระบบภายใน 7 วัน"], ["สูง (7.0 ถึง 8.9)", "15 วัน", "30 วัน", "15 วัน"],
     ["ปานกลาง (4.0 ถึง 6.9)", "30 วัน", "90 วัน", "30 วัน"], ["ต่ำ (ต่ำกว่า 4.0)", "รอบบำรุงรักษาถัดไป", "รอบบำรุงรักษาถัดไป", "รอบบำรุงรักษาถัดไป"]], "w": [4.5, 3.5, 3.5, 5.0]}),
  ("Exceptions", "ข้อยกเว้น", "State how vulnerabilities that cannot be fixed within SLA are handled.", "ระบุวิธีจัดการช่องโหว่ที่แก้ไขไม่ได้ภายในกรอบเวลา",
   "Vulnerabilities that cannot be remediated within SLA require compensating controls (such as virtual patching, isolation, or disabling the service) and an approved exception (GV-PRC-003).",
   "ช่องโหว่ที่แก้ไขไม่ได้ภายในกรอบเวลาต้องมีมาตรการชดเชย (เช่น Virtual patching การแยกเครือข่าย หรือการปิดบริการ) และข้อยกเว้นที่ได้รับอนุมัติ (GV-PRC-003)"),
 ],
 bp=[("Prioritize by exploitability and asset criticality, not only CVSS score.", "จัดลำดับความสำคัญตามความเป็นไปได้ในการถูกโจมตีและความสำคัญของทรัพย์สิน ไม่ใช่เฉพาะคะแนน CVSS"),
     ("Use authenticated scans; unauthenticated scans miss most missing patches.", "ใช้การสแกนแบบยืนยันตัวตน เพราะการสแกนแบบไม่ยืนยันตัวตนตรวจไม่พบแพตช์ที่ขาดส่วนใหญ่"),
     ("Track mean time to remediate by severity as a KPI.", "ติดตามระยะเวลาเฉลี่ยในการแก้ไขตามระดับความรุนแรงเป็น KPI")],
 mistakes=[("Scanning without remediation tracking, producing reports that nobody acts on.", "สแกนโดยไม่ติดตามการแก้ไข ทำให้ได้รายงานที่ไม่มีใครดำเนินการ"),
           ("Active scanning of fragile medical or OT devices, causing outages.", "สแกนแบบ Active กับอุปกรณ์การแพทย์หรือ OT ที่เปราะบาง ทำให้ระบบหยุดทำงาน")],
)

C["ID-PRC-002"] = dict(
 purpose=("This procedure describes how vulnerabilities are identified, validated, prioritized, assigned, remediated, verified, and reported (ID.RA-01, ID.RA-08).",
          "ระเบียบปฏิบัตินี้อธิบายวิธีระบุ ยืนยัน จัดลำดับความสำคัญ มอบหมาย แก้ไข ตรวจสอบผล และรายงานช่องโหว่ (ID.RA-01, ID.RA-08)"),
 sections=[
  ("Process Steps", "ขั้นตอนการดำเนินงาน", "Describe the end-to-end process with roles and timing.", "อธิบายกระบวนการตั้งแต่ต้นจนจบพร้อมบทบาทและระยะเวลา",
   {"t": ["Step", "Activity", "Actor"], "r": [
     ["1", "Collect findings from scans, penetration tests, vendor advisories, threat intelligence, and external reports", "[CISO]"],
     ["2", "Validate and remove false positives; map to assets and owners", "Security engineer"],
     ["3", "Prioritize using ID-STD-002 timelines, exploitability, and asset criticality", "Security engineer"],
     ["4", "Assign tickets to system owners and record in ID-REG-006", "Security engineer"],
     ["5", "Remediate through patching (PR-PRC-007) or configuration change (PR-PRC-006)", "System owner, [ITM]"],
     ["6", "Rescan to verify closure", "Security engineer"],
     ["7", "Escalate overdue items; request exception where needed", "[CISO]"],
     ["8", "Report KPIs monthly", "[CISO]"]], "w": [1.2, 11.3, 4.0]},
   {"t": ["ขั้นตอน", "กิจกรรม", "ผู้ดำเนินการ"], "r": [
     ["1", "รวบรวมข้อตรวจพบจากการสแกน การทดสอบเจาะระบบ ประกาศของผู้ขาย ข้อมูลข่าวกรองภัยคุกคาม และรายงานจากภายนอก", "[CISO]"],
     ["2", "ยืนยันผลและคัดผลบวกลวงออก เชื่อมโยงกับทรัพย์สินและเจ้าของ", "วิศวกรความมั่นคงปลอดภัย"],
     ["3", "จัดลำดับความสำคัญตามกรอบเวลาใน ID-STD-002 ความเป็นไปได้ในการถูกโจมตี และความสำคัญของทรัพย์สิน", "วิศวกรความมั่นคงปลอดภัย"],
     ["4", "มอบหมายงานให้เจ้าของระบบและบันทึกใน ID-REG-006", "วิศวกรความมั่นคงปลอดภัย"],
     ["5", "แก้ไขโดยติดตั้งแพตช์ (PR-PRC-007) หรือเปลี่ยนการตั้งค่า (PR-PRC-006)", "เจ้าของระบบ [ITM]"],
     ["6", "สแกนซ้ำเพื่อยืนยันการปิด", "วิศวกรความมั่นคงปลอดภัย"],
     ["7", "ยกระดับรายการที่เลยกำหนด และขอยกเว้นเมื่อจำเป็น", "[CISO]"],
     ["8", "รายงาน KPI ทุกเดือน", "[CISO]"]], "w": [1.2, 11.3, 4.0]}),
 ],
 bp=[("Subscribe to ThaiCERT advisories and vendor security bulletins for all critical products.", "ติดตามประกาศของ ThaiCERT และประกาศด้านความมั่นคงปลอดภัยของผู้ขายสำหรับผลิตภัณฑ์สำคัญทุกรายการ"),
     ("Hold a monthly vulnerability review with infrastructure and application owners.", "จัดประชุมทบทวนช่องโหว่ทุกเดือนร่วมกับเจ้าของโครงสร้างพื้นฐานและแอปพลิเคชัน")],
 mistakes=[("Closing tickets without rescanning, so unfixed vulnerabilities are reported as closed.", "ปิดงานโดยไม่สแกนซ้ำ ทำให้ช่องโหว่ที่ยังไม่แก้ไขถูกรายงานว่าปิดแล้ว")],
)

C["ID-REG-006"] = dict(
 purpose=("This tracker records validated vulnerabilities, their severity, owner, due date, and remediation status, to show exposure and SLA compliance (ID.RA-01).",
          "ทะเบียนนี้บันทึกช่องโหว่ที่ยืนยันแล้ว ระดับความรุนแรง ผู้รับผิดชอบ กำหนดเสร็จ และสถานะการแก้ไข เพื่อแสดงความเสี่ยงและการปฏิบัติตามกรอบเวลา (ID.RA-01)"),
 fields=[
  ("Vuln ID", "รหัสช่องโหว่", "Unique reference.", "รหัสอ้างอิง", "V-2026-0001"),
  ("Source", "แหล่งที่มา", "Scan, pentest, advisory.", "การสแกน การทดสอบเจาะระบบ ประกาศ", ""),
  ("Asset", "ทรัพย์สิน", "Asset ID.", "รหัสทรัพย์สิน", ""),
  ("Vulnerability (CVE)", "ช่องโหว่ (CVE)", "Title and CVE.", "ชื่อและ CVE", ""),
  ("Severity and exposure", "ความรุนแรงและการเปิดเผย", "Per ID-STD-002.", "ตาม ID-STD-002", ""),
  ("Owner", "ผู้รับผิดชอบ", "System owner.", "เจ้าของระบบ", ""),
  ("Found and due date", "วันที่พบและกำหนดเสร็จ", "Dates.", "วันที่", ""),
  ("Status", "สถานะ", "Open, Fixed, Verified, Exception.", "เปิด แก้ไขแล้ว ยืนยันแล้ว ยกเว้น", ""),
 ],
 rows=[
  ["V-2026-0412", "External scan", "Patient portal reverse proxy", "Web server critical remote code execution (CVE reference)", "Critical, internet-facing, known exploited", "Application Manager", "02/09/2026, due 04/09/2026", "Verified 03/09/2026"],
  ["V-2026-0398", "Authenticated scan", "SRV-HIS-APP01", "Windows cumulative update missing", "High, internal", "IT Infrastructure Manager", "15/08/2026, due 14/09/2026", "Verified 10/09/2026"],
  ["V-2026-0377", "Penetration test 2026", "HIS web module", "Insecure direct object reference on report viewer", "High, internal", "HIS Vendor A via CIO", "01/08/2026, due 31/08/2026", "Open (vendor fix scheduled 10/2026, overdue)"],
  ["V-2026-0350", "Vendor advisory", "MED-IMG-002", "Embedded OS vulnerability", "High, isolated VLAN", "Director of Radiology", "20/07/2026, due 19/08/2026", "Exception EXC-2026-007"],
 ],
 bp=[("Generate the tracker from the scanning tool and ticketing system rather than by hand.", "สร้างทะเบียนจากเครื่องมือสแกนและระบบจัดการงาน แทนการบันทึกด้วยมือ")],
 mistakes=[("Tracking thousands of low findings and losing sight of critical ones.", "ติดตามข้อตรวจพบระดับต่ำหลายพันรายการจนมองไม่เห็นรายการระดับวิกฤต")],
)

C["ID-PRC-003"] = dict(
 purpose=("This procedure governs how penetration tests are planned, authorized, performed, reported, and followed up, so that testing is safe, legal, and effective (ID.RA-01, ID.IM-02).",
          "ระเบียบปฏิบัตินี้กำกับการวางแผน การอนุมัติ การดำเนินการ การรายงาน และการติดตามผลการทดสอบเจาะระบบ เพื่อให้การทดสอบปลอดภัย ถูกกฎหมาย และมีประสิทธิผล (ID.RA-01, ID.IM-02)"),
 sections=[
  ("Testing Requirements", "ข้อกำหนดการทดสอบ", "Set frequency, scope, and tester requirements.", "กำหนดความถี่ ขอบเขต และข้อกำหนดของผู้ทดสอบ",
   ["Test internet-facing systems and critical internal systems at least once a year and after major changes.", "Use qualified testers (for example, OSCP, GPEN, CREST) independent of the team that built the system.",
    "Use a recognized methodology such as OWASP Web Security Testing Guide, PTES, or NIST SP 800-115.", "Sign the authorization and rules of engagement (ID-FRM-002) before testing."],
   ["ทดสอบระบบที่เปิดสู่อินเทอร์เน็ตและระบบภายในที่สำคัญอย่างน้อยปีละครั้ง และหลังการเปลี่ยนแปลงสำคัญ", "ใช้ผู้ทดสอบที่มีคุณสมบัติ (เช่น OSCP GPEN CREST) และเป็นอิสระจากทีมที่พัฒนาระบบ",
    "ใช้ระเบียบวิธีที่เป็นที่ยอมรับ เช่น OWASP Web Security Testing Guide, PTES หรือ NIST SP 800-115", "ลงนามแบบอนุมัติและกติกาการทดสอบ (ID-FRM-002) ก่อนเริ่มทดสอบ"]),
  ("Process Steps", "ขั้นตอนการดำเนินงาน", "Describe steps from scoping to retest.", "อธิบายขั้นตอนตั้งแต่การกำหนดขอบเขตจนถึงการทดสอบซ้ำ",
   {"n": ["Define scope, objectives, and test type (black, grey, or white box).", "Sign authorization and rules of engagement; notify the SOC and system owners.", "Perform testing within the agreed window; stop and escalate if a critical issue or service impact occurs.",
          "Receive the report with findings, evidence, risk ratings, and recommendations.", "Record findings in ID-REG-006 and remediate per ID-STD-002.", "Retest to confirm closure."]},
   {"n": ["กำหนดขอบเขต วัตถุประสงค์ และประเภทการทดสอบ (Black box, Grey box หรือ White box)", "ลงนามแบบอนุมัติและกติกาการทดสอบ และแจ้ง SOC และเจ้าของระบบ", "ทดสอบภายในช่วงเวลาที่ตกลง และหยุดพร้อมยกระดับทันทีหากพบประเด็นวิกฤตหรือกระทบการให้บริการ",
          "รับรายงานที่มีข้อตรวจพบ หลักฐาน ระดับความเสี่ยง และข้อเสนอแนะ", "บันทึกข้อตรวจพบใน ID-REG-006 และแก้ไขตาม ID-STD-002", "ทดสอบซ้ำเพื่อยืนยันการปิด"]}),
 ],
 bp=[("Rotate testing providers every two to three years for a fresh view.", "หมุนเวียนผู้ให้บริการทดสอบทุก 2 ถึง 3 ปี เพื่อให้ได้มุมมองใหม่"),
     ("Include an assumed-breach internal test, not only external tests, to measure ransomware resilience.", "รวมการทดสอบภายในแบบสมมติว่าถูกเจาะระบบแล้ว ไม่ใช่เฉพาะการทดสอบจากภายนอก เพื่อวัดความทนทานต่อแรนซัมแวร์")],
 mistakes=[("Testing production clinical systems during peak hours without a stop procedure.", "ทดสอบระบบคลินิกที่ใช้งานจริงในช่วงเวลาเร่งด่วนโดยไม่มีขั้นตอนการหยุดทดสอบ")],
)

C["ID-FRM-002"] = dict(
 purpose=("This form authorizes a penetration test in writing and defines the rules of engagement, protecting the organization and testers and separating authorized testing from offenses under the Computer Crime Act B.E. 2550.",
          "แบบฟอร์มนี้ใช้อนุมัติการทดสอบเจาะระบบเป็นลายลักษณ์อักษรและกำหนดกติกาการทดสอบ เพื่อคุ้มครององค์กรและผู้ทดสอบ และแยกการทดสอบที่ได้รับอนุญาตออกจากความผิดตาม พ.ร.บ.ว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. 2550"),
 fields=[
  ("Test name and reference", "ชื่อและเลขอ้างอิงการทดสอบ", "Engagement reference.", "เลขอ้างอิงงาน", "PT-2026-01"),
  ("Testing organization and testers", "ผู้ให้บริการและผู้ทดสอบ", "Company, named testers, source IP addresses.", "บริษัท รายชื่อผู้ทดสอบ และ IP ต้นทาง", ""),
  ("In-scope targets", "เป้าหมายในขอบเขต", "Systems, URLs, IP ranges.", "ระบบ URL ช่วง IP", ""),
  ("Out-of-scope targets", "เป้าหมายนอกขอบเขต", "Systems that must not be tested.", "ระบบที่ห้ามทดสอบ", ""),
  ("Test window", "ช่วงเวลาทดสอบ", "Dates and hours.", "วันและเวลา", ""),
  ("Permitted and prohibited techniques", "เทคนิคที่อนุญาตและที่ห้าม", "For example, no denial of service, no social engineering unless approved.", "เช่น ห้ามโจมตีให้ระบบหยุดให้บริการ ห้ามใช้วิศวกรรมสังคมหากไม่ได้รับอนุมัติ", ""),
  ("Data handling", "การจัดการข้อมูล", "How test data and findings are protected and destroyed.", "วิธีปกป้องและทำลายข้อมูลการทดสอบและข้อตรวจพบ", ""),
  ("Emergency contacts and stop procedure", "ผู้ติดต่อฉุกเฉินและขั้นตอนหยุดทดสอบ", "Who to call and when to stop.", "ผู้ที่ต้องติดต่อและเมื่อใดต้องหยุด", ""),
 ],
 cmc_vals=["PT-2026-01 Annual external and internal test", "Contracted testing firm; three named testers; source IPs listed in annex", "Patient portal, external IP range, HIS web modules (test environment and read-only production)",
           "Medical devices, PACS modalities, life-support systems, production databases", "4 to 15 August 2026, 20:00 to 06:00 for production targets",
           "No denial of service; no data modification in production; phishing excluded", "Findings encrypted; test data deleted within 30 days of final report; certificate of deletion provided",
           "Security Manager (24x7 phone) and MSSP SOC; testers stop immediately on any clinical system slowdown"],
 approvals=["CISO", "SYSOWN", "CIO"],
 bp=[("Get written approval from the system owner and, for hosted systems, from the hosting provider.", "ขออนุมัติเป็นลายลักษณ์อักษรจากเจ้าของระบบ และจากผู้ให้บริการโฮสต์กรณีระบบอยู่ภายนอก")],
 mistakes=[("Starting tests on verbal approval, exposing testers to legal risk.", "เริ่มทดสอบโดยได้รับอนุมัติด้วยวาจา ทำให้ผู้ทดสอบมีความเสี่ยงทางกฎหมาย")],
)

C["ID-PRC-004"] = dict(
 purpose=("This procedure defines how cyber threat intelligence is collected, assessed, shared, and used to inform risk assessment, detection, and vulnerability prioritization (ID.RA-02, ID.RA-03).",
          "ระเบียบปฏิบัตินี้กำหนดวิธีรวบรวม ประเมิน แบ่งปัน และใช้ข้อมูลข่าวกรองภัยคุกคามไซเบอร์ในการประเมินความเสี่ยง การตรวจจับ และการจัดลำดับความสำคัญของช่องโหว่ (ID.RA-02, ID.RA-03)"),
 sections=[
  ("Sources", "แหล่งข้อมูล", "List intelligence sources by type.", "ระบุแหล่งข้อมูลข่าวกรองตามประเภท",
   ["Government and sector: ThaiCERT and NCSA advisories, sector information-sharing groups.", "Vendor: security bulletins for critical products.", "Commercial or managed: MSSP threat intelligence feeds.", "Open source: CISA Known Exploited Vulnerabilities catalog, MITRE ATT&CK updates."],
   ["ภาครัฐและภาคส่วน: ประกาศของ ThaiCERT และ สกมช. และกลุ่มแบ่งปันข้อมูลของภาคส่วน", "ผู้ขาย: ประกาศด้านความมั่นคงปลอดภัยของผลิตภัณฑ์สำคัญ", "เชิงพาณิชย์หรือผู้ให้บริการ: ข้อมูลข่าวกรองจาก MSSP", "แหล่งเปิด: รายการ CISA Known Exploited Vulnerabilities และการปรับปรุง MITRE ATT&CK"],
   ["ThaiCERT and NCSA advisories; the hospital CII information-sharing group.", "Vendor bulletins for HIS, PACS, LIS, Microsoft, and network equipment.", "MSSP threat intelligence included in the monitoring service.", "CISA KEV catalog checked weekly by the security engineer."]),
  ("Process", "กระบวนการ", "Describe how intelligence is triaged and turned into action.", "อธิบายวิธีคัดกรองข้อมูลข่าวกรองและแปลงเป็นการดำเนินการ",
   {"t": ["Step", "Activity", "Output"], "r": [["1", "Review new intelligence daily for relevance to our assets and sector", "Relevant items"], ["2", "Assess urgency: active exploitation, exposure, critical assets", "Priority"], ["3", "Act: patch, block indicators, add detections, or update risk", "Ticket or rule"], ["4", "Share relevant indicators with sector peers as permitted", "Shared report"], ["5", "Summarize monthly threat trends for management", "Threat summary"]], "w": [1.2, 10.0, 5.3]},
   {"t": ["ขั้นตอน", "กิจกรรม", "ผลลัพธ์"], "r": [["1", "ทบทวนข้อมูลข่าวกรองใหม่ทุกวันว่าเกี่ยวข้องกับทรัพย์สินและภาคส่วนหรือไม่", "รายการที่เกี่ยวข้อง"], ["2", "ประเมินความเร่งด่วน: มีการโจมตีจริง การเปิดเผยต่อภายนอก ทรัพย์สินสำคัญ", "ลำดับความสำคัญ"], ["3", "ดำเนินการ: ติดตั้งแพตช์ บล็อกตัวบ่งชี้ เพิ่มกฎการตรวจจับ หรือปรับปรุงความเสี่ยง", "งานหรือกฎ"], ["4", "แบ่งปันตัวบ่งชี้ที่เกี่ยวข้องกับองค์กรในภาคส่วนเดียวกันตามที่อนุญาต", "รายงานที่แบ่งปัน"], ["5", "สรุปแนวโน้มภัยคุกคามรายเดือนให้ผู้บริหาร", "สรุปภัยคุกคาม"]], "w": [1.2, 10.0, 5.3]}),
 ],
 bp=[("Focus on intelligence you can act on; a feed you never use is cost without value.", "มุ่งเน้นข้อมูลข่าวกรองที่นำไปดำเนินการได้ ข้อมูลที่ไม่เคยใช้เป็นต้นทุนที่ไม่มีคุณค่า"),
     ("Join a sector information-sharing group; peers often see the same campaigns first.", "เข้าร่วมกลุ่มแบ่งปันข้อมูลของภาคส่วน เพราะองค์กรในภาคส่วนเดียวกันมักเห็นแคมเปญโจมตีเดียวกันก่อน")],
 mistakes=[("Buying expensive threat feeds without a process to use them.", "ซื้อข้อมูลข่าวกรองราคาแพงโดยไม่มีกระบวนการนำไปใช้")],
)

C["ID-PRC-005"] = dict(
 purpose=("This procedure defines how the organization receives, validates, fixes, and responds to vulnerability reports from external researchers, customers, and suppliers (ID.RA-08).",
          "ระเบียบปฏิบัตินี้กำหนดวิธีรับ ตรวจสอบ แก้ไข และตอบกลับรายงานช่องโหว่จากนักวิจัยภายนอก ลูกค้า และผู้ให้บริการ (ID.RA-08)"),
 sections=[
  ("Disclosure Channel and Policy", "ช่องทางและนโยบายการรับแจ้ง", "Publish a channel and state what reporters can expect.", "เผยแพร่ช่องทางและระบุสิ่งที่ผู้แจ้งจะได้รับ",
   ["Publish a dedicated security contact email address and a security.txt file on the website.", "Acknowledge reports within 3 working days and give status updates every 14 days.",
    "Do not take legal action against good-faith researchers who follow the policy.", "Coordinate public disclosure after a fix is available."],
   ["เผยแพร่อีเมลติดต่อด้านความมั่นคงปลอดภัยโดยเฉพาะ และไฟล์ security.txt บนเว็บไซต์", "ตอบรับรายงานภายใน 3 วันทำการ และแจ้งสถานะทุก 14 วัน",
    "ไม่ดำเนินคดีกับนักวิจัยที่สุจริตและปฏิบัติตามนโยบาย", "ประสานการเปิดเผยต่อสาธารณะหลังมีการแก้ไขแล้ว"]),
  ("Handling Steps", "ขั้นตอนการจัดการ", "Describe internal handling steps.", "อธิบายขั้นตอนการจัดการภายใน",
   {"n": ["Log the report and acknowledge receipt.", "Validate and rate severity; involve the vendor if the issue is in a supplied product.", "Remediate through the vulnerability management procedure (ID-PRC-002).", "Inform the reporter and agree disclosure timing.", "Treat any evidence of exploitation as a security incident (RS-PRC-001)."]},
   {"n": ["บันทึกรายงานและตอบรับ", "ตรวจสอบและประเมินความรุนแรง และประสานผู้ขายหากเป็นปัญหาในผลิตภัณฑ์ที่จัดหามา", "แก้ไขตามระเบียบปฏิบัติการบริหารจัดการช่องโหว่ (ID-PRC-002)", "แจ้งผู้รายงานและตกลงช่วงเวลาการเปิดเผย", "หากพบหลักฐานการถูกโจมตี ให้จัดการเป็นเหตุการณ์ความมั่นคงปลอดภัย (RS-PRC-001)"]}),
 ],
 bp=[("Follow ISO/IEC 29147 for disclosure and ISO/IEC 30111 for internal handling.", "ใช้ ISO/IEC 29147 สำหรับการเปิดเผยช่องโหว่ และ ISO/IEC 30111 สำหรับการจัดการภายใน")],
 mistakes=[("Researchers cannot find a contact, so they disclose publicly.", "นักวิจัยหาช่องทางติดต่อไม่ได้ จึงเปิดเผยต่อสาธารณะ")],
)

C["ID-PRC-006"] = dict(
 purpose=("This procedure defines how nonconformities and improvement opportunities from audits, tests, exercises, incidents, and operations are recorded, analyzed for root cause, corrected, and verified (ID.IM-01 to ID.IM-04; ISO/IEC 27001:2022 Clause 10).",
          "ระเบียบปฏิบัตินี้กำหนดวิธีบันทึก วิเคราะห์สาเหตุที่แท้จริง แก้ไข และยืนยันผลของข้อบกพร่องและโอกาสในการปรับปรุงจากการตรวจสอบ การทดสอบ การฝึกซ้อม เหตุการณ์ และการปฏิบัติงาน (ID.IM-01 ถึง ID.IM-04; ISO/IEC 27001:2022 ข้อ 10)"),
 sections=[
  ("Improvement Sources", "แหล่งที่มาของการปรับปรุง", "List inputs that generate improvement actions.", "ระบุข้อมูลนำเข้าที่ทำให้เกิดการปรับปรุง",
   {"t": ["Source", "CSF subcategory"], "r": [["Audits, assessments, management review", "ID.IM-01"], ["Penetration tests, exercises, DR tests", "ID.IM-02"], ["Incidents, near misses, operational metrics", "ID.IM-03"], ["Lessons learned that change response and recovery plans", "ID.IM-04"]], "w": [11.0, 5.5]},
   {"t": ["แหล่งที่มา", "CSF Subcategory"], "r": [["การตรวจสอบ การประเมิน การทบทวนโดยฝ่ายบริหาร", "ID.IM-01"], ["การทดสอบเจาะระบบ การฝึกซ้อม การทดสอบ DR", "ID.IM-02"], ["เหตุการณ์ เหตุการณ์เกือบเกิด ตัวชี้วัดการปฏิบัติงาน", "ID.IM-03"], ["บทเรียนที่ทำให้แผนรับมือและแผนกู้คืนเปลี่ยนแปลง", "ID.IM-04"]], "w": [11.0, 5.5]}),
  ("Process Steps", "ขั้นตอนการดำเนินงาน", "Describe steps from recording to verification (Clause 10.2).", "อธิบายขั้นตอนตั้งแต่การบันทึกจนถึงการยืนยันผล (ข้อ 10.2)",
   {"n": ["Record the nonconformity or opportunity in ID-REG-007.", "Take immediate correction where needed to control the effect.", "Analyze root cause (for example, five whys) and check whether similar issues exist elsewhere.",
          "Agree corrective action, owner, and due date.", "Implement and update affected documents and plans.", "Verify effectiveness after implementation and close the record."]},
   {"n": ["บันทึกข้อบกพร่องหรือโอกาสในการปรับปรุงใน ID-REG-007", "ดำเนินการแก้ไขเฉพาะหน้าเมื่อจำเป็นเพื่อควบคุมผลกระทบ", "วิเคราะห์สาเหตุที่แท้จริง (เช่น ใช้วิธี Five whys) และตรวจสอบว่ามีปัญหาลักษณะเดียวกันที่อื่นหรือไม่",
          "ตกลงการแก้ไข ผู้รับผิดชอบ และกำหนดเสร็จ", "ดำเนินการและปรับปรุงเอกสารและแผนที่ได้รับผลกระทบ", "ยืนยันประสิทธิผลหลังดำเนินการ และปิดรายการ"]}),
 ],
 bp=[("Separate correction (fix the instance) from corrective action (remove the cause).", "แยกการแก้ไขเฉพาะหน้า (แก้ไขกรณีที่พบ) ออกจากการแก้ไขที่ต้นเหตุ (ขจัดสาเหตุ)"),
     ("Check effectiveness weeks after closure, for example by resampling.", "ตรวจสอบประสิทธิผลหลังปิดรายการหลายสัปดาห์ เช่น การสุ่มตัวอย่างซ้ำ")],
 mistakes=[("Closing findings when a document is written rather than when practice changes.", "ปิดข้อตรวจพบเมื่อเขียนเอกสารเสร็จ แทนที่จะปิดเมื่อการปฏิบัติงานเปลี่ยนแปลงจริง")],
)

C["ID-REG-007"] = dict(
 purpose=("This register records nonconformities, audit findings, and improvement actions with root cause, owner, due date, and verification, as evidence required by ISO/IEC 27001:2022 Clause 10.2.",
          "ทะเบียนนี้บันทึกข้อบกพร่อง ข้อตรวจพบจากการตรวจสอบ และการปรับปรุง พร้อมสาเหตุที่แท้จริง ผู้รับผิดชอบ กำหนดเสร็จ และการยืนยันผล เป็นหลักฐานที่ ISO/IEC 27001:2022 ข้อ 10.2 กำหนด"),
 fields=[
  ("Item ID", "รหัสรายการ", "Unique reference.", "รหัสอ้างอิง", "CAR-2026-001"),
  ("Source", "แหล่งที่มา", "Audit, test, exercise, incident, review.", "การตรวจสอบ การทดสอบ การฝึกซ้อม เหตุการณ์ การทบทวน", ""),
  ("Description", "รายละเอียด", "Nonconformity or opportunity.", "ข้อบกพร่องหรือโอกาสในการปรับปรุง", ""),
  ("Root cause", "สาเหตุที่แท้จริง", "Result of analysis.", "ผลการวิเคราะห์", ""),
  ("Corrective action", "การแก้ไขที่ต้นเหตุ", "Action agreed.", "การดำเนินการที่ตกลง", ""),
  ("Owner and due date", "ผู้รับผิดชอบและกำหนดเสร็จ", "Role and date.", "บทบาทและวันที่", ""),
  ("Status", "สถานะ", "Open, Implemented, Verified effective, Closed.", "เปิด ดำเนินการแล้ว ยืนยันประสิทธิผลแล้ว ปิด", ""),
  ("Verification evidence", "หลักฐานการยืนยันผล", "How effectiveness was confirmed.", "วิธียืนยันประสิทธิผล", ""),
 ],
 rows=[
  ["CAR-2025-021", "IA-2025-04-02", "38 HIS accounts of former staff remained active", "No automated leaver trigger from HR to HIS", "Automate HR-to-HIS deprovisioning; monthly reconciliation", "CIO, 30/04/2026", "Verified effective", "06/2026 sample: 0 of 1,402 accounts belonged to leavers"],
  ["CAR-2025-022", "IA-2025-04-05", "No HIS restore test in 12 months", "Restore testing not scheduled or owned", "Monthly restore tests with record PR-REC-003", "IT Infrastructure Manager, 28/02/2026", "Closed", "Seven consecutive successful monthly tests"],
  ["CAR-2026-004", "EX-2026-01 tabletop", "Clinical downtime forms not available on two wards", "Downtime kits not included in ward checklists", "Add downtime kits to ward monthly checklist", "Director of Nursing, 31/05/2026", "Verified effective", "Spot check of 10 wards in July 2026"],
  ["CAR-2026-011", "INC-2026-014", "BEC attempt reached finance staff; payment verification relied on email", "No out-of-band verification rule for bank detail changes", "Call-back verification for any vendor bank change", "CFO, 31/07/2026", "Implemented", "Effectiveness check scheduled 10/2026"],
 ],
 bp=[("Use one register for all sources so management sees all improvement work together.", "ใช้ทะเบียนเดียวสำหรับทุกแหล่งที่มา เพื่อให้ผู้บริหารเห็นงานปรับปรุงทั้งหมดร่วมกัน")],
 mistakes=[("Records with no root cause, so the same finding repeats next year.", "รายการที่ไม่มีการวิเคราะห์สาเหตุที่แท้จริง ทำให้ข้อตรวจพบเดิมเกิดซ้ำในปีถัดไป")],
)

C["ID-PLN-002"] = dict(
 purpose=("This program plans the annual set of cybersecurity tests and exercises (tabletop, technical, recovery) that validate plans and identify improvements (ID.IM-02, ID.IM-04).",
          "แผนนี้กำหนดชุดการทดสอบและการฝึกซ้อมด้านความมั่นคงปลอดภัยไซเบอร์ประจำปี (การฝึกซ้อมแบบ Tabletop การทดสอบทางเทคนิค และการทดสอบการกู้คืน) เพื่อยืนยันความใช้ได้ของแผนและระบุสิ่งที่ต้องปรับปรุง (ID.IM-02, ID.IM-04)"),
 sections=[
  ("Annual Exercise Calendar", "ปฏิทินการฝึกซ้อมประจำปี", "List each exercise with type, scenario, participants, and timing.", "ระบุการฝึกซ้อมแต่ละครั้งพร้อมประเภท สถานการณ์ ผู้เข้าร่วม และช่วงเวลา",
   {"t": ["Exercise", "Type", "Scenario", "Participants", "Quarter"], "r": [
     ["Executive tabletop", "Discussion", "Ransomware with data extortion", "[ISSC], [COMMS], [LEGAL]", "Q1"], ["Technical response drill", "Functional", "Compromised privileged account", "IT, [SOC]", "Q2"],
     ["DR test", "Full or partial failover", "Loss of primary data center", "IT, system owners", "Q2"], ["Phishing simulation", "Technical", "Credential harvesting", "All staff", "Quarterly"],
     ["National readiness test (if CII)", "As defined by NCSA", "As defined by NCSA", "As required", "As scheduled"]], "w": [3.5, 3.0, 4.0, 3.5, 2.5]},
   {"t": ["การฝึกซ้อม", "ประเภท", "สถานการณ์", "ผู้เข้าร่วม", "ไตรมาส"], "r": [
     ["Tabletop ระดับผู้บริหาร", "การอภิปราย", "แรนซัมแวร์พร้อมการขู่เปิดเผยข้อมูล", "[ISSC] [COMMS] [LEGAL]", "Q1"], ["การซ้อมรับมือทางเทคนิค", "เชิงปฏิบัติ", "บัญชีสิทธิ์ระดับสูงถูกยึด", "IT [SOC]", "Q2"],
     ["การทดสอบ DR", "สลับระบบทั้งหมดหรือบางส่วน", "ศูนย์ข้อมูลหลักใช้งานไม่ได้", "IT เจ้าของระบบ", "Q2"], ["การทดสอบฟิชชิ่งจำลอง", "ทางเทคนิค", "การหลอกขโมยรหัสผ่าน", "บุคลากรทุกคน", "ทุกไตรมาส"],
     ["การทดสอบความพร้อมระดับประเทศ (กรณี CII)", "ตามที่ สกมช. กำหนด", "ตามที่ สกมช. กำหนด", "ตามที่กำหนด", "ตามกำหนดการ"]], "w": [3.5, 3.0, 4.0, 3.5, 2.5]},
   {"t": ["Exercise", "Type", "Scenario", "Participants", "Date"], "r": [
     ["EX-2026-01 Executive tabletop", "Discussion", "Ransomware encrypts HIS during night shift", "ISSC, Corporate Communications, Legal, ward heads", "February 2026 (done)"],
     ["EX-2026-02 Technical drill", "Functional", "Compromised domain administrator", "IT, MSSP", "May 2026 (done)"],
     ["DR-2026-01 DR test", "Partial failover", "HIS and PACS fail over to Nonthaburi DR site", "IT, HIS Vendor A, Vendor B", "May 2026 (done)"],
     ["Phishing simulations", "Technical", "Credential harvesting and invoice fraud", "All staff", "Quarterly"],
     ["NCSA national cyber exercise", "As defined by NCSA", "Sector scenario", "Security Manager, CIO", "September 2026 (done)"]], "w": [3.5, 3.0, 4.0, 3.5, 2.5]}),
 ],
 bp=[("Increase exercise realism each year: start with discussion, move to functional and full-scale tests.", "เพิ่มความสมจริงของการฝึกซ้อมทุกปี โดยเริ่มจากการอภิปราย แล้วจึงขยับไปสู่การทดสอบเชิงปฏิบัติและเต็มรูปแบบ"),
     ("Include key suppliers and clinical or business leaders, not only IT.", "ให้ผู้ให้บริการหลักและผู้นำด้านคลินิกหรือธุรกิจเข้าร่วม ไม่ใช่เฉพาะฝ่าย IT"),
     ("Record lessons learned (ID-TPL-001) and track actions in ID-REG-007.", "บันทึกบทเรียนที่ได้รับ (ID-TPL-001) และติดตามการดำเนินการใน ID-REG-007")],
 mistakes=[("Running the same scripted scenario every year, so the exercise tests memory, not capability.", "ใช้สถานการณ์เดิมทุกปี ทำให้การฝึกซ้อมทดสอบความจำ ไม่ใช่ความสามารถ")],
)

C["ID-TPL-001"] = dict(
 purpose=("This template records lessons learned after an incident, exercise, or test, and turns them into tracked improvements to plans and controls (ID.IM-03, ID.IM-04).",
          "แม่แบบนี้ใช้บันทึกบทเรียนที่ได้รับหลังเหตุการณ์ การฝึกซ้อม หรือการทดสอบ และแปลงเป็นการปรับปรุงแผนและมาตรการควบคุมที่มีการติดตาม (ID.IM-03, ID.IM-04)"),
 sections=[
  ("Summary", "สรุป", "Describe the event, timeline, and impact briefly.", "อธิบายเหตุการณ์ ลำดับเวลา และผลกระทบโดยย่อ",
   {"t": ["Item", "Response"], "r": [["Event or exercise reference", ""], ["Date and duration", ""], ["Summary of what happened", ""], ["Impact", ""]], "w": [5.5, 11.0]},
   {"t": ["หัวข้อ", "คำตอบ"], "r": [["เลขอ้างอิงเหตุการณ์หรือการฝึกซ้อม", ""], ["วันที่และระยะเวลา", ""], ["สรุปสิ่งที่เกิดขึ้น", ""], ["ผลกระทบ", ""]], "w": [5.5, 11.0]},
   {"t": ["Item", "Response"], "r": [["Reference", "EX-2026-01 Executive ransomware tabletop"], ["Date and duration", "18 February 2026, 3 hours"], ["Summary", "Scenario: HIS encrypted at 02:00; MSSP alert; downtime procedures activated; decision on NCSA and PDPC notification; media inquiry at 09:00."], ["Impact (simulated)", "HIS down 18 hours; two wards lacked downtime forms; notification decision took 5 hours to reach."]], "w": [5.5, 11.0]}),
  ("What Went Well, What to Improve", "สิ่งที่ทำได้ดีและสิ่งที่ต้องปรับปรุง", "Record strengths, gaps, and root causes.", "บันทึกจุดแข็ง ช่องว่าง และสาเหตุที่แท้จริง",
   {"t": ["Observation", "Type (strength or gap)", "Root cause", "Action and owner"], "r": [["", "", "", ""]]},
   {"t": ["ข้อสังเกต", "ประเภท (จุดแข็ง หรือ ช่องว่าง)", "สาเหตุที่แท้จริง", "การดำเนินการและผู้รับผิดชอบ"], "r": [["", "", "", ""]]},
   {"t": ["Observation", "Type", "Root cause", "Action and owner"], "r": [
     ["Escalation from MSSP to on-call reached Security Manager in 12 minutes", "Strength", "Tested call tree", "Keep; retest quarterly"],
     ["Downtime forms missing on two wards", "Gap", "Not in ward checklists", "CAR-2026-004, Director of Nursing"],
     ["Unclear who decides on PDPC and NCSA notification at night", "Gap", "Decision authority not in IR plan", "Update RS-PLN-001 and RS-PRC-003, Security Manager"],
     ["Communications holding statement drafted quickly", "Strength", "Template RC-TPL-001 available", "Keep"]]}),
 ],
 bp=[("Hold the review within two weeks while memory is fresh, and keep it blameless.", "จัดการทบทวนภายใน 2 สัปดาห์ขณะที่ยังจำได้ชัดเจน และไม่มุ่งหาผู้กระทำผิด"),
     ("Update the affected plans and record the update in their revision history.", "ปรับปรุงแผนที่ได้รับผลกระทบ และบันทึกการปรับปรุงในประวัติการแก้ไขของแผนนั้น")],
 mistakes=[("Lessons are written but never assigned or tracked.", "เขียนบทเรียนไว้แต่ไม่มีการมอบหมายหรือติดตาม")],
)
