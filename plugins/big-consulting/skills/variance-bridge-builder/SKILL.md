---
name: variance-bridge-builder
description: Builds a budget-to-actual or forecast-to-actual variance bridge, decomposing each material variance into volume, rate, mix, timing, and one-off effects with plain-language commentary. Use during month-end or quarter-end reporting, when preparing variance commentary for executives, or when a variance explanation keeps changing.
---

# Variance Bridge Builder

## What this produces
A plan-to-actual waterfall bridge, a decomposition of each material variance, and executive commentary on what it means for the full year.

## Inputs to ask for
- Plan (budget or latest forecast) and actuals by line for the period (attach spreadsheet)
- Volume and rate data behind the plan (units, headcount, prices) where available
- The materiality threshold (default: 5% of the line or a stated dollar amount)
- Any known one-offs, reclasses, or timing items
If volume data is missing, bridge at line level and flag which variances cannot be decomposed.

## Method
1. Compute variance by line; keep only those above the materiality threshold, and group the rest as "other".
2. Decompose each material variance: volume effect = (actual volume minus plan volume) x plan rate; rate effect = (actual rate minus plan rate) x actual volume; mix where multiple products or segments exist.
3. Separate timing (will reverse within the year) from permanent variances. Label reclasses as non-economic.
4. Isolate one-offs and state them separately so the underlying run rate is visible.
5. For each permanent variance, state the full-year impact if it persists.
6. Write commentary per line in three parts: what happened, why, what it does to the full year.

## Output format
- Bridge table: Step | Driver | Amount | Timing or Permanent
- Waterfall description (start, steps in descending size, end)
- Commentary per material line, 60 words maximum each
- Full-year impact summary

## Quality checks
- The bridge steps sum exactly to the total variance
- Volume plus rate plus mix equals each line's variance
- Every one-off is named, never buried in "other"
- "Other" is under 10% of the total variance

## Notes from the source article
- **Replaces:** The monthly scramble where FP&A analysts pull actuals against budget, chase business leads for explanations, and turn the answers into a waterfall and commentary for the executive pack.
- **Example request:** “We missed Q2 EBITDA by USD 1.8M against budget. Budget and actuals attached. Build the bridge and write the commentary for the CFO.”
- **What the user still owns:** Calling a timing variance permanent when the business lead insists it will come back. The bridge shows the math; your credibility rides on the label.
- When handing the deliverable back, name in one line the decision above that stays with the user.
