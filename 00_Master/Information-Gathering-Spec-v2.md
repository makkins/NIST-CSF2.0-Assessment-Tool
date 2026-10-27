# Information Gathering Tool v2.0: Specification

Version 2.0 (rev 6), 25 October 2026. Owner: Punthat. Status: frozen 25 October 2026 at app version 2.0.0. M1 to M5 built and tested (Sections 20 to 24). Changes from here are patch releases (v2.0.x) that fix defects only.

Replaces: `00_Master/Interview-Assessment.html` (schema `csf-interview/3`) and the assessment use of `00_Master/Document-Audit-Tracker.html` (app `csf-doc-audit` v1).
Related: `claude/tooling-improvement-plan.md` (v1.2), `claude/interview-system-profile-spec.md` (v1.0), `claude/csf-tier-rubric.md`, `claude/current-it-landscape-spec.md`, `claude/csf-document-framework-register.md`.

## 1. Key Message

One offline HTML file, `00_Master/Information-Gathering.html`, runs all of P1 fact gathering. It merges the Interview Assessment and the Document Audit Tracker into one engagement state, so documents, interviews, technical checks, and evidence share one Evidence Register. It records the Current state only; it holds no Target. Industry changes the content, scale changes the workflow, and every engagement still rates all 106 CSF 2.0 Subcategories. It ends with one handoff file, `csf-p1-handoff/1`, that the Gap Analysis reads. After the acceptance test passes, v2.0 is frozen: patch releases (v2.0.x) fix defects only.

## 2. Decisions

| ID | Decision | Effect |
|---|---|---|
| D-IG-01 | Merge Interview and Document Audit into Information-Gathering.html. Keep the standalone Audit Tracker build for the Document Framework project | One state, one Evidence Register. Closes plan issues 7 and 15 |
| D-IG-02 | The Workshop stays a separate file with no link to this tool. Gap Analysis joins Current (P1 handoff) and Target (Workshop) | Removes the Target selector. Fieldwork does not wait for executives. Assessors rate without seeing the Target |
| D-IG-03 | Industry pack changes content; Engagement scale changes workflow | Base content is industry-neutral |
| D-IG-04 | Scale is derived from five facts, proposed by the tool, confirmed by the assessor. No external size standard is cited | Scale sets workflow only. No size threshold from law or standards to maintain. Regulatory requirements come from industry packs and regulatory flags (D-IG-03, Section 6.3), not from scale |
| D-IG-05 | Adaptive depth: screening per Category, drill-down per Subcategory. Driven by screening result, regulatory mandate, and scale. All 106 Subcategories are always rated | Small engagements finish faster without losing coverage |
| D-IG-06 | Freeze content, workflow, and schema at v2.0. Patch releases fix defects only | |
| D-IG-07 | AI prompts target Claude and return JSON that the tool imports after assessor review | |
| D-IG-08 | Client self-assessment is exported as Excel and imported back. This is the only Excel import, limited to templates the tool generated (schema `csf-ig-sa/1`) | Exception to tooling plan Principle 1 |
| D-IG-09 | Defaults accepted on 23 October 2026: auto-migration from older files, optional password on save, lead file plus session files, evidence file naming, print packs, offline single file, TH and EN for all content, three test samples | See Sections 12 to 15 |

## 3. Scope

| In scope | Out of scope (owner) |
|---|---|
| Setup, scale, industry, regulatory flags | Target Tier and risk criteria (Workshop) |
| Pre-fieldwork pack: request list, schedule, emails, self-assessment, AI prompts | Gap Findings, risk scoring, recommendations (Gap Analysis) |
| Interviews, system and vendor profiles, environment, departments, technical checks, observations | Document roadmap waves and sourcing (Gap Analysis and P3; standalone Audit Tracker keeps its Gap roadmap tab) |
| Document review against the Register | Writing client documents (Document Framework) |
| Evidence Register | |
| Current Tier per Subcategory and Category | |
| P1 Summary and Landscape lock (plan W3-1) | |
| P1 handoff JSON and Excel deliverable | |

## 4. Architecture

| Item | Design |
|---|---|
| Delivery | One HTML file, no external requests, works offline. Size target under 2.5 MB |
| Build | `build_ig.py` with a new `ig_template.html`. It reads the same sources as today (`iq_*.py`, `tc.py`, `sessions.py`, `sysprofile.py`, `envprofile.py`, `deptprofile.py`, `rubric.py`, `register-ids.json`, `dictionary.py`, `site_data.json`) plus new `screening.py`, `packs.py`, `evidence.py`, `comms.py`, `prompts.py` |
| Standalone Audit Tracker | `build.py` still builds `Document-Audit-Tracker.html` for the Document Framework. Its confirm dialog and View mode patch move into `audit_template.html` and `build_html.py` first (plan Section 11 item 2) |
| State | One engagement object, app `csf-ig`, schema `csf-ig/4` |
| Autosave | Browser storage, as today, with a Setup switch to turn it off on shared computers |
| Save file | JSON. Optional password: AES-GCM with a PBKDF2-SHA256 key, using the browser Web Crypto API. No password, no encryption |
| Retired file | `Interview-Assessment.html` stays in `00_Master` until you delete it |

## 5. Navigation

Six stages replace the current twelve flat tabs. Each stage shows a completion bar.

| Stage | Tabs | Main users |
|---|---|---|
| 0. Setup | Engagement; Scale and industry; Team and aliases | Lead assessor |
| 1. Prepare | Request list; Schedule; Communications; Self-assessment; AI prompts | Lead assessor |
| 2. Fieldwork | Interview; Systems and BIA; Vendors; Environment; Departments; Technical; Observations | All assessors |
| 3. Documents | Applicability; Review | Assessor assigned to documents |
| 4. Evidence | Evidence Register; Requests and follow-up | All assessors |
| 5. Summary | Rate; Category tiers; Landscape lock; Dashboard; Export | Lead assessor |

## 6. Setup

### 6.1 Engagement facts

Client name, alias, assessor team, engagement reference, scope note, assessment start date, evidence cut-off date, sites in scope.

### 6.2 Scale

The tool asks five facts and proposes a scale. The assessor confirms or overrides with a reason.

| Fact | Field |
|---|---|
| Employees in scope | Number |
| IT staff (in-house and outsourced full-time) | Number |
| Business systems in scope | Number |
| Sites in scope | Number |
| Operational technology (OT), medical devices, or building systems on the network | Yes or No |

| Proposed scale | Rule (tool convention) |
|---|---|
| Small (S) | Under 200 employees, 15 systems or fewer, 2 sites or fewer |
| Large (L) | Over 40 systems, or over 5 sites, or over 1,000 employees with over 20 systems |
| Medium (M) | Everything else |
| Step up one level | CII operator, or OT present, with a Small result |

Scale measures fieldwork effort, so systems and sites drive it more than headcount. Document applicability (Register package rules) keeps the Audit Tracker organization size from employees only: under 200 small, 200 to 1,000 medium, over 1,000 large. Example: CMC (1,200 staff, 7 systems, 2 sites) is a Medium engagement and a large organization for document applicability.

| Workflow effect | S | M | L |
|---|---|---|---|
| Session plan | 4 combined sessions, about 1.5 days | S1 to S10, about 3 to 4 days | S1 to S10, with S2, S6, and S9 repeated per site or business unit |
| Systems sampled | 2 | 3 to 5 | 5 to 8, at least 1 per site |
| Department interviews | 2 | 4 to 6 | Per business unit |
| Default document review | Quick | Quick, Full for Required | Full for Required and Essential |
| Self-assessment | Optional | Recommended for S3 to S5 | Recommended |
| Drill-down default | By screening result | By screening result | All Categories |

### 6.3 Industry pack and regulatory flags

The Setup merges today's Audit profile flags (CII, PDPA, Computer Crime Act service provider, ISO/IEC 27001 certification, specialist staff, MSSP, cloud, generative AI, OT, development) with the industry choice.

| Pack | TSIC section | Adds |
|---|---|---|
| General | Any | Base content only |
| Healthcare | Q | CII public health, PDPA sensitive data, medical devices, Hospital Accreditation, clinical shared workstations, break-glass access |
| Manufacturing | C | OT and industrial control systems, IEC 62443 reference, supplier and plant network |
| Financial services | K | Bank of Thailand, SEC, and Office of Insurance Commission requirements, third-party and cloud outsourcing, fraud and customer channels |
| Hospitality and retail | I, G | PCI DSS, point-of-sale and guest networks, customer data, seasonal staff |
| Energy and utilities | D, E | CII energy, OT, safety systems |
| Public sector | O | CII government services, government standards for websites and services |

Each pack contains:

* a terminology map (customer, patient, guest, member);
* mandate tags per Subcategory, each with a legal reference and a verification status;
* added probes and technical checks.

Other obligations: a free list in Setup for requirements outside the packs, such as foreign law that applies by contract (for example a HIPAA business associate agreement with a United States client, or GDPR) and customer security requirements. Each entry records its source, and the assessor tags the affected Subcategories as mandates.

In v2.0, a pack does not add Register documents. The Register stays the Document Framework scope.

Base content is made industry-neutral. About 30 healthcare-specific phrases move into the Healthcare pack.

### 6.4 Team and aliases

Assessors (name, initials), interviewees (name, role, department, dates), and an alias map for client, people, vendors, sites, and systems. The alias map anonymizes AI prompts and the optional anonymized export (plan W4-5).

## 7. Adaptive Depth

| Element | Rule |
|---|---|
| Screening question | One per Category, 22 in total, in plain language for the interviewee. Answer: Practice exists; Partly; No practice; Unknown |
| Drill-down required | Any of: the Category carries a mandate tag; screening is Practice exists, Partly, or Unknown; scale is L; the assessor chooses drill-down |
| No practice | The tool offers batch rating: every Subcategory in the Category gets Tier 0 or 1 with one shared reason, evidence level Stated. The assessor can change any line |
| Coverage | Every Subcategory still ends rated or Not applicable. The handoff fails validation if any is blank |
| Path record | Each Subcategory records how it was rated: Drill-down, Batch, or Document only |

## 8. Content Changes

### 8.1 Methodology fixes

| ID | Change |
|---|---|
| A1 | Remove the Target Tier selector, the Gap column, and Target bars. Category tiers show Current only |
| A2 | Show mandate tags per Subcategory from the pack and Setup flags. A tagged Subcategory forces drill-down and an evidence request |
| A3 | Replace the free-text evidence reference with Evidence Register links (Section 9) |
| A4 | The Category tiers tab shows, beside the suggested tier (rule R4): lowest Subcategory tier, number of tagged Subcategories below Tier 2, and number capped |
| A5 | Coverage (rule R3): Core profile fields use every Criticality A system; Full profile fields use sampled systems. The coverage note shows both populations |
| A6 | Labels read "Implementation level (Tier-aligned)" in exports. The rubric note stays |
| A7 | Remove the Dashboard "Average Current Tier" tile and Function average bars (decision A14). Show the tier distribution per Category |

### 8.2 New probes and technical checks

| Topic | Subcategory | New item |
|---|---|---|
| Mobile device management and personal devices | PR.AA-05, PR.DS-01, PR.PS-01 | Technical check EP-07 |
| Messaging apps carrying customer or patient data | PR.DS-02, GV.PO-01 | Technical check DATA-07, department question |
| Generative AI use and data entered into AI tools | ID.AM-02, GV.PO-01, PR.DS-01 | Technical check DATA-08, probe on GV.PO-01 |
| Break-glass and emergency access accounts | PR.AA-05 | Technical check IAM-09 |
| Personnel screening at hiring | GV.RR-04 | Probe |
| External attack surface (domains, public IP addresses, certificates) | ID.AM-01, ID.RA-01 | Technical check AST-06 |
| Building systems and Internet of Things devices (CCTV, access control, building management) | ID.AM-01, PR.IR-01 | Technical check OT-04 |

### 8.3 Unchanged

The 106 Subcategory questions, scene and scenario framing, the 74 technical checks, system, vendor, and development profiles, environment fields and tables, department fields, Tier Rubric v1.2 rules R3 and R4, the evidence cap, and the session sequence logic all stay. Wording changes only where Section 6.3 moves healthcare terms into a pack.

## 9. Evidence Model

### 9.1 Evidence Register

Every fact that lifts a rating above Stated points to an Evidence ID.

| Field | Content |
|---|---|
| ID | `EV-<initials>-<number>`, for example `EV-PS-014`. Initials prevent clashes when files merge |
| Kind | Document; Record; System export; Screenshot; Live demonstration; Walk-through; Client self-assessment |
| Title and client reference | File name or system screen |
| Record date | The date the evidence shows (the as-of date), not the date received |
| Received date, provided by | Person from the interviewee list |
| Confidentiality | Normal; Restricted |
| Links | Register IDs, Subcategories, technical checks, systems, observations |
| Review | For Document and Record: link to the Register review (Section 9.3) |
| Cut-off flag | Automatic when the record date or received date falls after the evidence cut-off |

### 9.2 Evidence rules

| Rating evidence level | Requires |
|---|---|
| Documented | At least one linked Document, Record, or System export |
| Demonstrated | At least one linked Live demonstration, Screenshot, or Walk-through |
| Stated | No link needed. The evidence cap applies as today |
| Tier 3 or higher on Documented | At least one linked Record or System export dated within 12 months before the cut-off. Otherwise the tool flags "No current-cycle record" |

### 9.3 Document review (from the Audit Tracker)

| Element | Design |
|---|---|
| Applicability | Unchanged Audit rules (trigger, package, profile conditions, override with reason), driven by the merged Setup |
| Client document inventory | One received file can cover several Register IDs; one Register ID can be covered by several files. The mapping lives on the Evidence record |
| Quick review | Status (Exists, Partial, Missing, Not applicable) plus the 5 control checks (owner, approval, version history, review cycle, communication) |
| Full review | Quick review plus all content checks (about 12 per document) |
| Result | Status, review note, and linked Evidence IDs feed the Subcategory view and the handoff |
| Removed from this tool | Recommendation field, Gap roadmap tab, Activities tab. The standalone Audit Tracker keeps them |

### 9.4 Requests

One request list covers documents and technical evidence. Statuses: Requested, Received, Does not exist, Withheld. Marking an item Received creates an Evidence record prefilled from the request.

## 10. Rating Workflow

| Element | Design |
|---|---|
| Capture mode (default in Fieldwork) | The Interview view hides tier controls. The assessor records statements, probes, documents mentioned, technical answers, and observations |
| Statements | Per Subcategory: person, short statement, stance (Yes, Partly, No, Unknown), date. Self-assessment answers arrive as statements from "Client self-assessment, unverified" |
| Conflict flag | Stances differ between people, or a statement differs from linked profile or technical results |
| Rate mode (Summary stage) | One Category at a time: all statements, evidence, profile results, technical checks, coverage, and conflicts on one screen, then the tier per Subcategory |
| Rules kept | Evidence cap, coverage rule R3, suggested Category tier R4, reason required on override |
| Optional | The assessor can rate in Capture mode when the facts are clear |

## 11. Utilization: Prepare Stage

### 11.1 Initial request list

Generated at Setup and sent before kickoff.

| Source | Content |
|---|---|
| Register | In-scope documents with Level Required, plus package Essential, grouped by owner role |
| Technical evidence list (new, about 25 items) | Standard exports mapped to technical checks, for example the administrator group membership export, firewall rule summary, backup job report, latest vulnerability scan summary, EDR coverage report, MFA enrollment report |
| Output | Excel for the client with columns for "We have it", file name, and owner. Uses the self-assessment template (Section 11.4) |

### 11.2 Interview schedule

The tool builds a draft schedule from the scale, session dependencies, roles, and interviewee names. The assessor edits dates and times. The schedule exports to Excel and fills the invitation emails.

### 11.3 Communications (TH and EN)

Each template shows subject and body with merge fields from Setup and state, plus a copy button. No AI is needed.

| ID | Email | Sent |
|---|---|---|
| C1 | Kickoff and engagement confirmation | Before kickoff |
| C2 | Initial document and evidence request | With C1 or right after |
| C3 | Session invitation per role (agenda, duration, what to prepare) | One week before each session |
| C4 | Self-assessment cover note | With the Excel |
| C5 | Session read-back and thank you (key facts and new requests from that session) | Same day as the session |
| C6 | Outstanding evidence reminder (open requests by owner) | Weekly |
| C7 | Evidence cut-off notice | One week before the cut-off |
| C8 | P1 close and fact validation (locked Landscape summary) | End of P1 |

### 11.4 Client self-assessment (`csf-ig-sa/1`)

| Sheet | Content |
|---|---|
| Instructions | Purpose, deadline, contact, how to answer |
| Questions | One row per Category screening question and per drill-down Subcategory in scope: ID, plain question, answer drop-down, comment, document name |
| Systems | Core profile C1 to C9 with drop-downs, one row per system |
| Documents | Initial request list with "We have it", file name, owner |
| Hidden metadata | Schema ID, engagement ID, question set hash, generation date |

Sheets are protected so that only answer cells can change. Import checks the metadata, then loads answers as unverified statements, Core profile values as unconfirmed (only into empty fields), and document answers into request statuses. A difference report lists every self-assessment answer that conflicts with fieldwork.

### 11.5 AI prompts (Claude)

Each prompt replaces names with aliases before copy, states the JSON output schema, and has an import screen where the assessor accepts or rejects each item.

| ID | Prompt | Input | Output |
|---|---|---|---|
| P-01 | Client pre-research | Client name and industry (public information only) | Suggested Setup facts, regulatory flags, likely systems (`csf-ig-pre/1`) |
| P-02 | Interview notes to capture | Session ID, its questions, raw notes or transcript | Statements, stances, documents mentioned, requests, observations, follow-ups (`csf-ig-notes/1`) |
| P-03 | Document review assist | Register check list and the client document text | Check results with quoted support (`csf-ig-docrev/1`) |
| P-04 | Follow-up questions | Conflicts, Unknown answers, open requests | Question list per interviewee |
| P-05 | Landscape facts draft | Locked state summary | Draft facts for the Landscape lock (plan W3-1), facts only |

## 12. Collaboration

| Element | Design |
|---|---|
| Lead file | One per engagement. Holds Setup, aliases, and the merged result |
| Session file | Any assessor exports a session file (same schema, marked with assessor initials) |
| Merge | Lists keyed by ID are combined. For single fields: if only one side has a value, take it; if both differ, show a conflict list where the lead picks one |
| Change marks | Evidence and statements carry dates and assessor initials. Other fields carry no change marks; the lead resolves every difference in the merge screen (decided in M3) |

## 13. Outputs

### 13.1 P1 handoff `csf-p1-handoff/1` (JSON)

| Block | Content |
|---|---|
| engagement | Alias, scale, industry pack, flags, sites, cut-off, app version, rubric version, question set hash, export time, source hash |
| subcategories (106) | Stated tier, counted tier, evidence level, Evidence IDs, coverage band and percentage, statements count, conflict flag, mandate tags, rating path, notes, gap note |
| categories (22) | Suggested tier, override and reason, lowest Subcategory tier, capped count |
| systems | BIA impacts, tolerable downtime, criticality, Core, Full, and Development profiles, sampled flag |
| vendors | Vendor profile and linked systems |
| environment | Fields and tables (sites, tools, incident history, changes in flight, prior assessments) |
| documents | Register ID, applicability, level for client, review status, review depth, Evidence IDs |
| evidence | Full Evidence Register |
| observations | Vulnerabilities and incident indicators |
| requests | Open items at export |
| landscape | Locked facts with Evidence IDs |

Validation before export: all 106 Subcategories rated or Not applicable; every Documented or Demonstrated rating has a link; Landscape locked; no unresolved merge conflict. The JSON Schema is `00_Master/Gap-Analysis-Method/schemas/csf-p1-handoff-1.schema.json`; `00_Master/Gap-Analysis-Method/tools/check_handoff.py` applies the schema and these rules outside the tool. With aliases on, names in the handoff are replaced and `engagement.aliased` is true.

### 13.2 Excel deliverable

The current 22 sheets, plus Evidence Register, Document Review, Statements and Conflicts, and Self-assessment Differences. Target and Gap columns are removed.

## 14. Security

| Control | Design |
|---|---|
| Password on save | Optional, Section 4 |
| Autosave switch | Off on shared computers |
| Anonymized export | Applies the alias map to the Excel and handoff |
| Restricted evidence | Shown with a marker and left out of AI prompts |
| Help text | Handling guidance for laptops, email, and USB |

## 15. Migration

| Source | Handling |
|---|---|
| `csf-interview/3` save file | Converted on open. Free-text evidence references become notes on the Subcategory, not Evidence records. The Target is dropped, with a notice |
| `csf-doc-audit` v1 save file | Imported into Documents. The recommendation field moves into the review note |
| Combined engagement file (both parts) | Both conversions in one step |

## 16. Acceptance Test (before freeze)

| # | Test |
|---|---|
| 1 | Three samples run end to end: Small manufacturing, Medium hospital (CMC), Large bank |
| 2 | Each sample exports a valid `csf-p1-handoff/1` with 106 rated Subcategories |
| 3 | No Documented or Demonstrated rating lacks an Evidence ID |
| 4 | A merge of two session files with conflicts resolves without data loss |
| 5 | Self-assessment round trip: export, fill, import, difference report |
| 6 | Each AI prompt imports a sample JSON output |
| 7 | CMC `csf-interview/3` and Audit save files migrate without loss of ratings or document statuses |
| 8 | Password save and open round trip |
| 9 | No Target value anywhere in state or exports |
| 10 | Existing checks still pass: `check_enums.py`, `check_html.py`, Landscape parity, and Design Summary 15.1 items 1 to 4 |
| 11 | All labels, emails, and prompts exist in TH and EN |
| 12 | Every legal reference in the packs is Verified or marked [VERIFY] in the verification log |

## 17. Milestones

| ID | Output | Approval point |
|---|---|---|
| M0 | This specification | Your approval |
| M1 | Architecture: merged template, `csf-ig/4` state, migration, Setup with scale and pack switch, navigation stages, standalone Audit Tracker patch moved into scripts | Smoke test with CMC data |
| M2 | Content: methodology fixes A1 to A7, 22 screening questions, new probes and checks, neutral base wording, six industry packs with a verification log | You review the pack legal references |
| M3 | Workflow: adaptive depth, Capture and Rate modes, statements and conflicts, Evidence Register, document review depth, merge | Walk-through on CMC |
| M4 | Utilization: request list, technical evidence list, schedule, emails, self-assessment round trip, AI prompts and import screens, password save | You sample-check the Thai text |
| M5 | Three samples, acceptance test, Excel deliverable, handoff validator, updated `run_checks.py`, freeze v2.0 | Freeze |

Gap Analysis changes to read `csf-p1-handoff/1` and the Workshop export form the first task of the next phase.

## 18. Items to Verify Before Freeze

| Item | Why |
|---|---|
| CII code of practice and standard framework (2021) Category mapping (plan decision D5) | Sets mandate tags for every CII client |
| Bank of Thailand, SEC, and Office of Insurance Commission IT risk requirements: current notification numbers and key clauses | Financial services pack |
| PCI DSS current version and applicable requirements | Hospitality and retail pack |
| Hospital Accreditation information management standard references | Healthcare pack |
| PDPA breach notification timing and PDPC notifications cited in questions | Base content |

## 19. Change Log

| Version | Date | Change |
|---|---|---|
| 2.0 (rev 6), frozen | 25 October 2026 | M5 results and freeze (Section 24). Prompt bodies stay in English by design (Section 11.5); acceptance item 11 checks prompt names and descriptions in TH and EN |
| 2.0 draft (rev 5) | 23 October 2026 | M4 results (Section 23). Request list items join Requests only after "Use this list". Encrypted files use the `.enc.json` name |
| 2.0 draft (rev 4) | 23 October 2026 | M3 results (Section 22). Merge resolves differences by field instead of by change marks |
| 2.0 draft (rev 3) | 23 October 2026 | M2 results (Section 21). MOB-01 renamed EP-07 to follow the domain ID format. A3 moved to M3 with the Evidence Register |
| 2.0 draft (rev 2) | 23 October 2026 | Large scale rule changed so headcount alone does not make an engagement Large; document applicability uses employees only. M1 results added (Section 20) |
| 2.0 draft (rev 1) | 23 October 2026 | Clarified D-IG-04: scale does not affect regulatory requirements. Added "Other obligations" to Section 6.3 |
| 2.0 draft | 23 October 2026 | First specification after the review of Interview-Assessment.html and Document-Audit-Tracker.html |

## 20. M1 Build Results (23 October 2026)

| Item | Result |
|---|---|
| Delivered | `00_Master/Information-Gathering.html` (app 2.0.0-m1, schema `csf-ig/4`), built by `_Build-Source/build_ig.py` from `ig_template.html` and `packs.py` |
| Navigation | Six stages with progress bars; each stage shows its own tab row. Presentation view shows Category tiers and Dashboard only |
| Setup | Engagement (alias, evidence cut-off), assessor team with initials, interviewees; Scale and industry (five facts, proposed and confirmed scale with reason, seven industry packs, regulatory flags, other obligations with Subcategory check) |
| Documents | Applicability and Document review ported from the Audit Tracker; Gap roadmap, Activities, and Recommendation removed from this tool |
| Target | Removed from state, Category tiers, Dashboard, and Excel (A1). Dashboard shows tier distribution per Category; no average above Category (A7). Category tiers add the lowest Subcategory tier (part of A4) |
| Migration | Opens `csf-ig/4`, `csf-interview/2` and `/3`, `csf-doc-audit` v1, and combined engagement files. Tests pass for ratings, document statuses, checks, scope overrides, profile flags, round trip, and the impact scale remap |
| Excel | Same sheets as `csf-interview/3` (Gap Analysis and Landscape read it unchanged), Target and Gap columns removed, plus Engagement Setup and Document Review sheets. Summary carries `csf-ig/4` |
| Gap Analysis | Accepts `csf-ig/4` Interview exports; `landscape_facts.py` accepts it too. No other change |
| Audit Tracker | Confirm dialog and View mode moved into `audit_template.html` and `build_html.py`; Document Map uses the same View mode patch. Both rebuild byte-identical to the delivered files |
| Checks | `run_checks.py` builds Information Gathering instead of Interview. All checks pass except acceptance 6b (no sample IMP uses TOOL-07), which failed before M1 |
| Not in M1 | Industry pack content, screening and adaptive depth, Evidence Register, Capture and Rate modes, merge, Prepare stage tools, password on save, P1 handoff JSON. These follow in M2 to M5 |
| Your action | `Interview-Assessment.html` and `_Build-Source/build_interview.py` stay until you delete them. `build_interview.py` is still imported by `build_ig.py` for `load_data`, so keep it until M5 |

## 21. M2 Build Results (23 October 2026)

| Item | Result |
|---|---|
| Version | App 2.0.0-m2, schema unchanged (`csf-ig/4`); new state keys `scr` and `setup.popts` are optional, so M1 files open unchanged |
| Screening | 22 Category screening questions (EN and TH) in `screening.py`, shown at the top of each Subcategory, in session print packs, and in Category tiers. Answers: Practice exists, Partly, No practice, Unknown. Batch rating and drill-down rules follow in M3 |
| Mandate tags (A2) | 26 tags in `packs.py`: CII Sections 44, 54, 57; PDPA Sections 26, 37(1), 37(4), 39, 40; Computer Crime Act Section 26; ISO/IEC 27001 clauses; National Health Act Section 7; BOT, SEC, OIC; PCI DSS; NCSC minimum standards; references for HA, IEC 62443, and the State Hospital guideline. Other obligations become mandate tags. Shown on Scale and industry, as an M marker and filter in the Interview list, as a box in each Subcategory, in print packs, and in Excel (Mandates sheet and Subcategories columns). Verification log: `claude/ig-packs-verification-log.md` |
| Packs | Seven packs with options (for example BOT, SEC, OIC for Financial services; card data for Hospitality), terminology, 23 extra probes, and 8 pack technical checks that appear only when the pack is selected |
| New checks and probes | EP-07 mobile devices, DATA-07 messaging apps, DATA-08 generative AI, IAM-09 break-glass accounts, AST-06 external attack surface, OT-04 building systems and IoT; probes on GV.RR-04 (screening) and GV.PO-01 (AI and messaging) |
| Neutral wording | Base content no longer names HIS or PACS or assumes clinical owners; healthcare wording sits in the Healthcare pack |
| A4 | Category tiers show the lowest Subcategory tier, the count of mandated Subcategories below Tier 2, and the screening answer |
| A5 | Coverage counts Core profile answers on every Criticality A system and Full profile answers on sampled systems |
| A6 | Excel Summary states that tier values are implementation levels (Tier-aligned). Column names stay unchanged because the Gap Analysis reads them |
| A3 | Moved to M3 with the Evidence Register |
| Checks | All checks pass except acceptance 6b (known, unchanged). Migration tests still pass. EN and TH strings complete |

## 22. M3 Build Results (23 October 2026)

| Item | Result |
|---|---|
| Version | App 2.0.0-m3, schema `csf-ig/4`; new keys `ev`, `drill`, `rules.link`, and per Subcategory `st` and `path` are optional, so M1 and M2 files open unchanged |
| Navigation | Evidence stage: Evidence Register, Requests. Summary stage: Rate, Category tiers, Dashboard |
| Evidence Register (A3) | `EV-<initials>-<number>` records with kind, title, client reference, record date, received date, provider, confidentiality, and links to Subcategories, documents, technical checks, observations, and systems. Linked from each Subcategory and each document. Marking a request Received creates a linked record. After cut-off records are flagged and do not count |
| Evidence rules | With the link rule on, Documented or Demonstrated without a matching linked record counts as Tier 1 and shows "Evidence link missing". Tier 3 or higher on Documented without a Record or System export from the last 12 months shows "No current-cycle record". Older files open with the link rule off and a notice, so their ratings do not change |
| Statements and conflicts | Per Subcategory: person, answer (Yes, Partly, No, Unknown), statement. Conflict when answers differ or contradict a technical check. Interview list marker C and filter |
| Adaptive depth | Per Category: drill-down when a mandate tag applies, the scale is Large, the assessor chooses it, or screening found some practice; batch allowed when screening found no practice. Batch rating fills unrated Subcategories at Tier 0 or 1, evidence Stated, one reason. Each Subcategory records its rating path: Drill-down, Batch, or Document only |
| Capture and Rate | In Fieldwork the rating block is collapsed ("Rate now", optional). Summary > Rate shows one Category with statements, evidence, checks, coverage, conflicts, mandate tags, and tier controls |
| Document review depth | Quick (5 control checks) or Full (all checks). Defaults: Small all Quick; Medium Full for Required; Large Full for Required and Essential. Override per document |
| Merge | Setup > Merge session file. People, systems, vendors, departments, team, evidence, observations, obligations, and environment rows match by name or ID; references to people and systems are remapped; statements are combined; every field that differs is listed for the lead to choose |
| Excel | New sheets Evidence Register and Statements; Subcategories add rating path, statements, conflict, evidence link missing, and current-cycle columns; Evidence reference lists the linked Evidence IDs |
| Tests | Sample tiers unchanged with the link rule on; evidence rules, cut-off, conflict, depth, batch, review depth, request-to-evidence, merge with remap: 14 of 14 pass. Migration tests pass. `run_checks.py`: all pass except acceptance 6b (known) |
| Known limits | An observation added by merge gets a new number, so an Evidence link to its old OBS ID must be updated by hand |

## 23. M4 Build Results (23 October 2026)

| Item | Result |
|---|---|
| Version | App 2.0.0-m4, schema `csf-ig/4`; new optional keys `pre`, `sched`, `prep`, `sa`, `land`, and `setup.anonX`, so M1 to M3 files open unchanged |
| Navigation | Prepare stage: Interview plan, Initial request, Schedule, Emails, Self-assessment, AI prompts. Summary stage adds Landscape facts |
| Initial request (11.1) | In-scope Required and Essential documents plus 25 standard technical evidence items (`techev.py`, TE-01 to TE-25), each shown only when a linked technical check is active. The assessor unticks items, then presses "Use this list"; items then appear on Requests with owner role and type. Excel export for the client |
| Schedule (11.2) | Small: 4 combined sessions. Medium: one row per session. Large: sessions S2, S6, and S9 split by site when there are two or more sites. Date, time, and place feed the emails. Excel export |
| Emails (11.3) | C1 to C8 in EN and TH (`comms.py`), filled from Setup, schedule, requests, statements, and Landscape facts. Missing fields show `[PLACEHOLDER: field]`. Copy buttons for subject and body |
| Self-assessment (11.4) | Workbook `csf-ig-sa/1`: Instructions, Questions (22 screening questions plus drill-down Subcategories), Systems (Core profile drop-downs), Documents; hidden `_lists` and `_meta`. Protected sheets, only yellow cells editable. Import checks schema and engagement reference, warns when the question set changed, adds answers as client statements (never a Tier), fills only empty Core profile fields, adds new systems, and updates request statuses. Difference report lists answers that disagree with interview statements or the rating |
| AI prompts (11.5) | P-01 to P-05 (`prompts.py`). P-01 uses the client name and public sources only. P-02 to P-05 replace names of the client, people, vendors, sites, and team with aliases and leave Restricted evidence out. Imports for P-01, P-02, P-03, and P-05 check the schema, list each item with a checkbox, restore real names, and apply only selected items. P-04 has no import |
| Landscape facts | Fact list with block and Evidence or record IDs, unknown IDs flagged, lock and unlock. P-05 import is refused while locked |
| Security (Section 14) | Save asks for an optional password: AES-GCM 256-bit with PBKDF2-SHA256 (600,000 iterations), minimum 8 characters. Opening a protected file asks for the password; merge accepts protected session files. Setup has "Do not keep data in this browser" (clears the browser copy) and "Use aliases in the Excel export" |
| Tests | M4 test 31 of 31: request list, schedule by scale, all 16 email variants without unfilled fields, self-assessment export, edit in Excel format (openpyxl), import, wrong engagement refused, difference report, password save and open (short and wrong password refused, state identical after open), alias checks, all four AI imports, locked Landscape, autosave off, alias Excel export, EN and TH render without errors, 390 px width without horizontal scroll. Migration 15 of 15, M3 14 of 14, EN and TH keys complete. `run_checks.py`: all pass except acceptance 6b (known) |
| Moved to M5 | Self-assessment Differences sheet in the Excel deliverable (Section 13.2) and alias map for the handoff JSON |
| Your check | Sample-check the Thai email text (Emails tab, language TH) and the Thai self-assessment instructions |

## 24. M5 Build Results and Freeze (25 October 2026)

| Item | Result |
|---|---|
| Version | App 2.0.0, schema `csf-ig/4`. Frozen |
| Samples | Setup > Load sample offers three fictional examples: Small manufacturer (Siam Precision Parts, scale S, 5 systems, no networked OT), Medium hospital (CMC, scale M), Large bank (Krung Nakhon Bank, scale L, CII, Bank of Thailand option). Each rates all 106 Subcategories, links evidence to every Documented or Demonstrated rating, uses the initial request list, and ends with locked Landscape facts. The CMC sample now rates all 106 Subcategories (it previously left 15 unrated); Gap Analysis checks still pass on its export |
| P1 handoff | Summary > P1 handoff shows the export checks (106 rated or N/A, evidence links, Landscape locked, no open merge, no Target) and notes (open requests, late evidence, cut-off). Export is blocked until all checks pass. Blocks follow Section 13.1, plus technical check results |
| Validator | JSON Schema and `check_handoff.py` in the Gap Analysis method pack, so the next phase can validate any handoff file without the tool |
| Excel | New sheets: Self-assessment Differences and Landscape Facts. Existing sheet and column names unchanged, so Gap Analysis reads the export as before |
| Build | `build_ig.py` no longer imports `build_interview.py` (`build_gap.py` still does) |
| Fixtures | `_Build-Source/fixtures/` holds the CMC `csf-interview/3` and Audit Tracker save files, so the migration test no longer needs `Interview-Assessment.html` |
| Acceptance (Section 16) | `ig_acceptance.py`: 24 of 24 pass. Items 1 to 3 and 9 for each sample, aliased handoff, merge without data loss, self-assessment round trip, four AI imports plus P-04, migration of the fixtures, password round trip, TH and EN completeness, verification log status for all 26 mandate tags |
| Item 10 | `run_checks.py` now runs the acceptance test. All checks pass except Gap acceptance 6b (no sample IMP uses the bought-not-deployed tool TOOL-07). 6b belongs to the Gap Analysis sample data, not to this tool, and stays open for the next phase |
| Open legal items | 7 mandate tags remain "Verify clause" (PDPA-40, CCA-26, HC-HA, BOT-19, PCI-3-4, PCI-6-10, PCI-12) and plan decision D5 is open. The tool shows them as references to verify; they are content checks, not tool defects |
| Your action | You can now delete `Interview-Assessment.html`, `_Build-Source/gap_compact_template.html`, and `00_Master/tmp/`. Keep `build_interview.py` and `interview_template.html`: `build_gap.py` still uses them for `load_data` and shared styles |
| Next phase | Gap Analysis reads `csf-p1-handoff/1` (validated by `check_handoff.py`) and the Workshop export |
