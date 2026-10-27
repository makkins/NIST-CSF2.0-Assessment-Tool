# -*- coding: utf-8 -*-
"""Interview question bank: Detect (DE), Respond (RS), Recover (RC)."""
from iq_idpr import Q, add

# DE.CM Continuous Monitoring
add("DE.CM-01", "SOC ITM",
    ("How are networks and network services monitored for suspicious activity?",
     "เฝ้าระวังเครือข่ายและบริการเครือข่ายเพื่อหากิจกรรมที่น่าสงสัยอย่างไร"),
    [("Who watches the alerts outside office hours?", "ใครเฝ้าดูการแจ้งเตือนนอกเวลาทำการ"),
     ("Are firewall, VPN, and DNS logs monitored?", "มีการเฝ้าระวังบันทึกของไฟร์วอลล์ VPN และ DNS หรือไม่")],
    ("Monitoring procedure, SIEM or MSSP reports, alert samples", "ขั้นตอนการเฝ้าระวัง รายงานจาก SIEM หรือ MSSP ตัวอย่างการแจ้งเตือน"))
add("DE.CM-02", "FAC",
    ("Is the physical environment monitored, for example with CCTV, door alarms, and access logs?",
     "มีการเฝ้าระวังสภาพแวดล้อมทางกายภาพหรือไม่ เช่น กล้องวงจรปิด สัญญาณเตือนประตู และบันทึกการเข้าออก"),
    [("Are alerts from restricted areas reviewed?", "มีการตรวจสอบการแจ้งเตือนจากพื้นที่หวงห้ามหรือไม่"),
     ("How long is CCTV footage kept?", "เก็บภาพกล้องวงจรปิดไว้นานเท่าใด")],
    ("CCTV coverage plan, alarm logs", "แผนการติดตั้งกล้องวงจรปิด บันทึกสัญญาณเตือน"))
add("DE.CM-03", "SOC ITM HR",
    ("Is user activity monitored to detect misuse, such as unusual logins or mass downloads?",
     "มีการเฝ้าระวังกิจกรรมของผู้ใช้เพื่อตรวจจับการใช้งานผิดวัตถุประสงค์หรือไม่ เช่น การเข้าสู่ระบบผิดปกติหรือการดาวน์โหลดจำนวนมาก"),
    [("Are privileged account activities reviewed?", "มีการทบทวนกิจกรรมของบัญชีสิทธิ์สูงหรือไม่"),
     ("Are staff informed that activity is monitored?", "พนักงานได้รับแจ้งว่ามีการเฝ้าระวังกิจกรรมหรือไม่")],
    ("User activity monitoring rules, privileged activity reviews", "กฎการเฝ้าระวังกิจกรรมผู้ใช้ ผลการทบทวนกิจกรรมสิทธิ์สูง"))
add("DE.CM-06", "SOC PROC ITM",
    ("Are supplier and service provider activities on your systems monitored?",
     "มีการเฝ้าระวังกิจกรรมของผู้ให้บริการบนระบบขององค์กรหรือไม่"),
    [("Is vendor remote access recorded and approved per session?", "การเข้าถึงระยะไกลของผู้ขายได้รับการบันทึกและอนุมัติเป็นรายครั้งหรือไม่"),
     ("Do you review cloud provider security alerts?", "มีการตรวจสอบการแจ้งเตือนด้านความมั่นคงปลอดภัยจากผู้ให้บริการคลาวด์หรือไม่")],
    ("Vendor access logs, session recordings, cloud security alerts", "บันทึกการเข้าถึงของผู้ขาย การบันทึกเซสชัน การแจ้งเตือนจากคลาวด์"))
add("DE.CM-09", "SOC ITM",
    ("Are endpoints, servers, applications, and cloud workloads monitored for malicious activity?",
     "มีการเฝ้าระวังเครื่องลูกข่าย เซิร์ฟเวอร์ ระบบงาน และคลาวด์เพื่อหากิจกรรมที่เป็นอันตรายหรือไม่"),
    [("What share of endpoints and servers run antimalware or EDR?", "เครื่องลูกข่ายและเซิร์ฟเวอร์ติดตั้ง Antimalware หรือ EDR แล้วสัดส่วนเท่าใด"),
     ("Are email and web traffic filtered?", "มีการกรองอีเมลและการใช้งานเว็บหรือไม่")],
    ("EDR coverage report, email security reports", "รายงานความครอบคลุม EDR รายงานความมั่นคงปลอดภัยอีเมล"))

# DE.AE Adverse Event Analysis
add("DE.AE-02", "SOC",
    ("How are alerts analyzed to understand what is happening?",
     "วิเคราะห์การแจ้งเตือนอย่างไรเพื่อทำความเข้าใจสิ่งที่เกิดขึ้น"),
    [("Walk me through how the last alert was investigated.", "อธิบายขั้นตอนการตรวจสอบการแจ้งเตือนครั้งล่าสุด"),
     ("Are there written triage steps or use cases?", "มีขั้นตอนการคัดกรองหรือกรณีการใช้งานที่เป็นลายลักษณ์อักษรหรือไม่")],
    ("Alert triage procedure, SIEM use case list, ticket samples", "ขั้นตอนการคัดกรองการแจ้งเตือน รายการกรณีการใช้งานใน SIEM ตัวอย่างตั๋วงาน"))
add("DE.AE-03", "SOC",
    ("Is information from multiple sources correlated, for example in a security information and event management (SIEM) system?",
     "มีการเชื่อมโยงข้อมูลจากหลายแหล่งหรือไม่ เช่น ในระบบบริหารจัดการข้อมูลและเหตุการณ์ด้านความมั่นคงปลอดภัย (SIEM)"),
    [("Which log sources feed the SIEM?", "แหล่งบันทึกใดส่งข้อมูลเข้า SIEM"),
     ("Are correlation rules tuned and reviewed?", "มีการปรับและทบทวนกฎการเชื่อมโยงหรือไม่")],
    ("SIEM source list, correlation rules", "รายการแหล่งข้อมูล SIEM กฎการเชื่อมโยง"))
add("DE.AE-04", "SOC CISO",
    ("How does the team estimate the impact and scope of a security event?",
     "ทีมประเมินผลกระทบและขอบเขตของเหตุการณ์ด้านความมั่นคงปลอดภัยอย่างไร"),
    [("Does the analyst know which assets are critical when assessing impact?", "ผู้วิเคราะห์ทราบหรือไม่ว่าทรัพย์สินใดสำคัญเมื่อประเมินผลกระทบ"),
     ("Are business owners consulted?", "มีการปรึกษาเจ้าของกระบวนการธุรกิจหรือไม่")],
    ("Impact assessment criteria, incident tickets", "เกณฑ์การประเมินผลกระทบ ตั๋วงานเหตุการณ์"))
add("DE.AE-06", "SOC CISO",
    ("How is information about security events passed to the right people and tools?",
     "ส่งข้อมูลเกี่ยวกับเหตุการณ์ด้านความมั่นคงปลอดภัยไปยังบุคคลและเครื่องมือที่เหมาะสมอย่างไร"),
    [("How does the MSSP or monitoring team notify you, and how fast?", "MSSP หรือทีมเฝ้าระวังแจ้งองค์กรอย่างไร และเร็วเพียงใด"),
     ("Is there an on-call list?", "มีรายชื่อผู้รับผิดชอบตามเวรหรือไม่")],
    ("Notification matrix, on-call roster, MSSP SLA", "ตารางการแจ้ง ตารางเวร SLA ของ MSSP"))
add("DE.AE-07", "SOC",
    ("Is threat intelligence and business context used when analyzing alerts?",
     "มีการใช้ข้อมูลข่าวกรองภัยคุกคามและบริบททางธุรกิจในการวิเคราะห์การแจ้งเตือนหรือไม่"),
    [("Are indicators of compromise (IOC) loaded into security tools?", "มีการนำตัวบ่งชี้การถูกบุกรุก (IOC) เข้าเครื่องมือด้านความมั่นคงปลอดภัยหรือไม่"),
     ("Does the analyst see asset owner and criticality in the alert?", "ผู้วิเคราะห์เห็นเจ้าของและระดับความสำคัญของทรัพย์สินในการแจ้งเตือนหรือไม่")],
    ("Threat intelligence integration, enriched alert samples", "การเชื่อมต่อข้อมูลข่าวกรอง ตัวอย่างการแจ้งเตือนที่เพิ่มบริบท"))
add("DE.AE-08", "SOC CISO",
    ("What criteria decide when an event becomes a declared incident, and who declares it?",
     "ใช้เกณฑ์ใดตัดสินว่าเหตุการณ์ใดเป็นเหตุการณ์ด้านความมั่นคงปลอดภัยที่ต้องประกาศ และใครเป็นผู้ประกาศ"),
    [("Are severity levels defined?", "มีการกำหนดระดับความรุนแรงหรือไม่"),
     ("How many incidents were declared last year?", "ปีที่ผ่านมาประกาศเหตุการณ์กี่ครั้ง")],
    ("Incident classification criteria, incident log", "เกณฑ์การจัดประเภทเหตุการณ์ ทะเบียนเหตุการณ์"))

# RS.MA Incident Management
add("RS.MA-01", "CISO SOC PROC",
    ("When an incident is declared, how is the incident response plan executed with third parties such as the MSSP, suppliers, and forensic firms?",
     "เมื่อประกาศเหตุการณ์ ดำเนินการตามแผนรับมือเหตุการณ์ร่วมกับบุคคลภายนอก เช่น MSSP ผู้ให้บริการ และบริษัทนิติวิทยาศาสตร์ดิจิทัล อย่างไร"),
    [("Is there a retainer with an incident response or forensic provider?", "มีสัญญาจ้างล่วงหน้ากับผู้ให้บริการรับมือเหตุการณ์หรือนิติวิทยาศาสตร์ดิจิทัลหรือไม่"),
     ("Was the plan used in a real incident or exercise last year?", "ปีที่ผ่านมาได้ใช้แผนในเหตุการณ์จริงหรือการฝึกซ้อมหรือไม่")],
    ("Incident response plan, retainer contract, incident reports", "แผนรับมือเหตุการณ์ สัญญาจ้างล่วงหน้า รายงานเหตุการณ์"))
add("RS.MA-02", "SOC",
    ("How are incident reports triaged and validated?",
     "คัดกรองและยืนยันรายงานเหตุการณ์อย่างไร"),
    [("How do staff report a suspicious email or event?", "พนักงานรายงานอีเมลหรือเหตุการณ์ที่น่าสงสัยอย่างไร"),
     ("How quickly are reports reviewed?", "รายงานได้รับการตรวจสอบเร็วเพียงใด")],
    ("Incident reporting channel, triage records", "ช่องทางการรายงานเหตุการณ์ บันทึกการคัดกรอง"))
add("RS.MA-03", "SOC CISO",
    ("How are incidents categorized and prioritized?",
     "จัดประเภทและจัดลำดับความสำคัญของเหตุการณ์อย่างไร"),
    [("Does priority consider data type, such as health or personal data?", "การจัดลำดับพิจารณาประเภทข้อมูล เช่น ข้อมูลสุขภาพหรือข้อมูลส่วนบุคคล หรือไม่"),
     ("Are categories consistent with regulatory reporting categories?", "ประเภทเหตุการณ์สอดคล้องกับประเภทที่ต้องรายงานหน่วยงานกำกับหรือไม่")],
    ("Severity matrix, incident register", "ตารางระดับความรุนแรง ทะเบียนเหตุการณ์"))
add("RS.MA-04", "CISO SOC CEO",
    ("How and when are incidents escalated to management, the crisis team, or regulators?",
     "ยกระดับเหตุการณ์ไปยังผู้บริหาร ทีมบริหารวิกฤต หรือหน่วยงานกำกับอย่างไรและเมื่อใด"),
    [("Who has authority to shut down a system or disconnect the internet?", "ใครมีอำนาจปิดระบบหรือตัดการเชื่อมต่ออินเทอร์เน็ต"),
     ("Is the escalation contact list current?", "รายชื่อผู้ติดต่อเพื่อยกระดับเป็นปัจจุบันหรือไม่")],
    ("Escalation matrix, crisis management plan", "ตารางการยกระดับ แผนบริหารวิกฤต"))
add("RS.MA-05", "CISO BCM",
    ("What criteria decide when to move from incident response to recovery?",
     "ใช้เกณฑ์ใดตัดสินว่าจะเปลี่ยนจากการรับมือเหตุการณ์ไปสู่การกู้คืน"),
    [("Who decides that containment is complete?", "ใครตัดสินว่าการควบคุมเหตุการณ์เสร็จสมบูรณ์"),
     ("Are recovery criteria written in the plan?", "มีเกณฑ์การเริ่มกู้คืนระบุไว้ในแผนหรือไม่")],
    ("Incident response plan recovery criteria", "เกณฑ์การเริ่มกู้คืนในแผนรับมือเหตุการณ์"))

# RS.AN Incident Analysis
add("RS.AN-03", "SOC",
    ("How is root cause analysis performed after an incident?",
     "วิเคราะห์หาสาเหตุที่แท้จริงหลังเกิดเหตุการณ์อย่างไร"),
    [("Can you show a root cause analysis from a past incident?", "แสดงผลการวิเคราะห์สาเหตุจากเหตุการณ์ที่ผ่านมาได้หรือไม่"),
     ("Who does the analysis: internal staff, MSSP, or external experts?", "ใครเป็นผู้วิเคราะห์ เจ้าหน้าที่ภายใน MSSP หรือผู้เชี่ยวชาญภายนอก")],
    ("Incident reports with root cause, post-incident review", "รายงานเหตุการณ์ที่ระบุสาเหตุ ผลการทบทวนหลังเหตุการณ์"))
add("RS.AN-06", "SOC LEGAL",
    ("Are investigation actions recorded in a way that preserves their integrity?",
     "มีการบันทึกการดำเนินการระหว่างการสืบสวนในรูปแบบที่รักษาความถูกต้องหรือไม่"),
    [("Is there an incident log or ticket with timestamps for each action?", "มีบันทึกหรือตั๋วงานที่ระบุเวลาของแต่ละการดำเนินการหรือไม่"),
     ("Could the records be used as evidence in court?", "บันทึกเหล่านี้ใช้เป็นพยานหลักฐานในชั้นศาลได้หรือไม่")],
    ("Incident timeline, investigation log", "ลำดับเหตุการณ์ บันทึกการสืบสวน"))
add("RS.AN-07", "SOC LEGAL",
    ("How is incident evidence collected and preserved, including chain of custody?",
     "เก็บรวบรวมและรักษาพยานหลักฐานของเหตุการณ์อย่างไร รวมถึงห่วงโซ่การครอบครองพยานหลักฐาน"),
    [("Does the team know how to capture memory and disk images before rebuilding?", "ทีมทราบวิธีเก็บภาพหน่วยความจำและดิสก์ก่อนติดตั้งระบบใหม่หรือไม่"),
     ("Is there a chain of custody form?", "มีแบบฟอร์มห่วงโซ่การครอบครองพยานหลักฐานหรือไม่")],
    ("Evidence handling procedure, chain of custody forms", "ขั้นตอนการจัดการพยานหลักฐาน แบบฟอร์มห่วงโซ่การครอบครอง"))
add("RS.AN-08", "SOC CISO",
    ("How is the magnitude of an incident estimated and confirmed, for example the number of records or systems affected?",
     "ประเมินและยืนยันขนาดของเหตุการณ์อย่างไร เช่น จำนวนระเบียนหรือระบบที่ได้รับผลกระทบ"),
    [("How would you determine how many patients or customers were affected in a data breach?", "หากข้อมูลรั่วไหล จะหาจำนวนผู้รับบริการหรือลูกค้าที่ได้รับผลกระทบอย่างไร"),
     ("Is the estimate updated as the investigation progresses?", "มีการปรับปรุงการประเมินระหว่างการสืบสวนหรือไม่")],
    ("Incident reports, breach assessment worksheet", "รายงานเหตุการณ์ แบบประเมินการละเมิดข้อมูล"))

# RS.CO Reporting and Communication
add("RS.CO-02", "CISO DPO LEGAL",
    ("How are internal and external stakeholders, including regulators, notified of incidents within the required timelines?",
     "แจ้งผู้มีส่วนได้ส่วนเสียภายในและภายนอก รวมถึงหน่วยงานกำกับ เกี่ยวกับเหตุการณ์ภายในกำหนดเวลาอย่างไร"),
    [("Who reports a personal data breach to the PDPC within 72 hours under PDPA s.37(4)?", "ใครเป็นผู้แจ้งเหตุละเมิดข้อมูลส่วนบุคคลต่อ สคส. ภายใน 72 ชั่วโมงตาม PDPA มาตรา 37(4)"),
     ("For CII, who reports to the NCSA and the sector regulator, and within what time? [VERIFY]", "สำหรับ CII ใครเป็นผู้รายงานต่อ สกมช. และหน่วยงานกำกับ และภายในเวลาเท่าใด [VERIFY]")],
    ("Notification procedure, regulator contact list, past notifications", "ขั้นตอนการแจ้งเหตุ รายชื่อผู้ติดต่อหน่วยงานกำกับ การแจ้งเหตุที่ผ่านมา"))
add("RS.CO-03", "CISO COMMS",
    ("How is incident information shared with designated stakeholders, such as partners, CERTs, and insurers?",
     "แบ่งปันข้อมูลเหตุการณ์กับผู้มีส่วนได้ส่วนเสียที่กำหนด เช่น คู่ค้า ศูนย์ CERT และบริษัทประกันภัย อย่างไร"),
    [("Who approves what is shared outside the organization?", "ใครอนุมัติข้อมูลที่จะเปิดเผยภายนอกองค์กร"),
     ("Is there a communication template?", "มีแม่แบบการสื่อสารหรือไม่")],
    ("Communication plan, message templates", "แผนการสื่อสาร แม่แบบข้อความ"))

# RS.MI Mitigation
add("RS.MI-01", "SOC ITM",
    ("How are incidents contained, for example by isolating hosts or disabling accounts?",
     "ควบคุมเหตุการณ์อย่างไร เช่น การแยกเครื่องหรือการระงับบัญชี"),
    [("Can the team isolate an infected endpoint remotely within minutes?", "ทีมแยกเครื่องที่ติดมัลแวร์จากระยะไกลได้ภายในไม่กี่นาทีหรือไม่"),
     ("Are there playbooks for ransomware and account compromise?", "มีคู่มือปฏิบัติสำหรับแรนซัมแวร์และบัญชีถูกยึดหรือไม่")],
    ("Incident playbooks, containment records", "คู่มือปฏิบัติการรับมือเหตุการณ์ บันทึกการควบคุมเหตุการณ์"))
add("RS.MI-02", "SOC ITM",
    ("How is the threat fully removed before systems return to service?",
     "กำจัดภัยคุกคามให้หมดก่อนนำระบบกลับมาให้บริการอย่างไร"),
    [("Are compromised systems rebuilt rather than cleaned?", "ระบบที่ถูกบุกรุกได้รับการติดตั้งใหม่แทนการทำความสะอาดหรือไม่"),
     ("Are all credentials reset after a compromise?", "หลังถูกบุกรุก มีการรีเซ็ตข้อมูลยืนยันตัวตนทั้งหมดหรือไม่")],
    ("Eradication checklist, incident closure records", "รายการตรวจสอบการกำจัดภัยคุกคาม บันทึกการปิดเหตุการณ์"))

# RC.RP Recovery Plan Execution
add("RC.RP-01", "BCM ITM CISO",
    ("Once recovery starts, how is the recovery part of the incident response plan or disaster recovery plan executed?",
     "เมื่อเริ่มการกู้คืน ดำเนินการตามส่วนการกู้คืนของแผนรับมือเหตุการณ์หรือแผนกู้คืนระบบอย่างไร"),
    [("Who leads recovery, and is that written in the plan?", "ใครเป็นผู้นำการกู้คืน และระบุไว้ในแผนหรือไม่"),
     ("Was the plan used in the last real outage?", "ได้ใช้แผนในเหตุระบบล่มจริงครั้งล่าสุดหรือไม่")],
    ("Disaster recovery plan, recovery records", "แผนกู้คืนระบบ บันทึกการกู้คืน"))
add("RC.RP-02", "BCM ITM SYSOWN",
    ("How are recovery actions selected and prioritized, for example by system criticality and RTO?",
     "เลือกและจัดลำดับการกู้คืนอย่างไร เช่น ตามความสำคัญของระบบและ RTO"),
    [("Is there an agreed recovery order for systems?", "มีลำดับการกู้คืนระบบที่ตกลงร่วมกันหรือไม่"),
     ("Do business owners agree with that order?", "เจ้าของกระบวนการธุรกิจเห็นด้วยกับลำดับนั้นหรือไม่")],
    ("System recovery priority list, BIA", "ลำดับความสำคัญในการกู้คืนระบบ BIA"))
add("RC.RP-03", "ITM SOC",
    ("How is the integrity of backups verified before using them to restore?",
     "ตรวจสอบความถูกต้องของข้อมูลสำรองก่อนนำมากู้คืนอย่างไร"),
    [("How would you make sure a backup is not already infected with ransomware?", "จะมั่นใจได้อย่างไรว่าข้อมูลสำรองไม่ได้ติดแรนซัมแวร์อยู่แล้ว"),
     ("Are backups scanned or checked before restore?", "มีการสแกนหรือตรวจสอบข้อมูลสำรองก่อนกู้คืนหรือไม่")],
    ("Restore procedure, backup integrity checks", "ขั้นตอนการกู้คืน การตรวจสอบความถูกต้องของข้อมูลสำรอง"))
add("RC.RP-04", "BCM CISO SYSOWN",
    ("How are critical business functions and security considered when deciding post-incident operating norms?",
     "พิจารณาหน้าที่ทางธุรกิจที่สำคัญและความมั่นคงปลอดภัยอย่างไรในการกำหนดการดำเนินงานหลังเหตุการณ์"),
    [("Are manual workarounds defined for critical services during recovery?", "มีการกำหนดวิธีทำงานด้วยมือสำหรับบริการสำคัญระหว่างกู้คืนหรือไม่"),
     ("Are extra controls applied after restoring, such as heightened monitoring?", "มีการเพิ่มการควบคุมหลังกู้คืน เช่น การเฝ้าระวังเข้มข้นขึ้น หรือไม่")],
    ("Business continuity plan, manual procedures", "แผนความต่อเนื่องทางธุรกิจ ขั้นตอนการทำงานด้วยมือ"))
add("RC.RP-05", "ITM SYSOWN",
    ("How is the integrity of restored systems verified and normal operation confirmed?",
     "ตรวจสอบความถูกต้องของระบบที่กู้คืนและยืนยันการกลับสู่การดำเนินงานปกติอย่างไร"),
    [("Do system owners sign off that a restored system works correctly?", "เจ้าของระบบลงนามยืนยันว่าระบบที่กู้คืนทำงานถูกต้องหรือไม่"),
     ("Are restored systems checked for remaining malicious activity?", "มีการตรวจสอบระบบที่กู้คืนว่ายังมีกิจกรรมอันตรายหลงเหลือหรือไม่")],
    ("Recovery verification checklist, sign-off records", "รายการตรวจสอบการกู้คืน บันทึกการลงนามรับรอง"))
add("RC.RP-06", "CISO BCM",
    ("What criteria declare the end of recovery, and what documentation is completed?",
     "ใช้เกณฑ์ใดประกาศสิ้นสุดการกู้คืน และจัดทำเอกสารใดให้ครบถ้วน"),
    [("Is a final incident report produced and approved?", "มีการจัดทำและอนุมัติรายงานเหตุการณ์ฉบับสมบูรณ์หรือไม่"),
     ("Is the lessons-learned meeting held within a set time?", "มีการประชุมถอดบทเรียนภายในเวลาที่กำหนดหรือไม่")],
    ("Final incident report, recovery closure record", "รายงานเหตุการณ์ฉบับสมบูรณ์ บันทึกการปิดการกู้คืน"))

# RC.CO Recovery Communication
add("RC.CO-03", "CISO COMMS BCM",
    ("How are recovery progress and status communicated to management and affected stakeholders?",
     "สื่อสารความคืบหน้าและสถานะการกู้คืนไปยังผู้บริหารและผู้มีส่วนได้ส่วนเสียที่ได้รับผลกระทบอย่างไร"),
    [("How often are status updates sent during an outage?", "ระหว่างระบบล่มมีการส่งข้อมูลสถานะบ่อยเพียงใด"),
     ("Is there an alternate channel if email is down?", "มีช่องทางสำรองหรือไม่หากอีเมลใช้งานไม่ได้")],
    ("Communication plan, status update records", "แผนการสื่อสาร บันทึกการแจ้งสถานะ"))
add("RC.CO-04", "COMMS CEO LEGAL",
    ("How are public updates about an incident and recovery approved and released?",
     "อนุมัติและเผยแพร่ข้อมูลต่อสาธารณะเกี่ยวกับเหตุการณ์และการกู้คืนอย่างไร"),
    [("Who is the authorized spokesperson?", "ใครเป็นโฆษกที่ได้รับมอบหมาย"),
     ("Are holding statements prepared in advance?", "มีการเตรียมแถลงการณ์เบื้องต้นไว้ล่วงหน้าหรือไม่")],
    ("Crisis communication plan, approved holding statements", "แผนการสื่อสารในภาวะวิกฤต แถลงการณ์เบื้องต้นที่อนุมัติแล้ว"))

if __name__ == "__main__":
    print(len(Q))
