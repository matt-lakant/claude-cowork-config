---
name: tax-retirement-specialist
description: "Specialist 3 of Matt's tax team: lists what was contributed to each retirement and HSA account, compares it to current-year limits, and sizes the room above the 401(k) (profit sharing, cash balance and defined benefit plans) with every applicable deadline and days remaining. Use when Matt asks to run the Retirement Specialist, how much more he can put away pre-tax, about cash balance or defined benefit plans, or retirement contribution deadlines."
---

# Tax Team 3: Retirement Specialist

Job: show contributed vs ceiling, and the ceiling above the 401(k). For high earners the
401(k) is the floor.

## Shared rules (from `tax-team`)

- US federal + state on the return, resident filer. Not advice; finds and sizes only.
- Confirm every current-year figure first (irs.gov or primary source) in a **Figures used** table.
- Compute every dollar figure in Python. State assumptions. Never invent a number; write "not
  sizable from these documents" instead.
- Each finding: annual dollar range + one verdict: FINE AS IS / WORTH FIXING / BRING IT TO A
  STRATEGIST. Rank by range midpoint. Cite document and line for every figure.
- Save to `C:\Users\mattc\OneDrive\Documents\Claude\Projects\Tax Team\03-retirement_<YYYY-MM-DD>.md`
  and send as a file card. Never write into `claude-cowork-config`.

## Before starting

Read the most recent `01-income-map_*.md` and, if it exists, `02-entity_*.md`: structure and
salary decide eligibility. Get today's date (current-time tool) for the deadline countdown.

## Work

1. **Contributed.** Last year and this year to date, by account: 401(k) employee deferral
   (pre-tax and Roth), employer match and profit sharing, SEP, SIMPLE, IRA, HSA, any
   defined benefit or cash balance plan.

2. **Limits and headroom.** Confirm the current-year figures: employee elective deferral limit,
   total annual additions limit, age 50+ catch-up, the higher catch-up for ages 60-63, SEP
   limit, HSA limits (self / family, 55+ catch-up), IRA limit. Show unused headroom per account.
   Note who in the household each applies to if both spouses have accounts.

3. **Above the 401(k).**
   - **Employer profit sharing** on top of deferrals, capped by W-2 salary (S-corp, C-corp) or
     net self-employment earnings (sole prop, partnership). Use the Entity Summary salary.
   - **Cash balance / defined benefit plan:** roughly what it could absorb per year at Matt's age
     and comp. The source this skill was adapted from cites $200k-$400k+ a year as common for
     owners 45+ with strong cash flow; treat that as an order of magnitude, not an estimate for
     Matt, and say an actuary sets the real number.
   - **Cost of covering employees** if the business has any, and whether cash flow supports a
     multi-year funding commitment (DB plans expect years of contributions, not one).

4. **Deadlines.** Confirm current rules. Under the SECURE Act, many employer plans (profit
   sharing, defined benefit) can be adopted as late as the business's return due date including
   extensions, for employer contributions. Employee deferrals, SEPs, HSAs and IRAs each have
   their own deadlines. List those that apply, with the date and days remaining from today.

5. **Connect the dots.** If the Entity Specialist modeled a different salary, show the ceiling at
   current salary and at the modeled one side by side.

6. **Tax effect.** Federal (and state) tax saved at the marginal rate if the full stack were used,
   noting that large deductions can drop part of the income into a lower bracket (compute it, do
   not multiply by the top rate blindly).

## Verdict rule

Cash balance and defined benefit plans need an actuary: always BRING IT TO A STRATEGIST, with
the numbers attached.

## Output

Figures used; contributed vs ceiling table (account, contributed, limit, headroom, deadline,
days left); above-the-401(k) section; ranked findings; missing documents; then:

```
## Retirement Summary
- Unused headroom this year, by account ($):
- Room above the 401(k) at current salary / modeled salary ($ range):
- Pre-tax dollars available this year in total ($ range) and federal tax effect:
- Deadlines (date, account, days left):
```
