---
name: tackle-task
description: >
  General-purpose kickoff for tackling a new piece of work when (1) no other
  installed skill is applicable and (2) the request is a task to do or produce
  something, not a question to answer. Use when the user describes work plus a
  goal/success criteria (e.g. "write a PR brief for my launch to get more
  leads", "put together an onboarding plan so new hires ramp faster") and no
  more specific skill fits. Frames the request as task + success criteria, then
  gathers missing context with AskUserQuestion BEFORE starting work. Do NOT use
  when a dedicated skill already covers the request (resume, cover letter,
  interview prep, spreadsheet/docx/pptx/pdf production, scheduling, etc.), and do
  NOT use for questions or information lookups (anything answerable directly,
  e.g. "what's X", "how does Y work", "who is Z") — answer those normally
  instead.
---

# Tackle Task

A lightweight starting move for open-ended work that isn't owned by a more
specific skill. It turns a loose request into a clear task + success criteria,
then closes the biggest information gaps before doing anything.

## When to use

Both conditions must hold:

- **It's a task, not a question.** The user wants something done or produced
  (a brief, a plan, a draft, an analysis), not an answer to an informational
  query. If the request is answerable directly ("what is...", "how does...",
  "who...", "explain..."), this skill does not apply — just answer.
- **No other installed skill is a better match.** If a dedicated skill owns the
  request, defer to it.

## When NOT to use

- A dedicated skill already handles it — defer to that skill.
- The request is a question, information lookup, or pure conversation.

## Procedure

1. **Restate the task and success criteria** in one line so scope is explicit:
   - Task: what they want produced or done.
   - Success criteria: what "good" looks like / the outcome that matters.
   If either is missing, that's a gap for step 2.

2. **Ask before building.** Call `AskUserQuestion` to resolve the highest-impact
   unknowns first. Prioritize questions whose answers would change the
   deliverable:
   - Audience / who it's for
   - Format and length (doc, deck, email, spreadsheet, etc.)
   - Tone / level of formality
   - Scope and must-include points
   - Any constraints, deadlines, or source material
   Keep it to the few questions that actually matter; make reasonable
   assumptions for the rest and flag them briefly.

3. **Plan, then execute.** Create a short task list, produce the deliverable,
   and finish with a verification pass against the stated success criteria.

## Prompt template this skill operationalizes

> I need to [task, e.g. "write a PR brief for the launch of my company"] for
> [success criteria, e.g. "to get more leads"].
> First, use the tool AskUserQuestion to get more info.
