---
name: cycle-time-log-study
description: Analyzes system event logs to measure end-to-end cycle time, step durations, waits, process variants, and rework, then reconciles the findings with frontline observation. Use when the user has a CSV export from a ticketing, ERP, CRM, or workflow system and wants to know how long work really takes, where it waits, or how many different ways it actually flows.
---

# Cycle-Time Log Study

## What this produces
A cycle-time distribution, a variant table, a wait-time ranking by step and handoff, and a list of what the log cannot see.

## Inputs to ask for
- Event log export (CSV): case ID, activity, timestamp, and ideally resource and case attributes
- Business-hours calendar and time zone
- The observed process map, to compare against
- Which case segments matter (product, region, priority)
Without a case ID the analysis cannot run; ask for one.

## Method
1. Clean: remove duplicates, fix time zones, sort events per case, and drop (and count) cases open at the window's edges.
2. Measure end-to-end cycle time per case in calendar and business hours. Report median, 90th percentile, and the gap between them.
3. Find variants (distinct activity sequences). Report the main path's share and the top ten.
4. Measure time between consecutive activities. Rank the longest waits, especially handoffs between resources or teams.
5. Detect rework: repeated activities within a case. Report rework rate and its cycle-time penalty.
6. Cut by segment to find where the 90th percentile tail lives.
7. Reconcile with observation: list steps seen on the floor that never appear in the log (email, phone, spreadsheets).
8. Compute on the full file; if it is too large to attach, request a filtered export.

## Output format
- Data quality: rows, cases, dropped, date range
- Cycle time: Segment | Cases | Median | P90 | P90/median ratio
- Variants: Variant | Cases | Share | Median cycle time
- Waits: From step | To step | Median wait | P90 wait
- Invisible work: steps observed but absent from the log

## Quality checks
- Business hours and calendar hours are both reported
- Incomplete cases are excluded and counted
- Averages never appear alone; medians and P90 do
- Off-system work is named explicitly

## Notes from the source article
- **Replaces:** The time study done with system data: analysts export event logs, clean timestamps for a week, and finally see how long each case takes and where it sits idle.
- **Example request:** “Here’s a six-month ticket export from our IT service desk. Tell me how long requests really take, where they wait, and how many paths they actually follow.”
- **What the user still owns:** Deciding which cycle time the customer cares about, and whether the tail cases deserve a separate process.
- When handing the deliverable back, name in one line the decision above that stays with the user.
