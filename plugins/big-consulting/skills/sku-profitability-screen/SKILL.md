---
name: sku-profitability-screen
description: Calculates fully loaded SKU profitability including complexity costs, tests substitution and customer dependency, and recommends keep, reprice, minimum order, make-to-order, or delist. Use when the catalog has grown faster than revenue, before a portfolio review, or when inventory and changeovers keep rising.
---

# SKU Profitability Screen

## What this produces
A SKU table with loaded margin, class, recommendation, and net P&L effect, plus SKUs top customers depend on.

## Inputs to ask for
- By SKU: units, net revenue, standard cost, variances, launch date, category
- Inventory on hand, write-offs, and obsolescence by SKU
- Changeovers by SKU; customer-by-SKU sales matrix
- Cost of capital and storage cost, for carrying cost
If carrying cost is unknown, use 20% of inventory value per year and label it an assumption.

## Method
1. Fully loaded margin = standard margin minus inventory carrying cost, write-offs, and changeover cost attributable to the SKU.
2. Find the tail: SKUs making up the bottom 5% of revenue. Report count and share of inventory.
3. Classify: Core, Strategic (launched in the last 24 months or with a stated portfolio role), Tail profitable, Tail unprofitable.
4. For each tail SKU, name a substitute and a transfer rate (revenue that moves to it). Default 50%, labeled.
5. Flag any candidate bought by a top-20 customer.
6. Net effect = minus lost margin x (1 minus transfer rate), plus freed variable cost. Count changeover savings only if capacity is constrained or overtime goes away.
7. Recommend: Keep, Reprice, Minimum order, Make-to-order, or Delist.

## Output format
- Table: SKU | Revenue | Standard margin | Complexity cost | Loaded margin | Class | Substitute | Transfer % | Top-customer flag | Recommendation | Net effect
- Summary: SKUs by recommendation, total net effect, inventory released
- List of top-customer-flagged SKUs for sales review

## Quality checks
- Fixed cost counts as saved only where it is actually removed
- Every transfer rate is sourced or labeled an assumption
- Strategic SKUs are excluded from delist unless the user overrides
- Net effect includes lost margin as well as cost saved

## Notes from the source article
- **Replaces:** The complexity workstream that loads each SKU with hidden costs and brings a delist list to a product committee.
- **Example request:** “We have 4,200 active SKUs and sliding margins. Here’s SKU sales, cost, and inventory. What should we cut, and what is it worth?”
- **What the user still owns:** The product managers, and the customers who call when their SKU disappears. Defending the list is a leadership job.
- When handing the deliverable back, name in one line the decision above that stays with the user.
