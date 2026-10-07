---
name: cs-signal-log
description: "Adds small customer signals (champion left, ticket spike, late invoice, pricing question, competitor mention, thank-you) to the CS brain's signals-log.md as dated one-liners and checks for real patterns: one account three times in 30 days, or one signal across three accounts. Use when Matt says \"log this signal\", \"I noticed...\" about a customer, or \"any patterns in the signal log\"."
---

# CS 10: Signal Log

Job: one running log of small signals, so patterns show up.

## Inputs

What Matt noticed, and the current `signals-log.md`.

## Work

1. Write each signal as one line: `date · account · signal · good/bad/unclear · source`.
2. Check the log (in code, over the dated lines) for the same account three or more times in
   30 days, and the same signal across three or more accounts in 30 days.
3. Say which pattern, if any, deserves a conversation.

## Output

The new lines to add on top of the log, then any pattern found with the lines that support it.
Write after go.

One signal is a note. Do not call it a trend.

## When not to use it

The customer said it in confidence. Some things belong in Matt's head, not a shared file.

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
