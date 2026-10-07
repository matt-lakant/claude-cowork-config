---
name: cs-memory-keeper
description: "Saves what mattered in a customer success session into the CS brain: new facts, decisions, promises and open questions, sorted to the right account, people, signals or rules file, shown as a change list before anything is written. Use at the end of CS account work, when Matt says \"save this to the brain\", \"file what we did\", \"update the account file from this session\". Not for Claude's own memory of Matt."
---

# CS 01: Memory Keeper

Job: make sure the next session can pick up where this one stopped.

## Inputs

This session's conversation, plus the current brain files for every account it touched
(`accounts/<account>.md`, and `people/` files for anyone named).

## Work

1. List every new fact, decision, promise and open question from this session, one line each,
   dated today.
2. Sort each line to the file it belongs in: an account file (and which section), a person
   file, `signals-log.md` or `rules.md`.
3. Show the exact lines to add and the exact lines to change. Mark anything that contradicts
   what is already on file, quoting both.

## Output

A change list grouped by file (`File | Add | Change | Conflict`). Once Matt says go, write the
files, update `INDEX.md`, and list the files changed.

Lines that are INFERRED appear in the list with that label and are not written until confirmed.

## When not to use it

The session was brainstorming with nothing decided. Filing half-thoughts as facts is how a
brain goes bad.

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
