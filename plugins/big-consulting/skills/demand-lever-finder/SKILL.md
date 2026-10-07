---
name: demand-lever-finder
description: Sizes consumption savings for a spend category through policy, frequency, specification, substitution, and elimination levers, scored for user impact and time to savings. Use when price negotiation has run out of room, for categories like travel, contractors, software, fleet, print, or mobile, or when spend grows with headcount.
---

# Demand Lever Finder

## What this produces
A lever matrix for one category: baseline, savings, user impact, enforcement, and months to realize.

## Inputs to ask for
- 12 months of category spend with units (trips, seats, hours, devices, service visits)
- Current policy documents and approval thresholds
- Who consumes it: by role, department, or site
- Service levels or specifications in current contracts
If units are missing, ask for them; demand levers cannot be sized on dollars alone.

## Method
1. Write the category equation: spend = eligible users x frequency x specification x rate.
2. Policy levers: tighten eligibility (who may buy), approval thresholds, and pre-trip or pre-purchase approval.
3. Frequency levers: reduce how often (cleaning cycles, report refreshes, device refresh from 3 to 4 years, meeting travel).
4. Specification levers: lower grade or tier (economy class, standard laptop, lower SLA, fewer premium licenses).
5. Substitution and elimination: video in place of travel, shared pools in place of assigned assets, stopping unused services.
6. Size each lever: baseline units x expected reduction % x rate. Label every reduction % as an estimate with a basis.
7. Score user impact 1 to 5, enforcement mechanism (system block, approval, report), and months to savings.

## Output format
- Category equation with baseline values
- Lever table: Lever | Type | Baseline units | Reduction % | Annual savings | User impact | Enforcement | Months to savings
- Top five levers ranked by savings per point of user impact
- Policy text changes, drafted

## Quality checks
- Every lever changes a term in the category equation
- Levers are not stacked beyond 100% of any baseline
- Each lever names how it will be enforced
- Savings shown are consumption only, with no price effects mixed in

## Notes from the source article
- **Replaces:** The demand-management workstream: who may buy, how often, and to what specification.
- **Example request:** “Travel is USD 6.2M and climbing. Here’s the booking data and our policy. What can we save without renegotiating with the airlines?”
- **What the user still owns:** The exceptions. Every policy lever creates a line of executives asking to be excused.
- When handing the deliverable back, name in one line the decision above that stays with the user.
