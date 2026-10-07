---
name: market-sizing-triangulator
description: Sizes a market three independent ways (top-down, bottom-up, supply-side or analog), reconciles the gaps, and returns a defended range with an assumption log. Use when the user asks how big a market is, needs a TAM/SAM/SOM, is weighing entry or expansion, or wants a single analyst-report number pressure-tested.
---

# Market Sizing Triangulator

## What this produces
A one-page market size: point estimate, range, three methods side by side, and why they differ.

## Inputs to ask for
- Market definition: what is bought, by whom, where, for which year
- Analyst or association reports in hand (attach PDFs)
- Own revenue in the segment, customer counts, average contract value (CSV)
- A buyer universe (CRM export, industry census, target account list)
If an input is missing, use a labeled assumption and name the source that would replace it.

## Method
1. Define the market in one sentence plus exclusions. Fix price level (end-user spend vs manufacturer revenue) and currency. Separate TAM, SAM (what the offer can serve), and SOM (winnable in 3 to 5 years).
2. Top-down: a published total times filter ratios for segment, geography, and addressability. Source every ratio.
3. Bottom-up: buyers x adoption rate x annual spend per buyer, by segment. For business buyers, use establishment counts by industry code and size band.
4. Supply-side or analog: sum competitor revenues plus an estimated tail, or apply the penetration curve of a comparable product at the same age.
5. If the three land within about 25%, set the estimate and range. If wider, decompose the gap to its driver (usually definition, price level, or penetration) and fix it. Never average a gap you cannot explain.
6. Split growth into volume and price, each tied to a named driver.
7. Run sensitivity on the three highest-swing inputs.

## Output format
- Definition box
- Table: Method | Formula | Key inputs | Source | Result
- Reconciliation (under 150 words), final range, CAGR
- Sensitivity: Input | Low | Base | High | Resulting size
- Assumption log: ID | Assumption | Value | Basis | Confidence

## Quality checks
- Same year, currency, and price level in all three methods
- SOM at most SAM, SAM at most TAM, no double counting across segments
- Implied spend per buyer is plausible against the buyer's budget
- Every number is sourced or tagged as an assumption

## Notes from the source article
- **Replaces:** The first two weeks of a market entry study: one analyst builds a top-down number from syndicated reports, another counts buyers bottom-up, and a manager reconciles the two the night before the steering committee.
- **Example request:** “Size the US market for outsourced accounts-payable processing for companies between USD 50M and USD 1B in revenue. Our CRM export and the analyst report our vendor sent are attached.”
- **What the user still owns:** Choosing the definition that fits the decision you are making, and judging whether a market that size deserves the management attention it will cost.
- When handing the deliverable back, name in one line the decision above that stays with the user.
