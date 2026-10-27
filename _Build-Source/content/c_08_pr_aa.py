# -*- coding: utf-8 -*-
# PR.AA Identity Management, Authentication, and Access Control (incl. physical)
C = {}

C["PR-POL-001"] = dict(
 purpose=("This policy sets the principles for granting, using, reviewing, and removing access to [Organization Name] information and systems, so that only authorized and authenticated users access what they need (PR.AA).",
          "นโยบายนี้กำหนดหลักการในการให้สิทธิ์ ใช้งาน ทบทวน และถอนสิทธิ์การเข้าถึงข้อมูลและระบบของ [ชื่อองค์กร] เพื่อให้เฉพาะผู้ใช้ที่ได้รับอนุญาตและยืนยันตัวตนแล้วเข้าถึงได้เฉพาะสิ่งที่จำเป็น (PR.AA)"),
 sections=[
  ("Policy Statements", "ข้อความนโยบาย", "State mandatory access control principles.", "ระบุหลักการควบคุมการเข้าถึงที่บังคับ",
   ["Access is granted on a need-to-know and least-privilege basis, approved by the system owner.", "Every user has a unique identity; shared accounts are prohibited unless approved and controlled.",
    "Authentication strength matches risk: multi-factor authentication (MFA) is required for remote access, privileged access, and access to Restricted data (PR-STD-001).",
    "Privileged access is separate from normal user access and is managed under PR-STD-002.", "Duties are segregated so that no single person can complete a critical transaction alone (ISO/IEC 27001:2022 Annex A 5.3).",
    "Access is reviewed at least quarterly for privileged and critical systems, and semi-annually for others (PR-PRC-002).", "Access is removed promptly when no longer needed (GV-STD-001).",
    "Access to personal data is logged to support audit trails, as required by the PDPC Notification on Security Measures B.E. 2565."],
   ["ให้สิทธิ์ตามหลักความจำเป็นต้องรู้และสิทธิ์น้อยที่สุด โดยเจ้าของระบบเป็นผู้อนุมัติ", "ผู้ใช้ทุกคนมีตัวตนที่ไม่ซ้ำกัน ห้ามใช้บัญชีร่วมกัน เว้นแต่ได้รับอนุมัติและมีการควบคุม",
    "ระดับการยืนยันตัวตนต้องเหมาะสมกับความเสี่ยง โดยต้องใช้การยืนยันตัวตนหลายปัจจัย (MFA) สำหรับการเข้าถึงระยะไกล สิทธิ์ระดับสูง และการเข้าถึงข้อมูลระดับ Restricted (PR-STD-001)",
    "แยกสิทธิ์ระดับสูงออกจากสิทธิ์ผู้ใช้ทั่วไป และบริหารตาม PR-STD-002", "แบ่งแยกหน้าที่เพื่อไม่ให้บุคคลใดดำเนินธุรกรรมสำคัญได้ครบถ้วนเพียงคนเดียว (ISO/IEC 27001:2022 Annex A 5.3)",
    "ทบทวนสิทธิ์อย่างน้อยทุกไตรมาสสำหรับสิทธิ์ระดับสูงและระบบสำคัญ และทุก 6 เดือนสำหรับระบบอื่น (PR-PRC-002)", "ถอนสิทธิ์ทันทีเมื่อไม่จำเป็นอีกต่อไป (GV-STD-001)",
    "บันทึก Log การเข้าถึงข้อมูลส่วนบุคคลเพื่อใช้เป็นหลักฐานการตรวจสอบ ตามประกาศ คกก.คุ้มครองข้อมูลส่วนบุคคล เรื่องมาตรการรักษาความมั่นคงปลอดภัย พ.ศ. 2565"],
   ["Access to HIS is role-based by clinical function (physician, nurse, pharmacist, registration) and approved by the department head.", "Every staff member has a unique account; shared ward accounts were removed in 2025.",
    "MFA is required for remote access, privileged access, and all vendor access. Shared clinical workstations use badge tap plus PIN to balance speed and security.",
    "Administrators use separate admin accounts through the PAM jump host.", "Pharmacy order verification and dispensing are segregated in HIS.",
    "HIS, PACS, LIS, and privileged access are reviewed quarterly; other systems semi-annually.", "Leavers are disabled on the last working day through HR integration.",
    "All access to patient records is logged in HIS and retained for at least two years for privacy investigations."]),
  ("Emergency Access", "การเข้าถึงในกรณีฉุกเฉิน", "Define controlled emergency (break-glass) access.", "กำหนดการเข้าถึงในกรณีฉุกเฉิน (Break-glass) ที่มีการควบคุม",
   "Emergency access accounts may be used only when normal access is unavailable and delay would harm the business or people. Each use is logged, reviewed by the [CISO] within one working day, and the credentials are reset after use.",
   "บัญชีสำหรับเข้าถึงในกรณีฉุกเฉินใช้ได้เฉพาะเมื่อการเข้าถึงปกติใช้ไม่ได้ และความล่าช้าจะก่อความเสียหายต่อธุรกิจหรือบุคคล การใช้งานทุกครั้งต้องบันทึก [CISO] ทบทวนภายใน 1 วันทำการ และเปลี่ยนรหัสผ่านหลังใช้งาน",
   "Break-glass access in HIS lets clinicians view a patient record outside their assigned ward in emergencies. Each use requires a reason, is logged, and is reviewed by the DPO team within one working day."),
 ],
 bp=[("Define role-based access profiles with business owners; it reduces approval effort and access creep.", "กำหนดโปรไฟล์สิทธิ์ตามบทบาทร่วมกับเจ้าของธุรกิจ เพื่อลดภาระการอนุมัติและการสะสมสิทธิ์เกินจำเป็น"),
     ("Centralize identity through single sign-on (SSO) where possible so one disable action removes all access.", "รวมศูนย์การบริหารตัวตนผ่าน Single Sign-On (SSO) เมื่อทำได้ เพื่อให้การปิดบัญชีครั้งเดียวถอนสิทธิ์ทั้งหมด"),
     ("Design clinical or operational access for speed as well as security; slow login drives workarounds.", "ออกแบบการเข้าถึงในงานคลินิกหรืองานปฏิบัติการให้รวดเร็วควบคู่กับความมั่นคงปลอดภัย เพราะการเข้าสู่ระบบที่ช้าทำให้ผู้ใช้หาทางเลี่ยง")],
 mistakes=[("Granting access by copying another user's profile, which spreads excessive rights.", "ให้สิทธิ์โดยคัดลอกโปรไฟล์ของผู้ใช้อื่น ทำให้สิทธิ์เกินจำเป็นแพร่กระจาย"),
           ("Access reviews done by IT rather than by business owners who know who needs access.", "การทบทวนสิทธิ์ทำโดยฝ่าย IT แทนเจ้าของธุรกิจที่รู้ว่าใครต้องการสิทธิ์")],
 rev="Updated in July 2026 to add badge tap plus PIN for shared clinical workstations after the Ward 5A and 6B pilot.",
)

C["PR-STD-001"] = dict(
 purpose=("This standard sets requirements for identity proofing, account management, passwords, multi-factor authentication, and federation (PR.AA-01 to PR.AA-04).",
          "มาตรฐานนี้กำหนดข้อกำหนดด้านการพิสูจน์ตัวตน การบริหารบัญชี รหัสผ่าน การยืนยันตัวตนหลายปัจจัย และการเชื่อมโยงตัวตน (PR.AA-01 ถึง PR.AA-04)"),
 sections=[
  ("Requirements", "ข้อกำหนด", "Set measurable identity and authentication requirements, referencing NIST SP 800-63B-4.", "กำหนดข้อกำหนดด้านตัวตนและการยืนยันตัวตนที่วัดผลได้ โดยอ้างอิง NIST SP 800-63B-4",
   {"t": ["ID", "Requirement", "Value"], "r": [
     ["IA-01", "Identity proofing before account creation", "Verify against HR record or government ID for external users"],
     ["IA-02", "Password minimum length (single-factor)", "15 characters"], ["IA-03", "Password minimum length (used with MFA)", "8 characters; 12 recommended"],
     ["IA-04", "Password composition rules and periodic forced change", "Not required; change only on evidence of compromise"],
     ["IA-05", "Block known compromised and common passwords", "Required"], ["IA-06", "Account lockout or throttling", "Lock or delay after 10 failed attempts"],
     ["IA-07", "MFA for remote access, privileged access, cloud admin, email from unmanaged devices", "Required; phishing-resistant MFA (FIDO2) for privileged access"],
     ["IA-08", "Service accounts", "Unique, owner assigned, interactive login disabled, password 25+ characters or managed identity"],
     ["IA-09", "Default and vendor accounts", "Renamed or disabled; default passwords changed before production"],
     ["IA-10", "Session timeout on shared workstations", "Lock after 10 minutes of inactivity"],
     ["IA-11", "Federation and single sign-on", "Use SAML 2.0 or OpenID Connect with signed assertions; validate tokens (PR.AA-04)"]], "w": [1.5, 8.0, 7.0]},
   {"t": ["รหัส", "ข้อกำหนด", "ค่าที่กำหนด"], "r": [
     ["IA-01", "พิสูจน์ตัวตนก่อนสร้างบัญชี", "ตรวจสอบกับข้อมูล HR หรือบัตรประจำตัวสำหรับผู้ใช้ภายนอก"],
     ["IA-02", "ความยาวรหัสผ่านขั้นต่ำ (กรณีใช้ปัจจัยเดียว)", "15 ตัวอักษร"], ["IA-03", "ความยาวรหัสผ่านขั้นต่ำ (กรณีใช้ร่วมกับ MFA)", "8 ตัวอักษร แนะนำ 12 ตัวอักษร"],
     ["IA-04", "กฎการผสมอักขระและการบังคับเปลี่ยนรหัสผ่านตามรอบ", "ไม่บังคับ ให้เปลี่ยนเมื่อมีหลักฐานว่ารหัสผ่านรั่วไหลเท่านั้น"],
     ["IA-05", "บล็อกรหัสผ่านที่รั่วไหลแล้วและรหัสผ่านที่ใช้บ่อย", "บังคับ"], ["IA-06", "การล็อกบัญชีหรือหน่วงเวลา", "ล็อกหรือหน่วงเวลาหลังผิดพลาด 10 ครั้ง"],
     ["IA-07", "MFA สำหรับการเข้าถึงระยะไกล สิทธิ์ระดับสูง ผู้ดูแลระบบคลาวด์ และอีเมลจากอุปกรณ์ที่ไม่ได้บริหารจัดการ", "บังคับ และใช้ MFA ที่ทนต่อฟิชชิ่ง (FIDO2) สำหรับสิทธิ์ระดับสูง"],
     ["IA-08", "บัญชีบริการ (Service account)", "ไม่ซ้ำ มีเจ้าของ ปิดการเข้าสู่ระบบแบบโต้ตอบ รหัสผ่าน 25 ตัวอักษรขึ้นไปหรือใช้ Managed identity"],
     ["IA-09", "บัญชีค่าเริ่มต้นและบัญชีของผู้ขาย", "เปลี่ยนชื่อหรือปิด และเปลี่ยนรหัสผ่านค่าเริ่มต้นก่อนใช้งานจริง"],
     ["IA-10", "การหมดเวลาของเซสชันบนเครื่องที่ใช้ร่วมกัน", "ล็อกหลังไม่มีการใช้งาน 10 นาที"],
     ["IA-11", "การเชื่อมโยงตัวตนและ Single Sign-On", "ใช้ SAML 2.0 หรือ OpenID Connect ที่ลงนาม Assertion และตรวจสอบ Token (PR.AA-04)"]], "w": [1.5, 8.0, 7.0]},
   {"t": ["ID", "Requirement", "CMC value"], "r": [
     ["IA-01", "Identity proofing", "HR record for staff; professional license check for physicians; national ID for patient portal users with OTP to registered phone"],
     ["IA-02", "Password minimum length (single-factor)", "15 characters"], ["IA-03", "Password minimum length (with MFA)", "12 characters"],
     ["IA-04", "Forced periodic change", "Removed in 2025; change on compromise only"], ["IA-05", "Banned password list", "Enabled in the directory"],
     ["IA-06", "Lockout", "10 failed attempts, 15-minute lock"], ["IA-07", "MFA", "Microsoft Authenticator for staff; FIDO2 keys for domain admins; badge tap plus PIN for shared clinical workstations"],
     ["IA-08", "Service accounts", "Inventory in PR-REG-001; HIS interface accounts rotated annually"], ["IA-09", "Default accounts", "Checked at device onboarding by Biomedical Engineering and IT"],
     ["IA-10", "Session timeout", "10 minutes on clinical workstations; 15 minutes elsewhere"], ["IA-11", "Federation", "Microsoft Entra ID SSO for Microsoft 365 and ERP; HIS SSO planned 2027"]], "w": [1.5, 6.0, 9.0]}),
 ],
 bp=[("Follow NIST SP 800-63B guidance: length and breach checks beat complexity rules and forced rotation.", "ปฏิบัติตามแนวทาง NIST SP 800-63B ความยาวรหัสผ่านและการตรวจสอบรหัสผ่านที่รั่วไหลได้ผลดีกว่ากฎความซับซ้อนและการบังคับเปลี่ยนตามรอบ"),
     ("Move privileged users to phishing-resistant MFA first; push-notification MFA is vulnerable to fatigue attacks.", "ให้ผู้มีสิทธิ์ระดับสูงใช้ MFA ที่ทนต่อฟิชชิ่งก่อน เพราะ MFA แบบแจ้งเตือนเสี่ยงต่อการโจมตีแบบส่งคำขอซ้ำ (MFA fatigue)"),
     ("Monitor for impossible travel and anomalous sign-ins.", "เฝ้าระวังการเข้าสู่ระบบจากตำแหน่งที่เป็นไปไม่ได้และการเข้าสู่ระบบที่ผิดปกติ")],
 mistakes=[("Enforcing 90-day password changes, which leads to predictable passwords.", "บังคับเปลี่ยนรหัสผ่านทุก 90 วัน ทำให้ผู้ใช้ตั้งรหัสผ่านที่คาดเดาได้"),
           ("Exempting executives from MFA.", "ยกเว้น MFA ให้ผู้บริหาร")],
)

C["PR-STD-002"] = dict(
 purpose=("This standard sets requirements for managing privileged accounts and administrative access, the most targeted access in ransomware attacks (PR.AA-05).",
          "มาตรฐานนี้กำหนดข้อกำหนดในการบริหารบัญชีสิทธิ์ระดับสูงและการเข้าถึงในฐานะผู้ดูแลระบบ ซึ่งเป็นเป้าหมายหลักของการโจมตีด้วยแรนซัมแวร์ (PR.AA-05)"),
 sections=[
  ("Requirements", "ข้อกำหนด", "Set measurable privileged access requirements.", "กำหนดข้อกำหนดด้านสิทธิ์ระดับสูงที่วัดผลได้",
   {"t": ["ID", "Requirement"], "r": [
     ["PA-01", "Administrators use a separate named privileged account, never their daily user account."],
     ["PA-02", "All privileged accounts are recorded in the Privileged Account Register (PR-REG-001) with owner and justification."],
     ["PA-03", "Privileged access requires phishing-resistant MFA and goes through a privileged access management (PAM) jump host with session recording."],
     ["PA-04", "Domain and cloud tenant administrator accounts are limited to the minimum number (target: no more than 5)."],
     ["PA-05", "Use just-in-time elevation where available; standing privileges are reviewed quarterly."],
     ["PA-06", "Privileged sessions are logged and forwarded to the security monitoring platform."],
     ["PA-07", "Administrators use hardened admin workstations that do not browse the internet or read email."],
     ["PA-08", "Emergency (break-glass) accounts are stored in a sealed vault, monitored, and tested twice a year."],
     ["PA-09", "Local administrator passwords on endpoints and servers are unique and rotated automatically."]], "w": [1.6, 14.9]},
   {"t": ["รหัส", "ข้อกำหนด"], "r": [
     ["PA-01", "ผู้ดูแลระบบใช้บัญชีสิทธิ์ระดับสูงแยกที่ระบุชื่อ และห้ามใช้บัญชีผู้ใช้ประจำวัน"],
     ["PA-02", "บันทึกบัญชีสิทธิ์ระดับสูงทุกบัญชีในทะเบียนบัญชีสิทธิ์ระดับสูง (PR-REG-001) พร้อมเจ้าของและเหตุผล"],
     ["PA-03", "การเข้าถึงด้วยสิทธิ์ระดับสูงต้องใช้ MFA ที่ทนต่อฟิชชิ่ง และผ่าน Jump host ของระบบบริหารสิทธิ์ระดับสูง (PAM) ที่บันทึกเซสชัน"],
     ["PA-04", "จำกัดบัญชีผู้ดูแลโดเมนและผู้ดูแล Tenant คลาวด์ให้น้อยที่สุด (เป้าหมาย: ไม่เกิน 5 บัญชี)"],
     ["PA-05", "ใช้การยกระดับสิทธิ์เฉพาะเมื่อจำเป็น (Just-in-time) เมื่อทำได้ และทบทวนสิทธิ์ถาวรทุกไตรมาส"],
     ["PA-06", "บันทึก Log เซสชันสิทธิ์ระดับสูงและส่งไปยังระบบเฝ้าระวังความมั่นคงปลอดภัย"],
     ["PA-07", "ผู้ดูแลระบบใช้เครื่องสำหรับผู้ดูแลระบบที่เสริมความแข็งแรงแล้ว และไม่ใช้ท่องอินเทอร์เน็ตหรืออ่านอีเมล"],
     ["PA-08", "เก็บบัญชีฉุกเฉิน (Break-glass) ในตู้นิรภัยที่ปิดผนึก เฝ้าระวัง และทดสอบปีละ 2 ครั้ง"],
     ["PA-09", "รหัสผ่านผู้ดูแลระบบภายในเครื่องของอุปกรณ์ปลายทางและเซิร์ฟเวอร์ต้องไม่ซ้ำกันและเปลี่ยนอัตโนมัติ"]], "w": [1.6, 14.9]}),
 ],
 bp=[("Implement a tiered administration model (Tier 0 identity systems, Tier 1 servers, Tier 2 workstations) to stop credential reuse across tiers.", "ใช้รูปแบบการแบ่งระดับผู้ดูแลระบบ (Tier 0 ระบบตัวตน Tier 1 เซิร์ฟเวอร์ Tier 2 เครื่องผู้ใช้) เพื่อป้องกันการนำข้อมูลยืนยันตัวตนไปใช้ข้ามระดับ"),
     ("Route all vendor administrative access through the same PAM platform.", "ให้การเข้าถึงในฐานะผู้ดูแลระบบของผู้ให้บริการทั้งหมดผ่านระบบ PAM เดียวกัน")],
 mistakes=[("Dozens of domain administrator accounts, many unused or belonging to former vendors.", "มีบัญชีผู้ดูแลโดเมนหลายสิบบัญชี ซึ่งหลายบัญชีไม่ได้ใช้หรือเป็นของผู้ให้บริการเดิม")],
 rev="Updated in June 2026 after the PAM platform went live for domain administrators and HIS administrators (MR26-01).",
)

C["PR-STD-003"] = dict(
 purpose=("This standard sets requirements for remote access by staff and third parties, including VPN, remote desktop, and vendor support tools.",
          "มาตรฐานนี้กำหนดข้อกำหนดการเข้าถึงระยะไกลของบุคลากรและบุคคลภายนอก รวมถึง VPN Remote desktop และเครื่องมือสนับสนุนของผู้ขาย"),
 sections=[
  ("Requirements", "ข้อกำหนด", "Set remote access requirements for staff and vendors.", "กำหนดข้อกำหนดการเข้าถึงระยะไกลสำหรับบุคลากรและผู้ให้บริการ",
   {"t": ["ID", "Requirement"], "r": [
     ["RA-01", "Remote access only through approved solutions (VPN or zero trust network access) with MFA."],
     ["RA-02", "No remote desktop protocol (RDP) or administration ports exposed directly to the internet."],
     ["RA-03", "Devices connecting remotely must be organization-managed or pass a device health check."],
     ["RA-04", "Third-party remote access is approved per session or for a defined period (PR-FRM-003), uses named accounts, and goes through the PAM jump host with session recording."],
     ["RA-05", "Vendor remote access tools installed on our systems (for example, unattended remote support agents) are prohibited unless approved and inventoried."],
     ["RA-06", "Remote sessions time out after [30] minutes of inactivity."],
     ["RA-07", "Remote access logs are retained and monitored."]], "w": [1.6, 14.9]},
   {"t": ["รหัส", "ข้อกำหนด"], "r": [
     ["RA-01", "เข้าถึงระยะไกลผ่านช่องทางที่อนุมัติเท่านั้น (VPN หรือ Zero trust network access) และใช้ MFA"],
     ["RA-02", "ห้ามเปิดพอร์ต Remote Desktop Protocol (RDP) หรือพอร์ตสำหรับผู้ดูแลระบบสู่อินเทอร์เน็ตโดยตรง"],
     ["RA-03", "อุปกรณ์ที่เชื่อมต่อระยะไกลต้องเป็นอุปกรณ์ที่องค์กรบริหารจัดการ หรือผ่านการตรวจสอบสถานะความพร้อมของอุปกรณ์"],
     ["RA-04", "การเข้าถึงระยะไกลของบุคคลภายนอกต้องได้รับอนุมัติเป็นรายครั้งหรือตามช่วงเวลาที่กำหนด (PR-FRM-003) ใช้บัญชีที่ระบุชื่อ และผ่าน Jump host ของ PAM ที่บันทึกเซสชัน"],
     ["RA-05", "ห้ามติดตั้งเครื่องมือเข้าถึงระยะไกลของผู้ขายบนระบบขององค์กร (เช่น Agent สนับสนุนระยะไกลแบบไม่ต้องมีผู้ดูแล) เว้นแต่ได้รับอนุมัติและบันทึกในทะเบียน"],
     ["RA-06", "เซสชันระยะไกลหมดเวลาหลังไม่มีการใช้งาน [30] นาที"],
     ["RA-07", "เก็บรักษาและเฝ้าระวัง Log การเข้าถึงระยะไกล"]], "w": [1.6, 14.9]},
   {"t": ["ID", "CMC requirement"], "r": [
     ["RA-01", "Staff remote access through the CMC VPN with Microsoft Authenticator MFA."],
     ["RA-02", "External attack surface scan weekly confirms no RDP exposure."],
     ["RA-03", "Only CMC-managed laptops can connect to the VPN; physicians use the HIS web portal through the reverse proxy with MFA."],
     ["RA-04", "HIS Vendor A, PACS Vendor B, and LIS Vendor C connect through the PAM jump host; sessions recorded and kept 180 days."],
     ["RA-05", "Two unapproved remote support agents found on modality workstations in 2026 were removed (INC-2026-021)."],
     ["RA-06", "30 minutes for staff VPN; 15 minutes for vendor sessions."],
     ["RA-07", "VPN and jump host logs forwarded to the MSSP."]], "w": [1.6, 14.9]}),
 ],
 bp=[("Prefer zero trust network access that grants access per application rather than full network access.", "เลือกใช้ Zero trust network access ที่ให้สิทธิ์ระดับแอปพลิเคชัน แทนการเข้าถึงเครือข่ายทั้งหมด"),
     ("Disable vendor accounts by default and enable them only for approved sessions.", "ปิดบัญชีของผู้ให้บริการเป็นค่าเริ่มต้น และเปิดใช้เฉพาะเซสชันที่ได้รับอนุมัติ")],
 mistakes=[("Vendors keep always-on VPN accounts with shared passwords for years.", "ผู้ให้บริการมีบัญชี VPN ที่เปิดตลอดเวลาและใช้รหัสผ่านร่วมกันเป็นเวลาหลายปี")],
 rev="Updated in August 2026 after the PACS vendor remote access issue: unapproved remote support agents prohibited and vendor session timeout reduced.",
)

C["PR-PRC-001"] = dict(
 purpose=("This procedure describes how user access is requested, approved, provisioned, changed, and removed for joiners, movers, and leavers (PR.AA-01, PR.AA-05).",
          "ระเบียบปฏิบัตินี้อธิบายวิธีขอ อนุมัติ จัดสรร เปลี่ยนแปลง และถอนสิทธิ์ผู้ใช้สำหรับพนักงานเข้าใหม่ ย้ายงาน และพ้นสภาพ (PR.AA-01, PR.AA-05)"),
 sections=[
  ("Process Steps", "ขั้นตอนการดำเนินงาน", "Describe steps for joiner, mover, and leaver events with timelines.", "อธิบายขั้นตอนสำหรับการเข้าใหม่ ย้ายงาน และพ้นสภาพ พร้อมระยะเวลา",
   {"t": ["Event", "Step", "Actor", "Timing"], "r": [
     ["Joiner", "HR creates the record; manager submits User Access Request (PR-FRM-001) based on role profile", "HR, line manager", "Before start date"],
     ["Joiner", "System owner approves; IT provisions and records the ticket", "System owner, IT", "Within 2 working days"],
     ["Mover", "HR records transfer; manager requests new access; old access removed", "HR, manager, IT", "Old access removed within 5 working days"],
     ["Leaver", "HR notifies; IT disables accounts and completes GV-FRM-003", "HR, IT", "On last working day"],
     ["Temporary access", "Request with end date; access expires automatically", "Requester, IT", "As approved"],
     ["All", "Requests without approval are rejected; approvers cannot approve their own access", "IT", "Always"]], "w": [2.5, 8.5, 3.0, 2.5]},
   {"t": ["เหตุการณ์", "ขั้นตอน", "ผู้ดำเนินการ", "ระยะเวลา"], "r": [
     ["เข้าใหม่", "HR สร้างข้อมูลพนักงาน ผู้บังคับบัญชายื่นแบบฟอร์มขอสิทธิ์ (PR-FRM-001) ตามโปรไฟล์บทบาท", "HR ผู้บังคับบัญชา", "ก่อนวันเริ่มงาน"],
     ["เข้าใหม่", "เจ้าของระบบอนุมัติ ฝ่าย IT จัดสรรสิทธิ์และบันทึกงาน", "เจ้าของระบบ ฝ่าย IT", "ภายใน 2 วันทำการ"],
     ["ย้ายงาน", "HR บันทึกการย้าย ผู้บังคับบัญชาขอสิทธิ์ใหม่ และถอนสิทธิ์เดิม", "HR ผู้บังคับบัญชา ฝ่าย IT", "ถอนสิทธิ์เดิมภายใน 5 วันทำการ"],
     ["พ้นสภาพ", "HR แจ้ง ฝ่าย IT ปิดบัญชีและดำเนินการตาม GV-FRM-003", "HR ฝ่าย IT", "ในวันทำงานสุดท้าย"],
     ["สิทธิ์ชั่วคราว", "ขอพร้อมวันสิ้นสุด และสิทธิ์หมดอายุโดยอัตโนมัติ", "ผู้ขอ ฝ่าย IT", "ตามที่อนุมัติ"],
     ["ทุกกรณี", "ปฏิเสธคำขอที่ไม่มีการอนุมัติ และผู้อนุมัติต้องไม่อนุมัติสิทธิ์ของตนเอง", "ฝ่าย IT", "ตลอดเวลา"]], "w": [2.5, 8.5, 3.0, 2.5]}),
 ],
 bp=[("Automate provisioning from the HR system using role-based profiles.", "จัดสรรสิทธิ์โดยอัตโนมัติจากระบบ HR ด้วยโปรไฟล์ตามบทบาท"),
     ("Measure time to provision and time to deprovision as KPIs.", "วัดระยะเวลาการจัดสรรและการถอนสิทธิ์เป็น KPI")],
 mistakes=[("Movers keep old access, accumulating rights over years.", "พนักงานที่ย้ายงานยังคงมีสิทธิ์เดิม ทำให้สิทธิ์สะสมเพิ่มขึ้นตลอดหลายปี")],
)

C["PR-PRC-002"] = dict(
 purpose=("This procedure defines how system owners review user and privileged access periodically to confirm it is still appropriate, and how excess access is removed (PR.AA-05).",
          "ระเบียบปฏิบัตินี้กำหนดวิธีที่เจ้าของระบบทบทวนสิทธิ์ผู้ใช้และสิทธิ์ระดับสูงตามรอบ เพื่อยืนยันว่ายังเหมาะสม และวิธีถอนสิทธิ์ที่เกินจำเป็น (PR.AA-05)"),
 sections=[
  ("Review Frequency", "ความถี่ในการทบทวน", "Set review frequency by access type.", "กำหนดความถี่ในการทบทวนตามประเภทสิทธิ์",
   {"t": ["Access type", "Frequency", "Reviewer"], "r": [["Privileged accounts", "Quarterly", "[CISO] and system owner"], ["Critical systems", "Quarterly", "System owner"], ["Other systems", "Semi-annually", "System owner"], ["Third-party accounts", "Quarterly", "Business owner of the supplier"]], "w": [6.0, 4.0, 6.5]},
   {"t": ["ประเภทสิทธิ์", "ความถี่", "ผู้ทบทวน"], "r": [["บัญชีสิทธิ์ระดับสูง", "ทุกไตรมาส", "[CISO] และเจ้าของระบบ"], ["ระบบสำคัญ", "ทุกไตรมาส", "เจ้าของระบบ"], ["ระบบอื่น", "ทุก 6 เดือน", "เจ้าของระบบ"], ["บัญชีของบุคคลภายนอก", "ทุกไตรมาส", "เจ้าของธุรกิจที่ดูแลผู้ให้บริการ"]], "w": [6.0, 4.0, 6.5]}),
  ("Process Steps", "ขั้นตอนการดำเนินงาน", "Describe the review cycle.", "อธิบายรอบการทบทวน",
   {"n": ["IT extracts the current access list from the system, with roles and last login.", "The reviewer confirms, changes, or removes each entry within 10 working days.", "IT removes rejected access within 5 working days.",
          "IT reruns the extract to verify removals.", "The reviewer signs the User Access Review Record (PR-REC-001).", "The [CISO] reports completion and exceptions to the [ISSC]."]},
   {"n": ["ฝ่าย IT ดึงรายการสิทธิ์ปัจจุบันจากระบบ พร้อมบทบาทและวันที่เข้าสู่ระบบล่าสุด", "ผู้ทบทวนยืนยัน เปลี่ยนแปลง หรือถอนสิทธิ์แต่ละรายการภายใน 10 วันทำการ", "ฝ่าย IT ถอนสิทธิ์ที่ถูกปฏิเสธภายใน 5 วันทำการ",
          "ฝ่าย IT ดึงข้อมูลอีกครั้งเพื่อยืนยันการถอนสิทธิ์", "ผู้ทบทวนลงนามในบันทึกผลการทบทวนสิทธิ์ (PR-REC-001)", "[CISO] รายงานความครบถ้วนและข้อยกเว้นต่อ [ISSC]"]}),
 ],
 bp=[("Include last login dates so reviewers can spot dormant accounts.", "แสดงวันที่เข้าสู่ระบบล่าสุด เพื่อให้ผู้ทบทวนเห็นบัญชีที่ไม่ได้ใช้งาน"),
     ("Disable accounts with no login for 90 days automatically.", "ปิดบัญชีที่ไม่ได้เข้าสู่ระบบ 90 วันโดยอัตโนมัติ")],
 mistakes=[("Reviewers approve the whole list without checking (rubber stamping).", "ผู้ทบทวนอนุมัติทั้งรายการโดยไม่ตรวจสอบ")],
)

C["PR-FRM-001"] = dict(
 purpose=("This form requests, justifies, and approves user access to a system.", "แบบฟอร์มนี้ใช้ขอ ระบุเหตุผล และอนุมัติสิทธิ์การเข้าใช้งานระบบ"),
 fields=[
  ("Request number", "เลขที่คำขอ", "Assigned by IT service desk.", "กำหนดโดย IT Service Desk", "UAR-2026-0001"),
  ("Request type", "ประเภทคำขอ", "New, Change, Remove, Temporary.", "ใหม่ เปลี่ยนแปลง ถอน ชั่วคราว", ("New", "ใหม่")),
  ("User name, employee ID, position, department", "ชื่อผู้ใช้ รหัสพนักงาน ตำแหน่ง หน่วยงาน", "Identity of the user.", "ข้อมูลตัวตนของผู้ใช้", ""),
  ("Employment type", "ประเภทการจ้าง", "Employee, contractor, vendor, student.", "พนักงาน ผู้รับจ้าง ผู้ให้บริการ นักศึกษา", ""),
  ("System and role or profile requested", "ระบบและบทบาทหรือโปรไฟล์ที่ขอ", "Use the standard role profile where available.", "ใช้โปรไฟล์บทบาทมาตรฐานเมื่อมี", ""),
  ("Business justification", "เหตุผลทางธุรกิจ", "Why the access is needed.", "เหตุผลที่ต้องการสิทธิ์", ""),
  ("Access period", "ช่วงเวลาการใช้สิทธิ์", "Permanent or end date.", "ถาวร หรือวันสิ้นสุด", ""),
  ("Data classification accessed", "ชั้นข้อมูลที่เข้าถึง", "Highest class per PR-STD-004.", "ชั้นสูงสุดตาม PR-STD-004", ""),
  ("AUP and NDA acknowledged", "รับทราบ AUP และ NDA แล้ว", "Yes with date.", "ใช่ พร้อมวันที่", ""),
  ("Provisioned by and date", "ผู้จัดสรรสิทธิ์และวันที่", "Completed by IT.", "กรอกโดยฝ่าย IT", ""),
 ],
 cmc_vals=["UAR-2026-1184", "New", "Registered Nurse (name withheld in sample), employee 26-0451, Ward 6B, Nursing Department", "Employee",
           "HIS: Nurse Ward profile (Ward 6B); LIS: results viewer; Microsoft 365 E3", "Inpatient nursing care on Ward 6B", "Permanent", "Restricted (patient data)",
           "AUP and GV-FRM-002 signed 1 September 2026", "IT Service Desk, 2 September 2026"],
 approvals=["Line Manager", "SYSOWN", "ITM"],
 bp=[("Pre-fill role profiles so managers select a role instead of listing individual permissions.", "กำหนดโปรไฟล์บทบาทไว้ล่วงหน้า เพื่อให้ผู้บังคับบัญชาเลือกบทบาทแทนการระบุสิทธิ์ทีละรายการ")],
 mistakes=[("IT grants access on verbal or chat requests without a record.", "ฝ่าย IT ให้สิทธิ์ตามคำขอทางวาจาหรือข้อความแชตโดยไม่มีบันทึก")],
)

C["PR-FRM-002"] = dict(
 purpose=("This form requests and approves privileged (administrative) access with stronger justification and controls than normal access.",
          "แบบฟอร์มนี้ใช้ขอและอนุมัติสิทธิ์ระดับสูง (ผู้ดูแลระบบ) ซึ่งต้องมีเหตุผลและการควบคุมที่เข้มงวดกว่าสิทธิ์ทั่วไป"),
 fields=[
  ("Request number", "เลขที่คำขอ", "Assigned by security team.", "กำหนดโดยทีมความมั่นคงปลอดภัย", "PAR-2026-001"),
  ("Requester and role", "ผู้ขอและบทบาท", "Name and position.", "ชื่อและตำแหน่ง", ""),
  ("Privileged account name", "ชื่อบัญชีสิทธิ์ระดับสูง", "Separate admin account (for example, adm-name).", "บัญชีผู้ดูแลแยก (เช่น adm-ชื่อ)", ""),
  ("Systems and privilege level", "ระบบและระดับสิทธิ์", "Domain admin, server admin, database admin, application admin.", "ผู้ดูแลโดเมน ผู้ดูแลเซิร์ฟเวอร์ ผู้ดูแลฐานข้อมูล ผู้ดูแลแอปพลิเคชัน", ""),
  ("Justification", "เหตุผล", "Specific tasks requiring privilege.", "งานเฉพาะที่ต้องใช้สิทธิ์ระดับสูง", ""),
  ("Access mode", "รูปแบบการเข้าถึง", "Standing or just-in-time; through PAM.", "ถาวร หรือ Just-in-time ผ่าน PAM", ""),
  ("Duration", "ระยะเวลา", "End date; maximum 12 months before re-approval.", "วันสิ้นสุด สูงสุด 12 เดือนก่อนต้องอนุมัติใหม่", ""),
  ("Controls confirmed", "ยืนยันมาตรการควบคุม", "Phishing-resistant MFA, PAM vaulting, session recording.", "MFA ที่ทนต่อฟิชชิ่ง การเก็บรหัสใน PAM การบันทึกเซสชัน", ""),
 ],
 cmc_vals=["PAR-2026-014", "Security Engineer (name withheld in sample)", "adm-se02", "Windows server administrator for clinical server zone; no domain admin",
           "Deploy EDR agents and security configuration baselines on clinical servers", "Just-in-time through PAM, 4-hour elevation per request", "1 April 2026 to 31 March 2027",
           "FIDO2 key issued; account vaulted in PAM; sessions recorded"],
 approvals=["Requester", "SYSOWN", "CISO", "CIO"],
 bp=[("Require the CISO to approve all Tier 0 (identity system) privileges.", "กำหนดให้ CISO อนุมัติสิทธิ์ระดับ Tier 0 (ระบบตัวตน) ทุกรายการ")],
 mistakes=[("Granting domain admin for convenience when server admin would do.", "ให้สิทธิ์ผู้ดูแลโดเมนเพื่อความสะดวก ทั้งที่สิทธิ์ผู้ดูแลเซิร์ฟเวอร์ก็เพียงพอ")],
)

C["PR-FRM-003"] = dict(
 purpose=("This form requests and approves remote access by a third party (vendor, contractor, or partner) for support or maintenance.",
          "แบบฟอร์มนี้ใช้ขอและอนุมัติการเข้าถึงระยะไกลของบุคคลภายนอก (ผู้ขาย ผู้รับจ้าง หรือพันธมิตร) เพื่อการสนับสนุนหรือบำรุงรักษา"),
 fields=[
  ("Request number", "เลขที่คำขอ", "Assigned by security team.", "กำหนดโดยทีมความมั่นคงปลอดภัย", "TRA-2026-001"),
  ("Supplier and supplier ID", "ผู้ให้บริการและรหัสผู้ให้บริการ", "From GV-REG-009.", "จาก GV-REG-009", ""),
  ("Named individuals", "รายชื่อบุคคล", "Each person needs a named account.", "แต่ละคนต้องมีบัญชีที่ระบุชื่อ", ""),
  ("Target systems", "ระบบเป้าหมาย", "Hosts or applications.", "เครื่องหรือแอปพลิเคชัน", ""),
  ("Purpose and ticket reference", "วัตถุประสงค์และเลขที่งาน", "Support case or change number.", "เลขเคสสนับสนุนหรือเลขที่การเปลี่ยนแปลง", ""),
  ("Access window", "ช่วงเวลาการเข้าถึง", "Start and end date and time.", "วันและเวลาเริ่มต้นและสิ้นสุด", ""),
  ("Access method", "วิธีการเข้าถึง", "PAM jump host with MFA and session recording.", "Jump host ของ PAM พร้อม MFA และการบันทึกเซสชัน", ""),
  ("NDA and contract confirmed", "ยืนยัน NDA และสัญญา", "GV-FRM-002 and contract clauses in place.", "มี GV-FRM-002 และข้อสัญญาครบถ้วน", ""),
  ("Account disabled after window", "ปิดบัญชีหลังหมดช่วงเวลา", "Date and by whom.", "วันที่และผู้ดำเนินการ", ""),
 ],
 cmc_vals=["TRA-2026-0207", "PACS Vendor B (SUP-002)", "Two named support engineers (names withheld in sample)", "PACS application servers PACS-APP01 and PACS-APP02",
           "Vendor case 55812; change CHG-2026-0612 PACS minor upgrade", "14 September 2026 22:00 to 15 September 2026 04:00", "CMC PAM jump host, Microsoft Authenticator MFA, sessions recorded",
           "GV-FRM-002 on file; contract clause SC-05 confirmed", "Disabled automatically 15 September 2026 04:00; verified by Security Engineer"],
 approvals=["SYSOWN", "CISO"],
 bp=[("Make vendor accounts disabled by default and time-bound by the form.", "กำหนดให้บัญชีผู้ให้บริการปิดเป็นค่าเริ่มต้น และเปิดตามช่วงเวลาที่ระบุในแบบฟอร์ม")],
 mistakes=[("One request covers an entire contract year for an unnamed vendor team.", "คำขอเดียวครอบคลุมทั้งปีสัญญาสำหรับทีมผู้ขายที่ไม่ระบุชื่อ")],
)

C["PR-REC-001"] = dict(
 purpose=("This record documents the result of each periodic user access review, with decisions, removals, and reviewer sign-off, as audit evidence (PR.AA-05).",
          "บันทึกนี้ใช้บันทึกผลการทบทวนสิทธิ์ผู้ใช้ตามรอบ พร้อมการตัดสินใจ การถอนสิทธิ์ และการลงนามของผู้ทบทวน เป็นหลักฐานการตรวจสอบ (PR.AA-05)"),
 fields=[
  ("Review ID", "รหัสการทบทวน", "System and period.", "ระบบและช่วงเวลา", "UARV-HIS-2026Q3"),
  ("System", "ระบบ", "System reviewed.", "ระบบที่ทบทวน", "HIS"),
  ("Accounts reviewed", "จำนวนบัญชีที่ทบทวน", "Total in extract.", "จำนวนทั้งหมดในข้อมูลที่ดึง", ""),
  ("Confirmed", "ยืนยันคงไว้", "Number kept unchanged.", "จำนวนที่คงไว้", ""),
  ("Modified", "เปลี่ยนแปลง", "Number with role changes.", "จำนวนที่เปลี่ยนบทบาท", ""),
  ("Removed", "ถอนสิทธิ์", "Number removed.", "จำนวนที่ถอน", ""),
  ("Removal verified on", "ยืนยันการถอนเมื่อ", "Date of re-extract check.", "วันที่ตรวจสอบซ้ำ", ""),
  ("Reviewer and sign-off date", "ผู้ทบทวนและวันที่ลงนาม", "System owner.", "เจ้าของระบบ", ""),
 ],
 rows=[
  ["UARV-HIS-2026Q2", "HIS", "1,402", "1,355", "31", "16", "15/07/2026", "Medical Director and Director of Nursing, 10/07/2026"],
  ["UARV-HIS-2026Q3", "HIS", "1,418", "1,380", "22", "16", "14/10/2026", "Medical Director and Director of Nursing, 09/10/2026"],
  ["UARV-PAM-2026Q3", "Privileged accounts (all)", "46", "41", "2", "3", "08/10/2026", "Security Manager and IT Infrastructure Manager, 06/10/2026"],
  ["UARV-ERP-2026H1", "ERP", "214", "198", "9", "7", "20/07/2026", "CFO, 15/07/2026"],
 ],
 bp=[("Keep the extract file with the record to show what the reviewer saw.", "เก็บไฟล์ข้อมูลที่ดึงไว้ร่วมกับบันทึก เพื่อแสดงสิ่งที่ผู้ทบทวนเห็น")],
 mistakes=[("Recording completion without evidence that removals happened.", "บันทึกว่าทบทวนเสร็จแล้วโดยไม่มีหลักฐานว่าได้ถอนสิทธิ์จริง")],
)

C["PR-REG-001"] = dict(
 purpose=("This register lists all privileged, service, shared, and emergency accounts with owner, purpose, controls, and review date (PR.AA-05).",
          "ทะเบียนนี้ระบุบัญชีสิทธิ์ระดับสูง บัญชีบริการ บัญชีใช้ร่วม และบัญชีฉุกเฉินทั้งหมด พร้อมเจ้าของ วัตถุประสงค์ มาตรการควบคุม และวันที่ทบทวน (PR.AA-05)"),
 fields=[
  ("Account", "บัญชี", "Account name.", "ชื่อบัญชี", "adm-jdoe"),
  ("Type", "ประเภท", "Admin, service, shared, emergency.", "ผู้ดูแล บริการ ใช้ร่วม ฉุกเฉิน", ""),
  ("System and privilege", "ระบบและสิทธิ์", "Scope of privilege.", "ขอบเขตสิทธิ์", ""),
  ("Owner", "เจ้าของ", "Accountable person or role.", "บุคคลหรือบทบาทที่รับผิดชอบ", ""),
  ("Purpose", "วัตถุประสงค์", "Why it exists.", "เหตุผลที่มีบัญชี", ""),
  ("Controls", "มาตรการควบคุม", "MFA, vaulted, recorded, rotation.", "MFA เก็บใน Vault บันทึกเซสชัน เปลี่ยนรหัส", ""),
  ("Approval reference", "เลขอ้างอิงการอนุมัติ", "PR-FRM-002 number.", "เลขที่ PR-FRM-002", ""),
  ("Last reviewed", "ทบทวนล่าสุด", "Date.", "วันที่", ""),
 ],
 rows=[
  ["adm-itm01", "Admin", "Domain administrator (Tier 0)", "IT Infrastructure Manager", "Directory administration", "FIDO2 MFA, PAM vaulted, sessions recorded", "PAR-2026-003", "06/10/2026"],
  ["svc-his-hl7", "Service", "HIS interface engine database read and write", "Application Manager", "HL7 interface between HIS, PACS, LIS", "No interactive login; 32-character password rotated annually", "PAR-2025-021", "06/10/2026"],
  ["bg-domain-01", "Emergency", "Domain administrator", "Security Manager", "Break-glass if PAM unavailable", "Sealed in safe; alert on use; tested 06/2026", "PAR-2025-001", "06/10/2026"],
  ["vnd-pacsb-01", "Vendor", "PACS application administrator", "Director of Radiology", "Vendor B support", "Disabled by default; enabled per TRA form; recorded", "PAR-2026-009", "06/10/2026"],
 ],
 bp=[("Discover privileged accounts with tools, not only from requests, to find unknown admins.", "ค้นหาบัญชีสิทธิ์ระดับสูงด้วยเครื่องมือ ไม่ใช่จากคำขอเท่านั้น เพื่อพบผู้ดูแลที่ไม่รู้จัก")],
 mistakes=[("Service accounts with domain admin rights and passwords unchanged for years.", "บัญชีบริการมีสิทธิ์ผู้ดูแลโดเมนและไม่เคยเปลี่ยนรหัสผ่านมาหลายปี")],
)

C["PR-POL-002"] = dict(
 purpose=("This policy sets principles for protecting facilities, equipment, and people from unauthorized physical access and environmental threats (PR.AA-06, PR.IR-02, DE.CM-02).",
          "นโยบายนี้กำหนดหลักการในการปกป้องสถานที่ อุปกรณ์ และบุคลากรจากการเข้าถึงทางกายภาพโดยไม่ได้รับอนุญาตและภัยคุกคามจากสภาพแวดล้อม (PR.AA-06, PR.IR-02, DE.CM-02)"),
 sections=[
  ("Security Zones and Controls", "เขตความมั่นคงปลอดภัยและมาตรการ", "Define physical zones and required controls.", "กำหนดเขตทางกายภาพและมาตรการที่ต้องมี",
   {"t": ["Zone", "Examples", "Minimum controls"], "r": [
     ["Public", "Lobby, reception", "Staffed reception, CCTV"], ["Internal", "Offices, wards", "Badge access or staffed entry, visitor badges"],
     ["Secure", "Server rooms, network closets", "Badge plus PIN, access list, CCTV, access log reviewed monthly"],
     ["Critical", "Data center", "Two-factor entry, escort for visitors, CCTV with 90-day retention, environmental monitoring"]], "w": [2.5, 5.5, 8.5]},
   {"t": ["เขต", "ตัวอย่าง", "มาตรการขั้นต่ำ"], "r": [
     ["สาธารณะ", "ล็อบบี้ แผนกต้อนรับ", "มีเจ้าหน้าที่ต้อนรับ กล้องวงจรปิด"], ["ภายใน", "สำนักงาน หอผู้ป่วย", "บัตรผ่านหรือมีเจ้าหน้าที่ควบคุมทางเข้า บัตรผู้มาติดต่อ"],
     ["ปลอดภัย", "ห้องเซิร์ฟเวอร์ ตู้เครือข่าย", "บัตรผ่านพร้อม PIN รายชื่อผู้มีสิทธิ์ กล้องวงจรปิด ทบทวน Log การเข้าออกทุกเดือน"],
     ["วิกฤต", "ศูนย์ข้อมูล", "การเข้าออกสองปัจจัย ผู้มาติดต่อต้องมีผู้นำพา กล้องวงจรปิดเก็บ 90 วัน การเฝ้าระวังสภาพแวดล้อม"]], "w": [2.5, 5.5, 8.5]}),
  ("Environmental Protection", "การป้องกันด้านสภาพแวดล้อม", "Set requirements against fire, flood, power, and temperature threats (PR.IR-02).", "กำหนดข้อกำหนดป้องกันไฟไหม้ น้ำท่วม ไฟฟ้า และอุณหภูมิ (PR.IR-02)",
   ["Critical facilities have fire detection and suppression suitable for IT equipment, uninterruptible power supply (UPS), generator backup, and temperature and humidity monitoring with alerts.",
    "Equipment is placed above flood level where flood risk exists.", "Environmental systems are tested and maintained on schedule."],
   ["สถานที่สำคัญต้องมีระบบตรวจจับและดับเพลิงที่เหมาะกับอุปกรณ์ IT เครื่องสำรองไฟฟ้า (UPS) เครื่องกำเนิดไฟฟ้าสำรอง และระบบเฝ้าระวังอุณหภูมิและความชื้นพร้อมแจ้งเตือน",
    "ติดตั้งอุปกรณ์สูงกว่าระดับน้ำท่วมในพื้นที่ที่มีความเสี่ยงน้ำท่วม", "ทดสอบและบำรุงรักษาระบบสภาพแวดล้อมตามกำหนด"],
   ["The Riverside data center has gas fire suppression, dual UPS, a generator with 48 hours of fuel, and temperature alerts to the IT on-call phone.",
    "After the 2011 flood experience, Riverside network equipment was moved to the third floor.", "Generator load tests run monthly; UPS battery tests quarterly by Facilities."]),
 ],
 bp=[("Review physical access lists for secure areas monthly and remove leavers immediately.", "ทบทวนรายชื่อผู้มีสิทธิ์เข้าเขตปลอดภัยทุกเดือน และถอนสิทธิ์ผู้พ้นสภาพทันที"),
     ("Integrate badge system events with security monitoring for after-hours alerts.", "เชื่อมเหตุการณ์จากระบบบัตรผ่านเข้ากับระบบเฝ้าระวัง เพื่อแจ้งเตือนการเข้าออกนอกเวลา")],
 mistakes=[("Network closets left unlocked or used as storage rooms.", "ตู้หรือห้องเครือข่ายไม่ได้ล็อกหรือถูกใช้เป็นห้องเก็บของ")],
)

C["PR-PRC-003"] = dict(
 purpose=("This procedure describes how physical access to secure and critical areas is requested, granted, monitored, reviewed, and revoked, and how visitors are handled (PR.AA-06).",
          "ระเบียบปฏิบัตินี้อธิบายวิธีขอ อนุมัติ เฝ้าระวัง ทบทวน และยกเลิกการเข้าถึงเขตปลอดภัยและเขตวิกฤต และวิธีจัดการผู้มาติดต่อ (PR.AA-06)"),
 sections=[
  ("Process Steps", "ขั้นตอนการดำเนินงาน", "Describe steps for staff access and visitor access.", "อธิบายขั้นตอนสำหรับการเข้าถึงของบุคลากรและผู้มาติดต่อ",
   {"t": ["Activity", "Actor", "Control"], "r": [
     ["Request access to a secure area with justification", "Requester's manager", "Area owner approves"], ["Program badge and add to the access list", "[FAC]", "Access list updated"],
     ["Register visitors, check ID, issue temporary badge, escort in secure areas", "Reception or area owner", "Visitor log (PR-FRM-004)"],
     ["Review access logs for secure areas monthly; investigate anomalies", "[FAC] with [CISO]", "Review record"], ["Revoke badges for leavers on the last day", "HR, [FAC]", "GV-FRM-003"]], "w": [8.0, 4.0, 4.5]},
   {"t": ["กิจกรรม", "ผู้ดำเนินการ", "มาตรการควบคุม"], "r": [
     ["ขอสิทธิ์เข้าเขตปลอดภัยพร้อมเหตุผล", "ผู้บังคับบัญชาของผู้ขอ", "เจ้าของพื้นที่อนุมัติ"], ["ตั้งค่าบัตรและเพิ่มในรายชื่อผู้มีสิทธิ์", "[FAC]", "ปรับปรุงรายชื่อผู้มีสิทธิ์"],
     ["ลงทะเบียนผู้มาติดต่อ ตรวจบัตรประจำตัว ออกบัตรชั่วคราว และนำพาในเขตปลอดภัย", "แผนกต้อนรับหรือเจ้าของพื้นที่", "แบบบันทึกผู้มาติดต่อ (PR-FRM-004)"],
     ["ทบทวน Log การเข้าออกเขตปลอดภัยทุกเดือน และสอบสวนความผิดปกติ", "[FAC] ร่วมกับ [CISO]", "บันทึกการทบทวน"], ["ยกเลิกบัตรของผู้พ้นสภาพในวันสุดท้าย", "HR [FAC]", "GV-FRM-003"]], "w": [8.0, 4.0, 4.5]}),
 ],
 bp=[("Collect only the visitor data needed and inform visitors through a privacy notice.", "เก็บข้อมูลผู้มาติดต่อเท่าที่จำเป็น และแจ้งผ่านประกาศความเป็นส่วนตัว")],
 mistakes=[("Vendor engineers enter the data center unescorted on a shared badge.", "วิศวกรของผู้ขายเข้าศูนย์ข้อมูลโดยไม่มีผู้นำพาและใช้บัตรร่วมกัน")],
)

C["PR-FRM-004"] = dict(
 purpose=("This log records each entry to secure and critical areas by visitors and non-authorized staff, as evidence of controlled physical access.",
          "แบบบันทึกนี้ใช้บันทึกการเข้าเขตปลอดภัยและเขตวิกฤตของผู้มาติดต่อและบุคลากรที่ไม่ได้อยู่ในรายชื่อผู้มีสิทธิ์ เพื่อเป็นหลักฐานการควบคุมการเข้าถึงทางกายภาพ"),
 fields=[
  ("Date", "วันที่", "Date of visit.", "วันที่เข้า", ""),
  ("Visitor name and company", "ชื่อผู้มาติดต่อและบริษัท", "As on ID.", "ตามบัตรประจำตัว", ""),
  ("ID checked (type, last 4 digits)", "ตรวจบัตรประจำตัว (ประเภท เลข 4 หลักท้าย)", "Do not record full ID numbers.", "ห้ามบันทึกเลขบัตรเต็ม", ""),
  ("Area and purpose", "พื้นที่และวัตถุประสงค์", "Room and reason.", "ห้องและเหตุผล", ""),
  ("Escort name", "ชื่อผู้นำพา", "Authorized staff.", "บุคลากรที่มีสิทธิ์", ""),
  ("Time in and out", "เวลาเข้าและออก", "Times.", "เวลา", ""),
  ("Badge number", "หมายเลขบัตร", "Temporary badge.", "บัตรชั่วคราว", ""),
  ("Equipment brought in or out", "อุปกรณ์ที่นำเข้าหรือออก", "Laptops, media.", "โน้ตบุ๊ก สื่อบันทึกข้อมูล", ""),
 ],
 cmc_vals=["15 September 2026", "PACS Vendor B engineer (name withheld in sample)", "Passport, last 4 digits recorded", "Riverside data center; PACS storage upgrade (CHG-2026-0612)",
           "Senior System Administrator", "08:10 to 11:45", "V-DC-03", "One vendor laptop in and out; no media left"],
 approvals=["Reviewer", "FAC"],
 bp=[("Record only the last four digits of ID numbers, consistent with data minimization under the PDPA.", "บันทึกเฉพาะเลข 4 หลักท้ายของบัตรประจำตัว ให้สอดคล้องกับหลักการเก็บข้อมูลเท่าที่จำเป็นตาม PDPA")],
 mistakes=[("Copying full ID cards of every visitor and storing them indefinitely.", "ถ่ายสำเนาบัตรประชาชนของผู้มาติดต่อทุกคนและเก็บไว้โดยไม่มีกำหนด")],
)
