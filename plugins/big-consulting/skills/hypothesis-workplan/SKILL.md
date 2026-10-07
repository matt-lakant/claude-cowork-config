---
name: hypothesis-workplan
description: Converts an issue tree into a hypothesis-driven workplan with a falsifiable hypothesis, analysis, kill criterion, data source, owner, and due date for each branch. Use when an issue tree exists and the team needs a week-by-week plan, or when a project is running analyses without a clear point of view.
---

# Hypothesis-Driven Workplan

## What this produces
A workplan table covering every live branch of the issue tree, sequenced by week, with each row ending in the one chart that would answer it.

## Inputs to ask for
- The issue tree (attach or paste)
- Project length in weeks and the date of the decision meeting
- Team members available and their approximate days per week
- Known data access limits (systems that take weeks to extract from)
If there is no tree, build a quick one first and confirm it with the user.

## Method
1. For each leaf, write a hypothesis as a falsifiable claim with a number: "Freight cost per order rose more than 15% because order size fell," never "look at freight."
2. Write the analysis that tests it and the specific result that would kill it (the kill criterion). A hypothesis with no kill criterion is an opinion.
3. Name the end product: the single chart or table that would appear in the final document if the hypothesis holds.
4. Assign a data source and a realistic extraction lead time.
5. Sequence: long-lead data first, high-value branches first, dependent analyses after their inputs.
6. Load-check: total effort per person per week must fit capacity. Cut or defer until it does.
7. Set two checkpoints before the decision meeting where the hypotheses are revised based on results.

## Output format
- Table: # | Branch | Hypothesis | Analysis | Kill criterion | End-product chart | Data source | Owner | Week due
- Week-by-week view (one line per week listing what lands)
- Checkpoint dates and what gets decided at each
- Capacity note: planned vs available person-days

## Quality checks
- Every hypothesis contains a direction and a magnitude
- Every row has a kill criterion
- No person is loaded above available capacity
- Long-lead data requests appear in week one

## Notes from the source article
- **Replaces:** The workplan the engagement manager builds in week one: a hypothesis on every branch, the analysis that would prove or kill it, who owns it, and when it lands.
- **Example request:** “Here’s our issue tree on rising customer churn. We have six weeks and three people part-time. Build the workplan.”
- **What the user still owns:** Letting a hypothesis die in front of the people who proposed it. The plan only works if killed hypotheses stay dead.
- When handing the deliverable back, name in one line the decision above that stays with the user.
