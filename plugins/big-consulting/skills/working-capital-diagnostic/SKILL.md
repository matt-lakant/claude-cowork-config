---
name: working-capital-diagnostic
description: Diagnoses working capital by computing DSO, DPO, DIO, and the cash conversion cycle from ledger exports, segmenting the drivers, and sizing the cash release from specific levers. Use when cash is tight, when a lender or board asks about working capital, or before a cash-release program.
---

# Working Capital Diagnostic

## What this produces
Current DSO, DPO, DIO, and cash conversion cycle with trends, a driver breakdown for each, and a sized list of cash-release levers.

## Inputs to ask for
- 12 months of revenue and COGS by month
- AR aging by customer, AP aging by supplier, inventory by SKU or category (attach CSVs)
- Standard and actual payment terms for customers and suppliers
Without aging detail, compute headline metrics from balances and flag that levers cannot be sized.

## Method
1. Calculate: DSO = AR / revenue x days; DPO = AP / COGS x days; DIO = inventory / COGS x days; cash conversion cycle = DSO + DIO minus DPO. Use average balances and state the day count.
2. Trend monthly; flag seasonality and quarter-end window dressing.
3. DSO drivers: split into terms (contractual) versus overdue (collections). Rank customers by overdue dollars; find disputes and billing errors.
4. DPO drivers: compare contractual terms to actual payment days; flag early payments and suppliers on terms shorter than the company standard.
5. DIO drivers: segment inventory by movement (days of cover, slow-moving, obsolete); flag SKUs above 180 days of cover.
6. Size levers: cash release = days improved x (daily revenue or daily COGS). Separate one-time release from recurring benefit.

## Output format
- Metrics table: Metric | Current | 12-month trend | Target | Gap in days | Cash value
- Driver findings for DSO, DPO, DIO (five bullets each maximum)
- Lever table: Lever | Days | Cash released | Effort | Customer or supplier risk
- Total one-time cash release

## Quality checks
- Formulas use consistent periods and average balances
- Every cash figure shows its days x daily-value calculation
- Supplier-term extensions note the relationship and supply risk

## Notes from the source article
- **Replaces:** A working capital diagnostic: consultants pulling AR, AP, and inventory ledgers, computing DSO, DPO, and DIO, and sizing the releasable cash.
- **Example request:** “Our cash conversion cycle feels long. AR, AP, and inventory exports attached. How much cash is sitting in working capital and where?”
- **What the user still owns:** How hard to push suppliers and customers. The math says stretch terms; you know which supplier you cannot afford to lose.
- When handing the deliverable back, name in one line the decision above that stays with the user.
