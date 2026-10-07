---
name: cs-quiet-account-spotter
description: "Ranks customer accounts in the CS brain as active, slowing or quiet (no real two-way contact in 45 days by default), cross-checked against days to renewal, with the likely reason and first move for each. Use when Matt asks \"which accounts have gone quiet\", \"who haven't we heard from\", \"who should I call this week\", or as part of the signal watcher routine."
---

# CS 09: Quiet Account Spotter

Job: catch accounts going quiet before the renewal forecast does.

## Inputs

All account files (last contact, usage notes, open tickets, renewal date). Matt may give a
different quiet threshold.

## Work

1. Mark each account active, slowing or quiet. Quiet means no real two-way contact in 45 days,
   or the threshold Matt gives.
2. Compute days quiet and days to renewal in code from the dates on file. Quiet inside 120 days
   of renewal goes to the top.
3. For each quiet account, name the most likely reason from what is on file, or say the file
   does not tell.

## Output

A table ranked by urgency `Account | Status | Days quiet | Days to renewal | Likely reason |
First move`, then the three to call this week.

A sent email is not contact. Count only replies, calls and meetings.

## When not to use it

Last-contact dates are not kept up. Run `cs-call-note-filer` after every call for a month
first.

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
