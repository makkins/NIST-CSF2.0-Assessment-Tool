# -*- coding: utf-8 -*-
"""AI prompts P-01 to P-05 for Claude (Information Gathering spec v2.0 Section 11.5).
The tool fills {{fields}}, replaces names with aliases (except P-01, which uses public information only),
leaves restricted evidence out, and imports the JSON reply after the assessor accepts each item.
Prompt bodies are in English because the JSON contract is in English; notes and documents may be in Thai."""

RULES = """Rules:
- Use only the information given below. Do not invent facts, names, dates, or numbers.
- Where the information is missing, leave the field empty or write "unknown".
- Reply with one JSON object only, no other text, exactly in the schema shown."""

PROMPTS = [
 dict(id="P-01", imp="csf-ig-pre/1", n=["Client pre-research", "ค้นข้อมูลลูกค้าก่อนเริ่มงาน"],
  d=["Public information only. Suggests Setup facts, regulatory flags, and likely systems.", "ใช้ข้อมูลสาธารณะเท่านั้น เสนอข้อมูลใน Setup ข้อกำหนดตามกฎหมาย และระบบที่น่าจะมี"],
  body="""You help a cybersecurity consultant prepare a NIST CSF 2.0 assessment in Thailand.
Research the organization below using public sources only (company website, annual report, Form 56-1 One Report, regulator lists, news).

Organization: {{client}}
Industry pack chosen by the consultant: {{industry}}

Find, with a source URL for each item:
1. Approximate number of employees, number of sites, and whether it runs operational technology or medical devices.
2. Whether it is likely designated Critical Information Infrastructure (CII) under the Cybersecurity Act B.E. 2562, which regulator supervises it (for example Bank of Thailand, SEC, OIC), and whether it processes sensitive personal data under the PDPA.
3. Business systems it publicly mentions (for example ERP, core banking, hospital information system, e-commerce platform).
4. Public cybersecurity incidents in the last three years.

{{rules}}

Schema:
{"schema":"csf-ig-pre/1","facts":{"emp":0,"sites":0,"ot":false},"flags":{"cii":false,"pdpa":true,"iso":false},"industry":"gen|hc|mfg|fin|hosp|util|pub","systems":[{"name":"","svc":"","source":""}],"incidents":[{"date":"","summary":"","source":""}],"notes":""}"""),
 dict(id="P-02", imp="csf-ig-notes/1", n=["Interview notes to statements", "แปลงบันทึกสัมภาษณ์เป็นคำบอกเล่า"],
  d=["Turns raw notes or a transcript of one session into statements, document requests, observations, and follow-ups.", "แปลงบันทึกหรือบทถอดเสียงของหนึ่งรอบสัมภาษณ์เป็นคำบอกเล่า รายการขอเอกสาร ข้อสังเกต และคำถามติดตาม"],
  body="""You help a cybersecurity consultant record an interview for a NIST CSF 2.0 assessment.
Session: {{session}}
People in the session (aliases): {{people}}

Subcategories covered in this session (ID: outcome | main question):
{{subs}}

For each Subcategory the notes address, record what each person said, and the answer in one word:
Y = the practice exists, P = partly, N = does not exist, U = unknown or unclear.
Also list documents the people mentioned, evidence to request, technical weaknesses observed, and questions to follow up.
Keep statements short and factual. Do not rate maturity.

{{rules}}

Schema:
{"schema":"csf-ig-notes/1","session":"{{sessionId}}","items":[{"sub":"PR.AA-01","person":"Person 1","stance":"Y|P|N|U","statement":"","docs":[""],"requests":[""]}],"observations":[{"system":"","description":"","severity":"C|H|M|L"}],"followups":[{"person":"","question":""}]}

Notes:
[PASTE THE INTERVIEW NOTES OR TRANSCRIPT HERE]"""),
 dict(id="P-03", imp="csf-ig-docrev/1", n=["Document review assist", "ช่วยตรวจเอกสาร"],
  d=["Checks one client document against the Register checks for the chosen review depth, with quoted support.", "ตรวจเอกสารของลูกค้าหนึ่งฉบับกับรายการตรวจตามระดับการตรวจ พร้อมข้อความอ้างอิง"],
  body="""You help a cybersecurity consultant review a client document.
Reference document type: {{doc}}
Review depth: {{depth}}

Checks (ID: requirement):
{{checks}}

For each check, answer P (pass), F (fail), or NA (not applicable), and quote the sentence from the client document that supports the answer. If no sentence supports a pass, answer F.
Then suggest an overall status: Exists (all pass), Partial (some pass), or Missing (none pass).

{{rules}}

Schema:
{"schema":"csf-ig-docrev/1","doc":"{{docId}}","checks":[{"id":"ctl-owner","result":"P|F|NA","quote":""}],"status":"Exists|Partial|Missing","note":""}

Client document text:
[PASTE THE DOCUMENT TEXT HERE]"""),
 dict(id="P-04", imp="", n=["Follow-up questions", "คำถามติดตาม"],
  d=["Drafts follow-up questions per interviewee from conflicts, unknown answers, and open requests. No import.", "ร่างคำถามติดตามรายผู้ให้สัมภาษณ์จากข้อมูลที่ขัดกัน คำตอบที่ไม่ทราบ และรายการที่ค้าง ไม่มีการนำเข้า"],
  body="""You help a cybersecurity consultant close open points before the evidence cut-off.
Draft short, neutral follow-up questions, grouped by person or role. Ask for evidence where a document or screen would settle the point.

Conflicting answers:
{{conflicts}}

Unknown answers:
{{unknowns}}

Open requests:
{{openReq}}

Reply as a plain list grouped by person or role. Do not add facts that are not given above."""),
 dict(id="P-05", imp="csf-ig-land/1", n=["Landscape facts draft", "ร่างข้อเท็จจริงสภาพปัจจุบัน"],
  d=["Drafts short current-state facts with Evidence IDs from the recorded state. Facts only, no judgment.", "ร่างข้อเท็จจริงสภาพปัจจุบันแบบสั้นพร้อม Evidence ID จากข้อมูลที่บันทึก เฉพาะข้อเท็จจริง ไม่ประเมิน"],
  body="""You help a cybersecurity consultant write the current IT landscape for a NIST CSF 2.0 assessment.
From the recorded state below, write 10 to 20 short facts about how things work today: systems and their criticality, identity and access, backup and recovery, monitoring, suppliers, technology in place, incidents, and changes in flight.
Each fact must be one sentence, factual, with no judgment or recommendation, and must cite the Evidence IDs or record IDs it comes from.

Recorded state:
{{state}}

{{rules}}

Schema:
{"schema":"csf-ig-land/1","facts":[{"block":"Systems|Identity|Backup|Monitoring|Suppliers|Tools|Incidents|Changes|Other","text":"","ev":["<Evidence ID or record ID>"]}]}"""),
]
