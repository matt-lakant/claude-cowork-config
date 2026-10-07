---
name: analysis-prioritizer
description: Ranks a list of candidate analyses by decision impact, value at stake, effort, and data availability, cuts the ones whose result would not change the recommendation, and writes an explicit "will not analyze" list. Use when a project has too many analyses for the time left, when a team is boiling the ocean, or when deciding where to spend analyst days.
---

# Analysis Prioritizer

## What this produces
A ranked analysis list marked Keep, Cut, or Defer, plus a "we will not analyze" list with the reason for each cut.

## Inputs to ask for
- The candidate analyses (from the workplan, or a brain dump)
- The key question and the decision date
- Team capacity in person-days until the decision
- Value sizing by branch, if any (otherwise estimate order of magnitude and label it)

## Method
1. For each analysis, write the expected result and what the team would recommend if it came back that way. Then write what it would recommend if the result were the opposite.
2. So-what test: if the recommendation is the same either way, the analysis does not change the decision. Cut it.
3. Score survivors on four factors, 1 to 5: decision impact, value at stake, effort (inverse), data availability.
4. Apply 80/20: identify the few branches that hold roughly 80% of the value and concentrate effort there.
5. Set precision: decide the accuracy each analysis needs to support the decision (directional, plus or minus 20%, plus or minus 5%). Most need directional.
6. Fit to capacity: fill available person-days from the top of the ranking; everything below the line is Defer.
7. Write a stopping rule for each Keep: the point at which the team has enough to decide.

## Output format
- Ranked table: Rank | Analysis | Expected result | Changes decision? | Impact | Value | Effort | Data | Score | Precision needed | Keep/Cut/Defer
- "We will not analyze" list: Analysis | Reason
- Capacity check: days required vs available
- Stopping rules for each Keep

## Quality checks
- Every cut has a stated reason
- Planned effort fits within available capacity
- At least one analysis per high-value branch survives
- Precision targets are set, not left at "as accurate as possible"

## Notes from the source article
- **Replaces:** The mid-project reset where the engagement manager asks what each of 40 planned analyses would change and cuts to the eight that decide the answer.
- **Example request:** “We have 30 analyses planned for the pricing review and three weeks left. Tell me which eight matter and which to kill.”
- **What the user still owns:** Telling a senior stakeholder their favorite analysis got cut. The list gives you the reason; delivering it is on you.
- When handing the deliverable back, name in one line the decision above that stays with the user.
