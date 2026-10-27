# -*- coding: utf-8 -*-
# GV.SC Cybersecurity Supply Chain Risk Management
C = {}

C["GV-POL-006"] = dict(
 purpose=("This policy sets how [Organization Name] manages cybersecurity risk from suppliers, service providers, and technology products across their life cycle (GV.SC-01).",
          "นโยบายนี้กำหนดวิธีที่ [ชื่อองค์กร] บริหารความเสี่ยงด้านไซเบอร์จากผู้จำหน่าย ผู้ให้บริการ และผลิตภัณฑ์เทคโนโลยีตลอดวงจรชีวิต (GV.SC-01)"),
 sections=[
  ("Policy Statements", "ข้อความนโยบาย", "State the mandatory principles of the supply chain risk program (GV.SC-01 to GV.SC-03).", "ระบุหลักการที่บังคับของแผนงานบริหารความเสี่ยงห่วงโซ่อุปทาน (GV.SC-01 ถึง GV.SC-03)",
   ["All suppliers that access, process, host, or support [Organization Name] information or systems are risk-tiered before contract and reviewed at a frequency based on tier.",
    "Security requirements are included in contracts in proportion to supplier tier (GV-STD-002).",
    "Supplier risks are recorded in the risk register and reported with other enterprise risks.",
    "Suppliers are included in incident response, business continuity, and exercises where they support critical services (GV.SC-08).",
    "Access and data are removed when the relationship ends (GV.SC-10)."],
   ["ผู้ให้บริการทุกรายที่เข้าถึง ประมวลผล จัดเก็บ หรือสนับสนุนข้อมูลหรือระบบของ [ชื่อองค์กร] ต้องได้รับการจัดระดับความเสี่ยงก่อนทำสัญญา และทบทวนตามความถี่ที่กำหนดตามระดับ",
    "ระบุข้อกำหนดด้านความมั่นคงปลอดภัยในสัญญาให้เหมาะสมกับระดับของผู้ให้บริการ (GV-STD-002)",
    "บันทึกความเสี่ยงจากผู้ให้บริการในทะเบียนความเสี่ยงและรายงานร่วมกับความเสี่ยงองค์กรอื่น",
    "ให้ผู้ให้บริการที่สนับสนุนบริการสำคัญเข้าร่วมในการรับมือเหตุการณ์ ความต่อเนื่องทางธุรกิจ และการฝึกซ้อม (GV.SC-08)",
    "ถอนสิทธิ์การเข้าถึงและข้อมูลเมื่อสิ้นสุดความสัมพันธ์ (GV.SC-10)"]),
  ("Roles", "บทบาท", "Define roles of procurement, business owners, security, legal, and suppliers (GV.SC-02).", "กำหนดบทบาทของฝ่ายจัดซื้อ เจ้าของธุรกิจ หน่วยงานความมั่นคงปลอดภัย ฝ่ายกฎหมาย และผู้ให้บริการ (GV.SC-02)",
   {"t": ["Role", "Responsibility"], "r": [["Business owner", "Owns the supplier relationship and its risk"], ["[PROC]", "Runs sourcing, keeps the supplier register, ensures assessment before contract"], ["[CISO]", "Sets requirements, assesses security risk, monitors high-tier suppliers"], ["[LEGAL]", "Includes security and data protection clauses"], ["[DPO]", "Reviews processing of personal data and DPAs"], ["Supplier", "Meets contract requirements and reports incidents"]], "w": [4.0, 12.5]},
   {"t": ["บทบาท", "ความรับผิดชอบ"], "r": [["เจ้าของธุรกิจ", "เป็นเจ้าของความสัมพันธ์และความเสี่ยงของผู้ให้บริการ"], ["[PROC]", "ดำเนินการจัดหา ดูแลทะเบียนผู้ให้บริการ และควบคุมให้มีการประเมินก่อนทำสัญญา"], ["[CISO]", "กำหนดข้อกำหนด ประเมินความเสี่ยงด้านความมั่นคงปลอดภัย และติดตามผู้ให้บริการระดับสูง"], ["[LEGAL]", "ระบุข้อสัญญาด้านความมั่นคงปลอดภัยและการคุ้มครองข้อมูล"], ["[DPO]", "ทบทวนการประมวลผลข้อมูลส่วนบุคคลและข้อตกลง DPA"], ["ผู้ให้บริการ", "ปฏิบัติตามข้อกำหนดในสัญญาและรายงานเหตุการณ์"]], "w": [4.0, 12.5]}),
 ],
 bp=[("Start with the 10 to 20 suppliers that matter most rather than assessing every vendor equally.", "เริ่มจากผู้ให้บริการ 10 ถึง 20 รายที่สำคัญที่สุด แทนการประเมินทุกรายเท่ากัน"),
     ("Embed the security step in the procurement workflow so it cannot be skipped.", "ฝังขั้นตอนด้านความมั่นคงปลอดภัยไว้ในกระบวนการจัดซื้อจัดจ้าง เพื่อไม่ให้ข้ามได้"),
     ("Use NIST SP 800-161 Rev. 1 for product and software supply chain practices.", "ใช้ NIST SP 800-161 Rev. 1 สำหรับแนวปฏิบัติด้านห่วงโซ่อุปทานของผลิตภัณฑ์และซอฟต์แวร์")],
 mistakes=[("Assessing vendors only at onboarding and never again.", "ประเมินผู้ให้บริการเฉพาะตอนเริ่มต้นแล้วไม่ประเมินอีก"),
           ("Letting business units sign SaaS subscriptions with a credit card, bypassing procurement and security.", "ปล่อยให้หน่วยธุรกิจสมัครใช้ SaaS ด้วยบัตรเครดิต โดยไม่ผ่านฝ่ายจัดซื้อและหน่วยงานความมั่นคงปลอดภัย")],
)

C["GV-PRC-008"] = dict(
 purpose=("This procedure defines how suppliers are tiered, assessed before contract, monitored during the relationship, and offboarded, so that supplier risk stays within appetite.",
          "ระเบียบปฏิบัตินี้กำหนดวิธีการจัดระดับ ประเมินก่อนทำสัญญา ติดตามระหว่างความสัมพันธ์ และยุติความสัมพันธ์กับผู้ให้บริการ เพื่อให้ความเสี่ยงจากผู้ให้บริการอยู่ในระดับที่ยอมรับได้"),
 sections=[
  ("Supplier Tiering", "การจัดระดับผู้ให้บริการ", "Define tier criteria and the assurance required for each tier (GV.SC-04).", "กำหนดเกณฑ์การจัดระดับและระดับการให้ความเชื่อมั่นที่ต้องการในแต่ละระดับ (GV.SC-04)",
   {"t": ["Tier", "Criteria", "Assessment", "Review frequency"], "r": [
     ["Tier 1 (Critical)", "Supports a critical service, holds sensitive data, or has privileged or remote access", "Full questionnaire, evidence review, ISO/IEC 27001 or SOC 2 report, possible on-site review", "Annual"],
     ["Tier 2 (High)", "Holds internal or personal data, or network access with limits", "Standard questionnaire and evidence", "Every two years"],
     ["Tier 3 (Low)", "No data or system access", "Basic declaration", "At renewal"]], "w": [3.0, 5.5, 5.5, 2.5]},
   {"t": ["ระดับ", "เกณฑ์", "การประเมิน", "ความถี่ในการทบทวน"], "r": [
     ["ระดับ 1 (วิกฤต)", "สนับสนุนบริการสำคัญ เก็บข้อมูลอ่อนไหว หรือมีสิทธิ์ระดับสูงหรือการเข้าถึงระยะไกล", "แบบสอบถามฉบับเต็ม ตรวจหลักฐาน รายงาน ISO/IEC 27001 หรือ SOC 2 และอาจตรวจ ณ สถานที่", "ทุกปี"],
     ["ระดับ 2 (สูง)", "เก็บข้อมูลภายในหรือข้อมูลส่วนบุคคล หรือมีการเข้าถึงเครือข่ายแบบจำกัด", "แบบสอบถามมาตรฐานและหลักฐาน", "ทุก 2 ปี"],
     ["ระดับ 3 (ต่ำ)", "ไม่มีการเข้าถึงข้อมูลหรือระบบ", "หนังสือรับรองพื้นฐาน", "เมื่อต่อสัญญา"]], "w": [3.0, 5.5, 5.5, 2.5]}),
  ("Process Steps", "ขั้นตอนการดำเนินงาน", "Describe the life-cycle steps (GV.SC-06, GV.SC-07, GV.SC-10; ID.RA-10).", "อธิบายขั้นตอนตลอดวงจรชีวิต (GV.SC-06, GV.SC-07, GV.SC-10; ID.RA-10)",
   {"t": ["Step", "Activity", "Actor", "Output"], "r": [
     ["1", "Register the supplier and complete the tiering questions", "Business owner, [PROC]", "Entry in GV-REG-009"],
     ["2", "Send the Vendor Security Assessment Questionnaire (GV-FRM-006) by tier", "[CISO]", "Completed questionnaire and evidence"],
     ["3", "Assess risk, agree remediation, and decide go or no-go", "[CISO], business owner", "Assessment result; risk entry if needed"],
     ["4", "Include required clauses (GV-STD-002) and DPA (GV-TPL-004)", "[LEGAL], [PROC]", "Signed contract"],
     ["5", "Monitor: reassess by tier, track incidents, review access and performance", "[CISO], business owner", "Reassessment record"],
     ["6", "Offboard: revoke access, recover data, confirm deletion (GV-FRM-007)", "Business owner, [ITM]", "Signed offboarding checklist"]], "w": [1.2, 7.3, 3.8, 4.2]},
   {"t": ["ขั้นตอน", "กิจกรรม", "ผู้ดำเนินการ", "ผลลัพธ์"], "r": [
     ["1", "ลงทะเบียนผู้ให้บริการและตอบคำถามจัดระดับ", "เจ้าของธุรกิจ [PROC]", "รายการใน GV-REG-009"],
     ["2", "ส่งแบบสอบถามประเมินความมั่นคงปลอดภัย (GV-FRM-006) ตามระดับ", "[CISO]", "แบบสอบถามที่ตอบแล้วพร้อมหลักฐาน"],
     ["3", "ประเมินความเสี่ยง ตกลงการแก้ไข และตัดสินใจดำเนินการต่อหรือไม่", "[CISO] เจ้าของธุรกิจ", "ผลการประเมิน และรายการความเสี่ยง (ถ้ามี)"],
     ["4", "ระบุข้อสัญญาที่กำหนด (GV-STD-002) และ DPA (GV-TPL-004)", "[LEGAL] [PROC]", "สัญญาที่ลงนามแล้ว"],
     ["5", "ติดตาม: ประเมินซ้ำตามระดับ ติดตามเหตุการณ์ ทบทวนสิทธิ์และผลการให้บริการ", "[CISO] เจ้าของธุรกิจ", "บันทึกการประเมินซ้ำ"],
     ["6", "ยุติความสัมพันธ์: ถอนสิทธิ์ เรียกคืนข้อมูล ยืนยันการลบ (GV-FRM-007)", "เจ้าของธุรกิจ [ITM]", "แบบตรวจสอบการยุติความสัมพันธ์ที่ลงนามแล้ว"]], "w": [1.2, 7.3, 3.8, 4.2]}),
 ],
 bp=[("Accept independent assurance (ISO/IEC 27001 certificate with scope, SOC 2 Type II report) instead of long questionnaires for large providers.", "ยอมรับการรับรองจากผู้ตรวจสอบอิสระ (ใบรับรอง ISO/IEC 27001 พร้อมขอบเขต หรือรายงาน SOC 2 Type II) แทนแบบสอบถามยาวสำหรับผู้ให้บริการรายใหญ่"),
     ("Monitor critical suppliers continuously through breach news and external attack surface ratings.", "ติดตามผู้ให้บริการระดับวิกฤตอย่างต่อเนื่องผ่านข่าวเหตุละเมิดและการประเมินพื้นผิวการโจมตีจากภายนอก"),
     ("Hold an annual security review meeting with each Tier 1 supplier.", "จัดประชุมทบทวนด้านความมั่นคงปลอดภัยประจำปีกับผู้ให้บริการระดับ 1 ทุกราย")],
 mistakes=[("Accepting a certificate without checking that its scope covers the service you buy.", "ยอมรับใบรับรองโดยไม่ตรวจสอบว่าขอบเขตครอบคลุมบริการที่จัดซื้อ")],
 rev="Updated in August 2026 after the PACS vendor remote access issue to require Tier 1 vendors to use the CMC jump host with session recording.",
)

C["GV-REG-009"] = dict(
 purpose=("This register lists all suppliers and the services they provide, their tier, data and access, assessment status, and contract dates (GV.SC-04, ID.AM-04).",
          "ทะเบียนนี้ระบุผู้ให้บริการทุกรายและบริการที่ให้ ระดับ การเข้าถึงข้อมูลและระบบ สถานะการประเมิน และวันที่ของสัญญา (GV.SC-04, ID.AM-04)"),
 fields=[
  ("Supplier ID", "รหัสผู้ให้บริการ", "Unique reference.", "รหัสอ้างอิง", "SUP-001"),
  ("Supplier and service", "ผู้ให้บริการและบริการ", "Company and service description.", "บริษัทและรายละเอียดบริการ", ""),
  ("Business owner", "เจ้าของธุรกิจ", "Accountable role.", "บทบาทที่รับผิดชอบ", ""),
  ("Data and access", "ข้อมูลและการเข้าถึง", "Data types, remote or privileged access.", "ประเภทข้อมูล การเข้าถึงระยะไกลหรือสิทธิ์ระดับสูง", ""),
  ("Tier", "ระดับ", "1, 2, or 3.", "1 2 หรือ 3", "1"),
  ("Last assessment and result", "การประเมินล่าสุดและผล", "Date and outcome.", "วันที่และผล", ""),
  ("Assurance held", "หลักฐานการรับรอง", "Certificate or report and expiry.", "ใบรับรองหรือรายงานและวันหมดอายุ", ""),
  ("Contract end", "วันสิ้นสุดสัญญา", "Date.", "วันที่", ""),
  ("DPA signed", "ลงนาม DPA", "Yes, No, Not applicable.", "ใช่ ไม่ใช่ ไม่เกี่ยวข้อง", "Yes"),
 ],
 rows=[
  ["SUP-001", "HIS Vendor A: HIS licensing, support, customization", "CIO", "All patient data; privileged remote support", "1", "03/2026: Acceptable with 2 actions", "ISO/IEC 27001 (expires 11/2027)", "12/2028", "Yes"],
  ["SUP-002", "PACS Vendor B: PACS and modality support", "Director of Radiology", "Images; remote access to PACS and modalities", "1", "08/2026: Conditional (jump host required)", "None; questionnaire and evidence", "06/2027", "Yes"],
  ["SUP-003", "LIS Vendor C: laboratory system", "Laboratory Director", "Lab results; remote support", "1", "05/2026: Acceptable", "ISO/IEC 27001 (expires 02/2027)", "09/2027", "Yes"],
  ["SUP-004", "MSSP Vendor E: 24x7 monitoring and incident response retainer", "Security Manager", "Logs, read-only security console access", "1", "01/2026: Acceptable", "ISO/IEC 27001 and SOC 2 Type II", "02/2028", "Yes"],
  ["SUP-005", "Microsoft: Microsoft 365", "CIO", "Email, documents, identity", "1", "02/2026: Acceptable (independent reports)", "ISO/IEC 27001, SOC 2 Type II", "Annual subscription", "Yes (online terms)"],
  ["SUP-006", "Cleaning services company", "Facilities and Engineering Manager", "Physical access to wards, no system access", "3", "At renewal 2025", "Not applicable", "12/2026", "Not applicable"],
 ],
 bp=[("Reconcile the register with accounts payable data each year to find suppliers that bypassed procurement.", "กระทบยอดทะเบียนกับข้อมูลเจ้าหนี้ทุกปี เพื่อค้นหาผู้ให้บริการที่ไม่ได้ผ่านฝ่ายจัดซื้อ"),
     ("Record fourth parties (sub-processors) for Tier 1 suppliers.", "บันทึกผู้ให้บริการช่วง (Fourth party) ของผู้ให้บริการระดับ 1")],
 mistakes=[("Keeping the register in procurement only, without security tier or access data.", "เก็บทะเบียนไว้ที่ฝ่ายจัดซื้อเท่านั้นโดยไม่มีข้อมูลระดับความเสี่ยงหรือการเข้าถึง")],
)

C["GV-FRM-006"] = dict(
 purpose=("This questionnaire collects evidence of a supplier's security and privacy controls so that risk can be assessed before contract and at reassessment.",
          "แบบสอบถามนี้รวบรวมหลักฐานด้านมาตรการรักษาความมั่นคงปลอดภัยและความเป็นส่วนตัวของผู้ให้บริการ เพื่อประเมินความเสี่ยงก่อนทำสัญญาและเมื่อประเมินซ้ำ"),
 fields=[
  ("Governance and certification", "การกำกับดูแลและการรับรอง", "Security policy, responsible person, ISO/IEC 27001 or SOC 2 scope and date.", "นโยบายความมั่นคงปลอดภัย ผู้รับผิดชอบ ขอบเขตและวันที่ของ ISO/IEC 27001 หรือ SOC 2", ""),
  ("Data protection", "การคุ้มครองข้อมูล", "Data location, encryption at rest and in transit, retention, deletion.", "ที่ตั้งข้อมูล การเข้ารหัสขณะจัดเก็บและขณะส่ง การเก็บรักษา การลบ", ""),
  ("Access control", "การควบคุมการเข้าถึง", "MFA, privileged access management, access reviews for staff who access customer data.", "MFA การบริหารสิทธิ์ระดับสูง และการทบทวนสิทธิ์ของพนักงานที่เข้าถึงข้อมูลลูกค้า", ""),
  ("Vulnerability and patch management", "การบริหารช่องโหว่และแพตช์", "Scan frequency, patch timelines, penetration tests.", "ความถี่การสแกน กรอบเวลาการติดตั้งแพตช์ การทดสอบเจาะระบบ", ""),
  ("Secure development", "การพัฒนาอย่างมั่นคงปลอดภัย", "Secure development practices, software bill of materials (SBOM) availability.", "แนวปฏิบัติการพัฒนาอย่างมั่นคงปลอดภัย และการจัดทำรายการส่วนประกอบซอฟต์แวร์ (SBOM)", ""),
  ("Logging and monitoring", "การบันทึกและการเฝ้าระวัง", "Log retention and 24x7 monitoring.", "ระยะเวลาเก็บ Log และการเฝ้าระวังตลอด 24 ชั่วโมง", ""),
  ("Incident response", "การรับมือเหตุการณ์", "Notification time to customers, contact point, history of breaches in the last 3 years.", "ระยะเวลาแจ้งลูกค้า จุดติดต่อ ประวัติเหตุละเมิดใน 3 ปีที่ผ่านมา", ""),
  ("Business continuity", "ความต่อเนื่องทางธุรกิจ", "Recovery time objective (RTO), recovery point objective (RPO), and last DR test date.", "เป้าหมายระยะเวลาการกู้คืน (RTO) เป้าหมายจุดกู้คืนข้อมูล (RPO) และวันที่ทดสอบ DR ครั้งล่าสุด", ""),
  ("Sub-processors", "ผู้ประมวลผลช่วง", "List and locations.", "รายชื่อและสถานที่ตั้ง", ""),
  ("Staff security", "ความมั่นคงปลอดภัยของบุคลากร", "Screening, NDA, training.", "การตรวจสอบประวัติ NDA และการอบรม", ""),
 ],
 cmc_vals=["Security policy approved 2025; no ISO/IEC 27001 certificate; plans certification 2027", "Images stored on CMC premises only; vendor holds no copies; TLS 1.2 for remote sessions",
           "Engineers use named accounts; MFA through the CMC jump host from August 2026; no shared accounts allowed", "Modality OS patches certified quarterly by the manufacturer; no customer-facing penetration test report",
           "SBOM available for the PACS application on request", "Vendor logs remote sessions; CMC records sessions on the jump host for 180 days",
           "Commits to notify CMC within 24 hours; no reported breaches in 3 years", "Vendor support RTO 8 hours; CMC DR test of PACS completed May 2026",
           "Regional support center in Singapore (remote support only)", "Engineers sign GV-FRM-002; annual security training"],
 approvals=["Reviewer", "CISO", "SYSOWN"],
 bp=[("Ask for evidence (reports, screenshots, certificates) rather than yes or no answers for Tier 1 suppliers.", "ขอหลักฐาน (รายงาน ภาพหน้าจอ ใบรับรอง) แทนคำตอบใช่หรือไม่ สำหรับผู้ให้บริการระดับ 1"),
     ("Use a recognized question set, such as the Shared Assessments SIG Lite or the Cloud Security Alliance CAIQ, to reduce supplier effort.", "ใช้ชุดคำถามที่เป็นที่ยอมรับ เช่น Shared Assessments SIG Lite หรือ Cloud Security Alliance CAIQ เพื่อลดภาระของผู้ให้บริการ")],
 mistakes=[("Sending a 300-question form to a low-risk supplier.", "ส่งแบบสอบถาม 300 ข้อให้ผู้ให้บริการที่มีความเสี่ยงต่ำ")],
)

C["GV-STD-002"] = dict(
 purpose=("This standard sets the security and privacy clauses that contracts must contain, scaled by supplier tier, so requirements are enforceable (GV.SC-05).",
          "มาตรฐานนี้กำหนดข้อสัญญาด้านความมั่นคงปลอดภัยและความเป็นส่วนตัวที่สัญญาต้องมี ตามระดับของผู้ให้บริการ เพื่อให้ข้อกำหนดบังคับใช้ได้ (GV.SC-05)"),
 sections=[
  ("Contract Requirements by Tier", "ข้อกำหนดในสัญญาตามระดับ", "List required clauses and the tiers to which they apply.", "ระบุข้อสัญญาที่ต้องมีและระดับของผู้ให้บริการที่ต้องใช้",
   {"t": ["ID", "Clause", "Tier 1", "Tier 2", "Tier 3"], "r": [
     ["SC-01", "Compliance with [Organization Name] security policies and applicable law", "Yes", "Yes", "Yes"],
     ["SC-02", "Confidentiality and data processing agreement (GV-TPL-004) where personal data is processed", "Yes", "Yes", "If applicable"],
     ["SC-03", "Incident notification within 24 hours of awareness and cooperation in investigation", "Yes", "Yes", "No"],
     ["SC-04", "Right to audit or to receive independent assurance reports each year", "Yes", "On request", "No"],
     ["SC-05", "Named personnel, background checks, and MFA for any access", "Yes", "Yes", "No"],
     ["SC-06", "Vulnerability and patch timelines for supplied products", "Yes", "Yes", "No"],
     ["SC-07", "Participation in incident response and continuity exercises (GV.SC-08)", "Yes", "No", "No"],
     ["SC-08", "Sub-contractor approval and flow-down of requirements", "Yes", "Yes", "No"],
     ["SC-09", "Return and certified deletion of data at contract end (GV.SC-10)", "Yes", "Yes", "If applicable"],
     ["SC-10", "Service levels for availability and recovery aligned with the BIA", "Yes", "If critical", "No"]], "w": [1.5, 8.5, 2.2, 2.2, 2.1]},
   {"t": ["รหัส", "ข้อสัญญา", "ระดับ 1", "ระดับ 2", "ระดับ 3"], "r": [
     ["SC-01", "ปฏิบัติตามนโยบายความมั่นคงปลอดภัยของ [ชื่อองค์กร] และกฎหมายที่เกี่ยวข้อง", "ใช่", "ใช่", "ใช่"],
     ["SC-02", "การรักษาความลับและข้อตกลงการประมวลผลข้อมูล (GV-TPL-004) เมื่อมีการประมวลผลข้อมูลส่วนบุคคล", "ใช่", "ใช่", "ถ้าเกี่ยวข้อง"],
     ["SC-03", "แจ้งเหตุการณ์ภายใน 24 ชั่วโมงนับแต่ทราบเหตุ และให้ความร่วมมือในการสอบสวน", "ใช่", "ใช่", "ไม่"],
     ["SC-04", "สิทธิในการตรวจสอบ หรือได้รับรายงานการรับรองจากผู้ตรวจสอบอิสระทุกปี", "ใช่", "เมื่อร้องขอ", "ไม่"],
     ["SC-05", "ระบุบุคลากร ตรวจสอบประวัติ และใช้ MFA ในการเข้าถึงทุกครั้ง", "ใช่", "ใช่", "ไม่"],
     ["SC-06", "กรอบเวลาการแก้ไขช่องโหว่และติดตั้งแพตช์ของผลิตภัณฑ์ที่ส่งมอบ", "ใช่", "ใช่", "ไม่"],
     ["SC-07", "เข้าร่วมการรับมือเหตุการณ์และการฝึกซ้อมความต่อเนื่อง (GV.SC-08)", "ใช่", "ไม่", "ไม่"],
     ["SC-08", "การอนุมัติผู้รับจ้างช่วง และการถ่ายทอดข้อกำหนด", "ใช่", "ใช่", "ไม่"],
     ["SC-09", "ส่งคืนและลบข้อมูลพร้อมหนังสือรับรองเมื่อสิ้นสุดสัญญา (GV.SC-10)", "ใช่", "ใช่", "ถ้าเกี่ยวข้อง"],
     ["SC-10", "ระดับการให้บริการด้านความพร้อมใช้งานและการกู้คืนที่สอดคล้องกับ BIA", "ใช่", "ถ้าเป็นบริการสำคัญ", "ไม่"]], "w": [1.5, 8.5, 2.2, 2.2, 2.1]}),
 ],
 bp=[("Create a standard security schedule that Legal attaches to every contract, rather than negotiating clauses one by one.", "จัดทำภาคผนวกด้านความมั่นคงปลอดภัยมาตรฐานที่ฝ่ายกฎหมายแนบกับทุกสัญญา แทนการเจรจาทีละข้อ"),
     ("Align incident notice periods with your own legal deadlines (72 hours to the PDPC; 24 hours for CII reporting).", "กำหนดระยะเวลาแจ้งเหตุให้สอดคล้องกับกำหนดตามกฎหมายขององค์กร (72 ชั่วโมงสำหรับ สคส. และ 24 ชั่วโมงสำหรับการรายงานของ CII)"),
     ("Add security requirements at renewal for legacy contracts that lack them.", "เพิ่มข้อกำหนดด้านความมั่นคงปลอดภัยเมื่อต่อสัญญาเดิมที่ยังไม่มี")],
 mistakes=[("Signing multi-year vendor contracts with no right to audit and no incident notice clause.", "ลงนามสัญญาหลายปีกับผู้ให้บริการโดยไม่มีสิทธิในการตรวจสอบและไม่มีข้อกำหนดการแจ้งเหตุ")],
)

C["GV-STD-003"] = dict(
 purpose=("This standard sets security requirements for acquiring hardware, software, and services, including authenticity, integrity, and supplier assessment before purchase (GV.SC-09, ID.RA-09, ID.RA-10).",
          "มาตรฐานนี้กำหนดข้อกำหนดด้านความมั่นคงปลอดภัยในการจัดหาฮาร์ดแวร์ ซอฟต์แวร์ และบริการ รวมถึงความถูกต้องแท้จริง ความครบถ้วน และการประเมินผู้ให้บริการก่อนจัดซื้อ (GV.SC-09, ID.RA-09, ID.RA-10)"),
 sections=[
  ("Acquisition Requirements", "ข้อกำหนดในการจัดหา", "List requirements that apply before purchase and before deployment.", "ระบุข้อกำหนดที่ใช้ก่อนการจัดซื้อและก่อนการติดตั้งใช้งาน",
   {"t": ["ID", "Requirement"], "r": [
     ["ACQ-01", "Define security requirements (authentication, logging, encryption, patch support period) in every request for proposal (RFP)."],
     ["ACQ-02", "Buy hardware and software only from authorized resellers or manufacturers; verify digital signatures and checksums before installation."],
     ["ACQ-03", "Require a minimum supported life of [5] years for new systems and a published end-of-support date."],
     ["ACQ-04", "Request a software bill of materials (SBOM) for critical software and medical or operational technology devices."],
     ["ACQ-05", "Complete supplier assessment (GV-PRC-008) before contract for Tier 1 and Tier 2 suppliers."],
     ["ACQ-06", "Run a security test or proof of concept (PoC) review for critical systems before go-live."],
     ["ACQ-07", "Review cloud services against the Cloud Security Standard (PR-STD-014)."]], "w": [1.8, 14.7]},
   {"t": ["รหัส", "ข้อกำหนด"], "r": [
     ["ACQ-01", "กำหนดข้อกำหนดด้านความมั่นคงปลอดภัย (การยืนยันตัวตน การบันทึก Log การเข้ารหัส ระยะเวลาสนับสนุนแพตช์) ในเอกสารเชิญชวนเสนอราคา (RFP) ทุกฉบับ"],
     ["ACQ-02", "จัดซื้อฮาร์ดแวร์และซอฟต์แวร์จากตัวแทนจำหน่ายที่ได้รับอนุญาตหรือผู้ผลิตเท่านั้น และตรวจสอบลายมือชื่อดิจิทัลและค่า Checksum ก่อนติดตั้ง"],
     ["ACQ-03", "กำหนดระยะเวลาสนับสนุนขั้นต่ำ [5] ปีสำหรับระบบใหม่ และต้องมีวันสิ้นสุดการสนับสนุนที่ประกาศชัดเจน"],
     ["ACQ-04", "ขอรายการส่วนประกอบซอฟต์แวร์ (SBOM) สำหรับซอฟต์แวร์สำคัญและอุปกรณ์การแพทย์หรือ OT"],
     ["ACQ-05", "ประเมินผู้ให้บริการ (GV-PRC-008) ก่อนทำสัญญาสำหรับผู้ให้บริการระดับ 1 และระดับ 2"],
     ["ACQ-06", "ทดสอบความมั่นคงปลอดภัยหรือทบทวนการทดสอบแนวคิด (PoC) สำหรับระบบสำคัญก่อนใช้งานจริง"],
     ["ACQ-07", "ทบทวนบริการคลาวด์ตามมาตรฐานความมั่นคงปลอดภัยบนระบบคลาวด์ (PR-STD-014)"]], "w": [1.8, 14.7]},
   {"t": ["ID", "CMC requirement"], "r": [
     ["ACQ-01", "Security requirements annex attached to every IT and medical equipment RFP since 2025."],
     ["ACQ-02", "Medical devices bought only through manufacturer-authorized distributors."],
     ["ACQ-03", "Minimum 7 years of security patch support for medical devices; 5 years for IT systems."],
     ["ACQ-04", "SBOM requested for all new imaging and laboratory devices from 2026."],
     ["ACQ-05", "Vendor assessment completed before contract for HIS, PACS, LIS, and MSSP."],
     ["ACQ-06", "Vulnerability scan of new medical devices in the biomedical engineering lab before connection."],
     ["ACQ-07", "Cloud services reviewed by the Security Manager and DPO."]], "w": [1.8, 14.7]}),
 ],
 bp=[("Involve security at requirement definition, not after vendor selection.", "ให้หน่วยงานความมั่นคงปลอดภัยเข้าร่วมตั้งแต่การกำหนดความต้องการ ไม่ใช่หลังจากเลือกผู้ขายแล้ว"),
     ("Score security requirements in vendor evaluation with a defined weight.", "ให้คะแนนข้อกำหนดด้านความมั่นคงปลอดภัยในการประเมินผู้ขายโดยกำหนดน้ำหนักชัดเจน")],
 mistakes=[("Buying medical or OT equipment whose operating system goes out of support within two years of purchase.", "จัดซื้ออุปกรณ์การแพทย์หรือ OT ที่ระบบปฏิบัติการหมดการสนับสนุนภายใน 2 ปีหลังซื้อ")],
)

C["GV-FRM-007"] = dict(
 purpose=("This checklist ensures that access, data, and assets are recovered and obligations confirmed when a supplier relationship ends (GV.SC-10).",
          "แบบตรวจสอบนี้ทำให้การถอนสิทธิ์ การเรียกคืนข้อมูลและทรัพย์สิน และการยืนยันหน้าที่ครบถ้วนเมื่อสิ้นสุดความสัมพันธ์กับผู้ให้บริการ (GV.SC-10)"),
 fields=[
  ("Supplier and service", "ผู้ให้บริการและบริการ", "From GV-REG-009.", "จาก GV-REG-009", ""),
  ("Contract end date", "วันสิ้นสุดสัญญา", "Date.", "วันที่", ""),
  ("Accounts and remote access revoked", "ถอนบัญชีและการเข้าถึงระยะไกล", "VPN, jump host, application, cloud accounts.", "VPN Jump host บัญชีแอปพลิเคชันและคลาวด์", ""),
  ("Shared credentials rotated", "เปลี่ยนรหัสผ่านที่ใช้ร่วม", "Service and administrator passwords known to the supplier.", "รหัสผ่านบัญชีบริการและผู้ดูแลระบบที่ผู้ให้บริการทราบ", ""),
  ("Data returned", "ส่งคืนข้อมูล", "Format and date.", "รูปแบบและวันที่", ""),
  ("Deletion certificate received", "ได้รับหนังสือรับรองการลบข้อมูล", "Date and reference.", "วันที่และเลขอ้างอิง", ""),
  ("Assets and badges returned", "คืนทรัพย์สินและบัตร", "Equipment, tokens, badges.", "อุปกรณ์ อุปกรณ์ยืนยันตัวตน บัตร", ""),
  ("Firewall rules and integrations removed", "ลบกฎไฟร์วอลล์และการเชื่อมต่อระบบ", "Rules and API keys.", "กฎไฟร์วอลล์และ API key", ""),
  ("Registers updated", "ปรับปรุงทะเบียน", "GV-REG-009, ID-REG-002, PR-REG-001.", "GV-REG-009, ID-REG-002, PR-REG-001", ""),
 ],
 cmc_vals=["SUP-011 Former nurse call maintenance contractor", "31 May 2026", "Remote support VPN profile and two local accounts disabled 31 May 2026",
           "Nurse call server administrator password changed 31 May 2026", "Configuration backup handed over on USB (encrypted) 31 May 2026", "Certificate DEL-2026-03 received 10 June 2026",
           "One maintenance laptop and two badges returned", "Firewall rule FW-0412 removed (change CHG-2026-0388)", "All three registers updated 12 June 2026"],
 approvals=["SYSOWN", "ITM", "CISO"],
 bp=[("Start offboarding 60 days before contract end so data return is planned.", "เริ่มกระบวนการยุติความสัมพันธ์ 60 วันก่อนสัญญาสิ้นสุด เพื่อวางแผนการส่งคืนข้อมูล")],
 mistakes=[("Leaving vendor firewall rules and VPN accounts active years after the contract ends.", "ปล่อยให้กฎไฟร์วอลล์และบัญชี VPN ของผู้ให้บริการยังใช้งานได้หลายปีหลังสัญญาสิ้นสุด")],
)
