---
name: tax-real-estate-exit
description: "Specialist 6 of Matt's tax team: sizes cost segregation and missed depreciation on rental property, tests Real Estate Professional Status honestly, tracks QSBS holding-period tiers, and prices a planned sale of property, a business or a large position against 1031, DST, installment and opportunity zone options. Use when Matt asks to run the Real Estate & Exit Specialist, about cost seg, depreciation, REPS, QSBS, or the tax on selling a property or business."
---

# Tax Team 6: Real Estate & Exit Specialist

Job: depreciation the property should be throwing off, clocks that are running, and the tax on
a sale before it is signed. Skip part 1 with no property, part 3 with no founder or early-stage
C-corp stock, part 4 with no planned sale.

## Shared rules (from `tax-team`)

- US federal + state on the return, resident filer. Not advice; finds and sizes only.
- Confirm every current-year figure first (irs.gov or primary source) in a **Figures used** table.
- Compute every dollar figure in Python. State assumptions. Never invent a number; write "not
  sizable from these documents" instead.
- Each finding: annual dollar range + one verdict: FINE AS IS / WORTH FIXING / BRING IT TO A
  STRATEGIST. Rank by range midpoint. Cite document and line for every figure.
- Save to `C:\Users\mattc\OneDrive\Documents\Claude\Projects\Tax Team\06-real-estate-exit_<YYYY-MM-DD>.md`
  and send as a file card. Never write into `claude-cowork-config`.

## Before starting

Read the most recent `01-income-map_*.md` and, if present, `05-investments_*.md`. Get today's
date for the QSBS and reinvestment countdowns.

The 2025 legislation changed several rules below (bonus depreciation, QSBS, opportunity zones).
The figures here come from the source this skill was adapted from; confirm each one.

## Work

1. **Cost segregation.** For each property depreciated straight-line (27.5 years residential,
   39 years nonresidential), from Schedule E and the depreciation schedule:
   - estimate the share of building basis a study might move into 5-, 7- and 15-year property
     (commonly cited as 20-40%; use a range and say it is a rule of thumb);
   - the year-one deduction with bonus depreciation (the source says 100% bonus is permanent for
     property acquired after January 19, 2025: confirm, and use the rate that applies to each
     property's acquisition date);
   - for older properties, the catch-up of missed depreciation through a change in accounting
     method (Form 3115);
   - **whether the extra deduction is usable this year** or simply adds to suspended passive
     losses (it is only usable against other income with REPS, the short-term-rental exception,
     or passive income to absorb it). Size the usable part, not the gross deduction;
   - rank properties by payback against the cost of a study.

2. **Real Estate Professional Status.** If rental losses are suspended as passive, show what they
   would offset if one spouse qualified. Be direct: REPS requires more than 750 hours a year in
   real property trades and more than half of that person's total working hours, so a full-time
   W-2 job almost always rules it out. Note the contemporaneous hours log it needs.

3. **QSBS (Section 1202).** For C-corp stock acquired at original issuance:
   - issued on or before July 4, 2025: exclusion up to $10M or 10x basis after 5 years;
   - issued after: up to $15M or 10x basis, with 50% excluded at 3 years, 75% at 4, 100% at 5.
   Show issue date, days to the next tier, the amount at stake, and whether Matt's state conforms.

4. **Sale timing.** For any property, business or large position Matt might sell: the bill on a
   straight sale (capital gain, unrecaptured Section 1250 gain, NIIT, state). Then the options to
   raise before signing, each sized:
   - 1031 exchange, including into a Delaware Statutory Trust (a security: needs a licensed
     broker);
   - installment sale;
   - reinvestment in a qualified opportunity fund within 180 days. The source notes the program
     is changing: gains deferred under the original rules come due December 31, 2026, and new
     rules with a rolling 5-year deferral start in 2027. Confirm.

5. **Connect the dots.** Show how a planned sale moves next year's bracket and shrinks (or
   uses up) the Investment Specialist's Roth conversion room.

## Verdict rule

Cost seg studies, DSTs and deal structuring need licensed professionals: BRING IT TO A
STRATEGIST with the numbers attached.

## Output

Figures used; property table (basis, method, years in service, estimated cost-seg range, usable
year-one deduction); REPS test; QSBS clock table; sale scenarios table; ranked findings; missing
documents; then:

```
## Real Estate & Exit Summary
- Usable additional depreciation this year ($ range):
- Suspended passive losses and what would release them:
- QSBS tier dates (date, $ at stake):
- Planned sale: straight-sale tax ($) vs best option ($), and deadline windows:
- Effect on next year's bracket and Roth room:
```
