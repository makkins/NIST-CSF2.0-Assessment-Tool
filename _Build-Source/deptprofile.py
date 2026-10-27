# -*- coding: utf-8 -*-
"""Department user interviews (session S2C) for the Interview Assessment.
One row per department. Standard questions U1 to U8 use drop-down answers with a rating (G Good, W Weak, P Poor, U Unknown, X not applicable),
the same scale as the System Profile. U9 holds custom questions that the assessor adds per engagement.
The main value is the cross-check: department answers are compared with the IT answers in the System and Environment profiles,
and every disagreement becomes a conflict the Gap Analysis can cite (evidence ID DEPT:<department> or <field>:<department>).
Pairs are (EN, TH). Thai text is a working translation."""

UNK = ["unk", "U", "Unknown", "ไม่ทราบ"]

def F(id, typ, n, ask, feeds, block, opts=()):
    return dict(id=id, type=typ, n=n, ask=ask, s=feeds.split(), block=block.split(),
                o=[dict(c=c, r=r, n=[en, th]) for c, r, en, th in opts])

DEPT_FIELDS = [
 F("U1", "sys", ["Systems used", "ระบบที่ใช้งาน"], ["Which systems do you use to do your work, including any tool or app the IT team did not provide?", "ใช้ระบบใดในการทำงานบ้าง รวมถึงเครื่องมือหรือแอปที่ IT ไม่ได้จัดให้"],
   "ID.AM-01 ID.AM-02", "B3"),
 F("U2", "sel", ["Login and password sharing", "การล็อกอินและการใช้รหัสผ่านร่วมกัน"], ["How do you log in, and does anyone share an account or a password?", "ล็อกอินอย่างไร มีการใช้บัญชีหรือรหัสผ่านร่วมกันหรือไม่"],
   "PR.AA-01 PR.AA-05", "B5",
   [["own", "G", "Each person uses a named account", "ทุกคนใช้บัญชีของตนเอง"], ["some", "W", "Named accounts, but passwords are shared sometimes", "มีบัญชีของตนเอง แต่บางครั้งบอกรหัสผ่านกัน"],
    ["shared", "P", "Shared account for the team or shift", "ใช้บัญชีร่วมกันทั้งทีมหรือทั้งกะ"], UNK]),
 F("U3", "sel", ["Shared workstations", "เครื่องที่ใช้ร่วมกัน"], ["Do several people work on one computer that stays logged in?", "มีหลายคนใช้เครื่องเดียวกันโดยล็อกอินค้างไว้หรือไม่"],
   "PR.AA-01", "B5",
   [["no", "G", "Each person logs in and locks the screen", "แต่ละคนล็อกอินเองและล็อกหน้าจอ"], ["switch", "W", "Shared computer, users switch accounts", "ใช้เครื่องร่วมกัน แต่สลับบัญชีผู้ใช้"],
    ["stay", "P", "Shared computer stays logged in all shift", "ใช้เครื่องร่วมกันโดยล็อกอินค้างไว้ทั้งกะ"], UNK]),
 F("U4", "multi", ["Personal channels for work data", "ช่องทางส่วนตัวสำหรับข้อมูลงาน"], ["Do you send or keep work files through personal apps or devices?", "ส่งหรือเก็บไฟล์งานผ่านแอปหรืออุปกรณ์ส่วนตัวหรือไม่"],
   "PR.DS-01 PR.DS-10", "B8",
   [["line", "P", "Personal LINE or other chat app", "LINE หรือแชตส่วนตัว"], ["mail", "P", "Personal email", "อีเมลส่วนตัว"], ["cloud", "P", "Personal cloud storage", "คลาวด์ส่วนตัว"],
    ["usb", "W", "USB drive", "USB drive"], ["phone", "W", "Photos on personal phones", "ถ่ายภาพด้วยโทรศัพท์ส่วนตัว"], ["none", "G", "None", "ไม่มี"]]),
 F("U5", "sel", ["Working from outside", "การทำงานจากภายนอก"], ["How do you work from home or another site?", "ทำงานจากบ้านหรือนอกสถานที่อย่างไร"],
   "PR.AA-03 PR.IR-01", "B4",
   [["none", "X", "No remote work", "ไม่ได้ทำงานจากภายนอก"], ["vpnm", "G", "Company VPN with a second factor", "VPN ขององค์กรพร้อมปัจจัยที่สอง"], ["vpn", "W", "Company VPN with password only", "VPN ขององค์กรด้วยรหัสผ่านอย่างเดียว"],
    ["tool", "P", "Remote access tool or personal device", "โปรแกรมรีโมตหรืออุปกรณ์ส่วนตัว"], UNK]),
 F("U6", "sel", ["Security training", "การอบรมด้านความมั่นคงปลอดภัย"], ["When did you last receive security awareness training?", "ได้รับการอบรมด้านความมั่นคงปลอดภัยครั้งล่าสุดเมื่อใด"],
   "PR.AT-01", "B9",
   [["12m", "G", "Within 12 months", "ภายใน 12 เดือน"], ["old", "W", "More than 12 months ago", "เกิน 12 เดือน"], ["never", "P", "Never", "ไม่เคย"], UNK]),
 F("U7", "sel", ["Reporting a suspicious event", "การแจ้งเหตุที่น่าสงสัย"], ["If you receive a strange email or your computer behaves oddly, whom do you tell?", "หากได้รับอีเมลแปลกหรือเครื่องทำงานผิดปกติ จะแจ้งใคร"],
   "DE.AE-02 RS.MA-01", "B12",
   [["named", "G", "Names the reporting channel", "ระบุช่องทางแจ้งได้ถูกต้อง"], ["it", "W", "Would tell IT informally", "จะบอก IT แบบไม่เป็นทางการ"], ["dk", "P", "Does not know", "ไม่ทราบ"]]),
 F("U8", "sel", ["Work during a system outage", "การทำงานเมื่อระบบล่ม"], ["If your main system stops, how do you keep working?", "หากระบบหลักหยุดทำงาน จะทำงานต่ออย่างไร"],
   "RC.RP-02 ID.AM-05", "B2",
   [["doc", "G", "Written manual procedure, practiced", "มีขั้นตอนทำงานด้วยมือที่เขียนไว้และเคยซ้อม"], ["inf", "W", "Informal workaround", "มีวิธีทำงานแทนแบบไม่เป็นทางการ"],
    ["stop", "P", "Work stops", "งานหยุด"], UNK]),
]

if __name__ == "__main__":
    print(len(DEPT_FIELDS), "department fields")
