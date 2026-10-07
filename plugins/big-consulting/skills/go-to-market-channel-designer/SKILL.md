---
name: go-to-market-channel-designer
description: Designs which sales and delivery channels serve which customer segments and offers, based on channel economics, deal complexity, and buyer preference, and writes the rules that prevent channel conflict. Use when the user is launching into a new segment, rethinking field versus inside versus partner versus self-serve, or seeing sales cost grow faster than revenue.
---

# Go-to-Market Channel Designer

## What this produces
Channel economics, a segment-by-channel assignment, conflict rules, and a transition plan.

## Inputs to ask for
- Revenue, deal count, and average deal size by segment and current channel.
- Sales and marketing cost by channel: headcount, fully loaded cost per role, partner margins or fees, marketing spend.
- Cycle length, win rates, and buyer preference evidence (interviews, how customers bought last year).
- If channel cost is not tracked, build it from headcount and pay and label it estimated.

## Method
1. Candidates: field, inside, partners or resellers, distributors, marketplaces, self-serve digital.
2. Compute per channel: cost per deal, cost of sale as % of first-year revenue, customer acquisition cost (CAC), CAC payback in months on gross margin, and lifetime value to CAC (LTV:CAC).
3. Set thresholds with the user. Common starting heuristics: payback under 18 months, LTV:CAC of 3 or more, cost of sale under 30% of first-year revenue. Show which channels pass per segment.
4. Match by deal complexity: number of buyers involved, need for configuration or site visits, contract length. Complex, high-value deals justify field coverage; transactional deals move down-channel.
5. Where buyers prefer a channel the economics reject, flag it and price the cost of honoring the preference.
6. Write conflict rules: account ownership, deal registration, pricing floors by channel, and compensation for handoffs between channels.
7. Build a transition plan for accounts that move channels, with the revenue at risk and the service guarantee offered.

## Output format
1. Channel economics table: Channel | Cost per Deal | Cost of Sale % | CAC | Payback (Months) | LTV:CAC.
2. Assignment matrix: Segment x Offer, primary and secondary channel.
3. Conflict rules (numbered, under 10).
4. Transition plan: Accounts Moving | Revenue at Risk | Timing | Mitigation.

## Quality checks
- Every channel cost traces to an input or is labeled estimated.
- Each segment has exactly one primary channel.
- Transition revenue at risk is quantified.

## Notes from the source article
- **Replaces:** A channel strategy study: modeling cost to sell through field, inside, partner, and digital, matching channels to segments, and writing conflict rules.
- **Example request:** “Our field reps are spending half their time on USD 8K orders. Here are deal data and sales costs by rep. Design which customers belong in field, inside sales, distributors, and online.”
- **What the user still owns:** The people side. Reassigning accounts changes someone’s paycheck, and those conversations are leadership work.
- When handing the deliverable back, name in one line the decision above that stays with the user.
