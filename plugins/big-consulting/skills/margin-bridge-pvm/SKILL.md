---
name: margin-bridge-pvm
description: Decomposes a gross margin change between two periods into volume, mix, price, cost, FX, and portfolio effects with zero residual. Use when margin moved and leadership wants to know why, for quarterly reviews or earnings prep, or before blaming pricing or procurement.
---

# Margin Bridge

## What this produces
A reconciled bridge in dollars and margin points, top products per bar, and a waterfall chart spec.

## Inputs to ask for
- Two periods of data by product or SKU (CSV): units, net revenue, COGS, ideally COGS split into material, labor, freight, overhead
- Currency by line if multi-currency, and the FX rates used
- Known one-offs: inventory write-downs, recalls, standard-cost revaluations
With only segment data, bridge at segment level and note mix is understated.

## Method
1. Use net price (after discounts and rebates) and unit margin m = net price minus unit cost. Period 1 is the base.
2. Volume = (total units P2 minus total units P1) x average unit margin P1.
3. Mix = sum of units P2 x m P1, minus total units P2 x average m P1.
4. Price = sum of units P2 x (price P2 minus price P1).
5. Cost = minus sum of units P2 x (unit cost P2 minus unit cost P1), split by material, labor, freight, overhead absorption.
6. Pull new and discontinued products into their own bar; pull FX translation into its own bar at constant-currency rates.
7. Confirm the bars sum exactly to the change. Any residual is an error to find.
8. Rank the ten products driving each bar.

## Output format
- Bridge table: Start margin | Volume | Mix | Price | Material | Labor | Freight | Overhead absorption | FX | New/discontinued | One-offs | End margin
- Same bridge in margin percentage points
- Top-10 drivers per bar
- Waterfall chart spec; three-sentence summary

## Quality checks
- Residual is zero
- The same base period is used for every effect
- Overhead absorption is separated from true cost inflation
- One-offs are shown, never buried in cost

## Notes from the source article
- **Replaces:** The analyst who spends a week splitting a gross margin change into price, volume, mix, and cost for the CFO’s deck.
- **Example request:** “Gross margin fell 240 basis points year over year. Here’s SKU-level units, revenue, and COGS for both years. Bridge it.”
- **What the user still owns:** Deciding which bar to act on, and who owns getting that margin back.
- When handing the deliverable back, name in one line the decision above that stays with the user.
