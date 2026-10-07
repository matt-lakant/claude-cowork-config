---
name: build-buy-partner
description: Compares building, buying, or partnering for a capability using differentiation, total cost, time to value, control, and risk, and recommends one path with conditions. Use when the user is deciding whether to build software or AI in-house, license a product, or engage a partner or managed service.
---

# Build, Buy, or Partner Decision

## What this produces
An options comparison, a five-year total cost view per option, and a recommendation memo with the conditions that would change it.

## Inputs to ask for
- The capability and the business outcome it serves
- Whether it differentiates the company or is standard practice for the industry
- Internal team capacity and skills
- Vendor or partner options and quotes, if any
- Required timeline and integration points
- If no market options have been identified, list the categories to research and stop before scoring buy

## Method
1. Test differentiation first. If customers would not pay more or choose you because of this capability, buying is the default.
2. Define options concretely: build (team, stack, timeline), buy (named product category, configuration, integration), partner (who does what, who owns the IP and the data).
3. Build five-year total cost per option: build includes staff, hosting, maintenance, and the cost of keeping skills; buy includes licenses at scale, implementation, integration, and price escalation; partner includes fees, transition, and exit cost.
4. Score time to first value and time to full value.
5. Score control: data ownership, roadmap influence, ability to switch, and exposure to vendor lock-in.
6. Score risk: delivery risk, vendor viability, key-person dependency, security.
7. Recommend, and name the trigger that would reverse the decision (volume, cost, vendor roadmap).

## Output format
- Options table: Criterion | Build | Buy | Partner, with weights
- Five-year cost table by option and year
- Recommendation memo, under 300 words, with reversal triggers

## Quality checks
- Differentiation is argued, not asserted
- Build cost includes maintenance after launch
- Exit cost is included for buy and partner
- Weights are shown and were set before scoring

## Notes from the source article
- **Replaces:** The sourcing-options analysis a technology strategy team runs before a major capability investment: options, criteria, cost comparison, and recommendation.
- **Example request:** “Our team wants to build our own AI quoting tool. Two vendors sell something close. Here’s what we know. Should we build, buy, or partner?”
- **What the user still owns:** Deciding what is truly core to your business, and living with that decision for five years.
- When handing the deliverable back, name in one line the decision above that stays with the user.
