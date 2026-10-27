# -*- coding: utf-8 -*-
"""Email templates C1 to C8 for the Prepare stage (Information Gathering spec v2.0 Section 11.3).
Merge fields in double braces are filled by the tool from Setup and state:
{{client}} {{assessor}} {{ref}} {{scope}} {{cutoff}} {{reqDue}} {{saDue}} {{schedule}} {{requestSummary}}
{{session}} {{sessionDate}} {{sessionTime}} {{sessionLoc}} {{attendees}} {{objective}} {{duration}} {{prepare}}
{{facts}} {{newRequests}} {{openByOwner}} {{openCount}} {{landscape}}
A missing value prints as [PLACEHOLDER: ...] so the assessor sees what to fill before sending."""

COMMS = [
 dict(id="C1", when=["Before kickoff", "ก่อนประชุมเริ่มงาน"], n=["Kickoff and engagement confirmation", "ยืนยันการเริ่มงานและขอบเขต"], sess=False,
  subj=["Cybersecurity assessment {{ref}}: kickoff and next steps", "การประเมินความมั่นคงปลอดภัยไซเบอร์ {{ref}}: การเริ่มงานและขั้นตอนถัดไป"],
  body=["""Dear {{client}} team,

Thank you for confirming the cybersecurity assessment. This email confirms the scope, the plan, and what we need from you.

Scope: {{scope}}
Approach: interviews, document review, and technical checks aligned with the NIST Cybersecurity Framework (CSF) 2.0. We record how things work today. We do not test systems or change any settings.
Evidence cut-off date: {{cutoff}}. Evidence dated or received after this date will not count in the results.

Next steps:
1. We will send the initial document and evidence request list.
2. Please confirm the interview schedule below and the people for each session.

{{schedule}}

Please contact me with any questions.

Best regards,
{{assessor}}""",
"""เรียน ทีมงาน {{client}}

ขอบคุณที่ยืนยันการประเมินความมั่นคงปลอดภัยไซเบอร์ อีเมลนี้ยืนยันขอบเขต แผนงาน และสิ่งที่ต้องการจากท่าน

ขอบเขต: {{scope}}
วิธีการ: สัมภาษณ์ ตรวจเอกสาร และตรวจทางเทคนิค ตามกรอบ NIST Cybersecurity Framework (CSF) 2.0 โดยบันทึกสภาพการทำงานปัจจุบัน ไม่มีการทดสอบระบบหรือเปลี่ยนแปลงการตั้งค่าใด ๆ
วันตัดรอบหลักฐาน: {{cutoff}} หลักฐานที่ลงวันที่หรือได้รับหลังวันนี้จะไม่นำมาประกอบผลการประเมิน

ขั้นตอนถัดไป
1. ทีมงานจะส่งรายการขอเอกสารและหลักฐานเบื้องต้น
2. ขอให้ยืนยันตารางสัมภาษณ์ด้านล่าง และผู้เข้าร่วมของแต่ละรอบ

{{schedule}}

หากมีข้อสงสัย โปรดติดต่อได้ตลอดเวลา

ขอแสดงความนับถือ
{{assessor}}"""]),
 dict(id="C2", when=["With C1 or right after", "พร้อม C1 หรือหลังจากนั้นทันที"], n=["Initial document and evidence request", "ขอเอกสารและหลักฐานเบื้องต้น"], sess=False,
  subj=["Cybersecurity assessment {{ref}}: initial document and evidence request", "การประเมินความมั่นคงปลอดภัยไซเบอร์ {{ref}}: ขอเอกสารและหลักฐานเบื้องต้น"],
  body=["""Dear {{client}} team,

Please find attached the initial request list. It groups each item by the role that usually holds it.

{{requestSummary}}

For each item, please mark whether you have it and add the file name. If a document does not exist, mark it "No". That is a valid answer; it helps us plan the interviews.
Please send the files by {{reqDue}}. Shared drive links are fine.

Best regards,
{{assessor}}""",
"""เรียน ทีมงาน {{client}}

ทีมงานได้แนบรายการขอเอกสารเบื้องต้น โดยจัดกลุ่มตามบทบาทที่มักเป็นผู้ดูแลเอกสารนั้น

{{requestSummary}}

ขอให้ระบุในแต่ละรายการว่ามีหรือไม่ พร้อมชื่อไฟล์ หากไม่มีเอกสารนั้น ให้ระบุว่า "ไม่มี" ซึ่งเป็นคำตอบที่ใช้ได้และช่วยในการวางแผนการสัมภาษณ์
ขอให้ส่งไฟล์ภายในวันที่ {{reqDue}} โดยส่งเป็นลิงก์ไดรฟ์ที่แชร์ได้

ขอแสดงความนับถือ
{{assessor}}"""]),
 dict(id="C3", when=["One week before each session", "หนึ่งสัปดาห์ก่อนแต่ละรอบ"], n=["Session invitation", "เชิญเข้าร่วมการสัมภาษณ์"], sess=True,
  subj=["Interview invitation: {{session}} on {{sessionDate}}", "เชิญเข้าร่วมการสัมภาษณ์: {{session}} วันที่ {{sessionDate}}"],
  body=["""Dear {{attendees}},

We would like to invite you to the following interview for the cybersecurity assessment.

Session: {{session}}
Date and time: {{sessionDate}}, {{sessionTime}}
Location: {{sessionLoc}}
Duration: {{duration}}
Purpose: {{objective}}

To prepare, please have these documents at hand if they exist:
{{prepare}}

No slides are needed. We will ask how things work today and may ask you to show a screen.

Best regards,
{{assessor}}""",
"""เรียน {{attendees}}

ขอเรียนเชิญเข้าร่วมการสัมภาษณ์สำหรับการประเมินความมั่นคงปลอดภัยไซเบอร์ ตามรายละเอียดต่อไปนี้

รอบ: {{session}}
วันและเวลา: {{sessionDate}} {{sessionTime}}
สถานที่: {{sessionLoc}}
ระยะเวลา: {{duration}}
วัตถุประสงค์: {{objective}}

เพื่อเตรียมความพร้อม ขอให้เตรียมเอกสารต่อไปนี้ (หากมี)
{{prepare}}

ไม่ต้องเตรียมสไลด์ ทีมงานจะสอบถามวิธีการทำงานปัจจุบัน และอาจขอให้แสดงหน้าจอระบบประกอบ

ขอแสดงความนับถือ
{{assessor}}"""]),
 dict(id="C4", when=["With the self-assessment Excel", "พร้อมไฟล์ Excel แบบประเมินตนเอง"], n=["Self-assessment cover note", "นำส่งแบบประเมินตนเอง"], sess=False,
  subj=["Cybersecurity assessment {{ref}}: self-assessment questionnaire", "การประเมินความมั่นคงปลอดภัยไซเบอร์ {{ref}}: แบบประเมินตนเอง"],
  body=["""Dear {{client}} team,

Please find attached the self-assessment questionnaire. It helps us focus the interviews on what matters most.

- Answer each question Yes, Partly, No, Unknown, or Not applicable, and add a short comment where useful.
- "Unknown" and "No" are acceptable answers. We check every answer in the interviews.
- Please do not add, delete, or rename sheets, rows, or columns.

Please return the file by {{saDue}}.

Best regards,
{{assessor}}""",
"""เรียน ทีมงาน {{client}}

ทีมงานได้แนบแบบประเมินตนเอง เพื่อช่วยให้การสัมภาษณ์มุ่งเน้นในประเด็นที่สำคัญที่สุด

- ตอบแต่ละข้อว่า ใช่ บางส่วน ไม่ใช่ ไม่ทราบ หรือไม่เกี่ยวข้อง และเพิ่มคำอธิบายสั้น ๆ ตามความเหมาะสม
- คำตอบ "ไม่ทราบ" และ "ไม่ใช่" เป็นคำตอบที่ใช้ได้ ทีมงานจะตรวจสอบทุกคำตอบในการสัมภาษณ์
- ขอให้ไม่เพิ่ม ลบ หรือเปลี่ยนชื่อชีต แถว หรือคอลัมน์

ขอให้ส่งไฟล์คืนภายในวันที่ {{saDue}}

ขอแสดงความนับถือ
{{assessor}}"""]),
 dict(id="C5", when=["Same day as the session", "วันเดียวกับการสัมภาษณ์"], n=["Session read-back and thank you", "สรุปผลการสัมภาษณ์และขอบคุณ"], sess=True,
  subj=["Summary of today's session: {{session}}", "สรุปการสัมภาษณ์วันนี้: {{session}}"],
  body=["""Dear {{attendees}},

Thank you for your time today. Below are the key facts we recorded. Please reply within two working days if anything is incorrect or missing.

Key facts:
{{facts}}

Documents and evidence requested in this session:
{{newRequests}}

Best regards,
{{assessor}}""",
"""เรียน {{attendees}}

ขอบคุณที่สละเวลาในวันนี้ ด้านล่างเป็นข้อเท็จจริงหลักที่ทีมงานบันทึกไว้ หากมีข้อมูลใดไม่ถูกต้องหรือขาดหายไป ขอให้แจ้งกลับภายใน 2 วันทำการ

ข้อเท็จจริงหลัก
{{facts}}

เอกสารและหลักฐานที่ขอในรอบนี้
{{newRequests}}

ขอแสดงความนับถือ
{{assessor}}"""]),
 dict(id="C6", when=["Weekly", "ทุกสัปดาห์"], n=["Outstanding evidence reminder", "แจ้งเตือนเอกสารที่ยังค้าง"], sess=False,
  subj=["Reminder: outstanding documents for the cybersecurity assessment {{ref}}", "แจ้งเตือน: เอกสารที่ยังค้างสำหรับการประเมินความมั่นคงปลอดภัยไซเบอร์ {{ref}}"],
  body=["""Dear {{client}} team,

The following items are still open. Please send them, or tell us they do not exist, before the evidence cut-off date of {{cutoff}}.

{{openByOwner}}

Best regards,
{{assessor}}""",
"""เรียน ทีมงาน {{client}}

รายการต่อไปนี้ยังค้างอยู่ ขอให้ส่งเอกสาร หรือแจ้งว่าไม่มีเอกสารนั้น ก่อนวันตัดรอบหลักฐาน {{cutoff}}

{{openByOwner}}

ขอแสดงความนับถือ
{{assessor}}"""]),
 dict(id="C7", when=["One week before the cut-off", "หนึ่งสัปดาห์ก่อนวันตัดรอบ"], n=["Evidence cut-off notice", "แจ้งวันตัดรอบหลักฐาน"], sess=False,
  subj=["Evidence cut-off on {{cutoff}}", "วันตัดรอบหลักฐาน {{cutoff}}"],
  body=["""Dear {{client}} team,

The evidence cut-off date is {{cutoff}}. {{openCount}} items are still open. Items not received by that date will be reported as not provided, and the related practices will be rated on interview statements only.

{{openByOwner}}

Best regards,
{{assessor}}""",
"""เรียน ทีมงาน {{client}}

วันตัดรอบหลักฐานคือ {{cutoff}} ขณะนี้ยังมี {{openCount}} รายการที่ค้างอยู่ รายการที่ไม่ได้รับภายในวันดังกล่าวจะรายงานว่าไม่ได้รับ และการปฏิบัติที่เกี่ยวข้องจะประเมินจากคำบอกเล่าในการสัมภาษณ์เท่านั้น

{{openByOwner}}

ขอแสดงความนับถือ
{{assessor}}"""]),
 dict(id="C8", when=["End of information gathering", "เมื่อเก็บข้อมูลเสร็จ"], n=["Fact validation and close of information gathering", "ยืนยันข้อเท็จจริงและปิดการเก็บข้อมูล"], sess=False,
  subj=["Cybersecurity assessment {{ref}}: please confirm the current-state facts", "การประเมินความมั่นคงปลอดภัยไซเบอร์ {{ref}}: ขอยืนยันข้อเท็จจริงสภาพปัจจุบัน"],
  body=["""Dear {{client}} team,

Fieldwork is complete. Below is the summary of how things work today, based on the interviews, documents, and technical checks. Please confirm these facts, or tell us what is incorrect, within five working days. We will then start the gap analysis.

{{landscape}}

Best regards,
{{assessor}}""",
"""เรียน ทีมงาน {{client}}

การเก็บข้อมูลภาคสนามเสร็จสิ้นแล้ว ด้านล่างเป็นสรุปสภาพการทำงานปัจจุบันจากการสัมภาษณ์ เอกสาร และการตรวจทางเทคนิค ขอให้ยืนยันข้อเท็จจริงเหล่านี้ หรือแจ้งรายการที่ไม่ถูกต้อง ภายใน 5 วันทำการ จากนั้นทีมงานจะเริ่มการวิเคราะห์ช่องว่าง

{{landscape}}

ขอแสดงความนับถือ
{{assessor}}"""]),
]
