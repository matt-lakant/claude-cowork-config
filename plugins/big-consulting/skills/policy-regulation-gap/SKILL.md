---
name: policy-regulation-gap
description: Extracts obligations from a regulation, standard, or contract requirement and maps each to the company's policies, procedures, and controls, rating coverage and drafting fixes. Use when the user attaches a regulation or standard and their policies and asks where they fall short, what a new rule requires, or how to prepare for an exam or certification.
---

# Policy Gap Analyzer

## What this produces
An obligations register, a coverage map to current policies and controls, and a prioritized gap list with draft policy language.

## Inputs to ask for
- The full text of the regulation or standard (PDF or pasted), and which sections apply
- Current policies and procedures (attach documents)
- Control list, if one exists
- The company's jurisdiction, industry, and size, for applicability
- If only a summary of the regulation is available, say that obligations may be missed and ask for the source text

## Method
1. Extract every obligation: each "shall," "must," or required outcome becomes one row, quoted verbatim with its section reference as it appears in the source.
2. Classify each: governance, policy, process, technical, documentation, reporting, or training.
3. Mark applicability and any exemption thresholds stated in the text.
4. Map each obligation to the policy clause, procedure step, and control that satisfies it.
5. Rate coverage: covered, partial (exists but misses scope, frequency, or evidence), or gap.
6. Prioritize gaps by enforcement exposure, effective date, and effort.
7. Draft policy language for each gap in the company's existing policy style.

## Output format
- Obligations register: ID | Section | Obligation (quoted) | Type | Applies (Y/N)
- Coverage map: Obligation ID | Policy clause | Procedure | Control | Rating | Note
- Gap list: Priority | Obligation | Gap | Fix | Owner | Effective date
- Draft policy language, grouped by policy

## Quality checks
- Every section reference comes from the supplied text; none is added from memory
- Partial ratings say exactly what is missing
- Applicability decisions are explained
- The output states it is not legal advice and flags items for counsel

## Notes from the source article
- **Replaces:** The regulatory gap assessment: lawyers and consultants reading a new rule line by line and mapping each obligation to policies and controls.
- **Example request:** “Here’s the new state privacy law and our current privacy policy and data retention procedure. Show me every obligation we don’t meet yet.”
- **What the user still owns:** Interpreting ambiguous requirements with counsel and deciding how much compliance risk the business carries.
- When handing the deliverable back, name in one line the decision above that stays with the user.
