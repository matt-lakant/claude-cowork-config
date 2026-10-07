---
name: thirteen-week-cash-forecaster
description: Builds a direct-method 13-week cash flow forecast from receivables, payables, payroll, and committed spend, with a weekly liquidity view and variance-to-actual tracking. Use when cash is tight, when a lender requires a 13-week forecast, before a covenant test, or to set up weekly treasury discipline.
---

# 13-Week Cash Forecaster

## What this produces
A 13-week direct-method cash forecast from opening to closing cash and liquidity, plus a weekly variance template.

## Inputs to ask for
- Opening cash balances by account and available credit lines
- AR aging with expected collection timing; AP aging and payment runs (attach CSVs)
- Payroll calendar and amounts, rent, debt service, taxes, capex commitments
- Minimum cash buffer and covenant thresholds
If collection history is missing, apply customer terms plus average days late and label it an assumption.

## Method
1. Use the direct method: forecast receipts and disbursements by week, never derived from the P&L.
2. Receipts: forecast collections by customer for the top customers covering 80% of AR, using historical days-to-pay; group the tail.
3. Disbursements: payroll on its calendar, AP by payment run, fixed commitments on due dates, taxes and debt service on statutory or contractual dates.
4. Calculate weekly net cash flow, closing cash, and liquidity (cash plus undrawn facility) against the minimum buffer.
5. Flag the low point and any week breaching the buffer or a covenant.
6. List levers for breach weeks: collection pushes, payment timing, capex deferral, drawdown, with cash amount and week.
7. Set the weekly rhythm: roll one week forward, record actual vs forecast by line, and explain variances above 10%.

## Output format
- Weekly table: Line | Wk1 ... Wk13 | Total
- Liquidity summary: low-point week, amount, headroom vs buffer
- Levers table: Lever | Week | Cash impact | Owner
- Variance template: Line | Forecast | Actual | Variance | Reason

## Quality checks
- Closing cash each week equals opening plus net flow
- No P&L accruals or non-cash items appear
- Every receipt and payment ties to aging, calendar, or contract

## Notes from the source article
- **Replaces:** The 13-week cash model restructuring advisors build in week one of a liquidity crunch and update weekly.
- **Example request:** “Our bank wants a 13-week cash forecast by Friday. AR and AP aging and the payroll calendar are attached. Build it and show me the low point.”
- **What the user still owns:** The lender conversation. The forecast is only credible if it holds week after week, and you are the one who explains the misses.
- When handing the deliverable back, name in one line the decision above that stays with the user.
