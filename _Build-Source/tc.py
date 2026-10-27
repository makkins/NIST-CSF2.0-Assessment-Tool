# -*- coding: utf-8 -*-
"""Technical control checks for the technical interview track.
Each check: id, domain, CSF Subcategories, reference, check question (EN, TH), good practice (EN, TH).
References: CIS Critical Security Controls v8.1 Safeguard numbers (verify against the current CIS publication), ISO/IEC 27002:2022 controls, NIST SP 800-63B, NIST SP 800-82 Rev. 3, Thai Computer Crime Act s.26."""

DOMAINS = {
 "AST": (["Asset and software inventory", "ทะเบียนทรัพย์สินและซอฟต์แวร์"], "ITM SYSOWN"),
 "IAM": (["Identity and privileged access", "การบริหารตัวตนและสิทธิ์สูง"], "ITM"),
 "EP":  (["Endpoint protection and hardening", "การป้องกันและตั้งค่าเครื่องลูกข่ายและเซิร์ฟเวอร์"], "ITM SOC"),
 "NET": (["Network security and remote access", "ความมั่นคงปลอดภัยเครือข่ายและการเข้าถึงระยะไกล"], "ITM"),
 "EML": (["Email and web protection", "การป้องกันอีเมลและเว็บ"], "ITM"),
 "DATA":(["Data protection and encryption", "การปกป้องข้อมูลและการเข้ารหัส"], "ITM DPO"),
 "BKP": (["Backup and recovery", "การสำรองและกู้คืนข้อมูล"], "ITM BCM"),
 "VUL": (["Vulnerability and patch management", "การบริหารช่องโหว่และแพตช์"], "ITM SOC"),
 "LOG": (["Logging and security monitoring", "การบันทึกและเฝ้าระวังความมั่นคงปลอดภัย"], "SOC ITM"),
 "CLD": (["Cloud and Microsoft 365", "คลาวด์และ Microsoft 365"], "ITM"),
 "APP": (["Application security", "ความมั่นคงปลอดภัยของระบบงาน"], "DEV SYSOWN"),
 "SUP": (["Third-party technical access", "การเข้าถึงทางเทคนิคของผู้ให้บริการ"], "ITM PROC"),
 "OT":  (["OT and medical devices", "ระบบ OT และอุปกรณ์การแพทย์"], "ITM SYSOWN"),
 "PHY": (["Physical and environmental", "ความมั่นคงปลอดภัยทางกายภาพและสิ่งแวดล้อม"], "FAC ITM"),
 "IR":  (["Incident response readiness", "ความพร้อมรับมือเหตุการณ์"], "SOC CISO"),
}

TC = []
def c(id, d, subs, ref, q_en, q_th, g_en, g_th, pack=None):
    """pack: industry pack ID (packs.py). A pack check shows only when that pack is selected."""
    x = dict(id=id, d=d, s=subs.split(), ref=ref, q=[q_en, q_th], g=[g_en, g_th])
    if pack:
        x["pack"] = pack
    TC.append(x)

# AST
c("AST-01","AST","ID.AM-01","CIS 1.1, 1.3",
  "Is there a hardware inventory that covers servers, endpoints, network devices, and mobile devices, fed by an automated discovery tool?",
  "มีทะเบียนฮาร์ดแวร์ที่ครอบคลุมเซิร์ฟเวอร์ เครื่องลูกข่าย อุปกรณ์เครือข่าย และอุปกรณ์เคลื่อนที่ และได้ข้อมูลจากเครื่องมือสำรวจอัตโนมัติหรือไม่",
  "One inventory with owner, location, and criticality for every asset; discovery runs at least weekly; reconciled with procurement records at least every six months.",
  "มีทะเบียนเดียวที่ระบุเจ้าของ ที่ตั้ง และระดับความสำคัญของทุกทรัพย์สิน เครื่องมือสำรวจทำงานอย่างน้อยสัปดาห์ละครั้ง และกระทบยอดกับข้อมูลจัดซื้ออย่างน้อยทุก 6 เดือน")
c("AST-02","AST","ID.AM-01 PR.IR-01","CIS 1.2",
  "What happens when an unknown device connects to the network?",
  "เมื่อมีอุปกรณ์ที่ไม่รู้จักเชื่อมต่อเครือข่ายจะเกิดอะไรขึ้น",
  "Unknown devices are detected and removed, quarantined, or added to the inventory within one week; network access control (NAC) or port security blocks unmanaged devices on sensitive segments.",
  "ตรวจพบอุปกรณ์ที่ไม่รู้จักและนำออก กักแยก หรือเพิ่มเข้าทะเบียนภายในหนึ่งสัปดาห์ และใช้การควบคุมการเข้าถึงเครือข่าย (NAC) หรือ Port Security กันอุปกรณ์ที่ไม่ได้บริหารจัดการออกจากเครือข่ายส่วนที่อ่อนไหว")
c("AST-03","AST","ID.AM-02 PR.PS-02","CIS 2.1, 2.2",
  "Is there a software inventory with version and vendor support status, and is unsupported software flagged?",
  "มีทะเบียนซอฟต์แวร์ที่ระบุเวอร์ชันและสถานะการสนับสนุนจากผู้ขาย และมีการระบุซอฟต์แวร์ที่หมดการสนับสนุนหรือไม่",
  "Inventory reviewed at least every six months; unsupported software has a documented exception with compensating controls and a replacement date.",
  "ทบทวนทะเบียนอย่างน้อยทุก 6 เดือน ซอฟต์แวร์ที่หมดการสนับสนุนมีการยกเว้นเป็นลายลักษณ์อักษรพร้อมมาตรการชดเชยและวันที่ทดแทน")
c("AST-04","AST","ID.AM-02 ID.AM-04","CIS 2.1, 15.1",
  "Are cloud and software as a service (SaaS) applications in use known, including those bought by departments?",
  "ทราบหรือไม่ว่ามีการใช้แอปพลิเคชันคลาวด์และซอฟต์แวร์แบบบริการ (SaaS) ใดบ้าง รวมถึงที่หน่วยงานซื้อเอง",
  "SaaS discovery through firewall, proxy, or cloud access security broker (CASB) logs; each service has a business owner and is linked to the supplier inventory.",
  "สำรวจ SaaS จากบันทึกของไฟร์วอลล์ พร็อกซี หรือ Cloud Access Security Broker (CASB) ทุกบริการมีเจ้าของฝั่งธุรกิจและเชื่อมกับทะเบียนผู้ให้บริการ")
c("AST-05","AST","ID.AM-03","CIS 12.4, 3.8",
  "Are network architecture and data flow diagrams current, and do they show internet, supplier, and cloud connections?",
  "แผนผังสถาปัตยกรรมเครือข่ายและการไหลของข้อมูลเป็นปัจจุบัน และแสดงการเชื่อมต่ออินเทอร์เน็ต ผู้ให้บริการ และคลาวด์หรือไม่",
  "Diagrams updated after every significant change and reviewed at least annually; they show segments, firewalls, and where sensitive data flows.",
  "ปรับปรุงแผนผังทุกครั้งที่มีการเปลี่ยนแปลงสำคัญและทบทวนอย่างน้อยปีละครั้ง แสดงส่วนของเครือข่าย ไฟร์วอลล์ และเส้นทางของข้อมูลอ่อนไหว")

# IAM
c("IAM-01","IAM","PR.AA-03","CIS 6.3, 6.4, 6.5",
  "Is multi-factor authentication (MFA) enforced for email, remote access (VPN), cloud administration, and all administrator accounts?",
  "บังคับใช้การยืนยันตัวตนหลายปัจจัย (MFA) กับอีเมล การเข้าถึงระยะไกล (VPN) การดูแลคลาวด์ และบัญชีผู้ดูแลระบบทั้งหมดหรือไม่",
  "MFA on 100% of externally exposed applications, remote access, and administrative access; phishing-resistant methods (FIDO2 or number matching) for administrators; no SMS for privileged accounts.",
  "ใช้ MFA ครบทุกระบบที่เข้าถึงจากภายนอก การเข้าถึงระยะไกล และการเข้าถึงสิทธิ์ผู้ดูแล ใช้วิธีที่ทนต่อฟิชชิง (FIDO2 หรือ Number Matching) สำหรับผู้ดูแลระบบ และไม่ใช้ SMS กับบัญชีสิทธิ์สูง")
c("IAM-02","IAM","PR.AA-01 GV.RR-04","CIS 6.1, 6.2, 5.3",
  "How quickly are accounts disabled when staff leave, and are dormant accounts disabled automatically?",
  "บัญชีถูกระงับเร็วเพียงใดเมื่อพนักงานลาออก และบัญชีที่ไม่ได้ใช้งานถูกระงับอัตโนมัติหรือไม่",
  "Leaver accounts disabled on the last working day, triggered by HR; accounts unused for 45 days disabled automatically; monthly reconciliation of HR list against active accounts.",
  "ระงับบัญชีของผู้ลาออกในวันทำงานสุดท้ายโดยมี HR เป็นผู้แจ้ง ระงับบัญชีที่ไม่ใช้งาน 45 วันโดยอัตโนมัติ และกระทบยอดรายชื่อจาก HR กับบัญชีที่ใช้งานอยู่ทุกเดือน")
c("IAM-03","IAM","PR.AA-05","CIS 5.4, 12.8",
  "Do administrators use separate accounts for admin work, and how many domain or global administrators exist?",
  "ผู้ดูแลระบบใช้บัญชีแยกสำหรับงานดูแลระบบหรือไม่ และมีผู้ดูแลโดเมนหรือ Global Administrator กี่ราย",
  "Dedicated admin accounts without email or internet browsing; domain or global administrators kept to a small named group (typically 2 to 4); admin work from hardened admin workstations.",
  "ใช้บัญชีผู้ดูแลแยกที่ไม่มีอีเมลและไม่ใช้ท่องเว็บ จำกัดผู้ดูแลโดเมนหรือ Global Administrator ไว้กลุ่มเล็กที่ระบุชื่อ (โดยทั่วไป 2 ถึง 4 ราย) และทำงานดูแลระบบจากเครื่องที่ตั้งค่าความปลอดภัยเฉพาะ")
c("IAM-04","IAM","PR.AA-05","CIS 5.4, 6.8",
  "Is privileged access managed with a privileged access management (PAM) tool or password vault, with session logging?",
  "มีการบริหารสิทธิ์สูงด้วยเครื่องมือบริหารสิทธิ์สูง (PAM) หรือที่เก็บรหัสผ่าน พร้อมการบันทึกเซสชันหรือไม่",
  "Privileged passwords vaulted and rotated; just-in-time elevation where possible; privileged sessions recorded for critical systems; local administrator passwords unique per machine (for example Windows LAPS).",
  "เก็บรหัสผ่านสิทธิ์สูงในที่เก็บรหัสผ่านและหมุนเวียนเปลี่ยน ยกระดับสิทธิ์เฉพาะเมื่อจำเป็น บันทึกเซสชันสิทธิ์สูงในระบบสำคัญ และรหัสผ่านผู้ดูแลเครื่องไม่ซ้ำกันในแต่ละเครื่อง (เช่น Windows LAPS)")
c("IAM-05","IAM","PR.AA-05","CIS 6.1, 6.8",
  "Are user access reviews performed for critical systems, and is access granted by role?",
  "มีการทบทวนสิทธิ์ผู้ใช้ของระบบสำคัญ และให้สิทธิ์ตามบทบาทหรือไม่",
  "Role-based access defined with system owners; access reviews at least every six months for critical systems (quarterly for privileged access); removals completed and evidenced.",
  "กำหนดสิทธิ์ตามบทบาทร่วมกับเจ้าของระบบ ทบทวนสิทธิ์ระบบสำคัญอย่างน้อยทุก 6 เดือน (สิทธิ์สูงทุกไตรมาส) และถอนสิทธิ์ครบถ้วนพร้อมหลักฐาน")
c("IAM-06","IAM","PR.AA-01","CIS 5.5, 5.2",
  "Are service accounts and shared accounts inventoried, owned, and protected with strong unique passwords?",
  "บัญชีบริการและบัญชีที่ใช้ร่วมกันมีทะเบียน มีเจ้าของ และใช้รหัสผ่านที่แข็งแรงไม่ซ้ำกันหรือไม่",
  "Service account inventory reviewed quarterly; no interactive logon for service accounts; managed service accounts or vaulted passwords; shared accounts removed or tied to named users.",
  "ทบทวนทะเบียนบัญชีบริการทุกไตรมาส บัญชีบริการเข้าสู่ระบบแบบโต้ตอบไม่ได้ ใช้ Managed Service Account หรือเก็บรหัสในที่เก็บรหัสผ่าน และยกเลิกบัญชีใช้ร่วมหรือผูกกับผู้ใช้ที่ระบุชื่อ")
c("IAM-07","IAM","PR.AA-03 PR.AA-04","CIS 5.2, 6.7; NIST SP 800-63B",
  "What is the password standard, and is single sign-on (SSO) used for business applications?",
  "มาตรฐานรหัสผ่านคืออะไร และใช้การลงชื่อเข้าใช้ครั้งเดียว (SSO) กับระบบงานหรือไม่",
  "Minimum 8 characters with MFA or 14 without, checked against breached-password lists, no forced periodic change without cause (NIST SP 800-63B); SSO through a central identity provider for business applications.",
  "ความยาวอย่างน้อย 8 ตัวอักษรเมื่อใช้ MFA หรือ 14 ตัวอักษรเมื่อไม่ใช้ ตรวจกับรายการรหัสผ่านที่รั่วไหล ไม่บังคับเปลี่ยนตามรอบโดยไม่มีเหตุ (NIST SP 800-63B) และใช้ SSO ผ่านผู้ให้บริการตัวตนส่วนกลางกับระบบงาน")
c("IAM-08","IAM","PR.AA-02","ISO/IEC 27002:2022 5.16, 5.17",
  "How does the service desk verify identity before a password or MFA reset?",
  "Service Desk ยืนยันตัวตนอย่างไรก่อนรีเซ็ตรหัสผ่านหรือ MFA",
  "Documented verification (call-back to a registered number, manager approval, or video check); MFA resets for administrators need a second approver; reset requests logged.",
  "มีขั้นตอนยืนยันตัวตนเป็นลายลักษณ์อักษร (โทรกลับเบอร์ที่ลงทะเบียน การอนุมัติจากหัวหน้า หรือตรวจผ่านวิดีโอ) การรีเซ็ต MFA ของผู้ดูแลต้องมีผู้อนุมัติคนที่สอง และบันทึกทุกคำขอ")

# EP
c("EP-01","EP","DE.CM-09 PR.PS-05","CIS 10.1, 10.6, 10.7",
  "Is endpoint detection and response (EDR) or antimalware installed on all endpoints and servers, centrally managed?",
  "ติดตั้งระบบตรวจจับและตอบสนองที่เครื่องลูกข่าย (EDR) หรือ Antimalware ครบทุกเครื่องลูกข่ายและเซิร์ฟเวอร์ และบริหารจากส่วนกลางหรือไม่",
  "EDR with behavior-based detection on at least 98% of endpoints and servers; coverage gaps reported weekly; tamper protection on; alerts monitored 24/7 in-house or by a managed service.",
  "ติดตั้ง EDR ที่ตรวจจับจากพฤติกรรมอย่างน้อยร้อยละ 98 ของเครื่องลูกข่ายและเซิร์ฟเวอร์ รายงานเครื่องที่ยังไม่ครอบคลุมทุกสัปดาห์ เปิดการป้องกันการปิดระบบ และเฝ้าดูการแจ้งเตือนตลอด 24 ชั่วโมงโดยทีมภายในหรือผู้ให้บริการ")
c("EP-02","EP","PR.PS-05 PR.AA-05","CIS 5.4, 2.5",
  "Do standard users have local administrator rights, and is unapproved software blocked?",
  "ผู้ใช้ทั่วไปมีสิทธิ์ผู้ดูแลเครื่องหรือไม่ และมีการบล็อกซอฟต์แวร์ที่ไม่ได้รับอนุญาตหรือไม่",
  "No local admin rights for standard users; software installed through a managed catalog; application allowlisting on servers and high-risk endpoints.",
  "ผู้ใช้ทั่วไปไม่มีสิทธิ์ผู้ดูแลเครื่อง ติดตั้งซอฟต์แวร์ผ่านแคตตาล็อกที่บริหารจัดการ และใช้การอนุญาตเฉพาะโปรแกรมที่กำหนดบนเซิร์ฟเวอร์และเครื่องที่มีความเสี่ยงสูง")
c("EP-03","EP","PR.PS-01","CIS 4.1, 4.8",
  "Are secure configuration baselines (for example CIS Benchmarks) applied to Windows, servers, and network devices, and is drift checked?",
  "มีการใช้ค่ามาตรฐานการตั้งค่าที่ปลอดภัย (เช่น CIS Benchmarks) กับ Windows เซิร์ฟเวอร์ และอุปกรณ์เครือข่าย และตรวจการเบี่ยงเบนหรือไม่",
  "Baselines documented and deployed through group policy or endpoint management; unnecessary services disabled; compliance scanned at least quarterly.",
  "มีค่ามาตรฐานเป็นลายลักษณ์อักษรและนำไปใช้ผ่าน Group Policy หรือระบบบริหารเครื่องลูกข่าย ปิดบริการที่ไม่จำเป็น และสแกนความสอดคล้องอย่างน้อยทุกไตรมาส")
c("EP-04","EP","PR.DS-10","CIS 4.3, 4.10",
  "Are screen lock and session timeout enforced on all endpoints?",
  "บังคับใช้การล็อกหน้าจอและการหมดเวลาเซสชันกับเครื่องลูกข่ายทุกเครื่องหรือไม่",
  "Automatic lock after 15 minutes or less on workstations and 2 minutes on mobile devices; shared clinical or kiosk devices use fast user switching or tap-and-go.",
  "ล็อกอัตโนมัติภายใน 15 นาทีบนเครื่องลูกข่าย และ 2 นาทีบนอุปกรณ์เคลื่อนที่ เครื่องที่ใช้ร่วมกันใช้การสลับผู้ใช้อย่างรวดเร็วหรือแตะบัตรเข้าใช้")
c("EP-05","EP","PR.DS-01","CIS 3.6, 3.9",
  "Is full-disk encryption enabled on laptops, and is removable media controlled?",
  "เปิดการเข้ารหัสทั้งดิสก์บนโน้ตบุ๊ก และควบคุมสื่อบันทึกข้อมูลแบบถอดได้หรือไม่",
  "BitLocker or FileVault on 100% of laptops with recovery keys escrowed; USB storage blocked or encrypted by policy; autorun disabled (CIS 10.3).",
  "เปิด BitLocker หรือ FileVault ครบทุกโน้ตบุ๊กและเก็บกุญแจกู้คืนไว้ส่วนกลาง บล็อกหรือบังคับเข้ารหัส USB ตามนโยบาย และปิด Autorun (CIS 10.3)")
c("EP-06","EP","PR.IR-01","CIS 4.4, 4.5",
  "Are host firewalls enabled on servers and endpoints with default-deny inbound rules?",
  "เปิดไฟร์วอลล์ประจำเครื่องบนเซิร์ฟเวอร์และเครื่องลูกข่าย โดยปฏิเสธการเชื่อมต่อขาเข้าเป็นค่าเริ่มต้นหรือไม่",
  "Host firewall on for all profiles; inbound blocked except required services; workstation-to-workstation SMB and RDP blocked to slow ransomware spread.",
  "เปิดไฟร์วอลล์ประจำเครื่องทุกโปรไฟล์ บล็อกขาเข้ายกเว้นบริการที่จำเป็น และบล็อก SMB และ RDP ระหว่างเครื่องลูกข่ายเพื่อชะลอการแพร่ของแรนซัมแวร์")

# NET
c("NET-01","NET","PR.IR-01","CIS 12.2, 13.4",
  "Is the network segmented, with servers, users, guests, management, and OT or medical devices in separate zones with filtered traffic between them?",
  "มีการแบ่งส่วนเครือข่าย โดยแยกเซิร์ฟเวอร์ ผู้ใช้ ผู้มาติดต่อ ระบบบริหารจัดการ และ OT หรืออุปกรณ์การแพทย์ ออกเป็นโซน และกรองการรับส่งข้อมูลระหว่างโซนหรือไม่",
  "Zones defined by function and sensitivity; firewall rules between zones on a least-privilege basis; guest Wi-Fi isolated from internal networks.",
  "กำหนดโซนตามหน้าที่และความอ่อนไหว กำหนดกฎไฟร์วอลล์ระหว่างโซนตามหลักสิทธิ์น้อยที่สุด และแยก Wi-Fi ผู้มาติดต่อออกจากเครือข่ายภายใน")
c("NET-02","NET","PR.IR-01 ID.RA-07","CIS 4.2, 12.3",
  "Are firewall rules reviewed regularly, and are any-any or temporary rules removed?",
  "มีการทบทวนกฎไฟร์วอลล์สม่ำเสมอ และนำกฎ Any-Any หรือกฎชั่วคราวออกหรือไม่",
  "Rule review at least every six months; each rule has an owner, business reason, and expiry if temporary; changes go through change management.",
  "ทบทวนกฎอย่างน้อยทุก 6 เดือน ทุกกฎมีเจ้าของ เหตุผลทางธุรกิจ และวันหมดอายุหากเป็นกฎชั่วคราว และการเปลี่ยนแปลงผ่านกระบวนการบริหารการเปลี่ยนแปลง")
c("NET-03","NET","PR.AA-03 PR.IR-01","CIS 12.7, 6.4, 13.5",
  "How is remote access provided (VPN, remote desktop tools), and is remote desktop protocol (RDP) exposed to the internet?",
  "ให้การเข้าถึงระยะไกลอย่างไร (VPN หรือเครื่องมือควบคุมระยะไกล) และมี Remote Desktop Protocol (RDP) เปิดสู่อินเทอร์เน็ตหรือไม่",
  "Remote access only through VPN or zero trust access with MFA; no RDP, SMB, or admin interfaces exposed to the internet; VPN appliances patched within days of critical advisories.",
  "เข้าถึงระยะไกลผ่าน VPN หรือ Zero Trust Access ที่มี MFA เท่านั้น ไม่เปิด RDP SMB หรือหน้าจอผู้ดูแลสู่อินเทอร์เน็ต และแพตช์อุปกรณ์ VPN ภายในไม่กี่วันหลังมีประกาศช่องโหว่วิกฤต")
c("NET-04","NET","PR.IR-01 PR.PS-01","CIS 12.3, 12.6, 4.7",
  "Are network devices managed through a separate management network with secure protocols, and are default passwords changed?",
  "อุปกรณ์เครือข่ายถูกบริหารผ่านเครือข่ายบริหารจัดการที่แยกต่างหากด้วยโปรโตคอลที่ปลอดภัย และเปลี่ยนรหัสผ่านเริ่มต้นแล้วหรือไม่",
  "Management interfaces only on a management VLAN; SSH and HTTPS only (no Telnet or HTTP); default accounts disabled or renamed; configurations backed up.",
  "หน้าจอผู้ดูแลอยู่ใน VLAN บริหารจัดการเท่านั้น ใช้ SSH และ HTTPS เท่านั้น (ไม่ใช้ Telnet หรือ HTTP) ปิดหรือเปลี่ยนชื่อบัญชีเริ่มต้น และสำรองค่าการตั้งค่า")
c("NET-05","NET","DE.CM-01","CIS 13.3, 13.6",
  "Is network traffic monitored, for example with intrusion detection or prevention (IDS/IPS) and flow logs?",
  "มีการเฝ้าระวังการรับส่งข้อมูลบนเครือข่ายหรือไม่ เช่น ระบบตรวจจับหรือป้องกันการบุกรุก (IDS/IPS) และบันทึก Flow",
  "IDS/IPS at the internet edge and between critical zones; NetFlow or firewall logs sent to the security information and event management (SIEM) system; alerts reviewed daily.",
  "มี IDS/IPS ที่ขอบอินเทอร์เน็ตและระหว่างโซนสำคัญ ส่ง NetFlow หรือบันทึกไฟร์วอลล์เข้าระบบ SIEM และทบทวนการแจ้งเตือนทุกวัน")
c("NET-06","NET","PR.IR-04","ISO/IEC 27002:2022 8.6, 8.20",
  "Are internet-facing services protected against denial-of-service (DoS) attacks and capacity problems?",
  "บริการที่เปิดสู่อินเทอร์เน็ตได้รับการป้องกันการโจมตีแบบปฏิเสธการให้บริการ (DoS) และปัญหาขีดความสามารถหรือไม่",
  "DDoS protection from the internet provider or a cloud service for critical public services; bandwidth and resource alerts set at about 80%; redundant internet links for critical sites.",
  "ใช้การป้องกัน DDoS จากผู้ให้บริการอินเทอร์เน็ตหรือบริการคลาวด์กับบริการสาธารณะที่สำคัญ ตั้งการแจ้งเตือนแบนด์วิดท์และทรัพยากรที่ประมาณร้อยละ 80 และมีลิงก์อินเทอร์เน็ตสำรองสำหรับไซต์สำคัญ")

# EML
c("EML-01","EML","PR.DS-02 DE.CM-09","CIS 9.5",
  "Are SPF, DKIM, and DMARC configured for your email domains, and is DMARC set to quarantine or reject?",
  "ตั้งค่า SPF, DKIM และ DMARC ให้โดเมนอีเมลแล้ว และ DMARC ตั้งเป็น Quarantine หรือ Reject หรือไม่",
  "SPF and DKIM on all sending domains; DMARC at p=quarantine or p=reject with reports monitored; parked domains set to reject.",
  "ตั้ง SPF และ DKIM ทุกโดเมนที่ส่งอีเมล DMARC อยู่ที่ p=quarantine หรือ p=reject และติดตามรายงาน โดเมนที่ไม่ใช้งานตั้งเป็น Reject")
c("EML-02","EML","DE.CM-09 PR.PS-05","CIS 9.6, 9.7",
  "Does the email gateway scan attachments and links, block dangerous file types, and sandbox suspicious files?",
  "Email Gateway สแกนไฟล์แนบและลิงก์ บล็อกไฟล์ประเภทอันตราย และทดสอบไฟล์ต้องสงสัยใน Sandbox หรือไม่",
  "Executable and macro-enabled attachments blocked by default; links rewritten and checked at click time; attachment sandboxing; external email banner.",
  "บล็อกไฟล์แนบที่เรียกใช้ได้และไฟล์ที่มีมาโครเป็นค่าเริ่มต้น ตรวจลิงก์ ณ เวลาที่คลิก ทดสอบไฟล์แนบใน Sandbox และแสดงป้ายเตือนอีเมลจากภายนอก")
c("EML-03","EML","DE.CM-09 PR.IR-01","CIS 9.2, 9.3",
  "Is DNS filtering or a web proxy used to block malicious and uncategorized websites?",
  "ใช้ DNS Filtering หรือ Web Proxy บล็อกเว็บไซต์อันตรายและเว็บไซต์ที่ไม่มีการจัดหมวดหรือไม่",
  "DNS filtering for all devices, including off-network laptops; URL category filtering blocks malware, phishing, and newly registered domains.",
  "ใช้ DNS Filtering กับทุกอุปกรณ์ รวมถึงโน้ตบุ๊กที่อยู่นอกเครือข่าย และกรองตามหมวด URL เพื่อบล็อกมัลแวร์ ฟิชชิง และโดเมนที่เพิ่งจดทะเบียน")
c("EML-04","EML","PR.AT-01 RS.MA-02","CIS 14.2, 14.6",
  "Can users report suspicious email with one click, and are phishing simulations run?",
  "ผู้ใช้แจ้งอีเมลต้องสงสัยได้ด้วยการคลิกครั้งเดียว และมีการจำลองฟิชชิงหรือไม่",
  "Report-phish button in the mail client feeding the security team; simulations at least quarterly; click and report rates tracked and trending better.",
  "มีปุ่มแจ้งฟิชชิงในโปรแกรมอีเมลส่งถึงทีมความมั่นคงปลอดภัย จำลองฟิชชิงอย่างน้อยทุกไตรมาส และติดตามอัตราการคลิกและการแจ้งให้มีแนวโน้มดีขึ้น")

# DATA
c("DATA-01","DATA","PR.DS-01 ID.AM-07","CIS 3.11, 3.12",
  "Is sensitive data encrypted at rest in databases, file shares, and backups, and stored in restricted locations?",
  "ข้อมูลอ่อนไหวได้รับการเข้ารหัสขณะจัดเก็บในฐานข้อมูล ที่เก็บไฟล์ส่วนกลาง และข้อมูลสำรอง และเก็บในตำแหน่งที่จำกัดสิทธิ์หรือไม่",
  "Database or storage encryption for systems holding health, ID card, or financial data; sensitive data kept in designated systems, not on local drives or open shares.",
  "เข้ารหัสฐานข้อมูลหรือที่จัดเก็บสำหรับระบบที่มีข้อมูลสุขภาพ บัตรประชาชน หรือการเงิน และเก็บข้อมูลอ่อนไหวในระบบที่กำหนด ไม่เก็บในเครื่องหรือโฟลเดอร์ที่เปิดกว้าง")
c("DATA-02","DATA","PR.DS-02","CIS 3.10",
  "Is data in transit encrypted (TLS 1.2 or higher), including internal applications and file transfers?",
  "ข้อมูลระหว่างการส่งได้รับการเข้ารหัส (TLS 1.2 ขึ้นไป) รวมถึงระบบงานภายในและการโอนไฟล์หรือไม่",
  "TLS 1.2 or 1.3 on all web applications and APIs; legacy protocols (SSL, TLS 1.0 and 1.1, FTP) disabled; secure file transfer (SFTP or a managed sharing tool) for external exchange.",
  "ใช้ TLS 1.2 หรือ 1.3 กับเว็บแอปพลิเคชันและ API ทั้งหมด ปิดโปรโตคอลเก่า (SSL, TLS 1.0 และ 1.1, FTP) และใช้การโอนไฟล์ที่ปลอดภัย (SFTP หรือเครื่องมือแชร์ที่บริหารจัดการ) กับภายนอก")
c("DATA-03","DATA","PR.DS-01 PR.AA-05","CIS 3.3",
  "Are file shares and SharePoint or OneDrive permissions reviewed, and is 'Everyone' or anonymous link sharing restricted?",
  "มีการทบทวนสิทธิ์ของโฟลเดอร์ส่วนกลางและ SharePoint หรือ OneDrive และจำกัดการแชร์แบบ 'Everyone' หรือลิงก์ไม่ระบุตัวตนหรือไม่",
  "No sensitive folders shared with Everyone or anonymous links; external sharing limited to approved domains; permission reports reviewed at least every six months.",
  "ไม่มีโฟลเดอร์ข้อมูลอ่อนไหวแชร์กับ Everyone หรือลิงก์ไม่ระบุตัวตน จำกัดการแชร์ภายนอกเฉพาะโดเมนที่อนุมัติ และทบทวนรายงานสิทธิ์อย่างน้อยทุก 6 เดือน")
c("DATA-04","DATA","PR.DS-01 PR.DS-02","CIS 3.13",
  "Is data loss prevention (DLP) used to detect or block sensitive data leaving by email, web, or USB?",
  "ใช้ระบบป้องกันข้อมูลรั่วไหล (DLP) ตรวจจับหรือบล็อกข้อมูลอ่อนไหวที่ออกทางอีเมล เว็บ หรือ USB หรือไม่",
  "DLP rules for Thai ID card numbers, health records, and financial data on email and cloud storage; start in monitor mode, then block high-confidence matches.",
  "มีกฎ DLP สำหรับเลขบัตรประชาชน ข้อมูลสุขภาพ และข้อมูลการเงิน บนอีเมลและคลาวด์ เริ่มจากโหมดเฝ้าดู แล้วบล็อกเมื่อการตรวจพบมีความแม่นยำสูง")
c("DATA-05","DATA","ID.AM-08 PR.PS-03","CIS 3.5; ISO/IEC 27002:2022 7.14",
  "How are disks and devices sanitized or destroyed before disposal or return to a vendor?",
  "ล้างหรือทำลายดิสก์และอุปกรณ์อย่างไรก่อนจำหน่ายหรือส่งคืนผู้ขาย",
  "Sanitization following NIST SP 800-88 or physical destruction; certificate of destruction from vendors; disposal record kept per device.",
  "ล้างข้อมูลตาม NIST SP 800-88 หรือทำลายทางกายภาพ ได้รับหนังสือรับรองการทำลายจากผู้ขาย และเก็บบันทึกการจำหน่ายรายอุปกรณ์")
c("DATA-06","DATA","PR.DS-01","CIS 3.4; PDPA s.37(3)",
  "Are retention periods applied, and is old personal data deleted when no longer needed?",
  "มีการใช้ระยะเวลาการเก็บรักษา และลบข้อมูลส่วนบุคคลเก่าเมื่อไม่จำเป็นแล้วหรือไม่",
  "Retention schedule per data type agreed with legal and the DPO; automated deletion or archive where systems allow; deletion evidenced.",
  "มีตารางระยะเวลาการเก็บรักษาตามประเภทข้อมูลที่ตกลงกับฝ่ายกฎหมายและ DPO ลบหรือย้ายเก็บอัตโนมัติเมื่อระบบรองรับ และมีหลักฐานการลบ")

# BKP
c("BKP-01","BKP","PR.DS-11","CIS 11.2, 11.4",
  "Do backups follow the 3-2-1 rule, with at least one offline or immutable copy that administrators cannot delete?",
  "การสำรองข้อมูลเป็นไปตามหลัก 3-2-1 และมีสำเนาอย่างน้อยหนึ่งชุดแบบออฟไลน์หรือแก้ไขไม่ได้ที่ผู้ดูแลระบบลบไม่ได้หรือไม่",
  "Three copies, two media, one off-site; one copy immutable or air-gapped; backup frequency matches the recovery point objective (RPO) of each critical system.",
  "มี 3 สำเนา บนสื่อ 2 ประเภท และ 1 ชุดนอกสถานที่ มีสำเนาหนึ่งชุดที่แก้ไขไม่ได้หรือแยกขาดจากเครือข่าย และความถี่การสำรองสอดคล้องกับจุดเป้าหมายในการกู้คืนข้อมูล (RPO) ของแต่ละระบบสำคัญ")
c("BKP-02","BKP","PR.DS-11","CIS 11.3",
  "Is the backup system isolated from the main domain, with separate credentials and MFA?",
  "ระบบสำรองข้อมูลแยกจากโดเมนหลัก ใช้บัญชีแยกและมี MFA หรือไม่",
  "Backup servers not joined to the production domain; separate admin accounts with MFA; backup console not reachable from user networks; backup data encrypted.",
  "เซิร์ฟเวอร์สำรองข้อมูลไม่อยู่ในโดเมนใช้งานจริง ใช้บัญชีผู้ดูแลแยกพร้อม MFA หน้าจอระบบสำรองเข้าจากเครือข่ายผู้ใช้ไม่ได้ และเข้ารหัสข้อมูลสำรอง")
c("BKP-03","BKP","PR.DS-11 RC.RP-03","CIS 11.5",
  "Are restore tests performed for critical systems, and do they measure actual recovery time against the RTO?",
  "มีการทดสอบกู้คืนระบบสำคัญ และวัดเวลากู้คืนจริงเทียบกับ RTO หรือไม่",
  "Full restore test of each critical system at least annually and sample file restores quarterly; results recorded with actual time versus RTO; gaps fed into the improvement plan.",
  "ทดสอบกู้คืนเต็มระบบของแต่ละระบบสำคัญอย่างน้อยปีละครั้ง และสุ่มกู้คืนไฟล์ทุกไตรมาส บันทึกผลพร้อมเวลาจริงเทียบ RTO และนำช่องว่างเข้าแผนปรับปรุง")
c("BKP-04","BKP","PR.DS-11","CIS 11.2",
  "Are backup jobs monitored daily, and are failures followed up?",
  "มีการเฝ้าดูงานสำรองข้อมูลทุกวัน และติดตามงานที่ล้มเหลวหรือไม่",
  "Daily backup report reviewed; failed jobs re-run within 24 hours; coverage checked against the critical system list, including SaaS such as Microsoft 365.",
  "ทบทวนรายงานการสำรองทุกวัน รันงานที่ล้มเหลวใหม่ภายใน 24 ชั่วโมง และตรวจความครอบคลุมเทียบรายการระบบสำคัญ รวมถึง SaaS เช่น Microsoft 365")
c("BKP-05","BKP","PR.IR-03 RC.RP-02","ISO/IEC 27002:2022 8.14, 5.30",
  "Is there a disaster recovery site or cloud recovery option for critical systems, and has failover been tested?",
  "มีศูนย์สำรองหรือทางเลือกกู้คืนบนคลาวด์สำหรับระบบสำคัญ และเคยทดสอบการสลับการทำงานหรือไม่",
  "Recovery capability sized to RTO; documented runbooks; failover test at least annually; recovery order agreed with the business.",
  "ขีดความสามารถในการกู้คืนสอดคล้องกับ RTO มีคู่มือขั้นตอนเป็นลายลักษณ์อักษร ทดสอบการสลับการทำงานอย่างน้อยปีละครั้ง และตกลงลำดับการกู้คืนกับฝ่ายธุรกิจ")

# VUL
c("VUL-01","VUL","ID.RA-01","CIS 7.5, 7.6",
  "Are authenticated vulnerability scans run on internal systems, and external scans on internet-facing assets?",
  "มีการสแกนช่องโหว่แบบยืนยันตัวตนกับระบบภายใน และสแกนจากภายนอกกับทรัพย์สินที่เปิดสู่อินเทอร์เน็ตหรือไม่",
  "Internal authenticated scans at least monthly; external scans at least monthly and after changes; scan coverage compared against the asset inventory.",
  "สแกนภายในแบบยืนยันตัวตนอย่างน้อยเดือนละครั้ง สแกนจากภายนอกอย่างน้อยเดือนละครั้งและหลังมีการเปลี่ยนแปลง และเทียบความครอบคลุมกับทะเบียนทรัพย์สิน")
c("VUL-02","VUL","PR.PS-02 ID.RA-06","CIS 7.3, 7.4, 7.7",
  "What are the patch timelines by severity, and what share of systems meet them?",
  "กำหนดเวลาแพตช์ตามระดับความรุนแรงคือเท่าใด และระบบที่ทำได้ตามกำหนดคิดเป็นสัดส่วนเท่าใด",
  "Critical internet-facing within 7 days (actively exploited within 72 hours), critical internal within 14 days, high within 30 days; OS and application patching automated; compliance reported monthly.",
  "ช่องโหว่วิกฤตบนระบบที่เปิดสู่อินเทอร์เน็ตภายใน 7 วัน (ที่ถูกใช้โจมตีจริงภายใน 72 ชั่วโมง) วิกฤตภายในภายใน 14 วัน ระดับสูงภายใน 30 วัน แพตช์ระบบปฏิบัติการและแอปพลิเคชันแบบอัตโนมัติ และรายงานผลทุกเดือน")
c("VUL-03","VUL","ID.RA-01 ID.IM-02","CIS 18.1, 18.2, 18.3",
  "Is penetration testing performed on critical and internet-facing systems, and are findings fixed and retested?",
  "มีการทดสอบเจาะระบบกับระบบสำคัญและระบบที่เปิดสู่อินเทอร์เน็ต และแก้ไขพร้อมทดสอบซ้ำหรือไม่",
  "External penetration test at least annually and after major changes; internal test for critical environments; high findings retested and closed.",
  "ทดสอบเจาะระบบจากภายนอกอย่างน้อยปีละครั้งและหลังการเปลี่ยนแปลงใหญ่ ทดสอบภายในสำหรับสภาพแวดล้อมสำคัญ และทดสอบซ้ำจนปิดข้อตรวจพบระดับสูง")
c("VUL-04","VUL","ID.RA-02 ID.RA-08","CIS 7.1, 7.2",
  "How are vendor advisories and known exploited vulnerability alerts tracked and acted on?",
  "ติดตามและดำเนินการกับประกาศของผู้ขายและรายการช่องโหว่ที่ถูกใช้โจมตีจริงอย่างไร",
  "Subscriptions to vendor advisories, ThaiCERT, and the CISA Known Exploited Vulnerabilities (KEV) catalog; each relevant advisory has a ticket, owner, and due date.",
  "สมัครรับประกาศจากผู้ขาย ThaiCERT และรายการ Known Exploited Vulnerabilities (KEV) ของ CISA ทุกประกาศที่เกี่ยวข้องมีตั๋วงาน เจ้าของ และวันครบกำหนด")
c("VUL-05","VUL","PR.PS-02 PR.PS-03","CIS 2.2, 12.1",
  "Which operating systems, applications, or network devices are past end of support, and what compensating controls exist?",
  "มีระบบปฏิบัติการ ระบบงาน หรืออุปกรณ์เครือข่ายใดที่หมดการสนับสนุนแล้ว และมีมาตรการชดเชยอะไร",
  "End-of-support list maintained; each item isolated, monitored, and approved as a time-bound exception with a replacement plan.",
  "มีรายการระบบหมดการสนับสนุน แต่ละรายการถูกแยกเครือข่าย เฝ้าระวัง และอนุมัติเป็นข้อยกเว้นที่มีกำหนดเวลาพร้อมแผนทดแทน")

# LOG
c("LOG-01","LOG","PR.PS-04","CIS 8.2, 8.5, 8.9",
  "Which log sources are collected centrally: domain controllers, firewalls, VPN, email, cloud, EDR, critical applications?",
  "เก็บบันทึกจากแหล่งใดไว้ส่วนกลางบ้าง เช่น Domain Controller ไฟร์วอลล์ VPN อีเมล คลาวด์ EDR และระบบงานสำคัญ",
  "All of these sources forward to a central log platform or SIEM; a log source register shows coverage and alerts when a source stops sending.",
  "ทุกแหล่งดังกล่าวส่งบันทึกเข้าแพลตฟอร์มส่วนกลางหรือ SIEM มีทะเบียนแหล่งบันทึกที่แสดงความครอบคลุม และแจ้งเตือนเมื่อแหล่งใดหยุดส่ง")
c("LOG-02","LOG","PR.PS-04","CIS 8.3, 8.10; Computer Crime Act s.26",
  "How long are logs retained, and are they protected from modification?",
  "เก็บรักษาบันทึกนานเท่าใด และได้รับการปกป้องจากการแก้ไขหรือไม่",
  "At least 90 days searchable (Computer Crime Act s.26 where it applies) and 12 months archived for investigations; write-once or access-restricted storage.",
  "ค้นหาได้อย่างน้อย 90 วัน (พ.ร.บ.คอมพิวเตอร์ฯ มาตรา 26 ในกรณีที่ใช้บังคับ) และเก็บถาวร 12 เดือนเพื่อการสืบสวน ใช้ที่จัดเก็บแบบเขียนครั้งเดียวหรือจำกัดสิทธิ์การเข้าถึง")
c("LOG-03","LOG","PR.PS-04 RS.AN-06","CIS 8.4",
  "Are all systems synchronized to a trusted time source?",
  "ทุกระบบตั้งเวลาให้ตรงกับแหล่งเวลาที่เชื่อถือได้หรือไม่",
  "At least two internal NTP servers synced to a trusted source; all servers, network devices, and cloud logs use the same time zone or UTC.",
  "มี NTP Server ภายในอย่างน้อย 2 ตัวที่ซิงก์กับแหล่งที่เชื่อถือได้ และเซิร์ฟเวอร์ อุปกรณ์เครือข่าย และบันทึกคลาวด์ใช้เขตเวลาเดียวกันหรือ UTC")
c("LOG-04","LOG","DE.CM-01 DE.AE-02 DE.AE-06","CIS 8.11, 13.1",
  "Who monitors security alerts, during which hours, and what is the response time?",
  "ใครเฝ้าดูการแจ้งเตือนด้านความมั่นคงปลอดภัย ในช่วงเวลาใด และเวลาตอบสนองเท่าใด",
  "24/7 monitoring in-house or by a managed security service provider (MSSP); critical alerts acknowledged within 15 to 30 minutes; escalation contacts tested.",
  "เฝ้าระวังตลอด 24 ชั่วโมงโดยทีมภายในหรือผู้ให้บริการด้านความมั่นคงปลอดภัย (MSSP) ตอบรับการแจ้งเตือนวิกฤตภายใน 15 ถึง 30 นาที และทดสอบรายชื่อผู้ติดต่อเพื่อยกระดับแล้ว")
c("LOG-05","LOG","DE.AE-03 DE.CM-03","CIS 8.11; MITRE ATT&CK",
  "Which detection use cases are in place, for example impossible travel, brute force, new admin accounts, mass file changes?",
  "มีกรณีการตรวจจับใดบ้าง เช่น การเข้าสู่ระบบจากสถานที่ที่เป็นไปไม่ได้ การเดารหัสผ่าน การสร้างบัญชีผู้ดูแลใหม่ และการเปลี่ยนแปลงไฟล์จำนวนมาก",
  "A documented use case catalog mapped to MITRE ATT&CK, covering at least identity misuse, privilege changes, ransomware behavior, and data exfiltration; rules reviewed quarterly.",
  "มีรายการกรณีการตรวจจับเป็นลายลักษณ์อักษรที่จับคู่กับ MITRE ATT&CK ครอบคลุมอย่างน้อยการใช้ตัวตนผิดปกติ การเปลี่ยนสิทธิ์ พฤติกรรมแรนซัมแวร์ และการนำข้อมูลออก และทบทวนกฎทุกไตรมาส")
c("LOG-06","LOG","DE.CM-03 PR.AA-05","CIS 8.5, 3.14",
  "Is access to sensitive data and privileged activity logged and reviewed?",
  "มีการบันทึกและทบทวนการเข้าถึงข้อมูลอ่อนไหวและกิจกรรมสิทธิ์สูงหรือไม่",
  "Audit logging on in critical applications for read and export of sensitive records; privileged activity reports reviewed at least monthly.",
  "เปิดบันทึกการตรวจสอบในระบบงานสำคัญสำหรับการอ่านและส่งออกข้อมูลอ่อนไหว และทบทวนรายงานกิจกรรมสิทธิ์สูงอย่างน้อยเดือนละครั้ง")

# CLD
c("CLD-01","CLD","PR.AA-03 PR.AA-05","CIS 6.3, 6.5; CIS Microsoft 365 Foundations Benchmark",
  "Are legacy authentication protocols blocked and conditional access policies applied in Microsoft 365 or the identity provider?",
  "บล็อกโปรโตคอลการยืนยันตัวตนแบบเก่าและใช้นโยบาย Conditional Access ใน Microsoft 365 หรือผู้ให้บริการตัวตนแล้วหรือไม่",
  "Legacy authentication blocked; conditional access requires MFA for all users and compliant devices for admins; risky sign-in policies enabled where licensed.",
  "บล็อกการยืนยันตัวตนแบบเก่า Conditional Access บังคับ MFA กับผู้ใช้ทุกคนและบังคับอุปกรณ์ที่ผ่านเกณฑ์สำหรับผู้ดูแล และเปิดนโยบายการเข้าสู่ระบบที่มีความเสี่ยงเมื่อมีไลเซนส์")
c("CLD-02","CLD","PR.PS-01 DE.CM-09","CIS Microsoft 365 Foundations Benchmark",
  "Is the cloud tenant configuration reviewed against a benchmark, for example Microsoft Secure Score or the CIS Microsoft 365 Benchmark?",
  "มีการทบทวนการตั้งค่า Cloud Tenant เทียบกับเกณฑ์อ้างอิงหรือไม่ เช่น Microsoft Secure Score หรือ CIS Microsoft 365 Benchmark",
  "Secure Score or a configuration assessment tool reviewed monthly with a target; high-impact recommendations tracked to closure; audit logging enabled tenant-wide.",
  "ทบทวน Secure Score หรือเครื่องมือประเมินการตั้งค่าทุกเดือนพร้อมเป้าหมาย ติดตามข้อแนะนำที่มีผลกระทบสูงจนปิด และเปิดบันทึกการตรวจสอบทั้ง Tenant")
c("CLD-03","CLD","GV.SC-02 PR.DS-11","ISO/IEC 27002:2022 5.23",
  "Is the shared responsibility model documented for each critical cloud service, including who backs up the data?",
  "มีการบันทึกการแบ่งความรับผิดชอบร่วมสำหรับบริการคลาวด์สำคัญแต่ละบริการ รวมถึงผู้รับผิดชอบสำรองข้อมูลหรือไม่",
  "Responsibility matrix per service; third-party backup for SaaS data such as Microsoft 365 mail and OneDrive; exit plan for each critical cloud service.",
  "มีตารางความรับผิดชอบรายบริการ ใช้การสำรองข้อมูลจากภายนอกสำหรับข้อมูล SaaS เช่น อีเมลและ OneDrive ของ Microsoft 365 และมีแผนการย้ายออกสำหรับบริการคลาวด์สำคัญ")
c("CLD-04","CLD","PR.AA-05 DE.CM-06","CIS 6.8",
  "How many global or subscription owner administrators exist in each cloud platform, and are their activities monitored?",
  "แต่ละแพลตฟอร์มคลาวด์มีผู้ดูแลระดับ Global หรือ Subscription Owner กี่ราย และมีการเฝ้าระวังกิจกรรมของเขาหรือไม่",
  "Two to four global administrators with phishing-resistant MFA; just-in-time role activation (for example Privileged Identity Management); alerts on role assignment changes.",
  "มีผู้ดูแลระดับ Global 2 ถึง 4 ราย ใช้ MFA ที่ทนต่อฟิชชิง เปิดบทบาทเฉพาะเมื่อจำเป็น (เช่น Privileged Identity Management) และแจ้งเตือนเมื่อมีการเปลี่ยนบทบาท")

# APP
c("APP-01","APP","PR.PS-06","CIS 16.1, 16.9",
  "Is there a secure development process, and are developers trained in secure coding (for example OWASP Top 10)?",
  "มีกระบวนการพัฒนาอย่างปลอดภัย และนักพัฒนาได้รับการอบรมการเขียนโค้ดอย่างปลอดภัย (เช่น OWASP Top 10) หรือไม่",
  "Security requirements defined at design; developers trained at least annually; outsourced developers bound to the same standard by contract.",
  "กำหนดข้อกำหนดด้านความมั่นคงปลอดภัยตั้งแต่การออกแบบ อบรมนักพัฒนาอย่างน้อยปีละครั้ง และผูกผู้รับจ้างพัฒนาให้ใช้มาตรฐานเดียวกันผ่านสัญญา")
c("APP-02","APP","PR.PS-06 ID.RA-01","CIS 16.12, 16.13",
  "Is code scanned (static and dependency analysis) and are applications tested for security before go-live?",
  "มีการสแกนโค้ด (การวิเคราะห์แบบสถิตและไลบรารีที่ใช้) และทดสอบความมั่นคงปลอดภัยของระบบงานก่อนเปิดใช้หรือไม่",
  "Static application security testing (SAST) and software composition analysis (SCA) in the build pipeline; application penetration test before go-live for internet-facing systems; high findings fixed before release.",
  "ใช้การทดสอบความมั่นคงปลอดภัยแบบสถิต (SAST) และการวิเคราะห์ส่วนประกอบซอฟต์แวร์ (SCA) ในขั้นตอน Build ทดสอบเจาะระบบงานก่อนเปิดใช้สำหรับระบบที่เปิดสู่อินเทอร์เน็ต และแก้ข้อตรวจพบระดับสูงก่อนเผยแพร่")
c("APP-03","APP","PR.PS-06 PR.IR-01","CIS 16.8",
  "Are development, test, and production environments separated, and is production data masked in test?",
  "แยกสภาพแวดล้อมการพัฒนา ทดสอบ และใช้งานจริง และปิดบังข้อมูลจริงในสภาพแวดล้อมทดสอบหรือไม่",
  "Separate environments and accounts; developers have no standing production access; real personal data masked or synthetic in non-production.",
  "แยกสภาพแวดล้อมและบัญชี นักพัฒนาไม่มีสิทธิ์เข้าระบบจริงแบบถาวร และใช้ข้อมูลที่ปิดบังหรือข้อมูลสังเคราะห์แทนข้อมูลส่วนบุคคลจริงนอกระบบใช้งานจริง")
c("APP-04","APP","PR.PS-06 GV.SC-09","CIS 16.4, 16.2",
  "Are third-party libraries and components tracked, and is there a process to fix reported vulnerabilities in your applications?",
  "มีการติดตามไลบรารีและส่วนประกอบจากภายนอก และมีกระบวนการแก้ช่องโหว่ที่ได้รับแจ้งในระบบงานหรือไม่",
  "Component inventory or software bill of materials (SBOM) per application; vulnerable components updated within defined timelines; intake channel for vulnerability reports.",
  "มีทะเบียนส่วนประกอบหรือรายการส่วนประกอบซอฟต์แวร์ (SBOM) ของแต่ละระบบ อัปเดตส่วนประกอบที่มีช่องโหว่ภายในเวลาที่กำหนด และมีช่องทางรับแจ้งช่องโหว่")
c("APP-05","APP","PR.IR-01 DE.CM-09","CIS 13.10",
  "Are internet-facing web applications protected by a web application firewall (WAF)?",
  "เว็บแอปพลิเคชันที่เปิดสู่อินเทอร์เน็ตได้รับการป้องกันด้วย Web Application Firewall (WAF) หรือไม่",
  "WAF in blocking mode for critical internet-facing applications with the OWASP core rule set; WAF logs sent to the SIEM.",
  "ใช้ WAF ในโหมดบล็อกกับระบบงานสำคัญที่เปิดสู่อินเทอร์เน็ตด้วยชุดกฎหลักของ OWASP และส่งบันทึก WAF เข้า SIEM")

# SUP
c("SUP-01","SUP","GV.SC-04 DE.CM-06","CIS 15.1, 6.1",
  "Is there a list of suppliers with remote or privileged access, and is their access approved per session or time-limited?",
  "มีรายชื่อผู้ให้บริการที่มีสิทธิ์เข้าถึงระยะไกลหรือสิทธิ์สูง และการเข้าถึงได้รับอนุมัติเป็นรายครั้งหรือจำกัดเวลาหรือไม่",
  "Named accounts for each vendor engineer; access enabled on request and disabled after use; MFA required; sessions logged or recorded.",
  "บัญชีระบุชื่อสำหรับวิศวกรของผู้ขายแต่ละคน เปิดสิทธิ์เมื่อขอและปิดหลังใช้งาน บังคับ MFA และบันทึกหรืออัดเซสชัน")
c("SUP-02","SUP","DE.CM-06","CIS 15.6",
  "Are vendor remote access tools (for example TeamViewer or AnyDesk) controlled, or can vendors install them freely?",
  "เครื่องมือควบคุมระยะไกลของผู้ขาย (เช่น TeamViewer หรือ AnyDesk) ได้รับการควบคุม หรือผู้ขายติดตั้งได้อย่างอิสระ",
  "One approved remote access method; unapproved remote tools blocked by application control and detected by EDR.",
  "มีวิธีเข้าถึงระยะไกลที่อนุมัติวิธีเดียว และบล็อกเครื่องมือที่ไม่ได้อนุมัติด้วยการควบคุมแอปพลิเคชัน และตรวจจับด้วย EDR")
c("SUP-03","SUP","GV.SC-10","CIS 15.7",
  "When a supplier contract ends, are accounts, VPN profiles, and firewall rules removed?",
  "เมื่อสัญญาผู้ให้บริการสิ้นสุด มีการลบบัญชี โปรไฟล์ VPN และกฎไฟร์วอลล์หรือไม่",
  "Supplier offboarding checklist covers accounts, keys, certificates, VPN, firewall rules, and data return or destruction; completion signed off.",
  "รายการตรวจสอบการยุติผู้ให้บริการครอบคลุมบัญชี กุญแจ ใบรับรอง VPN กฎไฟร์วอลล์ และการคืนหรือทำลายข้อมูล และลงนามรับรองเมื่อเสร็จ")

# OT
c("OT-01","OT","ID.AM-01 ID.AM-05","NIST SP 800-82 Rev. 3; IEC 62443-2-1",
  "Is there an inventory of OT and medical devices with operating system version, network location, and vendor support status?",
  "มีทะเบียนระบบ OT และอุปกรณ์การแพทย์ ที่ระบุเวอร์ชันระบบปฏิบัติการ ตำแหน่งบนเครือข่าย และสถานะการสนับสนุนจากผู้ขายหรือไม่",
  "Complete inventory built with passive discovery where possible; each device has a business or production owner, criticality, and patch support status.",
  "มีทะเบียนครบถ้วนที่สร้างจากการสำรวจแบบ Passive เมื่อทำได้ ทุกอุปกรณ์มีเจ้าของฝั่งธุรกิจหรือฝั่งผลิต ระดับความสำคัญ และสถานะการรองรับแพตช์")
c("OT-02","OT","PR.IR-01","NIST SP 800-82 Rev. 3; IEC 62443-3-3",
  "Are OT and medical devices on separate network zones with only required traffic allowed?",
  "ระบบ OT และอุปกรณ์การแพทย์อยู่ในโซนเครือข่ายแยก และอนุญาตเฉพาะการรับส่งข้อมูลที่จำเป็นหรือไม่",
  "Dedicated VLANs or zones per device class; firewall allowlists to the systems they must reach (for example an imaging server, a SCADA server, or a core business system); no direct internet access.",
  "มี VLAN หรือโซนแยกตามประเภทอุปกรณ์ ไฟร์วอลล์อนุญาตเฉพาะระบบที่ต้องเชื่อมต่อ (เช่น เซิร์ฟเวอร์ภาพทางการแพทย์ เซิร์ฟเวอร์ SCADA หรือระบบงานหลัก) และไม่เชื่อมต่ออินเทอร์เน็ตโดยตรง")
c("OT-03","OT","PR.PS-02 GV.SC-05","NIST SP 800-82 Rev. 3",
  "How are unpatchable or legacy devices protected, and do vendor contracts cover patching and remote support security?",
  "ป้องกันอุปกรณ์รุ่นเก่าหรือที่แพตช์ไม่ได้อย่างไร และสัญญากับผู้ขายครอบคลุมการแพตช์และความมั่นคงปลอดภัยของการสนับสนุนระยะไกลหรือไม่",
  "Compensating controls (isolation, allowlisting, monitoring) for each unpatchable device; contracts require security updates and controlled remote access.",
  "มีมาตรการชดเชย (แยกเครือข่าย อนุญาตเฉพาะโปรแกรม และเฝ้าระวัง) สำหรับอุปกรณ์ที่แพตช์ไม่ได้ และสัญญากำหนดให้ผู้ขายให้อัปเดตด้านความมั่นคงปลอดภัยและควบคุมการเข้าถึงระยะไกล")

# PHY
c("PHY-01","PHY","PR.AA-06","ISO/IEC 27002:2022 7.2, 7.3",
  "Is access to the server room and network closets restricted by card or key, with the access list reviewed?",
  "การเข้าห้องเซิร์ฟเวอร์และตู้เครือข่ายจำกัดด้วยบัตรหรือกุญแจ และทบทวนรายชื่อผู้มีสิทธิ์หรือไม่",
  "Electronic access control with logs; access list reviewed at least quarterly; visitors signed in and escorted; network closets locked.",
  "ใช้ระบบควบคุมการเข้าออกแบบอิเล็กทรอนิกส์ที่มีบันทึก ทบทวนรายชื่ออย่างน้อยทุกไตรมาส ผู้มาติดต่อลงชื่อและมีผู้นำพา และล็อกตู้เครือข่าย")
c("PHY-02","PHY","DE.CM-02","ISO/IEC 27002:2022 7.4",
  "Are CCTV and door alarms in place for restricted areas, and are alerts monitored?",
  "มีกล้องวงจรปิดและสัญญาณเตือนประตูในพื้นที่หวงห้าม และมีการเฝ้าดูการแจ้งเตือนหรือไม่",
  "CCTV covers entrances to restricted areas with footage kept at least 30 days; door-forced and door-held alarms go to security staff.",
  "กล้องครอบคลุมทางเข้าพื้นที่หวงห้ามและเก็บภาพอย่างน้อย 30 วัน และสัญญาณเตือนประตูถูกงัดหรือเปิดค้างส่งถึงเจ้าหน้าที่รักษาความปลอดภัย")
c("PHY-03","PHY","PR.IR-02","ISO/IEC 27002:2022 7.5, 7.11",
  "Is the server room protected with UPS, generator, cooling, fire suppression, and temperature and water sensors, and are they tested?",
  "ห้องเซิร์ฟเวอร์มี UPS เครื่องกำเนิดไฟฟ้า ระบบทำความเย็น ระบบดับเพลิง และเซนเซอร์อุณหภูมิและน้ำรั่ว และมีการทดสอบหรือไม่",
  "UPS sized for orderly shutdown or generator start; generator tested monthly under load; redundant cooling; gas-based suppression; sensor alerts sent 24/7.",
  "UPS รองรับการปิดระบบอย่างเป็นลำดับหรือจนเครื่องกำเนิดไฟฟ้าทำงาน ทดสอบเครื่องกำเนิดไฟฟ้าแบบมีโหลดทุกเดือน ระบบทำความเย็นสำรอง ระบบดับเพลิงแบบก๊าซ และส่งการแจ้งเตือนจากเซนเซอร์ตลอด 24 ชั่วโมง")

# IR
c("IR-01","IR","RS.MA-01 RS.MI-01","CIS 17.4, 17.5",
  "Are incident response playbooks in place for ransomware, phishing or business email compromise, and compromised accounts?",
  "มีคู่มือปฏิบัติการรับมือเหตุการณ์สำหรับแรนซัมแวร์ ฟิชชิงหรือการแอบอ้างอีเมลธุรกิจ และบัญชีถูกยึดหรือไม่",
  "Playbooks with technical steps, decision points, and contacts; stored offline as well as online; reviewed annually and after incidents.",
  "คู่มือมีขั้นตอนทางเทคนิค จุดตัดสินใจ และผู้ติดต่อ เก็บทั้งแบบออฟไลน์และออนไลน์ และทบทวนทุกปีและหลังเกิดเหตุ")
c("IR-02","IR","RS.MI-01","CIS 17.4; EDR capability",
  "Can the team isolate a host, disable an account, and block an indicator across the environment within minutes?",
  "ทีมแยกเครื่อง ระงับบัญชี และบล็อกตัวบ่งชี้ทั่วทั้งระบบได้ภายในไม่กี่นาทีหรือไม่",
  "EDR network isolation available to on-call staff; documented steps to disable accounts and revoke sessions in on-premises and cloud identity; tested in exercises.",
  "เจ้าหน้าที่ตามเวรใช้ฟังก์ชันแยกเครื่องของ EDR ได้ มีขั้นตอนระงับบัญชีและยกเลิกเซสชันทั้งในระบบภายในและคลาวด์ และทดสอบในการฝึกซ้อม")
c("IR-03","IR","RS.AN-07 RS.AN-06","CIS 17.4; NIST SP 800-86",
  "Is there forensic capability, either in-house tools or a retainer, to collect memory, disk, and log evidence?",
  "มีขีดความสามารถด้านนิติวิทยาศาสตร์ดิจิทัลหรือไม่ ไม่ว่าเครื่องมือภายในหรือสัญญาจ้างล่วงหน้า เพื่อเก็บหลักฐานจากหน่วยความจำ ดิสก์ และบันทึก",
  "Incident response retainer with agreed response time, or trained staff with tools; evidence handling and chain of custody procedure; evidence storage location defined.",
  "มีสัญญาจ้างล่วงหน้าด้านรับมือเหตุการณ์ที่กำหนดเวลาตอบสนอง หรือมีเจ้าหน้าที่ที่ผ่านการอบรมพร้อมเครื่องมือ มีขั้นตอนจัดการหลักฐานและห่วงโซ่การครอบครอง และกำหนดที่เก็บหลักฐาน")
c("IR-04","IR","ID.IM-02 ID.IM-04","CIS 17.7, 17.8",
  "Are technical incident response exercises or tabletop exercises run, and are post-incident reviews held?",
  "มีการฝึกซ้อมการรับมือเหตุการณ์ทางเทคนิคหรือการฝึกซ้อมบนโต๊ะ และจัดการทบทวนหลังเหตุการณ์หรือไม่",
  "At least one tabletop per year with management and one technical drill; lessons-learned review within two weeks of significant incidents; actions tracked.",
  "ฝึกซ้อมบนโต๊ะร่วมกับผู้บริหารอย่างน้อยปีละครั้งและซ้อมทางเทคนิคหนึ่งครั้ง ทบทวนบทเรียนภายใน 2 สัปดาห์หลังเหตุการณ์สำคัญ และติดตามการดำเนินการ")
c("IR-05","IR","RS.CO-02 RS.MA-04","CIS 17.2, 17.6",
  "Is there an out-of-band communication channel and a current contact list for incidents?",
  "มีช่องทางสื่อสารสำรองที่แยกจากระบบปกติ และรายชื่อผู้ติดต่อที่เป็นปัจจุบันสำหรับเหตุการณ์หรือไม่",
  "Contact list for internal, supplier, regulator, and insurer contacts reviewed quarterly and held offline; alternate channel (for example a separate messaging group or phone bridge) not dependent on corporate email.",
  "รายชื่อผู้ติดต่อภายใน ผู้ให้บริการ หน่วยงานกำกับ และบริษัทประกันภัย ทบทวนทุกไตรมาสและเก็บแบบออฟไลน์ และมีช่องทางสำรอง (เช่น กลุ่มสนทนาแยกหรือสายประชุมทางโทรศัพท์) ที่ไม่พึ่งอีเมลขององค์กร")

# ---- added in Information Gathering v2.0 (spec Section 8.2) ----
c("EP-07","EP","PR.AA-05 PR.DS-01 PR.PS-01","CIS 4.11, 4.12; ISO/IEC 27002:2022 8.1",
  "Are phones, tablets, and personal devices that reach company email or data enrolled in mobile device management (MDM), with screen lock, encryption, and remote wipe?",
  "โทรศัพท์ แท็บเล็ต และอุปกรณ์ส่วนตัวที่เข้าถึงอีเมลหรือข้อมูลขององค์กร ลงทะเบียนในระบบบริหารอุปกรณ์เคลื่อนที่ (MDM) และบังคับล็อกหน้าจอ การเข้ารหัส และการลบข้อมูลจากระยะไกลหรือไม่",
  "Company data on mobile devices is reachable only from enrolled or app-protected devices; policy enforces PIN, encryption, and a supported operating system; a lost device is wiped within one day of the report.",
  "เข้าถึงข้อมูลองค์กรบนอุปกรณ์เคลื่อนที่ได้เฉพาะจากอุปกรณ์ที่ลงทะเบียนหรือแอปที่ได้รับการปกป้อง นโยบายบังคับ PIN การเข้ารหัส และระบบปฏิบัติการที่ยังได้รับการสนับสนุน และลบข้อมูลในอุปกรณ์ที่สูญหายภายในหนึ่งวันหลังได้รับแจ้ง")
c("DATA-07","DATA","PR.DS-02 GV.PO-01","ISO/IEC 27002:2022 5.14; PDPA s.37",
  "Do staff send customer, patient, or other personal data through consumer messaging apps such as LINE, and is there an approved alternative?",
  "พนักงานส่งข้อมูลลูกค้า ผู้ป่วย หรือข้อมูลส่วนบุคคลอื่นผ่านแอปสนทนาทั่วไป เช่น LINE หรือไม่ และมีช่องทางที่องค์กรอนุมัติให้ใช้แทนหรือไม่",
  "A written rule says which channels may carry personal or confidential data; the organization provides an approved, managed messaging or file-sharing tool; department interviews or spot checks confirm that staff use it.",
  "มีกฎเป็นลายลักษณ์อักษรว่าช่องทางใดส่งข้อมูลส่วนบุคคลหรือข้อมูลลับได้ องค์กรจัดเครื่องมือสนทนาหรือแชร์ไฟล์ที่อนุมัติและควบคุมได้ และการสัมภาษณ์รายแผนกหรือการสุ่มตรวจยืนยันว่าพนักงานใช้จริง")
c("DATA-08","DATA","ID.AM-02 GV.PO-01 PR.DS-01","ISO/IEC 27002:2022 5.10; NIST AI 600-1",
  "Do staff use generative AI tools for work, which tools, and what data may they enter?",
  "พนักงานใช้เครื่องมือ Generative AI ในการทำงานหรือไม่ ใช้เครื่องมือใด และอนุญาตให้ป้อนข้อมูลประเภทใด",
  "Approved AI tools are listed; enterprise accounts with data-use controls are used; a rule bans entering personal, confidential, or customer data into unapproved tools; web filtering or data loss prevention (DLP) enforces it.",
  "มีรายการเครื่องมือ AI ที่อนุมัติ ใช้บัญชีระดับองค์กรที่ควบคุมการนำข้อมูลไปใช้ได้ มีกฎห้ามป้อนข้อมูลส่วนบุคคล ข้อมูลลับ หรือข้อมูลลูกค้าลงในเครื่องมือที่ไม่ได้อนุมัติ และใช้การกรองเว็บหรือ DLP บังคับใช้")
c("IAM-09","IAM","PR.AA-05 PR.AA-01","ISO/IEC 27002:2022 8.2; NIST SP 800-53 Rev. 5 AC-2",
  "Are there emergency (break-glass) accounts for critical systems, and how are they protected and monitored?",
  "มีบัญชีฉุกเฉิน (break-glass) สำหรับระบบสำคัญหรือไม่ และปกป้องและเฝ้าระวังบัญชีเหล่านี้อย่างไร",
  "A small number of emergency accounts exist only for systems that must stay reachable when normal sign-in fails; credentials are sealed or vaulted; any use raises an alert and is reviewed; passwords are changed after each use.",
  "มีบัญชีฉุกเฉินจำนวนน้อยเฉพาะระบบที่ต้องเข้าถึงได้เมื่อการล็อกอินปกติใช้ไม่ได้ รหัสผ่านถูกปิดผนึกหรือเก็บในตู้นิรภัยดิจิทัล ทุกการใช้งานแจ้งเตือนและได้รับการทบทวน และเปลี่ยนรหัสผ่านหลังใช้งานทุกครั้ง")
c("AST-06","AST","ID.AM-01 ID.RA-01","ISO/IEC 27002:2022 5.9, 8.8",
  "Is there a current list of internet-facing assets (domains, public IP addresses, certificates, and cloud services), and is it scanned for exposure?",
  "มีรายการทรัพย์สินที่เปิดสู่อินเทอร์เน็ต (โดเมน IP สาธารณะ ใบรับรอง และบริการคลาวด์) ที่เป็นปัจจุบัน และมีการสแกนหาจุดเปิดเผยหรือไม่",
  "The external asset list is reconciled at least quarterly with DNS, certificate, and cloud records; external scans run at least monthly; every unknown exposure gets an owner and is closed.",
  "กระทบยอดรายการทรัพย์สินภายนอกกับข้อมูล DNS ใบรับรอง และคลาวด์อย่างน้อยไตรมาสละครั้ง สแกนจากภายนอกอย่างน้อยเดือนละครั้ง และทุกจุดเปิดเผยที่ไม่รู้จักมีเจ้าของและถูกปิด")
c("OT-04","OT","ID.AM-01 PR.IR-01","NIST SP 800-82 Rev. 3; NIST IR 8259A",
  "Are building systems and Internet of Things (IoT) devices such as CCTV, door access, building management, and network printers listed, separated from the office network, and patched?",
  "ระบบอาคารและอุปกรณ์ IoT เช่น กล้องวงจรปิด ระบบควบคุมการเข้าออก ระบบบริหารอาคาร และเครื่องพิมพ์เครือข่าย มีรายการ แยกจากเครือข่ายสำนักงาน และได้รับการแพตช์หรือไม่",
  "Building and IoT devices are listed with owners; they sit on separate segments; default passwords are changed; vendor remote access follows the supplier access rule.",
  "อุปกรณ์อาคารและ IoT มีรายการพร้อมเจ้าของ อยู่ในส่วนเครือข่ายแยก เปลี่ยนรหัสผ่านเริ่มต้นแล้ว และการเข้าถึงระยะไกลของผู้ขายเป็นไปตามกฎการเข้าถึงของผู้ให้บริการ")

# ---- industry pack checks (packs.py); shown only when the pack is selected ----
c("HC-01","OT","ID.AM-01 ID.RA-01 GV.SC-05","IEC 80001-1:2021; MDS2 form (NEMA/MITA)",
  "For networked medical devices, do you hold the manufacturer security disclosure (for example the MDS2 form), the end-of-support date, and the patch policy?",
  "สำหรับอุปกรณ์การแพทย์ที่เชื่อมต่อเครือข่าย มีเอกสารเปิดเผยข้อมูลความมั่นคงปลอดภัยจากผู้ผลิต (เช่น แบบฟอร์ม MDS2) วันสิ้นสุดการสนับสนุน และนโยบายแพตช์หรือไม่",
  "Biomedical engineering and IT keep one device list that includes the security disclosure, end-of-support date, and patch policy; procurement asks for them before purchase.",
  "ฝ่ายวิศวกรรมชีวการแพทย์และ IT ใช้รายการอุปกรณ์เดียวกันที่ระบุเอกสารเปิดเผยข้อมูลความมั่นคงปลอดภัย วันสิ้นสุดการสนับสนุน และนโยบายแพตช์ และฝ่ายจัดซื้อขอเอกสารเหล่านี้ก่อนซื้อ", pack="hc")
c("HC-02","IAM","PR.AA-01 PR.AA-05","ISO 27799:2016; ISO/IEC 27002:2022 8.5",
  "On shared clinical workstations, how do staff sign in and switch users, and is emergency access to patient records logged and reviewed?",
  "ที่เครื่องที่ใช้ร่วมกันในหน่วยบริการ เจ้าหน้าที่ล็อกอินและสลับผู้ใช้อย่างไร และการเข้าถึงเวชระเบียนแบบฉุกเฉินมีการบันทึกและทบทวนหรือไม่",
  "Each clinician signs in with a personal account, using fast user switching or badge sign-in; emergency access needs a reason, is logged, and is reviewed by the record owner within one week.",
  "เจ้าหน้าที่แต่ละคนล็อกอินด้วยบัญชีของตนเองโดยใช้การสลับผู้ใช้แบบรวดเร็วหรือบัตร การเข้าถึงแบบฉุกเฉินต้องระบุเหตุผล มีการบันทึก และเจ้าของข้อมูลทบทวนภายในหนึ่งสัปดาห์", pack="hc")
c("MFG-01","NET","PR.IR-01 DE.CM-01","IEC 62443-3-3; NIST SP 800-82 Rev. 3",
  "Is there a demilitarized zone (DMZ) between the office network and the plant network, with no direct traffic between them?",
  "มีเขตกันชน (DMZ) ระหว่างเครือข่ายสำนักงานกับเครือข่ายโรงงาน และไม่มีการรับส่งข้อมูลโดยตรงระหว่างกันหรือไม่",
  "Office and plant networks meet only in a DMZ; data such as production reports passes through brokered services; remote access to the plant uses a jump host with multi-factor authentication and session recording.",
  "เครือข่ายสำนักงานและโรงงานเชื่อมต่อกันผ่าน DMZ เท่านั้น ข้อมูลเช่นรายงานการผลิตผ่านบริการตัวกลาง และการเข้าถึงโรงงานจากระยะไกลใช้ jump host ที่มี MFA และบันทึกเซสชัน", pack="mfg")
c("MFG-02","OT","PR.PS-01 PR.AA-05","IEC 62443-2-1; NIST SP 800-82 Rev. 3",
  "How are engineering workstations and PLC programming laptops controlled, including USB media and program change approval?",
  "ควบคุมเครื่องวิศวกรรมและโน้ตบุ๊กสำหรับเขียนโปรแกรม PLC อย่างไร รวมถึงสื่อ USB และการอนุมัติการเปลี่ยนแปลงโปรแกรม",
  "Engineering workstations are dedicated, hardened, and kept off the internet; USB media is scanned at a kiosk; PLC program changes are approved and the last known good version is backed up.",
  "เครื่องวิศวกรรมใช้เฉพาะงาน ตั้งค่าตามมาตรฐาน และไม่เชื่อมต่ออินเทอร์เน็ต สแกนสื่อ USB ที่จุดตรวจ การเปลี่ยนโปรแกรม PLC ได้รับอนุมัติ และสำรองเวอร์ชันล่าสุดที่ใช้งานได้", pack="mfg")
c("FIN-01","IAM","PR.AA-03 DE.CM-01 DE.AE-02","BOT SorNorSor. 21/2562 (verify clause); ISO/IEC 27002:2022 8.5",
  "Are customer-facing digital channels protected with strong customer authentication, device binding, and fraud monitoring?",
  "ช่องทางดิจิทัลที่ให้บริการลูกค้ามีการยืนยันตัวตนลูกค้าแบบเข้ม การผูกอุปกรณ์ และการเฝ้าระวังการทุจริตหรือไม่",
  "High-risk transactions need a second factor and device binding; fraud rules monitor channels in real time; cyber and fraud alerts are correlated and handled by one process.",
  "ธุรกรรมความเสี่ยงสูงต้องใช้ปัจจัยที่สองและผูกอุปกรณ์ มีกฎตรวจจับการทุจริตแบบเวลาจริง และรวมการแจ้งเตือนด้านไซเบอร์กับการทุจริตไว้ในกระบวนการเดียว", pack="fin")
c("HOS-01","NET","PR.IR-01 ID.AM-03","PCI DSS v4.0.1 Requirements 1 and 11.4.5",
  "Is the cardholder data environment separated from guest Wi-Fi and office networks, and is the PCI scope documented and tested?",
  "ระบบที่เกี่ยวข้องกับข้อมูลบัตร (CDE) แยกจาก Wi-Fi สำหรับแขกและเครือข่ายสำนักงาน และมีเอกสารและการทดสอบขอบเขต PCI หรือไม่",
  "Point-of-sale and payment systems sit in a separate segment; a current data flow diagram defines the scope; segmentation is tested at least annually.",
  "ระบบ POS และระบบชำระเงินอยู่ในส่วนเครือข่ายแยก มีแผนภาพการไหลของข้อมูลที่เป็นปัจจุบันกำหนดขอบเขต และทดสอบการแบ่งส่วนเครือข่ายอย่างน้อยปีละครั้ง", pack="hosp")
c("UTL-01","OT","PR.AA-03 PR.IR-01 DE.CM-01","IEC 62443-3-3; NIST SP 800-82 Rev. 3",
  "How are remote sites, field devices, and SCADA links protected, and are safety systems separated from control networks?",
  "ปกป้องสถานีระยะไกล อุปกรณ์ภาคสนาม และการเชื่อมต่อ SCADA อย่างไร และระบบความปลอดภัย (safety system) แยกจากเครือข่ายควบคุมหรือไม่",
  "Remote links are encrypted and authenticated; field device access uses named accounts; safety instrumented systems are on separate networks; control network traffic is monitored.",
  "การเชื่อมต่อระยะไกลเข้ารหัสและยืนยันตัวตน การเข้าถึงอุปกรณ์ภาคสนามใช้บัญชีที่ระบุชื่อ ระบบความปลอดภัยอยู่ในเครือข่ายแยก และมีการเฝ้าระวังการรับส่งข้อมูลในเครือข่ายควบคุม", pack="util")
c("PUB-01","DATA","ID.AM-05 PR.DS-01","NCSC notifications on security categories and minimum standards B.E. 2566",
  "Has each information system been classified low, medium, or high for confidentiality, integrity, and availability, and are the matching minimum measures in place?",
  "ระบบสารสนเทศแต่ละระบบได้รับการจัดระดับต่ำ กลาง หรือสูง ตามความลับ ความถูกต้อง และความพร้อมใช้ และใช้มาตรการขั้นต่ำตามระดับแล้วหรือไม่",
  "Every system has a recorded category with the date of the last review (at least every three years) and a checklist of the minimum measures for its category.",
  "ทุกระบบมีระดับที่บันทึกไว้พร้อมวันที่ทบทวนครั้งล่าสุด (อย่างน้อยทุก 3 ปี) และมีรายการตรวจมาตรการขั้นต่ำตามระดับ", pack="pub")

if __name__ == "__main__":
    import collections
    print(len(TC), collections.Counter(x["d"] for x in TC))
