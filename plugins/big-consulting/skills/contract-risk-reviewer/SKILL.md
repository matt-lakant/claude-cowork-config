---
name: contract-risk-reviewer
description: Reviews a commercial contract clause by clause against a negotiation playbook, rates each clause's risk, and proposes redlines and fallback positions. Use when the user attaches an MSA, SaaS agreement, supply agreement, NDA, or SOW and asks what is risky, what to push back on, or whether it is ready to sign.
---

# Contract Risk Reviewer

## What this produces
A clause risk table, a prioritized list of issues to negotiate with proposed redlines, and a short summary for the business owner.

## Inputs to ask for
- The contract (DOCX or PDF), including all exhibits and order forms
- Which side the company is on (buyer or seller)
- The company's contract playbook or standard positions, if any
- Deal value, term, and how critical the service is
- If no playbook exists, use common market positions and label them as such

## Method
1. Read the whole agreement, including exhibits and documents incorporated by reference. Note conflicts between them and the order of precedence.
2. Review core risk clauses: limitation of liability (cap, carve-outs), indemnification, IP ownership, confidentiality, data protection, warranties, service levels and credits, price increases, renewal and termination, assignment and change of control, governing law, insurance, audit rights, exclusivity.
3. Compare each clause to the playbook: standard, acceptable fallback, or escalate.
4. Rate risk by exposure in dollars and likelihood of it mattering for this deal.
5. Draft redlines for escalated clauses with the reason in one sentence and a fallback.
6. Note what is missing that should be there.

## Output format
- Summary: five lines, sign or negotiate, top three issues
- Clause table: Section | Clause | What it says | Position vs playbook | Risk (H/M/L) | Proposed change
- Redlines with rationale and fallback
- Missing clauses list

## Quality checks
- Every section reference matches the document
- Liability cap is stated in dollars for this deal
- Auto-renewal and notice dates are called out
- Output states it is a first-pass review and not legal advice

## Notes from the source article
- **Replaces:** The first-pass review of each third-party agreement against the company’s negotiating playbook.
- **Example request:** “Here’s the MSA from our new logistics provider. We’re the customer, USD 2M a year, three-year term. What do I push back on?”
- **What the user still owns:** The final call on risk you accept to close the deal, and a lawyer’s sign-off where the stakes warrant it.
- When handing the deliverable back, name in one line the decision above that stays with the user.
