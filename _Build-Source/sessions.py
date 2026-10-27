# -*- coding: utf-8 -*-
"""Recommended interview sequence for the information gathering phase, and the system-level control set for critical system sampling.
Every CSF 2.0 Subcategory is assigned to exactly one session, in the order it should be asked. Pairs are (EN, TH)."""

SESSIONS = [
 dict(id="S1", n=["Executive context and business priorities", "บริบทผู้บริหารและลำดับความสำคัญทางธุรกิจ"],
      r="CEO CIO CFO CRO", dur=["60 to 90 minutes", "60 ถึง 90 นาที"], dep=[], par=False, areas=[],
      obj=["Understand what the business must protect, how much risk management accepts, and who is accountable. Capture the business services that later drive the Quick BIA.",
           "เข้าใจว่าธุรกิจต้องปกป้องอะไร ผู้บริหารรับความเสี่ยงได้แค่ไหน และใครรับผิดชอบ พร้อมรวบรวมบริการทางธุรกิจที่จะใช้ทำ Quick BIA ต่อ"],
      out=["Top business services, risk appetite statements as stated, accountability, budget context, candidate critical services. Environment profile: sites, IT organization, incident history.",
           "บริการทางธุรกิจหลัก ระดับความเสี่ยงที่ยอมรับได้ตามที่ผู้บริหารให้ข้อมูล ผู้รับผิดชอบ บริบทงบประมาณ และรายชื่อบริการที่น่าจะสำคัญ Environment profile: สถานที่ โครงสร้างทีม IT และประวัติเหตุการณ์"],
      subs="GV.OC-01 GV.OC-04 GV.OC-05 GV.OC-02 GV.RM-01 GV.RM-02 GV.RM-04 GV.RM-07 GV.RR-01 GV.RR-03 GV.OV-01"),
 dict(id="S2", n=["Quick BIA and system discovery", "Quick BIA และการสำรวจระบบ"],
      r="CIO ITM BCM SYSOWN", dur=["Part A 90 minutes; Part B 45 to 60 minutes for about 30 systems", "ส่วน A 90 นาที ส่วน B 45 ถึง 60 นาทีสำหรับประมาณ 30 ระบบ"], dep=["S1"], par=False, areas=["AST"],
      obj=["Part A with business users: ask each department which systems they use to do their work, link each system to the business services from S1, score impact and tolerable downtime, and agree which systems are critical. Part B with IT: walk down the list and fill the Core system profile (origin, authentication, MFA, admin accounts, internet exposure, vendor access, patching, backup) for every system. Select 3 to 5 systems for deep-dive sampling.",
           "ส่วน A กับผู้ใช้งานธุรกิจ: ถามแต่ละหน่วยงานว่าใช้ระบบใดทำงาน เชื่อมแต่ละระบบกับบริการทางธุรกิจจาก S1 ให้คะแนนผลกระทบและเวลาหยุดที่รับได้ และตกลงว่าระบบใดสำคัญ ส่วน B กับ IT: ไล่ตามรายชื่อและกรอก Core system profile (ที่มา วิธียืนยันตัวตน MFA บัญชีผู้ดูแล การเปิดสู่อินเทอร์เน็ต การเข้าถึงของผู้ขาย การแพตช์ การสำรองข้อมูล) ให้ครบทุกระบบ แล้วเลือก 3 ถึง 5 ระบบเพื่อสุ่มตรวจเชิงลึก"],
      out=["System list with criticality A, B, or C (preliminary, not a full BIA), Core profile for every system, shared infrastructure, systems selected for sampling",
           "รายชื่อระบบพร้อมระดับความสำคัญ A, B หรือ C (เบื้องต้น ไม่ใช่ BIA เต็มรูปแบบ) Core profile ของทุกระบบ โครงสร้างพื้นฐานที่ใช้ร่วมกัน และระบบที่เลือกสุ่มตรวจ"],
      subs="ID.AM-05 ID.AM-02 ID.AM-01 ID.AM-04 ID.AM-03 ID.AM-07 ID.AM-08"),
 dict(id="S2C", n=["Department user interviews", "สัมภาษณ์ผู้ใช้งานรายแผนก"],
      r="DEPT", dur=["About 30 minutes per department", "ประมาณ 30 นาทีต่อแผนก"], dep=["S2"], par=False, areas=[],
      obj=["Ask frontline users in each department how they really work: systems and apps used, login and password sharing, shared computers, personal channels for work data, remote work, training, incident reporting, and outage workarounds. Compare the answers with what IT stated in S2 Part B and S3.",
           "ถามผู้ใช้งานหน้างานในแต่ละแผนกว่าทำงานจริงอย่างไร ทั้งระบบและแอปที่ใช้ การล็อกอินและการใช้รหัสผ่านร่วมกัน เครื่องที่ใช้ร่วมกัน ช่องทางส่วนตัวสำหรับข้อมูลงาน การทำงานจากภายนอก การอบรม การแจ้งเหตุ และวิธีทำงานเมื่อระบบล่ม แล้วเทียบกับคำตอบของ IT ใน S2 ส่วน B และ S3"],
      out=["Departments tab: U1 to U8 answers per department, custom questions (U9), systems IT did not list, and conflicts with IT answers.",
           "แท็บแผนก: คำตอบ U1 ถึง U8 รายแผนก คำถามเพิ่มเติม (U9) ระบบที่ IT ไม่ได้ระบุ และจุดที่ขัดกับคำตอบของ IT"],
      subs=""),
 dict(id="S3", n=["Governance, risk, and policy", "การกำกับดูแล ความเสี่ยง และนโยบาย"],
      r="CISO CRO IA ITM", dur=["90 minutes", "90 นาที"], dep=["S1"], par=True, areas=[],
      obj=["Check how security is governed in practice: roles, policy, risk method and register, change and exception control, oversight, and audit follow-up.",
           "ตรวจว่าการกำกับดูแลด้านความมั่นคงปลอดภัยทำจริงอย่างไร ทั้งบทบาท นโยบาย วิธีและทะเบียนความเสี่ยง การควบคุมการเปลี่ยนแปลงและการยกเว้น การกำกับติดตาม และการติดตามผลการตรวจสอบ"],
      out=["Governance structure, policy status, risk register status, open audit findings. Environment profile: data center and DR site, staff remote access, workstations, changes in flight.", "โครงสร้างการกำกับดูแล สถานะนโยบาย สถานะทะเบียนความเสี่ยง และข้อตรวจพบที่ยังเปิดอยู่ Environment profile: ศูนย์ข้อมูลและศูนย์สำรอง การเข้าถึงระยะไกลของพนักงาน เครื่องลูกข่าย และการเปลี่ยนแปลงที่กำลังดำเนินการ"],
      subs="GV.RR-02 GV.PO-01 GV.PO-02 GV.RM-03 GV.RM-05 GV.RM-06 ID.RA-03 ID.RA-04 ID.RA-05 ID.RA-06 ID.RA-07 GV.OV-02 GV.OV-03 ID.IM-01"),
 dict(id="S4", n=["Legal, privacy, and people", "กฎหมาย การคุ้มครองข้อมูล และบุคลากร"],
      r="DPO LEGAL HR", dur=["60 to 90 minutes", "60 ถึง 90 นาที"], dep=["S1"], par=True, areas=[],
      obj=["Confirm legal and regulatory duties (CII, PDPA, sector rules), HR security practices, and awareness training.",
           "ยืนยันหน้าที่ตามกฎหมายและหน่วยงานกำกับ (CII, PDPA และกฎเฉพาะอุตสาหกรรม) แนวปฏิบัติด้านความมั่นคงปลอดภัยของงานบุคคล และการอบรมสร้างความตระหนัก"],
      out=["Applicable laws and duties, HR joiner-mover-leaver practice, training coverage", "กฎหมายและหน้าที่ที่ใช้บังคับ แนวปฏิบัติการรับเข้า ย้าย และพ้นสภาพ และความครอบคลุมของการอบรม"],
      subs="GV.OC-03 GV.RR-04 PR.AT-01 PR.AT-02"),
 dict(id="S5", n=["Third-party and supply chain", "ผู้ให้บริการและห่วงโซ่อุปทาน"],
      r="PROC LEGAL ITM", dur=["60 to 90 minutes", "60 ถึง 90 นาที"], dep=["S1"], par=True, areas=[],
      obj=["Identify critical suppliers and how they are selected, contracted, monitored, involved in incidents, and offboarded.",
           "ระบุผู้ให้บริการสำคัญ และวิธีคัดเลือก ทำสัญญา ติดตาม ให้มีส่วนร่วมในการรับมือเหตุการณ์ และยุติการใช้บริการ"],
      out=["Vendor profile for each vendor with system or data access: service, access, data, contract clauses, data processing agreement, due diligence (feeds S6)", "Vendor profile ของผู้ขายที่เข้าถึงระบบหรือข้อมูล: บริการ การเข้าถึง ข้อมูล ข้อสัญญา ข้อตกลงการประมวลผลข้อมูล และการตรวจสอบ (ใช้ต่อใน S6)"],
      subs="GV.SC-01 GV.SC-04 GV.SC-02 GV.SC-03 GV.SC-05 GV.SC-06 ID.RA-10 ID.RA-09 GV.SC-07 GV.SC-09 GV.SC-08 GV.SC-10"),
 dict(id="S6", n=["Technical controls deep-dive and critical system sampling", "เจาะลึก Technical Control และสุ่มตรวจระบบสำคัญ"],
      r="ITM DEV SYSOWN", dur=["Half day to 1 day", "ครึ่งวันถึง 1 วัน"], dep=["S2", "S5"], par=False, areas=["IAM", "EP", "NET", "EML", "DATA", "BKP", "VUL", "CLD", "APP", "SUP", "OT"],
      obj=["Check how protective controls are implemented, using the technical checks, and test them on the critical systems selected in S2.",
           "ตรวจว่ามีการนำการควบคุมเชิงป้องกันไปใช้จริงอย่างไร ด้วยรายการตรวจทางเทคนิค และทดสอบกับระบบสำคัญที่เลือกไว้ใน S2"],
      out=["Technical check results, Full system profile for sampled systems, Development profile for in-house or customized systems, system sampling matrix, evidence seen, technical observations. Environment profile: network segmentation, medical devices and OT, backup architecture, security tool inventory.", "ผลการตรวจทางเทคนิค Full system profile ของระบบที่สุ่มตรวจ Development profile ของระบบที่พัฒนาเองหรือปรับแต่ง ตารางสุ่มตรวจรายระบบ หลักฐานที่เห็น และข้อสังเกตทางเทคนิค Environment profile: การแบ่งส่วนเครือข่าย อุปกรณ์การแพทย์และ OT สถาปัตยกรรมการสำรองข้อมูล และรายการเครื่องมือด้านความมั่นคงปลอดภัย"],
      subs="PR.AA-01 PR.AA-03 PR.AA-04 PR.AA-05 PR.AA-02 PR.DS-01 PR.DS-02 PR.DS-10 PR.DS-11 PR.PS-01 PR.PS-02 PR.PS-03 PR.PS-05 PR.PS-06 PR.IR-01 PR.IR-03 PR.IR-04 ID.RA-01 ID.RA-02 ID.RA-08"),
 dict(id="S7", n=["Detection and security monitoring", "การตรวจจับและเฝ้าระวังความมั่นคงปลอดภัย"],
      r="SOC ITM", dur=["60 to 90 minutes", "60 ถึง 90 นาที"], dep=["S6"], par=False, areas=["LOG"],
      obj=["Check what is logged, who watches, how alerts are analyzed, and when an event becomes an incident. Include the MSSP if monitoring is outsourced.",
           "ตรวจว่าบันทึกอะไร ใครเฝ้าดู วิเคราะห์การแจ้งเตือนอย่างไร และเมื่อใดเหตุการณ์ทั่วไปกลายเป็นเหตุการณ์ด้านความมั่นคงปลอดภัย รวม MSSP หากจ้างเฝ้าระวังจากภายนอก"],
      out=["Log coverage, monitoring hours, incident declaration criteria (feeds S8)", "ความครอบคลุมของบันทึก ช่วงเวลาเฝ้าระวัง และเกณฑ์การประกาศเหตุการณ์ (ใช้ต่อใน S8)"],
      subs="PR.PS-04 DE.CM-01 DE.CM-03 DE.CM-06 DE.CM-09 DE.AE-02 DE.AE-03 DE.AE-04 DE.AE-06 DE.AE-07 DE.AE-08"),
 dict(id="S8", n=["Incident response, recovery, and continuity", "การรับมือเหตุการณ์ การกู้คืน และความต่อเนื่อง"],
      r="CISO SOC BCM COMMS LEGAL", dur=["90 minutes, ideally as a short scenario walk-through", "90 นาที ควรเดินตามสถานการณ์จำลองสั้น ๆ"], dep=["S2", "S7"], par=False, areas=["IR"],
      obj=["Walk through a ransomware scenario on a critical system from S2: escalation, containment, evidence, notification, recovery order, and communication.",
           "เดินตามสถานการณ์แรนซัมแวร์บนระบบสำคัญจาก S2 ตั้งแต่การยกระดับ การควบคุม หลักฐาน การแจ้งเหตุ ลำดับการกู้คืน และการสื่อสาร"],
      out=["Incident and recovery capability, notification readiness, lessons-learned practice", "ขีดความสามารถในการรับมือและกู้คืน ความพร้อมในการแจ้งเหตุ และการถอดบทเรียน"],
      subs="RS.MA-01 RS.MA-02 RS.MA-03 RS.MA-04 RS.AN-03 RS.AN-06 RS.AN-07 RS.AN-08 RS.MI-01 RS.MI-02 RS.CO-02 RS.CO-03 RS.MA-05 RC.RP-01 RC.RP-02 RC.RP-03 RC.RP-05 RC.RP-04 RC.RP-06 RC.CO-03 RC.CO-04 ID.IM-04 ID.IM-02 ID.IM-03"),
 dict(id="S9", n=["Facilities walk-through", "เดินตรวจพื้นที่และอาคาร"],
      r="FAC ITM", dur=["30 to 45 minutes on site", "30 ถึง 45 นาทีหน้างาน"], dep=["S2"], par=True, areas=["PHY"],
      obj=["Observe physical access, environmental protection, and monitoring of the server room and network closets that host the critical systems.",
           "สังเกตการควบคุมการเข้าถึงทางกายภาพ การป้องกันด้านสิ่งแวดล้อม และการเฝ้าระวังของห้องเซิร์ฟเวอร์และตู้เครือข่ายที่ระบบสำคัญตั้งอยู่"],
      out=["Physical and environmental observations with photos where allowed", "ข้อสังเกตด้านกายภาพและสิ่งแวดล้อม พร้อมภาพถ่ายหากได้รับอนุญาต"],
      subs="PR.AA-06 PR.IR-02 DE.CM-02"),
 dict(id="S10", n=["Wrap-up and document request confirmation", "สรุปและยืนยันรายการขอเอกสาร"],
      r="CIO ITM", dur=["30 minutes", "30 นาที"], dep=["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9"], par=False, areas=[],
      obj=["Read back the document request list built during the interviews, confirm owners and due dates, and agree the open evidence requests.",
           "ทวนรายการขอเอกสารที่รวบรวมระหว่างสัมภาษณ์ ยืนยันผู้รับผิดชอบและวันส่ง และตกลงรายการขอหลักฐานที่ยังค้าง"],
      out=["Confirmed document and evidence request list with owners and dates. Environment profile: prior assessments and audits.", "รายการขอเอกสารและหลักฐานที่ยืนยันแล้ว พร้อมผู้รับผิดชอบและวันส่ง Environment profile: การประเมินและการตรวจสอบครั้งก่อน"],
      subs=""),
]
for s in SESSIONS:
    s["subs"] = s["subs"].split()
    s["r"] = s["r"].split()

PRINCIPLES = [
 ["Business before technology: S1 tells you what matters, so later answers can be judged against it.", "ธุรกิจก่อนเทคโนโลยี: S1 บอกว่าอะไรสำคัญ จึงใช้ตัดสินคำตอบในรอบถัดไปได้"],
 ["Systems before technical checks: S2 names the critical systems, so S6 to S8 test controls on real systems instead of general statements.", "รายชื่อระบบก่อนการตรวจทางเทคนิค: S2 ระบุระบบสำคัญ ทำให้ S6 ถึง S8 ทดสอบการควบคุมบนระบบจริง แทนคำตอบแบบภาพรวม"],
 ["Governance does not need the system list: S3, S4, and S5 depend only on S1 and can run in parallel with S2 when the schedule is tight.", "งานกำกับดูแลไม่ต้องรอรายชื่อระบบ: S3, S4 และ S5 ขึ้นกับ S1 เท่านั้น และทำคู่ขนานกับ S2 ได้เมื่อเวลาจำกัด"],
 ["Rules before practice: hearing the stated rules in S3 first lets you check in S6 to S8 whether practice follows them.", "กติกาก่อนการปฏิบัติ: รับฟังกติกาที่ประกาศไว้ใน S3 ก่อน แล้วตรวจใน S6 ถึง S8 ว่าทำตามจริงหรือไม่"],
 ["Prevention, detection, then response: S8 reuses the tools and contacts found in S6 and S7 in one scenario walk-through.", "ป้องกัน ตรวจจับ แล้วจึงรับมือ: S8 นำเครื่องมือและผู้ติดต่อที่พบใน S6 และ S7 มาใช้ในการเดินสถานการณ์จำลองครั้งเดียว"],
 ["Collect document requests as you go, and confirm them last: interviewees often remember documents they denied having in the written request list.", "รวบรวมรายการขอเอกสารระหว่างทาง แล้วยืนยันตอนท้าย: ผู้ให้สัมภาษณ์มักนึกเอกสารที่เคยตอบว่าไม่มีในรายการขอเอกสารได้ระหว่างสัมภาษณ์"],
]

# System-level controls for critical system sampling (S6). Each: key, CSF Subcategories, label (EN, TH).
SYSCTL = [
 ("own", "ID.AM-05 GV.RR-02", ["System owner named and accountable", "มีเจ้าของระบบที่ระบุชื่อและรับผิดชอบ"]),
 ("mfa", "PR.AA-03", ["MFA for users and administrators", "ใช้ MFA กับผู้ใช้และผู้ดูแลระบบ"]),
 ("priv", "PR.AA-05", ["Administrator accounts limited and named", "บัญชีผู้ดูแลจำกัดจำนวนและระบุชื่อ"]),
 ("uar", "PR.AA-05", ["User access reviewed in the last 12 months", "ทบทวนสิทธิ์ผู้ใช้ภายใน 12 เดือน"]),
 ("bkp", "PR.DS-11", ["Backup protected, with an off-site or immutable copy", "ข้อมูลสำรองได้รับการปกป้อง และมีสำเนานอกสถานที่หรือแก้ไขไม่ได้"]),
 ("rst", "PR.DS-11 RC.RP-03", ["Restore tested in the last 12 months", "ทดสอบกู้คืนภายใน 12 เดือน"]),
 ("dr", "PR.IR-03 RC.RP-02", ["Recovery meets the tolerable downtime", "การกู้คืนทำได้ทันเวลาหยุดที่รับได้"]),
 ("pat", "PR.PS-02", ["Supported version, patched on schedule", "เวอร์ชันที่ยังได้รับการสนับสนุน และแพตช์ตามรอบ"]),
 ("log", "PR.PS-04 DE.CM-09", ["Security logs sent to central logging or SIEM", "ส่งบันทึกด้านความมั่นคงปลอดภัยเข้าระบบส่วนกลางหรือ SIEM"]),
 ("edr", "DE.CM-09", ["EDR or antimalware on servers", "มี EDR หรือ Antimalware บนเซิร์ฟเวอร์"]),
 ("ven", "DE.CM-06 GV.SC-05", ["Vendor remote access controlled and logged", "ควบคุมและบันทึกการเข้าถึงระยะไกลของผู้ขาย"]),
 ("enc", "PR.DS-01 PR.DS-02", ["Sensitive data encrypted at rest and in transit", "เข้ารหัสข้อมูลอ่อนไหวขณะจัดเก็บและส่งผ่าน"]),
 ("seg", "PR.IR-01", ["Network segment and access filtering in place", "อยู่ในส่วนเครือข่ายที่แยกและกรองการเข้าถึง"]),
]
SYSCTL = [dict(k=k, s=s.split(), n=n) for k, s, n in SYSCTL]

if __name__ == "__main__":
    from iq_dersrc import Q
    allsubs = [x for s in SESSIONS for x in s["subs"]]
    print(len(allsubs), len(set(allsubs)), set(Q) - set(allsubs), set(allsubs) - set(Q))
    print(all(x in Q for c in SYSCTL for x in c["s"]))
