---
name: strategic-workforce-planner
description: Projects workforce supply and demand for critical roles over 3 to 5 years from the business plan, headcount, attrition, and retirement data, then recommends how to close each gap. Use when the user is planning growth, facing retirements or hard-to-fill roles, or needs headcount plans tied to business drivers.
---

# Strategic Workforce Planner

## What this produces
A demand and supply projection for critical role families, the gap by year, and a gap-closing plan with cost and lead time for each move.

## Inputs to ask for
- Business plan volumes by year (revenue, units, sites, customers).
- HRIS export: role, location, hire date, birth year or retirement eligibility, pay.
- Trailing 2-year attrition and time-to-fill by role family.
- If attrition data is missing, use the user's estimate and label it.

## Method
1. Pick critical role families: those with high value per role, long time-to-fill, or scarce supply. Limit to 5 to 10.
2. Model demand from drivers: role headcount = business volume / productivity ratio (for example, accounts per manager). Adjust productivity for planned automation or AI.
3. Model supply: current headcount minus attrition, minus retirements (using eligibility and historical retirement rates), plus internal promotions in.
4. Gap = demand minus supply by year and role family.
5. For each gap, compare responses: build (develop internally), buy (hire), borrow (contractors, partners), and automate. Compare cost per FTE-equivalent and lead time against when the gap opens.
6. Run a downside and upside volume case.

## Output format
1. Critical roles and why each qualifies.
2. Projection table: Role Family | Year | Demand | Supply | Gap.
3. Gap-closing plan: Role | Gap | Response | Cost | Lead Time | Start By.
4. Sensitivity on volume cases.

## Quality checks
- Demand ties to a stated driver and productivity ratio.
- Start-by dates account for lead time.
- Attrition and retirement assumptions are shown by role family.

## Notes from the source article
- **Replaces:** A workforce planning engagement, when a team projects talent supply against demand driven by the business plan and recommends build, buy, or borrow moves for the critical roles.
- **Example request:** “We plan to open four new plants by 2029 and a third of our maintenance techs can retire in five years. Build the workforce plan for our critical roles.”
- **What the user still owns:** Funding the build options before the gap is visible. Training pipelines must start years before the shortage shows up in a budget.
- When handing the deliverable back, name in one line the decision above that stays with the user.
