---
name: cs-morning-brief
description: "Gives Matt his customer success day in one screen from the CS brain and today's calendar: three lines per customer meeting, promises due this week, renewals inside 90 days, and new signals since yesterday's handoff. Use when Matt asks for his \"CS brief\", \"customer brief\", \"what's on with my accounts today\", or runs the briefing routine. Not the general morning brief (the `morning` skill)."
---

# CS 16: Morning Brief

Job: the day in one screen.

## Inputs

Today's date; today's calendar (from a connected calendar such as Outlook via Microsoft 365, or
pasted by Matt); yesterday's handoff in `handoffs/`; the signal log and account files.

## Work

1. For each customer meeting today, three lines: where things stand, open promises, the one
   thing to raise.
2. List promises due this week and renewals inside 90 days (compute dates in code).
3. List new signals since yesterday's handoff.

## Output

One screen, in this order: Today's calls · Due this week · New signals · One thing Matt would
otherwise miss. Read only; nothing is written.

If yesterday's handoff is missing, say so at the top. Do not rebuild it from guesses.

## When not to use it

Matt will read it and then open the account files anyway. If the brief is not trusted, fix the
brain, not the brief.

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
