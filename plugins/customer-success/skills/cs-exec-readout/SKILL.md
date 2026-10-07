---
name: cs-exec-readout
description: "Turns the customer renewal report into a one-page readout for a leader (CRO, CFO, CEO, CCO): the number that reader cares about, what changed since last week, what is needed from them, the three accounts needing a decision, published behind a private link with a two-line cover message. Use when Matt asks for an \"exec readout\", \"renewal summary for the CRO\", \"one-pager for leadership\"."
---

# CS 21: Exec Readout

Job: a leader reads it in two minutes.

## Inputs

This week's renewal report (from `reports/`) and who is reading it.

## Work

1. Lead with the number that reader cares about, then what changed since last week, then what
   is needed from them.
2. Keep account detail to the three that need a decision.
3. Strip customer contact names and anything said in confidence.

## Output

The one-page readout as a private Docs artifact (a link Matt shares, not an attachment), also
saved to `reports/exec-readout_<date>.md`, plus a two-line message to send with the link. The
message is in Matt's name, so draft it with `writing-voice`.

## When not to use it

The reader wants the full table. Send the renewal report.

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
