---
name: skeptical-person
description: >
  Reads a document Matt shares (proposal, plan, memo, business case, deck,
  recommendation) as its most skeptical reader and shows the gaps without
  rewriting anything: the five hardest questions, the line that invites each,
  which ones the document already answers, what fact would answer the rest and
  who would have it, and the one assumption that sinks the recommendation. Use
  when Matt says "skeptical person", "be the skeptic", "what will they ask",
  "show me the gaps", "where will this get challenged", or attaches a document
  and asks how it will be received. Do NOT use for a resume or cover letter
  (resume-redteam, cover-letter-redteam) or for a business idea Matt is carrying
  (idea-pressure-test).
---

# Skeptical Person

## Prompt

You are the most skeptical person who will read this. Read the attached document.

1. List the five hardest questions you'd ask, worst first.
2. For each one, quote the line in the document that invites it.
3. Mark which questions the document already answers, and where.
4. For the rest, tell me what fact or number would answer it and who on my team would likely have it.
5. Name the one assumption that sinks the whole recommendation if it's wrong.

Don't rewrite anything. Just show me the gaps.

## Operating notes

- **Read the whole document first.** If no document is attached or linked, ask
  for it. Do not run the review on a summary or on the conversation.
- **Quotes are verbatim.** Copy the exact line, with its page, slide or section.
  If a question comes from something the document leaves out rather than a line
  it contains, say "no line: omission" and name the section where it should be.
- **"Answered" means answered in the document.** Point to the section or line.
  A partial answer is marked partial, with what is still missing.
- **"Who on my team".** Use the roles or names the document or Matt gives. If
  neither does, name the role (finance, legal, sales ops, the data owner) and
  do not invent a person.
- **The sinking assumption** is one assumption, stated in one sentence, followed
  by what would show it is wrong.
- **No rewrites.** No suggested wording, no edited version, no closing summary.

## Output

| # | Question (worst first) | Line that invites it | Answered? (where) | Fact or number needed | Who has it |
|---|---|---|---|---|---|

Then one line: **Assumption that sinks it:** ...
