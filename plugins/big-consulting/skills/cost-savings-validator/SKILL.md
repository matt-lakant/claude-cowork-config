---
name: cost-savings-validator
description: Tests claimed cost-program savings against baselines, actuals, and budgets, removes double counts and cost avoidance, and grades each claim by evidence. Use before reporting savings to the board, when the PMO number and the P&L disagree, or at each quarter close.
---

# Savings Validator

## What this produces
A claimed-to-validated reconciliation: every initiative graded, with in-year and run-rate savings that tie to the general ledger.

## Inputs to ask for
- Initiative list: claimed savings, GL lines affected, baseline period, start date, owner
- Baseline and current actuals by GL line; current budget
- Headcount rosters before and after, including contractors
- Implementation or one-time costs by initiative
If the baseline period is undefined for an initiative, grade it Identified at best and flag it.

## Method
1. Classify each claim: hard P&L reduction, cost avoidance, cash or working capital, one-time, or revenue. Only hard reductions count toward EBITDA savings.
2. Volume-adjust: savings = (baseline unit cost minus current unit cost) x current volume.
3. Double-count test: flag any GL line claimed by two initiatives.
4. Budget test: was next year's budget reduced by the saving? If not, mark it at risk of being re-spent.
5. Leakage test: headcount removed but backfilled or replaced by contractors; lower price offset by volume creep.
6. Net off one-time implementation costs in the year incurred.
7. Split in-year impact (by realization month) from annualized run-rate.
8. Grade: Validated (in actuals and budget), Committed (contract signed or HR action done), Identified (plan only), Doubtful.

## Output format
- Table: Initiative | Claimed | Type | Validated in-year | Run-rate | Grade | Issue | Owner
- Waterfall from claimed to validated: less avoidance, less double count, less leakage, less one-time cost
- Five-line summary for the CFO

## Quality checks
- Every validated dollar traces to a GL line
- Cost avoidance never appears in the EBITDA total
- In-year and run-rate are never added together
- Doubtful items name the evidence that would upgrade them

## Notes from the source article
- **Replaces:** The finance validation step when the PMO reports a big number and the CFO asks how much is in the P&L.
- **Example request:** “The PMO says the cost program delivered USD 38M. Here’s the initiative tracker, the GL by line for both years, and the headcount files. How much is real?”
- **What the user still owns:** Publishing the lower number. It is the one the board can trust.
- When handing the deliverable back, name in one line the decision above that stays with the user.
