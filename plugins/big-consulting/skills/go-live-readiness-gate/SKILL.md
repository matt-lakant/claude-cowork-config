---
name: go-live-readiness-gate
description: Runs a go/no-go readiness assessment for a system or process launch across solution, data, people, process, technology, support, business sign-off, and rollback, with thresholds set before results are read. Use when a go-live is weeks away, when preparing a go/no-go meeting, or when a team insists it is ready. This skill judges readiness; building the cutover runbook is a separate job.
---

# Go-Live Readiness Gate

## What this produces
A gate scorecard with evidence, a go, go-with-conditions, or no-go recommendation, the conditions attached, and the rollback trigger.

## Inputs to ask for
- Test results: pass rates, open defects by severity
- Data migration reconciliation: record counts and financial balances, source against target
- Training completion by role; named super-users
- Cutover plan, hypercare staffing, support escalation path
- Business process owner sign-offs; rollback plan and when it was last rehearsed
If a dimension has no evidence, score it not ready.

## Method
1. Set criteria and thresholds before reading results. Mark each must-have or should-have.
2. Default must-haves: zero open severity-1 defects; severity-2 within an agreed count with workarounds; migrated balances tie to source; training at or above 90% for affected roles; rollback rehearsed; process owner sign-offs.
3. Score each criterion met, partly met, or not met, citing the evidence document.
4. Decision logic: any must-have not met means no-go, unless the sponsor accepts a named risk in writing, which makes it go-with-conditions.
5. Define the rollback trigger: the observable condition and the latest time a rollback decision can be made.
6. For a no-go or conditional result, set the re-gate: which criteria must reach met, by what date, before a second vote.

## Output format
- Scorecard: Dimension | Criterion | Must or should | Threshold | Actual | Evidence | Status
- Recommendation with reasons in three lines
- Conditions: Condition | Owner | Due
- Rollback trigger and decision deadline
- Re-gate criteria and date

## Quality checks
- Thresholds were written before results were scored
- Every status cites evidence
- Sign-offs are named people
- The rollback plan has a trigger and a deadline

## Notes from the source article
- **Replaces:** The go/no-go assessment before a major launch: readiness checklists across testing, data, training, and support rolled into a recommendation for the steering committee.
- **Example request:** “We go live on the new order-management system in 12 days. Here are the test results, migration reconciliation, and training report. Are we ready?”
- **What the user still owns:** Saying no-go when the date has been announced. The gate gives you the evidence; the courage is still yours.
- When handing the deliverable back, name in one line the decision above that stays with the user.
