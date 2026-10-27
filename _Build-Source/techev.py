# -*- coding: utf-8 -*-
"""Standard technical evidence for the initial request list (Information Gathering spec v2.0 Section 11.1).
Each item: id, owner role key, linked technical checks, title (EN, TH). An item shows when at least one linked check is active."""

TECHEV = [
 ("TE-01", "ITM", "AST-01 OT-01", "Hardware asset inventory export, including OT and medical devices", "รายการทรัพย์สินฮาร์ดแวร์ที่ส่งออกจากระบบ รวมอุปกรณ์ OT และอุปกรณ์การแพทย์"),
 ("TE-02", "ITM", "AST-03 VUL-05", "Software inventory with versions and vendor support status", "รายการซอฟต์แวร์พร้อมเวอร์ชันและสถานะการสนับสนุนจากผู้ขาย"),
 ("TE-03", "ITM", "AST-06", "List of internet-facing domains, public IP addresses, and certificates", "รายการโดเมน IP สาธารณะ และใบรับรองที่เปิดสู่อินเทอร์เน็ต"),
 ("TE-04", "ITM", "AST-05", "Current network diagram and data flow diagram", "แผนภาพเครือข่ายและแผนภาพการไหลของข้อมูลฉบับปัจจุบัน"),
 ("TE-05", "ITM", "IAM-03 CLD-04", "Membership export of domain, global, and other administrator groups", "รายชื่อสมาชิกกลุ่มผู้ดูแลระบบระดับโดเมน global admin และกลุ่มสิทธิ์สูงอื่น"),
 ("TE-06", "ITM", "IAM-01", "MFA enrollment and enforcement report", "รายงานการลงทะเบียนและการบังคับใช้ MFA"),
 ("TE-07", "ITM", "IAM-02", "List of enabled accounts not used in the last 90 days", "รายการบัญชีที่ยังเปิดใช้แต่ไม่ได้ใช้งานในช่วง 90 วันที่ผ่านมา"),
 ("TE-08", "SYSOWN", "IAM-05", "Latest user access review record for one critical system", "บันทึกการทบทวนสิทธิ์ผู้ใช้ครั้งล่าสุดของระบบสำคัญหนึ่งระบบ"),
 ("TE-09", "ITM", "IAM-06", "Service account and shared account list with owners", "รายการบัญชีบริการและบัญชีใช้ร่วมพร้อมเจ้าของ"),
 ("TE-10", "ITM", "EP-01", "EDR or antivirus coverage report for endpoints and servers", "รายงานความครอบคลุมของ EDR หรือ Antivirus บนเครื่องลูกข่ายและเซิร์ฟเวอร์"),
 ("TE-11", "ITM", "EP-05 EP-07", "Disk encryption and mobile device management compliance report", "รายงานการเข้ารหัสดิสก์และการปฏิบัติตามนโยบาย MDM"),
 ("TE-12", "ITM", "NET-02", "Firewall rule set summary and the last rule review record", "สรุปกฎไฟร์วอลล์และบันทึกการทบทวนกฎครั้งล่าสุด"),
 ("TE-13", "ITM", "NET-03 SUP-01", "Remote access user list, including vendor accounts", "รายชื่อผู้ใช้การเข้าถึงระยะไกล รวมบัญชีของผู้ขาย"),
 ("TE-14", "ITM", "EML-01", "Email domain SPF, DKIM, and DMARC records", "ค่า SPF, DKIM และ DMARC ของโดเมนอีเมล"),
 ("TE-15", "ITM", "BKP-04", "Backup job report for the last 30 days", "รายงานงานสำรองข้อมูลย้อนหลัง 30 วัน"),
 ("TE-16", "ITM", "BKP-03", "Latest restore test record for a critical system", "บันทึกการทดสอบกู้คืนครั้งล่าสุดของระบบสำคัญ"),
 ("TE-17", "ITM", "VUL-01", "Latest internal and external vulnerability scan summary", "สรุปผลการสแกนช่องโหว่ภายในและภายนอกครั้งล่าสุด"),
 ("TE-18", "ITM", "VUL-02", "Patch compliance report by severity", "รายงานการติดตั้งแพตช์แยกตามระดับความรุนแรง"),
 ("TE-19", "CISO", "VUL-03", "Latest penetration test report and remediation status", "รายงานการทดสอบเจาะระบบครั้งล่าสุดและสถานะการแก้ไข"),
 ("TE-20", "SOC", "LOG-01 LOG-02", "List of log sources sent to central logging or SIEM, with retention", "รายการแหล่งล็อกที่ส่งเข้าระบบส่วนกลางหรือ SIEM พร้อมระยะเวลาเก็บรักษา"),
 ("TE-21", "SOC", "LOG-04 LOG-05", "Sample of security alerts from the last month and how they were handled", "ตัวอย่างการแจ้งเตือนด้านความมั่นคงปลอดภัยในเดือนที่ผ่านมาและการจัดการ"),
 ("TE-22", "ITM", "CLD-01 CLD-02", "Cloud tenant security score or benchmark report (for example Microsoft Secure Score)", "คะแนนหรือรายงานเทียบมาตรฐานความมั่นคงปลอดภัยของคลาวด์ (เช่น Microsoft Secure Score)"),
 ("TE-23", "CISO", "IR-04", "Latest incident response exercise or post-incident review report", "รายงานการฝึกซ้อมรับมือเหตุการณ์หรือการทบทวนหลังเหตุการณ์ครั้งล่าสุด"),
 ("TE-24", "FAC", "PHY-01", "Server room access list and the last access review", "รายชื่อผู้มีสิทธิ์เข้าห้องเซิร์ฟเวอร์และการทบทวนครั้งล่าสุด"),
 ("TE-25", "DEV", "APP-02", "Latest application security test or code scan summary", "สรุปผลการทดสอบความมั่นคงปลอดภัยของแอปพลิเคชันหรือการสแกนโค้ดครั้งล่าสุด"),
]
TECHEV = [dict(id=a, r=b, tcs=c.split(), n=[d, e]) for a, b, c, d, e in TECHEV]
