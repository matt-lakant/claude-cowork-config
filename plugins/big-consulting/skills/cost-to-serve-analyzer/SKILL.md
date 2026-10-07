---
name: cost-to-serve-analyzer
description: Builds a customer-level P&L by allocating service costs (orders, freight, returns, service, sales coverage, terms) with activity drivers, then produces a whale curve and segment actions. Use when some customers feel expensive to serve, before renegotiating terms, or when revenue grows faster than profit.
---

# Cost-to-Serve Analyzer

## What this produces
Net contribution by customer, a whale curve, cost-pool rates, top loss-makers with drivers, and segment actions.

## Inputs to ask for
- Net revenue and gross margin by customer
- Order count and order lines, shipments with freight cost and expedite flag, returns, credits
- Service tickets by customer, sales visits, rebates, payment terms and actual days to pay
- P&L cost for each pool (order entry, warehouse, freight, service, sales, collections)
Where a driver is missing, allocate that pool on revenue and label it.

## Method
1. Start from gross margin after rebates by customer.
2. Define cost pools and one driver each: orders, lines, shipments, expedites, returns, tickets, visits, days of credit.
3. Rate = pool cost / total driver volume. Cost of terms = receivable balance x cost of capital.
4. Customer net contribution = gross margin minus the sum of driver volume x rate.
5. Show two views: variable service cost only, then with fixed overhead allocated.
6. Sort by net contribution and plot cumulative profit (the whale curve). Report what share of customers produces 100% of profit.
7. Place each customer on a 2x2 of net price versus cost-to-serve.
8. Actions by segment: minimum order sizes, surcharges, service tiers, channel shift, terms changes.

## Output format
- Pool table: Pool | Cost | Driver | Volume | Rate
- Customer table: Customer | Revenue | Gross margin | Cost-to-serve | Net contribution | % | Top cost driver
- Whale curve data; bottom 20 customers with drivers
- Action list: Segment | Action | Customers | Margin impact

## Quality checks
- Allocated pools reconcile to the P&L
- No customer is called unprofitable on fixed-overhead allocation alone
- Revenue-based fallback allocations are labeled
- Every action names a specific driver it changes

## Notes from the source article
- **Replaces:** A customer profitability study: allocating orders, freight, returns, and service tickets to customers to produce the whale curve slide.
- **Example request:** “Here’s last year’s customer sales, orders, shipments, and service tickets. Which accounts actually lose us money, and why?”
- **What the user still owns:** The conversation with the sales leader whose biggest account sits at the bottom of the curve.
- When handing the deliverable back, name in one line the decision above that stays with the user.
