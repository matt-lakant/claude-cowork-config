---
name: cs-team-answer-finder
description: "Finds past situations across all accounts in the CS brain that look like the one Matt is in (same kind of customer, same kind of problem), what was tried, what happened and who handled it. Use when Matt asks \"has anyone dealt with this before\", \"who handled a situation like this\", \"what worked last time\"."
---

# CS 12: Team Answer Finder

Job: point Matt at the colleague worth a five-minute call.

## Inputs

A description of the situation, and the brain.

## Work

1. Find past situations across all accounts that look like this one: same kind of customer,
   same kind of problem (History, Risks, handoffs, signals).
2. For each, say what was tried, what happened and who handled it.
3. Name the person worth a five-minute call.

## Output

Up to five matches `Account | When | What happened | What was tried | Result | Who to ask`, then
what to try first here.

A loose match is worse than no match. Say when nothing on file really fits.

## When not to use it

The brain is under a month old. Ask in the team channel; it will be faster.

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
