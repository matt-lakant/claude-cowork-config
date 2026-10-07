---
name: price-waterfall-leakage
description: Builds a pocket price waterfall from list price to pocket margin and finds where revenue leaks through on-invoice and off-invoice concessions. Use when the user attaches invoice data and asks where margin is going, which customers are overdiscounted, or how much price leakage exists.
---

# Price Waterfall and Leakage Finder

## What this produces
A pocket price waterfall by segment, a pocket price band by customer, and ranked leakage items in dollars.

## Inputs to ask for
- 12 months of invoice lines (customer, SKU, date, quantity, list, invoice price) as CSV or XLSX
- Off-invoice items: rebates, co-op funds, absorbed freight, payment-term discounts, free goods
- Standard cost by SKU
- If off-invoice data is missing, build the on-invoice waterfall and list each missing element as a named gap for the user to estimate

## Method
1. Define layers: list, on-invoice discounts, invoice price, off-invoice items, pocket price, cost, pocket margin.
2. Allocate every off-invoice dollar to customer and SKU on its actual basis where one exists; otherwise by revenue share, flagged.
3. Compute each layer as percent of list, by segment, channel, and region.
4. Build the pocket price band for the top 20 SKUs: pocket price per unit across customers. A spread over 20 percent of the median signals leakage.
5. Regress pocket discount on annual customer volume. Customers far above the fitted line are off-policy.
6. Size the prize: move each off-policy customer to the line; sum by customer and element.
7. Separate earned concessions (tied to a documented commitment) from unearned ones.

## Output format
- Waterfall table: Layer | $ total | % of list | Best segment % | Worst segment %
- Top 25 off-policy customers: Customer | Volume | Pocket discount % | Fitted discount % | Gap $ | Primary leakage element
- Summary paragraph: total leakage $, top three elements, recoverable range

## Quality checks
- Waterfall reconciles to reported net revenue within 1 percent, or the gap is shown
- Every allocated item is labeled actual or allocated
- Recoverable estimate is framed as a range, never a point figure
- No customer is flagged off-policy on fewer than three months of data

## Notes from the source article
- **Replaces:** The first month of a pricing engagement: analysts joining invoice lines to rebate and freight ledgers to show what each customer really pays.
- **Example request:** “Here’s last year’s invoice export and rebate accruals. Build the price waterfall and tell me which customers get more than they earn.”
- **What the user still owns:** Deciding which of those customers you are willing to lose, and holding the line when their sales rep argues the relationship is special.
- When handing the deliverable back, name in one line the decision above that stays with the user.
