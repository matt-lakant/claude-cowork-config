---
name: cs-rule-writer
description: "Turns a customer success lesson into a standing rule in the CS brain's rules.md, written as trigger, action and deadline, with an owner and a check, tested for overlap with existing rules. Use when Matt says \"make this a rule\", \"we should always...\", or after cs-lost-renewal-review finds a repeated lesson."
---

# CS 14: Rule Writer

Job: a lesson becomes something the team and every skill follows.

## Inputs

The lesson (from `cs-lost-renewal-review` or Matt's own words) and the current `rules.md`.

## Work

1. Rewrite the lesson as a rule with a trigger and an action: "When X happens, we do Y within Z
   days."
2. Check it against existing rules for overlap or conflict.
3. Say who owns it and how anyone would know it is being followed.

## Output

The rule in one sentence, its owner, its check, and where it goes in `rules.md`. Flag any rule
it replaces (the old one moves to `archive/`, not deleted). Write after go.

A rule nobody can check is not a rule. If the check cannot be written, say so.

## When not to use it

There is one example. One lost renewal is a story. Wait for the second.

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
