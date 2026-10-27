# -*- coding: utf-8 -*-
"""System Profile and Vendor Profile fields for the Interview Assessment (spec: claude/interview-system-profile-spec.md v1.1).
Each option: [code, rating, EN, TH]. Rating: G Good, W Weak, P Poor, U Unknown, X not applicable.
samp: key of the System Sampling control (sessions.SYSCTL) that this field fills. ex: option is an exception candidate.
Pairs are (EN, TH). Thai text is a working translation and needs native review."""

UNK = ["unk", "U", "Unknown", "ไม่ทราบ"]

def F(id, sec, n, ask, feeds, opts, samp=None, ex=()):
    return dict(id=id, sec=sec, n=n, ask=ask, s=feeds.split(), o=opts, samp=samp, ex=list(ex))

PROFILE = [
 # ---------- Core: every system ----------
 F("C1", "core", ["Origin", "ที่มาของระบบ"], ["Was this system bought, built, or rented?", "ระบบนี้ซื้อมา พัฒนาเอง หรือเช่าใช้"], "ID.AM-02",
   [["cots", "G", "Commercial off-the-shelf (COTS), standard", "ซอฟต์แวร์สำเร็จรูป (COTS) ใช้ตามมาตรฐาน"],
    ["cotsc", "W", "COTS, customized", "ซอฟต์แวร์สำเร็จรูปที่ปรับแต่งเพิ่ม"],
    ["inh", "W", "In-house developed", "พัฒนาเองภายในองค์กร"],
    ["saas", "G", "Software as a service (SaaS)", "บริการซอฟต์แวร์บนคลาวด์ (SaaS)"],
    ["out", "W", "Outsourced custom build", "จ้างภายนอกพัฒนาเฉพาะ"]]),
 F("C2", "core", ["Users", "ผู้ใช้งาน"], ["Who logs in to this system?", "ใครบ้างที่ล็อกอินเข้าระบบนี้"], "",
   [["staff", "X", "Staff only", "พนักงานเท่านั้น"], ["vend", "X", "Staff and vendors", "พนักงานและผู้ขาย"],
    ["cust", "X", "Patients or customers", "ผู้ป่วยหรือลูกค้า"], ["pub", "X", "Public", "บุคคลทั่วไป"]]),
 F("C3", "core", ["Authentication", "วิธียืนยันตัวตน"], ["How do users log in?", "ผู้ใช้ล็อกอินด้วยวิธีใด"], "PR.AA-01 PR.AA-03",
   [["sso", "G", "Single sign-on through SAML or OpenID Connect", "Single sign-on ผ่าน SAML หรือ OpenID Connect"],
    ["dir", "G", "Directory, such as Active Directory or LDAP", "Directory เช่น Active Directory หรือ LDAP"],
    ["local", "W", "Local accounts in the application", "บัญชีภายในตัวระบบเอง"],
    ["shared", "P", "Shared account", "บัญชีใช้ร่วมกัน"], UNK]),
 F("C4", "core", ["Multi-factor authentication (MFA)", "การยืนยันตัวตนแบบหลายปัจจัย (MFA)"], ["Who must use a second factor to log in?", "ใครต้องใช้ปัจจัยที่สองในการล็อกอิน"], "PR.AA-03",
   [["all", "G", "All users", "ผู้ใช้ทุกคน"], ["adm", "W", "Administrators and remote access only", "เฉพาะผู้ดูแลระบบและการเข้าถึงระยะไกล"],
    ["rem", "W", "Remote access only", "เฉพาะการเข้าถึงระยะไกล"], ["none", "P", "None", "ไม่มี"],
    ["notsup", "P", "Not supported by the system", "ระบบไม่รองรับ"], UNK], samp="mfa", ex=["notsup"]),
 F("C5", "core", ["Administrator accounts", "บัญชีผู้ดูแลระบบ"], ["Who holds admin rights, and are the accounts named?", "ใครมีสิทธิ์ผู้ดูแลระบบ และบัญชีระบุตัวบุคคลหรือไม่"], "PR.AA-05",
   [["named", "G", "Named and limited", "ระบุชื่อและจำกัดจำนวน"], ["many", "W", "Named but too many", "ระบุชื่อแต่มีมากเกินไป"],
    ["shared", "P", "Shared or generic", "ใช้ร่วมกันหรือเป็นบัญชีกลาง"], ["vdef", "P", "Vendor default account in use", "ยังใช้บัญชีตั้งต้นของผู้ขาย"], UNK], samp="priv"),
 F("C6", "core", ["Internet exposure", "การเปิดสู่อินเทอร์เน็ต"], ["Can someone reach the login page from the internet?", "คนภายนอกเข้าถึงหน้าล็อกอินจากอินเทอร์เน็ตได้หรือไม่"], "PR.IR-01",
   [["no", "G", "Not exposed", "ไม่เปิดสู่อินเทอร์เน็ต"], ["vpn", "G", "Only through VPN or an access gateway", "ผ่าน VPN หรือ Access gateway เท่านั้น"],
    ["waf", "W", "Through a reverse proxy or web application firewall (WAF)", "ผ่าน Reverse proxy หรือ Web application firewall (WAF)"],
    ["direct", "P", "Directly exposed", "เปิดตรงสู่อินเทอร์เน็ต"], UNK]),
 F("C7", "core", ["Vendor remote access", "การเข้าถึงระยะไกลของผู้ขาย"], ["How does the vendor connect for support?", "ผู้ขายเชื่อมต่อเข้ามาดูแลระบบอย่างไร"], "DE.CM-06 GV.SC-05",
   [["none", "X", "No vendor access", "ผู้ขายไม่มีการเข้าถึง"], ["vpnm", "G", "VPN with MFA and logging", "VPN พร้อม MFA และบันทึกการใช้งาน"],
    ["vpn", "W", "VPN without MFA", "VPN ไม่มี MFA"], ["sup", "W", "Remote tool on request, supervised", "โปรแกรมรีโมตเปิดเมื่อร้องขอ มีคนคุม"],
    ["always", "P", "Remote tool always on, unattended", "โปรแกรมรีโมตเปิดค้างไว้ ไม่มีคนคุม"], UNK], samp="ven"),
 F("C8", "core", ["Platform support and patching", "การสนับสนุนและการแพตช์"], ["Is the version still supported, and when was it last patched?", "เวอร์ชันยังได้รับการสนับสนุนหรือไม่ และแพตช์ล่าสุดเมื่อใด"], "PR.PS-02",
   [["ok", "G", "Supported, patched within 30 days", "ยังได้รับการสนับสนุน แพตช์ภายใน 30 วัน"], ["late", "W", "Supported, patched late or ad hoc", "ยังได้รับการสนับสนุน แต่แพตช์ช้าหรือไม่เป็นรอบ"],
    ["eol", "P", "End of life", "หมดอายุการสนับสนุน"], ["vend", "U", "Vendor patches, status unknown", "ผู้ขายแพตช์ให้ ไม่ทราบสถานะ"], UNK], samp="pat", ex=["eol"]),
 F("C9", "core", ["Backup", "การสำรองข้อมูล"], ["How often is it backed up, and could ransomware delete the backup?", "สำรองข้อมูลบ่อยแค่ไหน และแรนซัมแวร์ลบข้อมูลสำรองได้หรือไม่"], "PR.DS-11",
   [["imm", "G", "Daily, with an offline or immutable copy", "ทุกวัน มีสำเนาแบบ Offline หรือ Immutable"], ["online", "W", "Daily, online only", "ทุกวัน แต่เก็บแบบออนไลน์เท่านั้น"],
    ["less", "W", "Less than daily", "น้อยกว่าวันละครั้ง"], ["none", "P", "None", "ไม่มี"], ["vend", "U", "Vendor-managed, not verified", "ผู้ขายดูแล ยังไม่ได้ตรวจสอบ"], UNK], samp="bkp"),
 F("C11", "core", ["Data held", "ข้อมูลที่จัดเก็บ"], ["Does this system hold personal data, and is any of it sensitive, for example health data?", "ระบบนี้เก็บข้อมูลส่วนบุคคลหรือไม่ และมีข้อมูลอ่อนไหว เช่น ข้อมูลสุขภาพ หรือไม่"], "ID.AM-07 PR.DS-01",
   [["none", "X", "No personal data", "ไม่มีข้อมูลส่วนบุคคล"], ["pd", "X", "Personal data", "ข้อมูลส่วนบุคคล"],
    ["spd", "X", "Sensitive personal data, for example health data", "ข้อมูลส่วนบุคคลที่อ่อนไหว เช่น ข้อมูลสุขภาพ"], ["unk", "X", "Unknown", "ไม่ทราบ"]]),
 # ---------- Full: Criticality A and sampled systems ----------
 F("F1", "full", ["System owner", "เจ้าของระบบ"], ["Who is accountable for this system on the business side?", "ใครรับผิดชอบระบบนี้ฝั่งธุรกิจ"], "ID.AM-05 GV.RR-02",
   [["bus", "G", "Named business owner", "มีเจ้าของฝั่งธุรกิจที่ระบุชื่อ"], ["it", "W", "IT owner only", "มีเฉพาะเจ้าของฝั่ง IT"], ["none", "P", "Nobody named", "ไม่มีผู้รับผิดชอบที่ระบุชื่อ"]], samp="own"),
 F("F2", "full", ["Account provisioning and removal", "การสร้างและลบบัญชีผู้ใช้"], ["What happens when someone joins, moves, or leaves?", "เมื่อมีคนเข้าใหม่ ย้าย หรือลาออก ทำอะไรกับบัญชีบ้าง"], "PR.AA-01",
   [["hr", "G", "Approved request linked to HR records", "มีการอนุมัติและเชื่อมกับข้อมูล HR"], ["man", "W", "Approved request, removal done manually", "มีการอนุมัติ แต่ลบบัญชีด้วยมือ"],
    ["noap", "P", "On request without approval", "สร้างตามคำขอ ไม่มีการอนุมัติ"], UNK]),
 F("F3", "full", ["Access review", "การทบทวนสิทธิ์"], ["When did someone last check who has access?", "ตรวจทานสิทธิ์ผู้ใช้ครั้งล่าสุดเมื่อใด"], "PR.AA-05",
   [["6m", "G", "Within 6 months", "ภายใน 6 เดือน"], ["12m", "W", "Within 12 months", "ภายใน 12 เดือน"], ["never", "P", "Over 12 months or never", "เกิน 12 เดือนหรือไม่เคย"], UNK], samp="uar"),
 F("F4", "full", ["Restore test", "การทดสอบกู้คืน"], ["When did you last restore this system from backup?", "กู้คืนระบบนี้จากข้อมูลสำรองครั้งล่าสุดเมื่อใด"], "PR.DS-11 RC.RP-03",
   [["full", "G", "Full restore within 12 months", "กู้คืนเต็มระบบภายใน 12 เดือน"], ["part", "W", "Partial restore within 12 months", "กู้คืนบางส่วนภายใน 12 เดือน"],
    ["never", "P", "Over 12 months or never", "เกิน 12 เดือนหรือไม่เคย"], UNK], samp="rst"),
 F("F5", "full", ["Recovery against tolerable downtime", "การกู้คืนเทียบกับเวลาหยุดที่รับได้"], ["Could you bring it back within the downtime the business accepts?", "กู้คืนได้ทันเวลาหยุดที่ธุรกิจรับได้หรือไม่"], "PR.IR-03 RC.RP-02",
   [["tested", "G", "Tested and meets it", "ทดสอบแล้วและทำได้ทัน"], ["exp", "W", "Expected to meet it, not tested", "คาดว่าทำได้ แต่ยังไม่ทดสอบ"],
    ["no", "P", "Will not meet it", "ทำไม่ทัน"], UNK], samp="dr"),
 F("F6", "full", ["Security logging", "การบันทึกด้านความมั่นคงปลอดภัย"], ["Where do login and admin logs go, and does anyone look at them?", "บันทึกการล็อกอินและงานผู้ดูแลระบบส่งไปที่ใด และมีใครตรวจดูหรือไม่"], "PR.PS-04 DE.CM-09",
   [["rev", "G", "Central logging or SIEM, reviewed", "ส่งเข้าระบบส่วนกลางหรือ SIEM และมีการตรวจดู"], ["cen", "W", "Central, not reviewed", "ส่งเข้าส่วนกลาง แต่ไม่มีการตรวจดู"],
    ["local", "W", "Local logs only", "เก็บในเครื่องเท่านั้น"], ["none", "P", "No security logs", "ไม่มีบันทึก"], UNK], samp="log"),
 F("F7", "full", ["Server protection", "การป้องกันเซิร์ฟเวอร์"], ["What protects the servers against malware?", "อะไรป้องกันเซิร์ฟเวอร์จากมัลแวร์"], "DE.CM-09",
   [["edr", "G", "Endpoint detection and response (EDR), monitored", "EDR และมีการเฝ้าระวัง"], ["av", "W", "Antivirus only", "Antivirus เท่านั้น"],
    ["none", "P", "None", "ไม่มี"], ["na", "X", "Appliance, not applicable", "เป็นอุปกรณ์ ไม่เกี่ยวข้อง"], UNK], samp="edr"),
 F("F8", "full", ["Encryption in transit", "การเข้ารหัสขณะส่งผ่าน"], ["Is traffic to and from this system encrypted?", "ข้อมูลที่รับส่งกับระบบนี้เข้ารหัสหรือไม่"], "PR.DS-02",
   [["all", "G", "All connections use TLS", "ทุกการเชื่อมต่อใช้ TLS"], ["some", "W", "Some connections", "บางการเชื่อมต่อ"], ["none", "P", "None", "ไม่มี"], UNK], samp="enc"),
 F("F9", "full", ["Encryption at rest", "การเข้ารหัสขณะจัดเก็บ"], ["Are the database and disks encrypted?", "ฐานข้อมูลและดิสก์เข้ารหัสหรือไม่"], "PR.DS-01",
   [["yes", "G", "Encrypted", "เข้ารหัส"], ["part", "W", "Partly", "บางส่วน"], ["no", "P", "Not encrypted", "ไม่เข้ารหัส"], UNK], samp="enc"),
 F("F10", "full", ["Network placement", "ตำแหน่งในเครือข่าย"], ["Which network segment is it in, and who can reach it?", "ระบบอยู่ในส่วนเครือข่ายใด และใครเข้าถึงได้"], "PR.IR-01",
   [["seg", "G", "Separate segment with filtered access", "แยกส่วนเครือข่ายและกรองการเข้าถึง"], ["shared", "W", "Shared server segment", "อยู่ในส่วนเซิร์ฟเวอร์ร่วมกับระบบอื่น"],
    ["flat", "P", "Flat network", "เครือข่ายไม่แบ่งส่วน"], UNK], samp="seg"),
 # ---------- Development: in-house, customized, or outsourced builds ----------
 F("D1", "dev", ["Who develops", "ผู้พัฒนา"], ["Who writes and changes the code today?", "ปัจจุบันใครเขียนและแก้ไขโค้ด"], "GV.SC-05 PR.PS-06",
   [["inh", "G", "In-house team", "ทีมภายใน"], ["vend", "W", "External vendor", "ผู้ขายภายนอก"], ["both", "W", "Both", "ทั้งสองฝ่าย"], ["gone", "P", "Original developer no longer available", "ผู้พัฒนาเดิมไม่อยู่แล้ว"]]),
 F("D2", "dev", ["Source code", "ซอร์สโค้ด"], ["Where is the source code kept, and who can change it?", "เก็บซอร์สโค้ดไว้ที่ใด และใครแก้ไขได้"], "PR.PS-06 GV.SC-05",
   [["repo", "G", "Central repository with access control and history, for example Git", "Repository กลางที่ควบคุมสิทธิ์และมีประวัติ เช่น Git"],
    ["share", "P", "File share or developer laptops", "File share หรือเครื่องของนักพัฒนา"], ["esc", "W", "Vendor only, with escrow", "ผู้ขายถือไว้ มี Escrow"],
    ["vonly", "P", "Vendor only, no escrow", "ผู้ขายถือไว้ ไม่มี Escrow"], UNK]),
 F("D3", "dev", ["Environments", "สภาพแวดล้อม"], ["Do you have separate development, test, and production?", "แยก Development, Test และ Production หรือไม่"], "PR.PS-06",
   [["three", "G", "All three separate", "แยกครบทั้งสาม"], ["two", "W", "Test and production only", "มีเฉพาะ Test และ Production"], ["prod", "P", "Production only", "มีเฉพาะ Production"]]),
 F("D4", "dev", ["Change and release", "การเปลี่ยนแปลงและการปล่อยระบบ"], ["How does a change reach production?", "การเปลี่ยนแปลงขึ้น Production อย่างไร"], "PR.PS-06 PR.PS-01",
   [["appr", "G", "Approved change with testing and rollback", "มีการอนุมัติ ทดสอบ และแผนย้อนกลับ"], ["inf", "W", "Tested informally", "ทดสอบแบบไม่เป็นทางการ"],
    ["direct", "P", "Developers change production directly", "นักพัฒนาแก้ไขบน Production โดยตรง"]]),
 F("D5", "dev", ["Security testing before release", "การทดสอบความมั่นคงปลอดภัยก่อนใช้งาน"], ["What security testing happens before go-live?", "ก่อนเปิดใช้งานมีการทดสอบด้านความมั่นคงปลอดภัยอะไรบ้าง"], "PR.PS-06 ID.RA-01",
   [["both", "G", "Code review or static analysis (SAST) plus penetration test", "Code review หรือ Static analysis (SAST) และ Penetration test"],
    ["pt", "W", "Penetration test only", "Penetration test เท่านั้น"], ["func", "P", "Functional testing only", "ทดสอบการทำงานเท่านั้น"], ["none", "P", "None", "ไม่มี"]]),
 F("D6", "dev", ["Last penetration test", "Penetration test ครั้งล่าสุด"], ["When was this system last penetration tested?", "ระบบนี้ทำ Penetration test ครั้งล่าสุดเมื่อใด"], "ID.RA-01",
   [["12m", "G", "Within 12 months", "ภายใน 12 เดือน"], ["3y", "W", "1 to 3 years ago", "1 ถึง 3 ปีก่อน"], ["never", "P", "Never", "ไม่เคย"], UNK]),
 F("D7", "dev", ["Third-party components", "ส่วนประกอบจากภายนอก"], ["Do you know which open-source libraries the system uses?", "ทราบหรือไม่ว่าระบบใช้ Open-source library ใดบ้าง"], "ID.RA-01 PR.PS-02",
   [["sca", "G", "Tracked with software composition analysis (SCA)", "ติดตามด้วย Software composition analysis (SCA)"], ["man", "W", "Listed manually", "จัดทำรายการด้วยมือ"], ["no", "P", "Not tracked", "ไม่ได้ติดตาม"]]),
 F("D8", "dev", ["Secrets", "ข้อมูลลับของระบบ"], ["Where are database passwords and API keys stored?", "รหัสผ่านฐานข้อมูลและ API key เก็บไว้ที่ใด"], "PR.DS-01 PR.AA-01",
   [["vault", "G", "Secrets vault", "Secrets vault"], ["cfg", "W", "Configuration files with restricted access", "ไฟล์ตั้งค่าที่จำกัดสิทธิ์"], ["hard", "P", "Hard-coded in the code", "ฝังไว้ในโค้ด"], UNK]),
 F("D9", "dev", ["Test data", "ข้อมูลทดสอบ"], ["What data do testers use?", "ผู้ทดสอบใช้ข้อมูลอะไร"], "PR.DS-01",
   [["mask", "G", "Masked or synthetic data", "ข้อมูลที่ปิดบังหรือสร้างขึ้น"], ["prod", "P", "Copy of production personal data", "สำเนาข้อมูลส่วนบุคคลจาก Production"], ["noenv", "P", "No test environment", "ไม่มีสภาพแวดล้อมทดสอบ"]]),
 F("D10", "dev", ["Secure coding standard", "มาตรฐานการเขียนโค้ดที่ปลอดภัย"], ["Do developers follow a written secure coding guideline?", "นักพัฒนาปฏิบัติตามแนวทางการเขียนโค้ดที่ปลอดภัยที่เป็นลายลักษณ์อักษรหรือไม่"], "PR.PS-06 PR.AT-02",
   [["yes", "G", "Approved and trained", "อนุมัติแล้วและมีการอบรม"], ["unused", "W", "Exists, not used", "มีแต่ไม่ได้ใช้"], ["none", "P", "None", "ไม่มี"]]),
 F("D11", "dev", ["Customization extent", "ระดับการปรับแต่ง"], ["How much custom code sits on top of the product? (COTS customized only)", "มีโค้ดที่เขียนเพิ่มบนผลิตภัณฑ์มากแค่ไหน (เฉพาะ COTS ที่ปรับแต่ง)"], "PR.PS-06",
   [["cfg", "G", "Configuration only", "ตั้งค่าเท่านั้น"], ["mod", "W", "Moderate custom code", "เขียนโค้ดเพิ่มปานกลาง"], ["heavy", "P", "Heavy custom code, for example custom ABAP in SAP", "เขียนโค้ดเพิ่มมาก เช่น Custom ABAP ใน SAP"]]),
 F("D12", "dev", ["Developer access to production", "สิทธิ์นักพัฒนาบน Production"], ["Can developers log in to production?", "นักพัฒนาล็อกอินเข้า Production ได้หรือไม่"], "PR.AA-05",
   [["no", "G", "No access", "ไม่มีสิทธิ์"], ["jit", "W", "Approved and logged access when needed", "เข้าได้เมื่อได้รับอนุมัติและมีบันทึก"], ["perm", "P", "Permanent access", "มีสิทธิ์ถาวร"]]),
]

DEV_ORIGINS = ["cotsc", "inh", "out"]

VENDOR = [
 F("V1", "ven", ["Service type", "ประเภทบริการ"], ["What does this vendor provide?", "ผู้ขายรายนี้ให้บริการอะไร"], "GV.SC-04",
   [["sw", "X", "Software vendor", "ผู้ขายซอฟต์แวร์"], ["msp", "X", "Managed IT service", "บริการ IT แบบ Managed service"], ["cloud", "X", "Cloud or SaaS provider", "ผู้ให้บริการคลาวด์หรือ SaaS"],
    ["med", "X", "Medical device vendor", "ผู้ขายอุปกรณ์การแพทย์"], ["bpo", "X", "Business process outsourcing", "จ้างทำกระบวนการธุรกิจ"], ["oth", "X", "Other", "อื่น ๆ"]]),
 F("V2", "ven", ["System access", "การเข้าถึงระบบ"], ["How does the vendor reach our systems?", "ผู้ขายเข้าถึงระบบของเราอย่างไร"], "GV.SC-04 DE.CM-06",
   [["none", "X", "None", "ไม่มี"], ["rem", "X", "Remote access", "เข้าถึงระยะไกล"], ["site", "X", "On-site access", "เข้าถึงที่หน้างาน"], ["host", "X", "Hosts our data", "เก็บข้อมูลของเราไว้"]]),
 F("V3", "ven", ["Data access", "การเข้าถึงข้อมูล"], ["What data can the vendor see?", "ผู้ขายเห็นข้อมูลอะไรได้บ้าง"], "GV.SC-04",
   [["none", "X", "None", "ไม่มี"], ["pd", "X", "Personal data", "ข้อมูลส่วนบุคคล"], ["spd", "X", "Sensitive personal data", "ข้อมูลส่วนบุคคลที่อ่อนไหว"]]),
 F("V4", "ven", ["Security clauses in contract", "ข้อกำหนดด้านความมั่นคงปลอดภัยในสัญญา"], ["Does the contract set security requirements and incident notification?", "สัญญากำหนดข้อกำหนดด้านความมั่นคงปลอดภัยและการแจ้งเหตุหรือไม่"], "GV.SC-05",
   [["full", "G", "Security requirements and incident notification", "มีข้อกำหนดด้านความมั่นคงปลอดภัยและการแจ้งเหตุ"], ["conf", "W", "Confidentiality only", "มีเฉพาะการรักษาความลับ"], ["none", "P", "None", "ไม่มี"], UNK]),
 F("V5", "ven", ["Data processing agreement", "ข้อตกลงการประมวลผลข้อมูล"], ["Is a data processing agreement signed under the PDPA?", "มีการลงนามข้อตกลงการประมวลผลข้อมูลตาม PDPA หรือไม่"], "GV.SC-05",
   [["yes", "G", "Signed", "ลงนามแล้ว"], ["no", "P", "Not signed", "ยังไม่ลงนาม"], ["na", "X", "Not applicable", "ไม่เกี่ยวข้อง"]]),
 F("V6", "ven", ["Security due diligence", "การตรวจสอบด้านความมั่นคงปลอดภัย"], ["When was the vendor's security last checked?", "ตรวจสอบความมั่นคงปลอดภัยของผู้ขายครั้งล่าสุดเมื่อใด"], "GV.SC-06 GV.SC-07",
   [["per", "G", "Before onboarding and periodically", "ก่อนเริ่มใช้และตรวจเป็นรอบ"], ["once", "W", "At onboarding only", "ตอนเริ่มใช้เท่านั้น"], ["never", "P", "Never", "ไม่เคย"]]),
 F("V7", "ven", ["Criticality", "ระดับความสำคัญ"], ["How much would the business suffer if this vendor failed?", "หากผู้ขายรายนี้มีปัญหา ธุรกิจจะได้รับผลกระทบมากแค่ไหน"], "GV.SC-04",
   [["A", "X", "A Critical", "A สำคัญมาก"], ["B", "X", "B Important", "B สำคัญ"], ["C", "X", "C Supporting", "C สนับสนุน"]]),
]

for f in PROFILE + VENDOR:
    f["o"] = [dict(c=c, r=r, n=[en, th]) for c, r, en, th in f["o"]]

if __name__ == "__main__":
    from sessions import SYSCTL
    keys = {c["k"] for c in SYSCTL}
    print(len(PROFILE), len(VENDOR), {f["samp"] for f in PROFILE if f["samp"]} - keys, keys - {f["samp"] for f in PROFILE if f["samp"]})
