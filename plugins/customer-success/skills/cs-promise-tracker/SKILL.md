---
name: cs-promise-tracker
description: "Finds every commitment made to a customer (feature dates, follow-ups, training, discounts, intros) across call notes, emails and the account file, and tracks whether each was kept, ranked by renewal proximity. Use when Matt asks \"what did we promise [account]\", \"open promises\", \"what do we owe them\", or before a QBR or renewal."
---

# CS 07: Promise Tracker

Job: keep the promises, not assign blame.

## Inputs

Call notes, emails and the account file for the account (Promises table and History).

## Work

1. Pull every commitment anyone on our side made: a feature date, a follow-up, a training
   session, a discount, an intro.
2. For each, record who promised, to whom, when, the due date if one was given, and the status:
   kept, open, late, broken, unknown.
3. Rank open and late promises by how close the renewal is.

## Output

A table `Promise | Who | To whom | Date | Due | Status`, then the three to close this week.
Changes to the account file's Promises table go in a change list.

"We'll look into it" counts as a promise if the customer would remember it as one. When in
doubt, list it and mark it SOFT.

## When not to use it

To catch a colleague out.

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
