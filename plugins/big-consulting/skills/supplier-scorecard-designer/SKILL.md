---
name: supplier-scorecard-designer
description: Designs and populates a weighted supplier scorecard covering quality, delivery, cost, responsiveness, and risk, with thresholds and consequences. Use when setting up supplier performance management, preparing a quarterly business review, or deciding which suppliers to grow, fix, or exit.
---

# Supplier Scorecard Designer

## What this produces
A scorecard design with metric definitions and weights, populated scores for each supplier, and a grow, fix, or exit recommendation per supplier.

## Inputs to ask for
- Receipt and delivery data: promised vs actual dates, quantities (attach CSV)
- Quality data: rejects, defects in parts per million, returns
- Price and invoice data, plus any service tickets or complaints
- The suppliers in scope and their annual spend
If a metric has no data source, keep it in the design, mark it "not yet measured," and exclude it from the weighting.

## Method
1. Select five dimensions: quality, delivery, cost, responsiveness, risk. Weight them by category (a critical component weights quality and delivery highest).
2. Define each metric with a formula: on-time in-full = orders delivered complete on the promised date / total orders; defect rate in parts per million; price variance to contract.
3. Set thresholds: green, amber, red, based on contract service levels or internal targets.
4. Calculate each supplier's scores for the last four quarters and show the trend.
5. Segment suppliers by spend and score: high spend and low score is the priority for corrective action.
6. Recommend per supplier: grow, maintain, corrective action plan, or exit, with the evidence.

## Output format
- Metric dictionary: Metric | Formula | Source | Weight | Green/Amber/Red thresholds
- Scorecard: Supplier | Spend | Quality | Delivery | Cost | Responsiveness | Risk | Total | Trend
- Recommendations: Supplier | Action | Evidence

## Quality checks
- Weights sum to 100% within each category
- On-time in-full counts partial deliveries as misses
- Every recommendation cites its scores

## Notes from the source article
- **Replaces:** The supplier performance program: consultants defining metrics, weights, and data sources, then building the quarterly business review scorecard procurement never had time to set up.
- **Example request:** “Build a scorecard for our top 30 suppliers from the receipts and quality data attached, and tell me who needs a corrective action plan.”
- **What the user still owns:** Following through on red scores. A scorecard with no consequence becomes wallpaper in the quarterly review.
- When handing the deliverable back, name in one line the decision above that stays with the user.
