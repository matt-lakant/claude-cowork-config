---
name: network-footprint-analyzer
description: Compares distribution or manufacturing footprint options on total landed cost, service level, capacity, and risk, using shipment, facility, and customer data. Use when considering opening, closing, or consolidating warehouses or plants, when freight costs are rising, or when a lease expiry forces a footprint decision.
---

# Network and Footprint Options Analyzer

## What this produces
A baseline of today's network cost and service, three to four footprint options scored on cost, service, capacity, and risk, and a recommendation with one-time costs and payback.

## Inputs to ask for
- 12 months of shipments: origin, destination (zip or city), weight, cost (attach CSV)
- Facility costs: lease, labor, overhead, capacity, lease expiry
- Demand by customer location and required delivery times
- Candidate locations under consideration
If candidates are not given, propose them from demand concentration and state the method.

## Method
1. Baseline: total cost by component (inbound freight, outbound freight, facility, inventory carrying) and share of demand served within each delivery-time band.
2. Map demand concentration: the share of volume within a day's drive of each facility.
3. Build options: status quo, consolidate, add a node, relocate. Keep to four.
4. For each option, estimate outbound freight from cost per mile or per pound by distance band from current shipment data, plus facility and inventory effects (fewer nodes usually means less safety stock).
5. Estimate one-time costs: moves, severance, fit-out, dual running, and calculate payback.
6. Score service, capacity headroom, and risk (single points of failure, labor market).

## Output format
- Baseline table by cost component and service band
- Options table: Option | Annual cost | Change vs baseline | Service in band % | One-time cost | Payback | Risk
- Recommendation and the assumptions that would change it

## Quality checks
- Freight estimates are calibrated to actual shipment costs
- Options meet required delivery times or show the shortfall
- This is a screening analysis; flag if a full optimization model is warranted

## Notes from the source article
- **Replaces:** A network strategy study: consultants modeling warehouses and plants, freight lanes, and service times to compare footprint options and recommend where to open, close, or consolidate.
- **Example request:** “Our Dallas warehouse lease is up in 18 months. Here’s a year of shipments and our facility costs. Compare keeping it, moving it, or consolidating into Memphis.”
- **What the user still owns:** The people in a closing building and the customers who feel the change. The model counts neither goodwill nor disruption.
- When handing the deliverable back, name in one line the decision above that stays with the user.
