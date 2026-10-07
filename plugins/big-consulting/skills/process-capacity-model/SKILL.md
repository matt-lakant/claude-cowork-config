---
name: process-capacity-model
description: Builds a capacity model from volume, observed handle times, shrinkage, and target utilization to calculate required staff, locate the bottleneck, and test scenarios. Use when the user asks how many people a process needs, is facing a backlog or volume change, is planning for seasonality, or wants to size the effect of a redesign or automation.
---

# Process Capacity Model

## What this produces
A required-FTE calculation by step and period, the bottleneck, backlog math, and scenario results.

## Inputs to ask for
- Volume by task type and period, with seasonality and peaks (spreadsheet)
- Handle time per task type, from observation or logs, including after-work
- Current staffing by role and schedule
- Shrinkage: PTO, training, meetings, breaks
- Current backlog and lead time target
If shrinkage is unknown, assume 30% and flag it.

## Method
1. Use observed handle times, not standards. Include after-work, rework rates, and interruptions.
2. Workload hours = volume x handle time, by task type and period.
3. Productive hours per FTE = paid hours x (1 minus shrinkage).
4. Required FTE = workload hours divided by (productive hours x target utilization). Set utilization near 80 to 85% for queue work, since wait times climb steeply above that.
5. Find the bottleneck: the step with the highest workload relative to capacity.
6. Apply Little's Law (WIP = throughput x lead time) to size the backlog and the capacity needed to clear it within a target period.
7. Run scenarios: volume up 20%, peak month, handle time cut by the redesign, automation of named steps.

## Output format
- Assumptions table: Input | Value | Source
- Capacity table: Step | Volume | Handle time | Workload hours | Required FTE | Current FTE | Gap
- Bottleneck statement
- Backlog clearance: Backlog | Extra capacity | Weeks to clear
- Scenarios: Scenario | Required FTE | Change vs base

## Quality checks
- Handle times are observed or logged, and sourced
- Shrinkage and utilization are explicit
- The model reproduces current performance before forecasting
- Capacity is modeled at peak

## Notes from the source article
- **Replaces:** The staffing spreadsheet that answers how many people a process needs, usually built on handle times someone once estimated.
- **Example request:** “Our order entry team has a 1,400-order backlog and volume goes up 25% in Q4. Here are volumes and observed handle times. How many people do we need, and where is the bottleneck?”
- **What the user still owns:** How to close the gap (hire, flex, cross-train, or redesign) and the judgment on what utilization level your people can sustain.
- When handing the deliverable back, name in one line the decision above that stays with the user.
