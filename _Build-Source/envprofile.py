# -*- coding: utf-8 -*-
"""Environment Profile for the Interview Assessment (spec: claude/current-it-landscape-spec.md v1.0, Section 6).
Organization-wide facts that feed the Current IT Landscape section of the Gap Analysis. Fields carry no rating:
they describe the environment and never change coverage. Where a field overlaps a Core profile field, the Core profile governs.
ENV_FIELDS: single answers. type: sel (one option), num (number), text, multi (several options).
ENV_TABLES: repeating rows. Each row gets an ID from its prefix, for example TOOL-01, so the Gap Analysis can cite it.
block: Landscape block(s) in the Gap Analysis report that use the answer. Pairs are (EN, TH). Thai text is a working translation."""

UNK = ["unk", "Unknown", "ไม่ทราบ"]

def O(opts):
    return [dict(c=c, n=[en, th]) for c, en, th in opts]

def F(id, k, sess, typ, n, ask, block, s="", o=()):
    return dict(id=id, k=k, sess=sess, type=typ, n=n, ask=ask, block=block.split(), s=s.split(), o=O(o))

ENV_FIELDS = [
 F("E2", "dc", "S3", "text", ["Primary data center", "ศูนย์ข้อมูลหลัก"], ["Where do the main servers run?", "เซิร์ฟเวอร์หลักตั้งอยู่ที่ใด"], "B4", "ID.AM-01"),
 F("E2", "dr", "S3", "sel", ["Disaster recovery (DR) site", "ศูนย์สำรองกรณีฉุกเฉิน (DR site)"], ["Is there a second site to run critical systems, and was failover tested?", "มีสถานที่สำรองสำหรับเปิดระบบสำคัญหรือไม่ และเคยทดสอบสลับไปใช้หรือไม่"], "B4", "PR.IR-03 RC.RP-02",
   [["tested", "Yes, failover tested within 12 months", "มี ทดสอบสลับภายใน 12 เดือน"], ["untested", "Yes, not tested", "มี แต่ยังไม่ทดสอบ"], ["none", "None", "ไม่มี"], UNK]),
 F("E3", "seg", "S6", "sel", ["Network segmentation", "การแบ่งส่วนเครือข่าย"], ["Is the network split into zones with filtering between them?", "เครือข่ายแบ่งเป็นโซนและมีการกรองระหว่างโซนหรือไม่"], "B4", "PR.IR-01",
   [["zone", "Segmented by zone with filtering", "แบ่งโซนและกรองการเข้าถึง"], ["part", "Partly segmented", "แบ่งบางส่วน"], ["flat", "Flat", "ไม่แบ่งส่วน"], UNK]),
 F("E4", "rem", "S3", "sel", ["Remote access for staff", "การเข้าถึงระยะไกลของพนักงาน"], ["How do staff connect from outside?", "พนักงานเชื่อมต่อจากภายนอกอย่างไร"], "B4 B5", "PR.AA-03 PR.IR-01",
   [["vpnm", "VPN with MFA", "VPN พร้อม MFA"], ["vpn", "VPN without MFA", "VPN ไม่มี MFA"], ["rdp", "Remote desktop exposed to the internet", "Remote desktop เปิดสู่อินเทอร์เน็ต"],
    ["tool", "Remote access tools, for example AnyDesk", "โปรแกรมรีโมต เช่น AnyDesk"], ["none", "No remote access", "ไม่มีการเข้าถึงระยะไกล"], UNK]),
 F("E5", "ws", "S3", "num", ["Workstations", "จำนวนเครื่องลูกข่าย"], ["About how many desktops and laptops are in use?", "มีเครื่องคอมพิวเตอร์และโน้ตบุ๊กใช้งานประมาณกี่เครื่อง"], "B4", "ID.AM-01"),
 F("E5", "eol", "S3", "sel", ["Workstations on end-of-life operating systems", "เครื่องที่ใช้ระบบปฏิบัติการหมดอายุการสนับสนุน"], ["What share of workstations run an operating system out of support?", "เครื่องที่ใช้ระบบปฏิบัติการหมดอายุการสนับสนุนมีสัดส่วนเท่าใด"], "B4", "PR.PS-02",
   [["lt5", "Below 5 percent", "ต่ำกว่าร้อยละ 5"], ["5to20", "5 to 20 percent", "ร้อยละ 5 ถึง 20"], ["gt20", "Above 20 percent", "มากกว่าร้อยละ 20"], UNK]),
 F("E6", "shws", "S3", "sel", ["Shared workstations in operational areas", "เครื่องใช้ร่วมกันในพื้นที่ปฏิบัติงาน"], ["Do several people use one logged-in workstation, for example at a service counter, nurse station, or production line?", "มีเครื่องที่หลายคนใช้ร่วมกันโดยล็อกอินค้างไว้หรือไม่ เช่น ที่เคาน์เตอร์บริการ เคาน์เตอร์พยาบาล หรือสายการผลิต"], "B4 B5", "PR.AA-01",
   [["yes", "Yes", "มี"], ["no", "No", "ไม่มี"], UNK]),
 F("E7", "otn", "S6", "num", ["Medical devices and operational technology (OT)", "อุปกรณ์การแพทย์และระบบควบคุมการปฏิบัติงาน (OT)"], ["About how many networked medical devices or OT devices are connected?", "มีอุปกรณ์การแพทย์หรืออุปกรณ์ OT ที่เชื่อมต่อเครือข่ายประมาณกี่เครื่อง"], "B4", "ID.AM-01"),
 F("E7", "otp", "S6", "sel", ["Medical device and OT network placement", "ตำแหน่งเครือข่ายของอุปกรณ์การแพทย์และ OT"], ["Are these devices on a separate network segment?", "อุปกรณ์เหล่านี้อยู่ในส่วนเครือข่ายแยกหรือไม่"], "B4", "PR.IR-01",
   [["sep", "Separate segment", "แยกส่วนเครือข่าย"], ["shared", "Shared with the corporate network", "อยู่ร่วมกับเครือข่ายสำนักงาน"], ["na", "No such devices", "ไม่มีอุปกรณ์ลักษณะนี้"], UNK]),
 F("E8", "bka", "S6", "sel", ["Backup architecture", "สถาปัตยกรรมการสำรองข้อมูล"], ["Is there a backup copy that ransomware cannot reach or delete?", "มีสำเนาข้อมูลสำรองที่แรนซัมแวร์เข้าถึงหรือลบไม่ได้หรือไม่"], "B4", "PR.DS-11",
   [["imm", "Offline or immutable copy", "มีสำเนาแบบ Offline หรือ Immutable"], ["online", "Online copy only", "มีเฉพาะสำเนาแบบออนไลน์"], ["none", "No central backup", "ไม่มีการสำรองข้อมูลส่วนกลาง"], UNK]),
 F("E10", "ith", "S1", "num", ["IT headcount", "จำนวนบุคลากร IT"], ["How many people work in IT, including contractors on site?", "มีบุคลากร IT กี่คน รวมผู้รับจ้างที่ประจำหน้างาน"], "B9", "GV.RR-03"),
 F("E10", "secr", "S1", "sel", ["Security role", "บทบาทด้านความมั่นคงปลอดภัย"], ["Who does security work day to day?", "ใครทำงานด้านความมั่นคงปลอดภัยในแต่ละวัน"], "B9", "GV.RR-02 GV.RR-03",
   [["ded", "Dedicated security role or team", "มีตำแหน่งหรือทีมเฉพาะ"], ["part", "Part-time, held by an IT role", "ทำควบคู่กับงาน IT"], ["none", "Nobody", "ไม่มีผู้รับผิดชอบ"]]),
 F("E10", "outs", "S1", "multi", ["Outsourced IT functions", "งาน IT ที่จ้างภายนอก"], ["Which IT functions does an outside company run?", "งาน IT ใดที่บริษัทภายนอกดูแล"], "B9", "GV.SC-04",
   [["sd", "Service desk", "Service desk"], ["infra", "Infrastructure", "โครงสร้างพื้นฐาน"], ["net", "Network", "เครือข่าย"], ["mon", "Security monitoring", "การเฝ้าระวังความมั่นคงปลอดภัย"],
    ["app", "Application support", "การดูแลแอปพลิเคชัน"], ["none", "None", "ไม่มี"]]),
]

def C(k, typ, n, o=()):
    return dict(k=k, type=typ, n=n, o=O(o))

ENV_TABLES = [
 dict(id="E1", k="sites", prefix="SITE", sess="S1", block=["B1", "B4"], n=["Sites", "สถานที่"], hint=["One row per hospital, branch, office, or data center in scope.", "หนึ่งแถวต่อโรงพยาบาล สาขา สำนักงาน หรือศูนย์ข้อมูลในขอบเขต"],
      cols=[C("name", "text", ["Site", "สถานที่"]),
            C("type", "sel", ["Type", "ประเภท"], [["hosp", "Hospital or plant", "โรงพยาบาลหรือโรงงาน"], ["branch", "Branch", "สาขา"], ["office", "Office", "สำนักงาน"], ["dc", "Data center", "ศูนย์ข้อมูล"], ["oth", "Other", "อื่น ๆ"]]),
            C("staff", "num", ["Staff", "จำนวนพนักงาน"])]),
 dict(id="E9", k="tools", prefix="TOOL", sess="S6", block=["B6"], n=["Security tool inventory", "รายการเครื่องมือด้านความมั่นคงปลอดภัย"], hint=["One row per security capability the client has, has bought, or plans. Record tools bought but not deployed: the Gap Analysis deploys them before it proposes anything new.", "หนึ่งแถวต่อขีดความสามารถด้านความมั่นคงปลอดภัยที่มีอยู่ ซื้อแล้ว หรือวางแผนไว้ บันทึกเครื่องมือที่ซื้อแล้วแต่ยังไม่ติดตั้งด้วย เพราะ Gap Analysis จะเสนอให้ใช้ของที่มีก่อนเสนอของใหม่"],
      cols=[C("cap", "sel", ["Capability", "ขีดความสามารถ"], [["fw", "Firewall", "Firewall"], ["edr", "Endpoint detection and response (EDR)", "Endpoint detection and response (EDR)"], ["av", "Antivirus", "Antivirus"],
              ["eml", "Email security", "ความปลอดภัยอีเมล"], ["log", "Central logging or SIEM", "Central logging หรือ SIEM"], ["bkp", "Backup", "การสำรองข้อมูล"], ["vs", "Vulnerability scanning", "การสแกนช่องโหว่"],
              ["pam", "Privileged access management (PAM)", "Privileged access management (PAM)"], ["mfa", "MFA provider", "ผู้ให้บริการ MFA"], ["waf", "Web application firewall (WAF)", "Web application firewall (WAF)"],
              ["dlp", "Data loss prevention (DLP)", "Data loss prevention (DLP)"], ["oth", "Other", "อื่น ๆ"]]),
            C("prod", "text", ["Product", "ผลิตภัณฑ์"]),
            C("cov", "sel", ["Coverage", "ความครอบคลุม"], [["full", "Full", "ครบ"], ["part", "Partial", "บางส่วน"], ["none", "None", "ไม่มี"]]),
            C("op", "sel", ["Operated by", "ผู้ดูแล"], [["inh", "In-house", "ทีมภายใน"], ["mssp", "MSSP", "MSSP"], ["vend", "Vendor", "ผู้ขาย"], ["nobody", "Nobody", "ไม่มีผู้ดูแล"]]),
            C("st", "sel", ["Status", "สถานะ"], [["use", "In use", "ใช้งานอยู่"], ["bnd", "Bought, not deployed", "ซื้อแล้ว ยังไม่ติดตั้ง"], ["plan", "Planned", "วางแผนไว้"]]),
            C("note", "text", ["Notes", "บันทึก"])]),
 dict(id="E11", k="hist", prefix="HIST", sess="S1", block=["B12"], n=["Incident history (last three years)", "ประวัติเหตุการณ์ (สามปีล่าสุด)"], hint=["Past security incidents the client confirms. Signs of an attack in progress go to the Observations tab as an Incident indicator, not here.", "เหตุการณ์ด้านความมั่นคงปลอดภัยในอดีตที่ลูกค้ายืนยัน หากพบสัญญาณการโจมตีที่ยังเกิดอยู่ ให้บันทึกในแท็บข้อสังเกตเป็นสัญญาณเหตุการณ์ ไม่ใช่ที่นี่"],
      cols=[C("date", "date", ["Date", "วันที่"]),
            C("type", "sel", ["Type", "ประเภท"], [["rw", "Ransomware", "แรนซัมแวร์"], ["acc", "Account compromise or phishing", "บัญชีถูกยึดหรือฟิชชิง"], ["mal", "Other malware", "มัลแวร์อื่น"],
              ["leak", "Data disclosure", "ข้อมูลรั่วไหล"], ["dos", "Service outage from an attack", "บริการหยุดจากการโจมตี"], ["oth", "Other", "อื่น ๆ"]]),
            C("sys", "text", ["Systems affected", "ระบบที่ได้รับผลกระทบ"]),
            C("imp", "text", ["Business impact", "ผลกระทบทางธุรกิจ"]),
            C("rep", "sel", ["Reported to a regulator", "แจ้งหน่วยงานกำกับ"], [["yes", "Yes", "แจ้งแล้ว"], ["no", "No", "ไม่ได้แจ้ง"], ["nr", "Not required", "ไม่ต้องแจ้ง"]])]),
 dict(id="E12", k="chg", prefix="CHG", sess="S3", block=["B13"], n=["Changes in flight", "การเปลี่ยนแปลงที่กำลังดำเนินการ"], hint=["Projects under way or planned that replace, move, or upgrade systems. The Gap Analysis checks every Improvement Action against this list.", "โครงการที่กำลังทำหรือวางแผนไว้ซึ่งจะเปลี่ยน ย้าย หรืออัปเกรดระบบ Gap Analysis จะตรวจ Improvement Action ทุกรายการกับรายการนี้"],
      cols=[C("proj", "text", ["Project", "โครงการ"]),
            C("sys", "sys", ["Affected systems", "ระบบที่เกี่ยวข้อง"]),
            C("date", "date", ["Target date", "วันที่เป้าหมาย"]),
            C("st", "sel", ["Status", "สถานะ"], [["plan", "Planned", "วางแผน"], ["prog", "In progress", "กำลังดำเนินการ"], ["contr", "Contracted", "ทำสัญญาแล้ว"]])]),
 dict(id="E13", k="prior", prefix="PRIOR", sess="S10", block=["B14"], n=["Prior assessments and audits", "การประเมินและการตรวจสอบครั้งก่อน"], hint=["Earlier audits and tests with their finding counts. Ask for the reports in the Document Request list.", "การตรวจสอบและการทดสอบครั้งก่อนพร้อมจำนวนข้อตรวจพบ ขอรายงานผ่านรายการขอเอกสาร"],
      cols=[C("type", "sel", ["Type", "ประเภท"], [["ia", "Internal audit", "ตรวจสอบภายใน"], ["ea", "External audit", "ตรวจสอบภายนอก"], ["pt", "Penetration test", "Penetration test"], ["cii", "CII audit", "การตรวจสอบ CII"], ["oth", "Other", "อื่น ๆ"]]),
            C("date", "date", ["Date", "วันที่"]),
            C("by", "text", ["Performed by", "ผู้ดำเนินการ"]),
            C("open", "num", ["Findings open", "ข้อตรวจพบที่ยังเปิด"]),
            C("closed", "num", ["Findings closed", "ข้อตรวจพบที่ปิดแล้ว"])]),
]

if __name__ == "__main__":
    print(len(ENV_FIELDS), "fields,", len(ENV_TABLES), "tables")
