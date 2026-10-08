---
name: cs-account-file-builder
description: "Builds or rebuilds the one-page account file in the CS brain (snapshot, why they bought, success in the customer's words, people, promises, dated history, risks, open questions) from CRM notes, contract summary, kickoff notes, emails and call notes, marking gaps UNKNOWN. Use when Matt says \"build the account file for [account]\", hands over a new account from sales, or an account has no file yet."
---

# CS 05: Account File Builder

Job: the one page every other skill depends on.

## Inputs

Everything available on the account: CRM notes, contract summary, kickoff notes, emails, call
notes. The shape is `templates/account-template.md` in the `cs-brain` skill folder (also
`accounts/_TEMPLATE.md` in the brain).

## Work

1. Fill the structure: Snapshot (plan, seats, renewal date, owner) · Why they bought · What
   success looks like in their words · People · Promises we made · History (dated) · Risks ·
   Open questions.
2. Quote the customer's own words for "why they bought" and "what success looks like" wherever
   the source has them.
3. Leave a section empty and marked UNKNOWN rather than filling it with a guess.

## Output

The finished `accounts/<account>.md` (shown first, written after go), then the UNKNOWNs ranked
by how much they matter before renewal. Add the file to `INDEX.md`.

Never invent a renewal date, a seat count or a contract value. Those come from the source or
they stay UNKNOWN.

## When not to use it

There is nothing but the company's name. Get the kickoff notes first.

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
