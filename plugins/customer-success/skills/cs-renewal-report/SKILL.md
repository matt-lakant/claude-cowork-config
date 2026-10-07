---
name: cs-renewal-report
description: "Builds the weekly customer renewal report from the CS brain for the next 90 or 120 days: on track, watch or at risk per account with two lines of evidence, open promises, last real contact, next step, and value totals by status. Use when Matt asks for the \"renewal report\", \"renewal forecast\", \"what's renewing\", or runs the Friday reporter routine."
---

# CS 20: Renewal Report

Job: a renewal report with a source behind every status.

## Inputs

Renewals in the window (90 or 120 days) with dates and values, from Matt or from the account
Snapshots, plus the brain.

## Work

1. For each renewal, a status: on track, watch, at risk. Give the two lines of evidence behind
   it, with file and date.
2. List open promises and the last real contact for each.
3. Add up the value by status in code, using only the values given or on file.

## Output

A five-line summary on top, then a table `Account | Renewal date | Value | Status | Evidence |
Open promises | Next step | Owner`. Save to `reports/renewal-report_<date>.md` and send it as a
file card.

No evidence on file means the status is unknown, not on track.

## When not to use it

To make the quarter look better than it is. It reports what is on file.

## Brain rules (reference copy in `cs-brain`)

- Locate the brain first (`cs-brain` > Where the brain lives). If a file this skill needs is
  missing or empty, say so and stop. Do not work around it.
- File only what the sources say. Anything inferred is labelled INFERRED and stays out of the
  brain until Matt confirms it.
- Renewal date, seat count, plan and contract value come from a source or stay UNKNOWN.
- Show the change list first and write only after Matt says go. Add lines, never overwrite;
  flag conflicts. Archive, never delete.
- Every claim carries the file and date it came from. Dates are `YYYY-MM-DD`.
- Never contact a customer and never send anything. Draft; Matt sends.
