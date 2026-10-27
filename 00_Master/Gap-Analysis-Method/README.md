# Gap Analysis Method Pack

Version 1.4, 17 October 2026. Tier Rubric 1.2. Interview schema `csf-interview/3`. Requires Gap Analysis HTML v1.3 or later (v1.2 reads `csf-gap-analyst/1` to `/4`, v1.1 reads `/3` and older, and v1.0 reads `/2` only). Department interviews (S2C) feed `departmentResults` and `departmentConflicts`.

## 1. Key Message

This pack holds everything the AI steps of Phase 2 Gap Analysis use: one Landscape prompt, one Analyst prompt with six Function context blocks, one Reviewer checklist, one cross-function Reviewer prompt, the calibration anchors, and the JSON schemas. The Gap Analysis HTML fills the prompts, validates every JSON the AI returns, and calculates all numbers itself. Copy this folder into each client project at kickoff and record the version. Do not edit it during an engagement.

## 2. Files

| File | Used at | Purpose |
|---|---|---|
| `prompts/05-landscape-prompt.md` | Stage 0b | Page key messages and block lines for the Current IT Landscape, facts only. Includes the follow-up message |
| `prompts/01-analyst-prompt.md` | Stage 1, steps 1, 3, 6 | Analyst instructions: analysis ladder, Observed and Inferred, seven transformations, six response stages with Target Tier depth, linked Register documents, Landscape rules (Section 9), writing standard. Includes the two follow-up messages |
| `prompts/02-function-context.md` | Stage 1, step 1 | Six blocks (GV, ID, PR, DE, RS, RC): main evidence, typical causes, what to watch, impact, links to flag |
| `prompts/03-reviewer-prompt.md` | Stage 1, step 2 | Checklist C01 to C21, pass or fail, one feedback round |
| `prompts/04-cross-function-reviewer-prompt.md` | Stage 2 | Proposals only: MergeIMP, SystemicRootCause, Calibration, MissingLink, Consistency |
| `calibration-anchors.md` | All AI steps and the assessor | Likelihood anchors L1-a to L5-a and impact rules on the client's Workshop scales |
| `schemas/csf-gap-landscape-facts-1.schema.json` | HTML to Landscape prompt | Landscape facts in blocks B1 to B14, security tools, changes in flight, prior assessments, incident history |
| `schemas/csf-gap-landscape-1.schema.json` | Landscape AI to HTML | Four page key messages and one line per block. Locks when verify is empty |
| `schemas/csf-gap-input-2.schema.json` | HTML to Analyst | Current version. Function input pack built from the Interview export, the Workshop risk criteria, the locked Landscape, and (1.3) the optional `documentRegister` of 142 framework documents |
| `schemas/csf-gap-input-1.schema.json` | HTML to Analyst | Version 1, kept for Gap Analysis HTML v1.0 |
| `schemas/csf-gap-analyst-5.schema.json` | Analyst to HTML | Current version. Version 4 with one change: the IMP key `angle` is now `stage`. |
| `schemas/csf-gap-analyst-4.schema.json` | Analyst to HTML | Version 4, kept so the HTML can still read older outputs. Version 3 plus six response stages (Validate and Sustain added), a status per stage that follows the Target Tier, `documents` and `documentGaps` on each Gap Finding |
| `schemas/csf-gap-analyst-3.schema.json` | Analyst to HTML | Version 3, kept so the HTML can still read older outputs. Version 2 plus `landscapeRefs`, `repeatFinding`, and on each IMP `changeInFlight` and `existingTool` |
| `schemas/csf-gap-analyst-2.schema.json` | Analyst to HTML | Version 2. Gap Findings in four layers (title, statement, supporting facts, consequence), Strengths, Observations, IMPs, verify items. Rejects tiers, scores, bands, and roadmap fields |
| `schemas/csf-gap-analyst-1.schema.json` | Analyst to HTML | Version 1, kept so the HTML can still read older outputs |
| `schemas/csf-gap-review-2.schema.json` | Reviewer to Analyst | Current version. Check results C01 to C21 and verdict (widened in 1.3 to accept C20 and C21) |
| `schemas/csf-gap-review-1.schema.json` | Reviewer to Analyst | Version 1. Its pattern stops at C15, so it rejected C16 results; use version 2 |
| `schemas/csf-gap-decisions-1.schema.json` | HTML to Analyst | Assessor decisions, resolved verify items, comments |
| `schemas/csf-gap-xreview-1.schema.json` | Reviewer 2 to HTML | Cross-function proposals with machine-readable changes |
| `tools/validate.py` | Testing and the HTML import rules | Schema check plus cross-reference and writing-standard rules. Version 4 rules: stage status against the IMP lists, Register document IDs, IMP documents inside the Gap Finding documents. With `--input`, also the Landscape cross-checks and, for an input pack, the Target Tier depth and document status checks |
| `tools/register-ids.json` | Single Register source (v2.0), validate.py | The only source for the core fields of the 142 documents: title, Thai title, hierarchy, type, category, level, trigger, package, wave, track, capability. The Excel register, the Audit Tracker data, and the project Register doc are generated from it by `_Build-Source`. Edit here only |
| `tools/dictionary.json` | All tools | Data Dictionary export from `_Build-Source/dictionary.py`: enums (stage status, stages, levels, packages, waves, tracks, capabilities), ID formats, field names, EN/TH labels. `check_enums.py` reads it |
| `tools/check_enums.py` | Build | Fails when the Dictionary, Register values, schemas, Analyst prompt, validate.py, or the Gap Analysis template disagree |
| `tools/landscape_facts.py` | Stage 0 | Builds `csf-gap-landscape-facts/1` from the Interview Excel export. Reference for the Gap Analysis HTML v1.1 |
| `_Build-Source/parity_landscape.py` | Build | Fails when the Landscape facts built in Python (`landscape_facts.py`) and in the Gap Analysis HTML differ on the CMC sample |
| `examples/` | Testing | CMC outputs that pass the validator: Landscape facts and output, Analyst round 3 (versions 2 and 3), Reviewer round 1, cross-function proposals |

## 3. Flow

```
Stage 0  HTML builds csf-gap-landscape-facts/1
Stage 0b Reviewer chat:  05-landscape-prompt               -> csf-gap-landscape/1 (round 1)
         HTML:           assessor comments, follow-up      -> csf-gap-landscape/1 (round 2)  [LOCK Landscape]
         HTML builds csf-gap-input/2 per Function, with the locked Landscape
Stage 1  Analyst chat:   01-analyst-prompt + 02 block      -> csf-gap-analyst/5 (round 1)
         Reviewer chat:  03-reviewer-prompt                -> csf-gap-review/2
         Analyst chat:   follow-up 1                       -> csf-gap-analyst/5 (round 2)
         HTML:           validate, assessor decides        -> csf-gap-decisions/1
         Analyst chat:   follow-up 2                       -> csf-gap-analyst/5 (round 3)   [LOCK Function]
Stage 2  Reviewer 2 chat: 04-cross-function-reviewer-prompt -> csf-gap-xreview/1
         HTML:           assessor accepts or rejects each   [LOCK Consolidation]
Stage 3  HTML checks every Landscape block is referenced (rule L2), renders the report, exports Gap Register, Strength Register, IMP list
```

## 4. Placeholders the HTML fills

| Placeholder | Source |
|---|---|
| `{{FUNCTION_ID}}`, `{{FUNCTION_NAME}}`, `{{CLIENT_ALIAS}}` | Engagement setup (alias when Anonymize is on) |
| `{{FUNCTION_CONTEXT}}` | The matching block in `02-function-context.md` |
| `{{CALIBRATION_ANCHORS}}` | `calibration-anchors.md` Sections 1 and 2 |
| `{{RISK_CRITERIA_JSON}}` | Workshop risk criteria JSON: likelihoodScale, impactScale, bandThresholds, appetiteBand |
| `{{OUTPUT_SCHEMA}}`, `{{REVIEW_SCHEMA}}`, `{{XREVIEW_SCHEMA}}` | The schema files |
| `{{INPUT_JSON}}` | The Function input pack |
| `{{LANDSCAPE_SCHEMA}}`, `{{LANDSCAPE_FACTS_JSON}}`, `{{ASSESSOR_COMMENTS_JSON}}` | Landscape schema, Landscape facts, assessor comments on the Landscape draft |
| `{{LANDSCAPE_JSON}}` | The locked Landscape (facts and approved key messages), for the cross-function Reviewer |
| `{{ANALYST_DRAFT_JSON}}`, `{{REVIEWER_FEEDBACK_JSON}}`, `{{ASSESSOR_DECISIONS_JSON}}`, `{{LOCKED_FUNCTIONS_JSON}}` | Earlier steps |

## 5. Impact area keys

The Workshop keys are the standard. The HTML maps Interview Excel columns on import.

| Key | Workshop name | Interview Excel column |
|---|---|---|
| ops | Operations | Operations |
| fin | Financial | Financial |
| legal | Legal and regulatory | Legal or regulatory |
| rep | Reputation | Reputation |
| safety | Health and safety | Health and safety |
| data | Personal data | Personal data |

## 6. Evidence ID conventions

| Evidence | Format | Example |
|---|---|---|
| Subcategory record | Subcategory ID | `PR.AA-03` |
| Interview notes | `NOTE:` plus Subcategory ID | `NOTE:PR.AA-01` |
| Technical check | Check ID | `IAM-01` |
| Profile answer | Field ID, colon, system name | `C4:HIS` |
| Sampling result | Control key, colon, system name | `mfa:PACS` |
| Vendor profile answer | Field ID, colon, vendor name | `V4:Sample HIS vendor` |
| Technical observation | Observation ID | `OBS-01` |
| Framework document | Document ID | `PR-STD-001` |
| Environment answer | `ENV:` plus field key | `ENV:seg` |
| Population result across all systems | `POP:` plus field ID | `POP:C4` |
| Quick BIA row | `BIA:` plus system name | `BIA:HIS` |
| Landscape rows | Row ID from the Interview export | `SITE-01`, `TOOL-07`, `HIST-01`, `CHG-01`, `PRIOR-01`, `DCF-01` |
| Department answer (S2C) | Field ID, colon, department | `U2:Finance`, `U9-1:Finance` |
| Engagement context and assessor notes | `ENG:`, `WS:`, or `NOTE:` plus key | `ENG:threat`, `WS:mandates`, `NOTE:B12` |
| Landscape block | Block ID | `B10` |

## 7. Rules that keep the flow one way

1. AI never calculates Tiers, coverage, risk scores, Risk Levels, or priority order. The schema rejects those fields.
2. One Reviewer round per Function. What the Analyst cannot fix becomes a verify item.
3. A Function locks only at round 3 with zero verify items.
4. Reviewer 2 proposes and the assessor decides. Locked content is never edited directly.
5. Any change after a lock needs a reason in the HTML change log.

## 8. Testing

```
pip install jsonschema
python tools/validate.py examples/*.json --input examples/cmc-landscape-facts.json
python tools/landscape_facts.py <interview-export.xlsx> landscape-facts.json
```

All examples must pass, including `examples/cmc-pr-analyst-output-v4.json` (the six-stage PR output, Target Tiers 2 and 3). The Target Tier and document status checks run only with a full input pack (`--input` with `csf-gap-input/2`), which the Gap Analysis HTML builds. The warning about unreferenced Landscape blocks is expected for a single Function. Paste any Analyst output into a file and run the same command before you import it, if the HTML is not at hand.

## 9. Version control

Raise the version for any change to a prompt, anchor, or schema. A schema change that removes or renames a field needs a new schema ID (for example `csf-gap-analyst/2`), and the HTML must keep reading the old one.

## 10. Change log

| Version | Date | Change |
|---|---|---|
| 1.4 | 17 October 2026 | Plan W0-3: Improvement Action key `angle` renamed to `stage` in new schema `csf-gap-analyst/5` (README Section 9 requires a new ID for a renamed field). Analyst prompt and Reviewer check C08 use `stage`. The HTML and `tools/validate.py` read `/4` and older outputs with `angle` unchanged. New example `examples/cmc-pr-analyst-output-v5.json` |
| 1.3 | 17 October 2026 | Six response stages: Validate and Sustain added to Fix, Find, Prevent, and Handle exceptions. Status per stage (Required, In place, Not applicable, Beyond Target Tier) follows the Target Tier of the Category: Target 2 ends at Validate, Target 3 and 4 need Sustain. Documents linked at Gap Finding level from the Register only, with `documentGaps` for needs the Register does not cover. New schema `csf-gap-analyst/4`; `csf-gap-input/2` gains optional `documentRegister`; `csf-gap-review/2` widened to C21. Analyst prompt Section 8, Reviewer checks C08, C20, C21, Function context lines for Validate and Sustain. `validate.py` v4 rules and `register-ids.json`. The label "band" becomes "Risk Level" in prose (JSON keys unchanged). Built into Gap Analysis HTML and Compact v1.2 |
| 1.2 | 17 October 2026 | Department interviews (S2C): `departmentResults` per Subcategory and `departmentConflicts` (DCF IDs) in the Landscape facts; Analyst Section 9 and Reviewer C17 cover them. Facts tool reads code columns, so Thai exports work. Built into Gap Analysis HTML v1.1 |
| 1.2 | 17 October 2026 | Current IT Landscape: prompt `05`, schemas `csf-gap-landscape-facts/1`, `csf-gap-landscape/1`, `csf-gap-input/2`, `csf-gap-analyst/3`, `csf-gap-review/2`. Analyst prompt Section 9 (Landscape rules), Reviewer checks C17 to C19, calibration rule 6, Landscape line in each Function block, cross-function Landscape consistency. `tools/landscape_facts.py`. Fixes the review schema pattern that rejected C16 |
| 1.1 | 16 October 2026 | Gap Findings split into four layers: `title`, `statement`, `supportingFacts`, `consequence` (schema `csf-gap-analyst/2`). Analyst prompt Section 5 and Reviewer check C16 added. HTML still reads `csf-gap-analyst/1` |
| 1.0 | 16 October 2026 | First release |
