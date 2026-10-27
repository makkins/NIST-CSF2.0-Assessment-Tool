# -*- coding: utf-8 -*-
"""NIST CSF 2.0 Tier Rubric, version 1.2 (source of truth: claude/csf-tier-rubric.md).
Category descriptors are practitioner judgment derived from the CSF 2.0 Tier characteristics (CSWP 29, SP 1302), not NIST text.
RUBRIC[category][tier] = [EN, TH]. Thai text is a working translation and needs native review."""

RUBRIC_VERSION = "1.2"

# Coverage-applicable Subcategories (rubric Section 6)
COVERAGE = ("ID.AM-01 ID.AM-02 ID.AM-03 ID.RA-01 PR.AA-01 PR.AA-03 PR.AA-05 PR.DS-01 PR.DS-02 PR.DS-11 PR.PS-01 PR.PS-02 "
            "PR.PS-03 PR.PS-04 PR.PS-05 PR.IR-01 DE.CM-01 DE.CM-03 DE.CM-06 DE.CM-09 RC.RP-03").split()

T0 = ["No practice exists, or nobody can describe one.", "ไม่มีการปฏิบัติ หรือไม่มีใครอธิบายได้"]

R = {
 "GV.OC": [
  ["Cybersecurity is discussed without reference to the mission, stakeholders, or legal duties. No record of requirements.", "พูดถึงความมั่นคงปลอดภัยโดยไม่เชื่อมกับพันธกิจ ผู้มีส่วนได้เสีย หรือหน้าที่ตามกฎหมาย ไม่มีการบันทึกข้อกำหนด"],
  ["Leadership knows key services, stakeholders, and legal duties (for example CII, PDPA). Some are written down but not maintained or used in decisions.", "ผู้บริหารรู้บริการหลัก ผู้มีส่วนได้เสีย และหน้าที่ตามกฎหมาย (เช่น CII, PDPA) มีบันทึกบางส่วนแต่ไม่ปรับปรุงและไม่ใช้ประกอบการตัดสินใจ"],
  ["Approved scope statement, legal and regulatory requirements register, and critical service and dependency list. Reviewed at least annually and on major change. Used to set priorities.", "มีขอบเขต ทะเบียนข้อกำหนดตามกฎหมายและหน่วยงานกำกับ และรายการบริการสำคัญกับการพึ่งพา ที่อนุมัติแล้ว ทบทวนอย่างน้อยปีละครั้งและเมื่อมีการเปลี่ยนแปลงสำคัญ และใช้กำหนดลำดับความสำคัญ"],
  ["Context is updated as business, threat, and regulatory changes occur. Stakeholder expectations are tracked and drive program changes.", "ปรับบริบทตามการเปลี่ยนแปลงของธุรกิจ ภัยคุกคาม และกฎหมาย ติดตามความคาดหวังของผู้มีส่วนได้เสียและใช้ปรับแผนงาน"]],
 "GV.RM": [
  ["No risk appetite or risk method. Risks are handled case by case.", "ไม่มีระดับความเสี่ยงที่ยอมรับได้และไม่มีวิธีบริหารความเสี่ยง จัดการเป็นรายกรณี"],
  ["Management accepts cybersecurity as a business risk. A risk method or appetite exists in draft or for IT only.", "ผู้บริหารยอมรับว่าความมั่นคงปลอดภัยเป็นความเสี่ยงทางธุรกิจ มีวิธีหรือระดับความเสี่ยงที่ยอมรับได้ในรูปแบบร่าง หรือใช้เฉพาะ IT"],
  ["Approved risk appetite and tolerance, one standard risk method, and cybersecurity risk in enterprise risk reporting. Applied consistently and reviewed annually.", "มีระดับความเสี่ยงที่ยอมรับได้ที่อนุมัติแล้ว วิธีประเมินความเสี่ยงมาตรฐานเดียว และรายงานความเสี่ยงไซเบอร์ในระดับองค์กร ใช้สม่ำเสมอและทบทวนทุกปี"],
  ["Appetite and method are adjusted from performance data and threat changes. Cyber risk is expressed in financial terms and used in investment decisions.", "ปรับระดับความเสี่ยงและวิธีการจากข้อมูลผลการดำเนินงานและภัยคุกคาม แสดงความเสี่ยงไซเบอร์เป็นตัวเงินและใช้ตัดสินใจลงทุน"]],
 "GV.RR": [
  ["Security duties fall on IT staff informally. No accountable executive.", "งานความมั่นคงปลอดภัยตกอยู่กับเจ้าหน้าที่ IT อย่างไม่เป็นทางการ ไม่มีผู้บริหารที่รับผิดชอบ"],
  ["A person holds security duties with management support, but authority, resources, and roles across departments are unclear.", "มีผู้รับผิดชอบงานความมั่นคงปลอดภัยและผู้บริหารสนับสนุน แต่อำนาจ ทรัพยากร และบทบาทข้ามหน่วยงานยังไม่ชัด"],
  ["Approved roles and RACI matrix, a named accountable executive, a defined reporting line, and a planned budget. HR practices include security. Reviewed annually.", "มีบทบาทและ RACI ที่อนุมัติแล้ว ผู้บริหารที่รับผิดชอบ สายการรายงาน และงบประมาณที่วางแผนไว้ งานบุคคลครอบคลุมเรื่องความมั่นคงปลอดภัย ทบทวนทุกปี"],
  ["Roles, staffing, and skills are adjusted from performance and workload data. Security accountability is part of leaders' performance goals.", "ปรับบทบาท กำลังคน และทักษะจากข้อมูลผลงานและภาระงาน ความรับผิดชอบด้านความมั่นคงปลอดภัยเป็นส่วนหนึ่งของเป้าหมายผลงานผู้บริหาร"]],
 "GV.PO": [
  ["No approved policy, or an outdated draft not communicated.", "ไม่มีนโยบายที่อนุมัติ หรือมีเพียงร่างเก่าที่ไม่ได้สื่อสาร"],
  ["A policy is approved but outdated, incomplete, or not communicated to all staff.", "มีนโยบายที่อนุมัติแล้ว แต่ล้าสมัย ไม่ครบ หรือไม่ได้สื่อสารให้พนักงานทุกคน"],
  ["An approved policy set aligned with the risk strategy, communicated, acknowledged, enforced, and reviewed at least annually. Exceptions are recorded.", "มีชุดนโยบายที่อนุมัติและสอดคล้องกับกลยุทธ์ความเสี่ยง สื่อสาร รับทราบ บังคับใช้ และทบทวนอย่างน้อยปีละครั้ง บันทึกการยกเว้น"],
  ["Policies change promptly after incidents, audit results, and threat changes. Policy compliance is measured.", "ปรับนโยบายทันทีหลังเกิดเหตุ ผลการตรวจสอบ และภัยคุกคามที่เปลี่ยนไป และวัดการปฏิบัติตามนโยบาย"]],
 "GV.OV": [
  ["Leadership receives no regular cybersecurity reporting.", "ผู้บริหารไม่ได้รับรายงานด้านความมั่นคงปลอดภัยเป็นประจำ"],
  ["Leadership receives occasional updates, usually after events. No review of strategy results.", "ผู้บริหารได้รับข้อมูลเป็นครั้งคราว มักหลังเกิดเหตุ ไม่มีการทบทวนผลของกลยุทธ์"],
  ["Scheduled reporting to a steering committee or board with defined metrics. Strategy and performance are reviewed at least annually and decisions are recorded.", "รายงานต่อคณะกรรมการตามรอบด้วยตัวชี้วัดที่กำหนด ทบทวนกลยุทธ์และผลการดำเนินงานอย่างน้อยปีละครั้งและบันทึกการตัดสินใจ"],
  ["Oversight uses trend metrics and independent assurance. Strategy changes based on results.", "การกำกับใช้แนวโน้มตัวชี้วัดและการตรวจสอบอิสระ และปรับกลยุทธ์ตามผลลัพธ์"]],
 "GV.SC": [
  ["Suppliers are selected and managed without security criteria.", "คัดเลือกและบริหารผู้ให้บริการโดยไม่มีเกณฑ์ด้านความมั่นคงปลอดภัย"],
  ["Security clauses or questionnaires are used for some suppliers, mostly at onboarding. No supplier criticality.", "ใช้ข้อสัญญาหรือแบบสอบถามด้านความมั่นคงปลอดภัยกับผู้ให้บริการบางราย ส่วนใหญ่ตอนเริ่มใช้ ไม่มีการจัดระดับความสำคัญ"],
  ["Supplier inventory with criticality. Security requirements in contracts with critical suppliers. Due diligence, monitoring, and offboarding run consistently. Supplier risk is in the risk register.", "มีทะเบียนผู้ให้บริการพร้อมระดับความสำคัญ มีข้อกำหนดในสัญญากับผู้ให้บริการสำคัญ ตรวจสอบก่อนใช้ ติดตาม และยุติบริการอย่างสม่ำเสมอ ความเสี่ยงอยู่ในทะเบียนความเสี่ยง"],
  ["Supplier risk is monitored continuously. Incident plans are coordinated with critical suppliers. The program changes based on supplier performance and incidents.", "ติดตามความเสี่ยงผู้ให้บริการต่อเนื่อง ประสานแผนรับมือเหตุการณ์กับผู้ให้บริการสำคัญ และปรับแผนงานตามผลงานและเหตุการณ์"]],
 "ID.AM": [
  ["No reliable inventory. Knowledge sits with individuals.", "ไม่มีทะเบียนที่เชื่อถือได้ ความรู้อยู่กับตัวบุคคล"],
  ["Inventories exist for some asset types or sites but are incomplete, unowned, or out of date.", "มีทะเบียนสำหรับบางประเภทหรือบางสถานที่ แต่ไม่ครบ ไม่มีเจ้าของ หรือไม่เป็นปัจจุบัน"],
  ["Inventories of hardware, software, services, data, and network flows with owners and criticality, covering all in-scope sites. Updated through change management and reconciled at least every six months.", "มีทะเบียนฮาร์ดแวร์ ซอฟต์แวร์ บริการ ข้อมูล และการไหลของเครือข่าย พร้อมเจ้าของและระดับความสำคัญ ครบทุกสถานที่ในขอบเขต ปรับผ่านการควบคุมการเปลี่ยนแปลงและกระทบยอดอย่างน้อยทุกหกเดือน"],
  ["Inventories update automatically in near real time. Discrepancies are detected and resolved. Criticality drives control selection.", "ทะเบียนปรับอัตโนมัติแบบเกือบทันที ตรวจพบและแก้ความคลาดเคลื่อน ระดับความสำคัญใช้กำหนดการควบคุม"]],
 "ID.RA": [
  ["Risks and vulnerabilities are found only after events or by vendors.", "พบความเสี่ยงและช่องโหว่หลังเกิดเหตุหรือเมื่อผู้ขายแจ้งเท่านั้น"],
  ["Vulnerability scans or risk assessments happen occasionally or for some systems. Results are not tracked to closure.", "สแกนช่องโหว่หรือประเมินความเสี่ยงเป็นครั้งคราวหรือบางระบบ ไม่ได้ติดตามผลจนปิด"],
  ["Scheduled risk assessments using the approved method. Vulnerability scanning of in-scope assets with remediation timelines. Threat information is used. The risk register is maintained and reviewed.", "ประเมินความเสี่ยงตามรอบด้วยวิธีที่อนุมัติ สแกนช่องโหว่ทรัพย์สินในขอบเขตพร้อมกำหนดเวลาแก้ไข ใช้ข้อมูลภัยคุกคาม ดูแลและทบทวนทะเบียนความเสี่ยง"],
  ["Threat and exposure data update risk scenarios continuously. The effectiveness of risk responses is measured.", "ใช้ข้อมูลภัยคุกคามและการเปิดเผยปรับสถานการณ์ความเสี่ยงต่อเนื่อง และวัดประสิทธิผลของการจัดการความเสี่ยง"]],
 "ID.IM": [
  ["Improvements are not recorded. Lessons from events are not captured.", "ไม่บันทึกการปรับปรุง ไม่เก็บบทเรียนจากเหตุการณ์"],
  ["Lessons learned or audit findings are recorded for some events, but follow-up is not tracked.", "บันทึกบทเรียนหรือข้อตรวจพบบางเหตุการณ์ แต่ไม่ติดตามผล"],
  ["An improvement register fed by assessments, audits, exercises, and incidents. Corrective actions are owned and tracked to closure. Exercises are planned annually.", "มีทะเบียนการปรับปรุงจากการประเมิน การตรวจสอบ การซ้อม และเหตุการณ์ มีเจ้าของและติดตามจนปิด วางแผนการซ้อมทุกปี"],
  ["Improvement is continuous and data-driven. The effect of each change is verified.", "ปรับปรุงต่อเนื่องด้วยข้อมูล และตรวจสอบผลของทุกการเปลี่ยนแปลง"]],
 "PR.AA": [
  ["Accounts are created and removed on request. Shared accounts are common and multi-factor authentication (MFA) is absent.", "สร้างและลบบัญชีตามคำขอ ใช้บัญชีร่วมกันทั่วไป และไม่มี MFA"],
  ["Identity and access practices are approved and applied to some systems. MFA or access reviews are partial.", "แนวปฏิบัติด้านตัวตนและสิทธิ์ได้รับอนุมัติและใช้กับบางระบบ MFA หรือการทบทวนสิทธิ์ยังไม่ครบ"],
  ["An identity and authentication standard is enforced across in-scope systems. MFA covers remote, privileged, and critical access. Joiner, mover, and leaver steps are linked to HR. Privileged accounts are limited and logged. Access is reviewed at defined intervals.", "บังคับใช้มาตรฐานตัวตนและการยืนยันตัวตนทุกระบบในขอบเขต MFA ครอบคลุมการเข้าถึงระยะไกล สิทธิ์สูง และระบบสำคัญ การเข้า ย้าย ออกเชื่อมกับ HR จำกัดและบันทึกบัญชีสิทธิ์สูง และทบทวนสิทธิ์ตามรอบ"],
  ["Access decisions are risk-based (conditional access, just-in-time privilege). Access anomalies are detected automatically. Review results drive role redesign.", "ตัดสินใจให้สิทธิ์ตามความเสี่ยง (Conditional access, Just-in-time privilege) ตรวจจับความผิดปกติอัตโนมัติ และใช้ผลทบทวนออกแบบบทบาทใหม่"]],
 "PR.AT": [
  ["No structured awareness training.", "ไม่มีการอบรมสร้างความตระหนักอย่างเป็นระบบ"],
  ["Training happens at onboarding or occasionally. No role-based content or completion tracking.", "อบรมตอนเริ่มงานหรือเป็นครั้งคราว ไม่มีเนื้อหาตามบทบาทและไม่ติดตามการเข้าอบรม"],
  ["An annual awareness program for all staff with completion tracking. Role-based training for privileged users, developers, and executives. Phishing exercises.", "มีโปรแกรมสร้างความตระหนักประจำปีสำหรับทุกคนพร้อมติดตามผล อบรมตามบทบาทสำหรับผู้มีสิทธิ์สูง นักพัฒนา และผู้บริหาร และมีการทดสอบฟิชชิง"],
  ["Training changes based on phishing results, incidents, and behavior metrics. Behavior change is measured.", "ปรับการอบรมตามผลฟิชชิง เหตุการณ์ และตัวชี้วัดพฤติกรรม และวัดการเปลี่ยนพฤติกรรม"]],
 "PR.DS": [
  ["Data protection depends on individual practice. Backups are irregular.", "การปกป้องข้อมูลขึ้นกับแต่ละบุคคล สำรองข้อมูลไม่สม่ำเสมอ"],
  ["Encryption and backups cover some systems. Data classification is not defined or not applied.", "การเข้ารหัสและสำรองข้อมูลครอบคลุมบางระบบ ไม่มีหรือไม่ได้ใช้การจัดชั้นข้อมูล"],
  ["Data classification is applied. Sensitive data is encrypted at rest and in transit. Backups have an offline or immutable copy and restores are tested at defined intervals across in-scope systems.", "ใช้การจัดชั้นข้อมูล เข้ารหัสข้อมูลอ่อนไหวขณะจัดเก็บและส่งผ่าน มีสำเนาสำรองแบบ Offline หรือ Immutable และทดสอบกู้คืนตามรอบทุกระบบในขอบเขต"],
  ["Data protection controls are monitored and tuned, for example data loss prevention (DLP). Backup and restore performance is measured against recovery objectives.", "เฝ้าระวังและปรับการควบคุมการปกป้องข้อมูล เช่น DLP และวัดผลการสำรองและกู้คืนเทียบกับเป้าหมายการกู้คืน"]],
 "PR.PS": [
  ["Systems are configured and patched case by case. Unsupported software is common.", "ตั้งค่าและแพตช์ระบบเป็นรายกรณี มีซอฟต์แวร์ที่หมดการสนับสนุนจำนวนมาก"],
  ["Baselines or patching exist for some platforms. Logging and software control are partial.", "มี Baseline หรือการแพตช์บางแพลตฟอร์ม การบันทึกและการควบคุมซอฟต์แวร์ยังไม่ครบ"],
  ["Secure configuration baselines, patching within defined timelines, end-of-life management, log generation, and software control apply to in-scope platforms. In-house software follows secure development. Compliance is checked.", "ใช้ Secure configuration baseline แพตช์ตามกำหนดเวลา จัดการระบบหมดอายุ สร้างบันทึก และควบคุมซอฟต์แวร์ทุกแพลตฟอร์มในขอบเขต ซอฟต์แวร์ที่พัฒนาเองใช้การพัฒนาที่ปลอดภัย และตรวจการปฏิบัติตาม"],
  ["Configuration drift and patch compliance are monitored automatically. Exceptions are risk-assessed and time-bound.", "เฝ้าระวังการเบี่ยงเบนของการตั้งค่าและการแพตช์อัตโนมัติ ข้อยกเว้นมีการประเมินความเสี่ยงและมีกำหนดเวลา"]],
 "PR.IR": [
  ["The network is largely flat. No resilience planning for capacity or environmental threats.", "เครือข่ายส่วนใหญ่ไม่แบ่งส่วน ไม่มีแผนรองรับด้านความจุหรือภัยด้านสิ่งแวดล้อม"],
  ["Some segmentation and resilience measures exist but are not based on risk or not documented.", "มีการแบ่งส่วนเครือข่ายและมาตรการรองรับบางส่วน แต่ไม่ได้อิงความเสี่ยงหรือไม่มีเอกสาร"],
  ["The network is segmented by risk with filtered access. Resilience mechanisms meet agreed recovery needs for critical services. Capacity and environmental protection are reviewed.", "แบ่งส่วนเครือข่ายตามความเสี่ยงและกรองการเข้าถึง กลไกรองรับตอบสนองความต้องการกู้คืนของบริการสำคัญ ทบทวนความจุและการป้องกันด้านสิ่งแวดล้อม"],
  ["Architecture changes based on threat and performance data. Resilience is tested regularly under realistic conditions.", "ปรับสถาปัตยกรรมจากข้อมูลภัยคุกคามและผลการทำงาน ทดสอบความทนทานสม่ำเสมอในสภาพใกล้เคียงจริง"]],
 "DE.CM": [
  ["Monitoring happens only when users report problems.", "เฝ้าระวังเฉพาะเมื่อผู้ใช้แจ้งปัญหา"],
  ["Some logs or antimalware alerts are collected. Review is irregular or limited to some systems.", "เก็บบันทึกหรือการแจ้งเตือนจาก Antimalware บางส่วน ตรวจดูไม่สม่ำเสมอหรือบางระบบ"],
  ["Networks, endpoints, user activity, and service providers are monitored for in-scope assets through central logging or a security operations function, with defined review and escalation.", "เฝ้าระวังเครือข่าย เครื่องลูกข่าย กิจกรรมผู้ใช้ และผู้ให้บริการของทรัพย์สินในขอบเขต ผ่านระบบบันทึกส่วนกลางหรือหน่วยปฏิบัติการด้านความมั่นคงปลอดภัย พร้อมขั้นตอนตรวจดูและยกระดับ"],
  ["Monitoring is tuned continuously from threat information and incidents. Monitoring coverage is measured.", "ปรับการเฝ้าระวังต่อเนื่องจากข้อมูลภัยคุกคามและเหตุการณ์ และวัดความครอบคลุม"]],
 "DE.AE": [
  ["Alerts are not analyzed. Users notice events first.", "ไม่วิเคราะห์การแจ้งเตือน ผู้ใช้พบเหตุการณ์ก่อน"],
  ["IT staff analyze some alerts when time allows. No criteria to declare an incident.", "เจ้าหน้าที่ IT วิเคราะห์การแจ้งเตือนบางรายการเมื่อมีเวลา ไม่มีเกณฑ์ประกาศเหตุการณ์"],
  ["A defined triage and correlation process with detection use cases. Incident declaration criteria exist. Events are analyzed within defined times.", "มีกระบวนการคัดกรองและเชื่อมโยงพร้อม Use case การตรวจจับ มีเกณฑ์ประกาศเหตุการณ์ และวิเคราะห์ภายในเวลาที่กำหนด"],
  ["Analysis is automated and enriched with threat information. Use cases improve from lessons learned.", "วิเคราะห์อัตโนมัติและเสริมด้วยข้อมูลภัยคุกคาม ปรับ Use case จากบทเรียน"]],
 "RS.MA": [
  ["Incidents are handled ad hoc by whoever is available.", "จัดการเหตุการณ์เฉพาะหน้าโดยใครก็ได้ที่ว่าง"],
  ["An incident response plan exists but is untested or unknown to some responders. Contacts are partly defined.", "มีแผนรับมือเหตุการณ์ แต่ยังไม่ทดสอบหรือผู้รับมือบางคนไม่รู้จัก รายชื่อผู้ติดต่อยังไม่ครบ"],
  ["An approved incident response plan and playbooks for priority scenarios. Roles and contacts are current. The plan is exercised at least annually. Incidents are recorded.", "มีแผนรับมือเหตุการณ์ที่อนุมัติและ Playbook สำหรับสถานการณ์สำคัญ บทบาทและผู้ติดต่อเป็นปัจจุบัน ซ้อมอย่างน้อยปีละครั้ง และบันทึกเหตุการณ์"],
  ["The plan changes based on exercises and incidents. Response performance is measured. Coordination with external parties is practiced.", "ปรับแผนจากการซ้อมและเหตุการณ์ วัดผลการรับมือ และฝึกประสานกับหน่วยงานภายนอก"]],
 "RS.AN": [
  ["No investigation beyond restoring service.", "ไม่มีการสืบสวนนอกจากกู้บริการ"],
  ["Basic investigation for some incidents. Evidence is not preserved consistently.", "สืบสวนเบื้องต้นบางเหตุการณ์ เก็บรักษาหลักฐานไม่สม่ำเสมอ"],
  ["Investigations establish root cause and scope. Evidence is collected and preserved. Incidents are categorized and prioritized by defined criteria.", "สืบสวนหาสาเหตุและขอบเขต เก็บและรักษาหลักฐาน จัดประเภทและลำดับความสำคัญตามเกณฑ์"],
  ["Forensic capability (in-house or retained) is used routinely. Findings feed detection and prevention.", "ใช้ขีดความสามารถด้านนิติวิทยาศาสตร์ดิจิทัล (ภายในหรือจ้างไว้) เป็นปกติ และนำผลไปปรับการตรวจจับและป้องกัน"]],
 "RS.CO": [
  ["Notification is decided case by case. Regulatory duties are unclear.", "ตัดสินใจแจ้งเหตุเป็นรายกรณี หน้าที่ตามกฎหมายไม่ชัด"],
  ["Some notification steps are known. Regulatory timelines (CII, PDPA) are not built into procedures.", "รู้ขั้นตอนแจ้งเหตุบางส่วน กรอบเวลาตามกฎหมาย (CII, PDPA) ยังไม่อยู่ในขั้นตอน"],
  ["Internal and external notification procedures include regulatory timelines and templates. Communication roles are defined and followed in exercises and incidents.", "ขั้นตอนแจ้งเหตุภายในและภายนอกมีกรอบเวลาตามกฎหมายและแบบฟอร์ม กำหนดบทบาทการสื่อสารและปฏิบัติจริงในการซ้อมและเหตุการณ์"],
  ["Communication is tested with stakeholders and regulators. Messages and timelines improve from experience.", "ทดสอบการสื่อสารกับผู้มีส่วนได้เสียและหน่วยงานกำกับ ปรับข้อความและกรอบเวลาจากประสบการณ์"]],
 "RS.MI": [
  ["Containment is improvised.", "ควบคุมเหตุการณ์แบบเฉพาะหน้า"],
  ["Containment steps are known for common cases but not documented or rehearsed.", "รู้ขั้นตอนควบคุมสำหรับกรณีทั่วไป แต่ไม่มีเอกสารหรือไม่ได้ซ้อม"],
  ["Playbooks document containment and eradication steps. Authority to isolate systems is defined. Newly found vulnerabilities are mitigated or recorded as accepted risk.", "Playbook ระบุขั้นตอนควบคุมและกำจัด กำหนดอำนาจตัดระบบ ช่องโหว่ใหม่ได้รับการแก้ไขหรือบันทึกเป็นความเสี่ยงที่ยอมรับ"],
  ["Containment is partly automated. Its effectiveness is measured.", "การควบคุมเป็นอัตโนมัติบางส่วน และวัดประสิทธิผล"]],
 "RC.RP": [
  ["Recovery depends on individual knowledge. No recovery plan.", "การกู้คืนขึ้นกับความรู้ของบุคคล ไม่มีแผนกู้คืน"],
  ["Recovery plans exist for some systems. Recovery objectives are not agreed or not tested.", "มีแผนกู้คืนบางระบบ เป้าหมายการกู้คืนยังไม่ตกลงหรือไม่ได้ทดสอบ"],
  ["The recovery plan follows Business Impact Analysis (BIA) recovery objectives. Restore order is defined. Backup integrity is checked before restore. Recovery is tested at least annually.", "แผนกู้คืนเป็นไปตามเป้าหมายจาก BIA กำหนดลำดับการกู้คืน ตรวจความถูกต้องของข้อมูลสำรองก่อนกู้คืน และทดสอบอย่างน้อยปีละครั้ง"],
  ["Recovery capability is measured against objectives. Plans improve from tests and incidents.", "วัดขีดความสามารถการกู้คืนเทียบกับเป้าหมาย และปรับแผนจากการทดสอบและเหตุการณ์"]],
 "RC.CO": [
  ["Recovery status is communicated informally.", "สื่อสารสถานะการกู้คืนอย่างไม่เป็นทางการ"],
  ["Some stakeholders are informed during recovery. No defined process.", "แจ้งผู้มีส่วนได้เสียบางส่วนระหว่างกู้คืน ไม่มีกระบวนการกำหนดไว้"],
  ["Recovery communication to internal and external stakeholders follows a defined process, including public statements through approved channels. Tested in exercises.", "สื่อสารการกู้คืนกับผู้มีส่วนได้เสียภายในและภายนอกตามกระบวนการ รวมถึงแถลงต่อสาธารณะผ่านช่องทางที่อนุมัติ และทดสอบในการซ้อม"],
  ["Communication improves from exercises, incidents, and stakeholder feedback.", "ปรับการสื่อสารจากการซ้อม เหตุการณ์ และความเห็นของผู้มีส่วนได้เสีย"]],
}
RUBRIC = {c: {"0": T0, "1": v[0], "2": v[1], "3": v[2], "4": v[3]} for c, v in R.items()}
