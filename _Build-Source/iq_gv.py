# -*- coding: utf-8 -*-
"""Interview question bank: Govern (GV). Each entry: r = interviewee role keys, q = main question, p = probes, e = evidence to request. All pairs are (EN, TH)."""
Q = {}
def add(sid, r, q, p, e):
    Q[sid] = dict(r=r.split(), q=list(q), p=[list(x) for x in p], e=list(e))

# GV.OC Organizational Context
add("GV.OC-01", "CEO CIO CISO",
    ("How does the organization's mission and business strategy shape what cybersecurity must protect first?",
     "พันธกิจและกลยุทธ์ธุรกิจขององค์กรกำหนดว่าด้านไซเบอร์ต้องปกป้องอะไรก่อนอย่างไร"),
    [("Can you name the three services whose disruption would hurt the business most?", "ระบุบริการ 3 อันดับแรกที่หากหยุดชะงักจะกระทบธุรกิจมากที่สุดได้หรือไม่"),
     ("Is cybersecurity mentioned in the corporate strategy or annual plan?", "แผนกลยุทธ์หรือแผนประจำปีขององค์กรกล่าวถึงด้านไซเบอร์หรือไม่")],
    ("Corporate strategy or annual plan, governance charter, cybersecurity strategy", "แผนกลยุทธ์หรือแผนประจำปี กฎบัตรการกำกับดูแล ยุทธศาสตร์ด้านไซเบอร์"))
add("GV.OC-02", "CISO CIO COMMS",
    ("Who are the internal and external stakeholders with cybersecurity expectations of the organization, and how do you capture those expectations?",
     "ผู้มีส่วนได้ส่วนเสียภายในและภายนอกที่คาดหวังด้านไซเบอร์จากองค์กรคือใคร และองค์กรรวบรวมความคาดหวังเหล่านั้นอย่างไร"),
    [("Do customers, regulators, or partners send security questionnaires or requirements?", "ลูกค้า หน่วยงานกำกับ หรือคู่ค้าส่งแบบสอบถามหรือข้อกำหนดด้านความมั่นคงปลอดภัยมาหรือไม่"),
     ("Is there a list of stakeholders and their expectations that is reviewed?", "มีรายชื่อผู้มีส่วนได้ส่วนเสียและความคาดหวังที่ได้รับการทบทวนหรือไม่")],
    ("Stakeholder register, customer security requirements, regulator correspondence", "ทะเบียนผู้มีส่วนได้ส่วนเสีย ข้อกำหนดด้านความมั่นคงปลอดภัยจากลูกค้า หนังสือจากหน่วยงานกำกับ"))
add("GV.OC-03", "LEGAL DPO CISO",
    ("How does the organization identify and track legal, regulatory, and contractual cybersecurity requirements, such as the Cybersecurity Act, PDPA, and sector rules?",
     "องค์กรระบุและติดตามข้อกำหนดด้านไซเบอร์ตามกฎหมาย หน่วยงานกำกับ และสัญญา เช่น พ.ร.บ.ไซเบอร์ PDPA และกฎเฉพาะอุตสาหกรรม อย่างไร"),
    [("Is the organization designated as Critical Information Infrastructure (CII)? Who confirmed it?", "องค์กรเป็นหน่วยงานโครงสร้างพื้นฐานสำคัญทางสารสนเทศ (CII) หรือไม่ และใครเป็นผู้ยืนยัน"),
     ("Who updates the requirement list when a new notification is issued?", "เมื่อมีประกาศใหม่ ใครเป็นผู้ปรับปรุงรายการข้อกำหนด")],
    ("Legal and regulatory requirements register, compliance calendar, contract clauses", "ทะเบียนข้อกำหนดทางกฎหมาย ปฏิทินการปฏิบัติตามกฎหมาย ข้อสัญญา"))
add("GV.OC-04", "CEO BCM SYSOWN",
    ("Which services do customers, patients, or partners depend on, and what availability or recovery commitments have you made to them?",
     "ลูกค้า ผู้รับบริการ หรือคู่ค้าพึ่งพาบริการใดขององค์กร และองค์กรให้คำมั่นเรื่องความพร้อมใช้งานหรือการกู้คืนไว้อย่างไร"),
    [("Are service level agreements (SLA) or recovery time objectives (RTO) defined for these services?", "มีการกำหนดข้อตกลงระดับบริการ (SLA) หรือเวลาเป้าหมายในการกู้คืน (RTO) สำหรับบริการเหล่านี้หรือไม่"),
     ("Was a Business Impact Analysis (BIA) performed?", "มีการวิเคราะห์ผลกระทบทางธุรกิจ (BIA) หรือไม่")],
    ("Service catalog, SLA, Business Impact Analysis report", "แคตตาล็อกบริการ SLA รายงานการวิเคราะห์ผลกระทบทางธุรกิจ"))
add("GV.OC-05", "CIO BCM PROC",
    ("Which external services, suppliers, and internal capabilities does the organization depend on to operate?",
     "องค์กรต้องพึ่งพาบริการภายนอก ผู้ให้บริการ และขีดความสามารถภายในใดบ้างเพื่อดำเนินงาน"),
    [("What happens if your cloud, internet, or key software provider is unavailable for a day?", "หากผู้ให้บริการคลาวด์ อินเทอร์เน็ต หรือซอฟต์แวร์หลักใช้งานไม่ได้หนึ่งวันจะเกิดอะไรขึ้น"),
     ("Are these dependencies recorded and linked to critical services?", "การพึ่งพาเหล่านี้ถูกบันทึกและเชื่อมโยงกับบริการสำคัญหรือไม่")],
    ("Dependency map, BIA, supplier inventory", "แผนผังการพึ่งพา BIA ทะเบียนผู้ให้บริการ"))

# GV.RM Risk Management Strategy
add("GV.RM-01", "CRO CISO CEO",
    ("What are the organization's cybersecurity risk management objectives, and who agreed to them?",
     "วัตถุประสงค์การบริหารความเสี่ยงด้านไซเบอร์ขององค์กรคืออะไร และใครเป็นผู้เห็นชอบ"),
    [("Are the objectives measurable and reviewed each year?", "วัตถุประสงค์วัดผลได้และได้รับการทบทวนทุกปีหรือไม่"),
     ("Did executive management or the board approve them?", "ผู้บริหารระดับสูงหรือคณะกรรมการอนุมัติหรือไม่")],
    ("Risk management framework or policy, approved objectives, meeting minutes", "กรอบหรือนโยบายการบริหารความเสี่ยง วัตถุประสงค์ที่ได้รับอนุมัติ รายงานการประชุม"))
add("GV.RM-02", "CRO CEO BOARD",
    ("Has management defined how much cybersecurity risk the organization is willing to accept, and how is that communicated?",
     "ผู้บริหารได้กำหนดระดับความเสี่ยงด้านไซเบอร์ที่องค์กรยอมรับได้หรือไม่ และสื่อสารอย่างไร"),
    [("Can you give an example of a risk that was rejected or accepted because of the appetite?", "ยกตัวอย่างความเสี่ยงที่ถูกปฏิเสธหรือยอมรับเพราะระดับความเสี่ยงที่ยอมรับได้ได้หรือไม่"),
     ("Are tolerance thresholds stated in numbers, such as maximum downtime or data loss?", "มีการกำหนดค่าเบี่ยงเบนที่ยอมรับได้เป็นตัวเลข เช่น เวลาหยุดระบบหรือการสูญหายข้อมูลสูงสุด หรือไม่")],
    ("Risk appetite statement, board resolution, risk tolerance thresholds", "แถลงการณ์ระดับความเสี่ยงที่ยอมรับได้ มติคณะกรรมการ เกณฑ์ค่าเบี่ยงเบน"))
add("GV.RM-03", "CRO CISO IA",
    ("How are cybersecurity risks included in the enterprise risk management (ERM) process and register?",
     "ความเสี่ยงด้านไซเบอร์ถูกรวมอยู่ในกระบวนการและทะเบียนการบริหารความเสี่ยงองค์กร (ERM) อย่างไร"),
    [("Does the enterprise risk register contain cybersecurity risks with owners?", "ทะเบียนความเสี่ยงองค์กรมีความเสี่ยงด้านไซเบอร์พร้อมเจ้าของหรือไม่"),
     ("Does the risk committee discuss cybersecurity risks regularly?", "คณะกรรมการความเสี่ยงพิจารณาความเสี่ยงด้านไซเบอร์อย่างสม่ำเสมอหรือไม่")],
    ("Enterprise risk register, risk committee minutes", "ทะเบียนความเสี่ยงองค์กร รายงานการประชุมคณะกรรมการความเสี่ยง"))
add("GV.RM-04", "CRO CISO",
    ("What direction has management given on risk response options: mitigate, transfer, avoid, or accept, and who can accept risk?",
     "ผู้บริหารให้แนวทางเรื่องทางเลือกการตอบสนองความเสี่ยง คือ ลด โอน หลีกเลี่ยง หรือยอมรับ ไว้อย่างไร และใครมีอำนาจยอมรับความเสี่ยง"),
    [("Is there a risk acceptance authority matrix?", "มีตารางอำนาจการยอมรับความเสี่ยงหรือไม่"),
     ("Does the organization use cyber insurance?", "องค์กรใช้ประกันภัยไซเบอร์หรือไม่")],
    ("Risk treatment guideline, risk acceptance forms, insurance policy", "แนวทางการจัดการความเสี่ยง แบบฟอร์มการยอมรับความเสี่ยง กรมธรรม์ประกันภัย"))
add("GV.RM-05", "CISO CRO PROC",
    ("How do cybersecurity risks, including supplier risks, get reported upward and across departments?",
     "ความเสี่ยงด้านไซเบอร์ รวมถึงความเสี่ยงจากผู้ให้บริการ ถูกรายงานขึ้นไปยังผู้บริหารและข้ามหน่วยงานอย่างไร"),
    [("Who would you tell if you found a serious risk today, and how fast?", "หากพบความเสี่ยงร้ายแรงวันนี้ คุณจะแจ้งใครและภายในเวลาเท่าใด"),
     ("Is the escalation path written down?", "เส้นทางการยกระดับเป็นลายลักษณ์อักษรหรือไม่")],
    ("Escalation matrix, risk reporting procedure, recent risk reports", "ตารางการยกระดับ ขั้นตอนการรายงานความเสี่ยง รายงานความเสี่ยงล่าสุด"))
add("GV.RM-06", "CRO CISO",
    ("What method does the organization use to rate, document, and prioritize cybersecurity risks?",
     "องค์กรใช้วิธีใดในการให้คะแนน บันทึก และจัดลำดับความสำคัญของความเสี่ยงด้านไซเบอร์"),
    [("Are likelihood and impact criteria defined and the same as the ERM criteria?", "มีการกำหนดเกณฑ์โอกาสและผลกระทบ และสอดคล้องกับเกณฑ์ของ ERM หรือไม่"),
     ("Do two assessors get the same score for the same risk?", "ผู้ประเมินสองคนให้คะแนนความเสี่ยงเดียวกันได้ผลเท่ากันหรือไม่")],
    ("Risk assessment methodology, risk matrix, sample completed assessment", "ระเบียบวิธีการประเมินความเสี่ยง ตารางความเสี่ยง ตัวอย่างผลการประเมิน"))
add("GV.RM-07", "CEO CIO CISO",
    ("Does the organization discuss positive risks, such as new technology or digital services, when making cybersecurity decisions?",
     "องค์กรพิจารณาความเสี่ยงเชิงบวก เช่น เทคโนโลยีหรือบริการดิจิทัลใหม่ ในการตัดสินใจด้านไซเบอร์หรือไม่"),
    [("Can you give an example where security enabled a business opportunity?", "ยกตัวอย่างกรณีที่ความมั่นคงปลอดภัยช่วยเปิดโอกาสทางธุรกิจได้หรือไม่"),
     ("Are opportunities recorded alongside risks?", "มีการบันทึกโอกาสควบคู่กับความเสี่ยงหรือไม่")],
    ("Risk register with opportunities, project business cases", "ทะเบียนความเสี่ยงที่รวมโอกาส กรณีธุรกิจของโครงการ"))

# GV.RR Roles, Responsibilities, and Authorities
add("GV.RR-01", "CEO BOARD CISO",
    ("How does executive leadership show accountability for cybersecurity risk?",
     "ผู้บริหารระดับสูงแสดงความรับผิดชอบต่อความเสี่ยงด้านไซเบอร์อย่างไร"),
    [("How often does the board or executive committee receive a cybersecurity briefing?", "คณะกรรมการหรือคณะผู้บริหารได้รับรายงานด้านไซเบอร์บ่อยเพียงใด"),
     ("Has an executive sponsored a security initiative or message in the last year?", "ในปีที่ผ่านมามีผู้บริหารสนับสนุนโครงการหรือสื่อสารเรื่องความมั่นคงปลอดภัยหรือไม่")],
    ("Governance charter, board agenda and minutes, executive communications", "กฎบัตรการกำกับดูแล วาระและรายงานการประชุมคณะกรรมการ การสื่อสารของผู้บริหาร"))
add("GV.RR-02", "CISO CIO HR",
    ("Are cybersecurity roles, responsibilities, and authorities defined, communicated, and enforced?",
     "บทบาท ความรับผิดชอบ และอำนาจหน้าที่ด้านไซเบอร์ได้รับการกำหนด สื่อสาร และบังคับใช้หรือไม่"),
    [("Who is accountable for security decisions today, and does that person have authority to stop a risky change?", "ปัจจุบันใครรับผิดชอบการตัดสินใจด้านความมั่นคงปลอดภัย และมีอำนาจระงับการเปลี่ยนแปลงที่มีความเสี่ยงหรือไม่"),
     ("Is there a RACI (Responsible, Accountable, Consulted, Informed) matrix?", "มีตาราง RACI (ผู้ปฏิบัติ ผู้รับผิดชอบ ผู้ให้คำปรึกษา ผู้รับทราบ) หรือไม่")],
    ("Organization chart, RACI matrix, job descriptions, appointment orders", "แผนผังองค์กร ตาราง RACI คำบรรยายลักษณะงาน คำสั่งแต่งตั้ง"))
add("GV.RR-03", "CIO CFO CISO",
    ("How is the cybersecurity budget and headcount decided, and is it based on risk?",
     "งบประมาณและอัตรากำลังด้านไซเบอร์ถูกกำหนดอย่างไร และอ้างอิงความเสี่ยงหรือไม่"),
    [("What share of the IT budget goes to security?", "งบด้านความมั่นคงปลอดภัยคิดเป็นสัดส่วนเท่าใดของงบ IT"),
     ("Were any security requests rejected last year, and why?", "ปีที่ผ่านมามีคำขอด้านความมั่นคงปลอดภัยที่ถูกปฏิเสธหรือไม่ เพราะอะไร")],
    ("Security budget, business cases, staffing plan", "งบประมาณด้านความมั่นคงปลอดภัย กรณีธุรกิจ แผนอัตรากำลัง"))
add("GV.RR-04", "HR CISO",
    ("How is cybersecurity built into human resources practices: screening, onboarding, role changes, discipline, and exit?",
     "ด้านไซเบอร์ถูกรวมไว้ในงานทรัพยากรบุคคลอย่างไร ตั้งแต่การคัดกรอง การรับเข้า การเปลี่ยนตำแหน่ง การลงโทษ และการพ้นสภาพ"),
    [("Do employees sign confidentiality and acceptable use agreements?", "พนักงานลงนามข้อตกลงรักษาความลับและการใช้งานที่ยอมรับได้หรือไม่"),
     ("How quickly does HR notify IT when someone leaves?", "ฝ่ายทรัพยากรบุคคลแจ้ง IT เร็วเพียงใดเมื่อมีพนักงานลาออก"),
     ("Are background or reference checks done before hiring people for privileged or sensitive roles?", "มีการตรวจสอบประวัติหรือบุคคลอ้างอิงก่อนจ้างบุคลากรในตำแหน่งที่มีสิทธิ์สูงหรือเข้าถึงข้อมูลอ่อนไหวหรือไม่")],
    ("HR security procedure, signed NDAs, onboarding and exit checklists", "ขั้นตอนความมั่นคงปลอดภัยด้านบุคลากร NDA ที่ลงนามแล้ว รายการตรวจสอบการรับเข้าและพ้นสภาพ"))

# GV.PO Policy
add("GV.PO-01", "CISO CIO",
    ("Is there an approved cybersecurity policy, and how is it communicated and enforced?",
     "มีนโยบายด้านไซเบอร์ที่ได้รับอนุมัติหรือไม่ และสื่อสารและบังคับใช้อย่างไร"),
    [("Who approved the policy and when?", "ใครอนุมัตินโยบายและเมื่อใด"),
     ("How do you know staff have read it? What happens when someone violates it?", "รู้ได้อย่างไรว่าพนักงานได้อ่านแล้ว และเมื่อมีผู้ฝ่าฝืนจะเกิดอะไรขึ้น"),
     ("Do the policies cover new ways of working, such as generative AI tools and messaging apps that carry work data?", "นโยบายครอบคลุมรูปแบบการทำงานใหม่หรือไม่ เช่น เครื่องมือ Generative AI และแอปสนทนาที่ใช้ส่งข้อมูลงาน")],
    ("Approved information security policy, acknowledgment records, violation cases", "นโยบายความมั่นคงปลอดภัยสารสนเทศที่อนุมัติแล้ว บันทึกการรับทราบ กรณีการฝ่าฝืน"))
add("GV.PO-02", "CISO",
    ("How often is the policy reviewed, and what triggers an update?",
     "นโยบายได้รับการทบทวนบ่อยเพียงใด และอะไรเป็นเหตุให้ต้องปรับปรุง"),
    [("When was the last review, and what changed?", "ทบทวนครั้งล่าสุดเมื่อใด และมีอะไรเปลี่ยนแปลง"),
     ("Is there a policy exception process?", "มีกระบวนการขอยกเว้นนโยบายหรือไม่")],
    ("Revision history, review minutes, exception register", "ประวัติการแก้ไข รายงานการทบทวน ทะเบียนการยกเว้น"))

# GV.OV Oversight
add("GV.OV-01", "CEO ISSC CISO",
    ("How does management review the results of the cybersecurity risk strategy and adjust direction?",
     "ผู้บริหารทบทวนผลลัพธ์ของกลยุทธ์ความเสี่ยงด้านไซเบอร์และปรับทิศทางอย่างไร"),
    [("Is there a steering committee that meets regularly?", "มีคณะกรรมการกำกับที่ประชุมสม่ำเสมอหรือไม่"),
     ("Name one decision the committee made last year.", "ระบุการตัดสินใจหนึ่งเรื่องที่คณะกรรมการทำในปีที่ผ่านมา")],
    ("Steering committee minutes, strategy review report", "รายงานการประชุมคณะกรรมการกำกับ รายงานการทบทวนกลยุทธ์"))
add("GV.OV-02", "CISO CRO IA",
    ("Is the risk strategy reviewed to confirm it still covers current requirements and threats?",
     "มีการทบทวนกลยุทธ์ความเสี่ยงเพื่อยืนยันว่ายังครอบคลุมข้อกำหนดและภัยคุกคามปัจจุบันหรือไม่"),
    [("Did a recent incident, audit, or new law cause a change in strategy?", "เหตุการณ์ การตรวจสอบ หรือกฎหมายใหม่ล่าสุดทำให้กลยุทธ์เปลี่ยนหรือไม่"),
     ("Does internal audit review cybersecurity?", "ฝ่ายตรวจสอบภายในตรวจด้านไซเบอร์หรือไม่")],
    ("Strategy review record, internal audit reports", "บันทึกการทบทวนกลยุทธ์ รายงานการตรวจสอบภายใน"))
add("GV.OV-03", "CISO ISSC",
    ("How is cybersecurity performance measured and reported?",
     "วัดและรายงานผลการดำเนินงานด้านไซเบอร์อย่างไร"),
    [("Which key performance indicators (KPI) and key risk indicators (KRI) are tracked?", "ติดตามตัวชี้วัดผลการดำเนินงาน (KPI) และตัวชี้วัดความเสี่ยง (KRI) ใดบ้าง"),
     ("Who receives the report and what action follows?", "ใครได้รับรายงาน และมีการดำเนินการต่ออย่างไร")],
    ("KPI and KRI dashboard, management reports", "แดชบอร์ด KPI และ KRI รายงานต่อผู้บริหาร"))

# GV.SC Supply Chain
add("GV.SC-01", "CISO PROC",
    ("Does the organization have a defined program for managing cybersecurity risk from suppliers?",
     "องค์กรมีแผนงานที่กำหนดไว้สำหรับบริหารความเสี่ยงด้านไซเบอร์จากผู้ให้บริการหรือไม่"),
    [("Is there a supplier security policy or procedure?", "มีนโยบายหรือขั้นตอนด้านความมั่นคงปลอดภัยของผู้ให้บริการหรือไม่"),
     ("Who owns supplier risk: procurement, IT, or security?", "ใครเป็นเจ้าของความเสี่ยงผู้ให้บริการ จัดซื้อ IT หรือฝ่ายความมั่นคงปลอดภัย")],
    ("Supplier security policy, third-party risk procedure", "นโยบายความมั่นคงปลอดภัยของผู้ให้บริการ ขั้นตอนบริหารความเสี่ยงบุคคลที่สาม"))
add("GV.SC-02", "PROC CISO",
    ("Are cybersecurity roles and responsibilities agreed with suppliers and partners?",
     "มีการตกลงบทบาทและความรับผิดชอบด้านไซเบอร์กับผู้ให้บริการและคู่ค้าหรือไม่"),
    [("For cloud services, is the shared responsibility split documented?", "สำหรับบริการคลาวด์ มีการบันทึกการแบ่งความรับผิดชอบร่วมกันหรือไม่"),
     ("Is there a named security contact at each critical supplier?", "ผู้ให้บริการสำคัญแต่ละรายมีผู้ติดต่อด้านความมั่นคงปลอดภัยที่ระบุชื่อหรือไม่")],
    ("Contracts, responsibility matrix, supplier contact list", "สัญญา ตารางความรับผิดชอบ รายชื่อผู้ติดต่อของผู้ให้บริการ"))
add("GV.SC-03", "CRO CISO PROC",
    ("Are supplier risks included in the cybersecurity and enterprise risk registers?",
     "ความเสี่ยงจากผู้ให้บริการถูกรวมไว้ในทะเบียนความเสี่ยงด้านไซเบอร์และความเสี่ยงองค์กรหรือไม่"),
    [("Give an example of a supplier risk in the register.", "ยกตัวอย่างความเสี่ยงจากผู้ให้บริการที่อยู่ในทะเบียน"),
     ("Is supplier concentration risk considered?", "พิจารณาความเสี่ยงจากการพึ่งพาผู้ให้บริการรายเดียวหรือไม่")],
    ("Risk register entries for suppliers", "รายการความเสี่ยงผู้ให้บริการในทะเบียนความเสี่ยง"))
add("GV.SC-04", "PROC CISO ITM",
    ("Is there a complete list of suppliers, ranked by how critical they are?",
     "มีรายชื่อผู้ให้บริการครบถ้วน พร้อมจัดลำดับตามความสำคัญหรือไม่"),
    [("What criteria decide that a supplier is critical?", "ใช้เกณฑ์ใดตัดสินว่าผู้ให้บริการรายใดสำคัญ"),
     ("Which suppliers have remote access to your systems?", "ผู้ให้บริการรายใดมีสิทธิ์เข้าถึงระบบจากระยะไกล")],
    ("Supplier register with criticality tiers", "ทะเบียนผู้ให้บริการพร้อมระดับความสำคัญ"))
add("GV.SC-05", "PROC LEGAL CISO",
    ("Do supplier contracts include cybersecurity requirements?",
     "สัญญากับผู้ให้บริการมีข้อกำหนดด้านไซเบอร์หรือไม่"),
    [("Do contracts cover breach notification, right to audit, data protection, and subcontractors?", "สัญญาครอบคลุมการแจ้งเหตุละเมิด สิทธิ์ในการตรวจสอบ การคุ้มครองข้อมูล และผู้รับจ้างช่วงหรือไม่"),
     ("Is there a data processing agreement for suppliers that handle personal data?", "มีสัญญาประมวลผลข้อมูลกับผู้ให้บริการที่ประมวลผลข้อมูลส่วนบุคคลหรือไม่")],
    ("Contract security clause template, sample signed contracts, data processing agreements", "แม่แบบข้อสัญญาด้านความมั่นคงปลอดภัย ตัวอย่างสัญญาที่ลงนามแล้ว สัญญาประมวลผลข้อมูล"))
add("GV.SC-06", "PROC CISO",
    ("What security due diligence is done before selecting a new supplier?",
     "มีการตรวจสอบความมั่นคงปลอดภัยใดก่อนเลือกผู้ให้บริการรายใหม่"),
    [("Is a security questionnaire or certificate (such as ISO 27001 or SOC 2) required?", "กำหนดให้ตอบแบบสอบถามหรือแสดงใบรับรอง เช่น ISO 27001 หรือ SOC 2 หรือไม่"),
     ("Can security block a purchase?", "ฝ่ายความมั่นคงปลอดภัยระงับการจัดซื้อได้หรือไม่")],
    ("Supplier assessment questionnaire, completed due diligence records", "แบบประเมินผู้ให้บริการ บันทึกการตรวจสอบก่อนคัดเลือก"))
add("GV.SC-07", "PROC CISO",
    ("How are risks from existing suppliers assessed and monitored over time?",
     "ประเมินและติดตามความเสี่ยงจากผู้ให้บริการปัจจุบันอย่างต่อเนื่องอย่างไร"),
    [("When was the last reassessment of a critical supplier?", "ประเมินผู้ให้บริการสำคัญซ้ำครั้งล่าสุดเมื่อใด"),
     ("Are supplier findings tracked to closure?", "ข้อตรวจพบของผู้ให้บริการได้รับการติดตามจนปิดหรือไม่")],
    ("Periodic supplier assessments, supplier review minutes", "ผลการประเมินผู้ให้บริการตามรอบ รายงานการทบทวนผู้ให้บริการ"))
add("GV.SC-08", "CISO SOC PROC",
    ("Are critical suppliers included in incident response plans and exercises?",
     "ผู้ให้บริการสำคัญถูกรวมไว้ในแผนรับมือเหตุการณ์และการฝึกซ้อมหรือไม่"),
    [("Do you know who to call at each critical supplier during an incident at night?", "หากเกิดเหตุตอนกลางคืน ทราบหรือไม่ว่าต้องติดต่อใครที่ผู้ให้บริการสำคัญแต่ละราย"),
     ("Has a supplier joined a tabletop exercise?", "ผู้ให้บริการเคยเข้าร่วมการฝึกซ้อมบนโต๊ะหรือไม่")],
    ("Incident response plan supplier section, exercise reports", "ส่วนผู้ให้บริการในแผนรับมือเหตุการณ์ รายงานการฝึกซ้อม"))
add("GV.SC-09", "PROC ITM DEV",
    ("How are supply chain security practices applied across the life cycle of technology products and services?",
     "นำแนวปฏิบัติความมั่นคงปลอดภัยของห่วงโซ่อุปทานไปใช้ตลอดวงจรชีวิตของผลิตภัณฑ์และบริการเทคโนโลยีอย่างไร"),
    [("Do you track software components or vendor patch support?", "มีการติดตามส่วนประกอบซอฟต์แวร์หรือการสนับสนุนแพตช์จากผู้ขายหรือไม่"),
     ("Are supplier security commitments checked during the contract?", "มีการตรวจสอบคำมั่นด้านความมั่นคงปลอดภัยของผู้ให้บริการระหว่างสัญญาหรือไม่")],
    ("Supplier performance reviews, software bill of materials (SBOM) where available", "การทบทวนผลงานผู้ให้บริการ รายการส่วนประกอบซอฟต์แวร์ (SBOM) หากมี"))
add("GV.SC-10", "PROC ITM LEGAL",
    ("What happens to access and data when a supplier contract ends?",
     "เมื่อสัญญากับผู้ให้บริการสิ้นสุด สิทธิ์การเข้าถึงและข้อมูลได้รับการจัดการอย่างไร"),
    [("Is there an exit checklist that covers account removal and data return or deletion?", "มีรายการตรวจสอบเมื่อสิ้นสุดสัญญาที่ครอบคลุมการลบบัญชีและการคืนหรือลบข้อมูลหรือไม่"),
     ("Do you obtain a certificate of data destruction?", "ได้รับหนังสือรับรองการทำลายข้อมูลหรือไม่")],
    ("Supplier offboarding checklist, data destruction certificates", "รายการตรวจสอบการยุติผู้ให้บริการ หนังสือรับรองการทำลายข้อมูล"))
