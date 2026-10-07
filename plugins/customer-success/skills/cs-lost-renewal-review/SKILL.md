---
name: cs-lost-renewal-review
description: "Reviews a churned or downgraded customer account from the CS brain: dated timeline from kickoff to loss, the earliest signal that was on file at the time, whether anyone acted, and what was controllable. Use when Matt says \"we lost <account>\", \"why did <account> churn\", \"post-mortem on the renewal\", or after any lost or shrunk renewal."
---

# CS 13: Lost Renewal Review

Job: find the earliest moment the loss could have been caught.

## Inputs

The full account file, its signal log lines and handoffs, and what the customer said when they
left.

## Work

1. Build a dated timeline from kickoff to loss.
2. Mark the first signal that, looking back, pointed to this. Compute how long before the loss
   it appeared and say whether anyone acted on it.
3. Separate what we could control from what we could not (budget cut, acquisition, champion
   left).

## Output

The timeline, the earliest catchable moment, and one or two lessons written as plain sentences.
Save to `reports/lost-renewal_<account>_<date>.md` after go. Hand a lesson to `cs-rule-writer`
only if it has appeared before.

Hindsight makes everything look obvious. Call a signal catchable only if it was on file at the
time.

## When not to use it

The loss happened this week and people are raw. Give it a fortnight.

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
