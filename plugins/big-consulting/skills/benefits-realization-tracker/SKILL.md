---
name: benefits-realization-tracker
description: Builds and updates a benefits register that tracks realized value against a ramp curve for each benefit, with leading adoption indicators, attribution adjustments, and exception actions. Use when a solution has gone live and its benefits need tracking, at monthly program reviews, or when benefits promised in business cases are no longer visible anywhere.
---

# Benefits Realization Tracker

## What this produces
A benefits register, a monthly tracker of realized against planned value, and an exceptions list with owner actions.

## Inputs to ask for
- Business cases or charters listing each benefit
- For each benefit: KPI, baseline and baseline period, target, owner, go-live date
- Monthly actuals for each KPI and for adoption measures (active users, transactions through the new process, compliance rate)
- Volume or seasonality data needed to adjust results
If a baseline was never frozen, propose one from historical data and label it for owner sign-off.

## Method
1. Register each benefit: type (revenue, cost, cash, risk, experience), KPI, P&L line if financial, owner, baseline, target.
2. Build a monthly ramp curve from go-live to full run-rate.
3. Pair every lagging financial benefit with one or two leading adoption indicators.
4. Adjust actuals for volume and seasonality, or compare against a control group where one exists. State the method.
5. Compute realized against ramp, monthly and cumulative.
6. Status: On track (within 10% of ramp), Behind, At risk, Realized, Abandoned.
7. For each Behind or At risk benefit, name the cause: adoption, process, data, or wrong estimate. Each cause gets an action.

## Output format
- Register: Benefit | Type | KPI | Baseline | Target | Owner | Go-live | Status
- Monthly tracker: Benefit | Planned to date | Realized to date | Variance | Leading indicator
- Exceptions: Benefit | Cause | Action | Owner | Due
- Cumulative realized against planned, one line

## Quality checks
- Baselines are frozen and dated
- No benefit is counted before its go-live
- Financial benefits match what finance sees
- Every exception has an owner in the business

## Notes from the source article
- **Replaces:** The value office that tracks every benefit promised in the business cases, month by month, against a ramp curve, after the project team has moved on.
- **Example request:** “We launched the new claims platform in April. Here are the business case benefits and five months of KPI data. Where are we against plan, and what’s lagging?”
- **What the user still owns:** Holding benefit owners to the numbers after the program team disbands.
- When handing the deliverable back, name in one line the decision above that stays with the user.
