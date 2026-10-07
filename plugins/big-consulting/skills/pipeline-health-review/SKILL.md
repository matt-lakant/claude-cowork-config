---
name: pipeline-health-review
description: Analyzes a CRM opportunity export for coverage, stage conversion, velocity, aging, slippage, and concentration, and produces a risk-adjusted forecast. Use when the user attaches a pipeline export and asks whether the forecast is real, why deals stall, or which reps need coaching.
---

# Pipeline Health Review

## What this produces
A risk-adjusted forecast, a list of deals needing attention, and a rep scorecard.

## Inputs to ask for
- Open opportunities: owner, account, amount, stage, created, close date, stage entry dates, forecast category
- Closed won and closed lost opportunities for the prior four quarters
- Quota by rep and team for the period
- If stage history is missing, use created and close dates and state the lost precision

## Method
1. Compute historical stage-to-stage conversion and win rate by segment and deal size band.
2. Compute coverage: open pipeline due this period divided by remaining quota. Compare to the coverage the user's own win rate requires (1 divided by win rate), instead of a generic multiple.
3. Compute velocity: number of opportunities times win rate times average deal size, divided by average cycle length in days.
4. Flag aged deals: time in current stage above twice the historical median for that stage.
5. Flag slippage: deals whose close date moved two or more times, and deals with close dates in the past.
6. Check concentration: share of the forecast in the top five deals.
7. Risk-adjust the forecast: weight each deal by historical conversion from its stage, haircut aged and slipped deals, and compare to the submitted commit.

## Output format
- Headline: submitted forecast, risk-adjusted forecast, gap, coverage ratio versus required
- Stage table: Stage | Open $ | Historical conversion % | Median days | Aged deals
- Deals needing attention: Deal | Owner | Amount | Issue | Question to ask
- Rep scorecard: Rep | Coverage | Win rate | Aged % | Slipped count

## Quality checks
- Conversion rates come from the user's history, not benchmarks
- Risk-adjusted forecast method is stated in one sentence
- Each flagged deal has a specific question for the rep
- Closed lost data is included, or its absence is flagged

## Notes from the source article
- **Replaces:** The commercial diagnostic: pulling the CRM, computing conversion and velocity, and showing which part of the forecast is real.
- **Example request:** “Here’s the Salesforce export for Q3. My team is calling USD 14M. Tell me what the pipeline actually supports and which deals I should ask about in Monday’s forecast call.”
- **What the user still owns:** The forecast you give the board, and the coaching conversation with the rep whose pipeline doesn’t hold up.
- When handing the deliverable back, name in one line the decision above that stays with the user.
