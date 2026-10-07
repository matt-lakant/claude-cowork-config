---
name: ai-business-case
description: Builds a business case for one AI use case or program with a bottom-up benefit model, full cost of ownership, adoption ramp, payback, and sensitivity. Use when the user needs to justify AI spend, prepare an investment committee request, compare AI options on economics, or check a vendor's ROI claims.
---

# AI Business Case Builder

## What this produces
A three-year case with benefits, costs, payback, NPV, and sensitivities, plus a one-page summary.

## Inputs to ask for
- Today's workflow: volume, time per unit, headcount, loaded cost, rework rate
- The expected change: which steps shrink or disappear
- Cost quotes: licenses or usage, implementation, integration
- Discount rate or hurdle rate
- Any vendor ROI claim, so it can be checked

## Method
1. Baseline: current annual cost of the workflow = volume times minutes per unit times loaded cost per minute, plus rework cost.
2. Benefit per unit: minutes saved per unit after AI, net of human review time. Review time is the most commonly omitted cost.
3. Adoption ramp by quarter. Full benefit on day one is never credible.
4. Classify benefits: hard (cost that leaves the P&L, such as overtime, contractors, vendor fees), capacity (hours freed for other work), and revenue or risk. Show them separately; approvers weigh them differently.
5. Full cost of ownership: licenses or usage at forecast volume, integration, data work, training, monitoring, prompt or model maintenance, internal staff time.
6. Compute cash flow by year, payback month, and NPV at the given rate.
7. Sensitivity: adoption at half, usage cost at double, benefit per unit at 70 percent. Report the break-even for each.

## Output format
- Summary: investment, annual hard benefit, payback, NPV, top risk
- Benefit table: Driver | Formula | Year 1 | Year 2 | Year 3 | Type
- Cost table by category and year
- Sensitivity table with break-even values

## Quality checks
- Capacity benefits are never added to hard savings without a label
- Human review time is included
- Usage-based costs scale with forecast volume
- Every input traces to the user or is marked an assumption

## Notes from the source article
- **Replaces:** The business case that gets an AI program through the investment committee: benefits, costs, payback.
- **Example request:** “Build the business case for using AI to process our 40,000 monthly supplier invoices. Here’s our AP headcount and cost, and two vendor quotes.”
- **What the user still owns:** Committing to the hard savings, which means deciding what happens to the freed capacity and the people in those roles.
- When handing the deliverable back, name in one line the decision above that stays with the user.
