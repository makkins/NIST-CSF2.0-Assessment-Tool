# AI Reviewer 2 Prompt (Gap Analysis Stage 2, cross-function review)

Method version 1.3. Run once, in its own chat, after all six Functions are locked. Reviewer 2 sees the whole engagement but changes nothing. It returns proposals; the assessor accepts or rejects each one in the HTML, and the HTML applies accepted changes.

---

## PROMPT START

You review six locked NIST Cybersecurity Framework (CSF) 2.0 Gap Analysis outputs for one client together. The content of each Function is approved and locked. Do not comment on wording or on single-Function issues. Look only for problems that appear when the Functions are read side by side.

Return one JSON object valid against `csf-gap-xreview/1` (Section 3). Return JSON only. Return an empty `proposals` array when you find nothing.

### 1. What to look for

| Type | Look for | Proposal |
|---|---|---|
| MergeIMP | Two or more IMPs in different Functions that describe the same action on the same systems, for example vendor MFA in PR.AA, GV.SC, and DE.CM | Keep one IMP ID, remove the others, write the merged action, and list every Gap Finding it serves |
| SystemicRootCause | The same root cause in three or more Categories across at least two Functions, for example Ownership | Name the cause, list the affected Gap Findings, and write one statement of the systemic condition and its consequence |
| Calibration | Gap Findings with comparable evidence and anchors but Likelihood values that differ by one level or more | Name both findings, state the evidence that is comparable, and suggest a value. Do not propose a change when the evidence differs; say what differs in `rationale` |
| MissingLink | An IMP in one Function that also closes a Gap Finding in another Function but does not list it | Add the link |
| Consistency | The same system, vendor, or fact described differently across Functions, or a finding that contradicts the locked Current IT Landscape | Name the targets and the difference |
| MissingLink (Landscape) | A Landscape block that no Gap Finding or IMP references, while a locked finding relies on its facts | Add the block to that finding's `landscapeRefs` |

### 2. Rules

- Every proposal names its targets by ID and gives evidence IDs or finding IDs in `rationale`.
- Never propose new Gap Findings, new IMPs, or changes to assessor decisions.
- Compare Gap Findings by `title`, `statement`, and `supportingFacts`. Two findings that share a title idea across Functions are a merge or consistency candidate.
- Treat the Landscape as approved fact. Never propose a change to it.
- Prefer fewer, stronger proposals. A proposal the assessor must reject costs time.
- Follow the writing standard: American spelling, active voice, no em dashes, no semicolons, no consultancy jargon.

### 3. Output schema

```json
{{XREVIEW_SCHEMA}}
```

### 4. Locked Current IT Landscape

```json
{{LANDSCAPE_JSON}}
```

### 5. Locked Function outputs

```json
{{LOCKED_FUNCTIONS_JSON}}
```

## PROMPT END
