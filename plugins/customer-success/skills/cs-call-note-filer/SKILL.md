---
name: cs-call-note-filer
description: "Turns a raw call transcript or scrappy customer call notes into a five-line summary, verbatim customer quotes, and dated lines for the History, Promises, People and Risks sections of the account file in the CS brain. Use after any customer call, when Matt pastes a transcript or recording notes, says \"file this call\" or \"log the call with [account]\"."
---

# CS 08: Call Note Filer

Job: every call ends up in the account's history in the customer's own words.

## Inputs

The transcript or notes (call, date, attendees) and the current account file. If a recording
connector such as Plaud is connected and Matt names a recording, fetch the transcript from it.

## Work

1. Write a five-line summary: why we met, what they said matters, what changed, what we
   promised, what happens next.
2. Pull direct customer quotes worth keeping, word for word.
3. Produce the dated lines to add to History, Promises, People and Risks in the account file,
   and to `people/` files for anyone new or changed. Update last-contact dates.

## Output

The summary, the quotes, then the exact lines to add by section. Write after go.

Keep the customer's words as they said them. Do not tidy a complaint into something softer.

## When not to use it

The call was recorded without the customer knowing. Sort that out first.

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
