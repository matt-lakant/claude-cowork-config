---
name: deal-value-sizer
description: Sizes the cost savings and revenue gains from combining two companies bottom-up, nets out the negative effects and one-time costs, phases them to run rate, and tests whether they cover the premium paid. Use when building or challenging an acquisition model, setting integration targets, or when someone asks "do the savings justify the price?"
---

# Deal Value Sizer

## What this produces
A lever-by-lever model of cost and revenue benefits, the one-time costs to achieve them, a quarterly phasing, and a premium coverage test.

## Inputs to ask for
- Both companies' cost baselines by function: headcount, compensation, third-party spend
- Revenue by customer and product for both
- Overlap data: sites, vendors, customers, systems
- Purchase price, premium over standalone value, and target close date
If one side's data is thin, size from the other side's ratios and label it ESTIMATED.

## Method
1. Confirm both baselines share a period and cost definitions.
2. Cost levers, each sized from a named driver: duplicate roles, site consolidation, vendor price harmonization to the better contract on overlapping spend, system retirement, duplicate public-company or corporate costs.
3. Revenue levers: cross-sell (addressable customers x attach rate x price), new geography, pricing. Give them a longer ramp and a probability weight, and keep them out of the price justification unless the user says otherwise.
4. Negative effects: customers lost to overlap, key-talent attrition, dual-running costs, retention bonuses.
5. One-time costs: severance, lease exits, system migration, outside help. Compare the total to annual run-rate savings.
6. Phase by quarter to full run rate. Compute NPV of net benefits and compare to the premium.
7. Rate each lever: identified, validated, or committed by a named owner.

## Output format
- Table: Lever | Type | Driver | Run-rate value | One-time cost | Quarter at run rate | Confidence
- Quarterly phasing table
- Premium coverage: NPV of cost levers alone, then with revenue levers, versus the premium
- Sensitivity on the top three levers

## Quality checks
- No savings counted twice (for example, a role in both headcount and function totals)
- Revenue gains reported separately from cost savings
- Every lever has a driver and a confidence rating

## Notes from the source article
- **Replaces:** The combination-benefits model a deal team builds during diligence to defend the purchase price.
- **Example request:** “We’re paying a 30% premium for a competitor with four overlapping plants. Here are both cost baselines and the customer files. Size the savings and tell me if they cover it.”
- **What the user still owns:** Committing to the number. Once it is in the board approval it becomes someone’s target, and the owners have to believe it first.
- When handing the deliverable back, name in one line the decision above that stays with the user.
