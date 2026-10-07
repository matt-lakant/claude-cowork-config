---
name: contract-leakage-finder
description: Compares invoices and purchase orders against contract terms to find price leakage, off-contract (maverick) spend, missed rebates and volume discounts, and payment-term breaches, and sizes recovery. Use when invoices seem higher than the deals negotiated, when contracted rebates or discounts may be going unclaimed, or during an AP or spend review. For validating total program savings against a baseline, use a savings validation pass instead.
---

# Contract Compliance and Leakage Finder

## What this produces
A leakage register by type and supplier, a recovery estimate, and fixes to stop future leakage.

## Inputs to ask for
- Invoice or AP line data: supplier, item, quantity, unit price, date, payment date (attach CSV)
- Contract terms: price lists, tiers, rebates, discounts, payment terms (attach contracts or summaries)
- Preferred supplier list by category
If contracts are PDFs, extract the price and term fields first and confirm them with the user.

## Method
1. Price compliance: match invoice unit price to contract price by item and date; leakage = (invoice minus contract) x quantity.
2. Maverick spend: spend in contracted categories paid to non-preferred suppliers, sized by the price gap to the contracted supplier.
3. Rebates and tiers: compare cumulative volume with rebate and tier thresholds; calculate earned but unclaimed amounts.
4. Payment terms: payments made earlier than terms, and early-payment discounts not taken.
5. Other: duplicate invoices, fees not in the contract, escalations applied early or above the index.
6. Rank recovery by amount and ease; separate recoverable from supplier (overcharges, rebates) and preventable internally (maverick, early payment).

## Output format
- Leakage summary: Type | Suppliers | Amount | Recoverable Y/N
- Detail register: Supplier | Invoice | Item | Contract price | Paid | Leakage
- Fixes: Control | Owner | Leakage prevented

## Quality checks
- Contract prices are matched by effective date
- Duplicate checks exclude legitimate repeat orders
- Recovery claims cite the contract clause

## Notes from the source article
- **Replaces:** A post-sourcing leakage review: analysts matching invoices against contract prices, finding off-contract spend, missed rebates, and unapplied discounts, then recovering what is owed.
- **Example request:** “We renegotiated our MRO contracts last year, but invoice prices don’t look like what we signed. AP data and contract price lists attached. Find where it’s leaking.”
- **What the user still owns:** How hard to chase recoveries. Clawing back overcharges from a strategic supplier is right, and the timing and tone are yours.
- When handing the deliverable back, name in one line the decision above that stays with the user.
