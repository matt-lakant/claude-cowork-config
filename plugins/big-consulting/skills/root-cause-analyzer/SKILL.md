---
name: root-cause-analyzer
description: Finds and verifies the root cause of a recurring operational problem using a sharp problem statement, Pareto stratification, an Ishikawa fishbone, and 5 whys tested against data and observation. Use when a defect, delay, complaint, or error keeps recurring, when past fixes did not hold, or when the user needs a root cause write-up for leadership or an audit.
---

# Root Cause Analyzer

## What this produces
A verified root cause statement with the evidence chain, rejected causes, and countermeasures that address the cause directly.

## Inputs to ask for
- The problem and when it started
- Defect or incident data (CSV with date, type, location, shift, product)
- Observation notes from where the problem occurs
- Past fixes tried and what happened
If there is no data, build the analysis and list the data needed to verify each cause.

## Method
1. Write the problem statement: what, where, when, how much, against what standard. No cause or solution inside it.
2. Stratify the data by type, shift, site, product, and customer. Pareto to find the few categories driving most of the volume.
3. Build the fishbone for the top category: methods, machines and systems, materials and inputs, people, measurement, environment. Draw candidates from observation first.
4. Run 5 whys down the likeliest branches. Stop at a cause the organization controls.
5. Verify each candidate: does it appear when the problem appears and disappear when it does not? Mark verified, refuted, or untested.
6. Reject "human error" and "needs training" as final answers. Ask why the process made the error easy.
7. Match countermeasures to the verified cause, favoring error-proofing over inspection or reminders.

## Output format
- Problem statement
- Pareto table: Category | Count | Share | Cumulative share
- Fishbone as a table: Category | Candidate cause | Source | Status
- 5 whys chain for each verified cause
- Countermeasures: Cause | Countermeasure | Type (error-proof, standardize, detect) | Owner | Check date

## Quality checks
- The problem statement is measurable and solution-free
- Every root cause is verified with evidence
- No final cause is a person
- Each countermeasure has a date to confirm the problem dropped

## Notes from the source article
- **Replaces:** The problem-solving session after a recurring failure: a whiteboard fishbone and five whys that end when someone says “training.”
- **Example request:** “Billing errors on our field service invoices have run at 8% for a year despite two retraining rounds. Here’s the error log. Find the real root cause.”
- **What the user still owns:** Accepting a root cause that points at a policy, a system, or a leadership decision, and funding the fix when it is not cheap.
- When handing the deliverable back, name in one line the decision above that stays with the user.
