---
name: value-stream-waste-mapper
description: Converts a process map and timings into a value stream map with touch time, wait time, process cycle efficiency, first-pass yield, and tagged waste at each step. Use when the user wants to know where time goes in a process, why lead times are long, or where to focus a lean or redesign effort.
---

# Value Stream Waste Mapper

## What this produces
A value stream table and timeline showing touch time vs wait time per step, overall process cycle efficiency, and a ranked list of waste.

## Inputs to ask for
- The as-is map (step list with lanes)
- Timings from observation: touch time per step
- Wait or queue times from observation or system logs
- Volumes, work in progress, and rework rates
Where timings are missing, use ranges from staff and mark them estimated.

## Method
1. For each step record touch time, wait before the step, WIP in queue, and percent complete and accurate (share arriving with nothing to fix).
2. Classify each step: value-added (the customer would pay for it and it changes the work), business-necessary (required by law or control), or non-value-added.
3. Tag waste using the eight lean wastes: defects, overproduction, waiting, unused skills, transport, inventory, motion, extra processing.
4. Compute lead time (sum of touch and wait), process cycle efficiency (value-added time divided by lead time), and rolled first-pass yield (product of each step's percent complete and accurate).
5. Rank waste by hours consumed per month (time x volume).
6. Mark the three largest opportunities as improvement bursts, each with a target.

## Output format
- Table: Step | Touch time | Wait before | WIP | %C&A | Class (VA/BNVA/NVA) | Waste type
- Timeline totals: lead time, value-added time, process cycle efficiency, rolled first-pass yield
- Waste ranking: Waste | Steps | Hours per month | Root hypothesis
- Improvement bursts: Opportunity | Target | Owner role

## Quality checks
- Every timing is tagged observed, logged, or estimated
- Business-necessary steps name the rule that requires them
- Lead time reconciles to the observed end-to-end time within about 15%
- Waste is ranked by hours

## Notes from the source article
- **Replaces:** The value stream mapping exercise, where a lean team times every step and queue and learns the work spends most of its life waiting.
- **Example request:** “Using the as-is map and the timings from last week’s observation, build the value stream for our purchase order process and tell me where the eleven days go.”
- **What the user still owns:** Challenging the steps labeled business-necessary. Controls accumulate, and someone with authority has to ask which ones still earn their cost.
- When handing the deliverable back, name in one line the decision above that stays with the user.
