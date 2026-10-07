---
name: third-party-risk-assessor
description: Tiers a vendor by inherent risk, reviews its due diligence evidence (questionnaire, SOC 2 report, financials, contract), and produces a residual risk rating with required remediations. Use when the user is onboarding a supplier, renewing a critical vendor, reviewing a SOC report, or building a vendor risk tiering model.
---

# Third-Party Risk Assessor

## What this produces
An inherent risk tier, a findings list from the evidence, a residual risk rating, and a remediation and monitoring plan for one vendor.

## Inputs to ask for
- What the vendor does, data it touches, systems it connects to, annual spend
- Security questionnaire responses
- SOC 2 Type II or ISO 27001 certificate and report (attach PDF)
- Financial statements or credit report, if available
- The draft or current contract
- If no SOC report exists, list compensating evidence to request

## Method
1. Tier inherent risk on: data sensitivity, system access, operational criticality (what stops if they fail), regulatory relevance, geography, substitutability, and spend. Tier 1 (critical) to Tier 3 (low).
2. Scale diligence to tier. Tier 3 gets a short questionnaire; Tier 1 gets full evidence review.
3. Read the SOC report: period covered, scope, subservice organizations carved out, exceptions noted, complementary user entity controls the company must operate. If the report period ended more than about three months ago, request a bridge (gap) letter covering the time since; a report whose period ended over a year ago is stale, so ask for the current one.
4. Check the questionnaire against the report for contradictions.
5. Review financial health and concentration: are you dependent on one supplier with no fallback?
6. Check contract protections: security obligations, breach notice timing, audit rights, subcontractor approval, data return, exit assistance.
7. Rate residual risk and set remediations with dates and monitoring frequency by tier.

## Output format
- Tier rationale table: Factor | Rating | Basis
- Findings: Area | Finding | Evidence | Severity
- Residual rating with a two-sentence rationale
- Remediation plan and monitoring schedule

## Quality checks
- SOC exceptions and carve-outs are all listed
- User entity controls are assigned to an internal owner
- Every finding cites the document and page
- Residual rating reflects findings, not vendor reputation

## Notes from the source article
- **Replaces:** The vendor risk program team that tiers suppliers, sends questionnaires, reads SOC reports, and writes a risk rating for each vendor.
- **Example request:** “We’re signing a new payroll provider. Here’s their SOC 2, their security questionnaire, and the draft MSA. Assess them.”
- **What the user still owns:** Accepting a vendor with open findings when the business needs them live next month.
- When handing the deliverable back, name in one line the decision above that stays with the user.
