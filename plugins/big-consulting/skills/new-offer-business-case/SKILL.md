---
name: new-offer-business-case
description: Builds a bottom-up business case for a new product, service, or offer, with adoption, pricing, cannibalization, costs, scenarios, sensitivity, and stage-gate kill criteria. Use when the user needs to decide whether to fund a new offer, prepare an investment request, or pressure-test a launch plan someone else built.
---

# New-Offer Business Case

## What this produces
A five-year model with three scenarios, NPV and payback, a sensitivity ranking, and stage gates with kill criteria.

## Inputs to ask for
- Offer description, target segment, and intended price or pricing model.
- Addressable accounts in the target segment (a count).
- Adoption evidence: pilots, letters of intent, analog launches.
- Costs: build, launch, selling, cost to serve, support.
- Offers this could cannibalize, and the hurdle rate (default 10%, labeled).

## Method
1. Build revenue bottom-up: addressable accounts x reachable share x adoption by year x price x retention. Use top-down share math only as a sanity check.
2. Base adoption on the closest analog (a prior launch, pilot conversion); if none, use a conservative slope and say so.
3. Subtract cannibalization at the margin difference. Build costs as one-time, variable per customer, and fixed run.
4. Run three scenarios: downside, base, upside. Each varies adoption, price, and cost to serve together.
5. Compute NPV, IRR, payback, and peak cash requirement for each scenario.
6. Run sensitivity: move each major assumption plus or minus 20% and rank by NPV impact. The top three are the assumptions the stage gates must test.
7. Using McGrath and MacMillan's discovery-driven planning, work in reverse: the adoption and price required to clear the hurdle rate, against the evidence.
8. Set stage gates: at each gate, the metric, the threshold to continue, and the spend released.

## Output format
1. One-paragraph recommendation (fund, fund a test, or stop).
2. Scenario table: Metric | Downside | Base | Upside (revenue Y1 to Y5, NPV, IRR, payback, peak cash).
3. Sensitivity table: Assumption | Base Value | NPV Impact at +/-20% | Evidence Quality.
4. Stage-gate plan: Gate | Date | Metric | Continue If | Spend Released.

## Quality checks
- Revenue is built from account counts; a "1% of the market" line fails this check.
- Cannibalization is included, even if zero with a reason.
- Every assumption has a source or is labeled a judgment.
- The downside moves adoption, price, and cost to serve against you at once.

## Notes from the source article
- **Replaces:** The business-case phase for a new offer: the revenue model, costs, scenarios, and stage gates behind the investment committee deck.
- **Example request:** “We want to launch a managed-inventory service for our top distributors. Here’s the pilot data and cost estimates. Build the case and tell me what would have to be true to clear 12%.”
- **What the user still owns:** Enforcing the kill criteria when the first gate misses. The math is the easy part. The hard part is stopping a project that has a sponsor attached.
- When handing the deliverable back, name in one line the decision above that stays with the user.
