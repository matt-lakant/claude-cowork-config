---
name: discount-governance-designer
description: Designs a discount governance system: approval matrix by discount band and deal size, give-get trading rules, floor prices, and exception tracking. Use when reps discount too much, quarter-end deals give away margin, or discounts vary widely across similar customers.
---

# Discount Governance Designer

## What this produces
A one-page discount policy: approval matrix, give-get menu, and monthly compliance report spec.

## Inputs to ask for
- Deal-level data for 12 months: rep, customer, deal size, list, net price, discount %, close date, approver
- Current discount policy and approval levels, even if informal
- Target margin and any price floors
- Pocket price band results, if built
- If deal data is missing, design the policy from the current rules and flag that the thresholds are unvalidated

## Method
1. Profile current behavior: discount distribution by rep, segment, and deal size; share of revenue closing in the last two weeks of each quarter and its average discount versus the rest.
2. Set three price points per segment: target, floor (lowest a rep can offer alone), and hard floor (executive signoff). Anchor them to the observed band.
3. Build the approval matrix: discount bands down one axis, deal size across the other, approver in each cell. Keep it to four levels or fewer.
4. Write give-get rules: every discount beyond target must trade for a named customer commitment (longer term, volume commitment, prepayment, reference, faster payment). Assign each a discount value.
5. Design the exception log: fields, reviewer, frequency.
6. Define compliance metrics: percent of deals in policy, discount by rep versus peers, approval turnaround (slow approvals push reps to discount early).

## Output format
- Approval matrix table
- Give-get menu: Customer commitment | Discount it earns | How it is enforced
- Price points by segment: Target | Floor | Hard floor
- Monthly report spec: Metric | Definition | Threshold | Owner

## Quality checks
- The matrix has no gaps or overlapping cells
- Every give has an enforcement mechanism in the contract or billing
- Thresholds are traced to observed data or labeled judgment
- Approval turnaround target is stated

## Notes from the source article
- **Replaces:** The governance workstream: turning price-band findings into an approval matrix and give-get rules sales will follow.
- **Example request:** “Our reps are discounting 18 percent on average and half of it happens in the last week of the quarter. Here’s the deal data. Build us a discount policy with real approval levels.”
- **What the user still owns:** Enforcing it on your best rep in the last week of a quarter, which is the only moment the policy is actually tested.
- When handing the deliverable back, name in one line the decision above that stays with the user.
