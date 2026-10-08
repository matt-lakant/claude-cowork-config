---
name: cs-account-search
description: "Answers a question about a customer from everything filed in the CS brain (account files, people, signal log, handoffs), newest first, with the file and date behind each claim and what the brain does not know. Use when Matt asks \"what did [account] say about X\", \"when did we last discuss Y with [account]\", or any factual question about a customer."
---

# CS 11: Account Search

Job: answer from what the team has filed, with receipts.

## Inputs

Matt's question and the brain.

## Work

1. Search account files, people files, the signal log and handoffs for anything that bears on
   the question (grep across the folder rather than reading every file).
2. Answer in plain words, newest information first.
3. After each claim, give the file and date it came from.

## Output

The answer, the sources, then what the brain does not know about this.

If files disagree, show both and say which is newer. Do not pick one quietly.

## When not to use it

The answer decides something large, such as a contract term. Read the contract.

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
