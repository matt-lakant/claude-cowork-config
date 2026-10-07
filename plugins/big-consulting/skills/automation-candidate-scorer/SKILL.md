---
name: automation-candidate-scorer
description: Scores process steps for elimination, simplification, rules-based automation, AI assistance, or human work, using observed volumes, times, and exception rates, and sizes the value of each. Use when the user asks what to automate, is evaluating RPA or AI for a process, needs a prioritized automation backlog, or wants to check a vendor's automation claims.
---

# Automation Candidate Scorer

## What this produces
A ranked backlog of steps with treatment, hours freed, effort, and required human checkpoints.

## Inputs to ask for
- Step list from the as-is map and value stream (with times and volumes)
- Observation notes on exceptions and judgment calls
- Systems involved and whether they have APIs
- Loaded hourly cost by role
- Regulatory or audit constraints
If exception rates are unknown, observe 50 items before scoring.

## Method
1. Ask first whether each step should exist. Eliminate or simplify before scoring for automation. Automating a broken step makes the broken step run faster.
2. Score remaining steps 1 to 5 on: monthly volume, minutes per item, rule-based share, input structure (structured, semi-structured, unstructured), exception rate from observation, system stability, error cost.
3. Assign a treatment: eliminate, standardize, workflow or system configuration, rules-based automation (stable screens, structured inputs, few exceptions), AI assistance (unstructured documents, drafting, classification, with human review), or keep human (judgment, relationships, high-stakes exceptions).
4. Monthly hours freed = volume x minutes per item / 60 x automatable share; annual value = hours freed x 12 x loaded hourly cost. Report hours, never headcount.
5. Estimate effort (low, medium, high) from systems, data, and change required.
6. Define human-in-the-loop checkpoints and the exception path for every automated step.

## Output format
- Table: Step | Volume | Minutes | Rule-based | Input type | Exception rate | Treatment | Hours freed per month | Annual value | Effort
- Value vs effort grid: quick wins, major projects, fill-ins, avoid
- Checkpoints: Step | Human review point | Exception route

## Quality checks
- Elimination was tested before automation
- Exception rates come from observation or logs
- AI treatments name their human review point
- Values tie to volume and time inputs

## Notes from the source article
- **Replaces:** The automation opportunity assessment: a spreadsheet of tasks scored for bots or AI, ending in a heat map that often automates work that should have been eliminated.
- **Example request:** “Score the 34 steps in our accounts payable process for automation. The value stream and last month’s volumes are attached. I want to know what to kill, what to automate, and where AI actually fits.”
- **What the user still owns:** What happens to the freed hours and the people who held them. Say it plainly and early, or adoption will stall.
- When handing the deliverable back, name in one line the decision above that stays with the user.
