# Information Gathering: Industry Packs and Mandate Tags (Verification Log)

Version 2.0 (M2), 2026-10-23. Source: `_Build-Source/packs.py`. Applies to `00_Master/Information-Gathering.html`.

## 1. Key Message

Mandate tags tell the assessor which Subcategories carry a legal, regulatory, contractual, or certification requirement for this client. Tags come from the regulatory flags, the industry pack and its options, and the client's other obligations. The legal instruments listed as "Instrument checked" were confirmed against a source; every Subcategory mapping is practitioner judgment. Items marked "Verify clause" need a check of the clause or number before a deliverable cites them.

## 2. Mandate and Reference Tags

| ID | Active when | Kind | Type | Instrument | Requirement | Subcategories | Status |
|---|---|---|---|---|---|---|---|
| CII-44 | `flag:cii` | Law | Mandate | Cybersecurity Act B.E. 2562, Section 44 | Keep a code of practice and a standard framework for cybersecurity. | GV.PO-01, GV.PO-02 | Instrument checked |
| CII-54 | `flag:cii` | Law | Mandate | Cybersecurity Act B.E. 2562, Section 54, and the 2024 notification on CII duties | Assess risk and complete an audit at least once a year; report results to the NCSA by 31 January. | ID.RA-05, ID.IM-02, GV.OV-01 | Instrument checked |
| CII-57 | `flag:cii` | Law | Mandate | Cybersecurity Act B.E. 2562, Section 57, and the 2024 notification (effective 20 June 2024) | Report significant cyber threats to the NCSA and the regulator within 24 hours. | RS.CO-02, RS.MA-01 | Instrument checked |
| PDPA-37S | `flag:pdpa` | Law | Mandate | PDPA B.E. 2562, Section 37(1), and the PDPC notification on security measures | Apply appropriate security measures to personal data, including access control. | PR.DS-01, PR.DS-02, PR.AA-05 | Instrument checked |
| PDPA-37B | `flag:pdpa` | Law | Mandate | PDPA B.E. 2562, Section 37(4), and the PDPC notification on breach notification (2022) | Notify the PDPC Office of a personal data breach within 72 hours unless it is unlikely to affect individuals; notify data subjects of high-risk breaches. | RS.CO-02, RS.MA-01 | Instrument checked |
| PDPA-39 | `flag:pdpa` | Law | Mandate | PDPA B.E. 2562, Section 39 | Keep a record of processing activities. | ID.AM-07 | Instrument checked |
| PDPA-40 | `flag:pdpa` | Law | Mandate | PDPA B.E. 2562, Section 40 | Bind data processors by agreement to protect personal data and follow the controller's instructions. | GV.SC-05 | Verify clause |
| CCA-26 | `flag:cca` | Law | Mandate | Computer Crime Act B.E. 2550 (amended B.E. 2560), Section 26, and the MDES notification on traffic data retention | Service providers keep computer traffic data for at least 90 days. | PR.PS-04 | Verify clause |
| ISO-RA | `flag:iso` | Standard | Mandate | ISO/IEC 27001:2022, Clauses 6.1.2 and 8.2 | Run and record information security risk assessments at planned intervals. | ID.RA-05, GV.RM-01 | Instrument checked |
| ISO-AUD | `flag:iso` | Standard | Mandate | ISO/IEC 27001:2022, Clauses 9.2 and 9.3 | Hold internal audits and management reviews at planned intervals. | ID.IM-02, GV.OV-01 | Instrument checked |
| HC-PDPA26 | `opt:hc:sens` | Law | Mandate | PDPA B.E. 2562, Section 26 (health data) | Process health data only on a Section 26 basis, with stronger protection for sensitive data. | GV.OC-03, PR.DS-01, PR.AA-05 | Instrument checked |
| HC-NHA7 | `pack:hc` | Law | Mandate | National Health Act B.E. 2550, Section 7 | Keep personal health information confidential. | PR.DS-01, PR.AA-05 | Instrument checked |
| HC-SHG | `opt:hc:state` | Guideline | Reference | NCSA and TMI Cybersecurity Operational Guidelines for State Hospitals B.E. 2567 | Guideline for state hospitals; confirm which parts the parent ministry requires. | GV.PO-01, PR.AA-05, PR.DS-11, RS.MA-01 | Instrument checked |
| HC-HA | `pack:hc` | Standard | Reference | Hospital Accreditation (HA) standards, information management chapter | Accreditation surveyors review information security and system continuity; confirm the current edition and section. | GV.PO-01, RC.RP-01 | Verify clause |
| OT-62443 | `pack:mfg` | Standard | Reference | IEC 62443-2-1 and 62443-3-3; NIST SP 800-82 Rev. 3 | Usual reference for OT security; usually a customer or insurer expectation, not law. | ID.AM-01, PR.IR-01, PR.PS-01, RC.RP-03 | Instrument checked |
| UT-62443 | `pack:util` | Standard | Reference | IEC 62443 and NIST SP 800-82 Rev. 3; Energy ISAC (NCSA and Ministry of Energy, 2025) | OT security reference and sector information sharing; check the regulator named in any CII designation. | ID.AM-01, PR.IR-01, RS.CO-03 | Instrument checked |
| BOT-21 | `opt:fin:bot` | Regulation | Mandate | Bank of Thailand Notification SorNorSor. 21/2562, IT risk governance of financial institutions | Board-level IT risk governance, IT and cyber risk management, and third-party risk management; check the clauses for each control. | GV.RR-01, GV.RM-01, GV.OV-01, GV.SC-04, GV.SC-07, PR.AA-05 | Instrument checked |
| BOT-19 | `opt:fin:bot` | Regulation | Mandate | Bank of Thailand Notification FPG. 19/2559, IT outsourcing | Controls and approvals for IT outsourcing, including cloud. | GV.SC-05, GV.SC-06 | Verify clause |
| SEC-37 | `opt:fin:sec` | Regulation | Mandate | SEC Notification Sor Thor. 37/2559 on IT system standards, updated by Sor Thor. 38/2565 | IT governance, security, and continuity standards for licensed businesses; check the clauses for each control. | GV.RM-01, PR.AA-05, PR.DS-11, DE.CM-01, RS.MA-01 | Instrument checked |
| OIC-63 | `opt:fin:oic` | Regulation | Mandate | OIC criteria on IT risk management B.E. 2563 (effective 1 January 2021) | A director with IT knowledge, outsourcing controls, and a report of critical cyber attacks within 72 hours. | GV.RR-01, GV.SC-05, RS.CO-02 | Instrument checked |
| PCI-8.4.2 | `opt:hosp:card` | Contract | Mandate | PCI DSS v4.0.1, Requirement 8.4.2 | Multi-factor authentication for all access into the cardholder data environment. | PR.AA-03 | Instrument checked |
| PCI-11.3 | `opt:hosp:card` | Contract | Mandate | PCI DSS v4.0.1, Requirements 11.3 and 11.4 | Quarterly internal and approved external vulnerability scans; annual penetration test, including segmentation tests. | ID.RA-01, ID.IM-02 | Instrument checked |
| PCI-3-4 | `opt:hosp:card` | Contract | Mandate | PCI DSS v4.0.1, Requirements 3 and 4 | Protect stored account data and encrypt cardholder data sent over open networks. | PR.DS-01, PR.DS-02 | Verify clause |
| PCI-6-10 | `opt:hosp:card` | Contract | Mandate | PCI DSS v4.0.1, Requirements 6.3 and 10 | Patch known vulnerabilities on a set timeline and log and review access to cardholder data. | PR.PS-02, PR.PS-04, DE.CM-09 | Verify clause |
| PCI-12 | `opt:hosp:card` | Contract | Mandate | PCI DSS v4.0.1, Requirements 12.8 and 12.10 | Manage service providers that affect card data, and keep an incident response plan ready. | GV.SC-07, RS.MA-01 | Verify clause |
| NCSC-66 | `opt:pub:state` | Regulation | Mandate | NCSC notifications on security categories and minimum standards for data and information systems B.E. 2566 (effective 18 January 2025) | Classify each data and information system low, medium, or high; review at least every three years; apply the minimum measures for the category. | ID.AM-05, ID.RA-05, GV.PO-01, PR.AA-05, PR.DS-01, PR.PS-02, DE.CM-01, RS.MA-01 | Instrument checked |

## 3. Sources Checked

| Instrument | Source |
|---|---|
| Cybersecurity Act Sections 44, 54, 57 and the 2024 notification | ThaiCERT CII page; Tilleke & Gibbins (Workshop verification log, 16 October 2026) |
| PDPA Sections 26, 37 and the PDPC breach notification (2022) | Tilleke & Gibbins (Workshop verification log, 16 October 2026) |
| PDPA Section 39 record of processing | Forvis Mazars Thailand, record of processing activities (checked 23 October 2026) |
| BOT SorNorSor. 21/2562 and FPG. 19/2559 | Google Cloud BOT Thailand compliance page (checked 23 October 2026); FPG 19 clause content not checked |
| SEC Sor Thor. 37/2559 and 38/2565; OIC B.E. 2563 | Huawei Cloud compliance page; Tilleke & Gibbins (Workshop verification log, 16 October 2026) |
| National Health Act Section 7; State Hospital Guidelines B.E. 2567 | Act text; MOPH-hosted guideline (Workshop verification log, 16 October 2026) |
| NCSC minimum standards B.E. 2566 | Tilleke & Gibbins (Workshop verification log, 16 October 2026) |
| PCI DSS v4.0.1 Requirements 8.4.2, 11.3, 11.4 | Secondary source summary of v4.0.1 (checked 23 October 2026); confirm against the PCI SSC document library |

## 4. Packs

| Pack | TSIC | Options | Extra probes | Pack checks |
|---|---|---|---|---|
| General | Any | - | 0 on - | - |
| Healthcare | Q | Processes health data (sensitive personal data) (default on); State hospital | 5 on PR.AA-05, ID.AM-01, PR.AA-01, GV.SC-05, RC.RP-01 | HC-01, HC-02 |
| Manufacturing | C | - | 4 on GV.OC-04, GV.OC-03, PR.IR-01, RC.RP-03 | MFG-01, MFG-02 |
| Financial services | K | Supervised by the Bank of Thailand; Licensed by the SEC; Supervised by the Office of Insurance Commission | 4 on RS.CO-02, GV.SC-05, GV.RR-01, DE.AE-02 | FIN-01 |
| Hospitality and retail | I, G | Stores, processes, or sends payment card data (default on) | 3 on PR.IR-01, PR.AA-01, GV.OC-03 | HOS-01 |
| Energy and utilities | D, E | - | 2 on GV.OC-04, RS.CO-03 | UTL-01 |
| Public sector | O | State agency (department, state enterprise, or public university) (default on) | 2 on ID.AM-05, GV.OC-03 | PUB-01 |

## 5. Open Items Before Freeze

| Item | Action |
|---|---|
| PDPA Section 40, Computer Crime Act Section 26 retention period, BOT FPG. 19/2559 clauses | Confirm clause text |
| PCI DSS Requirements 3, 4, 6.3, 10, 12.8, 12.10 | Confirm against the PCI SSC v4.0.1 document |
| Hospital Accreditation standard edition and section | Confirm with the current HA standard |
| CII Category coverage (tooling plan decision D5) | Still open; CII tags here cover Sections 44, 54, and 57 only |
