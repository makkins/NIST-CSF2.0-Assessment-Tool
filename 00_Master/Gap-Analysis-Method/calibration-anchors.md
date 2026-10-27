# Calibration Anchors for Likelihood and Impact

Method version 1.3. Used by the AI Analyst, the AI Reviewer, and the assessor. The level definitions belong to the client: they come from the Workshop risk criteria JSON (`likelihoodScale`, `impactScale`). The anchors below translate assessment evidence into those levels so that six separate Analyst sessions rate the same evidence the same way.

## 1. Likelihood anchors

Workshop level text is shown first. The anchors are practitioner judgment, not NIST text.

| Level | Workshop definition (default) | Anchor | Evidence pattern |
|---|---|---|---|
| 5 Very High | Expected within months, or already occurring | L5-a | Signs of compromise or active exploitation. Route to the Incident path, not to the Gap Analysis. Use L5 for a gap only when the same weakness is being exploited at peer organizations right now and the client is exposed in the same way |
| 4 High | Expected within a year. Controls are weak and the threat is active | L4-a | Control rated Poor or Unknown on one or more Criticality A systems, and an exposure path exists (internet-facing, vendor remote access, email or phishing, flat network), and the threat is active in the sector (peer incident, known ransomware tactic) |
| | | L4-b | Control absent across the organization (no practice, Tier 0 or 1) where the threat needs no special skill, for example no MFA on remote access or no offline backup |
| 3 Moderate | Could occur within one to two years. Similar events seen in the industry | L3-a | Control Weak or Partial on Criticality A systems, or Poor only on Criticality B or C systems |
| | | L3-b | Inferred gap with High confidence, where the extent is not yet confirmed (one level below the Observed equivalent) |
| | | L3-c | Governance or process gap that removes a safeguard but needs a second failure before harm, for example no access review |
| 2 Low | Could occur within five years. Controls are mostly effective | L2-a | Coverage Largely, residual gaps on non-critical systems, or a compensating control is confirmed |
| | | L2-b | Evidence gap only: practice is described but records are missing |
| 1 Very Low | Not expected within five years. Strong controls are in place | L1-a | Coverage Full with Documented or Demonstrated evidence. Only a theoretical path remains |

Rules:

1. Pick the highest anchor that the evidence fully meets. Cite the anchor ID and the evidence IDs.
2. An Inferred gap sits one level below the Observed equivalent unless confidence is High and the organizational cause is confirmed (then it may equal it). An Inferred gap with Low confidence gets no Likelihood; its only response is a Find action.
3. "Unknown" on a Criticality A system counts as absent for Likelihood, and the Analyst adds a [VERIFY] item.
4. A Foundation that blocks part of the path lowers Likelihood by at most one level. State which part it blocks.
5. Never use Likelihood to express importance. Importance comes from Impact and the Workshop priority.
6. "The threat is active" in L4-a needs a source: an incident history row (HIST ID) or the threat context recorded in Landscape B12. Without either, use the L3 anchor that fits.

## 2. Impact anchors

Rate each of the six Workshop areas (ops, fin, legal, rep, safety, data) on the Workshop impact scale for the worst credible consequence of this gap.

| Rule | Content |
|---|---|
| Starting point | The highest Quick BIA score of the linked systems in that area. The Interview Quick BIA uses the same 1 to 5 scale |
| Governance gaps without a system | Rate the consequence of the scenario that the gap enables, for example an unmanaged incident on the most critical service |
| Legal | Use 4 when the scenario triggers a mandatory notification or a regulator order (CII reporting, PDPA breach notification). Use 5 only when a license, accreditation, or criminal liability is plausible. Mark Thai legal thresholds [VERIFY] unless the Workshop regulatory verification confirms them |
| Personal data | Count records from the data owner or system profile. Any sensitive health record counts as at least 3 |
| Health and safety | Use only when the system supports patient care, production safety, or physical security |
| Rationale | One sentence per area that names the system, the scenario, and the scale text it matches |
| Not applicable | Set value to null with a short rationale |

## 3. Worked anchors (CMC sample)

| Gap | Likelihood | Why |
|---|---|---|
| No MFA for administrators and vendors on HIS, PACS, Active Directory | 4 (L4-a) | Poor on Criticality A, vendor remote access path, peer hospital ransomware |
| MFA is not a standard control (Inferred, High) | 3 (L3-b) | Extent beyond the sample not yet confirmed |
| No access review in 12 months | 3 (L3-c) | Needs a second failure (a leaver or a compromised account) before harm |
| Physical access records missing | 2 (L2-b) | Evidence gap only |
