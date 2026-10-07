---
name: close-process-diagnostic
description: Diagnoses the month-end close from a close checklist or task list, finds the critical path, bottlenecks, and rework, and produces a sequenced plan to shorten it. Use when the close takes too many days, when the team works nights at month-end, or when reporting reaches executives too late to act on.
---

# Close Process Diagnostic

## What this produces
A day-by-day close map with the critical path marked, a ranked list of bottlenecks with root causes, and a phased plan to reduce close days.

## Inputs to ask for
- The close checklist: task, owner, day (e.g., WD+2), duration, dependency (attach spreadsheet)
- Number of entities, ERPs, and manual journal entries per month
- Recurring close issues, late adjustments, and the target close day
If there is no checklist, interview the user through each close day and build one first.

## Method
1. Lay out tasks by working day and trace dependencies to find the critical path, the chain that sets the final close day.
2. Flag bottlenecks: tasks on the critical path waiting on another team, data, or a single person.
3. Classify root causes: late cutoffs, manual journals, intercompany mismatches, reconciliations done at month-end instead of continuously, late accruals, review loops.
4. Count manual journals and post-close adjustments; high counts signal upstream data problems.
5. Identify moves: shift tasks before day zero (pre-close accruals, continuous reconciliation), set materiality thresholds for estimates, standardize intercompany, remove reviews that change nothing.
6. Sequence the plan in three waves: policy and calendar changes (weeks), process fixes (months), system changes (quarters).

## Output format
- Close map: Day | Task | Owner | Duration | Dependency | Critical path (Y/N)
- Bottleneck table: Task | Delay caused (days) | Root cause | Fix | Wave
- Three-wave plan, one paragraph per wave

## Quality checks
- The critical path is traced through dependencies, not assumed
- Every bottleneck names its root cause, with the symptom listed separately
- Days saved per fix are estimated and do not double count
- Controls are not removed without noting the risk

## Notes from the source article
- **Replaces:** A close diagnostic: consultants mapping every close task by day, interviewing accountants about bottlenecks, and planning how to cut close days.
- **Example request:** “Our close takes 11 working days. Here’s the close checklist. Where are the days going and how do we get to six?”
- **What the user still owns:** The controls trade-off. Faster closes come partly from accepting estimates, and the auditors and audit committee need to hear that from you first.
- When handing the deliverable back, name in one line the decision above that stays with the user.
