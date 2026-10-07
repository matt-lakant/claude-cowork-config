---
name: inventory-policy-setter
description: Sets inventory policy by segmenting SKUs (ABC and demand variability) and calculating safety stock, reorder points, and order quantities against current stock. Use when inventory is high but service is poor, when setting warehouse stocking rules, or before committing to an inventory reduction target.
---

# Inventory Policy Setter

## What this produces
A SKU segmentation, safety stock, reorder point, and order quantity per SKU, and the inventory impact against today.

## Inputs to ask for
- 12 to 24 months of demand by SKU by week or month (attach CSV)
- Lead times by SKU (with variability), unit cost, on-hand
- Target service levels, or permission to propose them by segment
If lead-time variability is missing, assume zero and note that safety stock is understated.

## Method
1. Segment ABC by annual value (A about 80% of value) and XYZ by demand variability (coefficient of variation: X under 0.5, Y 0.5 to 1, Z above 1).
2. Set service targets by segment, e.g., AX 98%, CZ 90%. Convert these cycle service levels (odds of no stockout per cycle) to z: 95% = 1.65, 98% = 2.05, 99% = 2.33.
3. Safety stock = z x square root of (lead time x demand variance + average demand squared x lead time variance), in consistent time units.
4. Reorder point = average demand x lead time + safety stock.
5. Order quantity: economic order quantity = square root of (2 x annual demand x order cost / unit carrying cost), adjusted for minimums and pack sizes.
6. Compare target average inventory (safety stock + half the order quantity) with on-hand; flag excess and SKUs with no demand in 12 months.

## Output format
- Segment summary: Segment | SKUs | Value | Service target | Current days | Target days
- SKU policy table (top 50 by value): SKU | Segment | Safety stock | Reorder point | Order quantity | Current on-hand | Gap
- Impact: inventory change in dollars, excess and obsolete list

## Quality checks
- Time units match across demand and lead time
- Z-segment SKUs are flagged for make-to-order review
- Dollar impact reconciles to SKU-level totals

## Notes from the source article
- **Replaces:** An inventory optimization study: analysts segmenting SKUs, setting safety stock and reorder points, and sizing the inventory reduction.
- **Example request:** “We carry USD 40M of inventory and still stock out. Demand and lead time data attached. Set the policy and tell me what inventory should be.”
- **What the user still owns:** The service targets. Choosing 90% on a line means disappointing some customers, and sales must agree.
- When handing the deliverable back, name in one line the decision above that stays with the user.
