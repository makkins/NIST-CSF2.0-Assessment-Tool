# -*- coding: utf-8 -*-
"""Interview question bank: Identify (ID) and Protect (PR)."""
from iq_gv import Q, add

# ID.AM Asset Management
add("ID.AM-01", "ITM SYSOWN",
    ("How does the organization maintain its hardware inventory, and how complete and current is it?",
     "องค์กรจัดทำทะเบียนทรัพย์สินฮาร์ดแวร์อย่างไร และครบถ้วนเป็นปัจจุบันเพียงใด"),
    [("Is the inventory updated automatically or by hand? When was it last reconciled?", "ทะเบียนปรับปรุงอัตโนมัติหรือด้วยมือ และกระทบยอดครั้งล่าสุดเมื่อใด"),
     ("Are medical devices, OT, and network devices included?", "รวมอุปกรณ์การแพทย์ ระบบควบคุมอุตสาหกรรม (OT) และอุปกรณ์เครือข่ายหรือไม่")],
    ("Hardware asset register, discovery tool export", "ทะเบียนทรัพย์สินฮาร์ดแวร์ ผลส่งออกจากเครื่องมือสำรวจ"))
add("ID.AM-02", "ITM SYSOWN DEV",
    ("Is there an inventory of software, systems, and cloud services, including who owns each?",
     "มีทะเบียนซอฟต์แวร์ ระบบ และบริการคลาวด์ พร้อมเจ้าของแต่ละรายการหรือไม่"),
    [("How do you find software or cloud services bought without IT (shadow IT)?", "ค้นหาซอฟต์แวร์หรือบริการคลาวด์ที่จัดหาโดยไม่ผ่าน IT ได้อย่างไร"),
     ("Are versions and support end dates recorded?", "มีการบันทึกเวอร์ชันและวันสิ้นสุดการสนับสนุนหรือไม่")],
    ("Software and application inventory, system owner list", "ทะเบียนซอฟต์แวร์และระบบงาน รายชื่อเจ้าของระบบ"))
add("ID.AM-03", "ITM",
    ("Are network diagrams and data flow diagrams maintained for key systems?",
     "มีการจัดทำและปรับปรุงแผนผังเครือข่ายและแผนผังการไหลของข้อมูลสำหรับระบบสำคัญหรือไม่"),
    [("When was the network diagram last updated?", "แผนผังเครือข่ายปรับปรุงครั้งล่าสุดเมื่อใด"),
     ("Are connections to suppliers and the internet shown?", "แสดงการเชื่อมต่อกับผู้ให้บริการและอินเทอร์เน็ตหรือไม่")],
    ("Network diagram, data flow diagrams", "แผนผังเครือข่าย แผนผังการไหลของข้อมูล"))
add("ID.AM-04", "PROC ITM",
    ("Is there an inventory of services provided by suppliers, including cloud and managed services?",
     "มีทะเบียนบริการที่ได้รับจากผู้ให้บริการ รวมถึงบริการคลาวด์และบริการบริหารจัดการหรือไม่"),
    [("Does it show which business process each service supports?", "แสดงว่าบริการแต่ละรายการสนับสนุนกระบวนการธุรกิจใดหรือไม่"),
     ("Who keeps it up to date?", "ใครเป็นผู้ปรับปรุงให้เป็นปัจจุบัน")],
    ("Supplier service inventory", "ทะเบียนบริการของผู้ให้บริการ"))
add("ID.AM-05", "CISO SYSOWN BCM",
    ("How are assets classified and prioritized by criticality and business impact?",
     "จัดประเภทและจัดลำดับความสำคัญของทรัพย์สินตามความสำคัญและผลกระทบทางธุรกิจอย่างไร"),
    [("Which systems are rated most critical, and who decided?", "ระบบใดถูกจัดว่าสำคัญที่สุด และใครเป็นผู้ตัดสิน"),
     ("Does criticality drive patching, backup, and monitoring priorities?", "ระดับความสำคัญใช้กำหนดลำดับการแพตช์ การสำรองข้อมูล และการเฝ้าระวังหรือไม่")],
    ("Asset classification scheme, critical asset list, BIA", "เกณฑ์การจัดประเภททรัพย์สิน รายการทรัพย์สินสำคัญ BIA"))
add("ID.AM-07", "DPO CISO SYSOWN",
    ("Does the organization know where its sensitive data is stored and processed?",
     "องค์กรทราบหรือไม่ว่าข้อมูลสำคัญถูกจัดเก็บและประมวลผลที่ใด"),
    [("Is there a Record of Processing Activities (ROPA) under PDPA s.39?", "มีบันทึกรายการกิจกรรมการประมวลผล (ROPA) ตาม PDPA มาตรา 39 หรือไม่"),
     ("Is data classified, and are labels used?", "มีการจัดชั้นข้อมูลและการติดป้ายกำกับหรือไม่")],
    ("ROPA, data inventory, data classification standard", "ROPA ทะเบียนข้อมูล มาตรฐานการจัดชั้นข้อมูล"))
add("ID.AM-08", "ITM SYSOWN",
    ("How are systems and data managed across their life cycle, from acquisition to secure disposal?",
     "บริหารจัดการระบบและข้อมูลตลอดวงจรชีวิต ตั้งแต่การจัดหาจนถึงการทำลายอย่างปลอดภัยอย่างไร"),
    [("How are old disks and devices wiped or destroyed?", "ล้างหรือทำลายดิสก์และอุปกรณ์เก่าอย่างไร"),
     ("Are end-of-life systems tracked with a replacement plan?", "ระบบที่หมดอายุการสนับสนุนได้รับการติดตามพร้อมแผนทดแทนหรือไม่")],
    ("Asset life cycle procedure, disposal records, end-of-life list", "ขั้นตอนวงจรชีวิตทรัพย์สิน บันทึกการทำลาย รายการระบบหมดอายุ"))

# ID.RA Risk Assessment
add("ID.RA-01", "ITM SOC CISO",
    ("How are vulnerabilities identified, validated, and recorded?",
     "ระบุ ยืนยัน และบันทึกช่องโหว่อย่างไร"),
    [("How often are vulnerability scans run, and do they cover all critical systems?", "สแกนช่องโหว่บ่อยเพียงใด และครอบคลุมระบบสำคัญทั้งหมดหรือไม่"),
     ("When was the last penetration test, and were findings fixed?", "ทดสอบเจาะระบบครั้งล่าสุดเมื่อใด และแก้ไขข้อตรวจพบแล้วหรือไม่")],
    ("Scan reports, penetration test report, vulnerability tracker", "รายงานการสแกน รายงานทดสอบเจาะระบบ ทะเบียนติดตามช่องโหว่"))
add("ID.RA-02", "SOC CISO",
    ("Does the organization receive cyber threat intelligence, and from which sources?",
     "องค์กรได้รับข้อมูลข่าวกรองภัยคุกคามไซเบอร์หรือไม่ และจากแหล่งใด"),
    [("Are you a member of ThaiCERT, a sector CERT, or an information sharing group?", "เป็นสมาชิก ThaiCERT ศูนย์ CERT ของภาคส่วน หรือกลุ่มแลกเปลี่ยนข้อมูลหรือไม่"),
     ("Who reads the alerts and what do they do with them?", "ใครอ่านการแจ้งเตือน และนำไปดำเนินการอย่างไร")],
    ("Threat intelligence subscriptions, advisory handling records", "การสมัครรับข้อมูลข่าวกรอง บันทึกการจัดการประกาศเตือน"))
add("ID.RA-03", "CISO SOC",
    ("Are internal and external threats to the organization identified and recorded?",
     "มีการระบุและบันทึกภัยคุกคามภายในและภายนอกต่อองค์กรหรือไม่"),
    [("What are the top threats you worry about, such as ransomware or insider misuse?", "ภัยคุกคามหลักที่กังวลคืออะไร เช่น แรนซัมแวร์หรือการใช้งานผิดวัตถุประสงค์โดยบุคคลภายใน"),
     ("Is there a threat catalog used in risk assessment?", "มีบัญชีภัยคุกคามที่ใช้ในการประเมินความเสี่ยงหรือไม่")],
    ("Threat catalog or threat profile, risk assessment report", "บัญชีภัยคุกคาม รายงานการประเมินความเสี่ยง"))
add("ID.RA-04", "CISO CRO SYSOWN",
    ("How are the likelihood and impact of threats exploiting vulnerabilities assessed?",
     "ประเมินโอกาสและผลกระทบที่ภัยคุกคามจะใช้ช่องโหว่อย่างไร"),
    [("Do business owners take part in rating impact?", "เจ้าของกระบวนการธุรกิจมีส่วนร่วมในการให้คะแนนผลกระทบหรือไม่"),
     ("Is the assessment repeated at least once a year?", "มีการประเมินซ้ำอย่างน้อยปีละครั้งหรือไม่")],
    ("Risk assessment worksheets, workshop records", "แบบประเมินความเสี่ยง บันทึกการประชุมเชิงปฏิบัติการ"))
add("ID.RA-05", "CISO CRO",
    ("How does the organization combine threats, vulnerabilities, likelihood, and impact to decide which risks to address first?",
     "องค์กรนำภัยคุกคาม ช่องโหว่ โอกาส และผลกระทบ มาประกอบกันเพื่อตัดสินใจว่าจะจัดการความเสี่ยงใดก่อนอย่างไร"),
    [("Can you show the current top ten cybersecurity risks?", "แสดงความเสี่ยงด้านไซเบอร์ 10 อันดับแรกในปัจจุบันได้หรือไม่"),
     ("Is inherent risk recorded separately from residual risk?", "บันทึกความเสี่ยงก่อนควบคุมแยกจากความเสี่ยงคงเหลือหรือไม่")],
    ("Cybersecurity risk register, risk heat map", "ทะเบียนความเสี่ยงด้านไซเบอร์ แผนภาพความเสี่ยง"))
add("ID.RA-06", "CISO RISK",
    ("How are risk responses chosen, planned, tracked, and reported?",
     "เลือก วางแผน ติดตาม และรายงานการตอบสนองความเสี่ยงอย่างไร"),
    [("Does each risk have a treatment owner and target date?", "ความเสี่ยงแต่ละรายการมีเจ้าของแผนจัดการและวันที่เป้าหมายหรือไม่"),
     ("How many treatment actions are overdue?", "มีแผนจัดการความเสี่ยงที่เกินกำหนดกี่รายการ")],
    ("Risk treatment plan, status reports", "แผนจัดการความเสี่ยง รายงานความคืบหน้า"))
add("ID.RA-07", "ITM CISO",
    ("How are changes and exceptions assessed for security risk, approved, and tracked?",
     "ประเมินความเสี่ยงด้านความมั่นคงปลอดภัย อนุมัติ และติดตามการเปลี่ยนแปลงและการยกเว้นอย่างไร"),
    [("Does the change advisory board (CAB) review security impact?", "คณะกรรมการพิจารณาการเปลี่ยนแปลง (CAB) พิจารณาผลกระทบด้านความมั่นคงปลอดภัยหรือไม่"),
     ("Do exceptions have an expiry date?", "การยกเว้นมีวันหมดอายุหรือไม่")],
    ("Change management procedure, change records, exception register", "ขั้นตอนบริหารการเปลี่ยนแปลง บันทึกการเปลี่ยนแปลง ทะเบียนการยกเว้น"))
add("ID.RA-08", "CISO DEV",
    ("Is there a process to receive and respond to vulnerability reports from outside parties?",
     "มีกระบวนการรับและตอบสนองรายงานช่องโหว่จากบุคคลภายนอกหรือไม่"),
    [("If a researcher found a flaw in your website, how would they contact you?", "หากนักวิจัยพบช่องโหว่ในเว็บไซต์ จะติดต่อองค์กรได้อย่างไร"),
     ("Do you track vendor security advisories for products you use?", "ติดตามประกาศด้านความมั่นคงปลอดภัยของผู้ขายสำหรับผลิตภัณฑ์ที่ใช้หรือไม่")],
    ("Vulnerability disclosure policy, security contact page", "นโยบายการเปิดเผยช่องโหว่ หน้าช่องทางติดต่อด้านความมั่นคงปลอดภัย"))
add("ID.RA-09", "ITM PROC",
    ("How do you confirm that hardware and software are genuine and unaltered before use?",
     "ยืนยันว่าฮาร์ดแวร์และซอฟต์แวร์เป็นของแท้และไม่ถูกดัดแปลงก่อนใช้งานอย่างไร"),
    [("Is software downloaded only from official sources and checked against hashes or signatures?", "ดาวน์โหลดซอฟต์แวร์จากแหล่งทางการเท่านั้นและตรวจสอบค่าแฮชหรือลายมือชื่อดิจิทัลหรือไม่"),
     ("Is hardware bought only from authorized resellers?", "จัดซื้อฮาร์ดแวร์จากตัวแทนจำหน่ายที่ได้รับอนุญาตเท่านั้นหรือไม่")],
    ("Procurement rules, software approval records", "หลักเกณฑ์การจัดซื้อ บันทึกการอนุมัติซอฟต์แวร์"))
add("ID.RA-10", "PROC CISO",
    ("Are critical suppliers assessed for cybersecurity risk before purchase?",
     "มีการประเมินความเสี่ยงด้านไซเบอร์ของผู้ให้บริการสำคัญก่อนจัดซื้อหรือไม่"),
    [("Show an example assessment for a recent critical purchase.", "แสดงตัวอย่างผลการประเมินสำหรับการจัดซื้อสำคัญครั้งล่าสุด"),
     ("Are high-risk findings resolved before signing?", "ข้อตรวจพบความเสี่ยงสูงได้รับการแก้ไขก่อนลงนามหรือไม่")],
    ("Pre-contract supplier risk assessments", "ผลการประเมินความเสี่ยงผู้ให้บริการก่อนทำสัญญา"))

# ID.IM Improvement
add("ID.IM-01", "CISO IA",
    ("How are improvements identified from audits, assessments, and reviews, and tracked to completion?",
     "ระบุการปรับปรุงจากการตรวจสอบ การประเมิน และการทบทวน และติดตามจนเสร็จสิ้นอย่างไร"),
    [("Is there one tracker for all audit and assessment findings?", "มีทะเบียนเดียวที่ติดตามข้อตรวจพบจากการตรวจสอบและการประเมินทั้งหมดหรือไม่"),
     ("How many findings from the last audit are still open?", "ข้อตรวจพบจากการตรวจสอบครั้งล่าสุดยังเปิดอยู่กี่รายการ")],
    ("Findings tracker, corrective action plan", "ทะเบียนติดตามข้อตรวจพบ แผนปฏิบัติการแก้ไข"))
add("ID.IM-02", "CISO SOC BCM",
    ("Are lessons from security tests and exercises turned into improvements?",
     "บทเรียนจากการทดสอบและการฝึกซ้อมด้านความมั่นคงปลอดภัยถูกนำไปปรับปรุงหรือไม่"),
    [("What changed after the last tabletop exercise or penetration test?", "หลังการฝึกซ้อมบนโต๊ะหรือการทดสอบเจาะระบบครั้งล่าสุดมีอะไรเปลี่ยนแปลง"),
     ("Is there an after-action report?", "มีรายงานสรุปหลังการฝึกซ้อมหรือไม่")],
    ("Exercise reports, after-action reports, action tracker", "รายงานการฝึกซ้อม รายงานสรุปหลังการฝึกซ้อม ทะเบียนติดตามการดำเนินการ"))
add("ID.IM-03", "CISO ITM SOC",
    ("Are improvements identified from day-to-day operations and incidents?",
     "มีการระบุการปรับปรุงจากการปฏิบัติงานประจำวันและเหตุการณ์ที่เกิดขึ้นหรือไม่"),
    [("Are lessons-learned meetings held after significant incidents?", "มีการประชุมถอดบทเรียนหลังเหตุการณ์สำคัญหรือไม่"),
     ("Are operational metrics reviewed to find recurring problems?", "มีการทบทวนตัวชี้วัดการปฏิบัติงานเพื่อหาปัญหาที่เกิดซ้ำหรือไม่")],
    ("Lessons-learned records, problem management records", "บันทึกการถอดบทเรียน บันทึกการบริหารปัญหา"))
add("ID.IM-04", "CISO BCM SOC",
    ("Are the incident response plan and other cybersecurity plans established, communicated, maintained, and improved?",
     "แผนรับมือเหตุการณ์และแผนด้านไซเบอร์อื่นได้รับการจัดทำ สื่อสาร ดูแล และปรับปรุงหรือไม่"),
    [("When were the plans last updated, and do staff know where to find them during an outage?", "แผนปรับปรุงครั้งล่าสุดเมื่อใด และพนักงานทราบหรือไม่ว่าจะหาแผนได้ที่ไหนเมื่อระบบล่ม"),
     ("Are plans tested at least annually?", "มีการทดสอบแผนอย่างน้อยปีละครั้งหรือไม่")],
    ("Incident response plan, BCP, DRP, revision history", "แผนรับมือเหตุการณ์ BCP DRP ประวัติการแก้ไข"))

# PR.AA Identity Management, Authentication, and Access Control
add("PR.AA-01", "ITM HR",
    ("How are user, service, and device identities and credentials created, changed, and removed?",
     "สร้าง เปลี่ยนแปลง และลบตัวตนและข้อมูลยืนยันตัวตนของผู้ใช้ บริการ และอุปกรณ์อย่างไร"),
    [("How long after resignation is an account disabled? Can you show evidence for a recent leaver?", "หลังพนักงานลาออกนานเท่าใดบัญชีจึงถูกระงับ และแสดงหลักฐานของผู้ลาออกล่าสุดได้หรือไม่"),
     ("Are shared and service accounts inventoried with owners?", "บัญชีที่ใช้ร่วมกันและบัญชีบริการมีทะเบียนพร้อมเจ้าของหรือไม่")],
    ("Joiner-mover-leaver procedure, account request records, service account list", "ขั้นตอนการรับเข้า เปลี่ยนตำแหน่ง และพ้นสภาพ บันทึกคำขอบัญชี รายการบัญชีบริการ"))
add("PR.AA-02", "ITM HR",
    ("How is a person's identity verified before an account or credential is issued or reset?",
     "ยืนยันตัวตนของบุคคลก่อนออกหรือรีเซ็ตบัญชีหรือข้อมูลยืนยันตัวตนอย่างไร"),
    [("How does the service desk verify a caller who asks for a password reset?", "เจ้าหน้าที่ Service Desk ยืนยันตัวตนผู้โทรมาขอรีเซ็ตรหัสผ่านอย่างไร"),
     ("Are contractor identities verified the same way as employees?", "ยืนยันตัวตนผู้รับจ้างด้วยวิธีเดียวกับพนักงานหรือไม่")],
    ("Identity proofing procedure, service desk script", "ขั้นตอนการพิสูจน์ตัวตน แนวปฏิบัติของ Service Desk"))
add("PR.AA-03", "ITM CISO",
    ("How are users, services, and devices authenticated, and where is multi-factor authentication (MFA) used?",
     "ยืนยันตัวตนของผู้ใช้ บริการ และอุปกรณ์อย่างไร และใช้การยืนยันตัวตนหลายปัจจัย (MFA) ที่ใดบ้าง"),
    [("Is MFA enforced for email, remote access, cloud admin, and privileged accounts?", "บังคับใช้ MFA กับอีเมล การเข้าถึงระยะไกล ผู้ดูแลคลาวด์ และบัญชีสิทธิ์สูงหรือไม่"),
     ("What is the password standard, and is it technically enforced?", "มาตรฐานรหัสผ่านคืออะไร และบังคับใช้ด้วยระบบหรือไม่")],
    ("MFA coverage report, authentication policy settings", "รายงานความครอบคลุม MFA การตั้งค่านโยบายการยืนยันตัวตน"))
add("PR.AA-04", "ITM DEV",
    ("How are identity assertions, such as single sign-on (SSO) tokens and federation, protected and verified?",
     "ปกป้องและตรวจสอบข้อมูลยืนยันตัวตน เช่น โทเคนการลงชื่อเข้าใช้ครั้งเดียว (SSO) และการเชื่อมโยงตัวตน อย่างไร"),
    [("Which applications use SSO, and which still use local accounts?", "ระบบงานใดใช้ SSO และระบบใดยังใช้บัญชีภายในระบบ"),
     ("Are token lifetimes and signing keys managed?", "มีการบริหารอายุโทเคนและกุญแจลงนามหรือไม่")],
    ("SSO configuration, application integration list", "การตั้งค่า SSO รายการระบบที่เชื่อมต่อ"))
add("PR.AA-05", "ITM SYSOWN CISO",
    ("How are access rights defined, approved, and reviewed, including privileged access?",
     "กำหนด อนุมัติ และทบทวนสิทธิ์การเข้าถึงอย่างไร รวมถึงสิทธิ์สูง"),
    [("When was the last user access review for a critical system, and what was removed?", "ทบทวนสิทธิ์ผู้ใช้ของระบบสำคัญครั้งล่าสุดเมื่อใด และถอนสิทธิ์อะไรไปบ้าง"),
     ("How many domain administrators are there, and is privileged access controlled by a tool?", "มีผู้ดูแลโดเมนกี่ราย และควบคุมสิทธิ์สูงด้วยเครื่องมือหรือไม่")],
    ("Access control standard, access review records, privileged account list", "มาตรฐานการควบคุมการเข้าถึง บันทึกการทบทวนสิทธิ์ รายการบัญชีสิทธิ์สูง"))
add("PR.AA-06", "FAC ITM",
    ("How is physical access to offices, data centers, and equipment rooms controlled and monitored?",
     "ควบคุมและเฝ้าระวังการเข้าถึงทางกายภาพของสำนักงาน ศูนย์ข้อมูล และห้องอุปกรณ์อย่างไร"),
    [("Who has access to the server room, and is the list reviewed?", "ใครมีสิทธิ์เข้าห้องเซิร์ฟเวอร์ และรายชื่อได้รับการทบทวนหรือไม่"),
     ("Are visitors logged and escorted?", "ผู้มาติดต่อได้รับการบันทึกและมีผู้นำพาหรือไม่")],
    ("Access card logs, visitor log, server room access list", "บันทึกบัตรผ่าน สมุดผู้มาติดต่อ รายชื่อผู้มีสิทธิ์เข้าห้องเซิร์ฟเวอร์"))

# PR.AT Awareness and Training
add("PR.AT-01", "HR CISO",
    ("What cybersecurity awareness training do all staff receive, and how is it measured?",
     "พนักงานทุกคนได้รับการอบรมสร้างความตระหนักด้านไซเบอร์อะไรบ้าง และวัดผลอย่างไร"),
    [("What share of staff completed training this year?", "ปีนี้พนักงานผ่านการอบรมแล้วสัดส่วนเท่าใด"),
     ("Are phishing simulations run, and what is the click rate trend?", "มีการจำลองฟิชชิงหรือไม่ และแนวโน้มอัตราการคลิกเป็นอย่างไร")],
    ("Training plan, completion records, phishing simulation results", "แผนการอบรม บันทึกการผ่านการอบรม ผลการจำลองฟิชชิง"))
add("PR.AT-02", "CISO HR ITM",
    ("Do people in specialized roles, such as administrators, developers, and executives, receive role-based training?",
     "บุคลากรในบทบาทเฉพาะ เช่น ผู้ดูแลระบบ นักพัฒนา และผู้บริหาร ได้รับการอบรมตามบทบาทหรือไม่"),
    [("What security training did the IT team receive last year?", "ปีที่ผ่านมาทีม IT ได้รับการอบรมด้านความมั่นคงปลอดภัยอะไรบ้าง"),
     ("Is there a skills matrix for security-related roles?", "มีตารางทักษะสำหรับบทบาทที่เกี่ยวข้องกับความมั่นคงปลอดภัยหรือไม่")],
    ("Role-based training records, skills matrix", "บันทึกการอบรมตามบทบาท ตารางทักษะ"))

# PR.DS Data Security
add("PR.DS-01", "ITM DPO",
    ("How is stored data protected, for example with encryption, access control, and integrity checks?",
     "ปกป้องข้อมูลที่จัดเก็บอย่างไร เช่น การเข้ารหัส การควบคุมการเข้าถึง และการตรวจสอบความถูกต้อง"),
    [("Are laptops, mobile devices, and databases with sensitive data encrypted?", "โน้ตบุ๊ก อุปกรณ์เคลื่อนที่ และฐานข้อมูลที่มีข้อมูลสำคัญได้รับการเข้ารหัสหรือไม่"),
     ("Is there data loss prevention (DLP) or control over USB storage?", "มีระบบป้องกันข้อมูลรั่วไหล (DLP) หรือการควบคุมอุปกรณ์ USB หรือไม่")],
    ("Encryption standard, encryption status report, DLP policy", "มาตรฐานการเข้ารหัส รายงานสถานะการเข้ารหัส นโยบาย DLP"))
add("PR.DS-02", "ITM",
    ("How is data protected while it moves across networks, including email and file transfers?",
     "ปกป้องข้อมูลระหว่างการส่งผ่านเครือข่ายอย่างไร รวมถึงอีเมลและการโอนไฟล์"),
    [("Is TLS enforced on websites, APIs, and email?", "บังคับใช้ TLS กับเว็บไซต์ API และอีเมลหรือไม่"),
     ("How do staff send sensitive files to external parties?", "พนักงานส่งไฟล์สำคัญให้บุคคลภายนอกอย่างไร")],
    ("Cryptography standard, TLS configuration, secure file transfer tool", "มาตรฐานการเข้ารหัสลับ การตั้งค่า TLS เครื่องมือโอนไฟล์อย่างปลอดภัย"))
add("PR.DS-10", "ITM DEV",
    ("How is data protected while in use, for example on screens, in memory, and in shared sessions?",
     "ปกป้องข้อมูลขณะใช้งานอย่างไร เช่น บนหน้าจอ ในหน่วยความจำ และในเซสชันที่ใช้ร่วมกัน"),
    [("Are screen locks and session timeouts enforced?", "บังคับใช้การล็อกหน้าจอและการหมดเวลาเซสชันหรือไม่"),
     ("Is sensitive data masked in applications and reports?", "มีการปิดบังข้อมูลสำคัญในระบบงานและรายงานหรือไม่")],
    ("Endpoint configuration baseline, application masking rules", "ค่ามาตรฐานการตั้งค่าเครื่องลูกข่าย กฎการปิดบังข้อมูลในระบบงาน"))
add("PR.DS-11", "ITM BCM",
    ("How are backups created, protected from tampering or ransomware, and tested by restoring?",
     "สร้าง ปกป้องจากการดัดแปลงหรือแรนซัมแวร์ และทดสอบการกู้คืนข้อมูลสำรองอย่างไร"),
    [("Is there an offline or immutable backup copy?", "มีสำเนาข้อมูลสำรองแบบออฟไลน์หรือแก้ไขไม่ได้หรือไม่"),
     ("When was the last full restore test of a critical system, and did it meet the RTO?", "ทดสอบกู้คืนระบบสำคัญเต็มรูปแบบครั้งล่าสุดเมื่อใด และเป็นไปตาม RTO หรือไม่")],
    ("Backup standard, backup job reports, restore test records", "มาตรฐานการสำรองข้อมูล รายงานงานสำรองข้อมูล บันทึกการทดสอบกู้คืน"))

# PR.PS Platform Security
add("PR.PS-01", "ITM",
    ("Are secure configuration baselines defined and applied to servers, endpoints, network devices, and cloud?",
     "มีการกำหนดและใช้ค่ามาตรฐานการตั้งค่าที่ปลอดภัยกับเซิร์ฟเวอร์ เครื่องลูกข่าย อุปกรณ์เครือข่าย และคลาวด์หรือไม่"),
    [("Which benchmark is used, such as CIS Benchmarks?", "ใช้เกณฑ์อ้างอิงใด เช่น CIS Benchmarks"),
     ("How is configuration drift detected?", "ตรวจพบการตั้งค่าที่เบี่ยงเบนไปจากมาตรฐานอย่างไร")],
    ("Hardening standard, configuration compliance report", "มาตรฐานการตั้งค่าความปลอดภัย รายงานการปฏิบัติตามการตั้งค่า"))
add("PR.PS-02", "ITM SYSOWN",
    ("How is software patched, upgraded, and removed based on risk?",
     "แพตช์ อัปเกรด และถอนการติดตั้งซอฟต์แวร์ตามระดับความเสี่ยงอย่างไร"),
    [("What is the patch timeline for critical vulnerabilities, and what is the current compliance rate?", "กำหนดเวลาแพตช์ช่องโหว่ระดับวิกฤตคือเท่าใด และอัตราการปฏิบัติตามปัจจุบันเป็นเท่าใด"),
     ("Which unsupported operating systems or applications are still in use?", "ยังใช้ระบบปฏิบัติการหรือระบบงานที่หมดการสนับสนุนใดอยู่บ้าง")],
    ("Patch management procedure, patch compliance report, end-of-support list", "ขั้นตอนบริหารแพตช์ รายงานการแพตช์ รายการซอฟต์แวร์หมดการสนับสนุน"))
add("PR.PS-03", "ITM FAC",
    ("How is hardware maintained, replaced, and removed based on risk?",
     "บำรุงรักษา เปลี่ยน และปลดระวางฮาร์ดแวร์ตามระดับความเสี่ยงอย่างไร"),
    [("Is firmware updated on network devices and servers?", "มีการปรับปรุงเฟิร์มแวร์ของอุปกรณ์เครือข่ายและเซิร์ฟเวอร์หรือไม่"),
     ("Is there a hardware refresh plan for devices past vendor support?", "มีแผนทดแทนฮาร์ดแวร์ที่หมดการสนับสนุนจากผู้ขายหรือไม่")],
    ("Maintenance contracts, firmware records, refresh plan", "สัญญาบำรุงรักษา บันทึกเฟิร์มแวร์ แผนทดแทนอุปกรณ์"))
add("PR.PS-04", "ITM SOC",
    ("Which systems generate security logs, and are the logs centralized and retained?",
     "ระบบใดสร้างบันทึกด้านความมั่นคงปลอดภัย และบันทึกถูกรวมศูนย์และเก็บรักษาไว้หรือไม่"),
    [("Are logs kept at least 90 days as required by the Computer Crime Act s.26 where it applies?", "เก็บบันทึกอย่างน้อย 90 วันตาม พ.ร.บ.คอมพิวเตอร์ฯ มาตรา 26 ในกรณีที่ใช้บังคับหรือไม่"),
     ("Are logs protected from change or deletion?", "บันทึกได้รับการปกป้องจากการแก้ไขหรือลบหรือไม่")],
    ("Logging standard, log source list, SIEM retention settings", "มาตรฐานการบันทึก รายการแหล่งบันทึก การตั้งค่าการเก็บรักษาใน SIEM"))
add("PR.PS-05", "ITM",
    ("How is installation and execution of unauthorized software prevented?",
     "ป้องกันการติดตั้งและเรียกใช้ซอฟต์แวร์ที่ไม่ได้รับอนุญาตอย่างไร"),
    [("Do standard users have local administrator rights?", "ผู้ใช้ทั่วไปมีสิทธิ์ผู้ดูแลเครื่องหรือไม่"),
     ("Is application allowlisting or endpoint detection and response (EDR) used?", "ใช้การอนุญาตเฉพาะโปรแกรมที่กำหนดหรือระบบตรวจจับและตอบสนองที่เครื่องลูกข่าย (EDR) หรือไม่")],
    ("Endpoint policy, local admin report, EDR coverage", "นโยบายเครื่องลูกข่าย รายงานสิทธิ์ผู้ดูแลเครื่อง ความครอบคลุม EDR"))
add("PR.PS-06", "DEV CISO",
    ("Are secure software development practices built into in-house and outsourced development?",
     "มีการนำแนวปฏิบัติการพัฒนาซอฟต์แวร์อย่างปลอดภัยมาใช้กับการพัฒนาภายในและการจ้างพัฒนาหรือไม่"),
    [("Is code reviewed or scanned for security issues before release?", "มีการทบทวนหรือสแกนโค้ดหาปัญหาความมั่นคงปลอดภัยก่อนเผยแพร่หรือไม่"),
     ("Are development, test, and production environments separated?", "แยกสภาพแวดล้อมการพัฒนา ทดสอบ และใช้งานจริงหรือไม่")],
    ("Secure development standard, code scan reports, release checklist", "มาตรฐานการพัฒนาอย่างปลอดภัย รายงานการสแกนโค้ด รายการตรวจสอบก่อนเผยแพร่"))

# PR.IR Technology Infrastructure Resilience
add("PR.IR-01", "ITM",
    ("How is the network protected from unauthorized access, for example with segmentation, firewalls, and remote access controls?",
     "ปกป้องเครือข่ายจากการเข้าถึงโดยไม่ได้รับอนุญาตอย่างไร เช่น การแบ่งส่วนเครือข่าย ไฟร์วอลล์ และการควบคุมการเข้าถึงระยะไกล"),
    [("Are critical systems, medical devices, or OT separated from the user network?", "ระบบสำคัญ อุปกรณ์การแพทย์ หรือ OT ถูกแยกจากเครือข่ายผู้ใช้หรือไม่"),
     ("When were firewall rules last reviewed?", "ทบทวนกฎไฟร์วอลล์ครั้งล่าสุดเมื่อใด")],
    ("Network security standard, segmentation design, firewall rule review", "มาตรฐานความมั่นคงปลอดภัยเครือข่าย การออกแบบการแบ่งส่วน ผลการทบทวนกฎไฟร์วอลล์"))
add("PR.IR-02", "FAC ITM",
    ("How are data centers and equipment rooms protected from fire, flood, power loss, and heat?",
     "ปกป้องศูนย์ข้อมูลและห้องอุปกรณ์จากไฟไหม้ น้ำท่วม ไฟฟ้าดับ และความร้อนอย่างไร"),
    [("Are UPS, generator, cooling, and fire suppression tested?", "มีการทดสอบ UPS เครื่องกำเนิดไฟฟ้า ระบบทำความเย็น และระบบดับเพลิงหรือไม่"),
     ("Is the server room monitored for temperature and water?", "ห้องเซิร์ฟเวอร์มีการเฝ้าระวังอุณหภูมิและน้ำรั่วหรือไม่")],
    ("Facility maintenance and test records", "บันทึกการบำรุงรักษาและทดสอบอาคารสถานที่"))
add("PR.IR-03", "ITM BCM",
    ("What redundancy and failover exist for critical systems to meet resilience requirements?",
     "มีระบบสำรองและการสลับการทำงานใดสำหรับระบบสำคัญเพื่อให้เป็นไปตามข้อกำหนดด้านความยืดหยุ่น"),
    [("Is there a disaster recovery site, and has failover been tested?", "มีศูนย์สำรองหรือไม่ และเคยทดสอบการสลับการทำงานหรือไม่"),
     ("Which single points of failure are known?", "ทราบจุดล้มเหลวเดี่ยวใดบ้าง")],
    ("DR architecture, failover test reports", "สถาปัตยกรรมการกู้คืน รายงานการทดสอบการสลับการทำงาน"))
add("PR.IR-04", "ITM",
    ("How is capacity monitored and planned so systems stay available?",
     "เฝ้าระวังและวางแผนขีดความสามารถอย่างไรเพื่อให้ระบบพร้อมใช้งาน"),
    [("Do you get alerts before storage, CPU, or bandwidth run out?", "ได้รับการแจ้งเตือนก่อนพื้นที่จัดเก็บ CPU หรือแบนด์วิดท์เต็มหรือไม่"),
     ("Is there protection against denial-of-service (DoS) attacks for internet services?", "มีการป้องกันการโจมตีแบบปฏิเสธการให้บริการ (DoS) สำหรับบริการบนอินเทอร์เน็ตหรือไม่")],
    ("Capacity reports, monitoring dashboards", "รายงานขีดความสามารถ แดชบอร์ดการเฝ้าระวัง"))
