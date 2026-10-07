---
name: privacy-impact-assessment
description: Conducts a privacy impact assessment (or GDPR data protection impact assessment) for a new system, vendor, or data use: maps data flows, tests against privacy principles, rates risk to individuals, and lists mitigations. Use when the user is launching a product, onboarding a vendor that handles personal data, starting a new AI or analytics use of personal data, or needs a PIA or DPIA.
---

# Privacy Impact Assessment

## What this produces
A data flow inventory, a principle-by-principle assessment, a risk register for affected individuals, and a mitigation plan with a go or no-go recommendation.

## Inputs to ask for
- Project description and business purpose
- Data elements collected, sources, and whose data (customers, employees, children, patients)
- Systems, vendors, storage locations, and cross-border transfers
- Retention periods and deletion method
- Applicable laws the company is subject to
- Current privacy notice
- If data elements are unknown, request a sample record or schema

## Method
1. Map the data lifecycle: collect, use, share, store, delete. Name every system and recipient.
2. Flag sensitive categories (health, biometric, financial, location, children, government ID).
3. Test each principle: lawful basis or notice, purpose limitation, data minimization (is every field needed?), accuracy, retention, security, individual rights (access, deletion, correction, opt-out), and transfers.
4. Rate risk to individuals by likelihood and severity of harm: discrimination, financial loss, exposure, loss of control.
5. Propose mitigations: drop fields, pseudonymize, shorten retention, restrict access, update notice.
6. Rate residual risk. High residual risk may need consultation with the regulator under some laws; flag it for counsel.

## Output format
- Data inventory: Element | Source | Sensitive (Y/N) | Purpose | Systems | Recipients | Retention
- Principle assessment: Principle | Finding | Risk rating
- Risk and mitigation: Risk | Likelihood | Severity | Mitigation | Owner | Residual
- Recommendation: proceed, proceed with conditions, or stop

## Quality checks
- Every data element has a stated purpose, or is recommended for removal
- Transfers name destination and mechanism
- Retention is a period, not "as needed"
- Legal conclusions are flagged for counsel review

## Notes from the source article
- **Replaces:** The privacy assessment run before a new system or data use goes live: data mapping, risk rating, mitigations.
- **Example request:** “We want to feed call recordings into a vendor’s AI to score agent quality. Here’s the vendor DPA and our data schema. Do the privacy impact assessment.”
- **What the user still owns:** Whether the use is right for your customers and employees even where it is legal.
- When handing the deliverable back, name in one line the decision above that stays with the user.
