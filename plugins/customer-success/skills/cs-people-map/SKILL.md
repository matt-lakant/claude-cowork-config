---
name: cs-people-map
description: "Maps the people in a customer account from the CS brain: role, what they care about, last contact, warmth, who signed, who uses it daily, who decides the renewal, and whether the account is single-threaded. Use when Matt asks \"who do we know at <account>\", \"map the stakeholders\", \"are we single-threaded\", or before a renewal conversation."
---

# CS 06: People Map

Job: know who decides, who uses it, who went quiet and who left.

## Inputs

The account file and the `people/` files for the account, plus any contact notes Matt adds.

## Work

1. List each person with role, what they care about, last contact date, and warmth (warm,
   neutral, cold, unknown).
2. Mark the person who signed, the person who uses it daily, and the person who would decide
   the renewal. Say if any of those seats is empty.
3. Flag a single-threaded account: everything known runs through one contact.

## Output

A table `Name | Role | Cares about | Last contact | Warmth | Note`, then the one relationship to
build next and why. Proposed updates to `people/` files go in a change list.

Warmth comes from notes, not job titles. No notes means unknown.

## When not to use it

The account is a week old. There is no map to draw yet.

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
