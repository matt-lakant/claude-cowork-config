---
name: cs-chat-history-miner
description: "Runs across a batch of old exported chats and ranks which accounts and themes are worth importing into the CS brain first, with duplicates and empty chats on a skip list. Use when Matt has ten or more old chats to bring in, says \"which of these chats should I import\", or points at a full brain/imports/ folder."
---

# CS 04: Chat History Miner

Job: decide the import order so the brain gains the most, soonest.

## Inputs

A batch of exported chats, or their titles and first lines (pasted or in `imports/`).

## Work

1. Group the chats by account, then by theme (renewal, onboarding, escalation, QBR prep,
   pricing).
2. Rank the groups by how much the brain would gain: active accounts and upcoming renewals
   first (renewal dates from `accounts/`).
3. Flag duplicates and chats with nothing worth keeping.

## Output

A ranked import list `Group | Chats | Why it matters | Import order`, and a skip list. Then hand
the first group to `cs-chat-importer`.

Do not summarise chats that were not shown. Rank only what is in front of you.

## When not to use it

Fewer than ten chats. Run `cs-chat-importer` on each one.

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
