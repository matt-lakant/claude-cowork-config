---
name: interaction-qa-scorecard
description: Designs a weighted interaction quality scorecard with critical-error rules, then scores call transcripts, chats, or emails against it and reports calibration and coaching themes. Use when the user wants to build or fix a QA form, score a batch of interactions, or find out whether QA scores predict customer satisfaction.
---

# Interaction QA Scorecard

## What this produces
A scorecard with weighted criteria and behavioral definitions, scored interactions with evidence, coaching themes by agent or team, and a test of whether QA tracks customer outcomes.

## Inputs to ask for
- Current QA form, if one exists.
- A batch of transcripts, chat logs, or emails (attach), with agent ID and any linked CSAT or resolution flag.
- Compliance requirements (disclosures, identity verification, recording consent).
- If no form exists, build one first and confirm weights before scoring.

## Method
1. Build 8 to 12 criteria in three groups: compliance, resolution (understood the issue, resolved it, set expectations), and experience (clarity, empathy, effort).
2. Write each criterion as an observable behavior with pass and fail examples.
3. Mark compliance failures as critical errors: any one scores the interaction zero, reported separately.
4. Weight resolution criteria highest (40 to 50% combined) unless compliance risk dictates otherwise.
5. Score each interaction with a quoted line as evidence per criterion.
6. Check calibration: if human scores exist, report agreement per criterion; below 80% means the definition needs rewriting.
7. Where CSAT is linked, compare scores for high- and low-QA interactions. If QA does not separate them, flag criteria that do not predict outcomes.

## Output format
1. Scorecard: Criterion | Group | Weight | Pass Definition | Fail Example.
2. Scored table: Interaction | Agent | Score | Critical Error | Top Miss | Evidence.
3. Coaching themes by team (top 3).
4. QA to CSAT relationship.

## Quality checks
- Every score cites a line from the interaction.
- Critical errors are reported apart from averages.
- Criteria describe behaviors an evaluator can observe.

## Notes from the source article
- **Replaces:** A quality program redesign, when consultants rebuild the QA form, weight the criteria, set auto-fail rules, and run calibration sessions until evaluators agree.
- **Example request:** “Here are 150 chat transcripts with CSAT attached and our current QA form. Score them, and tell me whether our QA form measures anything customers care about.”
- **What the user still owns:** How scores get used. QA that feeds only discipline makes agents game the form; coaching is a management choice.
- When handing the deliverable back, name in one line the decision above that stays with the user.
