---
name: supplier-resilience-mapper
description: Maps critical items to suppliers and locations, scores each on concentration, geography, financial health, and time to recover, and builds mitigation plans for the highest exposures. Use when a supply disruption has hit or threatens, when a board asks about supply chain risk, or when a key supplier looks unstable.
---

# Supplier Resilience Mapper

## What this produces
An exposure map of critical items and suppliers, a risk score per item, revenue at risk, and a mitigation plan for the top exposures.

## Inputs to ask for
- Bill of materials or item list with suppliers, manufacturing locations, and spend (attach CSV)
- Which finished products or revenue lines each item supports
- Current inventory cover and qualification time for alternates
- Known issues: single-source items, supplier financial concerns, regional risks
If supplier sites are unknown, list them as data requests and score location risk as unknown.

## Method
1. Identify critical items: those whose absence stops shipment of material revenue.
2. For each, record source count (single, sole, multiple), site locations, and any known sub-tier dependency.
3. Estimate time to recover (weeks to qualify and ramp an alternate) against time to survive (weeks of inventory and buffer). When recover exceeds survive, the item is exposed.
4. Calculate revenue at risk: weekly revenue dependent on the item x exposure gap in weeks.
5. Score financial health and geographic concentration from facts provided; label judgments.
6. Choose mitigations per exposure: dual source, buffer stock, design change, supplier development, or contractual protections, with cost and time.

## Output format
- Exposure table: Item | Supplier(s) | Sites | Source type | Time to survive | Time to recover | Revenue at risk
- Top 10 exposures ranked by revenue at risk
- Mitigation plan: Item | Action | Cost | Time | Owner

## Quality checks
- Single-source (by choice) is distinguished from sole-source (only one exists)
- Revenue at risk shows its calculation
- Mitigation cost is compared with revenue at risk

## Notes from the source article
- **Replaces:** A supply risk assessment: consultants mapping critical parts to suppliers and sub-tier sources, scoring concentration and exposure, and building mitigation plans after a disruption scare.
- **Example request:** “After last year’s port delays, the board wants to know where we’re exposed. Here’s our BOM with suppliers. Map the risk and tell me what to fix first.”
- **What the user still owns:** How much insurance to buy. Dual sourcing and buffer stock cost money every year to guard against something that may not happen.
- When handing the deliverable back, name in one line the decision above that stays with the user.
