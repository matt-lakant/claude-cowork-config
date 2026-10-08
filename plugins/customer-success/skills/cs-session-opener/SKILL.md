---
name: cs-session-opener
description: "Loads the right customer success context at the start of a session from the CS brain: reads INDEX.md, pulls only the files the task needs, gives a 10-line account recap and a list of what is missing or stale. Use when Matt starts work on a customer account, says \"open [account]\", \"get me up to speed on [account]\", \"prep me for the [account] call\", or before any cs- skill that works on one account."
---

# CS 02: Session Opener

Job: Matt never re-explains an account.

## Inputs

The account or task Matt is about to work on; `INDEX.md` and the account file.

## Work

1. Read `INDEX.md` and pull only the files this task needs. Say which ones were read.
2. Write a 10-line recap: who they are, what they bought and why, where things stand, open
   promises, last signal, next date that matters.
3. List what is missing or older than 60 days, so Matt knows what not to trust.

## Output

The recap, the stale list, then one question: what are we doing today?

Do not pad the recap from general knowledge about the company. If it is not in the brain, it is
not in the recap.

## When not to use it

The work is not about an account. Loading context that is not needed makes the answers worse.

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
