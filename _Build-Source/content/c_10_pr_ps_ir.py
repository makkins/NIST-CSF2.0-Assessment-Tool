# -*- coding: utf-8 -*-
# PR.PS Platform Security; PR.IR Technology Infrastructure Resilience
C = {}

C["PR-STD-010"] = dict(
 purpose=("This standard requires every system to be built and kept to an approved secure configuration baseline, and defines how baselines are set, applied, and checked (PR.PS-01).",
          "มาตรฐานนี้กำหนดให้ทุกระบบต้องติดตั้งและคงการตั้งค่าตามมาตรฐานการตั้งค่าที่มั่นคงปลอดภัยที่อนุมัติ และกำหนดวิธีการกำหนด ใช้ และตรวจสอบมาตรฐานการตั้งค่า (PR.PS-01)"),
 sections=[
  ("Requirements", "ข้อกำหนด", "Set measurable configuration management requirements.", "กำหนดข้อกำหนดการบริหารการตั้งค่าที่วัดผลได้",
   {"t": ["ID", "Requirement"], "r": [
     ["CF-01", "Baselines exist for each platform (Windows, Linux, network devices, databases, cloud services), based on CIS Benchmarks Level 1 or vendor hardening guides."],
     ["CF-02", "New systems are built from approved images or templates that apply the baseline."],
     ["CF-03", "Unnecessary services, ports, accounts, and software are removed or disabled."],
     ["CF-04", "Configuration compliance is scanned at least monthly; deviations are fixed or approved as exceptions."],
     ["CF-05", "Baseline changes follow the Change Management Procedure (PR-PRC-006)."],
     ["CF-06", "Baselines are reviewed annually and when vendors release major versions."]], "w": [1.6, 14.9]},
   {"t": ["รหัส", "ข้อกำหนด"], "r": [
     ["CF-01", "มีมาตรฐานการตั้งค่าสำหรับแต่ละแพลตฟอร์ม (Windows, Linux อุปกรณ์เครือข่าย ฐานข้อมูล บริการคลาวด์) โดยอ้างอิง CIS Benchmarks ระดับ 1 หรือแนวทางเสริมความแข็งแรงของผู้ผลิต"],
     ["CF-02", "ติดตั้งระบบใหม่จาก Image หรือ Template ที่อนุมัติซึ่งตั้งค่าตามมาตรฐานแล้ว"],
     ["CF-03", "ลบหรือปิดบริการ พอร์ต บัญชี และซอฟต์แวร์ที่ไม่จำเป็น"],
     ["CF-04", "สแกนการปฏิบัติตามมาตรฐานการตั้งค่าอย่างน้อยทุกเดือน และแก้ไขส่วนที่เบี่ยงเบนหรือขออนุมัติเป็นข้อยกเว้น"],
     ["CF-05", "การเปลี่ยนแปลงมาตรฐานการตั้งค่าต้องผ่านระเบียบปฏิบัติการบริหารการเปลี่ยนแปลง (PR-PRC-006)"],
     ["CF-06", "ทบทวนมาตรฐานการตั้งค่าทุกปี และเมื่อผู้ผลิตออกรุ่นหลักใหม่"]], "w": [1.6, 14.9]}),
 ],
 bp=[("Automate baseline enforcement with group policy, configuration management tools, or cloud policies.", "บังคับใช้มาตรฐานการตั้งค่าโดยอัตโนมัติผ่าน Group policy เครื่องมือบริหารการตั้งค่า หรือนโยบายบนคลาวด์"),
     ("Test baselines on clinical or production applications before broad rollout.", "ทดสอบมาตรฐานการตั้งค่ากับแอปพลิเคชันคลินิกหรือแอปพลิเคชันใช้งานจริงก่อนขยายผล")],
 mistakes=[("Applying CIS Level 2 settings everywhere without testing, breaking applications.", "ใช้การตั้งค่า CIS ระดับ 2 กับทุกระบบโดยไม่ทดสอบ ทำให้แอปพลิเคชันใช้งานไม่ได้")],
)

C["PR-PRC-006"] = dict(
 purpose=("This procedure controls changes to systems and infrastructure so that changes are assessed for risk, approved, tested, recorded, and reversible (PR.PS-01, ID.RA-07).",
          "ระเบียบปฏิบัตินี้ควบคุมการเปลี่ยนแปลงระบบและโครงสร้างพื้นฐาน เพื่อให้การเปลี่ยนแปลงได้รับการประเมินความเสี่ยง อนุมัติ ทดสอบ บันทึก และย้อนกลับได้ (PR.PS-01, ID.RA-07)"),
 sections=[
  ("Change Types", "ประเภทการเปลี่ยนแปลง", "Define change categories and approval paths.", "กำหนดประเภทการเปลี่ยนแปลงและเส้นทางการอนุมัติ",
   {"t": ["Type", "Definition", "Approval"], "r": [
     ["Standard", "Pre-approved, low-risk, repeatable", "Pre-approved template"], ["Normal", "Assessed case by case", "Change advisory board (CAB)"],
     ["Emergency", "Needed urgently to restore service or fix a critical vulnerability", "Emergency CAB (two approvers); retrospective review within 5 working days"]], "w": [3.0, 7.0, 6.5]},
   {"t": ["ประเภท", "คำนิยาม", "การอนุมัติ"], "r": [
     ["มาตรฐาน (Standard)", "อนุมัติล่วงหน้า ความเสี่ยงต่ำ ทำซ้ำได้", "แม่แบบที่อนุมัติล่วงหน้า"], ["ปกติ (Normal)", "ประเมินเป็นรายกรณี", "คณะกรรมการพิจารณาการเปลี่ยนแปลง (CAB)"],
     ["ฉุกเฉิน (Emergency)", "จำเป็นเร่งด่วนเพื่อกู้บริการหรือแก้ไขช่องโหว่วิกฤต", "CAB ฉุกเฉิน (ผู้อนุมัติ 2 คน) และทบทวนย้อนหลังภายใน 5 วันทำการ"]], "w": [3.0, 7.0, 6.5]}),
  ("Process Steps", "ขั้นตอนการดำเนินงาน", "Describe steps from request to closure.", "อธิบายขั้นตอนตั้งแต่ยื่นคำขอจนปิดงาน",
   {"n": ["Submit the Change Request Form (PR-FRM-005) with description, risk, test, and rollback plans.", "Assess security impact; the [CISO] reviews changes to security controls, internet exposure, or critical systems.",
          "Approve at CAB; schedule outside peak hours for critical systems.", "Test in a non-production environment where possible.", "Implement, verify, and update the inventory and diagrams.", "Close the change; review failed changes."]},
   {"n": ["ยื่นแบบฟอร์มขอเปลี่ยนแปลงระบบ (PR-FRM-005) พร้อมรายละเอียด ความเสี่ยง แผนการทดสอบ และแผนย้อนกลับ", "ประเมินผลกระทบด้านความมั่นคงปลอดภัย โดย [CISO] ทบทวนการเปลี่ยนแปลงที่เกี่ยวกับมาตรการควบคุม การเปิดสู่อินเทอร์เน็ต หรือระบบสำคัญ",
          "อนุมัติโดย CAB และกำหนดเวลานอกช่วงเร่งด่วนสำหรับระบบสำคัญ", "ทดสอบในสภาพแวดล้อมที่ไม่ใช่ระบบจริงเมื่อทำได้", "ดำเนินการ ตรวจสอบผล และปรับปรุงทะเบียนทรัพย์สินและแผนภาพ", "ปิดงาน และทบทวนการเปลี่ยนแปลงที่ล้มเหลว"]}),
 ],
 bp=[("Detect unauthorized changes with configuration monitoring and compare against approved changes.", "ตรวจจับการเปลี่ยนแปลงที่ไม่ได้รับอนุญาตด้วยการเฝ้าระวังการตั้งค่า และเปรียบเทียบกับการเปลี่ยนแปลงที่อนุมัติ"),
     ("Include the security team as a standing CAB member.", "ให้ทีมความมั่นคงปลอดภัยเป็นสมาชิกประจำของ CAB")],
 mistakes=[("Emergency changes become the normal route to avoid CAB.", "ใช้การเปลี่ยนแปลงฉุกเฉินเป็นช่องทางปกติเพื่อเลี่ยง CAB")],
)

C["PR-FRM-005"] = dict(
 purpose=("This form requests, assesses, and approves a change to a system or infrastructure.", "แบบฟอร์มนี้ใช้ขอ ประเมิน และอนุมัติการเปลี่ยนแปลงระบบหรือโครงสร้างพื้นฐาน"),
 fields=[
  ("Change number and type", "เลขที่และประเภทการเปลี่ยนแปลง", "Standard, Normal, Emergency.", "มาตรฐาน ปกติ ฉุกเฉิน", "CHG-2026-0001, Normal"),
  ("Systems affected", "ระบบที่ได้รับผลกระทบ", "Asset IDs and services.", "รหัสทรัพย์สินและบริการ", ""),
  ("Description and reason", "รายละเอียดและเหตุผล", "What and why.", "สิ่งที่เปลี่ยนแปลงและเหตุผล", ""),
  ("Risk and security impact", "ความเสี่ยงและผลกระทบด้านความมั่นคงปลอดภัย", "Effect on controls, exposure, data.", "ผลต่อมาตรการควบคุม การเปิดเผยต่อภายนอก และข้อมูล", ""),
  ("Test plan and result", "แผนและผลการทดสอบ", "Where and how tested.", "สถานที่และวิธีทดสอบ", ""),
  ("Rollback plan", "แผนย้อนกลับ", "How to reverse.", "วิธีย้อนกลับ", ""),
  ("Schedule and downtime", "กำหนดการและระยะเวลาหยุดระบบ", "Window and user impact.", "ช่วงเวลาและผลกระทบต่อผู้ใช้", ""),
  ("Implementation result", "ผลการดำเนินการ", "Successful, failed, rolled back.", "สำเร็จ ล้มเหลว ย้อนกลับ", ""),
 ],
 cmc_vals=["CHG-2026-0612, Normal", "PACS-APP01, PACS-APP02; diagnostic imaging", "Apply PACS minor version upgrade from Vendor B to fix security vulnerabilities and a viewer bug",
           "Fixes two High vulnerabilities; vendor remote access needed (TRA-2026-0207); no change to data flows", "Tested on PACS test server 7 September 2026; radiologists confirmed viewer function",
           "Restore application server snapshots taken before the change; database unchanged", "14 September 2026 22:00 to 15 September 2026 04:00; read-only PACS mode for 30 minutes; Radiology informed",
           "Successful; completed 01:40; post-change scan clean"],
 approvals=["Requester", "SYSOWN", "CISO", "CIO"],
 bp=[("Make security impact a mandatory field so reviewers cannot skip it.", "กำหนดให้ผลกระทบด้านความมั่นคงปลอดภัยเป็นหัวข้อบังคับ เพื่อไม่ให้ผู้ทบทวนข้ามได้")],
 mistakes=[("Rollback plan stated as 'restore if needed' with no tested steps.", "ระบุแผนย้อนกลับเพียงว่าจะกู้คืนหากจำเป็น โดยไม่มีขั้นตอนที่ทดสอบแล้ว")],
)

C["PR-PRC-007"] = dict(
 purpose=("This procedure ensures that security updates for operating systems, applications, firmware, and devices are evaluated, tested, deployed, and verified within the timelines in ID-STD-002 (PR.PS-02, PR.PS-03).",
          "ระเบียบปฏิบัตินี้ทำให้การอัปเดตด้านความมั่นคงปลอดภัยของระบบปฏิบัติการ แอปพลิเคชัน เฟิร์มแวร์ และอุปกรณ์ได้รับการประเมิน ทดสอบ ติดตั้ง และตรวจสอบภายในกรอบเวลาที่กำหนดใน ID-STD-002 (PR.PS-02, PR.PS-03)"),
 sections=[
  ("Patch Cycle", "รอบการติดตั้งแพตช์", "Describe the monthly cycle and emergency path.", "อธิบายรอบรายเดือนและช่องทางฉุกเฉิน",
   {"t": ["Phase", "Activity", "Timing"], "r": [
     ["Identify", "Collect vendor releases and advisories; map to assets", "Release day"], ["Assess", "Prioritize by severity, exploitation, exposure, criticality", "Within 2 working days"],
     ["Test", "Deploy to a pilot group or test environment", "Within 5 working days"], ["Deploy", "Roll out in rings: pilot, general, critical systems in maintenance windows", "Per ID-STD-002 timelines"],
     ["Verify", "Confirm installation through endpoint management and rescans", "After each ring"], ["Emergency", "Known exploited critical vulnerability: emergency change, deploy within 48 hours for internet-facing systems", "As required"]], "w": [2.5, 9.5, 4.5]},
   {"t": ["ระยะ", "กิจกรรม", "ช่วงเวลา"], "r": [
     ["ระบุ", "รวบรวมการออกแพตช์และประกาศของผู้ขาย และเชื่อมโยงกับทรัพย์สิน", "วันที่ออกแพตช์"], ["ประเมิน", "จัดลำดับตามความรุนแรง การถูกโจมตีจริง การเปิดเผยต่อภายนอก และความสำคัญ", "ภายใน 2 วันทำการ"],
     ["ทดสอบ", "ติดตั้งกับกลุ่มนำร่องหรือสภาพแวดล้อมทดสอบ", "ภายใน 5 วันทำการ"], ["ติดตั้ง", "ทยอยติดตั้งเป็นวง ได้แก่ กลุ่มนำร่อง กลุ่มทั่วไป และระบบสำคัญในช่วงบำรุงรักษา", "ตามกรอบเวลาใน ID-STD-002"],
     ["ตรวจสอบ", "ยืนยันการติดตั้งผ่านระบบบริหารอุปกรณ์ปลายทางและการสแกนซ้ำ", "หลังแต่ละวง"], ["ฉุกเฉิน", "ช่องโหว่วิกฤตที่ถูกโจมตีจริง: ใช้การเปลี่ยนแปลงฉุกเฉิน และติดตั้งภายใน 48 ชั่วโมงสำหรับระบบที่เปิดสู่อินเทอร์เน็ต", "ตามความจำเป็น"]], "w": [2.5, 9.5, 4.5]}),
  ("Systems That Cannot Be Patched", "ระบบที่ติดตั้งแพตช์ไม่ได้", "State how unpatchable systems are handled.", "ระบุวิธีจัดการระบบที่ติดตั้งแพตช์ไม่ได้",
   "Where a vendor does not support a patch (for example, medical or OT devices), apply compensating controls such as network isolation, application allowlisting, and monitoring, and record an exception (GV-PRC-003).",
   "กรณีผู้ขายไม่รองรับแพตช์ (เช่น อุปกรณ์การแพทย์หรือ OT) ให้ใช้มาตรการชดเชย เช่น การแยกเครือข่าย การอนุญาตเฉพาะแอปพลิเคชันที่กำหนด และการเฝ้าระวัง และบันทึกข้อยกเว้น (GV-PRC-003)"),
 ],
 bp=[("Agree standing maintenance windows with business owners so critical systems are not skipped.", "ตกลงช่วงเวลาบำรุงรักษาประจำกับเจ้าของธุรกิจ เพื่อไม่ให้ระบบสำคัญถูกข้าม"),
     ("Patch third-party applications (browsers, PDF readers, Java), not only the operating system.", "ติดตั้งแพตช์แอปพลิเคชันของผู้ผลิตอื่น (เบราว์เซอร์ โปรแกรมอ่าน PDF Java) ไม่ใช่เฉพาะระบบปฏิบัติการ")],
 mistakes=[("Critical servers are excluded from patching 'because they are critical'.", "ไม่ติดตั้งแพตช์ให้เซิร์ฟเวอร์สำคัญเพราะเห็นว่าสำคัญเกินกว่าจะหยุดระบบ")],
)

C["PR-STD-011"] = dict(
 purpose=("This standard sets which events must be logged, how logs are protected, synchronized, retained, and forwarded for monitoring, including computer traffic data retention under the Computer Crime Act B.E. 2550 s.26 (PR.PS-04).",
          "มาตรฐานนี้กำหนดเหตุการณ์ที่ต้องบันทึก วิธีปกป้อง ปรับเวลาให้ตรงกัน เก็บรักษา และส่ง Log ไปเฝ้าระวัง รวมถึงการเก็บรักษาข้อมูลจราจรทางคอมพิวเตอร์ตาม พ.ร.บ.ว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. 2550 มาตรา 26 (PR.PS-04)"),
 sections=[
  ("Events to Log", "เหตุการณ์ที่ต้องบันทึก", "List minimum log events by source.", "ระบุเหตุการณ์ขั้นต่ำที่ต้องบันทึกตามแหล่งที่มา",
   {"t": ["Source", "Minimum events"], "r": [
     ["Identity systems", "Sign-in success and failure, MFA events, account and group changes, privilege changes"],
     ["Servers and endpoints", "Logons, process creation, service installation, security tool alerts, log clearing"],
     ["Network and security devices", "Allowed and denied connections at boundaries, VPN sessions, IPS and web proxy events"],
     ["Applications with sensitive data", "Access to records, exports, administrative actions, configuration changes"],
     ["Cloud services", "Administrative activity, sign-ins, sharing, API key use"],
     ["Internet access services for users (traffic data)", "Source, destination, time, duration, and identity where available (Computer Crime Act s.26)"]], "w": [5.0, 11.5]},
   {"t": ["แหล่งที่มา", "เหตุการณ์ขั้นต่ำ"], "r": [
     ["ระบบตัวตน", "การเข้าสู่ระบบสำเร็จและไม่สำเร็จ เหตุการณ์ MFA การเปลี่ยนแปลงบัญชีและกลุ่ม การเปลี่ยนแปลงสิทธิ์"],
     ["เซิร์ฟเวอร์และอุปกรณ์ปลายทาง", "การเข้าสู่ระบบ การสร้าง Process การติดตั้งบริการ การแจ้งเตือนจากเครื่องมือความมั่นคงปลอดภัย การลบ Log"],
     ["อุปกรณ์เครือข่ายและความมั่นคงปลอดภัย", "การเชื่อมต่อที่อนุญาตและปฏิเสธที่ขอบเครือข่าย เซสชัน VPN เหตุการณ์จาก IPS และ Web proxy"],
     ["แอปพลิเคชันที่มีข้อมูลอ่อนไหว", "การเข้าถึงข้อมูล การส่งออกข้อมูล การดำเนินการของผู้ดูแล การเปลี่ยนแปลงการตั้งค่า"],
     ["บริการคลาวด์", "กิจกรรมของผู้ดูแล การเข้าสู่ระบบ การแชร์ การใช้ API key"],
     ["บริการอินเทอร์เน็ตสำหรับผู้ใช้ (ข้อมูลจราจร)", "ต้นทาง ปลายทาง เวลา ระยะเวลา และตัวตนผู้ใช้เมื่อทำได้ (พ.ร.บ.คอมพิวเตอร์ฯ มาตรา 26)"]], "w": [5.0, 11.5]}),
  ("Protection, Time, and Retention", "การปกป้อง เวลา และการเก็บรักษา", "Set log protection, clock synchronization, and retention requirements.", "กำหนดข้อกำหนดการปกป้อง Log การปรับเวลาให้ตรงกัน และการเก็บรักษา",
   ["Forward logs to a central platform within 5 minutes; local logs are not the only copy.", "Restrict log access and prevent modification; alert on log clearing or forwarding failure.",
    "Synchronize all clocks to an approved time source (NTP) within 1 second (ISO/IEC 27001:2022 Annex A 8.17).",
    "Retain computer traffic data for at least 90 days where the organization acts as a service provider, and longer when officials request (Computer Crime Act B.E. 2550 s.26).", "Retain security logs for at least 1 year (online 90 days)."],
   ["ส่ง Log ไปยังระบบกลางภายใน 5 นาที และ Log ในเครื่องต้องไม่ใช่สำเนาเดียว", "จำกัดการเข้าถึง Log และป้องกันการแก้ไข แจ้งเตือนเมื่อมีการลบ Log หรือการส่ง Log ล้มเหลว",
    "ปรับเวลาของทุกระบบให้ตรงกับแหล่งเวลาที่อนุมัติ (NTP) คลาดเคลื่อนไม่เกิน 1 วินาที (ISO/IEC 27001:2022 Annex A 8.17)",
    "เก็บรักษาข้อมูลจราจรทางคอมพิวเตอร์อย่างน้อย 90 วันเมื่อองค์กรเป็นผู้ให้บริการ และนานกว่านั้นเมื่อพนักงานเจ้าหน้าที่ร้องขอ (พ.ร.บ.ว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. 2550 มาตรา 26)", "เก็บ Log ด้านความมั่นคงปลอดภัยอย่างน้อย 1 ปี (ออนไลน์ 90 วัน)"],
   ["Logs forwarded to the CMC log platform and on to the MSSP.", "Only the Security Manager and MSSP analysts can read the log platform; deletion disabled.",
    "All systems synchronize to the CMC NTP servers referenced to the national time source.", "Patient and guest Wi-Fi traffic data retained for 90 days as a service provider.", "Security logs kept 1 year online and 2 years in archive."]),
 ],
 bp=[("Prioritize log sources that help detect ransomware: identity, endpoint detection and response, VPN, and backup systems.", "ให้ความสำคัญกับแหล่ง Log ที่ช่วยตรวจจับแรนซัมแวร์ ได้แก่ ระบบตัวตน EDR VPN และระบบสำรองข้อมูล"),
     ("Confirm with Legal whether guest or patient Wi-Fi makes the organization a service provider under the Computer Crime Act.", "ยืนยันกับฝ่ายกฎหมายว่าการให้บริการ Wi-Fi แก่ผู้มาติดต่อหรือผู้ป่วยทำให้องค์กรเป็นผู้ให้บริการตาม พ.ร.บ.คอมพิวเตอร์ฯ หรือไม่")],
 mistakes=[("Logs kept only on the device, where attackers delete them.", "เก็บ Log ไว้บนอุปกรณ์เท่านั้น ซึ่งผู้โจมตีสามารถลบได้"),
           ("Clocks out of sync, which makes incident timelines unreliable.", "เวลาของระบบไม่ตรงกัน ทำให้ลำดับเหตุการณ์ในการสอบสวนไม่น่าเชื่อถือ")],
)

C["PR-STD-012"] = dict(
 purpose=("This standard sets requirements for protecting endpoints and servers against malware and unauthorized software (PR.PS-05, DE.CM-09).",
          "มาตรฐานนี้กำหนดข้อกำหนดในการปกป้องอุปกรณ์ปลายทางและเซิร์ฟเวอร์จากมัลแวร์และซอฟต์แวร์ที่ไม่ได้รับอนุญาต (PR.PS-05, DE.CM-09)"),
 sections=[
  ("Requirements", "ข้อกำหนด", "Set measurable endpoint protection requirements.", "กำหนดข้อกำหนดการป้องกันอุปกรณ์ปลายทางที่วัดผลได้",
   {"t": ["ID", "Requirement"], "r": [
     ["EP-01", "Endpoint detection and response (EDR) installed on all supported workstations and servers; coverage target 98%."],
     ["EP-02", "EDR tamper protection enabled; alerts sent to the [SOC]."],
     ["EP-03", "Standard users have no local administrator rights."],
     ["EP-04", "Only software in the Approved Software Register (PR-REG-003) may be installed; application allowlisting on servers and fixed-function devices."],
     ["EP-05", "Macros from the internet blocked; script execution restricted."],
     ["EP-06", "Removable media controlled according to PR-STD-004."],
     ["EP-07", "Full disk encryption on laptops."],
     ["EP-08", "Devices that cannot run EDR are isolated and covered by network monitoring under an approved exception."]], "w": [1.6, 14.9]},
   {"t": ["รหัส", "ข้อกำหนด"], "r": [
     ["EP-01", "ติดตั้ง EDR (Endpoint Detection and Response) บนเครื่องคอมพิวเตอร์และเซิร์ฟเวอร์ที่รองรับทั้งหมด เป้าหมายความครอบคลุม 98%"],
     ["EP-02", "เปิดการป้องกันการแก้ไข EDR และส่งการแจ้งเตือนไปยัง [SOC]"],
     ["EP-03", "ผู้ใช้ทั่วไปไม่มีสิทธิ์ผู้ดูแลระบบภายในเครื่อง"],
     ["EP-04", "ติดตั้งได้เฉพาะซอฟต์แวร์ในทะเบียนซอฟต์แวร์ที่อนุญาต (PR-REG-003) และใช้ Application allowlisting บนเซิร์ฟเวอร์และอุปกรณ์ที่ใช้งานเฉพาะ"],
     ["EP-05", "บล็อกแมโครจากอินเทอร์เน็ต และจำกัดการรันสคริปต์"],
     ["EP-06", "ควบคุมสื่อบันทึกข้อมูลแบบถอดได้ตาม PR-STD-004"],
     ["EP-07", "เข้ารหัสทั้งดิสก์บนโน้ตบุ๊ก"],
     ["EP-08", "อุปกรณ์ที่ติดตั้ง EDR ไม่ได้ต้องแยกเครือข่ายและเฝ้าระวังผ่านเครือข่าย ภายใต้ข้อยกเว้นที่อนุมัติ"]], "w": [1.6, 14.9]}),
 ],
 bp=[("Measure EDR coverage against the asset inventory weekly; gaps are where attackers hide.", "วัดความครอบคลุมของ EDR เทียบกับทะเบียนทรัพย์สินทุกสัปดาห์ เพราะช่องว่างคือที่ซ่อนของผู้โจมตี"),
     ("Remove local admin rights in phases with a self-service elevation option.", "ถอนสิทธิ์ผู้ดูแลภายในเครื่องเป็นระยะ พร้อมทางเลือกยกระดับสิทธิ์ด้วยตนเองที่มีการควบคุม")],
 mistakes=[("Antivirus installed but never monitored, so alerts go unseen.", "ติดตั้งโปรแกรมป้องกันไวรัสแต่ไม่มีการเฝ้าระวัง ทำให้ไม่มีใครเห็นการแจ้งเตือน")],
)

C["PR-REG-003"] = dict(
 purpose=("This register lists software approved for use, with version, owner, license, data classification limit, and conditions, to support allowlisting and prevent unauthorized software (PR.PS-05).",
          "ทะเบียนนี้ระบุซอฟต์แวร์ที่อนุญาตให้ใช้งาน พร้อมรุ่น เจ้าของ สิทธิ์การใช้งาน ระดับชั้นข้อมูลสูงสุดที่อนุญาต และเงื่อนไข เพื่อสนับสนุน Allowlisting และป้องกันซอฟต์แวร์ที่ไม่ได้รับอนุญาต (PR.PS-05)"),
 fields=[
  ("Software", "ซอฟต์แวร์", "Name and publisher.", "ชื่อและผู้ผลิต", ""),
  ("Approved versions", "รุ่นที่อนุมัติ", "Supported versions.", "รุ่นที่ได้รับการสนับสนุน", ""),
  ("Category", "ประเภท", "Business, utility, security, AI.", "ธุรกิจ เครื่องมือ ความมั่นคงปลอดภัย AI", ""),
  ("Owner", "เจ้าของ", "Business or IT owner.", "เจ้าของธุรกิจหรือ IT", ""),
  ("Max data class", "ชั้นข้อมูลสูงสุด", "Per PR-STD-004.", "ตาม PR-STD-004", ""),
  ("Conditions", "เงื่อนไข", "Restrictions on use.", "ข้อจำกัดการใช้งาน", ""),
  ("Approved by and date", "ผู้อนุมัติและวันที่", "Security review reference.", "เลขอ้างอิงการทบทวนด้านความมั่นคงปลอดภัย", ""),
 ],
 rows=[
  ["Microsoft 365 Apps", "Current channel", "Business", "CIO", "Restricted (with labels)", "Managed devices only for Restricted data", "Security Manager, 02/2025"],
  ["Microsoft 365 Copilot", "Tenant service", "AI", "CIO", "Internal; Restricted only in approved pilot", "Per GV-POL-005 and DPIA", "Security Manager and DPO, 07/2026"],
  ["PDF reader (enterprise edition)", "Latest", "Utility", "IT Service Desk Lead", "Confidential", "Auto-update enabled", "Security Manager, 03/2025"],
  ["DICOM viewer (Vendor B)", "8.x", "Clinical", "Director of Radiology", "Restricted", "Clinical workstations only", "Security Manager, 05/2025"],
  ["Remote support tool (vendor)", "Not approved", "Utility", "Not applicable", "Not applicable", "Prohibited; use PAM jump host", "Not approved, 08/2026"],
 ],
 bp=[("Publish the register to staff with a request route for new software.", "เผยแพร่ทะเบียนให้บุคลากรทราบ พร้อมช่องทางขออนุมัติซอฟต์แวร์ใหม่"),
     ("Use the register to drive allowlisting rules in endpoint tools.", "ใช้ทะเบียนเป็นฐานในการกำหนดกฎ Allowlisting ในเครื่องมือป้องกันอุปกรณ์ปลายทาง")],
 mistakes=[("Register exists on paper but endpoint tools still allow any installation.", "มีทะเบียนบนเอกสาร แต่เครื่องมือป้องกันอุปกรณ์ปลายทางยังอนุญาตให้ติดตั้งได้ทุกอย่าง")],
)

C["PR-STD-013"] = dict(
 purpose=("This standard sets secure software development requirements for in-house and outsourced development across the life cycle (PR.PS-06; NIST SP 800-218 Secure Software Development Framework).",
          "มาตรฐานนี้กำหนดข้อกำหนดการพัฒนาซอฟต์แวร์อย่างมั่นคงปลอดภัยสำหรับการพัฒนาภายในและการจ้างพัฒนาตลอดวงจรชีวิต (PR.PS-06; NIST SP 800-218 Secure Software Development Framework)"),
 sections=[
  ("Requirements by Phase", "ข้อกำหนดตามระยะ", "Set requirements for each development phase.", "กำหนดข้อกำหนดสำหรับแต่ละระยะของการพัฒนา",
   {"t": ["Phase", "Requirement"], "r": [
     ["Requirements", "Define security and privacy requirements, including authentication, logging, and data protection."],
     ["Design", "Perform threat modeling for systems handling Confidential or Restricted data."],
     ["Build", "Follow secure coding guidelines (OWASP); no secrets in source code; use approved libraries."],
     ["Verify", "Static analysis (SAST) and software composition analysis (SCA) in the pipeline; dynamic testing (DAST) before release; penetration test for critical apps."],
     ["Release", "Separate development, test, and production; production data not used in test unless masked (Annex A 8.31, 8.33)."],
     ["Maintain", "Fix vulnerabilities per ID-STD-002; monitor third-party components."],
     ["Outsourced", "Contracts require the same practices, code escrow or access, and vulnerability fix timelines (Annex A 8.30)."]], "w": [3.0, 13.5]},
   {"t": ["ระยะ", "ข้อกำหนด"], "r": [
     ["ความต้องการ", "กำหนดข้อกำหนดด้านความมั่นคงปลอดภัยและความเป็นส่วนตัว รวมถึงการยืนยันตัวตน การบันทึก Log และการปกป้องข้อมูล"],
     ["ออกแบบ", "วิเคราะห์ภัยคุกคาม (Threat modeling) สำหรับระบบที่จัดการข้อมูลระดับ Confidential หรือ Restricted"],
     ["พัฒนา", "ปฏิบัติตามแนวทางการเขียนโค้ดอย่างมั่นคงปลอดภัย (OWASP) ห้ามมีข้อมูลลับในซอร์สโค้ด และใช้ไลบรารีที่อนุมัติ"],
     ["ตรวจสอบ", "ใช้การวิเคราะห์โค้ดแบบ Static (SAST) และการวิเคราะห์ส่วนประกอบซอฟต์แวร์ (SCA) ใน Pipeline ทดสอบแบบ Dynamic (DAST) ก่อนเปิดใช้งาน และทดสอบเจาะระบบสำหรับแอปพลิเคชันสำคัญ"],
     ["เปิดใช้งาน", "แยกสภาพแวดล้อมพัฒนา ทดสอบ และใช้งานจริง ห้ามใช้ข้อมูลจริงในการทดสอบเว้นแต่ปกปิดข้อมูลแล้ว (Annex A 8.31, 8.33)"],
     ["บำรุงรักษา", "แก้ไขช่องโหว่ตาม ID-STD-002 และเฝ้าระวังส่วนประกอบจากภายนอก"],
     ["การจ้างพัฒนา", "สัญญากำหนดแนวปฏิบัติเดียวกัน การฝากหรือการเข้าถึงซอร์สโค้ด และกรอบเวลาการแก้ไขช่องโหว่ (Annex A 8.30)"]], "w": [3.0, 13.5]}),
 ],
 bp=[("Automate security tests in the CI/CD pipeline so they run on every change.", "ทำให้การทดสอบความมั่นคงปลอดภัยทำงานอัตโนมัติใน Pipeline CI/CD เพื่อให้ทดสอบทุกครั้งที่มีการเปลี่ยนแปลง"),
     ("Train developers on the vulnerabilities actually found in your code.", "อบรมนักพัฒนาเรื่องช่องโหว่ที่พบจริงในโค้ดขององค์กร")],
 mistakes=[("Copying production patient or customer data into test environments without masking.", "คัดลอกข้อมูลผู้ป่วยหรือลูกค้าจากระบบจริงไปยังสภาพแวดล้อมทดสอบโดยไม่ปกปิดข้อมูล")],
)

C["PR-STD-014"] = dict(
 purpose=("This standard sets security requirements for selecting, configuring, and operating cloud services (IaaS, PaaS, SaaS), based on the shared responsibility model (ISO/IEC 27001:2022 Annex A 5.23).",
          "มาตรฐานนี้กำหนดข้อกำหนดด้านความมั่นคงปลอดภัยในการเลือก ตั้งค่า และใช้งานบริการคลาวด์ (IaaS, PaaS, SaaS) ตามแนวคิดความรับผิดชอบร่วมกัน (ISO/IEC 27001:2022 Annex A 5.23)"),
 sections=[
  ("Requirements", "ข้อกำหนด", "Set cloud security requirements.", "กำหนดข้อกำหนดด้านความมั่นคงปลอดภัยบนคลาวด์",
   {"t": ["ID", "Requirement"], "r": [
     ["CL-01", "Every cloud service is approved through supplier assessment (GV-PRC-008) and recorded in ID-REG-002."],
     ["CL-02", "Document the shared responsibility split for each service."],
     ["CL-03", "Cloud administrators use SSO with phishing-resistant MFA; no root or global admin use for daily work."],
     ["CL-04", "Data location and cross-border transfer comply with the PDPA (s.28 and s.29) and contracts."],
     ["CL-05", "Encrypt data at rest and in transit; manage keys per PR-STD-005."],
     ["CL-06", "Enable cloud audit logging and forward logs to the monitoring platform."],
     ["CL-07", "Monitor cloud configuration continuously against secure baselines using automated configuration checks."],
     ["CL-08", "Back up SaaS data where the provider does not retain it sufficiently."],
     ["CL-09", "Plan exit: data export format and deletion at termination."],
     ["CL-10", "CII organizations confirm compliance with any NCSA or CRC cloud security requirements. [VERIFY]"]], "w": [1.6, 14.9]},
   {"t": ["รหัส", "ข้อกำหนด"], "r": [
     ["CL-01", "บริการคลาวด์ทุกบริการต้องผ่านการประเมินผู้ให้บริการ (GV-PRC-008) และบันทึกใน ID-REG-002"],
     ["CL-02", "ระบุการแบ่งความรับผิดชอบร่วมกันของแต่ละบริการเป็นลายลักษณ์อักษร"],
     ["CL-03", "ผู้ดูแลระบบคลาวด์ใช้ SSO และ MFA ที่ทนต่อฟิชชิ่ง และห้ามใช้บัญชี Root หรือ Global admin ในงานประจำวัน"],
     ["CL-04", "ที่ตั้งข้อมูลและการโอนข้อมูลข้ามประเทศเป็นไปตาม PDPA (มาตรา 28 และ 29) และสัญญา"],
     ["CL-05", "เข้ารหัสข้อมูลขณะจัดเก็บและขณะส่ง และบริหารกุญแจตาม PR-STD-005"],
     ["CL-06", "เปิดการบันทึก Log การตรวจสอบบนคลาวด์ และส่ง Log ไปยังระบบเฝ้าระวัง"],
     ["CL-07", "เฝ้าระวังการตั้งค่าคลาวด์อย่างต่อเนื่องเทียบกับมาตรฐานการตั้งค่า ด้วยการตรวจสอบการตั้งค่าอัตโนมัติ"],
     ["CL-08", "สำรองข้อมูลใน SaaS เมื่อผู้ให้บริการเก็บรักษาไม่เพียงพอ"],
     ["CL-09", "วางแผนการยุติบริการ ได้แก่ รูปแบบการส่งออกข้อมูลและการลบเมื่อสิ้นสุดสัญญา"],
     ["CL-10", "องค์กรที่เป็น CII ต้องยืนยันการปฏิบัติตามข้อกำหนดด้านความมั่นคงปลอดภัยของคลาวด์จาก สกมช. หรือ กกม. [VERIFY]"]], "w": [1.6, 14.9]}),
 ],
 bp=[("Use provider security benchmarks (for example, CIS Microsoft 365 Foundations Benchmark) as baselines.", "ใช้มาตรฐานการตั้งค่าของผู้ให้บริการหรือ CIS (เช่น CIS Microsoft 365 Foundations Benchmark) เป็นมาตรฐานการตั้งค่า"),
     ("Review external sharing settings in collaboration platforms quarterly.", "ทบทวนการตั้งค่าการแชร์ภายนอกในระบบทำงานร่วมกันทุกไตรมาส")],
 mistakes=[("Assuming the cloud provider is responsible for configuration and access.", "เข้าใจว่าผู้ให้บริการคลาวด์รับผิดชอบการตั้งค่าและการเข้าถึงแทนองค์กร")],
)

C["PR-STD-015"] = dict(
 purpose=("This standard sets security requirements for operational technology (OT) and connected medical devices, balancing safety, availability, and vendor support constraints (NIST SP 800-82 Rev. 3; IEC 80001-1).",
          "มาตรฐานนี้กำหนดข้อกำหนดด้านความมั่นคงปลอดภัยสำหรับเทคโนโลยีปฏิบัติการ (OT) และอุปกรณ์การแพทย์ที่เชื่อมต่อเครือข่าย โดยสมดุลระหว่างความปลอดภัย ความพร้อมใช้งาน และข้อจำกัดด้านการสนับสนุนของผู้ขาย (NIST SP 800-82 Rev. 3; IEC 80001-1)"),
 sections=[
  ("Requirements", "ข้อกำหนด", "Set OT and medical device security requirements.", "กำหนดข้อกำหนดด้านความมั่นคงปลอดภัยของ OT และอุปกรณ์การแพทย์",
   {"t": ["ID", "Requirement"], "r": [
     ["OT-01", "All connected devices are recorded in ID-REG-004 with manufacturer security information (for example, MDS2)."],
     ["OT-02", "Devices are placed in dedicated network segments with allow-only rules to the systems they need."],
     ["OT-03", "No direct internet access; vendor remote access only through the PAM jump host."],
     ["OT-04", "Patches are applied only when certified by the manufacturer; otherwise compensating controls and exceptions apply."],
     ["OT-05", "Default passwords changed; unused services and ports disabled where the manufacturer permits."],
     ["OT-06", "Passive network monitoring detects anomalies without disrupting devices."],
     ["OT-07", "New device purchases include security requirements (GV-STD-003)."],
     ["OT-08", "Clinical or operations staff and engineering jointly approve changes that affect device function."]], "w": [1.6, 14.9]},
   {"t": ["รหัส", "ข้อกำหนด"], "r": [
     ["OT-01", "บันทึกอุปกรณ์ที่เชื่อมต่อทั้งหมดใน ID-REG-004 พร้อมข้อมูลความมั่นคงปลอดภัยจากผู้ผลิต (เช่น MDS2)"],
     ["OT-02", "วางอุปกรณ์ในส่วนเครือข่ายเฉพาะ และอนุญาตเฉพาะการเชื่อมต่อไปยังระบบที่จำเป็น"],
     ["OT-03", "ห้ามเชื่อมต่ออินเทอร์เน็ตโดยตรง และการเข้าถึงระยะไกลของผู้ขายต้องผ่าน Jump host ของ PAM เท่านั้น"],
     ["OT-04", "ติดตั้งแพตช์เฉพาะที่ผู้ผลิตรับรอง หากไม่มีให้ใช้มาตรการชดเชยและข้อยกเว้น"],
     ["OT-05", "เปลี่ยนรหัสผ่านค่าเริ่มต้น และปิดบริการและพอร์ตที่ไม่ใช้ตามที่ผู้ผลิตอนุญาต"],
     ["OT-06", "ใช้การเฝ้าระวังเครือข่ายแบบ Passive เพื่อตรวจจับความผิดปกติโดยไม่รบกวนอุปกรณ์"],
     ["OT-07", "การจัดซื้ออุปกรณ์ใหม่ต้องมีข้อกำหนดด้านความมั่นคงปลอดภัย (GV-STD-003)"],
     ["OT-08", "บุคลากรด้านคลินิกหรือปฏิบัติการและฝ่ายวิศวกรรมต้องอนุมัติร่วมกันสำหรับการเปลี่ยนแปลงที่กระทบการทำงานของอุปกรณ์"]], "w": [1.6, 14.9]}),
 ],
 bp=[("Form a joint working group of IT, security, biomedical or plant engineering, and clinical or operations leads.", "จัดตั้งคณะทำงานร่วมระหว่าง IT ความมั่นคงปลอดภัย วิศวกรรมชีวการแพทย์หรือวิศวกรรมโรงงาน และผู้นำด้านคลินิกหรือปฏิบัติการ"),
     ("Prioritize segmentation; it protects devices that can never be patched.", "ให้ความสำคัญกับการแบ่งส่วนเครือข่าย เพราะช่วยปกป้องอุปกรณ์ที่ไม่สามารถติดตั้งแพตช์ได้")],
 mistakes=[("Running active vulnerability scans on infusion pumps or PLCs, causing device faults.", "สแกนช่องโหว่แบบ Active กับเครื่องให้สารละลายทางหลอดเลือดหรือ PLC ทำให้อุปกรณ์ขัดข้อง")],
)

C["PR-STD-016"] = dict(
 purpose=("This standard sets requirements for network segmentation, boundary protection, wireless, DNS, and web filtering to protect networks from unauthorized access (PR.IR-01).",
          "มาตรฐานนี้กำหนดข้อกำหนดด้านการแบ่งส่วนเครือข่าย การป้องกันขอบเครือข่าย เครือข่ายไร้สาย DNS และการกรองเว็บ เพื่อปกป้องเครือข่ายจากการเข้าถึงโดยไม่ได้รับอนุญาต (PR.IR-01)"),
 sections=[
  ("Requirements", "ข้อกำหนด", "Set measurable network security requirements.", "กำหนดข้อกำหนดด้านความมั่นคงปลอดภัยของเครือข่ายที่วัดผลได้",
   {"t": ["ID", "Requirement"], "r": [
     ["NW-01", "Segment the network into zones (ID-RPT-001); traffic between zones is denied by default and allowed by documented rules."],
     ["NW-02", "Internet-facing services sit in a DMZ behind a firewall and, for web, a web application firewall."],
     ["NW-03", "Management interfaces are reachable only from the management zone."],
     ["NW-04", "Wireless uses WPA2-Enterprise or WPA3 with directory authentication; guest Wi-Fi is isolated."],
     ["NW-05", "Network access control blocks unknown devices on wired ports in sensitive areas."],
     ["NW-06", "DNS filtering and web filtering block known malicious and high-risk categories."],
     ["NW-07", "Firewall rules are reviewed every six months; unused and overly broad rules are removed (PR-PRC-008)."],
     ["NW-08", "Email gateway filters malware and phishing and enforces SPF, DKIM, and DMARC."]], "w": [1.6, 14.9]},
   {"t": ["รหัส", "ข้อกำหนด"], "r": [
     ["NW-01", "แบ่งเครือข่ายเป็นโซน (ID-RPT-001) และปฏิเสธการเชื่อมต่อระหว่างโซนเป็นค่าเริ่มต้น โดยอนุญาตตามกฎที่บันทึกไว้"],
     ["NW-02", "บริการที่เปิดสู่อินเทอร์เน็ตอยู่ใน DMZ หลังไฟร์วอลล์ และใช้ Web application firewall สำหรับเว็บ"],
     ["NW-03", "เข้าถึงส่วนบริหารจัดการของอุปกรณ์ได้จากโซนบริหารจัดการเท่านั้น"],
     ["NW-04", "เครือข่ายไร้สายใช้ WPA2-Enterprise หรือ WPA3 พร้อมการยืนยันตัวตนผ่านไดเรกทอรี และแยก Wi-Fi ผู้มาติดต่อ"],
     ["NW-05", "ใช้ระบบควบคุมการเข้าถึงเครือข่ายบล็อกอุปกรณ์ที่ไม่รู้จักบนพอร์ตสายในพื้นที่อ่อนไหว"],
     ["NW-06", "ใช้การกรอง DNS และการกรองเว็บบล็อกหมวดหมู่ที่เป็นอันตรายและมีความเสี่ยงสูง"],
     ["NW-07", "ทบทวนกฎไฟร์วอลล์ทุก 6 เดือน และลบกฎที่ไม่ใช้หรือกว้างเกินไป (PR-PRC-008)"],
     ["NW-08", "เกตเวย์อีเมลกรองมัลแวร์และฟิชชิ่ง และบังคับใช้ SPF, DKIM และ DMARC"]], "w": [1.6, 14.9]}),
 ],
 bp=[("Segment to limit ransomware spread: separate user, server, management, backup, and device networks.", "แบ่งส่วนเครือข่ายเพื่อจำกัดการแพร่กระจายของแรนซัมแวร์ โดยแยกเครือข่ายผู้ใช้ เซิร์ฟเวอร์ บริหารจัดการ สำรองข้อมูล และอุปกรณ์"),
     ("Move DMARC policy to reject after monitoring.", "ปรับนโยบาย DMARC เป็น Reject หลังจากเฝ้าระวังแล้ว")],
 mistakes=[("Flat networks where any workstation can reach every server.", "เครือข่ายแบบแบนที่เครื่องผู้ใช้ใดก็เข้าถึงเซิร์ฟเวอร์ได้ทุกเครื่อง")],
)

C["PR-PRC-008"] = dict(
 purpose=("This procedure controls how firewall rules are requested, reviewed, implemented, and periodically recertified, to keep boundary controls tight (PR.IR-01).",
          "ระเบียบปฏิบัตินี้ควบคุมวิธีขอ ทบทวน ดำเนินการ และรับรองกฎไฟร์วอลล์ตามรอบ เพื่อให้การควบคุมขอบเครือข่ายรัดกุม (PR.IR-01)"),
 sections=[
  ("Process Steps", "ขั้นตอนการดำเนินงาน", "Describe steps for new rules and periodic review.", "อธิบายขั้นตอนสำหรับกฎใหม่และการทบทวนตามรอบ",
   {"t": ["Step", "Activity", "Actor"], "r": [
     ["1", "Submit the Firewall Rule Change Request (PR-FRM-006) with business owner and expiry", "Requester"],
     ["2", "Review for least privilege: specific source, destination, and port; no 'any' rules", "Network engineer"],
     ["3", "Security review for rules that expose services to the internet or cross critical zones", "[CISO]"],
     ["4", "Implement through change management with rule ID and comment", "Network engineer"],
     ["5", "Recertify all rules every six months with rule owners; remove unused or expired rules", "Network engineer, rule owners"]], "w": [1.2, 11.3, 4.0]},
   {"t": ["ขั้นตอน", "กิจกรรม", "ผู้ดำเนินการ"], "r": [
     ["1", "ยื่นแบบฟอร์มขอเปลี่ยนแปลงกฎไฟร์วอลล์ (PR-FRM-006) พร้อมเจ้าของธุรกิจและวันหมดอายุ", "ผู้ขอ"],
     ["2", "ทบทวนตามหลักสิทธิ์น้อยที่สุด ระบุต้นทาง ปลายทาง และพอร์ตเฉพาะ ห้ามใช้กฎแบบ Any", "วิศวกรเครือข่าย"],
     ["3", "ทบทวนด้านความมั่นคงปลอดภัยสำหรับกฎที่เปิดบริการสู่อินเทอร์เน็ตหรือข้ามโซนสำคัญ", "[CISO]"],
     ["4", "ดำเนินการผ่านการบริหารการเปลี่ยนแปลง พร้อมรหัสกฎและคำอธิบาย", "วิศวกรเครือข่าย"],
     ["5", "รับรองกฎทั้งหมดทุก 6 เดือนร่วมกับเจ้าของกฎ และลบกฎที่ไม่ใช้หรือหมดอายุ", "วิศวกรเครือข่าย เจ้าของกฎ"]], "w": [1.2, 11.3, 4.0]}),
 ],
 bp=[("Use rule hit counts to find unused rules during recertification.", "ใช้จำนวนครั้งที่กฎถูกใช้งานเพื่อค้นหากฎที่ไม่ได้ใช้ระหว่างการรับรอง")],
 mistakes=[("Temporary vendor rules remain for years because no expiry was set.", "กฎชั่วคราวสำหรับผู้ขายยังคงอยู่หลายปีเพราะไม่ได้กำหนดวันหมดอายุ")],
)

C["PR-FRM-006"] = dict(
 purpose=("This form requests and approves a firewall rule addition, change, or removal.", "แบบฟอร์มนี้ใช้ขอและอนุมัติการเพิ่ม เปลี่ยนแปลง หรือลบกฎไฟร์วอลล์"),
 fields=[
  ("Request number", "เลขที่คำขอ", "Assigned on submission.", "กำหนดเมื่อยื่นคำขอ", "FW-2026-001"),
  ("Action", "การดำเนินการ", "Add, change, remove.", "เพิ่ม เปลี่ยนแปลง ลบ", ""),
  ("Source (host or network, zone)", "ต้นทาง (เครื่องหรือเครือข่าย โซน)", "Specific addresses.", "ที่อยู่เฉพาะ", ""),
  ("Destination (host or network, zone)", "ปลายทาง (เครื่องหรือเครือข่าย โซน)", "Specific addresses.", "ที่อยู่เฉพาะ", ""),
  ("Ports and protocol", "พอร์ตและโปรโตคอล", "Specific ports only.", "เฉพาะพอร์ตที่กำหนด", ""),
  ("Business justification and owner", "เหตุผลทางธุรกิจและเจ้าของกฎ", "Why and who owns it.", "เหตุผลและผู้เป็นเจ้าของ", ""),
  ("Expiry date", "วันหมดอายุ", "Mandatory for temporary rules.", "บังคับสำหรับกฎชั่วคราว", ""),
  ("Security review notes", "ความเห็นการทบทวนด้านความมั่นคงปลอดภัย", "Completed by security.", "กรอกโดยทีมความมั่นคงปลอดภัย", ""),
 ],
 cmc_vals=["FW-2026-0144", "Add", "PAM jump host 10.50.1.10 (management zone)", "MED-IMG-002 and MED-IMG-005, VLAN 310 (medical device zone)", "TCP 3389 (RDP) and TCP 104 (DICOM test)",
           "Vendor B support through jump host only; owner Director of Radiology", "31 March 2027 (aligned with EXC-2026-007)", "Approved: source limited to jump host; sessions recorded; no internet path"],
 approvals=["Requester", "ITM", "CISO"],
 bp=[("Reject requests with 'any' in source, destination, or port unless the CISO approves an exception.", "ปฏิเสธคำขอที่ระบุ Any ในต้นทาง ปลายทาง หรือพอร์ต เว้นแต่ CISO อนุมัติเป็นข้อยกเว้น")],
 mistakes=[("Rules requested as 'open everything to the vendor so they can work'.", "ขอเปิดกฎทั้งหมดให้ผู้ขายเพื่อความสะดวกในการทำงาน")],
)

C["PR-STD-017"] = dict(
 purpose=("This standard sets requirements for redundancy, failover, and capacity management so that critical services meet availability and recovery objectives in normal and adverse situations (PR.IR-03, PR.IR-04).",
          "มาตรฐานนี้กำหนดข้อกำหนดด้านระบบสำรอง การสลับการทำงาน และการบริหารขีดความสามารถ เพื่อให้บริการสำคัญเป็นไปตามเป้าหมายความพร้อมใช้งานและการกู้คืนทั้งในสถานการณ์ปกติและไม่ปกติ (PR.IR-03, PR.IR-04)"),
 sections=[
  ("Requirements", "ข้อกำหนด", "Set resilience and capacity requirements by criticality.", "กำหนดข้อกำหนดด้านความยืดหยุ่นและขีดความสามารถตามระดับความสำคัญ",
   {"t": ["ID", "Requirement", "Critical", "High"], "r": [
     ["RS-01", "Redundant components (power, network, storage, servers)", "No single point of failure", "Redundant power and storage"],
     ["RS-02", "Alternate site or cloud region for recovery", "Required; meets RTO", "Recommended"],
     ["RS-03", "Dual internet and WAN links from different providers", "Required", "Recommended"],
     ["RS-04", "Capacity monitoring (CPU, memory, storage, bandwidth) with thresholds", "Alert at 80%", "Alert at 85%"],
     ["RS-05", "Capacity review and forecast", "Quarterly", "Semi-annually"],
     ["RS-06", "Protection against denial of service for internet-facing services", "Required", "Required"],
     ["RS-07", "Failover tested", "Annually", "Every two years"]], "w": [1.6, 7.4, 4.0, 3.5]},
   {"t": ["รหัส", "ข้อกำหนด", "วิกฤต", "สูง"], "r": [
     ["RS-01", "อุปกรณ์สำรอง (ไฟฟ้า เครือข่าย หน่วยจัดเก็บข้อมูล เซิร์ฟเวอร์)", "ไม่มีจุดล้มเหลวเดี่ยว", "ไฟฟ้าและหน่วยจัดเก็บข้อมูลสำรอง"],
     ["RS-02", "สถานที่สำรองหรือ Region คลาวด์สำรองสำหรับการกู้คืน", "บังคับ และเป็นไปตาม RTO", "แนะนำ"],
     ["RS-03", "เส้นทางอินเทอร์เน็ตและ WAN สองเส้นจากผู้ให้บริการต่างราย", "บังคับ", "แนะนำ"],
     ["RS-04", "การเฝ้าระวังขีดความสามารถ (CPU หน่วยความจำ หน่วยจัดเก็บ แบนด์วิดท์) พร้อมเกณฑ์", "แจ้งเตือนที่ 80%", "แจ้งเตือนที่ 85%"],
     ["RS-05", "การทบทวนและพยากรณ์ขีดความสามารถ", "ทุกไตรมาส", "ทุก 6 เดือน"],
     ["RS-06", "การป้องกันการโจมตีแบบปฏิเสธการให้บริการสำหรับบริการที่เปิดสู่อินเทอร์เน็ต", "บังคับ", "บังคับ"],
     ["RS-07", "การทดสอบการสลับการทำงาน", "ทุกปี", "ทุก 2 ปี"]], "w": [1.6, 7.4, 4.0, 3.5]}),
 ],
 bp=[("Align resilience design with BIA recovery objectives; spend where RTO is shortest.", "ออกแบบความยืดหยุ่นให้สอดคล้องกับเป้าหมายการกู้คืนใน BIA และลงทุนในจุดที่ RTO สั้นที่สุด")],
 mistakes=[("Redundant servers that share one storage array or one network switch.", "เซิร์ฟเวอร์สำรองที่ใช้หน่วยจัดเก็บข้อมูลหรือสวิตช์เครือข่ายเดียวกัน")],
)
