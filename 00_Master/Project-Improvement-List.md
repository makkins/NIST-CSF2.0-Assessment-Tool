# Project Improvement List: NIST CSF 2.0 Document Framework

Last updated: 10 October 2026

## Key Message

The implementation guidance layer (build order, waves, capability flags, sourcing, prerequisite activities, ISO/IEC 27002 themes, and tags) now lives in the master files only: the Document Map HTML, the Audit Tracker HTML, the Excel register, the Framework Summary, and the Tailoring Guide. The 426 individual .docx files do not carry it yet. Item 1 closes that gap; the other items extend the pack when there is time.

## Current State (version 1.1)

| Area | Status |
|---|---|
| 426 document files (Template TH, Template EN, CMC EN) | Done; Part A, Part B, revision history, no guidance layer |
| Document Map HTML (7 views, TH/EN, Help) | Done |
| Audit Tracker HTML (offline, Excel export, JSON save) | Done |
| Excel register with Implementation Roadmap, Prerequisite Activities, Process Flows sheets | Done |
| Framework Summary and Tailoring Guide (TH/EN) with build order and capability sections | Done |
| Build source (scripts, content, templates) | `_Build-Source` folder next to `00_Master` |

## Backlog

| No. | Improvement | Why it matters | Priority | Effort | Notes |
|---|---|---|---|---|---|
| 1 | Add an "Implementation Guidance" box to the Document Profile of all 426 .docx files: wave, track, build order, capability flag with reasons, sourcing options, prerequisite activities with agenda, dependencies, ISO/IEC 27002 theme, and tags | Clients who receive only the Word files lose the build order and staffing message | High | Medium: regenerate from the existing data, then re-run QA and re-copy 426 files to the Desktop | Deferred by decision on 10 October 2026. Reuse `ENRICH` in `build.py render()` |
| 2 | Activity templates as documents: meeting agenda and minutes templates for each of the 29 activities, a BIA questionnaire, risk appetite scenario cards, and a tabletop scenario pack | Organizations that have never run these meetings need ready-to-use material, not just an agenda | High | Medium | Store as a new folder, for example `04_Activity_Kits` |
| 3 | Effort and cost estimate per document (person-days by capability level) and a staffing calculator in the Audit Tracker | Turns the capability gap into a costed business case for an FTE or outsourcing decision | High | Medium | Needs calibration from real engagements |
| 4 | CMC-specific recommended order: apply the hospital profile (OT and medical devices earlier, CII duties, MSSP) and show it as a separate view or tracker sample | Keeps the case company consistent across the course modules | Medium | Low | Notes already exist for PR-STD-015, GV-POL-005, DE-GDL-001 |
| 5 | Sector overlays as tracker profiles: Bank of Thailand, SEC, OIC, and manufacturing (IEC 62443) additions | Required documents differ by regulator; the current tracker covers CII, PDPA, CCA, and ISO only | Medium | Medium | Mark every regulator reference [VERIFY] until confirmed |
| 6 | Maturity scoring (0 to 5) per document and CSF subcategory scoring in the tracker | Links document evidence to CSF Tier and Target Profile work | Medium | Medium | Option deferred when the two-level scale was chosen |
| 7 | Audit report generator: export the tracker result as a Word report with key message, findings by Function, and the gap roadmap | Saves manual report writing after each assessment | Medium | Medium | Follow the house deliverable standard (Pyramid Principle, American spelling) |
| 8 | Hosted team version of the tracker with shared storage and comments | Lets several assessors work on one client at once | Low | Medium | Client data would be stored on claude.ai; agree with the client first |
| 9 | Open the matching .docx from the Document Map (relative links in the Desktop copy) | Faster navigation from the map to the template | Low | Low | Works only in the offline copy, not the published page |
| 10 | Practitioner review of capability flags, sourcing, and activity durations | These are author judgment, not NIST or ISO requirements | Medium | Low | Ask two or three senior peers to challenge the flags |
| 11 | Re-verify the 21 documents with [VERIFY] items against current Thai notifications (CII, PDPC, sector regulators) | Thai notifications change often | High before client use | Low | Track in the Verify List sheet |
| 12 | Version control: keep the build scripts and outputs in a Git repository with a change log | Makes future updates traceable and repeatable | Low | Low | |

## How to Run an Update

1. Work in a copy of the `_Build-Source` folder (Python 3 with python-docx and openpyxl). Edit the data: `meta.py` (document list), `content/c_*.py` (document content), `enrich.py` and `enrich_activities.py` (guidance layer).
2. Rebuild: `build.py` (426 .docx), `master.py` (Excel and summary documents), `build_data.py` then `build_html.py` (two HTML pages).
3. Check: `qa.py` and `qa2.py` (writing standard), Excel recalculation, and a browser test of both HTML pages.
4. Deliver: copy to the Desktop folder and update the Project document `claude/csf-document-framework-register.md`.
