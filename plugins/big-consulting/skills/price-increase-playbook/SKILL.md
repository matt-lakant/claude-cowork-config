---
name: price-increase-playbook
description: Plans a differentiated price increase across the customer base: segments by value and switching risk, sets increase levels, computes breakeven volume loss, and writes communication and objection-handling scripts. Use when the user needs to raise prices, pass through cost inflation, or fix underpriced legacy accounts.
---

# Price Increase Playbook

## What this produces
A segmented increase plan with dollar impact, breakeven analysis, customer letter, rep scripts, and a realization tracker.

## Inputs to ask for
- Customer list with revenue, margin, current price versus list, tenure, and products held
- Contract terms: price escalator clauses, notice periods, renewal dates
- Cost increase drivers and amounts, if the increase is cost-driven
- Known competitor price moves
- Contribution margin percent
- If contract terms are unknown, flag notice timing as unconfirmed

## Method
1. Compute breakeven volume loss for each candidate increase: breakeven loss = increase % divided by (contribution margin % + increase %). A 5 percent increase at 30 percent margin breaks even at about 14 percent volume loss.
2. Segment customers on two axes: price position (paying below, at, or above the peer band) and switching risk (share of their spend, alternatives available, tenure, contract lock). Four to six segments is enough.
3. Assign increases by segment: largest for below-band, low-risk customers; smallest or none for above-band, high-risk ones.
4. Sequence by contract date and notice requirements.
5. Write the customer letter: increase, effective date, reason in business terms.
6. Write rep scripts for the five most likely objections, with the allowed concession for each and the approval needed.
7. Define realization tracking: announced increase, achieved increase, and customers lost by segment, weekly for the first 90 days.

## Output format
- Segment table: Segment | Customers | Revenue $ | Increase % | Expected realization % | Net $ impact
- Breakeven table by increase level
- Timing calendar by month
- Customer letter template and five objection scripts
- Realization tracker columns

## Quality checks
- Total impact is shown after an assumed realization rate, not at 100 percent
- No customer is scheduled before their contractual notice window
- The letter gives a reason the customer can repeat to their own boss
- Each top-20 account has a named owner

## Notes from the source article
- **Replaces:** The price-increase program: segmenting the book, setting differentiated increases, scripting reps, and tracking what sticks.
- **Example request:** “Our input costs rose 7 percent and we haven’t moved price in two years. Here’s the customer file with contract dates. Build the increase plan.”
- **What the user still owns:** Calling the three customers who will threaten to leave, and deciding in advance how much churn you will accept.
- When handing the deliverable back, name in one line the decision above that stays with the user.
