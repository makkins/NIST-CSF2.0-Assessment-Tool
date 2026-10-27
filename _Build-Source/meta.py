# -*- coding: utf-8 -*-
from dictionary import TYPES, TIERS, PPT, LEVEL_TH, TRIGGER_TH
"""Master metadata: roles, CSF catalog, document list."""

ROLES = {
 # key: (Template EN, Template TH, CMC EN)
 "BOARD": ("Board of Directors", "คณะกรรมการบริษัท", "CMC Board of Directors"),
 "AC":    ("Audit Committee", "คณะกรรมการตรวจสอบ", "CMC Audit Committee"),
 "CEO":   ("Chief Executive Officer (CEO)", "ประธานเจ้าหน้าที่บริหาร (CEO)", "Chief Executive Officer (CEO)"),
 "CFO":   ("Chief Financial Officer (CFO)", "ประธานเจ้าหน้าที่บริหารด้านการเงิน (CFO)", "Chief Financial Officer (CFO)"),
 "CIO":   ("Chief Information Officer (CIO)", "ประธานเจ้าหน้าที่บริหารด้านสารสนเทศ (CIO)", "Chief Information Officer (CIO)"),
 "CISO":  ("Chief Information Security Officer (CISO) or Security Manager", "ผู้บริหารด้านความมั่นคงปลอดภัยสารสนเทศ (CISO) หรือ Security Manager", "Security Manager"),
 "ISSC":  ("Information Security Steering Committee (ISSC)", "คณะกรรมการกำกับดูแลความมั่นคงปลอดภัยสารสนเทศ (ISSC)", "Information Security Steering Committee (ISSC)"),
 "DPO":   ("Data Protection Officer (DPO)", "เจ้าหน้าที่คุ้มครองข้อมูลส่วนบุคคล (DPO)", "Data Protection Officer (DPO)"),
 "ITM":   ("IT Infrastructure Manager", "ผู้จัดการฝ่ายโครงสร้างพื้นฐาน IT", "IT Infrastructure Manager"),
 "HR":    ("Human Resources Director", "ผู้อำนวยการฝ่ายทรัพยากรบุคคล", "Human Resources Director"),
 "LEGAL": ("Legal Counsel", "ที่ปรึกษากฎหมาย", "Legal Counsel"),
 "PROC":  ("Procurement Manager", "ผู้จัดการฝ่ายจัดซื้อ", "Procurement Manager"),
 "IA":    ("Head of Internal Audit", "หัวหน้าฝ่ายตรวจสอบภายใน", "Internal Audit Manager"),
 "BCM":   ("Business Continuity Management (BCM) Coordinator", "ผู้ประสานงานการบริหารความต่อเนื่องทางธุรกิจ (BCM)", "BCM Coordinator, Quality and Risk Management Department"),
 "SOC":   ("Security Operations Center (SOC) Lead", "หัวหน้าศูนย์ปฏิบัติการความมั่นคงปลอดภัย (SOC)", "SOC Lead (MSSP service manager with Security Manager oversight)"),
 "RISK":  ("Risk Owner", "เจ้าของความเสี่ยง", "Risk Owner (department head)"),
 "SYSOWN":("System Owner", "เจ้าของระบบ", "System Owner"),
 "DEV":   ("Head of Application Development", "หัวหน้าฝ่ายพัฒนาระบบงาน", "Application Manager"),
 "FAC":   ("Facilities Manager", "ผู้จัดการฝ่ายอาคารสถานที่", "Facilities and Engineering Manager"),
 "COMMS": ("Corporate Communications Manager", "ผู้จัดการฝ่ายสื่อสารองค์กร", "Corporate Communications Manager"),
 "CRO":   ("Chief Risk Officer (CRO) or Enterprise Risk Manager", "ผู้บริหารด้านความเสี่ยง (CRO) หรือผู้จัดการความเสี่ยงองค์กร", "Quality and Risk Management Director"),
}

# Placeholder replacement for the CMC set (applied to Template EN text)
CMC_REPLACE = [
 ("[Organization Name]", "Chaophraya Medical Center (CMC)"),
 ("[Organization]", "CMC"),
 ("[Sector Regulator]", "the Ministry of Public Health (as CII regulator for the public health sector) [VERIFY]"),
 ("[Critical Services]", "inpatient care, emergency care, outpatient services, diagnostic imaging, and laboratory services"),
 ("[Critical Systems]", "HIS, PACS, LIS, ERP, and Microsoft 365"),
]

FUNCTIONS = {
 "GV": ("Govern", "กำกับดูแล"), "ID": ("Identify", "ระบุ"), "PR": ("Protect", "ป้องกัน"),
 "DE": ("Detect", "ตรวจจับ"), "RS": ("Respond", "ตอบสนอง"), "RC": ("Recover", "กู้คืน"),
}

CATEGORIES = {
 "GV.OC": ("Organizational Context", "บริบทขององค์กร"),
 "GV.RM": ("Risk Management Strategy", "กลยุทธ์การบริหารความเสี่ยง"),
 "GV.RR": ("Roles, Responsibilities, and Authorities", "บทบาท ความรับผิดชอบ และอำนาจหน้าที่"),
 "GV.PO": ("Policy", "นโยบาย"),
 "GV.OV": ("Oversight", "การกำกับติดตาม"),
 "GV.SC": ("Cybersecurity Supply Chain Risk Management", "การบริหารความเสี่ยงห่วงโซ่อุปทานด้านไซเบอร์"),
 "ID.AM": ("Asset Management", "การบริหารจัดการทรัพย์สิน"),
 "ID.RA": ("Risk Assessment", "การประเมินความเสี่ยง"),
 "ID.IM": ("Improvement", "การปรับปรุง"),
 "PR.AA": ("Identity Management, Authentication, and Access Control", "การบริหารตัวตน การยืนยันตัวตน และการควบคุมการเข้าถึง"),
 "PR.AT": ("Awareness and Training", "การสร้างความตระหนักรู้และการฝึกอบรม"),
 "PR.DS": ("Data Security", "ความมั่นคงปลอดภัยของข้อมูล"),
 "PR.PS": ("Platform Security", "ความมั่นคงปลอดภัยของแพลตฟอร์ม"),
 "PR.IR": ("Technology Infrastructure Resilience", "ความยืดหยุ่นของโครงสร้างพื้นฐานเทคโนโลยี"),
 "DE.CM": ("Continuous Monitoring", "การเฝ้าระวังอย่างต่อเนื่อง"),
 "DE.AE": ("Adverse Event Analysis", "การวิเคราะห์เหตุการณ์ไม่พึงประสงค์"),
 "RS.MA": ("Incident Management", "การบริหารจัดการเหตุการณ์"),
 "RS.AN": ("Incident Analysis", "การวิเคราะห์เหตุการณ์"),
 "RS.CO": ("Incident Response Reporting and Communication", "การรายงานและการสื่อสารระหว่างรับมือเหตุการณ์"),
 "RS.MI": ("Incident Mitigation", "การลดผลกระทบของเหตุการณ์"),
 "RC.RP": ("Incident Recovery Plan Execution", "การดำเนินการตามแผนกู้คืน"),
 "RC.CO": ("Incident Recovery Communication", "การสื่อสารระหว่างการกู้คืน"),
}

SUBCATS = {
 "GV.OC-01": "Organizational mission is understood and informs cybersecurity risk management",
 "GV.OC-02": "Internal and external stakeholders and their cybersecurity expectations are understood",
 "GV.OC-03": "Legal, regulatory, and contractual cybersecurity requirements are understood and managed",
 "GV.OC-04": "Critical objectives, capabilities, and services that external stakeholders depend on are understood",
 "GV.OC-05": "Outcomes, capabilities, and services that the organization depends on are understood",
 "GV.RM-01": "Risk management objectives are established and agreed to by stakeholders",
 "GV.RM-02": "Risk appetite and risk tolerance statements are established, communicated, and maintained",
 "GV.RM-03": "Cybersecurity risk management is included in enterprise risk management processes",
 "GV.RM-04": "Strategic direction for appropriate risk response options is established and communicated",
 "GV.RM-05": "Lines of communication for cybersecurity risks, including supplier risks, are established",
 "GV.RM-06": "A standardized method for calculating, documenting, categorizing, and prioritizing risks is established",
 "GV.RM-07": "Strategic opportunities (positive risks) are characterized and included in discussions",
 "GV.RR-01": "Leadership is responsible and accountable for cybersecurity risk and fosters a risk-aware culture",
 "GV.RR-02": "Cybersecurity roles, responsibilities, and authorities are established, communicated, and enforced",
 "GV.RR-03": "Adequate resources are allocated commensurate with risk strategy, roles, and policies",
 "GV.RR-04": "Cybersecurity is included in human resources practices",
 "GV.PO-01": "Cybersecurity policy is established, communicated, and enforced based on context, strategy, and priorities",
 "GV.PO-02": "Cybersecurity policy is reviewed, updated, communicated, and enforced to reflect changes",
 "GV.OV-01": "Risk management strategy outcomes are reviewed to inform and adjust strategy and direction",
 "GV.OV-02": "Risk management strategy is reviewed and adjusted to ensure coverage of requirements and risks",
 "GV.OV-03": "Risk management performance is evaluated and reviewed for adjustments needed",
 "GV.SC-01": "A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established",
 "GV.SC-02": "Cybersecurity roles for suppliers, customers, and partners are established and coordinated",
 "GV.SC-03": "Supply chain risk management is integrated into cybersecurity and enterprise risk management",
 "GV.SC-04": "Suppliers are known and prioritized by criticality",
 "GV.SC-05": "Requirements to address supply chain risks are established, prioritized, and integrated into contracts",
 "GV.SC-06": "Planning and due diligence are performed to reduce risks before entering supplier relationships",
 "GV.SC-07": "Supplier risks are understood, recorded, prioritized, assessed, responded to, and monitored",
 "GV.SC-08": "Relevant suppliers are included in incident planning, response, and recovery activities",
 "GV.SC-09": "Supply chain security practices are integrated and monitored throughout the technology product and service life cycle",
 "GV.SC-10": "Supply chain risk management plans include provisions for activities after a partnership or service ends",
 "ID.AM-01": "Inventories of hardware managed by the organization are maintained",
 "ID.AM-02": "Inventories of software, services, and systems managed by the organization are maintained",
 "ID.AM-03": "Representations of authorized network communication and data flows are maintained",
 "ID.AM-04": "Inventories of services provided by suppliers are maintained",
 "ID.AM-05": "Assets are prioritized based on classification, criticality, resources, and impact on the mission",
 "ID.AM-07": "Inventories of data and corresponding metadata for designated data types are maintained",
 "ID.AM-08": "Systems, hardware, software, services, and data are managed throughout their life cycles",
 "ID.RA-01": "Vulnerabilities in assets are identified, validated, and recorded",
 "ID.RA-02": "Cyber threat intelligence is received from information sharing forums and sources",
 "ID.RA-03": "Internal and external threats to the organization are identified and recorded",
 "ID.RA-04": "Potential impacts and likelihoods of threats exploiting vulnerabilities are identified and recorded",
 "ID.RA-05": "Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent risk and inform prioritization",
 "ID.RA-06": "Risk responses are chosen, prioritized, planned, tracked, and communicated",
 "ID.RA-07": "Changes and exceptions are managed, assessed for risk impact, recorded, and tracked",
 "ID.RA-08": "Processes for receiving, analyzing, and responding to vulnerability disclosures are established",
 "ID.RA-09": "The authenticity and integrity of hardware and software are assessed prior to acquisition and use",
 "ID.RA-10": "Critical suppliers are assessed prior to acquisition",
 "ID.IM-01": "Improvements are identified from evaluations",
 "ID.IM-02": "Improvements are identified from security tests and exercises",
 "ID.IM-03": "Improvements are identified from execution of operational processes, procedures, and activities",
 "ID.IM-04": "Incident response plans and other cybersecurity plans that affect operations are established, communicated, maintained, and improved",
 "PR.AA-01": "Identities and credentials for authorized users, services, and hardware are managed",
 "PR.AA-02": "Identities are proofed and bound to credentials based on the context of interactions",
 "PR.AA-03": "Users, services, and hardware are authenticated",
 "PR.AA-04": "Identity assertions are protected, conveyed, and verified",
 "PR.AA-05": "Access permissions, entitlements, and authorizations are defined, managed, enforced, and reviewed",
 "PR.AA-06": "Physical access to assets is managed, monitored, and enforced commensurate with risk",
 "PR.AT-01": "Personnel are provided with awareness and training for general tasks with cybersecurity risks in mind",
 "PR.AT-02": "Individuals in specialized roles are provided with awareness and training for those roles",
 "PR.DS-01": "The confidentiality, integrity, and availability of data-at-rest are protected",
 "PR.DS-02": "The confidentiality, integrity, and availability of data-in-transit are protected",
 "PR.DS-10": "The confidentiality, integrity, and availability of data-in-use are protected",
 "PR.DS-11": "Backups of data are created, protected, maintained, and tested",
 "PR.PS-01": "Configuration management practices are established and applied",
 "PR.PS-02": "Software is maintained, replaced, and removed commensurate with risk",
 "PR.PS-03": "Hardware is maintained, replaced, and removed commensurate with risk",
 "PR.PS-04": "Log records are generated and made available for continuous monitoring",
 "PR.PS-05": "Installation and execution of unauthorized software are prevented",
 "PR.PS-06": "Secure software development practices are integrated and their performance is monitored",
 "PR.IR-01": "Networks and environments are protected from unauthorized logical access and usage",
 "PR.IR-02": "Technology assets are protected from environmental threats",
 "PR.IR-03": "Mechanisms are implemented to achieve resilience requirements in normal and adverse situations",
 "PR.IR-04": "Adequate resource capacity to ensure availability is maintained",
 "DE.CM-01": "Networks and network services are monitored to find potentially adverse events",
 "DE.CM-02": "The physical environment is monitored to find potentially adverse events",
 "DE.CM-03": "Personnel activity and technology usage are monitored to find potentially adverse events",
 "DE.CM-06": "External service provider activities and services are monitored to find potentially adverse events",
 "DE.CM-09": "Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events",
 "DE.AE-02": "Potentially adverse events are analyzed to better understand associated activities",
 "DE.AE-03": "Information is correlated from multiple sources",
 "DE.AE-04": "The estimated impact and scope of adverse events are understood",
 "DE.AE-06": "Information on adverse events is provided to authorized staff and tools",
 "DE.AE-07": "Cyber threat intelligence and other contextual information are integrated into the analysis",
 "DE.AE-08": "Incidents are declared when adverse events meet the defined incident criteria",
 "RS.MA-01": "The incident response plan is executed in coordination with relevant third parties once an incident is declared",
 "RS.MA-02": "Incident reports are triaged and validated",
 "RS.MA-03": "Incidents are categorized and prioritized",
 "RS.MA-04": "Incidents are escalated or elevated as needed",
 "RS.MA-05": "The criteria for initiating incident recovery are applied",
 "RS.AN-03": "Analysis is performed to establish what has taken place during an incident and the root cause",
 "RS.AN-06": "Actions performed during an investigation are recorded and the records' integrity and provenance are preserved",
 "RS.AN-07": "Incident data and metadata are collected, and their integrity and provenance are preserved",
 "RS.AN-08": "An incident's magnitude is estimated and validated",
 "RS.CO-02": "Internal and external stakeholders are notified of incidents",
 "RS.CO-03": "Information is shared with designated internal and external stakeholders",
 "RS.MI-01": "Incidents are contained",
 "RS.MI-02": "Incidents are eradicated",
 "RC.RP-01": "The recovery portion of the incident response plan is executed once initiated",
 "RC.RP-02": "Recovery actions are selected, scoped, prioritized, and performed",
 "RC.RP-03": "The integrity of backups and other restoration assets is verified before using them for restoration",
 "RC.RP-04": "Critical mission functions and cybersecurity risk management are considered to establish post-incident operational norms",
 "RC.RP-05": "The integrity of restored assets is verified, systems and services are restored, and normal operating status is confirmed",
 "RC.RP-06": "The end of incident recovery is declared based on criteria, and incident-related documentation is completed",
 "RC.CO-03": "Recovery activities and progress in restoring operational capabilities are communicated to designated stakeholders",
 "RC.CO-04": "Public updates on incident recovery are shared using approved methods and messaging",
}





# CMC applicable triggers: PDPA yes, CII yes, CCA service provider yes (patient and guest Wi-Fi), ISO 27001 not yet certified (target 2027)
CMC_TRIGGERS = {"All", "PDPA", "CII", "CCA"}

# id | csf | parents | basis | ppt | iso | sp80053 | owner | approver | review   (id, titles, type, category, level, trigger, package, wave, track, cap live in register-ids.json)
DOCS_TABLE = r"""
GV-CHR-001|GV.OC-01,GV.RR-01,GV.OV-01|-|ISO/IEC 27001:2022 Clause 5.1 and 5.3; CSA s.44 (CII)|Governance|5.1,5.3,A.5.4|PM-1,PM-2,PM-29|CISO|BOARD|Annual
GV-STR-001|GV.OC-01,GV.RM-01,GV.OV-01|GV-CHR-001|ISO/IEC 27001:2022 Clause 6.2 (documented information on information security objectives; the roadmap section is common practice)|Governance|6.2|PM-1,PM-9|CISO|BOARD|Annual
GV-RPT-001|GV.OC-01,GV.OC-02,GV.OC-04,GV.OC-05|GV-CHR-001|ISO/IEC 27001:2022 Clause 4.3 (scope as documented information)|Governance|4.1,4.2,4.3|PM-11,PM-8|CISO|ISSC|Annual
GV-REG-001|GV.OC-03|GV-RPT-001|ISO/IEC 27001:2022 Annex A 5.31; PDPA; CSA|Governance|A.5.31,A.5.32,A.5.34|PM-1,PT-1|LEGAL|ISSC|Annual and on legal change
GV-REG-002|GV.OC-02|GV-RPT-001|ISO/IEC 27001:2022 Clause 4.2 (not mandated as documented information)|Governance|4.2|PM-11|CISO|ISSC|Annual
GV-STM-001|GV.RM-01,GV.RM-02,GV.RM-03|GV-CHR-001|NIST IR 8286; ISO/IEC 27001:2022 Clause 6.1.2(a) risk acceptance criteria|Governance|6.1.2|PM-9,PM-28|CRO|BOARD|Annual
GV-POL-002|GV.RM-01,GV.RM-03,GV.RM-04,GV.RM-05,GV.RM-07,GV.SC-03|GV-POL-001,GV-STM-001|ISO/IEC 27001:2022 Clause 6.1; CSA s.44 (CII)|Governance|6.1,8.2,8.3|RA-1,PM-9|CISO|CEO|Annual
GV-PRC-001|GV.RM-06,ID.RA-03,ID.RA-04,ID.RA-05,ID.RA-06|GV-POL-002|ISO/IEC 27001:2022 Clause 6.1.2 and 6.1.3 (documented process); CSA s.54|Process|6.1.2,6.1.3|RA-3,PM-9|CISO|ISSC|Annual
GV-FRM-001|GV.RM-04,ID.RA-06|GV-PRC-001|ISO/IEC 27001:2022 Clause 6.1.3(f) (risk owner approval of residual risk)|Process|6.1.3|RA-7,PM-9|CISO|RISK|Annual
GV-CHR-002|GV.RR-01,GV.OV-01,GV.OV-02|GV-CHR-001|ISO/IEC 27001:2022 Clause 5.1 and 5.3|Governance|5.1,5.3|PM-2,PM-29|CISO|CEO|Annual
GV-REG-003|GV.RR-01,GV.RR-02|GV-CHR-001|ISO/IEC 27001:2022 Clause 5.3 and Annex A 5.2; CSA s.46 and s.52 (CII contact officers)|People|5.3,A.5.2,A.5.3|PM-2,PS-9|CISO|CIO|Annual
GV-TPL-001|GV.RR-02,GV.RR-04|GV-REG-003|Common practice; NICE Workforce Framework (NIST SP 800-181 Rev. 1)|People|A.5.2|PS-9|HR|CIO|Annual
GV-PLN-001|GV.RR-03|GV-STR-001|ISO/IEC 27001:2022 Clause 7.1 (resources; not mandated as documented information)|Governance|7.1|PM-3|CISO|CFO|Annual
GV-STD-001|GV.RR-04,PR.AA-05|GV-POL-001|ISO/IEC 27001:2022 Annex A 6.1 to 6.5|People|A.6.1,A.6.2,A.6.4,A.6.5|PS-2,PS-3,PS-4,PS-5,PS-7,PS-8|HR|ISSC|Annual
GV-FRM-002|GV.RR-04,GV.SC-05|GV-STD-001|ISO/IEC 27001:2022 Annex A 6.6|People|A.6.6|PS-6|LEGAL|LEGAL|Annual
GV-FRM-003|GV.RR-04,PR.AA-05,ID.AM-08|GV-STD-001|ISO/IEC 27001:2022 Annex A 5.11 and 6.5|People|A.5.11,A.6.5|PS-4,PS-5|HR|HR|Annual
GV-POL-001|GV.PO-01,GV.PO-02|GV-CHR-001|ISO/IEC 27001:2022 Clause 5.2 (documented information); PDPC Notification on Security Measures B.E. 2565|Governance|5.2,A.5.1|PM-1,PL-1|CISO|CEO|Annual
GV-PRC-002|GV.PO-02|GV-POL-001|ISO/IEC 27001:2022 Clause 7.5 (control of documented information; a procedure is not mandated)|Process|7.5,A.5.37|PL-1,PM-1|CISO|CIO|Annual
GV-POL-003|GV.PO-01,PR.AT-01|GV-POL-001|ISO/IEC 27001:2022 Annex A 5.10, 6.7, and 7.7|People|A.5.10,A.6.7,A.7.7|PL-4|CISO|CEO|Annual
GV-POL-005|GV.PO-01,GV.OC-03,PR.DS-10|GV-POL-003|NIST AI RMF 1.0; NIST AI 600-1 (Generative AI Profile)|People|A.5.10|PL-4|CISO|CEO|Annual
GV-PRC-003|GV.PO-02,ID.RA-07|GV-POL-001|ISO/IEC 27001:2022 Annex A 5.36|Process|A.5.36|PL-1,RA-7|CISO|CIO|Annual
GV-FRM-004|ID.RA-07|GV-PRC-003|ISO/IEC 27001:2022 Annex A 5.36|Process|A.5.36|RA-7|CISO|CIO|Annual
GV-REG-004|ID.RA-07,GV.OV-02|GV-PRC-003|ISO/IEC 27001:2022 Annex A 5.36|Process|A.5.36|RA-7,PM-4|CISO|ISSC|Quarterly
GV-REG-005|GV.PO-01,GV.RM-06|GV-PRC-001|ISO/IEC 27001:2022 Clause 6.1.3(d)|Governance|6.1.3|PL-2|CISO|ISSC|Annual
GV-REG-006|GV.OC-03,GV.PO-01|GV-REG-001|CSA s.44; NCSC Notification on Code of Practice and Standard Framework B.E. 2564; CRC Notification on CII duties 2024 [VERIFY]|Governance|A.5.31|PM-1|CISO|ISSC|Annual
GV-POL-004|GV.OC-03,GV.PO-01|GV-POL-001|PDPA s.37(1); PDPC Notification on Security Measures B.E. 2565|Governance|A.5.34|PT-1|DPO|CEO|Annual
GV-REG-007|GV.OC-03,ID.AM-07|GV-POL-004|PDPA s.39 (controller) and s.40 (processor)|Process|A.5.34|PT-2,PT-3|DPO|DPO|Annual and on change
GV-TPL-002|GV.OC-03|GV-POL-004|PDPA s.23|Process|A.5.34|PT-5|DPO|LEGAL|Annual
GV-PRC-004|GV.OC-03,ID.RA-04|GV-POL-004|Not explicitly mandated by the PDPA; supports the risk-based measures in PDPA s.37(1) [VERIFY current PDPC guidance]|Process|A.5.34|RA-8|DPO|ISSC|Annual
GV-TPL-003|ID.RA-04|GV-PRC-004|Supports PDPA s.37(1)|Process|A.5.34|RA-8|DPO|DPO|Annual
GV-PRC-005|GV.OC-03|GV-POL-004|PDPA s.30 to s.36 (data subject rights; 30-day response under s.30)|Process|A.5.34|PT-1|DPO|ISSC|Annual
GV-FRM-005|GV.OC-03|GV-PRC-005|PDPA s.30 to s.36|Process|A.5.34|PT-1|DPO|DPO|Annual
GV-TPL-004|GV.SC-05,GV.OC-03|GV-POL-004,GV-STD-002|PDPA s.40; PDPC Notification on Security Measures B.E. 2565 (processor agreement)|Process|A.5.20,A.5.34|SA-9,PT-1|DPO|LEGAL|Annual
GV-PRC-006|GV.OV-01,GV.OV-02,GV.OV-03|GV-CHR-002|ISO/IEC 27001:2022 Clause 9.3|Governance|9.3|PM-6,PM-9|CISO|ISSC|Annual
GV-REC-001|GV.OV-01,GV.OV-02|GV-PRC-006|ISO/IEC 27001:2022 Clause 9.3.3 (results of management reviews)|Governance|9.3|PM-9|CISO|ISSC|Each meeting
GV-REG-008|GV.OV-03,ID.IM-01|GV-STR-001|ISO/IEC 27001:2022 Clause 9.1 (documented evidence of monitoring and measurement results; the catalog records definitions and results)|Governance|9.1|PM-6,CA-7|CISO|ISSC|Annual
GV-TPL-005|GV.OV-01,GV.OV-03|GV-REG-008|Common practice; NIST IR 8286 series|Governance|9.1,9.3|PM-6|CISO|CEO|Annual
GV-PRC-007|GV.OV-02,ID.IM-01|GV-CHR-001|ISO/IEC 27001:2022 Clause 9.2; CSA s.54|Governance|9.2,A.5.35|CA-2,CA-7|IA|AC|Annual
GV-PLN-002|GV.OV-02|GV-PRC-007|ISO/IEC 27001:2022 Clause 9.2.2 (audit program); CSA s.54 (annual audit)|Governance|9.2|CA-2|IA|AC|Annual
GV-TPL-006|GV.OV-02,ID.IM-01|GV-PRC-007|ISO/IEC 27001:2022 Clause 9.2.2 (audit results); CSA s.54 (summary report to NCSA within 30 days)|Governance|9.2|CA-2|IA|AC|Annual
GV-POL-006|GV.SC-01,GV.SC-02,GV.SC-03|GV-POL-001|ISO/IEC 27001:2022 Annex A 5.19; NIST SP 800-161 Rev. 1|Process|A.5.19,A.5.21|SR-1,SA-9|CISO|CEO|Annual
GV-PRC-008|GV.SC-04,GV.SC-06,GV.SC-07,GV.SC-10,ID.RA-10|GV-POL-006|ISO/IEC 27001:2022 Annex A 5.19 and 5.22; NIST SP 800-161 Rev. 1|Process|A.5.19,A.5.22|SR-2,SR-6,SA-9|CISO|CIO|Annual
GV-REG-009|GV.SC-04,ID.AM-04|GV-PRC-008|ISO/IEC 27001:2022 Annex A 5.19|Process|A.5.19|SR-6,PM-30|PROC|CISO|Semi-annual
GV-FRM-006|GV.SC-06,GV.SC-07,ID.RA-10|GV-PRC-008|ISO/IEC 27001:2022 Annex A 5.19 and 5.21|Process|A.5.19,A.5.21|SR-6,SA-9|CISO|CISO|Annual
GV-STD-002|GV.SC-05,GV.SC-08|GV-POL-006|ISO/IEC 27001:2022 Annex A 5.20; PDPA s.40|Process|A.5.20,A.5.21|SA-4,SA-9,SR-5|CISO|CIO|Annual
GV-STD-003|GV.SC-09,ID.RA-09,ID.RA-10|GV-POL-006|ISO/IEC 27001:2022 Annex A 5.21 and 5.23; NIST SP 800-161 Rev. 1|Technology|A.5.21,A.5.23|SA-4,SR-3,SR-11|CISO|CIO|Annual
GV-FRM-007|GV.SC-10|GV-PRC-008|ISO/IEC 27001:2022 Annex A 5.20|Process|A.5.20|SA-9,PS-7|PROC|CISO|Annual
ID-STD-001|ID.AM-01,ID.AM-02,ID.AM-04,ID.AM-05,ID.AM-07,ID.AM-08|GV-POL-001|ISO/IEC 27001:2022 Annex A 5.9 and 5.11; CIS Controls v8.1 Controls 1 and 2|Technology|A.5.9,A.5.11|CM-8,PM-5|ITM|CIO|Annual
ID-PRC-001|ID.AM-08,PR.PS-03|ID-STD-001|ISO/IEC 27001:2022 Annex A 5.9, 7.13, and 7.14|Process|A.5.9,A.7.13,A.7.14|CM-8,MA-2,MP-6|ITM|CIO|Annual
ID-REG-001|ID.AM-01,ID.AM-05|ID-STD-001|ISO/IEC 27001:2022 Annex A 5.9; CIS Controls v8.1 Control 1|Technology|A.5.9|CM-8|ITM|CIO|Continuous; reconcile quarterly
ID-REG-002|ID.AM-02,ID.AM-04,ID.AM-05|ID-STD-001|ISO/IEC 27001:2022 Annex A 5.9; CIS Controls v8.1 Control 2|Technology|A.5.9|CM-8,CM-10|ITM|CIO|Continuous; reconcile quarterly
ID-REG-003|ID.AM-03,ID.AM-07|ID-STD-001|ISO/IEC 27001:2022 Annex A 5.9 and 5.12; supports PDPA s.39|Process|A.5.9,A.5.12,A.5.14|PM-5(1),CM-12|DPO|CISO|Annual
ID-RPT-001|ID.AM-03,PR.IR-01|ID-STD-001|ISO/IEC 27001:2022 Annex A 8.20 and 8.22; CIS Controls v8.1 Control 12|Technology|A.8.20,A.8.22|PL-8,CA-9|ITM|CIO|Annual and on major change
ID-REG-004|ID.AM-01,ID.AM-02,ID.AM-05|ID-STD-001|NIST SP 800-82 Rev. 3; IEC 80001-1|Technology|A.5.9|CM-8|FAC|CIO|Quarterly
ID-RPT-002|ID.AM-05,GV.OC-04,GV.OC-05|RC-POL-001|ISO 22301:2019 Clause 8.2.2; CRC Notification on CII duties 2024 (BCP criteria) [VERIFY]|Process|A.5.29,A.5.30|CP-2(8),RA-9|BCM|ISSC|Annual
ID-FRM-001|ID.AM-08,PR.DS-01|ID-PRC-001|ISO/IEC 27001:2022 Annex A 7.14 and 8.10; PDPA s.37(3); NIST SP 800-88|Technology|A.7.10,A.7.14,A.8.10|MP-6|ITM|ITM|Annual
ID-REG-005|ID.RA-03,ID.RA-04,ID.RA-05,ID.RA-06,GV.RM-06|GV-PRC-001|ISO/IEC 27001:2022 Clause 8.2 (results of risk assessments); CSA s.54|Process|6.1.2,8.2|RA-3,PM-28|CISO|ISSC|Quarterly
ID-PLN-001|ID.RA-06|ID-REG-005|ISO/IEC 27001:2022 Clause 6.1.3(e) and 8.3|Process|6.1.3,8.3|PM-4,CA-5|CISO|ISSC|Quarterly
ID-RPT-003|ID.RA-04,ID.RA-05|GV-PRC-001|CSA s.54 (annual risk assessment; summary to NCSA within 30 days); CRC Notification on CII duties 2024 [VERIFY]|Process|8.2|RA-3|CISO|ISSC|Annual
ID-STD-002|ID.RA-01,PR.PS-02|GV-POL-001|ISO/IEC 27001:2022 Annex A 8.8; CIS Controls v8.1 Control 7|Technology|A.8.8|RA-5,SI-2|CISO|CIO|Annual
ID-PRC-002|ID.RA-01,ID.RA-08,PR.PS-02|ID-STD-002|ISO/IEC 27001:2022 Annex A 8.8|Process|A.8.8|RA-5,SI-2|CISO|CIO|Annual
ID-REG-006|ID.RA-01,ID.RA-06|ID-PRC-002|ISO/IEC 27001:2022 Annex A 8.8|Technology|A.8.8|RA-5,PM-4|CISO|CIO|Continuous; report monthly
ID-PRC-003|ID.RA-01,ID.IM-02|ID-STD-002|ISO/IEC 27001:2022 Annex A 8.8 and 8.29; CIS Controls v8.1 Control 18|Technology|A.8.8,A.8.29|CA-8|CISO|CIO|Annual
ID-FRM-002|ID.RA-01|ID-PRC-003|Computer Crime Act B.E. 2550 s.5 and s.7 (written authorization separates testing from unauthorized access)|Process|A.8.29|CA-8|CISO|CIO|Annual
ID-PRC-004|ID.RA-02,ID.RA-03|GV-PRC-001|ISO/IEC 27001:2022 Annex A 5.7|Technology|A.5.7,A.5.6|PM-16,RA-10|CISO|CIO|Annual
ID-PRC-005|ID.RA-08|ID-PRC-002|ISO/IEC 29147 and ISO/IEC 30111|Process|A.8.8|RA-5(11)|CISO|CIO|Annual
ID-PRC-006|ID.IM-01,ID.IM-02,ID.IM-03,ID.IM-04|GV-POL-001|ISO/IEC 27001:2022 Clause 10.1 and 10.2|Process|10.1,10.2|PM-4,CA-5|CISO|ISSC|Annual
ID-REG-007|ID.IM-01,ID.IM-02,ID.IM-03,ID.IM-04|ID-PRC-006|ISO/IEC 27001:2022 Clause 10.2 (nature of nonconformities and results of corrective action)|Process|10.2|PM-4,CA-5|CISO|ISSC|Continuous; review monthly
ID-PLN-002|ID.IM-02,ID.IM-04|ID-PRC-006|CSA s.56 (readiness tests); CRC Notification on CII duties 2024 (annual BCP exercise) [VERIFY]|Process|A.5.24,A.5.30|CP-4,IR-3|CISO|ISSC|Annual
ID-TPL-001|ID.IM-03,ID.IM-04|ID-PRC-006|ISO/IEC 27001:2022 Annex A 5.27|Process|A.5.27|IR-4,IR-8|CISO|CIO|Annual
PR-POL-001|PR.AA-01,PR.AA-02,PR.AA-03,PR.AA-04,PR.AA-05|GV-POL-001|ISO/IEC 27001:2022 Annex A 5.15; PDPC Notification on Security Measures B.E. 2565 (access control and audit trail)|Technology|A.5.15,A.5.18,A.8.3|AC-1,IA-1|CISO|CEO|Annual
PR-STD-001|PR.AA-01,PR.AA-02,PR.AA-03,PR.AA-04|PR-POL-001|ISO/IEC 27001:2022 Annex A 5.16, 5.17, and 8.5; NIST SP 800-63B-4|Technology|A.5.16,A.5.17,A.8.5|IA-2,IA-5,IA-8|CISO|CIO|Annual
PR-STD-002|PR.AA-05,PR.AA-01|PR-POL-001|ISO/IEC 27001:2022 Annex A 8.2 and 8.18|Technology|A.8.2,A.8.18|AC-6,AC-2|CISO|CIO|Annual
PR-STD-003|PR.AA-03,PR.AA-05,PR.IR-01|PR-POL-001|ISO/IEC 27001:2022 Annex A 6.7 and 8.20|Technology|A.6.7,A.8.20|AC-17|CISO|CIO|Annual
PR-PRC-001|PR.AA-01,PR.AA-05|PR-POL-001|ISO/IEC 27001:2022 Annex A 5.16 and 5.18; PDPC Notification on Security Measures B.E. 2565|Process|A.5.16,A.5.18|AC-2|ITM|CIO|Annual
PR-PRC-002|PR.AA-05|PR-POL-001|ISO/IEC 27001:2022 Annex A 5.18|Process|A.5.18|AC-2|CISO|CIO|Annual
PR-FRM-001|PR.AA-01,PR.AA-05|PR-PRC-001|ISO/IEC 27001:2022 Annex A 5.18|Process|A.5.18|AC-2|ITM|CIO|Annual
PR-FRM-002|PR.AA-05|PR-STD-002|ISO/IEC 27001:2022 Annex A 8.2|Process|A.8.2|AC-6,AC-2|CISO|CIO|Annual
PR-FRM-003|PR.AA-05,GV.SC-07|PR-STD-003|ISO/IEC 27001:2022 Annex A 5.19 and 8.20|Process|A.5.19,A.8.20|AC-17,MA-4|CISO|CIO|Annual
PR-REC-001|PR.AA-05|PR-PRC-002|ISO/IEC 27001:2022 Annex A 5.18|Process|A.5.18|AC-2|SYSOWN|CISO|Each review cycle
PR-REG-001|PR.AA-05,PR.AA-01|PR-STD-002|ISO/IEC 27001:2022 Annex A 8.2|Technology|A.8.2|AC-2,AC-6|CISO|CIO|Quarterly
PR-POL-002|PR.AA-06,PR.IR-02,DE.CM-02|GV-POL-001|ISO/IEC 27001:2022 Annex A 7.1 to 7.14|Physical|A.7.1,A.7.2,A.7.4,A.7.5,A.7.11|PE-1|FAC|CEO|Annual
PR-PRC-003|PR.AA-06,DE.CM-02|PR-POL-002|ISO/IEC 27001:2022 Annex A 7.2 and 7.6|Physical|A.7.2,A.7.6|PE-2,PE-3,PE-6|FAC|CIO|Annual
PR-FRM-004|PR.AA-06|PR-PRC-003|ISO/IEC 27001:2022 Annex A 7.2|Physical|A.7.2|PE-8|FAC|FAC|Annual
PR-PLN-001|PR.AT-01,PR.AT-02|GV-POL-001|ISO/IEC 27001:2022 Clause 7.3 and Annex A 6.3; PDPC Notification on Security Measures B.E. 2565 (awareness)|People|7.3,A.6.3|AT-1,AT-2,AT-3|CISO|ISSC|Annual
PR-REG-002|PR.AT-02,GV.RR-04|PR-PLN-001|ISO/IEC 27001:2022 Clause 7.2 (documented evidence of competence)|People|7.2|AT-3,PM-13|CISO|HR|Annual
PR-REC-002|PR.AT-01,PR.AT-02|PR-PLN-001|ISO/IEC 27001:2022 Clause 7.2 (documented evidence of competence)|People|7.2,A.6.3|AT-4|HR|CISO|Continuous
PR-PRC-004|PR.AT-01|PR-PLN-001|NIST SP 800-50 Rev. 1|People|A.6.3|AT-2(1)|CISO|CIO|Annual
PR-POL-003|PR.DS-01,PR.DS-02,PR.DS-10|GV-POL-001|ISO/IEC 27001:2022 Annex A 5.12 and 5.13; PDPA s.37(1)|Governance|A.5.12,A.5.13,A.5.14|RA-2,MP-1,SC-1|CISO|CEO|Annual
PR-STD-004|PR.DS-01,PR.DS-02,PR.DS-10|PR-POL-003|ISO/IEC 27001:2022 Annex A 5.12, 5.13, and 5.14|Process|A.5.12,A.5.13,A.5.14|RA-2,MP-3,MP-4|CISO|CIO|Annual
PR-STD-005|PR.DS-01,PR.DS-02|PR-POL-003|ISO/IEC 27001:2022 Annex A 8.24|Technology|A.8.24|SC-8,SC-12,SC-13,SC-28|CISO|CIO|Annual
PR-STD-006|PR.DS-11|PR-POL-003|ISO/IEC 27001:2022 Annex A 8.13; CIS Controls v8.1 Control 11|Technology|A.8.13|CP-9|ITM|CIO|Annual
PR-PRC-005|PR.DS-11,RC.RP-03|PR-STD-006|ISO/IEC 27001:2022 Annex A 8.13|Technology|A.8.13|CP-9,CP-10|ITM|CIO|Annual
PR-REC-003|PR.DS-11,RC.RP-03|PR-PRC-005|ISO/IEC 27001:2022 Annex A 8.13|Technology|A.8.13|CP-9(1)|ITM|CISO|Each test
PR-STD-007|PR.DS-01,ID.AM-08|PR-POL-003|PDPA s.37(3); ISO/IEC 27001:2022 Annex A 5.33 and 8.10|Process|A.5.33,A.8.10|SI-12,MP-6|DPO|CIO|Annual
PR-STD-008|PR.DS-01,PR.DS-02,PR.DS-10|PR-POL-003|ISO/IEC 27001:2022 Annex A 8.12|Technology|A.8.12|AC-4,SI-4|CISO|CIO|Annual
PR-STD-009|PR.DS-01,PR.AA-03,PR.PS-01|GV-POL-003|ISO/IEC 27001:2022 Annex A 8.1 and 6.7|Technology|A.8.1,A.6.7|AC-19|CISO|CIO|Annual
PR-STD-010|PR.PS-01|GV-POL-001|ISO/IEC 27001:2022 Annex A 8.9; CIS Controls v8.1 Control 4; CIS Benchmarks|Technology|A.8.9|CM-2,CM-6,CM-7|ITM|CIO|Annual
PR-PRC-006|PR.PS-01,ID.RA-07|GV-POL-001|ISO/IEC 27001:2022 Annex A 8.32|Process|A.8.32|CM-3,CM-4|ITM|CIO|Annual
PR-FRM-005|PR.PS-01,ID.RA-07|PR-PRC-006|ISO/IEC 27001:2022 Annex A 8.32|Process|A.8.32|CM-3|ITM|CIO|Annual
PR-PRC-007|PR.PS-02,PR.PS-03,ID.RA-01|ID-STD-002|ISO/IEC 27001:2022 Annex A 8.8 and 8.19|Technology|A.8.8,A.8.19|SI-2|ITM|CIO|Annual
PR-STD-011|PR.PS-04,DE.CM-01,DE.CM-03,DE.CM-09|GV-POL-001|Computer Crime Act B.E. 2550 s.26 (service providers retain computer traffic data for at least 90 days; the Act sets the duty, not the document); ISO/IEC 27001:2022 Annex A 8.15 and 8.17|Technology|A.8.15,A.8.17|AU-2,AU-3,AU-8,AU-9,AU-11|CISO|CIO|Annual
PR-STD-012|PR.PS-05,DE.CM-09|GV-POL-001|ISO/IEC 27001:2022 Annex A 8.1, 8.7, and 8.19|Technology|A.8.1,A.8.7,A.8.19|SI-3,CM-7,CM-11|ITM|CIO|Annual
PR-REG-003|PR.PS-05,ID.AM-02|PR-STD-012|ISO/IEC 27001:2022 Annex A 8.19; CIS Controls v8.1 Control 2|Technology|A.8.19|CM-7(5),CM-10|ITM|CISO|Quarterly
PR-STD-013|PR.PS-06|GV-POL-001|ISO/IEC 27001:2022 Annex A 8.25 to 8.31; NIST SP 800-218 (SSDF)|Technology|A.8.25,A.8.26,A.8.28,A.8.29,A.8.31|SA-3,SA-8,SA-11,SA-15|DEV|CIO|Annual
PR-STD-014|PR.PS-01,PR.IR-01,GV.SC-05,PR.AA-05|GV-POL-006|ISO/IEC 27001:2022 Annex A 5.23; ISO/IEC 27017; CRC Notification on cloud security for CII [VERIFY]|Technology|A.5.23|SA-9,AC-20|CISO|CIO|Annual
PR-STD-015|PR.PS-01,PR.IR-01,PR.PS-02|GV-POL-001|NIST SP 800-82 Rev. 3; IEC 62443; IEC 80001-1|Technology|A.8.9,A.8.22|SC-7,CM-7|CISO|CIO|Annual
PR-STD-016|PR.IR-01|GV-POL-001|ISO/IEC 27001:2022 Annex A 8.20 to 8.23; CIS Controls v8.1 Controls 12 and 13|Technology|A.8.20,A.8.21,A.8.22,A.8.23|SC-7,AC-4|ITM|CIO|Annual
PR-PRC-008|PR.IR-01|PR-STD-016|ISO/IEC 27001:2022 Annex A 8.20 and 8.32|Technology|A.8.20,A.8.32|SC-7,CM-3|ITM|CIO|Annual
PR-FRM-006|PR.IR-01|PR-PRC-008|ISO/IEC 27001:2022 Annex A 8.20|Technology|A.8.20|SC-7,CM-3|ITM|CISO|Annual
PR-STD-017|PR.IR-03,PR.IR-04|RC-POL-001|ISO/IEC 27001:2022 Annex A 8.6 and 8.14|Technology|A.8.6,A.8.14|CP-2(2),CP-7,SC-5|ITM|CIO|Annual
DE-STD-001|DE.CM-01,DE.CM-02,DE.CM-03,DE.CM-06,DE.CM-09|GV-POL-001|CSA s.56 (monitoring mechanism); ISO/IEC 27001:2022 Annex A 8.16|Technology|A.8.16|SI-4,AU-6|CISO|CIO|Annual
DE-PRC-001|DE.CM-01,DE.CM-03,DE.CM-09,DE.AE-06|DE-STD-001|ISO/IEC 27001:2022 Annex A 8.16|Process|A.8.16|SI-4,IR-5|SOC|CISO|Annual
DE-REG-001|DE.CM-01,DE.CM-09,PR.PS-04|DE-STD-001|ISO/IEC 27001:2022 Annex A 8.15 and 8.16|Technology|A.8.15,A.8.16|AU-2,SI-4|SOC|CISO|Quarterly
DE-GDL-001|DE.CM-06,GV.SC-05|DE-STD-001,GV-STD-002|ISO/IEC 27001:2022 Annex A 5.22|Process|A.5.20,A.5.22|SA-9|CISO|CIO|Annual
DE-PRC-002|DE.AE-02,DE.AE-03,DE.AE-04,DE.AE-06,DE.AE-07|DE-STD-001|ISO/IEC 27001:2022 Annex A 5.25|Process|A.5.25|IR-4,SI-4|SOC|CISO|Annual
DE-STD-002|DE.AE-04,DE.AE-08,RS.MA-03|RS-PLN-001|CRC Notification on CII duties 2024 (incident reporting within 24 hours) [VERIFY]; ISO/IEC 27001:2022 Annex A 5.25|Process|A.5.25|IR-4,IR-8|CISO|CIO|Annual
DE-REG-002|DE.AE-02,DE.AE-07,DE.CM-01,DE.CM-09|DE-STD-001|MITRE ATT&CK; ISO/IEC 27001:2022 Annex A 8.16|Technology|A.8.16|SI-4|SOC|CISO|Quarterly
DE-PRC-003|DE.AE-02,DE.AE-03,DE.AE-07|DE-STD-001|NIST SP 800-53 Rev. 5 RA-10|Technology|A.8.16|RA-10|SOC|CISO|Annual
RS-PLN-001|RS.MA-01,RS.MA-04,RS.MA-05,RS.CO-02,RS.CO-03,GV.SC-08,ID.IM-04|GV-POL-001|CSA s.44 (incident response plan within the code of practice) and s.58; ISO/IEC 27001:2022 Annex A 5.24; NIST SP 800-61 Rev. 3|Process|A.5.24,A.5.26|IR-1,IR-8|CISO|CEO|Annual
RS-PRC-001|RS.MA-02,RS.MA-03,RS.MA-04,RS.MA-05,RS.MI-01,RS.MI-02|RS-PLN-001|ISO/IEC 27001:2022 Annex A 5.26; NIST SP 800-61 Rev. 3|Process|A.5.26|IR-4|CISO|CIO|Annual
RS-PLB-001|RS.MI-01,RS.MI-02,RS.AN-03,RC.RP-03|RS-PRC-001|NIST SP 800-61 Rev. 3; NIST IR 8374 (Ransomware Risk Management)|Process|A.5.26|IR-4|CISO|CIO|Annual
RS-PLB-002|RS.MI-01,RS.MI-02,RS.AN-03|RS-PRC-001|NIST SP 800-61 Rev. 3|Process|A.5.26|IR-4|CISO|CIO|Annual
RS-PLB-003|RS.MA-03,RS.AN-08,RS.CO-02,RS.CO-03|RS-PRC-001,GV-POL-004|PDPA s.37(4); PDPC Notification on Breach Notification Criteria B.E. 2565 [VERIFY]|Process|A.5.26,A.5.34|IR-4,IR-6|DPO|CIO|Annual
RS-PLB-004|RS.MI-01,RS.MI-02|RS-PRC-001|NIST SP 800-61 Rev. 3|Process|A.5.26|IR-4|CISO|CIO|Annual
RS-FRM-001|RS.MA-02|RS-PRC-001|ISO/IEC 27001:2022 Annex A 6.8|Process|A.6.8|IR-6|CISO|CISO|Annual
RS-REG-001|RS.MA-02,RS.MA-03,RS.AN-03,RS.AN-08|RS-PRC-001|ISO/IEC 27001:2022 Annex A 5.25 and 5.26|Process|A.5.25,A.5.26|IR-5|CISO|CIO|Continuous
RS-REG-002|RS.MA-01,RS.CO-02,RS.CO-03,GV.SC-08|RS-PLN-001|CSA s.46 and s.52 (contact officers and CII contact details within 30 days)|People|A.5.5,A.5.6|IR-6,IR-7|CISO|CIO|Quarterly
RS-PRC-002|RS.AN-03,RS.AN-06,RS.AN-07,RS.AN-08|RS-PLN-001|ISO/IEC 27001:2022 Annex A 5.28; ISO/IEC 27037|Process|A.5.28|AU-9,IR-4|CISO|CIO|Annual
RS-FRM-002|RS.AN-06,RS.AN-07|RS-PRC-002|ISO/IEC 27001:2022 Annex A 5.28; ISO/IEC 27037|Process|A.5.28|AU-9|CISO|CISO|Annual
RS-TPL-001|RS.AN-03,RS.AN-06,RS.AN-08|RS-PRC-001|ISO/IEC 27001:2022 Annex A 5.26 and 5.27|Process|A.5.26,A.5.27|IR-4,IR-6|CISO|CIO|Annual
RS-PRC-003|RS.CO-02,RS.CO-03|RS-PLN-001|PDPA s.37(4) (notify the PDPC within 72 hours); CSA s.57 and s.58; CRC Notification on CII duties 2024 [VERIFY]|Process|A.5.5,A.5.24|IR-6,IR-7|CISO|CEO|Annual
RS-TPL-002|RS.CO-02,RS.CO-03|RS-PRC-003|PDPA s.37(4); CSA s.57|Process|A.5.5|IR-6|DPO|LEGAL|Annual
RC-POL-001|RC.RP-01,GV.OC-04|GV-CHR-001|CRC Notification on CII duties 2024 (BCP) [VERIFY]; ISO 22301:2019 Clause 5.2; ISO/IEC 27001:2022 Annex A 5.29 and 5.30|Governance|A.5.29,A.5.30|CP-1|BCM|CEO|Annual
RC-PLN-001|RC.RP-01,RC.RP-02,RC.RP-04,RC.RP-06,RC.CO-03|RC-POL-001|CRC Notification on CII duties 2024 (prepare a BCP under prescribed criteria) [VERIFY]; ISO 22301:2019 Clause 8.4|Process|A.5.29,A.5.30|CP-2|BCM|CEO|Annual
RC-PLN-002|RC.RP-01,RC.RP-02,RC.RP-03,RC.RP-05|RC-PLN-001|ISO/IEC 27001:2022 Annex A 5.30; supports CRC Notification on CII duties 2024 [VERIFY]|Technology|A.5.30,A.8.14|CP-2,CP-10|ITM|CIO|Annual
RC-PRC-001|RC.RP-02,RC.RP-03,RC.RP-05|RC-PLN-002|ISO/IEC 27001:2022 Annex A 5.37|Technology|A.5.30,A.5.37|CP-10|ITM|CIO|Annual and after each test
RC-REC-001|RC.RP-02,RC.RP-05,ID.IM-02|ID-PLN-002|CRC Notification on CII duties 2024 (annual BCP exercise) [VERIFY]; ISO 22301:2019 Clause 8.5|Process|A.5.30|CP-4|BCM|ISSC|Each exercise
RC-FRM-001|RC.RP-04,RC.RP-05,RC.RP-06|RC-PLN-002|NIST SP 800-61 Rev. 3|Process|A.5.26|CP-10,IR-4|ITM|CIO|Annual
RC-PLN-003|RC.CO-03,RC.CO-04,RS.MA-04|RC-POL-001|ISO 22361:2022; ISO 22301:2019 Clause 8.4.2|Governance|A.5.29|CP-2,IR-8|BCM|CEO|Annual
RC-PRC-002|RC.CO-03,RC.CO-04|RC-PLN-001|ISO 22301:2019 Clause 8.4.3|Process|A.5.29|CP-2,IR-7|COMMS|CEO|Annual
RC-TPL-001|RC.CO-04,RC.CO-03|RC-PRC-002|ISO 22301:2019 Clause 8.4.3|Process|A.5.29|IR-7|COMMS|CEO|Annual
"""

def parse_docs():
    from register import REG
    R = REG["documents"]
    rows = {}
    for line in DOCS_TABLE.strip().splitlines():
        p = [x.strip() for x in line.split("|")]
        assert len(p) == 10, (len(p), line)
        rows[p[0]] = p
    assert set(rows) == set(R), sorted(set(rows) ^ set(R))
    docs = []
    for did, r in R.items():
        p = rows[did]
        d = dict(id=did, en=r["title"], th=r["th"], type=r["type"], cat=r["category"],
                 csf=[x for x in p[1].split(",") if x], parents=[] if p[2] == "-" else p[2].split(","),
                 level=r["level"], trigger=list(r["trigger"]), basis=p[3], ppt=p[4], pkg=r["package"],
                 iso=[x for x in p[5].split(",") if x], nist=[x for x in p[6].split(",") if x],
                 owner=p[7], approver=p[8], review=p[9])
        d["tier"] = TYPES[d["type"]][2]
        assert d["tier"] == r["hierarchy"], did
        d["fn"] = d["id"][:2]
        docs.append(d)
    return docs

DOCS = parse_docs()
DOC = {d["id"]: d for d in DOCS}
for d in DOCS:
    d["children"] = [c["id"] for c in DOCS if d["id"] in c["parents"]]

def cmc_level(d):
    """Resolve level for CMC context."""
    trig = set(d["trigger"])
    if d["level"] == "Required":
        if trig & CMC_TRIGGERS:
            return "Required"
        return "Expected"  # ISO-only requirement while CMC is not yet certified
    if d["level"] == "Expected" and ("CII" in trig and "CII" in CMC_TRIGGERS) and d["id"] in ("RS-PRC-003", "DE-STD-001", "ID-PLN-002", "ID-RPT-002", "RC-PLN-002"):
        return "Expected (high priority for CII)"
    return d["level"]

if __name__ == "__main__":
    print(len(DOCS))
    ids = [d["id"] for d in DOCS]
    assert len(ids) == len(set(ids))
    for d in DOCS:
        for p in d["parents"]:
            assert p in DOC, (d["id"], p)
        for c in d["csf"]:
            assert c in SUBCATS, (d["id"], c)
    covered = {c for d in DOCS for c in d["csf"]}
    print("missing subcats:", sorted(set(SUBCATS) - covered))
    print("subcats", len(SUBCATS))
    from collections import Counter
    print(Counter(d["fn"] for d in DOCS)); print(Counter(d["tier"] for d in DOCS)); print(Counter(d["pkg"] for d in DOCS))
