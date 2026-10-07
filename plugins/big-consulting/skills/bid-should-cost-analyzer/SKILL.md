---
name: bid-should-cost-analyzer
description: Normalizes supplier bids into a comparable total cost view, builds a should-cost model from material, labor, overhead, and margin, and sets negotiation targets per supplier. Use when RFP responses arrive, when bids come in inconsistent formats, or when a sole supplier's price looks high.
---

# Bid Comparison and Should-Cost Analyzer

## What this produces
A normalized bid comparison on total cost of ownership, a should-cost breakdown for the main items, and target prices for the next round.

## Inputs to ask for
- All bid submissions (attach spreadsheets or PDFs)
- Annual volumes and the evaluation scoring results
- Bill of materials or service composition for main items
- Cost references: material indices, regional labor rates
If cost references are missing, build the should-cost with labeled assumptions and show sensitivity.

## Method
1. Normalize bids to one basis: same volumes, currency, Incoterms, payment terms, and contract length. Convert payment terms to a cost using the company's cost of capital.
2. Add total cost of ownership items: freight, duties, quality costs, transition, inventory carrying.
3. Rank bids on total cost alongside the scoring results.
4. Build should-cost for items covering most of the spend: material (quantity x index price), labor (hours x regional rate), overhead (share of conversion cost), SG&A and margin (typical range for the industry, labeled).
5. Compare each bid with should-cost and with the lowest compliant bid, item by item. Flag gaps above 10%.
6. Set round-two targets per supplier: item-level asks with the evidence behind each.

## Output format
- Comparison grid: Supplier | Unit price total | TCO adjustments | Total cost | Score | Rank
- Should-cost table: Item | Material | Labor | Overhead | Margin | Should-cost | Best bid | Gap
- Negotiation targets: Supplier | Item | Current | Target | Evidence

## Quality checks
- All bids use identical volumes and terms after normalization
- Should-cost assumptions are labeled with sources
- The lowest price is not recommended if it fails a mandatory requirement

## Notes from the source article
- **Replaces:** The bid analysis after an RFP closes: analysts normalizing submissions into one grid, building a should-cost model, and setting targets for the next round.
- **Example request:** “Five bids came back on our machined parts RFP, all in different formats. Normalize them and tell me what each part should actually cost.”
- **What the user still owns:** Deciding when cheap is too cheap. A bid far below should-cost often returns as a change order once you depend on that supplier.
- When handing the deliverable back, name in one line the decision above that stays with the user.
