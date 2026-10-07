---
name: churn-driver-analysis
description: Measures customer retention by cohort and segment, identifies the drivers and leading indicators of churn, and sizes the value of improving retention. Use when the user reports losing customers or revenue, wants to understand why customers leave, or needs gross and net revenue retention analysis across the base.
---

# Churn Driver Analysis

## What this produces
Retention by cohort and segment, ranked churn drivers, leading indicators, and the dollar value of one point of retention.

## Inputs to ask for
- Customer revenue by month or quarter, 24+ months, with customer ID (CSV or XLSX).
- Churn records: date, reason code, and any exit notes.
- Behavioral data where available: usage, orders, tickets, late payments, contract dates, rep changes. If reason codes are missing, say driver confidence is lower.

## Method
1. Define churn with the user: logo churn, revenue churn, or downgrade. Compute gross revenue retention (GRR) and net revenue retention (NRR) for the trailing 12 months.
2. Build retention curves by acquisition cohort (quarter). Note whether curves flatten (a stable core) or keep declining.
3. Cut retention by segment, product, channel, deal size, tenure, and acquisition source. Report any cut that differs from the average by more than 5 points.
4. Split churn into controllable (service, price, fit, competitor) and uncontrollable (acquired, closed, moved); rank drivers on controllable only.
5. Test leading indicators: compare the 90 days before churn against retained customers on usage change, ticket volume, payment days, and contact changes. Use logistic regression if there are more than 200 churn events; otherwise compare rates side by side.
6. Code exit notes into reasons and reconcile them with behavior. Where the stated reason conflicts with the data, report both.
7. Size the prize: revenue retained per point of GRR, compounded over 3 years.

## Output format
1. Metrics summary: GRR, NRR, logo churn, trailing 12 months and prior year.
2. Cohort table: Cohort | Starting Customers | Retained at 4, 8, 12 Quarters.
3. Driver table: Driver | Share of Churned Revenue | Evidence | Controllable (Y/N).
4. Leading indicators: Signal | Churn Rate With Signal | Without | Lead Time.
5. Value of one point of retention, with the math shown.

## Quality checks
- Churn definition is stated once and applied consistently.
- Uncontrollable churn is excluded from driver rankings.
- Correlation is not described as causation.

## Notes from the source article
- **Replaces:** A retention diagnostic: cohort curves, a churn model, coded exit interviews, and the value of a point of retention.
- **Example request:** “We lost about 14% of recurring revenue last year and nobody agrees why. Here are monthly billing, the churn log, and ticket history. What is driving it?”
- **What the user still owns:** Fixing the drivers that live in someone’s org. When the analysis points at onboarding or a service team, the conversation with that leader is yours.
- When handing the deliverable back, name in one line the decision above that stays with the user.
