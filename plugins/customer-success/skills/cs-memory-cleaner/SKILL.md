---
name: cs-memory-cleaner
description: "Sweeps the CS brain for duplicates, active-account files untouched for 90 days, people who left, and promises with no status; proposes merge, update, archive or ask-the-owner for each and rebuilds INDEX.md, changing nothing until approved. Use when Matt says \"clean up the brain\", \"tidy the CS files\", or for the monthly rules-keeper run."
---

# CS 18: Memory Cleaner

Job: keep the brain trustworthy as it grows.

## Inputs

The whole brain folder, starting from `INDEX.md`.

## Work

1. Find duplicates, files for active accounts not touched in 90 days (compute from dates in
   code), people who have left, and promises with no status.
2. Propose a fix for each: merge, update, archive, or ask the owner.
3. Rebuild `INDEX.md` to match the folder as it will be after the fixes.

## Output

A change list `File | Problem | Proposed fix | Needs a human?`, then the new `INDEX.md`. Make no
changes until Matt approves the list.

Archive, never delete: move old files to `archive/` with the date in the name.

## When not to use it

The week before a big renewal. Clean up after, not during.

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
