---
name: profit-pool-mapper
description: Estimates how industry profit is distributed across value chain stages or segments, compares profit share with revenue share, and shows how the pool is shifting. Use when the user wants to know where the money is made in their industry, is choosing where to invest, or suspects they are competing for the low-margin part of the market.
---

# Profit Pool Mapper

## What this produces
A profit pool table and chart by stage or segment, today and in 3 to 5 years, with the user's share of each pool.

## Inputs to ask for
- Stage or segment list (reuse a value chain map if one exists)
- Revenue by stage: market sizes, association data, or estimates
- Filings of pure-play companies at each stage (attach PDFs)
- The user's revenue and operating profit by stage or segment
Where no pure-play exists, use segment disclosures of larger companies and mark confidence Low.

## Method
1. Pick one cut per chart: chain stages, customer segments, or products.
2. Estimate revenue per stage. Choose gross revenue or value added (revenue minus purchased inputs) and state it. Value added avoids double counting when stages are summed.
3. Take operating margin per stage from pure-play medians over three to five years to smooth the cycle. Use one margin measure throughout.
4. Profit = revenue x margin. Check the sum against any public figure for total industry profit.
5. Compute profit share minus revenue share per stage; large positive gaps mark where profit concentrates.
6. Repeat for a prior period and a forward estimate, naming the driver of each shift.
7. Place the user in each pool and flag overweight positions in shrinking pools.
8. In Claude Code, draw a variable-width bar chart: width = revenue share, height = operating margin, area = profit.

## Output format
- Table: Stage | Revenue | Revenue share | Operating margin | Profit | Profit share | Gap | Trend | Source | Confidence
- Chart, or a precise text description on claude.ai
- Shifts: 3 bullets
- User position: one paragraph

## Quality checks
- Revenue basis is stated and consistent
- Stage profits sum to a plausible industry total
- Margins are multi-year averages
- Every stage carries a source and confidence rating

## Notes from the source article
- **Replaces:** The profit pool exhibit that anchors a strategy deck: revenue and margin estimated at every stage, multiplied out, showing that the biggest revenue stage is rarely the most profitable.
- **Example request:** “Build a profit pool for residential solar: equipment, installation, financing, and servicing. I think installers like us hold half the revenue and a sliver of the profit, and I want numbers that prove or kill that.”
- **What the user still owns:** Whether you can realistically move toward the richer pool. Profit sits where it does for reasons, and only you can judge if your organization can compete there.
- When handing the deliverable back, name in one line the decision above that stays with the user.
