---
name: cs-conflict-checker
description: "Finds places where the CS brain gives two values for a fact that should have one (renewal date, seat count, plan, owner, main contact, stated goal), shows both with file and date, and suggests which is likely right without changing anything. Use when Matt asks \"is the brain consistent\", \"check for conflicts\", \"which renewal date is right for <account>\"."
---

# CS 19: Conflict Checker

Job: surface contradictions; never resolve them alone.

## Inputs

Files for one account or all accounts.

## Work

1. Compare facts that should have one value: renewal date, seat count, plan, owner, main
   contact, stated goal.
2. For each mismatch, show both versions with file and date.
3. Suggest which is likely right and why, without changing anything.

## Output

A table `Account | Fact | Version A | Version B | Newer | Who would know`, sorted by days to
renewal.

Newer is not always right. If the older line quotes a contract and the newer one quotes a chat,
say so.

## When not to use it

There is one source per fact. Nothing to compare.

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
