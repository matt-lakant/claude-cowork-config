---
name: jobs-to-be-done-mapper
description: Maps the job a customer is trying to get done into steps and measurable outcome statements, then scores which outcomes are underserved. Use when the user wants to find unmet customer needs, design a new offer or feature, or understand why customers switch, and has interviews, support data, or survey results about how customers work.
---

# Jobs-to-Be-Done Mapper

## What this produces
A job map, 30 to 60 outcome statements, an opportunity ranking, and a survey draft if scores do not yet exist.

## Inputs to ask for
- The customer (a specific role, not a company) and the core functional job, stated as verb + object (for example, "reconcile vendor invoices").
- Interview notes, support tickets, reviews, or observation notes describing how the job gets done today.
- Any survey data rating importance and satisfaction. If none, mark scores as pending.

## Method
1. State the core functional job with no solution in it; list emotional and social jobs separately.
2. Break the job into the universal steps from Bettencourt and Ulwick's job map: define, locate, prepare, confirm, execute, monitor, modify, conclude. Drop steps that do not apply; do not invent content to fill them.
3. For each step, write outcome statements in the form: direction (minimize) + metric (time, likelihood, number) + object + clarifier. Example: "Minimize the time it takes to match an invoice to its purchase order."
4. If survey data exists, score each outcome: opportunity = importance + max(importance minus satisfaction, 0), both on a 0 to 10 scale. Above 12 is a strong opportunity; 10 to 12 is worth pursuing; below 10 is served or overserved.
5. If no data exists, draft the survey: importance and satisfaction per outcome on 5-point scales, 150+ respondents per segment. Convert each to the 0 to 10 scale used in step 4 as the share of respondents answering 4 or 5, multiplied by 10.
6. Flag overserved outcomes (high satisfaction, low importance) as places to simplify or cut cost.

## Output format
1. Job statement (core, emotional, social).
2. Job map table: Step | What the customer does | Outcome statements.
3. Opportunity ranking: Outcome | Step | Importance | Satisfaction | Score | Verdict.
4. Survey draft (only if scores are pending).

## Quality checks
- No outcome statement mentions a product, feature, or technology.
- Every outcome uses the direction + metric + object form.
- Scores trace to survey data; none are estimated from interviews.

## Notes from the source article
- **Replaces:** An outcome-mapping workshop: consultants break the customer’s job into steps, write dozens of outcome statements, and survey to find the underserved ones.
- **Example request:** “Our buyers are AP managers trying to close the month faster. Here are 12 interview notes and 400 support tickets. Map the job and show me where they are underserved.”
- **What the user still owns:** Which underserved outcome you build against. The score shows where need is greatest; your capabilities and economics decide where you can actually win.
- When handing the deliverable back, name in one line the decision above that stays with the user.
