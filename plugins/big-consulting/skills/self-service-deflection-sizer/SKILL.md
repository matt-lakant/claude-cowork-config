---
name: self-service-deflection-sizer
description: Screens contact reasons for self-service or automation fit, estimates realistic containment and adoption, and sizes net savings after build and run cost. Use when the user is evaluating a portal, chatbot, AI agent, IVR, or FAQ investment, or needs to challenge a vendor's deflection claims.
---

# Self-Service Deflection Sizer

## What this produces
A fit score for each contact reason, a realistic deflection estimate by reason, net savings by year, and the top 10 self-service builds in priority order.

## Inputs to ask for
- Contact volume, handle time, and channel by reason (a contact driver analysis if available).
- Cost per assisted contact by channel and cost per self-service transaction.
- Current self-service usage and success rates, if any.
- Build and run costs for the proposed tools, or vendor quotes.

## Method
1. Remove failure demand first: contacts that should be eliminated at the source are not deflection candidates.
2. Score each remaining reason 1 to 5 on: simplicity, data availability (can the system answer without an agent), emotional stakes (reverse scored), authentication needs, and regulatory limits.
3. Set containment assumptions by fit tier as editable inputs. Starting heuristics: high fit 40 to 60%, medium 15 to 30%, low under 10%.
4. Apply an adoption ramp over 12 to 18 months; customers will not shift channels on day one.
5. Net savings = deflected contacts x (assisted cost minus self-service cost), minus build and run cost, minus leakage (failed self-service attempts that come back as longer assisted contacts).
6. Rank builds by net savings per dollar of build cost.

## Output format
1. Fit table: Reason | Volume | Fit Score | Tier | Containment Assumption.
2. Savings by year: Year | Deflected Contacts | Gross Savings | Costs | Leakage | Net.
3. Top 10 builds with savings and cost.
4. Assumptions to validate in a pilot.

## Quality checks
- Leakage is modeled, even if estimated.
- Vendor containment claims are shown against the tiered assumptions.
- Savings convert to FTE only after shrinkage and occupancy.

## Notes from the source article
- **Replaces:** The digital self-service business case, when a team screens every contact reason for self-service fit, estimates realistic adoption, and sizes the savings.
- **Example request:** “A vendor says their AI agent will deflect 70% of our calls. Here’s our volume by reason and cost per call. Tell me what’s realistic and what it’s worth.”
- **What the user still owns:** The customer experience when self-service fails. Savings that come from making agents hard to reach show up later as churn.
- When handing the deliverable back, name in one line the decision above that stays with the user.
