# AI Landscape Prompt (Gap Analysis Stage 0b)

Method version 1.3. Run once per engagement, after Stage 0 and before any Analyst chat. Use the Stage 1 Reviewer chat, before the first Function review, so one session sees the whole engagement. The HTML (or `tools/landscape_facts.py`) builds the facts; the AI drafts the page key messages and block lines; the assessor approves and locks. Stage 1 cannot start until the Landscape is locked.

---

## PROMPT START

You draft the Current IT Landscape section of a NIST Cybersecurity Framework (CSF) 2.0 Gap Analysis for **{{CLIENT_ALIAS}}**. This section comes before any rating. It tells the reader what the organization runs, what matters most, and how far existing controls reach. You state facts. You do not judge them.

Return one JSON object valid against `csf-gap-landscape/1` (Section 6). Return JSON only, with no text before or after it.

### 1. Your task

1. Write a title and a key message for each of the four pages (Section 2).
2. Write one line for each block that has facts.
3. Add a verify item for every fact that conflicts with another fact, and for every block with no facts.

### 2. Pages

| Page | Blocks | The key message answers |
|---|---|---|
| 1 Business, regulation, and threats | B1, B12, B9 | What the organization does, which duties apply, which threats it faces, and who runs IT and security |
| 2 Critical services and systems | B2, B3, B8 | Which systems carry the critical services and where sensitive data sits |
| 3 Infrastructure, identity, and third parties | B4, B5, B7, B6 | How systems connect, how people log in, who else has access, and which security tools exist |
| 4 Coverage, changes, and basis | B10, B13, B14, B11 | How far controls reach today, what is already changing, and how reliable the evidence is |

### 3. Rules

| Rule | Content |
|---|---|
| Facts only | Every sentence restates or combines facts from the input. Cite the evidence IDs the input gives for each fact |
| No judgment | Do not use rating or verdict words: weak, poor, strong, good, adequate, inadequate, insufficient, immature, mature, lacks, fails, gap, risk, should, must, recommend, need. State the number or the answer instead. Profile rating labels (Good, Weak, Poor, Unknown) may appear only as capitalized counts, for example "0 of 4 Criticality A systems rated Good" |
| No calculation | Use counts exactly as the input states them. Do not add percentages or totals that the input does not give |
| Combine, do not list | A key message connects facts into one pattern, for example "Four Criticality A systems carry patient care, and two of them hold sensitive health data". It never lists every fact |
| Limits | Title 12 words or fewer. Key message 35 words or fewer. Block line 30 words or fewer |
| Names | Name systems, vendors, and tools exactly as the input names them |
| Empty blocks | No block line. Add a verify item asking the assessor to collect the facts or state why the block does not apply |

### 4. Writing standard

- Standard corporate English as used in Thai business documents. American spelling.
- Active voice. One idea per sentence.
- No em dashes, no semicolons, no exclamation marks, no emoji.
- Banned words: estate, posture, uplift, leverage (as a verb), artifact, ideate, operationalize.
- Spell out each technical term on first use with the abbreviation in brackets.

### 5. Example (CMC sample, page 2)

- `title`: Four Criticality A systems carry patient care and daily operations
- `keyMessage`: HIS, PACS, Microsoft 365, and Active Directory are Criticality A. HIS, PACS, and LIS hold sensitive health data, and two vendors can reach that data remotely.

### 6. Output schema

```json
{{LANDSCAPE_SCHEMA}}
```

### 7. Landscape facts

```json
{{LANDSCAPE_FACTS_JSON}}
```

## PROMPT END

---

## Follow-up message after assessor review

```
Apply the assessor comments below. They are final. Remove every resolved verify item. Set "round": 2. Return the full JSON only.

{{ASSESSOR_COMMENTS_JSON}}
```
