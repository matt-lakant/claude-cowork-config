---
name: program-status-report-writer
description: Consolidates workstream updates into one program status report, reconciling conflicting dates, rating RAG by rule, and checking whether last period's commitments were kept. Use when compiling the weekly or biweekly program report, when workstream updates contradict each other, or when status reports stopped telling anyone anything. Steering committee packs are a separate job.
---

# Program Status Report Writer

## What this produces
A one-page program report: headline, workstream RAG and trend, cross-workstream conflicts, and commitments kept.

## Inputs to ask for
- This period's workstream updates and last period's report
- Milestones with baseline and forecast dates; budget plan, actual, and forecast at completion
- Current RAID log and the program's RAG thresholds
If no thresholds exist, use the defaults below and say so.

## Method
1. Normalize every workstream update to one template: done, next, milestones, risks, asks.
2. Reconcile: compare each date a workstream reports with the date others assume for it (data ready in week 12, testing assumes week 10). List every mismatch.
3. Check commitments: what each workstream promised last period, and the share it delivered.
4. Apply RAG by rule. Green: on baseline. Amber: slip up to 10 working days or budget variance up to 5%, with a recovery plan. Red: anything larger, or recovery needs a sponsor decision. Re-rate any green hiding a late critical milestone or overdue dependency.
5. Add a trend arrow per workstream against last period.
6. Show milestone variance in working days and budget forecast at completion.
7. Write the headline: overall state and the biggest threat, in one sentence.

## Output format
- Headline (one sentence) and asks: Ask | Owner | Needed by
- RAG table: Workstream | Status | Trend | Commitments kept | Why
- Cross-workstream conflicts: Item | Workstream A says | Workstream B assumes | Resolve by
- Milestones: Milestone | Baseline | Forecast | Variance
- Budget: Plan | Actual | Forecast at completion | Variance %
One page.

## Quality checks
- Every RAG status matches the stated criteria
- Every date conflict between workstreams is listed
- Commitments are checked against last period's report
- The headline would survive the reader reading only that line

## Notes from the source article
- **Replaces:** The Thursday scramble where the PMO chases workstream leads, reconciles updates that contradict each other, and produces a status report that is mostly green.
- **Example request:** “Here are this week’s workstream updates, last week’s report, and the milestone and budget sheets. Write the status report and flag where workstreams contradict each other.”
- **What the user still owns:** Letting a red stay red. The report will surface it, and the political cost of sending it is yours.
- When handing the deliverable back, name in one line the decision above that stays with the user.
