# -*- coding: utf-8 -*-
# GV.RR Roles and Responsibilities; GV.OV Oversight
C = {}

C["GV-CHR-002"] = dict(
 purpose=("These terms of reference set the purpose, authority, membership, and working rules of the Information Security Steering Committee (ISSC), the management body that directs and oversees the security program.",
          "ขอบเขตอำนาจหน้าที่นี้กำหนดวัตถุประสงค์ อำนาจ องค์ประกอบ และวิธีการทำงานของคณะกรรมการกำกับดูแลความมั่นคงปลอดภัยสารสนเทศ (ISSC) ซึ่งเป็นองค์กรระดับผู้บริหารที่กำหนดทิศทางและกำกับแผนงานด้านความมั่นคงปลอดภัย"),
 sections=[
  ("Membership and Quorum", "องค์ประกอบและองค์ประชุม", "List members by role, the chair, the secretary, and the quorum.", "ระบุกรรมการตามบทบาท ประธาน เลขานุการ และองค์ประชุม",
   {"t": ["Role", "Position"], "r": [["Chair", "[CEO]"], ["Members", "[CIO], [CFO], [CRO], [DPO], [HR], heads of key business units"], ["Secretary", "[CISO]"], ["Invited as needed", "[IA] (observer), [LEGAL], vendors"], ["Quorum", "Chair or delegate plus at least half of members"]], "w": [4.0, 12.5]},
   {"t": ["บทบาท", "ตำแหน่ง"], "r": [["ประธาน", "[CEO]"], ["กรรมการ", "[CIO] [CFO] [CRO] [DPO] [HR] และหัวหน้าหน่วยธุรกิจหลัก"], ["เลขานุการ", "[CISO]"], ["ผู้เข้าร่วมตามความจำเป็น", "[IA] (ผู้สังเกตการณ์) [LEGAL] และผู้ให้บริการ"], ["องค์ประชุม", "ประธานหรือผู้แทน และกรรมการไม่น้อยกว่ากึ่งหนึ่ง"]], "w": [4.0, 12.5]},
   {"t": ["Role", "Position"], "r": [["Chair", "CEO"], ["Members", "CIO, CFO, Medical Director, Director of Nursing, Quality and Risk Management Director, DPO, HR Director"], ["Secretary", "Security Manager"], ["Invited as needed", "Internal Audit Manager (observer), Legal Counsel, MSSP service manager"], ["Quorum", "Chair or CIO as delegate plus at least four members"]], "w": [4.0, 12.5]}),
  ("Responsibilities and Decision Rights", "หน้าที่และอำนาจตัดสินใจ", "State what the committee decides, recommends, and monitors.", "ระบุเรื่องที่คณะกรรมการตัดสินใจ เสนอแนะ และติดตาม",
   ["Approve security standards (Tier 2) and endorse policies for [CEO] approval.", "Approve High and Critical exceptions and risk acceptances within its authority.",
    "Review the risk register, KRIs, program status, incidents, and audit findings each quarter.", "Prioritize security investment and recommend the budget.", "Conduct the annual management review (GV-PRC-006)."],
   ["อนุมัติมาตรฐานด้านความมั่นคงปลอดภัย (ชั้นที่ 2) และให้ความเห็นชอบนโยบายก่อนเสนอ [CEO] อนุมัติ", "อนุมัติข้อยกเว้นและการยอมรับความเสี่ยงระดับสูงและวิกฤตภายใต้อำนาจที่ได้รับ",
    "ทบทวนทะเบียนความเสี่ยง KRI สถานะแผนงาน เหตุการณ์ และข้อตรวจพบจากการตรวจสอบทุกไตรมาส", "จัดลำดับความสำคัญของการลงทุนด้านความมั่นคงปลอดภัยและเสนองบประมาณ", "ดำเนินการทบทวนโดยฝ่ายบริหารประจำปี (GV-PRC-006)"]),
  ("Meetings and Records", "การประชุมและบันทึก", "Define meeting frequency, papers, minutes, and action tracking.", "กำหนดความถี่ในการประชุม เอกสารประกอบ บันทึกการประชุม และการติดตามมติ",
   ["Meets quarterly and within 48 hours of a Critical incident.", "Papers are circulated five working days before the meeting.", "The secretary issues minutes within five working days and tracks actions to closure (GV-REC-001)."],
   ["ประชุมทุกไตรมาส และภายใน 48 ชั่วโมงเมื่อเกิดเหตุการณ์ระดับวิกฤต", "ส่งเอกสารประกอบการประชุมล่วงหน้า 5 วันทำการ", "เลขานุการออกบันทึกการประชุมภายใน 5 วันทำการ และติดตามมติจนแล้วเสร็จ (GV-REC-001)"]),
 ],
 bp=[("Chair the committee at CEO or deputy level so decisions carry business authority.", "ให้ CEO หรือรองเป็นประธาน เพื่อให้การตัดสินใจมีอำนาจทางธุรกิจ"),
     ("Run meetings on decisions, not status updates; every agenda item should state the decision needed.", "ใช้การประชุมเพื่อตัดสินใจ ไม่ใช่รายงานความคืบหน้า ทุกวาระควรระบุสิ่งที่ต้องการให้ตัดสิน"),
     ("Combine with the IT steering committee in smaller organizations to avoid meeting fatigue.", "รวมกับคณะกรรมการกำกับด้าน IT ในองค์กรขนาดเล็ก เพื่อลดภาระการประชุม")],
 mistakes=[("Members send junior delegates, so the committee cannot decide.", "กรรมการส่งผู้แทนระดับปฏิบัติการ ทำให้คณะกรรมการตัดสินใจไม่ได้")],
)

C["GV-REG-003"] = dict(
 purpose=("This matrix assigns who is Responsible, Accountable, Consulted, and Informed (RACI) for each cybersecurity activity, so that every activity has one accountable owner (GV.RR-02).",
          "ตารางนี้กำหนดผู้ปฏิบัติ (Responsible) ผู้รับผิดชอบสูงสุด (Accountable) ผู้ให้คำปรึกษา (Consulted) และผู้รับทราบ (Informed) ของกิจกรรมด้านความมั่นคงปลอดภัยแต่ละรายการ เพื่อให้ทุกกิจกรรมมีผู้รับผิดชอบสูงสุดเพียงคนเดียว (GV.RR-02)"),
 fields=[
  ("Activity", "กิจกรรม", "Security activity or process.", "กิจกรรมหรือกระบวนการด้านความมั่นคงปลอดภัย", ("Approve policy", "อนุมัตินโยบาย")),
  ("Board", "คณะกรรมการ", "R, A, C, or I.", "R A C หรือ I", "I"),
  ("CEO", "CEO", "R, A, C, or I.", "R A C หรือ I", "A"),
  ("ISSC", "ISSC", "R, A, C, or I.", "R A C หรือ I", "C"),
  ("CIO", "CIO", "R, A, C, or I.", "R A C หรือ I", "C"),
  ("CISO", "CISO", "R, A, C, or I.", "R A C หรือ I", "R"),
  ("DPO", "DPO", "R, A, C, or I.", "R A C หรือ I", "C"),
  ("IT Ops", "ฝ่ายปฏิบัติการ IT", "R, A, C, or I.", "R A C หรือ I", "I"),
  ("Business owners", "เจ้าของธุรกิจ", "R, A, C, or I.", "R A C หรือ I", "I"),
  ("Internal Audit", "ตรวจสอบภายใน", "R, A, C, or I.", "R A C หรือ I", "I"),
 ],
 rows=[
  ["Set risk appetite", "A", "R", "C", "C", "C", "I", "I", "C", "I"],
  ["Approve Information Security Policy", "I", "A", "C", "C", "R", "C", "I", "I", "I"],
  ["Maintain risk register", "I", "I", "C", "C", "A/R", "C", "C", "R", "I"],
  ["Accept High risk", "I", "I", "C", "A", "C", "I", "I", "R", "I"],
  ["Grant user access to HIS", "", "", "", "A", "C", "", "R", "R (approve)", "I"],
  ["Run vulnerability scans and patching", "", "", "", "A", "C", "", "R", "I", "I"],
  ["24x7 security monitoring (MSSP)", "", "", "", "I", "A", "", "C", "", "I"],
  ["Declare and manage major incident", "I", "A", "I", "R", "R", "C", "R", "C", "I"],
  ["Notify PDPC of breach", "I", "A", "I", "C", "C", "R", "", "C", "I"],
  ["Notify NCSA and regulator (CII)", "I", "A", "I", "C", "R", "C", "", "", "I"],
  ["Annual cybersecurity audit", "I", "I", "I", "C", "C", "C", "C", "C", "A/R"],
 ],
 cmc_note="CMC registered the CIO as the executive contact officer and the Security Manager as the operational contact officer with NCSA under CSA s.46 and s.52.",
 bp=[("Allow only one A per activity; two accountable owners means none.", "กำหนดผู้รับผิดชอบสูงสุด (A) เพียงหนึ่งรายต่อกิจกรรม การมี A สองรายเท่ากับไม่มีใครรับผิดชอบ"),
     ("Keep the matrix to 20 to 40 key activities; detailed task assignments belong in procedures.", "จำกัดตารางไว้ที่กิจกรรมสำคัญ 20 ถึง 40 รายการ ส่วนการมอบหมายงานโดยละเอียดให้อยู่ในระเบียบปฏิบัติ"),
     ("Include outsourced parties such as the MSSP as columns where they perform activities.", "เพิ่มคอลัมน์ผู้ให้บริการภายนอก เช่น MSSP เมื่อผู้ให้บริการปฏิบัติกิจกรรมนั้น")],
 mistakes=[("Making the CISO accountable for business risk decisions that belong to business owners.", "กำหนดให้ CISO รับผิดชอบสูงสุดในการตัดสินใจด้านความเสี่ยงทางธุรกิจที่ควรเป็นของเจ้าของธุรกิจ")],
)

C["GV-TPL-001"] = dict(
 purpose=("These templates define job descriptions for core cybersecurity roles, including purpose, responsibilities, competencies, and reporting lines, to support hiring and performance management.",
          "แม่แบบนี้กำหนดคำบรรยายลักษณะงานของบทบาทหลักด้านความมั่นคงปลอดภัยไซเบอร์ ได้แก่ วัตถุประสงค์ หน้าที่ สมรรถนะ และสายการบังคับบัญชา เพื่อสนับสนุนการสรรหาและการบริหารผลการปฏิบัติงาน"),
 sections=[
  ("Security Manager or CISO", "Security Manager หรือ CISO", "Define purpose, key responsibilities, competencies, and qualifications.", "กำหนดวัตถุประสงค์ หน้าที่หลัก สมรรถนะ และคุณสมบัติ",
   {"t": ["Element", "Content"], "r": [
     ["Purpose", "Lead the cybersecurity program to keep risk within appetite."],
     ["Reports to", "[CIO] with access to [CEO] and [AC]"],
     ["Key responsibilities", "Strategy and roadmap; policy framework; risk management; security operations oversight; incident response leadership; regulatory compliance; board reporting; budget and team management."],
     ["Competencies", "Risk management, governance, stakeholder management, technical breadth across infrastructure, cloud, and applications."],
     ["Qualifications", "Bachelor's degree; 8 or more years in security; CISSP or CISM preferred."]], "w": [4.0, 12.5]},
   {"t": ["องค์ประกอบ", "เนื้อหา"], "r": [
     ["วัตถุประสงค์", "นำแผนงานด้านความมั่นคงปลอดภัยไซเบอร์ เพื่อควบคุมความเสี่ยงให้อยู่ในระดับที่ยอมรับได้"],
     ["รายงานต่อ", "[CIO] และมีช่องทางรายงาน [CEO] และ [AC]"],
     ["หน้าที่หลัก", "ยุทธศาสตร์และแผนงาน กรอบนโยบาย การบริหารความเสี่ยง การกำกับงานปฏิบัติการ การนำการรับมือเหตุการณ์ การปฏิบัติตามกฎหมาย การรายงานคณะกรรมการ และการบริหารงบประมาณและทีม"],
     ["สมรรถนะ", "การบริหารความเสี่ยง การกำกับดูแล การบริหารผู้มีส่วนได้ส่วนเสีย และความรู้ทางเทคนิคด้านโครงสร้างพื้นฐาน คลาวด์ และแอปพลิเคชัน"],
     ["คุณสมบัติ", "ปริญญาตรี ประสบการณ์ด้านความมั่นคงปลอดภัย 8 ปีขึ้นไป มี CISSP หรือ CISM จะพิจารณาเป็นพิเศษ"]], "w": [4.0, 12.5]}),
  ("Security Engineer", "วิศวกรความมั่นคงปลอดภัย", "Define purpose, key responsibilities, competencies, and qualifications.", "กำหนดวัตถุประสงค์ หน้าที่หลัก สมรรถนะ และคุณสมบัติ",
   {"t": ["Element", "Content"], "r": [["Purpose", "Design, implement, and operate security controls."], ["Reports to", "[CISO]"], ["Key responsibilities", "Identity and access controls, endpoint and network security, vulnerability management, log onboarding, incident handling support."], ["Competencies", "Windows and Linux administration, networking, scripting, cloud security."], ["Qualifications", "3 or more years in IT or security; Security+, CySA+, or vendor certifications preferred."]], "w": [4.0, 12.5]},
   {"t": ["องค์ประกอบ", "เนื้อหา"], "r": [["วัตถุประสงค์", "ออกแบบ ติดตั้ง และดำเนินการมาตรการควบคุมด้านความมั่นคงปลอดภัย"], ["รายงานต่อ", "[CISO]"], ["หน้าที่หลัก", "การควบคุมตัวตนและการเข้าถึง ความมั่นคงปลอดภัยของอุปกรณ์ปลายทางและเครือข่าย การบริหารช่องโหว่ การเชื่อมต่อ Log และสนับสนุนการจัดการเหตุการณ์"], ["สมรรถนะ", "การดูแลระบบ Windows และ Linux เครือข่าย การเขียนสคริปต์ และความมั่นคงปลอดภัยบนคลาวด์"], ["คุณสมบัติ", "ประสบการณ์ด้าน IT หรือความมั่นคงปลอดภัย 3 ปีขึ้นไป มี Security+ CySA+ หรือใบรับรองจากผู้ผลิตจะพิจารณาเป็นพิเศษ"]], "w": [4.0, 12.5]}),
  ("GRC Analyst", "นักวิเคราะห์ด้านการกำกับดูแล ความเสี่ยง และการปฏิบัติตามกฎเกณฑ์ (GRC)", "Define purpose, key responsibilities, competencies, and qualifications.", "กำหนดวัตถุประสงค์ หน้าที่หลัก สมรรถนะ และคุณสมบัติ",
   {"t": ["Element", "Content"], "r": [["Purpose", "Maintain the policy, risk, and compliance framework."], ["Reports to", "[CISO]"], ["Key responsibilities", "Document control, risk register, exceptions, vendor assessments, audit coordination, metrics reporting."], ["Competencies", "Risk analysis, writing, ISO/IEC 27001, NIST CSF, PDPA."], ["Qualifications", "2 or more years in audit, risk, or compliance; ISO/IEC 27001 Lead Implementer preferred."]], "w": [4.0, 12.5]},
   {"t": ["องค์ประกอบ", "เนื้อหา"], "r": [["วัตถุประสงค์", "ดูแลกรอบนโยบาย ความเสี่ยง และการปฏิบัติตามกฎเกณฑ์"], ["รายงานต่อ", "[CISO]"], ["หน้าที่หลัก", "การควบคุมเอกสาร ทะเบียนความเสี่ยง ข้อยกเว้น การประเมินผู้ให้บริการ การประสานงานตรวจสอบ และการรายงานตัวชี้วัด"], ["สมรรถนะ", "การวิเคราะห์ความเสี่ยง การเขียน ISO/IEC 27001 NIST CSF และ PDPA"], ["คุณสมบัติ", "ประสบการณ์ด้านตรวจสอบ ความเสี่ยง หรือการปฏิบัติตามกฎเกณฑ์ 2 ปีขึ้นไป มี ISO/IEC 27001 Lead Implementer จะพิจารณาเป็นพิเศษ"]], "w": [4.0, 12.5]}),
 ],
 bp=[("Map roles to the NICE Workforce Framework (NIST SP 800-181 Rev. 1) to define skills consistently.", "เชื่อมโยงบทบาทกับ NICE Workforce Framework (NIST SP 800-181 Rev. 1) เพื่อกำหนดทักษะให้สอดคล้องกัน"),
     ("Include security responsibilities in non-security job descriptions, such as system administrators and developers.", "ระบุหน้าที่ด้านความมั่นคงปลอดภัยในคำบรรยายลักษณะงานของบทบาทอื่น เช่น ผู้ดูแลระบบและนักพัฒนา")],
 mistakes=[("Hiring a technical specialist into a management role without governance and stakeholder skills.", "จ้างผู้เชี่ยวชาญด้านเทคนิคมาอยู่ในบทบาทผู้บริหารโดยไม่มีทักษะด้านการกำกับดูแลและการบริหารผู้มีส่วนได้ส่วนเสีย")],
)

C["GV-PLN-001"] = dict(
 purpose=("This plan sets the annual cybersecurity budget and resources (people, services, and technology) needed to deliver the strategy, with justification linked to risk.",
          "แผนนี้กำหนดงบประมาณและทรัพยากรด้านความมั่นคงปลอดภัยไซเบอร์ประจำปี (บุคลากร บริการ และเทคโนโลยี) ที่จำเป็นต่อการดำเนินยุทธศาสตร์ พร้อมเหตุผลที่เชื่อมโยงกับความเสี่ยง"),
 sections=[
  ("Budget by Category", "งบประมาณแยกตามหมวด", "Show capital and operating budget by category and initiative.", "แสดงงบลงทุนและงบดำเนินการแยกตามหมวดและโครงการ",
   {"t": ["Category", "Initiative", "Capital (THB)", "Operating (THB)", "Risk addressed"], "r": [["People", "[Headcount, training]", "", "", ""], ["Services", "[MSSP, assessments, retainer]", "", "", ""], ["Technology", "[Tools and licenses]", "", "", ""], ["Total", "", "", "", ""]]},
   {"t": ["หมวด", "โครงการ", "งบลงทุน (บาท)", "งบดำเนินการ (บาท)", "ความเสี่ยงที่จัดการ"], "r": [["บุคลากร", "[อัตรากำลัง การอบรม]", "", "", ""], ["บริการ", "[MSSP การประเมิน สัญญาบริการรับมือเหตุ]", "", "", ""], ["เทคโนโลยี", "[เครื่องมือและสิทธิ์การใช้งาน]", "", "", ""], ["รวม", "", "", "", ""]]},
   {"t": ["Category", "Initiative", "Capital (THB)", "Operating (THB)", "Risk addressed"], "r": [
     ["People", "Two security engineers; training and certification", "0", "3,600,000", "R-001, R-004"],
     ["Services", "MSSP 24x7 monitoring; incident response retainer; annual CII risk assessment and audit", "0", "4,800,000", "R-001, R-005"],
     ["Technology", "Privileged access management; immutable backup expansion; MFA licenses", "5,200,000", "1,400,000", "R-001, R-002, R-003"],
     ["Total 2026 (after 15% reduction)", "", "5,200,000", "9,800,000", ""]]}),
  ("Resource Plan", "แผนทรัพยากร", "Show staffing and service providers needed, with in-house versus outsourced decisions.", "แสดงบุคลากรและผู้ให้บริการที่จำเป็น พร้อมการตัดสินใจทำเองหรือจ้างภายนอก",
   {"t": ["Function", "In-house", "Outsourced", "Rationale"], "r": [["Governance and risk", "[CISO], GRC analyst", "", "Requires business knowledge"], ["24x7 monitoring", "", "MSSP", "Cost of a 24x7 in-house team"], ["Engineering", "Security engineers", "", "Daily control operation"], ["Incident response", "Coordination", "Retainer", "Specialist skills needed rarely"]], "w": [4.0, 4.0, 3.5, 5.0]},
   {"t": ["ฟังก์ชัน", "ทำเอง", "จ้างภายนอก", "เหตุผล"], "r": [["การกำกับดูแลและความเสี่ยง", "[CISO] นักวิเคราะห์ GRC", "", "ต้องเข้าใจธุรกิจ"], ["การเฝ้าระวัง 24 ชั่วโมง", "", "MSSP", "ต้นทุนของทีมภายใน 24 ชั่วโมง"], ["งานวิศวกรรม", "วิศวกรความมั่นคงปลอดภัย", "", "ดำเนินการมาตรการควบคุมประจำวัน"], ["การรับมือเหตุการณ์", "การประสานงาน", "สัญญาบริการรับมือเหตุ", "ใช้ทักษะเฉพาะเป็นครั้งคราว"]], "w": [4.0, 4.0, 3.5, 5.0]}),
 ],
 bp=[("Tie every budget line to a risk in the register and a gap in the CSF profile.", "เชื่อมทุกรายการงบประมาณกับความเสี่ยงในทะเบียนและช่องว่างใน CSF Profile"),
     ("Present options (minimum, recommended, accelerated) with the risk each leaves open.", "นำเสนอทางเลือก (ขั้นต่ำ แนะนำ เร่งรัด) พร้อมความเสี่ยงที่ยังเหลือในแต่ละทางเลือก"),
     ("Plan for recurring operating costs, not only purchases.", "วางแผนค่าใช้จ่ายดำเนินการที่เกิดซ้ำ ไม่ใช่เฉพาะการจัดซื้อ")],
 mistakes=[("Buying tools without budget for people to operate them.", "ซื้อเครื่องมือโดยไม่มีงบประมาณสำหรับบุคลากรที่ดูแล")],
 rev="Updated in April 2026 after the 15% budget reduction; data loss prevention deferred to 2027 and MSSP scope kept unchanged.",
)

C["GV-STD-001"] = dict(
 purpose=("This standard sets the security requirements for the employment life cycle, from screening and onboarding to role changes, discipline, and termination (GV.RR-04).",
          "มาตรฐานนี้กำหนดข้อกำหนดด้านความมั่นคงปลอดภัยตลอดวงจรการจ้างงาน ตั้งแต่การตรวจสอบประวัติและการรับเข้าทำงาน จนถึงการเปลี่ยนตำแหน่ง การลงโทษทางวินัย และการพ้นสภาพ (GV.RR-04)"),
 sections=[
  ("Requirements", "ข้อกำหนด", "State measurable requirements for each employment stage.", "กำหนดข้อกำหนดที่วัดผลได้สำหรับแต่ละช่วงของการจ้างงาน",
   {"t": ["ID", "Stage", "Requirement"], "r": [
     ["HR-01", "Screening", "Verify identity, qualifications, and references before hiring. Perform criminal record checks for privileged and sensitive roles, with consent and in line with the PDPA."],
     ["HR-02", "Terms", "Employment contracts include confidentiality and security obligations that continue after termination (ISO/IEC 27001:2022 Annex A 6.2 and 6.6)."],
     ["HR-03", "Onboarding", "New staff complete security awareness training and acknowledge the Acceptable Use Policy before receiving system access."],
     ["HR-04", "Role change", "HR notifies IT of transfers within 1 working day; old access is removed within 5 working days."],
     ["HR-05", "Termination", "HR notifies IT before or on the last day; accounts are disabled on the last working day, or immediately for involuntary termination."],
     ["HR-06", "Discipline", "A formal disciplinary process covers security violations (Annex A 6.4)."],
     ["HR-07", "Third-party staff", "Contractors and vendor staff follow the same requirements through contract terms."]], "w": [1.6, 2.8, 12.1]},
   {"t": ["รหัส", "ช่วง", "ข้อกำหนด"], "r": [
     ["HR-01", "การตรวจสอบประวัติ", "ตรวจสอบตัวตน คุณวุฒิ และบุคคลอ้างอิงก่อนจ้าง ตรวจสอบประวัติอาชญากรรมสำหรับตำแหน่งที่มีสิทธิ์ระดับสูงหรือตำแหน่งอ่อนไหว โดยได้รับความยินยอมและสอดคล้องกับ PDPA"],
     ["HR-02", "เงื่อนไขการจ้าง", "สัญญาจ้างระบุหน้าที่รักษาความลับและความมั่นคงปลอดภัยที่มีผลต่อเนื่องหลังพ้นสภาพ (ISO/IEC 27001:2022 Annex A 6.2 และ 6.6)"],
     ["HR-03", "การรับเข้าทำงาน", "พนักงานใหม่ต้องผ่านการอบรมความตระหนักรู้และลงนามรับทราบนโยบายการใช้งานที่ยอมรับได้ก่อนได้รับสิทธิ์เข้าระบบ"],
     ["HR-04", "การเปลี่ยนตำแหน่ง", "ฝ่ายทรัพยากรบุคคลแจ้งฝ่าย IT ภายใน 1 วันทำการ และถอนสิทธิ์เดิมภายใน 5 วันทำการ"],
     ["HR-05", "การพ้นสภาพ", "ฝ่ายทรัพยากรบุคคลแจ้งฝ่าย IT ก่อนหรือในวันทำงานสุดท้าย ปิดบัญชีในวันทำงานสุดท้าย หรือทันทีกรณีเลิกจ้าง"],
     ["HR-06", "การลงโทษทางวินัย", "มีกระบวนการทางวินัยที่ครอบคลุมการฝ่าฝืนด้านความมั่นคงปลอดภัย (Annex A 6.4)"],
     ["HR-07", "บุคลากรภายนอก", "ผู้รับจ้างและพนักงานของผู้ให้บริการต้องปฏิบัติตามข้อกำหนดเดียวกันผ่านเงื่อนไขในสัญญา"]], "w": [1.6, 2.8, 12.1]},
   {"t": ["ID", "Stage", "CMC requirement"], "r": [
     ["HR-01", "Screening", "Verify professional licenses for physicians, nurses, and pharmacists with the relevant councils; criminal record checks for IT administrators and finance staff."],
     ["HR-02", "Terms", "Contracts include patient confidentiality obligations consistent with professional ethics and PDPA."],
     ["HR-03", "Onboarding", "Clinical staff complete the 30-minute security and privacy module before HIS access."],
     ["HR-04", "Role change", "HR updates the HR system; the HIS role changes automatically through the identity integration (2026)."],
     ["HR-05", "Termination", "Accounts disabled on the last working day; resident physicians on rotation are disabled on rotation end date."],
     ["HR-06", "Discipline", "Security violations follow the CMC disciplinary regulation."],
     ["HR-07", "Third-party staff", "Outsourced nurses, cleaners, and vendor engineers sign GV-FRM-002."]], "w": [1.6, 2.8, 12.1]}),
 ],
 bp=[("Automate joiner, mover, and leaver events from the HR system to identity systems.", "เชื่อมต่อเหตุการณ์การเข้า ย้าย และออกจากระบบ HR ไปยังระบบบริหารตัวตนโดยอัตโนมัติ"),
     ("Reconcile HR leavers against active accounts every month.", "กระทบยอดรายชื่อพนักงานที่พ้นสภาพกับบัญชีที่ยังใช้งานทุกเดือน"),
     ("Obtain consent and limit background checks to what the role requires, consistent with the PDPA.", "ขอความยินยอมและจำกัดการตรวจสอบประวัติเท่าที่บทบาทนั้นจำเป็น ให้สอดคล้องกับ PDPA")],
 mistakes=[("Leavers keep access for weeks because HR and IT do not share a trigger.", "พนักงานที่พ้นสภาพยังมีสิทธิ์อยู่หลายสัปดาห์เพราะฝ่าย HR และ IT ไม่มีกลไกแจ้งร่วมกัน")],
)

C["GV-FRM-002"] = dict(
 purpose=("This agreement binds employees, contractors, and third parties to protect confidential information they access, during and after their engagement.",
          "สัญญานี้ผูกพันพนักงาน ผู้รับจ้าง และบุคคลภายนอกให้ปกป้องข้อมูลลับที่เข้าถึง ทั้งระหว่างและหลังสิ้นสุดการปฏิบัติงาน"),
 sections=[
  ("Key Clauses", "ข้อสัญญาหลัก", "Include the minimum clauses of a confidentiality agreement (ISO/IEC 27001:2022 Annex A 6.6).", "ระบุข้อสัญญาขั้นต่ำของสัญญาการรักษาความลับ (ISO/IEC 27001:2022 Annex A 6.6)",
   {"n": ["Definition of confidential information, including personal data.", "Obligation to use information only for the stated purpose.", "Obligation not to disclose without written authorization.",
          "Duty to report any actual or suspected disclosure immediately.", "Return or destruction of information at the end of the engagement.", "Duration: obligations continue for [X] years after termination, and indefinitely for personal data and trade secrets.",
          "Remedies and governing law (laws of Thailand)."]},
   {"n": ["คำนิยามของข้อมูลลับ รวมถึงข้อมูลส่วนบุคคล", "หน้าที่ใช้ข้อมูลเฉพาะตามวัตถุประสงค์ที่กำหนด", "หน้าที่ไม่เปิดเผยข้อมูลโดยไม่ได้รับอนุญาตเป็นลายลักษณ์อักษร",
          "หน้าที่แจ้งการเปิดเผยที่เกิดขึ้นหรือที่สงสัยทันที", "การส่งคืนหรือทำลายข้อมูลเมื่อสิ้นสุดการปฏิบัติงาน", "ระยะเวลา: หน้าที่มีผลต่อเนื่อง [X] ปีหลังสิ้นสุดสัญญา และไม่มีกำหนดสำหรับข้อมูลส่วนบุคคลและความลับทางการค้า",
          "การเยียวยาและกฎหมายที่ใช้บังคับ (กฎหมายไทย)"]},
   {"n": ["Confidential information includes patient records, images, results, and any data in HIS, PACS, and LIS.", "Use information only for patient care or assigned duties.", "Do not disclose without written authorization or a legal duty.",
          "Report any suspected disclosure to the DPO or Security Manager immediately.", "Return badges, devices, and documents at the end of the engagement.", "Obligations continue for five years after termination, and indefinitely for patient data.", "Governed by the laws of Thailand."]}),
 ],
 fields=[
  ("Signatory name", "ชื่อผู้ลงนาม", "Full name.", "ชื่อ-นามสกุล", ""),
  ("Organization or department", "หน่วยงานหรือบริษัท", "Employer or vendor.", "หน่วยงานต้นสังกัดหรือบริษัทผู้ให้บริการ", ""),
  ("Engagement or role", "งานหรือบทบาท", "Purpose of access.", "วัตถุประสงค์ของการเข้าถึง", ""),
  ("Start date", "วันที่เริ่มต้น", "Effective date.", "วันที่มีผล", ""),
 ],
 cmc_vals=["Vendor engineer (name withheld in sample)", "PACS Vendor B", "On-site PACS upgrade support", "3 August 2026"],
 approvals=["Requester", "LEGAL"],
 bp=[("Collect signatures before access is granted and store them centrally.", "เก็บลายมือชื่อก่อนให้สิทธิ์เข้าถึง และจัดเก็บไว้ที่ส่วนกลาง"),
     ("Use a shorter version for visitors and a full version for staff and vendors.", "ใช้ฉบับย่อสำหรับผู้มาติดต่อ และฉบับเต็มสำหรับพนักงานและผู้ให้บริการ")],
 mistakes=[("Vendors' engineers work on site without any signed agreement because the company contract is assumed to cover them.", "วิศวกรของผู้ให้บริการปฏิบัติงานในสถานที่โดยไม่ได้ลงนามสัญญา เพราะเข้าใจว่าสัญญาบริษัทครอบคลุมแล้ว")],
)

C["GV-FRM-003"] = dict(
 purpose=("This checklist ensures that all access, assets, and information are recovered when an employee or contractor leaves or changes role.",
          "แบบตรวจสอบนี้ทำให้การถอนสิทธิ์ การคืนทรัพย์สิน และการคืนข้อมูลครบถ้วนเมื่อพนักงานหรือผู้รับจ้างพ้นสภาพหรือเปลี่ยนตำแหน่ง"),
 fields=[
  ("Employee name and ID", "ชื่อและรหัสพนักงาน", "Person leaving or moving.", "ผู้พ้นสภาพหรือย้ายตำแหน่ง", ""),
  ("Event type and last working day", "ประเภทเหตุการณ์และวันทำงานสุดท้าย", "Resignation, termination, transfer, contract end.", "ลาออก เลิกจ้าง ย้าย สิ้นสุดสัญญา", ""),
  ("Directory and email account disabled", "ปิดบัญชีไดเรกทอรีและอีเมล", "Date, time, and by whom.", "วัน เวลา และผู้ดำเนินการ", ""),
  ("Business application access removed", "ถอนสิทธิ์ระบบงาน", "List each system.", "ระบุทุกระบบ", ""),
  ("Privileged and shared accounts reset", "รีเซ็ตบัญชีสิทธิ์ระดับสูงและบัญชีใช้ร่วม", "Passwords changed where the person knew them.", "เปลี่ยนรหัสผ่านที่บุคคลนั้นทราบ", ""),
  ("Remote access and MFA tokens revoked", "ยกเลิกการเข้าถึงระยะไกลและอุปกรณ์ MFA", "VPN, MFA app registrations.", "VPN และการลงทะเบียนแอป MFA", ""),
  ("Assets returned", "คืนทรัพย์สิน", "Laptop, phone, badge, keys, tokens with asset IDs.", "โน้ตบุ๊ก โทรศัพท์ บัตร กุญแจ อุปกรณ์ยืนยันตัวตน พร้อมรหัสทรัพย์สิน", ""),
  ("Data handover", "ส่งมอบข้อมูล", "Files and mailbox transferred to manager.", "ส่งมอบไฟล์และกล่องจดหมายให้ผู้บังคับบัญชา", ""),
  ("Exit reminder of confidentiality", "แจ้งเตือนหน้าที่รักษาความลับเมื่อออก", "Signed acknowledgment.", "ลงนามรับทราบ", ""),
 ],
 cmc_vals=["Staff nurse, Ward 5A (ID withheld in sample)", "Resignation; last working day 30 June 2026", "Disabled 30 June 2026, 17:05, by IT Service Desk",
           "HIS, LIS viewer, Microsoft 365, nurse call console removed 30 June 2026", "Not applicable (no privileged access)", "No VPN; Microsoft Authenticator registration removed",
           "Badge B-10422 returned; locker key returned", "Shift handover files moved to Ward 5A shared folder", "Signed 30 June 2026"],
 approvals=["Line Manager", "ITM", "HR"],
 bp=[("Trigger the checklist automatically from the HR system and close it within one working day.", "ให้ระบบ HR เริ่มแบบตรวจสอบโดยอัตโนมัติ และปิดให้เสร็จภายใน 1 วันทำการ")],
 mistakes=[("Forgetting local application accounts that are not linked to the directory, such as medical device consoles.", "ลืมบัญชีในแอปพลิเคชันที่ไม่ได้เชื่อมกับไดเรกทอรี เช่น คอนโซลของอุปกรณ์การแพทย์")],
)

C["GV-PRC-006"] = dict(
 purpose=("This procedure defines how top management reviews the security program at planned intervals to confirm it remains suitable, adequate, and effective (ISO/IEC 27001:2022 Clause 9.3).",
          "ระเบียบปฏิบัตินี้กำหนดวิธีที่ผู้บริหารระดับสูงทบทวนแผนงานด้านความมั่นคงปลอดภัยตามรอบที่กำหนด เพื่อยืนยันว่ายังเหมาะสม เพียงพอ และมีประสิทธิผล (ISO/IEC 27001:2022 ข้อ 9.3)"),
 sections=[
  ("Review Inputs", "ข้อมูลนำเข้าในการทบทวน", "List mandatory inputs (ISO/IEC 27001:2022 Clause 9.3.2).", "ระบุข้อมูลนำเข้าที่บังคับ (ISO/IEC 27001:2022 ข้อ 9.3.2)",
   {"n": ["Status of actions from previous reviews.", "Changes in external and internal issues and interested party needs.", "Feedback on security performance: nonconformities and corrective actions, monitoring and measurement results, audit results, and fulfillment of objectives.",
          "Feedback from interested parties.", "Results of risk assessment and status of the risk treatment plan.", "Opportunities for continual improvement."]},
   {"n": ["สถานะการดำเนินการตามมติการทบทวนครั้งก่อน", "การเปลี่ยนแปลงของประเด็นภายนอกและภายใน และความต้องการของผู้มีส่วนได้ส่วนเสีย", "ผลการดำเนินงานด้านความมั่นคงปลอดภัย ได้แก่ ข้อบกพร่องและการแก้ไข ผลการติดตามและวัดผล ผลการตรวจสอบ และการบรรลุวัตถุประสงค์",
          "ข้อเสนอแนะจากผู้มีส่วนได้ส่วนเสีย", "ผลการประเมินความเสี่ยงและสถานะของแผนการจัดการความเสี่ยง", "โอกาสในการปรับปรุงอย่างต่อเนื่อง"]}),
  ("Review Outputs", "ผลลัพธ์จากการทบทวน", "State the decisions the review must produce (Clause 9.3.3).", "ระบุการตัดสินใจที่การทบทวนต้องให้ผล (ข้อ 9.3.3)",
   ["Decisions on continual improvement opportunities.", "Any need for changes to the ISMS, including resources and objectives.", "Actions with owners and due dates, recorded in the minutes (GV-REC-001) and the Corrective Action and Improvement Register (ID-REG-007)."],
   ["การตัดสินใจเกี่ยวกับโอกาสในการปรับปรุงอย่างต่อเนื่อง", "ความจำเป็นในการเปลี่ยนแปลง ISMS รวมถึงทรัพยากรและวัตถุประสงค์", "การดำเนินการพร้อมผู้รับผิดชอบและกำหนดเวลา บันทึกในบันทึกการประชุม (GV-REC-001) และทะเบียนการแก้ไขข้อบกพร่องและการปรับปรุง (ID-REG-007)"]),
  ("Schedule", "กำหนดการ", "Define when the review takes place.", "กำหนดช่วงเวลาการทบทวน",
   "The [ISSC] conducts a full management review at least once a year, before the annual budget cycle, and after any major incident or significant change.",
   "[ISSC] ดำเนินการทบทวนโดยฝ่ายบริหารอย่างครบถ้วนอย่างน้อยปีละครั้ง ก่อนรอบงบประมาณประจำปี และหลังเหตุการณ์ร้ายแรงหรือการเปลี่ยนแปลงสำคัญ"),
 ],
 bp=[("Hold the review before budget planning so decisions can be funded.", "จัดการทบทวนก่อนการวางแผนงบประมาณ เพื่อให้การตัดสินใจได้รับงบประมาณ"),
     ("Use a standard agenda that mirrors Clause 9.3.2 so auditors can trace every input.", "ใช้วาระมาตรฐานที่สอดคล้องกับข้อ 9.3.2 เพื่อให้ผู้ตรวจสอบตรวจย้อนข้อมูลนำเข้าทุกรายการได้")],
 mistakes=[("Holding the review as a slide presentation with no recorded decisions.", "จัดการทบทวนเป็นการนำเสนอสไลด์โดยไม่มีการบันทึกการตัดสินใจ")],
)

C["GV-REC-001"] = dict(
 purpose=("These minutes record the inputs, discussion, decisions, and actions of each management review, as evidence required by ISO/IEC 27001:2022 Clause 9.3.3.",
          "บันทึกการประชุมนี้บันทึกข้อมูลนำเข้า การอภิปราย การตัดสินใจ และการดำเนินการของการทบทวนโดยฝ่ายบริหารแต่ละครั้ง เป็นหลักฐานที่ ISO/IEC 27001:2022 ข้อ 9.3.3 กำหนด"),
 sections=[
  ("Meeting Details", "รายละเอียดการประชุม", "Record date, attendees, quorum, and agenda.", "บันทึกวันที่ ผู้เข้าร่วม องค์ประชุม และวาระ",
   {"t": ["Item", "Detail"], "r": [["Meeting", "[ISSC] Management Review [No.]"], ["Date and place", "[Date], [Place]"], ["Chair", "[CEO]"], ["Attendees", "[Names and roles]"], ["Quorum met", "[Yes or No]"]], "w": [4.5, 12.0]},
   {"t": ["หัวข้อ", "รายละเอียด"], "r": [["การประชุม", "การทบทวนโดยฝ่ายบริหารของ [ISSC] ครั้งที่ [เลขที่]"], ["วันที่และสถานที่", "[วันที่] [สถานที่]"], ["ประธาน", "[CEO]"], ["ผู้เข้าร่วม", "[ชื่อและบทบาท]"], ["ครบองค์ประชุม", "[ครบ หรือ ไม่ครบ]"]], "w": [4.5, 12.0]},
   {"t": ["Item", "Detail"], "r": [["Meeting", "ISSC Management Review MR-2026-01"], ["Date and place", "22 January 2026, CMC Riverside Board Room"], ["Chair", "CEO"], ["Attendees", "CIO, CFO, Medical Director, Director of Nursing, Quality and Risk Management Director, DPO, HR Director, Security Manager (secretary); Internal Audit Manager (observer)"], ["Quorum met", "Yes"]], "w": [4.5, 12.0]}),
  ("Inputs Reviewed and Decisions", "ข้อมูลนำเข้าที่ทบทวนและมติ", "Record each mandatory input, the key points, and the decision.", "บันทึกข้อมูลนำเข้าที่บังคับแต่ละรายการ ประเด็นสำคัญ และมติ",
   {"t": ["Input (Clause 9.3.2)", "Key points", "Decision"], "r": [["Previous actions", "", ""], ["Changes in context", "", ""], ["Performance and audit results", "", ""], ["Risk assessment and treatment", "", ""], ["Improvement opportunities", "", ""]]},
   {"t": ["ข้อมูลนำเข้า (ข้อ 9.3.2)", "ประเด็นสำคัญ", "มติ"], "r": [["มติครั้งก่อน", "", ""], ["การเปลี่ยนแปลงบริบท", "", ""], ["ผลการดำเนินงานและการตรวจสอบ", "", ""], ["การประเมินและจัดการความเสี่ยง", "", ""], ["โอกาสในการปรับปรุง", "", ""]]},
   {"t": ["Input (Clause 9.3.2)", "Key points", "Decision"], "r": [
     ["Previous actions", "9 of 11 actions from 2025 closed", "Carry forward 2 actions (PAM rollout, vendor tiering)"],
     ["Changes in context", "CRC Notification 2024 deadlines; HA re-survey 2027", "Add CII matrix (GV-REG-006) to the document pack"],
     ["Performance and audit results", "IA-2025-04: 7 findings (2 High: stale HIS accounts, untested restores)", "Approve corrective actions; restore tests monthly for HIS"],
     ["Risk assessment and treatment", "Top risk R-001 ransomware remains High (score 12) after backup improvements", "Fund MSSP from March 2026"],
     ["Improvement opportunities", "Badge tap login requested by physicians", "Pilot on two wards in Q2 2026"]]}),
  ("Action Log", "บันทึกการดำเนินการ", "Record actions with owners and due dates.", "บันทึกการดำเนินการพร้อมผู้รับผิดชอบและกำหนดเวลา",
   {"t": ["Action ID", "Action", "Owner", "Due date", "Status"], "r": [["[ID]", "", "", "", ""]]},
   {"t": ["รหัส", "การดำเนินการ", "ผู้รับผิดชอบ", "กำหนดเสร็จ", "สถานะ"], "r": [["[รหัส]", "", "", "", ""]]},
   {"t": ["Action ID", "Action", "Owner", "Due date", "Status"], "r": [
     ["MR26-01", "Complete privileged access management for HIS and domain administrators", "IT Infrastructure Manager", "30 June 2026", "Closed"],
     ["MR26-02", "Onboard MSSP for 24x7 monitoring", "Security Manager", "31 March 2026", "Closed"],
     ["MR26-03", "Run monthly HIS restore tests", "IT Infrastructure Manager", "Monthly from February 2026", "On track"],
     ["MR26-04", "Pilot badge tap login on Wards 5A and 6B", "CIO", "30 June 2026", "Closed"]]}),
 ],
 bp=[("Circulate minutes within five working days and track actions in the corrective action register.", "ส่งบันทึกการประชุมภายใน 5 วันทำการ และติดตามการดำเนินการในทะเบียนการแก้ไขข้อบกพร่อง")],
 mistakes=[("Minutes record attendance but not decisions, so auditors cannot see management direction.", "บันทึกการประชุมระบุเพียงผู้เข้าร่วมแต่ไม่บันทึกมติ ทำให้ผู้ตรวจสอบไม่เห็นทิศทางของผู้บริหาร")],
)

C["GV-REG-008"] = dict(
 purpose=("This catalog defines the key performance indicators (KPIs) and key risk indicators (KRIs) used to measure the security program, including formula, source, target, and owner (ISO/IEC 27001:2022 Clause 9.1).",
          "บัญชีนี้กำหนดตัวชี้วัดผลการดำเนินงาน (KPI) และตัวชี้วัดความเสี่ยง (KRI) ที่ใช้วัดผลแผนงานด้านความมั่นคงปลอดภัย พร้อมสูตรคำนวณ แหล่งข้อมูล เป้าหมาย และผู้รับผิดชอบ (ISO/IEC 27001:2022 ข้อ 9.1)"),
 fields=[
  ("Metric ID", "รหัสตัวชี้วัด", "Unique reference.", "รหัสอ้างอิง", "KPI-01"),
  ("Type", "ประเภท", "KPI or KRI.", "KPI หรือ KRI", "KPI"),
  ("Metric", "ตัวชี้วัด", "Name and formula.", "ชื่อและสูตรคำนวณ", ("Patch compliance = patched / in scope", "อัตราการติดตั้งแพตช์ = เครื่องที่ติดตั้งแล้ว / เครื่องทั้งหมดในขอบเขต")),
  ("CSF link", "การเชื่อมโยงกับ CSF", "Related category.", "Category ที่เกี่ยวข้อง", "PR.PS"),
  ("Data source", "แหล่งข้อมูล", "System or record.", "ระบบหรือบันทึก", ""),
  ("Target or threshold", "เป้าหมายหรือเกณฑ์", "Target value or tolerance.", "ค่าเป้าหมายหรือค่าเบี่ยงเบนที่ยอมรับได้", "95%"),
  ("Frequency", "ความถี่", "Collection and reporting.", "การเก็บและรายงาน", ("Monthly", "รายเดือน")),
  ("Owner", "ผู้รับผิดชอบ", "Role.", "บทบาท", ""),
  ("Current value", "ค่าปัจจุบัน", "Latest measurement.", "ค่าล่าสุด", ""),
 ],
 rows=[
  ["KPI-01", "KPI", "Critical patches applied within SLA / total critical patches", "PR.PS-02", "Endpoint management and vulnerability scanner", "95%", "Monthly", "IT Infrastructure Manager", "88% (Sep 2026)"],
  ["KPI-02", "KPI", "Privileged and remote access with MFA / total", "PR.AA-03", "Identity platform", "100%", "Monthly", "Security Manager", "92%"],
  ["KPI-03", "KPI", "Staff completing annual awareness training / total staff", "PR.AT-01", "Learning system", "95%", "Quarterly", "Security Manager", "91%"],
  ["KPI-04", "KPI", "Critical log sources monitored / total critical sources", "DE.CM-01", "DE-REG-001", "95%", "Monthly", "SOC Lead", "81%"],
  ["KPI-05", "KPI", "Successful restore tests / scheduled restore tests", "PR.DS-11", "PR-REC-003", "100%", "Monthly", "IT Infrastructure Manager", "100%"],
  ["KRI-01", "KRI", "Internet-facing critical vulnerabilities older than 7 days", "ID.RA-01", "Vulnerability scanner", "0", "Weekly", "Security Manager", "0"],
  ["KRI-02", "KRI", "Open High or Critical risks without approved treatment older than 30 days", "ID.RA-06", "ID-REG-005", "0", "Quarterly", "Security Manager", "1"],
  ["KRI-03", "KRI", "Expired policy exceptions", "ID.RA-07", "GV-REG-004", "0", "Monthly", "Security Manager", "0"],
  ["KRI-04", "KRI", "Phishing simulation click rate", "PR.AT-01", "Phishing platform", "Below 10%", "Quarterly", "Security Manager", "12%"],
 ],
 bp=[("Measure fewer things well: 8 to 15 metrics that drive decisions are better than 50 that nobody reads.", "วัดผลน้อยแต่มีคุณภาพ ตัวชี้วัด 8 ถึง 15 ตัวที่ใช้ตัดสินใจได้ดีกว่า 50 ตัวที่ไม่มีใครอ่าน"),
     ("Link every KRI to a risk appetite tolerance (GV-STM-001).", "เชื่อมโยง KRI ทุกตัวกับเกณฑ์ค่าเบี่ยงเบนที่ยอมรับได้ (GV-STM-001)"),
     ("Automate collection from source systems to avoid manual manipulation.", "เก็บข้อมูลจากระบบต้นทางโดยอัตโนมัติ เพื่อหลีกเลี่ยงการปรับแต่งด้วยมือ")],
 mistakes=[("Reporting activity counts (number of alerts) that do not show risk or performance.", "รายงานจำนวนกิจกรรม (เช่น จำนวนการแจ้งเตือน) ซึ่งไม่ได้แสดงความเสี่ยงหรือผลการดำเนินงาน")],
)

C["GV-TPL-005"] = dict(
 purpose=("This template gives the Board a concise, decision-focused view of cyber risk, program progress, incidents, and requests for support.",
          "แม่แบบนี้ช่วยให้คณะกรรมการเห็นภาพความเสี่ยงด้านไซเบอร์ ความคืบหน้าของแผนงาน เหตุการณ์ และเรื่องที่ต้องการการสนับสนุน อย่างกระชับและเน้นการตัดสินใจ"),
 sections=[
  ("Report Structure", "โครงสร้างรายงาน", "Use a top-down structure: key message first, then evidence (Pyramid Principle).", "ใช้โครงสร้างจากบนลงล่าง โดยเริ่มจากข้อความสำคัญก่อน แล้วตามด้วยหลักฐาน (Pyramid Principle)",
   {"t": ["Page", "Key message", "Content"], "r": [
     ["1. Summary", "Overall cyber risk is [within or above] appetite", "Three to five headline messages and decisions requested"],
     ["2. Top risks", "Top five risks and trend", "Risk heat map; change since last report"],
     ["3. Program progress", "Roadmap is [on track or delayed]", "Milestones, budget used, CSF profile progress"],
     ["4. Incidents and compliance", "Significant incidents and regulatory status", "Incidents, notifications, audit findings overdue"],
     ["5. Decisions requested", "What the Board must decide", "Options, cost, and residual risk"]], "w": [3.5, 5.5, 7.5]},
   {"t": ["หน้า", "ข้อความสำคัญ", "เนื้อหา"], "r": [
     ["1. สรุป", "ความเสี่ยงด้านไซเบอร์โดยรวม [อยู่ภายใน หรือ เกิน] ระดับที่ยอมรับได้", "ข้อความหลัก 3 ถึง 5 ข้อ และเรื่องที่ขอให้ตัดสินใจ"],
     ["2. ความเสี่ยงสำคัญ", "ความเสี่ยงสำคัญ 5 อันดับและแนวโน้ม", "แผนภาพความเสี่ยง และการเปลี่ยนแปลงจากรายงานครั้งก่อน"],
     ["3. ความคืบหน้าแผนงาน", "แผนงาน [เป็นไปตามแผน หรือ ล่าช้า]", "เป้าหมายสำคัญ งบประมาณที่ใช้ และความคืบหน้าของ CSF Profile"],
     ["4. เหตุการณ์และการปฏิบัติตามกฎเกณฑ์", "เหตุการณ์สำคัญและสถานะด้านกฎหมาย", "เหตุการณ์ การแจ้งเหตุ และข้อตรวจพบที่เลยกำหนด"],
     ["5. เรื่องที่ขอให้ตัดสินใจ", "สิ่งที่คณะกรรมการต้องตัดสินใจ", "ทางเลือก ต้นทุน และความเสี่ยงคงเหลือ"]], "w": [3.5, 5.5, 7.5]},
   {"t": ["Page", "Key message (H1 2026 report)", "Content"], "r": [
     ["1. Summary", "Ransomware recovery capability improved; overall risk remains above appetite for vendor access", "Backup and MSSP delivered; vendor access is the main open gap"],
     ["2. Top risks", "R-001 ransomware moved from Critical (16) to High (12)", "Heat map with five risks"],
     ["3. Program progress", "Roadmap 78% on track despite 15% budget cut", "DLP deferred to 2027"],
     ["4. Incidents and compliance", "One email compromise attempt contained in 2 hours; no notifiable breach", "CII annual assessment submitted on time"],
     ["5. Decisions requested", "Approve THB 2.1 million for medical device network isolation in 2027", "Option A full isolation; Option B priority devices only"]], "w": [3.5, 5.5, 7.5]}),
 ],
 bp=[("Write in business terms: downtime, patient or customer impact, legal exposure, and cost.", "เขียนด้วยภาษาธุรกิจ ได้แก่ ระยะเวลาหยุดชะงัก ผลกระทบต่อผู้รับบริการ ความเสี่ยงทางกฎหมาย และต้นทุน"),
     ("Keep the report to five pages with an appendix for detail.", "จำกัดรายงานไว้ 5 หน้า และใส่รายละเอียดในภาคผนวก"),
     ("Show trends over time, not snapshots.", "แสดงแนวโน้มตามช่วงเวลา ไม่ใช่ภาพ ณ จุดเดียว")],
 mistakes=[("Presenting technical metrics (blocked attacks) that boards cannot act on.", "นำเสนอตัวชี้วัดทางเทคนิค (เช่น จำนวนการโจมตีที่ถูกบล็อก) ที่คณะกรรมการนำไปตัดสินใจไม่ได้")],
)

C["GV-PRC-007"] = dict(
 purpose=("This procedure defines how internal audit plans, performs, reports, and follows up independent audits of the security program (ISO/IEC 27001:2022 Clause 9.2) and the annual cybersecurity audit for CII (CSA s.54).",
          "ระเบียบปฏิบัตินี้กำหนดวิธีที่ฝ่ายตรวจสอบภายในวางแผน ดำเนินการ รายงาน และติดตามผลการตรวจสอบแผนงานด้านความมั่นคงปลอดภัยอย่างเป็นอิสระ (ISO/IEC 27001:2022 ข้อ 9.2) และการตรวจสอบด้านไซเบอร์ประจำปีสำหรับ CII (พ.ร.บ.ไซเบอร์ฯ มาตรา 54)"),
 sections=[
  ("Auditor Independence and Competence", "ความเป็นอิสระและความสามารถของผู้ตรวจสอบ", "State independence and competence requirements for auditors.", "ระบุข้อกำหนดด้านความเป็นอิสระและความสามารถของผู้ตรวจสอบ",
   ["Auditors do not audit their own work.", "Auditors hold relevant qualifications (for example, ISO/IEC 27001 Lead Auditor, CISA) or are supported by qualified external specialists.",
    "For CII, the annual audit is performed by an internal or external auditor that meets NCSA criteria [VERIFY current auditor qualification requirements]."],
   ["ผู้ตรวจสอบต้องไม่ตรวจสอบงานของตนเอง", "ผู้ตรวจสอบมีคุณวุฒิที่เกี่ยวข้อง (เช่น ISO/IEC 27001 Lead Auditor หรือ CISA) หรือได้รับการสนับสนุนจากผู้เชี่ยวชาญภายนอกที่มีคุณสมบัติ",
    "สำหรับ CII การตรวจสอบประจำปีดำเนินการโดยผู้ตรวจสอบภายในหรือภายนอกที่เป็นไปตามเกณฑ์ของ สกมช. [VERIFY ข้อกำหนดคุณสมบัติผู้ตรวจสอบฉบับปัจจุบัน]"]),
  ("Audit Process", "กระบวนการตรวจสอบ", "Describe the audit steps from planning to follow-up.", "อธิบายขั้นตอนการตรวจสอบตั้งแต่การวางแผนจนถึงการติดตามผล",
   {"t": ["Step", "Activity", "Output"], "r": [
     ["1", "Plan the annual program based on risk and previous results", "Internal Audit Program (GV-PLN-002)"], ["2", "Define scope, criteria, and audit plan for each audit", "Audit plan"],
     ["3", "Collect evidence through interviews, document review, sampling, and technical testing", "Working papers"], ["4", "Rate findings and agree facts with auditees", "Draft report"],
     ["5", "Issue the report to management and the [AC]", "Internal Audit Report (GV-TPL-006)"], ["6", "Track corrective actions to closure and verify effectiveness", "Updates in ID-REG-007"]], "w": [1.2, 9.3, 6.0]},
   {"t": ["ขั้นตอน", "กิจกรรม", "ผลลัพธ์"], "r": [
     ["1", "วางแผนการตรวจสอบประจำปีตามความเสี่ยงและผลครั้งก่อน", "แผนการตรวจสอบภายในประจำปี (GV-PLN-002)"], ["2", "กำหนดขอบเขต เกณฑ์ และแผนการตรวจสอบแต่ละครั้ง", "แผนการตรวจสอบ"],
     ["3", "รวบรวมหลักฐานผ่านการสัมภาษณ์ การทบทวนเอกสาร การสุ่มตัวอย่าง และการทดสอบทางเทคนิค", "กระดาษทำการ"], ["4", "จัดระดับข้อตรวจพบและยืนยันข้อเท็จจริงกับผู้รับการตรวจ", "ร่างรายงาน"],
     ["5", "ออกรายงานต่อผู้บริหารและ [AC]", "รายงานผลการตรวจสอบภายใน (GV-TPL-006)"], ["6", "ติดตามการแก้ไขจนแล้วเสร็จและยืนยันประสิทธิผล", "ปรับปรุงใน ID-REG-007"]], "w": [1.2, 9.3, 6.0]}),
 ],
 bp=[("Cover every ISMS clause and relevant Annex A control at least once in a three-year cycle, with high-risk areas every year.", "ตรวจสอบทุกข้อของ ISMS และมาตรการใน Annex A ที่เกี่ยวข้องอย่างน้อยหนึ่งครั้งในรอบ 3 ปี และตรวจพื้นที่ความเสี่ยงสูงทุกปี"),
     ("Combine the ISO internal audit and the CII annual audit where scopes overlap to reduce disruption.", "รวมการตรวจสอบภายในตาม ISO และการตรวจสอบประจำปีสำหรับ CII เมื่อขอบเขตทับซ้อนกัน เพื่อลดผลกระทบต่อการปฏิบัติงาน"),
     ("Test operating effectiveness with samples, not only design.", "ทดสอบประสิทธิผลการปฏิบัติงานด้วยการสุ่มตัวอย่าง ไม่ใช่เพียงการออกแบบ")],
 mistakes=[("The security team audits itself and calls it internal audit.", "ทีมความมั่นคงปลอดภัยตรวจสอบงานของตนเองแล้วเรียกว่าการตรวจสอบภายใน")],
)

C["GV-PLN-002"] = dict(
 purpose=("This program sets the annual schedule, scope, and resources for internal security audits and the CII annual cybersecurity audit.",
          "แผนนี้กำหนดกำหนดการ ขอบเขต และทรัพยากรสำหรับการตรวจสอบภายในด้านความมั่นคงปลอดภัยและการตรวจสอบด้านไซเบอร์ประจำปีสำหรับ CII"),
 sections=[
  ("Annual Audit Schedule", "กำหนดการตรวจสอบประจำปี", "List each audit with scope, criteria, timing, and auditor (ISO/IEC 27001:2022 Clause 9.2.2).", "ระบุการตรวจสอบแต่ละครั้งพร้อมขอบเขต เกณฑ์ ช่วงเวลา และผู้ตรวจสอบ (ISO/IEC 27001:2022 ข้อ 9.2.2)",
   {"t": ["Audit", "Scope", "Criteria", "Quarter", "Auditor"], "r": [["[Audit 1]", "", "", "Q1", ""], ["[Audit 2]", "", "", "Q2", ""], ["[Audit 3]", "", "", "Q3", ""], ["CII annual audit (if CII)", "Code of practice compliance", "CSA s.54; NCSC framework", "Q4", "Independent auditor"]]},
   {"t": ["การตรวจสอบ", "ขอบเขต", "เกณฑ์", "ไตรมาส", "ผู้ตรวจสอบ"], "r": [["[การตรวจสอบที่ 1]", "", "", "Q1", ""], ["[การตรวจสอบที่ 2]", "", "", "Q2", ""], ["[การตรวจสอบที่ 3]", "", "", "Q3", ""], ["การตรวจสอบประจำปีสำหรับ CII (กรณีเป็น CII)", "การปฏิบัติตามประมวลแนวทางปฏิบัติ", "พ.ร.บ.ไซเบอร์ฯ มาตรา 54 และกรอบมาตรฐานของ กมช.", "Q4", "ผู้ตรวจสอบอิสระ"]]},
   {"t": ["Audit", "Scope", "Criteria", "Quarter", "Auditor"], "r": [
     ["Identity and access management", "HIS, Active Directory, privileged access", "PR-POL-001, PR-STD-002, ISO Annex A 5.15 to 5.18", "Q1 2026", "Internal Audit with external IT specialist"],
     ["Backup and disaster recovery", "HIS, PACS, LIS restore capability", "PR-STD-006, RC-PLN-002", "Q2 2026", "Internal Audit"],
     ["Third-party and vendor remote access", "Medical device and system vendors", "GV-POL-006, PR-STD-003", "Q3 2026", "Internal Audit"],
     ["CII annual cybersecurity audit", "CMC code of practice and controls", "CSA s.54; NCSC framework B.E. 2564", "Q4 2026", "External auditor (firm under contract)"]]}),
 ],
 bp=[("Base the program on the risk register so audit effort follows risk.", "จัดทำแผนจากทะเบียนความเสี่ยง เพื่อให้การตรวจสอบมุ่งไปที่ความเสี่ยง"),
     ("Agree the program with the Audit Committee at the start of the year.", "ตกลงแผนกับคณะกรรมการตรวจสอบตั้งแต่ต้นปี")],
 mistakes=[("Scheduling all audits in the last quarter, which leaves no time to fix findings before year-end reporting.", "จัดการตรวจสอบทั้งหมดในไตรมาสสุดท้าย ทำให้ไม่มีเวลาแก้ไขข้อตรวจพบก่อนการรายงานสิ้นปี")],
)

C["GV-TPL-006"] = dict(
 purpose=("This template standardizes internal and CII audit reports so findings are clear, rated consistently, and traceable to corrective actions.",
          "แม่แบบนี้กำหนดรูปแบบรายงานการตรวจสอบภายในและการตรวจสอบสำหรับ CII ให้เป็นมาตรฐานเดียวกัน เพื่อให้ข้อตรวจพบชัดเจน จัดระดับสม่ำเสมอ และตรวจย้อนไปยังการแก้ไขได้"),
 sections=[
  ("Report Sections", "หัวข้อในรายงาน", "Include the minimum sections of an audit report.", "ระบุหัวข้อขั้นต่ำของรายงานการตรวจสอบ",
   {"n": ["Executive summary: overall opinion and key findings.", "Scope, criteria, period, and method.", "Findings: condition, criteria, cause, effect (risk), recommendation, rating, management response, owner, and due date.",
          "Status of previous findings.", "Distribution list and approval."]},
   {"n": ["บทสรุปผู้บริหาร: ความเห็นโดยรวมและข้อตรวจพบสำคัญ", "ขอบเขต เกณฑ์ ช่วงเวลา และวิธีการ", "ข้อตรวจพบ: สภาพที่พบ เกณฑ์ สาเหตุ ผลกระทบ (ความเสี่ยง) ข้อเสนอแนะ ระดับ คำชี้แจงของฝ่ายบริหาร ผู้รับผิดชอบ และกำหนดเสร็จ",
          "สถานะของข้อตรวจพบครั้งก่อน", "รายชื่อผู้รับรายงานและการอนุมัติ"]}),
  ("Finding Format", "รูปแบบข้อตรวจพบ", "Write each finding in a consistent structure.", "เขียนข้อตรวจพบแต่ละรายการด้วยโครงสร้างเดียวกัน",
   {"t": ["Element", "Content"], "r": [["Finding ID and title", ""], ["Condition (what we found)", ""], ["Criteria (what should be)", ""], ["Cause", ""], ["Effect (risk)", ""], ["Rating", "Critical, High, Medium, Low"], ["Recommendation", ""], ["Management response, owner, due date", ""]], "w": [5.5, 11.0]},
   {"t": ["องค์ประกอบ", "เนื้อหา"], "r": [["รหัสและชื่อข้อตรวจพบ", ""], ["สภาพที่พบ", ""], ["เกณฑ์ (สิ่งที่ควรเป็น)", ""], ["สาเหตุ", ""], ["ผลกระทบ (ความเสี่ยง)", ""], ["ระดับ", "วิกฤต สูง ปานกลาง ต่ำ"], ["ข้อเสนอแนะ", ""], ["คำชี้แจงของฝ่ายบริหาร ผู้รับผิดชอบ กำหนดเสร็จ", ""]], "w": [5.5, 11.0]},
   {"t": ["Element", "Example from IA-2025-04"], "r": [
     ["Finding ID and title", "IA-2025-04-02: HIS accounts of former staff remain active"],
     ["Condition", "38 of 1,410 active HIS accounts belonged to staff who left more than 30 days earlier."],
     ["Criteria", "GV-STD-001 HR-05 requires accounts to be disabled on the last working day."],
     ["Cause", "HR leaver list was emailed monthly; no automated trigger to HIS."],
     ["Effect", "Former staff could access patient records, creating a notifiable breach risk under PDPA."],
     ["Rating", "High"],
     ["Recommendation", "Automate HR-to-HIS deprovisioning and reconcile monthly until automated."],
     ["Management response", "Agreed. CIO; automation live 30 April 2026; monthly reconciliation from December 2025."]], "w": [5.5, 11.0]}),
 ],
 bp=[("Write findings so a reader outside IT understands the business risk.", "เขียนข้อตรวจพบให้ผู้อ่านที่ไม่ใช่ฝ่าย IT เข้าใจความเสี่ยงทางธุรกิจ"),
     ("Agree facts with auditees before issuing, to avoid disputes later.", "ยืนยันข้อเท็จจริงกับผู้รับการตรวจก่อนออกรายงาน เพื่อหลีกเลี่ยงข้อโต้แย้งภายหลัง")],
 mistakes=[("Findings describe symptoms without root cause, so the same issue returns.", "ข้อตรวจพบอธิบายอาการโดยไม่ระบุสาเหตุที่แท้จริง ทำให้ปัญหาเดิมเกิดซ้ำ")],
)
