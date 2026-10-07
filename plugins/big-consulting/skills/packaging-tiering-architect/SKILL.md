---
name: packaging-tiering-architect
description: Designs good-better-best packaging: sorts features into tiers, sets price steps and fences, and models customer migration and cannibalization. Use when the user is launching tiers, replacing one-size pricing, or deciding what goes in the base product versus paid add-ons.
---

# Packaging and Tiering Architect

## What this produces
A feature-by-tier matrix, tier prices, an add-on list, and a migration model showing revenue impact on current customers.

## Inputs to ask for
- Full feature or service list with unit cost to deliver each
- Usage data by feature
- Feature importance research, if any
- Current price and customer list with revenue and features used
- Competitor packaging
- If usage data is missing, have the user rate each feature and label outputs judgment-based

## Method
1. Classify each feature with Kano categories: must-be (expected in every tier), performance (more is better, good for tier steps), attractive (delighters, good for the top tier or add-ons). Mark features only one segment values as add-on candidates.
2. Build tiers around segments, not features. Each tier should map to a named buyer situation.
3. Put must-be features in the base. Use one or two performance features as each tier's reason to step up.
4. Set fences: the usage limits, service levels, or rights that stop a high-value customer from buying the lowest tier.
5. Price the tiers. Check each step ratio against the value added; the middle tier should look like the obvious choice.
6. Map every current customer to the tier they would land in based on current usage. Compute revenue at new prices versus today.
7. Flag customers facing increases over 10 percent or able to downgrade.

## Output format
- Feature matrix: Feature | Kano class | Base | Mid | Top | Add-on | Cost to deliver
- Tier table: Tier | Target buyer situation | Price | Step ratio | Fence
- Migration summary: Customers moving up / flat / down, revenue delta $ and %
- Top 10 customers at downgrade risk

## Quality checks
- No tier is defined only by a feature count
- Every fence is enforceable in contracts or the product
- Migration model totals match current revenue before price changes
- Downgrade exposure is stated, not buried

## Notes from the source article
- **Replaces:** The offer-architecture workstream: sorting features into good-better-best tiers and modeling where existing customers land.
- **Example request:** “Our managed services contract is one price for everyone. Here’s the service list and our customer usage. Design three tiers and show me what happens to revenue.”
- **What the user still owns:** Deciding which customers you will move and how, since a packaging change is also a sales conversation with every account you already have.
- When handing the deliverable back, name in one line the decision above that stays with the user.
