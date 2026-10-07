---
name: process-cost-calculator
description: Calculates the fully loaded cost per transaction of a process using time-driven activity-based costing, separates value-add work from rework, and sizes unused capacity. Use when someone asks what a process costs per unit, before an automation or outsourcing decision, or when a team says it is understaffed.
---

# Process Cost Calculator

## What this produces
Cost per transaction by type, an activity cost table tagged value-add, required, or waste, and unused capacity.

## Inputs to ask for
- Process name and its start and end points
- Roles, headcount, and fully loaded cost per role (salary, benefits, overhead)
- Activities with minutes per unit, from a time survey or team estimates as low / likely / high
- Annual volumes by transaction type; exception and rework rates; system cost
If minutes are missing, draft the activity list and ask the owner for the three estimates.

## Method
1. Practical capacity per FTE = paid hours minus breaks, training, and meetings. Default 80% of paid time, labeled.
2. Capacity cost rate = total fully loaded cost / total practical capacity minutes.
3. For each activity and transaction type, cost = minutes per unit x volume x rate.
4. Add allocated system cost per transaction.
5. Tag each activity: value-add, required (controls, compliance), or waste (rework, chasing approvals, re-keying, status checks).
6. Price the exception path separately: clean-path cost, exception-path cost, exception rate.
7. Unused capacity = practical capacity minus minutes the volume requires. Convert to FTEs and dollars.

## Output format
- Activity table: Activity | Driver | Volume | Minutes per unit | Cost per unit | Annual cost | Tag
- Cost per transaction by type, clean versus exception
- Waste total; unused capacity in FTEs and dollars
- Top three cost drivers, one line each

## Quality checks
- Modeled minutes are within 10% of practical capacity, or the gap is explained
- Labor cost is fully loaded
- Every minutes figure cites its source (survey, estimate, system log)
- Unused capacity is reported as capacity; any headcount decision is left to the user

## Notes from the source article
- **Replaces:** An activity-based costing study: time surveys and interviews that price one invoice, claim, or onboarding.
- **Example request:** “Our 14-person AP team says it’s drowning. Here are volumes by invoice type and time per step. What does one invoice cost us?”
- **What the user still owns:** What happens to freed capacity. Redeploy, stop backfilling, or reduce: that is a people decision.
- When handing the deliverable back, name in one line the decision above that stays with the user.
