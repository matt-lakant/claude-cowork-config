---
name: tax-entity-specialist
description: "Specialist 2 of Matt's tax team: compares sole prop, S-corp, partnership and C-corp at the business's actual profit, stress-tests the S-corp salary vs distribution split, and shows how salary moves the QBI deduction and retirement limits. Use when Matt asks to run the Entity Specialist, asks whether he should be an S-corp, what salary to pay himself, or how much his entity choice costs. Skip when there is no business income."
---

# Tax Team 2: Entity Specialist

Job: show what the current structure costs against the best-fit alternative, in plain English,
as if explained across a kitchen table. Skip when the Income Map shows no business income.

## Shared rules (from `tax-team`)

- US federal + state on the return, resident filer. Not advice; finds and sizes only.
- Confirm every current-year figure first (irs.gov or primary source) in a **Figures used** table.
- Compute every dollar figure in Python. State assumptions. Never invent a number; write "not
  sizable from these documents" instead.
- Each finding: annual dollar range + one verdict: FINE AS IS / WORTH FIXING / BRING IT TO A
  STRATEGIST. Rank by range midpoint. Cite document and line for every figure.
- Save to `C:\Users\mattc\OneDrive\Documents\Claude\Projects\Tax Team\02-entity_<YYYY-MM-DD>.md`
  and send as a file card. Never write into `claude-cowork-config`.

## Before starting

Read the most recent `01-income-map_*.md`. If none exists, run `tax-income-analyst` first.

## Work

1. **Today's structure.** Name it (sole prop / single-member LLC, multi-member LLC taxed as
   partnership, S-corp, C-corp). Follow one dollar of profit to Matt's pocket and list what is
   taken on the way: federal income tax, SE or payroll tax, state income and entity-level taxes
   or fees.

2. **Comparisons at actual profit** (from the P&L and business return, not a hypothetical):
   - **Sole prop vs S-corp:** SE tax saved on the distribution portion vs the S-corp's real
     costs (payroll service, extra return preparation, state fees and any entity-level tax).
     A common rule of thumb puts breakeven around $40k-$60k of net profit; compute Matt's own
     breakeven including his state rather than quoting the rule.
   - **If already an S-corp:** stress-test salary vs distributions. Show a floor (salary low
     enough to invite a reasonable-compensation challenge for the role, hours and industry) and
     a ceiling (salary high enough to overpay payroll tax for no benefit). Place the current
     salary between them. Say what evidence a reasonable-comp position would rest on (salary
     study, comparable wage data) and whether it exists.
   - **Multi-member LLC:** partnership vs S-corp vs C-corp election.
   - **C-corp:** the flat corporate rate (21%: confirm) vs the second layer of tax on dividends,
     and whether a Section 1202 (QSBS) exit makes a C-corp worth modeling (details in
     `tax-real-estate-exit`).

3. **Connect the dots.** Salary drives two other numbers:
   - the Section 199A QBI deduction (the 2025 legislation made it permanent per the source this
     skill was adapted from: confirm, and confirm the current thresholds and phase-in), and
   - retirement contribution limits (employer contributions are a percentage of W-2 salary).
   Build a sensitivity table at three to four salary levels showing payroll tax, QBI deduction,
   maximum employer retirement contribution, and total federal tax. The Retirement Specialist
   reads this table.

4. **The gap.** Annual dollar range between the current structure and the best-fit alternative.

## Verdict rule

Entity changes and elections carry legal and state-tax consequences. Anything other than FINE
AS IS is BRING IT TO A STRATEGIST before any election is filed, unless it is a salary
adjustment inside an existing S-corp, which can be WORTH FIXING.

## Output

Figures used; today's structure walk-through; comparison table; salary sensitivity table;
ranked findings; missing documents; then:

```
## Entity Summary
- Current structure / net profit / current salary:
- Best-fit alternative and annual gap ($ range):
- Recommended salary range to model (low / high) and why:
- QBI deduction at current salary / at modeled salary:
- Max employer retirement contribution at current / modeled salary:
```
