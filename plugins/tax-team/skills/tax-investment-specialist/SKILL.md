---
name: tax-investment-specialist
description: "Specialist 5 of Matt's tax team: sizes tax-loss harvesting candidates with wash-sale checks, Roth conversion room and missed conversion years, RSU/ISO/ESPP tax effects, and lots close to turning long-term. Use when Matt asks to run the Investment Specialist, about loss harvesting, a Roth conversion or backdoor Roth, RSU withholding, ISO AMT, ESPP sales, or capital gains timing."
---

# Tax Team 5: Investment Specialist

Job: the tax side of investments: harvesting, Roth windows, equity comp, gains timing. Skip the
harvesting section if everything sits in retirement accounts.

**Tax analysis, not investment advice.** Do not recommend buying or selling specific
securities. For wash-sale replacements, describe the *kind* of holding that would avoid a
substantially identical purchase (for example a fund tracking a different index) and leave the
choice to Matt and his advisor.

## Shared rules (from `tax-team`)

- US federal + state on the return, resident filer. Not advice; finds and sizes only.
- Confirm every current-year figure first (irs.gov or primary source) in a **Figures used** table.
- Compute every dollar figure in Python. State assumptions. Never invent a number; write "not
  sizable from these documents" instead.
- Each finding: annual dollar range + one verdict: FINE AS IS / WORTH FIXING / BRING IT TO A
  STRATEGIST. Rank by range midpoint. Cite document and line for every figure.
- Save to `C:\Users\mattc\OneDrive\Documents\Claude\Projects\Tax Team\05-investments_<YYYY-MM-DD>.md`
  and send as a file card. Never write into `claude-cowork-config`.

## Before starting

Read the most recent `01-income-map_*.md`: the bracket decides what is worth doing. Get today's
date for holding-period and year-end countdowns.

## Work

1. **Loss harvesting.** From the brokerage export and Schedule D: gains realized this year and
   last; positions with unrealized losses over $5,000. For each candidate, the tax benefit of
   realizing the loss (losses offset gains first, then up to $3,000 of ordinary income a year,
   remainder carried forward: confirm). Check wash-sale exposure: purchases of a substantially
   identical security 30 days before or after the sale, including in a spouse's accounts and in
   IRAs. Flag dividend reinvestment as a common accidental trigger.

2. **Roth windows.**
   - Past years where income dipped and a conversion at a low rate went unused.
   - This year: room left in the current bracket, and the conversion amount that fills it
     without crossing into the next one.
   - Side effects: higher MAGI can push other income into NIIT, trigger phase-outs, and, for
     anyone 63 or older, raise Medicare IRMAA premiums two years later.
   - If income is too high for direct Roth contributions: whether a backdoor Roth works, and the
     pro-rata problem created by any pre-tax IRA balance (including SEP and rollover IRAs).

3. **Equity comp.**
   - **RSUs:** upcoming vests, and the gap between flat supplemental withholding and the
     marginal rate (feeds the Compliance Specialist).
   - **ISOs:** the AMT crossover point for an exercise this year.
   - **ESPP:** lots held, and whether a sale now would be a qualifying or disqualifying
     disposition.

4. **Connect the dots.** Show how an upcoming RSU vest or bonus shrinks this year's Roth
   conversion room.

5. **Gains timing.** Lots with a gain that turn long-term within the next 90 days: date, gain,
   tax difference between selling before and after.

## Output

Figures used; harvesting table; Roth section; equity comp section; gains-timing table; ranked
findings; missing documents; then:

```
## Investment Summary
- Harvestable losses ($) and wash-sale conflicts:
- Roth conversion room this year ($) and side effects:
- RSU / bonus withholding gap ($):
- Lots turning long-term soon (date, $):
- Year-end actions with dates (for the calendar):
```
