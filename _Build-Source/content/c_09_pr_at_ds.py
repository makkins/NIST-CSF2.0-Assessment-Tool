# -*- coding: utf-8 -*-
# PR.AT Awareness and Training; PR.DS Data Security
C = {}

C["PR-PLN-001"] = dict(
 purpose=("This program plans security awareness and role-based training so that all personnel understand their responsibilities and specialized roles have the skills they need (PR.AT-01, PR.AT-02; NIST SP 800-50 Rev. 1).",
          "แผนนี้กำหนดการสร้างความตระหนักรู้และการฝึกอบรมตามบทบาท เพื่อให้บุคลากรทุกคนเข้าใจหน้าที่ของตน และบทบาทเฉพาะทางมีทักษะที่จำเป็น (PR.AT-01, PR.AT-02; NIST SP 800-50 Rev. 1)"),
 sections=[
  ("Audiences and Content", "กลุ่มเป้าหมายและเนื้อหา", "Define audiences, topics, delivery, and frequency.", "กำหนดกลุ่มเป้าหมาย หัวข้อ วิธีการ และความถี่",
   {"t": ["Audience", "Topics", "Delivery", "Frequency"], "r": [
     ["All personnel", "Phishing, passwords and MFA, data handling, reporting incidents, privacy basics, acceptable use", "E-learning plus quiz", "Onboarding and annually"],
     ["Managers", "Access approval, risk ownership, handling staff incidents", "Briefing", "Annually"],
     ["IT and administrators", "Secure configuration, privileged access, logging, incident handling", "Technical training", "Annually"],
     ["Developers", "Secure coding (OWASP Top 10), secrets handling", "Workshop", "Annually"],
     ["Executives and board", "Cyber risk, regulatory duties, crisis decisions", "Briefing and tabletop", "Annually"],
     ["High-risk roles (finance, HR)", "Business email compromise, payment fraud", "Targeted session", "Semi-annually"]], "w": [3.5, 6.5, 3.5, 3.0]},
   {"t": ["กลุ่มเป้าหมาย", "หัวข้อ", "วิธีการ", "ความถี่"], "r": [
     ["บุคลากรทุกคน", "ฟิชชิ่ง รหัสผ่านและ MFA การจัดการข้อมูล การรายงานเหตุ ความเป็นส่วนตัวเบื้องต้น การใช้งานที่ยอมรับได้", "E-learning พร้อมแบบทดสอบ", "เมื่อเริ่มงานและทุกปี"],
     ["ผู้บริหารหน่วยงาน", "การอนุมัติสิทธิ์ การเป็นเจ้าของความเสี่ยง การจัดการเหตุที่เกี่ยวกับบุคลากร", "การบรรยายสรุป", "ทุกปี"],
     ["ฝ่าย IT และผู้ดูแลระบบ", "การตั้งค่าอย่างมั่นคงปลอดภัย สิทธิ์ระดับสูง การบันทึก Log การจัดการเหตุการณ์", "การอบรมทางเทคนิค", "ทุกปี"],
     ["นักพัฒนา", "การเขียนโค้ดอย่างมั่นคงปลอดภัย (OWASP Top 10) การจัดการข้อมูลลับในโค้ด", "Workshop", "ทุกปี"],
     ["ผู้บริหารระดับสูงและคณะกรรมการ", "ความเสี่ยงด้านไซเบอร์ หน้าที่ตามกฎหมาย การตัดสินใจในภาวะวิกฤต", "การบรรยายสรุปและ Tabletop", "ทุกปี"],
     ["บทบาทความเสี่ยงสูง (การเงิน HR)", "การหลอกลวงทางอีเมลธุรกิจ การฉ้อโกงการชำระเงิน", "การอบรมเฉพาะกลุ่ม", "ทุก 6 เดือน"]], "w": [3.5, 6.5, 3.5, 3.0]},
   {"t": ["Audience", "Topics", "Delivery", "Frequency"], "r": [
     ["All staff (1,200)", "Phishing, MFA, patient data handling, reporting, acceptable use", "20-minute e-learning in Thai and English", "Onboarding and annually"],
     ["Physicians and nurses", "Patient privacy, shared workstation habits, clinical messaging rules", "10-minute module plus ward huddle talks", "Annually"],
     ["IT team (25)", "PAM use, secure configuration, incident first response", "Vendor and MSSP-led sessions", "Annually"],
     ["Finance and procurement", "Invoice fraud and bank detail change verification", "Targeted session after INC-2026-014", "Semi-annually"],
     ["ISSC and Audit Committee", "Ransomware decision-making, CII and PDPA notification duties", "Tabletop", "Annually"]], "w": [3.5, 6.5, 3.5, 3.0]}),
  ("Measurement", "การวัดผล", "Define how effectiveness is measured.", "กำหนดวิธีวัดประสิทธิผล",
   ["Completion rate (target 95%).", "Quiz pass rate (target 80%).", "Phishing simulation click rate (target below 10%) and report rate (target above 60%).", "Number of incidents caused by user error (trend)."],
   ["อัตราการเข้าอบรมครบ (เป้าหมาย 95%)", "อัตราการผ่านแบบทดสอบ (เป้าหมาย 80%)", "อัตราการคลิกในการทดสอบฟิชชิ่ง (เป้าหมายต่ำกว่า 10%) และอัตราการรายงาน (เป้าหมายมากกว่า 60%)", "จำนวนเหตุการณ์ที่เกิดจากความผิดพลาดของผู้ใช้ (แนวโน้ม)"]),
 ],
 bp=[("Keep modules short and role-specific; long generic courses have low retention.", "ทำบทเรียนให้สั้นและเฉพาะบทบาท เพราะหลักสูตรทั่วไปที่ยาวทำให้จดจำได้น้อย"),
     ("Measure reporting rate, not only click rate; reporting is the behavior that stops attacks.", "วัดอัตราการรายงาน ไม่ใช่เฉพาะอัตราการคลิก เพราะการรายงานคือพฤติกรรมที่หยุดการโจมตีได้"),
     ("Use real incidents (anonymized) as teaching material.", "ใช้เหตุการณ์จริง (ปกปิดข้อมูลระบุตัวตน) เป็นสื่อการสอน")],
 mistakes=[("Treating annual click-through training as the whole program.", "ถือว่าการอบรมออนไลน์ปีละครั้งคือแผนงานทั้งหมด")],
)

C["PR-REG-002"] = dict(
 purpose=("This matrix records the security competencies required for each specialized role, the current level of each person, and planned training, as evidence of competence (PR.AT-02; ISO/IEC 27001:2022 Clause 7.2).",
          "ตารางนี้บันทึกสมรรถนะด้านความมั่นคงปลอดภัยที่บทบาทเฉพาะทางแต่ละบทบาทต้องมี ระดับปัจจุบันของแต่ละบุคคล และการฝึกอบรมที่วางแผนไว้ เป็นหลักฐานด้านสมรรถนะ (PR.AT-02; ISO/IEC 27001:2022 ข้อ 7.2)"),
 fields=[
  ("Person or role", "บุคคลหรือบทบาท", "Name or role.", "ชื่อหรือบทบาท", ""),
  ("Competency", "สมรรถนะ", "Skill area.", "ด้านทักษะ", ("Incident handling", "การจัดการเหตุการณ์")),
  ("Required level (1 to 4)", "ระดับที่ต้องการ (1 ถึง 4)", "1 Awareness, 2 Practitioner, 3 Advanced, 4 Expert.", "1 รับรู้ 2 ปฏิบัติได้ 3 ขั้นสูง 4 ผู้เชี่ยวชาญ", "3"),
  ("Current level", "ระดับปัจจุบัน", "Assessed level.", "ระดับที่ประเมิน", "2"),
  ("Evidence", "หลักฐาน", "Certification, training, assessment.", "ใบรับรอง การอบรม การประเมิน", ""),
  ("Development action and date", "การพัฒนาและกำหนดเวลา", "Training or certification planned.", "การอบรมหรือการสอบใบรับรองที่วางแผนไว้", ""),
 ],
 rows=[
  ["Security Manager", "Risk management and governance", "4", "3", "ISO/IEC 27001 Lead Implementer; CISSP in progress", "CISSP by 06/2027"],
  ["Security Engineer 1", "Incident handling", "3", "2", "Internal drill EX-2026-02", "Incident handler course, Q1 2027"],
  ["Security Engineer 2", "Identity and PAM administration", "3", "3", "Vendor PAM certification 2026", "Maintain"],
  ["IT Infrastructure Manager", "Backup and recovery", "3", "3", "DR test DR-2026-01 lead", "Maintain"],
  ["Application Manager", "Secure development", "3", "2", "OWASP workshop 2025", "Secure code review training, Q4 2026"],
 ],
 bp=[("Base levels on observable evidence, not self-assessment alone.", "ประเมินระดับจากหลักฐานที่สังเกตได้ ไม่ใช่การประเมินตนเองเพียงอย่างเดียว"),
     ("Use the matrix to plan cross-training and succession for single points of failure.", "ใช้ตารางในการวางแผนฝึกอบรมข้ามสายงานและการสืบทอดตำแหน่งสำหรับบุคคลที่เป็นจุดเสี่ยงเดี่ยว")],
 mistakes=[("Listing certifications without linking them to role requirements.", "ระบุใบรับรองโดยไม่เชื่อมโยงกับข้อกำหนดของบทบาท")],
)

C["PR-REC-002"] = dict(
 purpose=("This record tracks completion of security awareness and role-based training for each person, as evidence for audit and regulators (PR.AT-01; ISO/IEC 27001:2022 Clause 7.2).",
          "บันทึกนี้ติดตามการเข้ารับการฝึกอบรมด้านความตระหนักรู้และการฝึกอบรมตามบทบาทของแต่ละบุคคล เป็นหลักฐานสำหรับการตรวจสอบและหน่วยงานกำกับดูแล (PR.AT-01; ISO/IEC 27001:2022 ข้อ 7.2)"),
 fields=[
  ("Course", "หลักสูตร", "Course name and version.", "ชื่อหลักสูตรและฉบับ", ""),
  ("Audience", "กลุ่มเป้าหมาย", "Target group.", "กลุ่มเป้าหมาย", ""),
  ("Required", "จำนวนที่ต้องอบรม", "Number of people.", "จำนวนคน", ""),
  ("Completed", "จำนวนที่อบรมแล้ว", "Number completed.", "จำนวนที่อบรมครบ", ""),
  ("Completion rate", "อัตราการอบรมครบ", "Percentage.", "ร้อยละ", ""),
  ("Pass rate", "อัตราการผ่าน", "Quiz pass percentage.", "ร้อยละการผ่านแบบทดสอบ", ""),
  ("Period", "ช่วงเวลา", "Reporting period.", "ช่วงเวลาที่รายงาน", ""),
 ],
 rows=[
  ["Security and Privacy Essentials 2026", "All staff", "1,214", "1,105", "91%", "88%", "01/2026 to 09/2026"],
  ["Patient Privacy for Clinicians 2026", "Physicians and nurses", "742", "698", "94%", "92%", "01/2026 to 09/2026"],
  ["Invoice Fraud Awareness", "Finance and procurement", "46", "46", "100%", "96%", "07/2026"],
  ["Ransomware Tabletop EX-2026-01", "ISSC and ward heads", "22", "20", "91%", "Not applicable", "02/2026"],
 ],
 bp=[("Export completion data from the learning system monthly and follow up with managers of non-completers.", "ดึงข้อมูลการอบรมจากระบบการเรียนรู้ทุกเดือน และติดตามผู้บังคับบัญชาของผู้ที่ยังไม่อบรม")],
 mistakes=[("No individual records, only attendance sheets that cannot prove who completed what.", "ไม่มีบันทึกรายบุคคล มีเพียงใบลงชื่อที่พิสูจน์ไม่ได้ว่าใครอบรมหลักสูตรใด")],
)

C["PR-PRC-004"] = dict(
 purpose=("This procedure governs simulated phishing campaigns that measure and improve staff resistance to phishing, while protecting staff privacy and trust.",
          "ระเบียบปฏิบัตินี้กำกับการทดสอบฟิชชิ่งจำลองเพื่อวัดและพัฒนาความสามารถของบุคลากรในการรับมือฟิชชิ่ง โดยคุ้มครองความเป็นส่วนตัวและความไว้วางใจของบุคลากร"),
 sections=[
  ("Rules", "กฎการดำเนินการ", "Set rules for running campaigns ethically.", "กำหนดกฎการทดสอบอย่างมีจริยธรรม",
   ["Campaigns are approved by the [CISO] and HR; executives are informed but not exempt.", "Scenarios reflect real threats but avoid content that causes distress (for example, fake bonuses or health alarms).",
    "Results are reported in aggregate; individual results are used only for coaching, not punishment, unless repeated after training.", "Users who click receive immediate short training.", "Personal data in results is handled per the employee privacy notice."],
   ["[CISO] และ HR อนุมัติการทดสอบ ผู้บริหารได้รับแจ้งแต่ไม่ได้รับการยกเว้น", "สถานการณ์สะท้อนภัยคุกคามจริง แต่หลีกเลี่ยงเนื้อหาที่สร้างความทุกข์ใจ (เช่น โบนัสปลอม หรือการแจ้งเตือนด้านสุขภาพ)",
    "รายงานผลในภาพรวม ใช้ผลรายบุคคลเพื่อการพัฒนาเท่านั้น ไม่ใช้ลงโทษ เว้นแต่เกิดซ้ำหลังได้รับการอบรมแล้ว", "ผู้ที่คลิกได้รับการอบรมสั้นทันที", "จัดการข้อมูลส่วนบุคคลในผลการทดสอบตามประกาศความเป็นส่วนตัวสำหรับพนักงาน"]),
  ("Campaign Steps", "ขั้นตอนการทดสอบ", "Describe steps per campaign.", "อธิบายขั้นตอนของการทดสอบแต่ละครั้ง",
   {"n": ["Plan scenario, audience, and timing; whitelist the simulation platform with the email team and SOC.", "Launch and monitor; pause if it disrupts operations.", "Deliver just-in-time training to clickers.", "Report click, credential entry, and report rates by department.", "Plan targeted training for high-risk groups."]},
   {"n": ["วางแผนสถานการณ์ กลุ่มเป้าหมาย และช่วงเวลา และแจ้งทีมอีเมลและ SOC ให้อนุญาตระบบทดสอบ", "เริ่มทดสอบและติดตาม หยุดชั่วคราวหากรบกวนการปฏิบัติงาน", "ให้การอบรมทันทีแก่ผู้ที่คลิก", "รายงานอัตราการคลิก การกรอกรหัสผ่าน และการรายงานแยกตามหน่วยงาน", "วางแผนการอบรมเฉพาะกลุ่มสำหรับกลุ่มความเสี่ยงสูง"]}),
 ],
 bp=[("Avoid running campaigns during clinical or operational peaks.", "หลีกเลี่ยงการทดสอบในช่วงที่งานคลินิกหรืองานปฏิบัติการหนาแน่น"),
     ("Celebrate departments with high report rates.", "ชื่นชมหน่วยงานที่มีอัตราการรายงานสูง")],
 mistakes=[("Publicly naming staff who clicked, which damages trust and reduces reporting.", "ประกาศชื่อบุคลากรที่คลิกต่อสาธารณะ ทำให้เสียความไว้วางใจและลดการรายงาน")],
)

C["PR-POL-003"] = dict(
 purpose=("This policy sets how information is classified and protected according to its sensitivity, at rest, in transit, and in use, throughout its life cycle (PR.DS-01, PR.DS-02, PR.DS-10).",
          "นโยบายนี้กำหนดวิธีจัดชั้นและปกป้องข้อมูลตามระดับความอ่อนไหว ทั้งขณะจัดเก็บ ขณะส่ง และขณะใช้งาน ตลอดวงจรชีวิตของข้อมูล (PR.DS-01, PR.DS-02, PR.DS-10)"),
 sections=[
  ("Policy Statements", "ข้อความนโยบาย", "State mandatory data protection principles.", "ระบุหลักการปกป้องข้อมูลที่บังคับ",
   ["All information has an owner who assigns its classification using the Information Classification and Handling Standard (PR-STD-004).",
    "Protection controls (encryption, access, labeling, sharing) are applied according to classification.", "Restricted and Confidential data are encrypted at rest and in transit (PR-STD-005).",
    "Data is backed up according to the Backup Standard (PR-STD-006).", "Data is retained only as long as required and then securely disposed of (PR-STD-007).",
    "Transfer of Restricted data to third parties requires a contract with security and data protection clauses."],
   ["ข้อมูลทุกประเภทมีเจ้าของ ซึ่งกำหนดชั้นข้อมูลตามมาตรฐานการจัดชั้นความลับและการจัดการข้อมูล (PR-STD-004)",
    "ใช้มาตรการปกป้อง (การเข้ารหัส การเข้าถึง การติดป้าย การแบ่งปัน) ตามชั้นข้อมูล", "เข้ารหัสข้อมูลระดับ Restricted และ Confidential ทั้งขณะจัดเก็บและขณะส่ง (PR-STD-005)",
    "สำรองข้อมูลตามมาตรฐานการสำรองข้อมูล (PR-STD-006)", "เก็บรักษาข้อมูลเท่าที่จำเป็น และทำลายอย่างมั่นคงปลอดภัย (PR-STD-007)",
    "การส่งข้อมูลระดับ Restricted ให้บุคคลภายนอกต้องมีสัญญาที่มีข้อกำหนดด้านความมั่นคงปลอดภัยและการคุ้มครองข้อมูล"]),
 ],
 bp=[("Keep classification to three or four levels that users can remember.", "จำกัดชั้นข้อมูลไว้ 3 ถึง 4 ระดับที่ผู้ใช้จดจำได้"),
     ("Apply default labels automatically where possible, rather than relying on users to label every file.", "ใช้การติดป้ายอัตโนมัติเป็นค่าเริ่มต้นเมื่อทำได้ แทนการพึ่งพาให้ผู้ใช้ติดป้ายทุกไฟล์")],
 mistakes=[("Classifying everything as Confidential, so the label carries no meaning.", "จัดทุกอย่างเป็นข้อมูลลับ ทำให้ป้ายกำกับไม่มีความหมาย")],
)

C["PR-STD-004"] = dict(
 purpose=("This standard defines the classification levels and the handling rules for each level, covering labeling, storage, sharing, transmission, printing, and disposal.",
          "มาตรฐานนี้กำหนดระดับชั้นข้อมูลและกฎการจัดการของแต่ละระดับ ครอบคลุมการติดป้าย การจัดเก็บ การแบ่งปัน การส่ง การพิมพ์ และการทำลาย"),
 sections=[
  ("Classification Levels", "ระดับชั้นข้อมูล", "Define each level with examples.", "กำหนดแต่ละระดับพร้อมตัวอย่าง",
   {"t": ["Level", "Definition", "Examples"], "r": [
     ["Restricted", "Disclosure could cause severe harm, legal penalty, or harm to individuals", "Sensitive personal data (PDPA s.26), credentials, encryption keys, merger plans"],
     ["Confidential", "Disclosure could harm the organization or individuals", "Personal data, contracts, financial results before release, security reports"],
     ["Internal", "For staff use; limited harm if disclosed", "Policies, internal announcements, procedures"],
     ["Public", "Approved for public release", "Website content, brochures"]], "w": [2.8, 6.2, 7.5]},
   {"t": ["ระดับ", "คำนิยาม", "ตัวอย่าง"], "r": [
     ["Restricted (ลับที่สุด)", "การเปิดเผยอาจก่อความเสียหายร้ายแรง โทษทางกฎหมาย หรืออันตรายต่อบุคคล", "ข้อมูลส่วนบุคคลอ่อนไหว (PDPA มาตรา 26) ข้อมูลยืนยันตัวตน กุญแจเข้ารหัส แผนควบรวมกิจการ"],
     ["Confidential (ลับ)", "การเปิดเผยอาจก่อความเสียหายต่อองค์กรหรือบุคคล", "ข้อมูลส่วนบุคคล สัญญา ผลประกอบการก่อนเผยแพร่ รายงานด้านความมั่นคงปลอดภัย"],
     ["Internal (ใช้ภายใน)", "สำหรับบุคลากร เกิดความเสียหายจำกัดหากเปิดเผย", "นโยบาย ประกาศภายใน ระเบียบปฏิบัติ"],
     ["Public (สาธารณะ)", "อนุมัติให้เผยแพร่สู่สาธารณะ", "เนื้อหาบนเว็บไซต์ แผ่นพับ"]], "w": [2.8, 6.2, 7.5]},
   {"t": ["Level", "Definition", "CMC examples"], "r": [
     ["Restricted", "Severe harm, legal penalty, or patient harm", "Medical records, images, lab results, HIV and mental health notes, credentials"],
     ["Confidential", "Harm to CMC or individuals", "Staff personal data, contracts, financial data, security reports"],
     ["Internal", "Staff use", "Clinical guidelines, internal announcements"],
     ["Public", "Approved for release", "Website, health education material"]], "w": [2.8, 6.2, 7.5]}),
  ("Handling Rules", "กฎการจัดการ", "Set rules per level for key handling activities.", "กำหนดกฎสำหรับกิจกรรมการจัดการหลักในแต่ละระดับ",
   {"t": ["Activity", "Restricted", "Confidential", "Internal"], "r": [
     ["Labeling", "Label required", "Label required", "Default label"], ["Storage", "Approved systems only; encrypted", "Approved systems; encrypted on portable devices", "Approved systems"],
     ["Email outside the organization", "Encrypted and approved only", "Encrypted", "Allowed"], ["Removable media", "Prohibited unless approved and encrypted", "Encrypted only", "Allowed"],
     ["Printing", "Secure print release; collect immediately", "Collect immediately", "No restriction"], ["Disposal", "Shred or destroy media (NIST SP 800-88 Purge or Destroy)", "Shred; wipe media", "Recycle bin"]], "w": [3.4, 4.6, 4.5, 4.0]},
   {"t": ["กิจกรรม", "Restricted", "Confidential", "Internal"], "r": [
     ["การติดป้าย", "ต้องติดป้าย", "ต้องติดป้าย", "ป้ายค่าเริ่มต้น"], ["การจัดเก็บ", "เฉพาะระบบที่อนุมัติและเข้ารหัส", "ระบบที่อนุมัติ และเข้ารหัสบนอุปกรณ์พกพา", "ระบบที่อนุมัติ"],
     ["การส่งอีเมลออกนอกองค์กร", "เข้ารหัสและได้รับอนุมัติเท่านั้น", "เข้ารหัส", "อนุญาต"], ["สื่อบันทึกข้อมูลแบบถอดได้", "ห้าม เว้นแต่ได้รับอนุมัติและเข้ารหัส", "เข้ารหัสเท่านั้น", "อนุญาต"],
     ["การพิมพ์", "ใช้การพิมพ์แบบยืนยันตัวตนที่เครื่องพิมพ์ และรับเอกสารทันที", "รับเอกสารทันที", "ไม่จำกัด"], ["การทำลาย", "ย่อยหรือทำลายสื่อ (NIST SP 800-88 Purge หรือ Destroy)", "ย่อยเอกสาร และล้างข้อมูลในสื่อ", "ถังรีไซเคิล"]], "w": [3.4, 4.6, 4.5, 4.0]}),
 ],
 bp=[("Use sensitivity labels in the collaboration platform that apply encryption automatically.", "ใช้ป้ายระดับความอ่อนไหวในระบบทำงานร่วมกันที่เข้ารหัสอัตโนมัติ"),
     ("Train staff with real examples from their own work.", "อบรมบุคลากรด้วยตัวอย่างจริงจากงานของตน")],
 mistakes=[("Rules that users cannot follow with the tools provided.", "กฎที่ผู้ใช้ปฏิบัติตามไม่ได้ด้วยเครื่องมือที่องค์กรจัดให้")],
)

C["PR-STD-005"] = dict(
 purpose=("This standard sets approved cryptographic algorithms, protocols, and key management practices to protect data at rest and in transit (PR.DS-01, PR.DS-02).",
          "มาตรฐานนี้กำหนดอัลกอริทึม โปรโตคอลการเข้ารหัส และแนวปฏิบัติการบริหารจัดการกุญแจที่อนุมัติ เพื่อปกป้องข้อมูลขณะจัดเก็บและขณะส่ง (PR.DS-01, PR.DS-02)"),
 sections=[
  ("Approved Cryptography", "การเข้ารหัสที่อนุมัติ", "List approved and prohibited algorithms and protocols.", "ระบุอัลกอริทึมและโปรโตคอลที่อนุมัติและที่ห้ามใช้",
   {"t": ["Use", "Approved", "Prohibited"], "r": [
     ["Data in transit", "TLS 1.2 (approved cipher suites) or TLS 1.3; SSH v2; IPsec with AES", "SSL, TLS 1.0 and 1.1, Telnet, FTP"],
     ["Data at rest", "AES-256 (full disk, database, backup)", "DES, 3DES, RC4"],
     ["Hashing", "SHA-256 or stronger", "MD5, SHA-1 for security purposes"],
     ["Password storage", "Salted adaptive hashing (bcrypt, scrypt, Argon2, PBKDF2)", "Plain text, unsalted hashes, reversible encryption"],
     ["Public key", "RSA 3072 or larger; ECDSA P-256 or larger", "RSA below 2048"]], "w": [3.5, 7.5, 5.5]},
   {"t": ["การใช้งาน", "ที่อนุมัติ", "ที่ห้ามใช้"], "r": [
     ["ข้อมูลขณะส่ง", "TLS 1.2 (ชุดการเข้ารหัสที่อนุมัติ) หรือ TLS 1.3, SSH v2, IPsec ด้วย AES", "SSL, TLS 1.0 และ 1.1, Telnet, FTP"],
     ["ข้อมูลขณะจัดเก็บ", "AES-256 (ทั้งดิสก์ ฐานข้อมูล ข้อมูลสำรอง)", "DES, 3DES, RC4"],
     ["การแฮช", "SHA-256 หรือสูงกว่า", "MD5 และ SHA-1 เพื่อวัตถุประสงค์ด้านความมั่นคงปลอดภัย"],
     ["การจัดเก็บรหัสผ่าน", "Adaptive hashing พร้อม Salt (bcrypt, scrypt, Argon2, PBKDF2)", "ข้อความธรรมดา แฮชที่ไม่มี Salt การเข้ารหัสที่ถอดกลับได้"],
     ["กุญแจสาธารณะ", "RSA 3072 บิตขึ้นไป หรือ ECDSA P-256 ขึ้นไป", "RSA ต่ำกว่า 2048 บิต"]], "w": [3.5, 7.5, 5.5]}),
  ("Key Management", "การบริหารจัดการกุญแจ", "Set key life-cycle requirements.", "กำหนดข้อกำหนดตลอดวงจรชีวิตของกุญแจ",
   ["Keys are generated in approved systems (hardware security module or cloud key management service).", "Keys are stored separately from the data they protect and access is limited to named custodians.",
    "Keys are rotated at least annually or on suspected compromise; certificates are tracked for expiry.", "Key backup and recovery is tested; destroyed keys are recorded."],
   ["สร้างกุญแจในระบบที่อนุมัติ (Hardware security module หรือบริการบริหารกุญแจบนคลาวด์)", "จัดเก็บกุญแจแยกจากข้อมูลที่ปกป้อง และจำกัดการเข้าถึงเฉพาะผู้ดูแลที่ระบุชื่อ",
    "เปลี่ยนกุญแจอย่างน้อยปีละครั้ง หรือเมื่อสงสัยว่ารั่วไหล และติดตามวันหมดอายุของใบรับรอง", "ทดสอบการสำรองและกู้คืนกุญแจ และบันทึกการทำลายกุญแจ"]),
 ],
 bp=[("Maintain a certificate inventory with automated expiry alerts; expired certificates cause outages.", "จัดทำทะเบียนใบรับรองพร้อมแจ้งเตือนวันหมดอายุอัตโนมัติ เพราะใบรับรองหมดอายุทำให้ระบบหยุดทำงาน"),
     ("Plan for post-quantum cryptography by inventorying where public-key algorithms are used.", "เตรียมพร้อมสำหรับการเข้ารหัสยุคหลังควอนตัม โดยสำรวจจุดที่ใช้อัลกอริทึมกุญแจสาธารณะ")],
 mistakes=[("Encryption keys stored on the same server as the encrypted database.", "จัดเก็บกุญแจเข้ารหัสไว้บนเซิร์ฟเวอร์เดียวกับฐานข้อมูลที่เข้ารหัส")],
)

C["PR-STD-006"] = dict(
 purpose=("This standard sets backup scope, frequency, retention, protection, and testing so that data can be restored within recovery objectives, including after ransomware (PR.DS-11).",
          "มาตรฐานนี้กำหนดขอบเขต ความถี่ ระยะเวลาเก็บรักษา การปกป้อง และการทดสอบการสำรองข้อมูล เพื่อให้กู้คืนข้อมูลได้ภายในเป้าหมาย รวมถึงหลังการโจมตีด้วยแรนซัมแวร์ (PR.DS-11)"),
 sections=[
  ("Requirements", "ข้อกำหนด", "Set measurable backup requirements by criticality.", "กำหนดข้อกำหนดการสำรองข้อมูลที่วัดผลได้ตามระดับความสำคัญ",
   {"t": ["ID", "Requirement", "Critical systems", "Other systems"], "r": [
     ["BK-01", "Backup frequency meets RPO from the BIA", "At least every 15 minutes (logs) and daily (full or incremental)", "Daily"],
     ["BK-02", "3-2-1 rule: three copies, two media types, one off-site", "Required", "Required"],
     ["BK-03", "At least one copy immutable or offline (air-gapped)", "Required", "Recommended"],
     ["BK-04", "Backups encrypted (AES-256)", "Required", "Required"],
     ["BK-05", "Backup admin accounts separate from the domain, with MFA", "Required", "Required"],
     ["BK-06", "Retention", "Daily 30 days; monthly 12 months; yearly per legal retention", "Daily 14 days; monthly 6 months"],
     ["BK-07", "Restore testing", "Monthly sample; full system annually", "Quarterly sample"],
     ["BK-08", "Backup job monitoring", "Failures alerted and fixed within 1 working day", "Within 3 working days"]], "w": [1.5, 6.5, 4.8, 3.7]},
   {"t": ["รหัส", "ข้อกำหนด", "ระบบสำคัญ", "ระบบอื่น"], "r": [
     ["BK-01", "ความถี่ในการสำรองข้อมูลเป็นไปตาม RPO จาก BIA", "อย่างน้อยทุก 15 นาที (Log) และทุกวัน (เต็มหรือส่วนเพิ่ม)", "ทุกวัน"],
     ["BK-02", "กฎ 3-2-1: สำเนา 3 ชุด สื่อ 2 ประเภท นอกสถานที่ 1 ชุด", "บังคับ", "บังคับ"],
     ["BK-03", "มีสำเนาอย่างน้อย 1 ชุดที่แก้ไขไม่ได้ (Immutable) หรือแยกออฟไลน์ (Air-gapped)", "บังคับ", "แนะนำ"],
     ["BK-04", "เข้ารหัสข้อมูลสำรอง (AES-256)", "บังคับ", "บังคับ"],
     ["BK-05", "บัญชีผู้ดูแลระบบสำรองข้อมูลแยกจากโดเมนและใช้ MFA", "บังคับ", "บังคับ"],
     ["BK-06", "ระยะเวลาเก็บรักษา", "รายวัน 30 วัน รายเดือน 12 เดือน รายปีตามกฎหมาย", "รายวัน 14 วัน รายเดือน 6 เดือน"],
     ["BK-07", "การทดสอบกู้คืน", "สุ่มทดสอบทุกเดือน และกู้คืนทั้งระบบปีละครั้ง", "สุ่มทดสอบทุกไตรมาส"],
     ["BK-08", "การเฝ้าระวังงานสำรองข้อมูล", "แจ้งเตือนความล้มเหลวและแก้ไขภายใน 1 วันทำการ", "ภายใน 3 วันทำการ"]], "w": [1.5, 6.5, 4.8, 3.7]}),
 ],
 bp=[("Protect backup infrastructure as a Tier 0 asset; attackers target backups before encrypting.", "ปกป้องโครงสร้างพื้นฐานการสำรองข้อมูลในระดับ Tier 0 เพราะผู้โจมตีมุ่งทำลายข้อมูลสำรองก่อนเข้ารหัสระบบ"),
     ("Test restores of whole systems, including application start-up, not only file recovery.", "ทดสอบการกู้คืนทั้งระบบ รวมถึงการเริ่มใช้งานแอปพลิเคชัน ไม่ใช่เฉพาะการกู้คืนไฟล์"),
     ("Back up SaaS data (such as email) that the provider does not fully protect.", "สำรองข้อมูลใน SaaS (เช่น อีเมล) ที่ผู้ให้บริการไม่ได้ปกป้องอย่างครบถ้วน")],
 mistakes=[("Backups joined to the same domain as production, so ransomware encrypts both.", "ระบบสำรองข้อมูลอยู่ในโดเมนเดียวกับระบบใช้งานจริง ทำให้แรนซัมแวร์เข้ารหัสทั้งสองส่วน"),
           ("Backup success is measured by job status, never by restore tests.", "วัดความสำเร็จของการสำรองข้อมูลจากสถานะงาน โดยไม่เคยทดสอบการกู้คืน")],
 rev="Updated in February 2026 after IA-2025-04 to require monthly HIS restore tests and immutable copies for all critical systems.",
)

C["PR-PRC-005"] = dict(
 purpose=("This procedure describes how backups are configured, monitored, protected, and restored, including verification of backup integrity before restoration (PR.DS-11, RC.RP-03).",
          "ระเบียบปฏิบัตินี้อธิบายวิธีตั้งค่า เฝ้าระวัง ปกป้อง และกู้คืนข้อมูลสำรอง รวมถึงการตรวจสอบความถูกต้องของข้อมูลสำรองก่อนกู้คืน (PR.DS-11, RC.RP-03)"),
 sections=[
  ("Daily Operations", "การปฏิบัติงานประจำวัน", "Define daily checks and failure handling.", "กำหนดการตรวจสอบประจำวันและการจัดการเมื่อเกิดความล้มเหลว",
   ["Check backup job status every morning and log failures in the IT ticketing system.", "Rerun failed critical jobs the same day; escalate to [ITM] if a second failure occurs.", "Confirm the immutable copy and the off-site replication completed."],
   ["ตรวจสอบสถานะงานสำรองข้อมูลทุกเช้า และบันทึกความล้มเหลวในระบบจัดการงานของ IT", "รันงานสำรองข้อมูลระบบสำคัญที่ล้มเหลวใหม่ในวันเดียวกัน และยกระดับต่อ [ITM] หากล้มเหลวซ้ำ", "ยืนยันว่าสำเนาแบบแก้ไขไม่ได้และการทำสำเนานอกสถานที่เสร็จสมบูรณ์"]),
  ("Restore Steps", "ขั้นตอนการกู้คืน", "Describe restore steps, including integrity checks.", "อธิบายขั้นตอนการกู้คืน รวมถึงการตรวจสอบความถูกต้อง",
   {"n": ["Receive an approved restore request (incident, change, or test).", "Select the restore point; for security incidents, choose a point before the earliest indicator of compromise.",
          "Verify backup integrity (checksum, malware scan of restored data in an isolated environment) before restoring to production (RC.RP-03).", "Restore and validate application function with the system owner.",
          "Record the result in PR-REC-003."]},
   {"n": ["รับคำขอกู้คืนที่ได้รับอนุมัติ (จากเหตุการณ์ การเปลี่ยนแปลง หรือการทดสอบ)", "เลือกจุดกู้คืน กรณีเหตุการณ์ด้านความมั่นคงปลอดภัยให้เลือกจุดก่อนสัญญาณการถูกโจมตีแรกสุด",
          "ตรวจสอบความถูกต้องของข้อมูลสำรอง (Checksum และสแกนมัลแวร์ในสภาพแวดล้อมที่แยกไว้) ก่อนกู้คืนสู่ระบบใช้งานจริง (RC.RP-03)", "กู้คืนและตรวจสอบการทำงานของแอปพลิเคชันร่วมกับเจ้าของระบบ",
          "บันทึกผลใน PR-REC-003"]}),
 ],
 bp=[("Keep restore runbooks for each critical system (RC-PRC-001) and update them after every test.", "จัดทำคู่มือการกู้คืนสำหรับระบบสำคัญแต่ละระบบ (RC-PRC-001) และปรับปรุงหลังการทดสอบทุกครั้ง")],
 mistakes=[("Restoring infected backups directly into production during a ransomware incident.", "กู้คืนข้อมูลสำรองที่ติดมัลแวร์สู่ระบบใช้งานจริงโดยตรงระหว่างเหตุการณ์แรนซัมแวร์")],
)

C["PR-REC-003"] = dict(
 purpose=("This record documents each backup restore test, the result, time taken, and issues found, as evidence that backups work (PR.DS-11, RC.RP-03).",
          "บันทึกนี้ใช้บันทึกการทดสอบกู้คืนข้อมูลแต่ละครั้ง ผลลัพธ์ ระยะเวลาที่ใช้ และปัญหาที่พบ เป็นหลักฐานว่าการสำรองข้อมูลใช้งานได้จริง (PR.DS-11, RC.RP-03)"),
 fields=[
  ("Test ID", "รหัสการทดสอบ", "Unique reference.", "รหัสอ้างอิง", "RT-2026-001"),
  ("System", "ระบบ", "System restored.", "ระบบที่กู้คืน", ""),
  ("Restore point and copy used", "จุดกู้คืนและสำเนาที่ใช้", "Date and copy type (immutable, off-site).", "วันที่และประเภทสำเนา (Immutable นอกสถานที่)", ""),
  ("Scope", "ขอบเขต", "Files, database, full system.", "ไฟล์ ฐานข้อมูล ทั้งระบบ", ""),
  ("Time to restore vs RTO", "เวลาที่ใช้เทียบกับ RTO", "Actual and target.", "เวลาจริงและเป้าหมาย", ""),
  ("Data validated by", "ผู้ตรวจสอบข้อมูล", "System owner.", "เจ้าของระบบ", ""),
  ("Result", "ผลลัพธ์", "Pass or Fail.", "ผ่าน หรือ ไม่ผ่าน", ""),
  ("Issues and actions", "ปัญหาและการดำเนินการ", "Link to ID-REG-007 if needed.", "เชื่อมโยง ID-REG-007 หากจำเป็น", ""),
 ],
 rows=[
  ["RT-2026-07", "HIS database", "31/07/2026 02:00, immutable copy", "Database to isolated test server", "2 h 40 min vs RTO 4 h", "HIS application analyst", "Pass", "None"],
  ["RT-2026-08", "HIS database", "31/08/2026 02:00, off-site copy", "Database to isolated test server", "3 h 05 min vs RTO 4 h", "HIS application analyst", "Pass", "Off-site copy slower; bandwidth review"],
  ["RT-2026-Q2", "PACS (sample 500 studies)", "30/06/2026, immutable copy", "Image archive sample", "1 h 10 min vs RTO 8 h", "PACS administrator", "Pass", "None"],
  ["RT-2026-Q3", "LIS full system", "15/09/2026, immutable copy", "Full system at DR site", "6 h 20 min vs RTO 8 h", "LIS administrator", "Pass", "License server step missing from runbook; runbook updated"],
 ],
 bp=[("Record actual restore times to show whether RTOs are realistic.", "บันทึกเวลากู้คืนจริงเพื่อแสดงว่า RTO สามารถทำได้จริงหรือไม่")],
 mistakes=[("Testing only file-level restores of non-critical data.", "ทดสอบเฉพาะการกู้คืนระดับไฟล์ของข้อมูลที่ไม่สำคัญ")],
)

C["PR-STD-007"] = dict(
 purpose=("This standard sets retention periods for key record types and the methods for secure deletion when retention ends, consistent with PDPA s.37(3) and other legal retention duties.",
          "มาตรฐานนี้กำหนดระยะเวลาเก็บรักษาของบันทึกประเภทสำคัญ และวิธีการลบอย่างมั่นคงปลอดภัยเมื่อสิ้นสุดระยะเวลาเก็บรักษา ให้สอดคล้องกับ PDPA มาตรา 37(3) และหน้าที่การเก็บรักษาตามกฎหมายอื่น"),
 sections=[
  ("Retention Schedule", "ตารางระยะเวลาเก็บรักษา", "Set retention periods with legal basis for key record types.", "กำหนดระยะเวลาเก็บรักษาพร้อมฐานทางกฎหมายสำหรับบันทึกประเภทสำคัญ",
   {"t": ["Record type", "Retention", "Basis", "Owner"], "r": [
     ["Computer traffic data (service providers)", "At least 90 days", "Computer Crime Act B.E. 2550 s.26", "[ITM]"],
     ["Security event logs", "At least 1 year online; [2] years archive", "Common practice; incident investigation needs", "[CISO]"],
     ["Accounting documents", "[Per accounting and tax law] [VERIFY]", "Accounting Act B.E. 2543 [VERIFY]", "[CFO]"],
     ["Employee records", "[Period] after employment ends [VERIFY]", "Labor and tax law [VERIFY]", "[HR]"],
     ["CCTV footage", "30 days unless needed for an incident", "Data minimization (PDPA)", "[FAC]"],
     ["Customer personal data", "Per ROPA entry", "PDPA s.37(3)", "Data owner"]], "w": [4.5, 4.0, 5.0, 3.0]},
   {"t": ["ประเภทบันทึก", "ระยะเวลาเก็บรักษา", "ฐานทางกฎหมาย", "เจ้าของ"], "r": [
     ["ข้อมูลจราจรทางคอมพิวเตอร์ (ผู้ให้บริการ)", "อย่างน้อย 90 วัน", "พ.ร.บ.ว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. 2550 มาตรา 26", "[ITM]"],
     ["Log เหตุการณ์ด้านความมั่นคงปลอดภัย", "ออนไลน์อย่างน้อย 1 ปี และจัดเก็บถาวร [2] ปี", "แนวปฏิบัติทั่วไปและความจำเป็นในการสอบสวนเหตุการณ์", "[CISO]"],
     ["เอกสารทางบัญชี", "[ตามกฎหมายบัญชีและภาษี] [VERIFY]", "พ.ร.บ.การบัญชี พ.ศ. 2543 [VERIFY]", "[CFO]"],
     ["ข้อมูลพนักงาน", "[ระยะเวลา] หลังสิ้นสุดการจ้าง [VERIFY]", "กฎหมายแรงงานและภาษี [VERIFY]", "[HR]"],
     ["ภาพจากกล้องวงจรปิด", "30 วัน เว้นแต่จำเป็นต่อการสอบสวนเหตุการณ์", "หลักการเก็บข้อมูลเท่าที่จำเป็น (PDPA)", "[FAC]"],
     ["ข้อมูลส่วนบุคคลของลูกค้า", "ตามรายการใน ROPA", "PDPA มาตรา 37(3)", "เจ้าของข้อมูล"]], "w": [4.5, 4.0, 5.0, 3.0]},
   {"t": ["Record type", "Retention", "Basis", "Owner"], "r": [
     ["Patient and guest Wi-Fi traffic data", "90 days", "Computer Crime Act B.E. 2550 s.26", "IT Infrastructure Manager"],
     ["Security logs (SIEM)", "1 year online; 2 years archive", "CMC incident investigation needs", "Security Manager"],
     ["Medical records", "Per MOPH and HA requirements [VERIFY]", "Health regulations [VERIFY]", "Director of Medical Records"],
     ["HIS access audit logs", "2 years", "Privacy investigations; PDPC Security Measures Notification", "DPO"],
     ["CCTV footage", "30 days unless needed for an incident", "Data minimization", "Facilities and Engineering Manager"],
     ["Recruitment records of unsuccessful applicants", "1 year", "ROPA-HR-03", "HR Director"]], "w": [4.5, 4.0, 5.0, 3.0]}),
  ("Disposal Methods", "วิธีการทำลาย", "Define secure deletion and destruction methods.", "กำหนดวิธีการลบและทำลายอย่างมั่นคงปลอดภัย",
   ["Electronic records: delete through system functions with deletion logs; anonymize where analytics needs remain.", "Media: sanitize per NIST SP 800-88 and record in ID-FRM-001.", "Paper: cross-cut shred or certified destruction service."],
   ["บันทึกอิเล็กทรอนิกส์: ลบผ่านฟังก์ชันของระบบพร้อม Log การลบ และทำให้ไม่สามารถระบุตัวตนได้กรณียังต้องใช้เพื่อการวิเคราะห์", "สื่อบันทึกข้อมูล: ล้างข้อมูลตาม NIST SP 800-88 และบันทึกใน ID-FRM-001", "เอกสารกระดาษ: ย่อยแบบตัดขวางหรือใช้บริการทำลายที่ได้รับการรับรอง"]),
 ],
 bp=[("Have Legal Counsel confirm retention periods; they vary by sector and change over time.", "ให้ที่ปรึกษากฎหมายยืนยันระยะเวลาเก็บรักษา เพราะแตกต่างตามภาคส่วนและเปลี่ยนแปลงได้"),
     ("Automate deletion in systems where possible rather than relying on manual clean-up.", "ตั้งค่าการลบอัตโนมัติในระบบเมื่อทำได้ แทนการพึ่งพาการลบด้วยมือ")],
 mistakes=[("Keeping everything forever 'just in case', which increases breach impact and conflicts with the PDPA.", "เก็บทุกอย่างไว้ตลอดไปเผื่อจำเป็น ซึ่งเพิ่มผลกระทบเมื่อเกิดเหตุละเมิดและขัดกับ PDPA")],
)

C["PR-STD-008"] = dict(
 purpose=("This standard sets requirements for detecting and preventing unauthorized transfer of sensitive data through email, web, cloud, endpoints, and removable media.",
          "มาตรฐานนี้กำหนดข้อกำหนดในการตรวจจับและป้องกันการส่งข้อมูลอ่อนไหวออกโดยไม่ได้รับอนุญาตผ่านอีเมล เว็บ คลาวด์ อุปกรณ์ปลายทาง และสื่อบันทึกข้อมูลแบบถอดได้"),
 sections=[
  ("Requirements", "ข้อกำหนด", "Set DLP coverage and response requirements.", "กำหนดขอบเขตและการตอบสนองของ DLP",
   {"t": ["ID", "Requirement"], "r": [
     ["DLP-01", "Define detection rules for Restricted data types (for example, national ID numbers, bank accounts, health records)."],
     ["DLP-02", "Monitor outbound email, web uploads, cloud sharing, and removable media for Restricted data."],
     ["DLP-03", "Start in monitor mode for 30 to 60 days, tune false positives, then block or warn by channel."],
     ["DLP-04", "Route alerts to the [SOC] and data owners; investigate High alerts within 1 working day."],
     ["DLP-05", "Block uploads of Restricted data to unapproved cloud storage and public AI tools."],
     ["DLP-06", "Review DLP rules every six months."]], "w": [1.8, 14.7]},
   {"t": ["รหัส", "ข้อกำหนด"], "r": [
     ["DLP-01", "กำหนดกฎการตรวจจับสำหรับข้อมูลระดับ Restricted (เช่น เลขประจำตัวประชาชน เลขบัญชีธนาคาร ข้อมูลสุขภาพ)"],
     ["DLP-02", "เฝ้าระวังอีเมลขาออก การอัปโหลดเว็บ การแชร์บนคลาวด์ และสื่อบันทึกข้อมูลแบบถอดได้ สำหรับข้อมูลระดับ Restricted"],
     ["DLP-03", "เริ่มในโหมดเฝ้าระวัง 30 ถึง 60 วัน ปรับลดผลบวกลวง แล้วจึงบล็อกหรือเตือนตามช่องทาง"],
     ["DLP-04", "ส่งการแจ้งเตือนไปยัง [SOC] และเจ้าของข้อมูล และสอบสวนการแจ้งเตือนระดับสูงภายใน 1 วันทำการ"],
     ["DLP-05", "บล็อกการอัปโหลดข้อมูลระดับ Restricted ไปยังคลาวด์ที่ไม่ได้รับอนุมัติและเครื่องมือ AI สาธารณะ"],
     ["DLP-06", "ทบทวนกฎ DLP ทุก 6 เดือน"]], "w": [1.8, 14.7]}),
 ],
 cmc_note="CMC deferred the DLP project to 2027 after the April 2026 budget reduction (risk R-011). Until then, Microsoft 365 external sharing restrictions and sensitivity labels act as interim controls.",
 bp=[("Classify and label data first; DLP without classification produces noise.", "จัดชั้นและติดป้ายข้อมูลก่อน เพราะ DLP ที่ไม่มีการจัดชั้นข้อมูลจะสร้างการแจ้งเตือนจำนวนมากที่ไม่มีประโยชน์"),
     ("Coordinate with HR and the DPO on monitoring scope and employee notice.", "ประสานกับ HR และ DPO เรื่องขอบเขตการเฝ้าระวังและการแจ้งพนักงาน")],
 mistakes=[("Switching to block mode on day one, disrupting legitimate business.", "เปิดโหมดบล็อกตั้งแต่วันแรก ทำให้การดำเนินธุรกิจตามปกติหยุดชะงัก")],
)

C["PR-STD-009"] = dict(
 purpose=("This standard sets security requirements for organization-owned mobile devices and personal devices (bring your own device, BYOD) that access organization data.",
          "มาตรฐานนี้กำหนดข้อกำหนดด้านความมั่นคงปลอดภัยสำหรับอุปกรณ์เคลื่อนที่ขององค์กรและอุปกรณ์ส่วนตัว (BYOD) ที่เข้าถึงข้อมูลขององค์กร"),
 sections=[
  ("Requirements", "ข้อกำหนด", "Set requirements by device ownership.", "กำหนดข้อกำหนดตามความเป็นเจ้าของอุปกรณ์",
   {"t": ["Requirement", "Organization-owned", "Personal (BYOD)"], "r": [
     ["Enrollment", "Full device management (MDM)", "App protection policies (MAM) without full device control"],
     ["Screen lock", "PIN of 6 digits or biometric", "PIN of 6 digits or biometric"], ["Encryption", "Required", "Required (device default)"],
     ["Operating system", "Supported version; updates within 30 days", "Supported version"], ["Jailbroken or rooted devices", "Blocked", "Blocked"],
     ["Data in organization apps", "Managed", "Copy and paste to personal apps blocked; selective wipe"],
     ["Lost or stolen device", "Report within 24 hours; remote wipe", "Report within 24 hours; selective wipe of organization data"]], "w": [4.5, 5.5, 6.5]},
   {"t": ["ข้อกำหนด", "อุปกรณ์ขององค์กร", "อุปกรณ์ส่วนตัว (BYOD)"], "r": [
     ["การลงทะเบียน", "บริหารจัดการทั้งอุปกรณ์ (MDM)", "นโยบายปกป้องแอปพลิเคชัน (MAM) โดยไม่ควบคุมทั้งอุปกรณ์"],
     ["การล็อกหน้าจอ", "PIN 6 หลักหรือไบโอเมตริกซ์", "PIN 6 หลักหรือไบโอเมตริกซ์"], ["การเข้ารหัส", "บังคับ", "บังคับ (ค่าเริ่มต้นของอุปกรณ์)"],
     ["ระบบปฏิบัติการ", "รุ่นที่ยังได้รับการสนับสนุน และอัปเดตภายใน 30 วัน", "รุ่นที่ยังได้รับการสนับสนุน"], ["อุปกรณ์ที่ถูก Jailbreak หรือ Root", "บล็อก", "บล็อก"],
     ["ข้อมูลในแอปขององค์กร", "บริหารจัดการ", "บล็อกการคัดลอกไปยังแอปส่วนตัว และลบเฉพาะข้อมูลองค์กรได้"],
     ["อุปกรณ์สูญหายหรือถูกขโมย", "แจ้งภายใน 24 ชั่วโมง และลบข้อมูลจากระยะไกล", "แจ้งภายใน 24 ชั่วโมง และลบเฉพาะข้อมูลขององค์กร"]], "w": [4.5, 5.5, 6.5]}),
 ],
 bp=[("Use app-level protection for BYOD to respect personal privacy while protecting organization data.", "ใช้การปกป้องระดับแอปพลิเคชันสำหรับ BYOD เพื่อเคารพความเป็นส่วนตัวพร้อมปกป้องข้อมูลขององค์กร")],
 mistakes=[("Staff photograph records with personal phones because no approved option exists.", "บุคลากรถ่ายภาพข้อมูลด้วยโทรศัพท์ส่วนตัวเพราะไม่มีทางเลือกที่อนุมัติ")],
)
