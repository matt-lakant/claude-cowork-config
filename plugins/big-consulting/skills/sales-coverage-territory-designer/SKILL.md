---
name: sales-coverage-territory-designer
description: Designs coverage inside the direct sales force (named account managers, field territory reps, inside reps, overlay specialists), calculates required headcount from workload, and balances territories on potential and workload. Use when the user is redrawing territories, resizing sales headcount, or fixing uneven quota attainment. Channel choices (partners, distributors, self-serve) come in as an input from the channel design.
---

# Sales Coverage and Territory Designer

## What this produces
A coverage model by segment, headcount built from workload, and balanced territories with a disruption count.

## Inputs to ask for
- Account list with current revenue, estimated potential (or firmographics to estimate it), location, industry, and current rep
- Rep roster with role, location, and attainment history
- Current call frequency by account type and average time per interaction
- Available selling hours per rep per year after admin and travel
- Which accounts the channel strategy already assigns to partners, distributors, or self-serve (exclude them from direct coverage)
- If potential is unavailable, estimate it from firmographics and label it a proxy

## Method
1. Segment accounts on current revenue and potential into a grid. High potential accounts with low current share are the priority.
2. Assign a direct coverage role to each cell (named account manager, field territory rep, inside rep, with overlay specialists where product depth is needed) based on potential and buying complexity. Accounts already assigned to indirect channels stay out of the workload math.
3. Compute workload: accounts per segment times interactions per year times hours per interaction, plus prospecting time. Divide by available selling hours to get FTEs per role.
4. Compare required FTEs to current roster by role and region.
5. Balance territories on potential and workload within about 10 to 15 percent of average, with reasonable travel.
6. Count relationship disruption: accounts whose rep changes, weighted by revenue. Minimize changes on top accounts.
7. Set quota logic tied to territory potential, not last year's result alone.

## Output format
- Coverage grid: Segment | Accounts | Revenue | Potential | Coverage model | Interactions/year
- Headcount table: Role | Required FTE | Current FTE | Gap
- Territory table: Territory | Rep | Accounts | Potential $ | Workload hours | Variance to average %
- Disruption summary: accounts and revenue changing hands

## Quality checks
- Workload math is shown with every input
- No territory is more than 15 percent off average without a stated reason
- Top 50 accounts by revenue keep their rep unless the change is justified
- Potential estimates are labeled measured or proxy

## Notes from the source article
- **Replaces:** The sales-effectiveness workstream: sizing account potential, setting coverage by segment, and redrawing territories.
- **Example request:** “We have 22 reps and 3,400 accounts, and attainment ranges from 40 to 160 percent. Here’s the account file. Redesign coverage and territories.”
- **What the user still owns:** Telling a veteran rep they are losing an account they have held for ten years, and managing the attrition that follows.
- When handing the deliverable back, name in one line the decision above that stays with the user.
