# Function Context Blocks

Method version 1.3. The HTML inserts one block into `{{FUNCTION_CONTEXT}}` of the Analyst prompt. Each block tells the Analyst where evidence for that Function usually sits, which causes are typical, and which links to other Functions to flag. Keep the blocks the same length and shape so all six outputs look alike.

---

## GV Govern

- **Scope:** GV.OC, GV.RM, GV.RR, GV.PO, GV.OV, GV.SC.
- **Main evidence:** interview notes from S1, S3, S4, S5; document status (charter, policy, risk method, RACI, supplier register); Vendor profile (V1 to V7).
- **Typical causes:** Ownership (no accountable executive), Capacity (no security function). These causes usually justify Inferred findings across all Functions; flag them for Stage 2 as systemic.
- **Watch for:** a policy that exists on paper but is unsigned or unknown to staff (precondition test); a risk register that IT keeps alone (lost decision for leadership); supplier contracts without security or notification clauses on vendors with remote access.
- **Impact:** usually legal and financial. For GV.SC, carry the impact of the linked systems from the Vendor profile.
- **Links to flag:** GV.SC to DE.CM-06 and PR.AA (vendor access); GV.RR to RS.MA (incident roles); GV.PO to every Prevent action in other Functions (the standard that makes a control the rule).
- **Validate and Sustain:** Validate: sample the policy, risk register, and RACI to confirm that owners know and use them. Sustain: an annual review recorded in the management review minutes.
- **Landscape blocks:** B1, B7, B9, B12, B14. Use B9 (security role, outsourced functions) for Ownership and Capacity causes and B14 for repeat findings.

## ID Identify

- **Scope:** ID.AM, ID.RA, ID.IM.
- **Main evidence:** Quick BIA and system list, Core profile C1 and C8, technical checks AST and VUL, document status (inventories, BIA, risk register), observations of type Vulnerability.
- **Typical causes:** Tooling (no discovery or scanning), Ownership (no system owner).
- **Watch for:** the system list built during S2 is itself evidence that no inventory exists; systems with Unknown answers show what the organization cannot see; vulnerabilities found by observation show that scanning does not run.
- **Impact:** inherit from the systems the gap leaves unseen. An unknown asset carries the impact of the most critical service it could touch.
- **Links to flag:** ID.AM to every coverage claim (coverage cannot be confirmed without an inventory); ID.RA-01 to PR.PS-02 (patching); ID.IM to RS and RC (lessons learned).
- **Validate and Sustain:** Validate: reconcile the inventory against a network scan or purchasing records. Sustain: a scheduled reconciliation and a remediation tracker with owners.
- **Landscape blocks:** B3, B8, B10, B11, B13. Use B3 and B10 for the population, B8 for where sensitive data sits, and B13 before any inventory or replacement action.

## PR Protect

- **Scope:** PR.AA, PR.AT, PR.DS, PR.PS, PR.IR.
- **Main evidence:** System Sampling and profiles (Core, Full, Development), coverage results, technical checks IAM, EP, NET, EML, DATA, BKP, CLD, APP, OT, PHY.
- **Typical causes:** Tooling, Skills, Vendor dependency (vendor-managed systems and vendor-held code).
- **Watch for:** profile results across all systems, not only the sample, to decide Observed versus Inferred; Development profile answers (no source code control, developers in production, production data in test) as evidence for PR.PS-06 and PR.DS; "Not supported by the system" and "End of life" answers as Handle exceptions candidates.
- **Impact:** start from the Quick BIA of the linked systems. Backup and identity gaps usually reach the highest operations score because they decide recovery from ransomware.
- **Links to flag:** PR.AA to GV.SC (vendor access); PR.DS-11 to RC.RP (restore); PR.PS-04 to DE.CM (logs).
- **Validate and Sustain:** Validate: retest the fixed systems, restore a backup, and check one newly added system against the standard. Sustain: scheduled access, coverage, and restore reviews with signed records.
- **Landscape blocks:** B4, B5, B6, B10, B13. Use B5 and B10 for extent, B6 before proposing any protective tool, and B13 for systems being replaced.

## DE Detect

- **Scope:** DE.CM, DE.AE.
- **Main evidence:** technical checks LOG, profile fields F6 (logging) and F7 (server protection), interview notes from S7, monitoring hours, managed security service provider (MSSP) contract status.
- **Typical causes:** Capacity (nobody watches), Tooling (no central logging), Vendor dependency (MSSP scope unclear).
- **Watch for:** logs that are collected but never reviewed (working control to condition of validity); monitoring that covers office hours only in a 24/7 operation; alerts with no criteria to declare an incident.
- **Impact:** the impact of the incident that goes unseen longer. Use the linked critical systems.
- **Links to flag:** DE.CM to PR.PS-04 (log generation); DE.AE to RS.MA (incident declaration).
- **Validate and Sustain:** Validate: send a test event and confirm it is detected and triaged in the defined time. Sustain: a periodic review of log source coverage.
- **Landscape blocks:** B4, B6, B9, B12. Use B6 for logging and monitoring tools, B9 for who watches, and B12 for the threats detection must catch.

## RS Respond

- **Scope:** RS.MA, RS.AN, RS.CO, RS.MI.
- **Main evidence:** S8 scenario walk-through notes, document status (incident response plan, playbooks, contact list), technical checks IR.
- **Typical causes:** Ownership (no incident manager), Skills (no forensic capability), Vendor dependency (no retained responder).
- **Watch for:** response that depends on named individuals (personal capability, not organizational); regulatory notification timelines that nobody can state (CII, PDPA); no authority to isolate a critical system at night.
- **Impact:** legal is often 4 because notification duties apply. Mark Thai legal thresholds [VERIFY] unless the Workshop regulatory verification confirms them.
- **Links to flag:** RS.MA to GV.RR (roles); RS.CO to GV.OC-03 (legal register); RS.MI to ID.RA (vulnerability handling).
- **Validate and Sustain:** Validate: run a tabletop exercise on the playbook and call the contact list to check it. Sustain: an annual exercise with a lessons learned entry.
- **Landscape blocks:** B9, B12, B14. Use B12 for the incident history and the scenarios that drive notification duties.

## RC Recover

- **Scope:** RC.RP, RC.CO.
- **Main evidence:** profile fields C9 (backup), F4 (restore test), F5 (recovery against tolerable downtime), Quick BIA tolerable downtime, S8 notes.
- **Typical causes:** Tooling (no immutable backup), Capacity (no restore testing), Ownership (no recovery order agreed with the business).
- **Watch for:** recovery time that was never tested against the tolerable downtime (instance to property); backups that ransomware can reach; recovery order that IT decides alone.
- **Impact:** operations and health and safety reach the Quick BIA maximum of the linked systems.
- **Links to flag:** RC.RP to PR.DS-11 (backup protection); RC.CO to RS.CO (communication).
- **Validate and Sustain:** Validate: run a restore or failover test against the recovery objective in the Business Impact Analysis (BIA). Sustain: an annual exercise report.
- **Landscape blocks:** B2, B4, B6, B13. Use B2 for tolerable downtime, B4 for the disaster recovery site and backup architecture, and B13 for systems being replaced.
