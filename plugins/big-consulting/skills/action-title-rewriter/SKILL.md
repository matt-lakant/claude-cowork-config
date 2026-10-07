---
name: action-title-rewriter
description: Rewrites slide titles into action titles, full-sentence conclusions the slide body proves, then checks that the titles read in sequence as one argument. Use when a deck has topic-label titles, before any executive or board presentation, or when someone says "the headlines are weak" or "tighten the titles."
---

# Action Title Rewriter

## What this produces
A title-by-title rewrite table, the rewritten titles as a single numbered read-through, and a list of slides to cut or split.

## Inputs to ask for
- The deck (attach the PPTX or PDF), or a pasted list of titles with a one-line description of each slide's chart or body
- The deck's governing message, if the author has one
- The audience
If only titles are given with no slide content, rewrite them but mark every title "body support unverified."

## Method
1. Extract every title and what the body actually shows (chart type, key number, comparison).
2. Classify each title: topic label, observation (what the data shows), insight (why it matters), or action (what to do). Every content slide should end as insight or action.
3. Rewrite each as a full sentence with subject, verb, and implication. Maximum 15 words and two lines. Quantify when the body has the number. One message per title.
4. Evidence check: the title may claim only what the body proves. If the claim outruns the data, soften it or note "body must show X."
5. Horizontal read: list the rewritten titles in order. They must read like a paragraph that argues the governing message. Flag jumps in logic, repeated points, and points the argument needs that have no slide.
6. Consistency pass: same term for the same thing, same units, same number format, same tense.
7. Flag slides to cut (no claim can be written because the slide has no message) and slides to split (two messages on one page).

## Output format
- Table: Slide # | Current title | Type | Rewritten title | Words | Body supports it? (Y / Partial / N) | Note
- Horizontal read: rewritten titles as a numbered list
- Cut and split list with one-line reasons

## Quality checks
- No title over 15 words
- Every number in a title appears in the slide body or the inputs
- No title uses a verb without direction ("impacts," "affects") where the data shows which way
- The horizontal read has no gap the audience would notice

## Notes from the source article
- **Replaces:** The associate’s late-night pass through a 40-page deck, turning “Q3 Revenue by Region” into sentences that say what each chart proves, followed by the manager’s red pen doing it all again.
- **Example request:** “Attached is the 32-page ops review deck for Thursday. Rewrite every title as an action title and tell me which slides don’t earn their place.”
- **What the user still owns:** How hard to state the claim. The skill will tell you when a title outruns its evidence; deciding whether the room needs a bold headline or a careful one depends on who is sitting in it.
- When handing the deliverable back, name in one line the decision above that stays with the user.
