---
name: cs-chat-importer
description: "Turns one exported ChatGPT, Claude or Codex chat into clean dated lines filed against the right account in the CS brain: customer facts, decisions, promises, and drafts marked DRAFT unless the chat shows they were sent. Use when Matt says \"import this chat\", drops a chat export in brain/imports/, or pastes an old conversation about a customer account."
---

# CS 03: Chat Importer

Job: get what an old chat knew about a customer into the brain, without the noise.

## Inputs

One exported chat (pasted, attached, or a file in `imports/`) and the list of account names
(from `accounts/`).

## Work

1. Identify which account or accounts the chat is about. If that cannot be told, say so and
   stop.
2. Pull out facts about the customer, decisions made, promises given, and drafts that were
   actually sent. Ignore the prompts and the assistant's filler.
3. Date each line with the chat's date, not today's. Mark anything older than six months as
   OLD.

## Output

A table `Account | Date | Type | Line | Source chat`, then the lines grouped by the brain file
they would go into. Write after Matt says go; move the processed export to `imports/done/` with
today's date in the name.

A draft in a chat is not proof it was sent. File it as DRAFT unless the chat says it went out.

## When not to use it

The chat holds customer data the company does not allow in AI tools. Check the policy line at
the top of `rules.md` before importing.

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
