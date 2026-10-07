---
name: three-horizons-growth-portfolio
description: Classifies growth initiatives into three horizons, sizes the gap between the revenue target and the core business's momentum, and tests whether the portfolio and its funding can close it. Use when the user is building a multi-year growth plan, allocating growth investment, or needs to show a board how a revenue target will be reached.
---

# Three Horizons Growth Portfolio

## What this produces
A core momentum forecast, the growth gap by year, a horizon-classified portfolio with risk-adjusted value, and the portfolio gaps to fill.

## Inputs to ask for
- The revenue target and year, plus 3+ years of core history by line.
- Growth initiatives with owner, stage, spend, and projected revenue (mark missing projections unknown).

## Method
1. Use the three horizons from Baghai, Coley, and White's The Alchemy of Growth: H1 defends and extends the core, H2 builds emerging businesses with proven early demand, H3 creates options that are still experiments.
2. Build H1 momentum: the current trajectory with no new initiatives, net of known headwinds (price pressure, contract losses, churn). Challenge any H1 line growing faster than its trailing 3-year rate.
3. Growth gap = target minus H1 momentum, by year.
4. Classify by evidence: H2 needs paying customers and a working model; anything earlier is H3. Reclassify initiatives placed too high.
5. Risk-adjust projections by stage. Starting probabilities if the user has none: H1 extensions 80%, H2 50%, H3 10 to 20%. Show them as editable assumptions.
6. Compare risk-adjusted H2 plus H3 value against the gap, year by year. Name the years where the gap stays open.
7. Compare the funding mix to the gap (a common starting heuristic is 70/20/10 across H1, H2, H3) and flag where H2 and H3 funding cannot close it.
8. Assign metrics by horizon: H1 margin and share, H2 growth and unit economics, H3 learning milestones.

## Output format
1. Gap summary: Year | Target | H1 Momentum | Gap | Risk-Adjusted H2+H3 | Remaining Gap.
2. Portfolio table: Initiative | Horizon | Stage Evidence | Spend | Projected Revenue | Probability | Risk-Adjusted Value | Metric.
3. Funding mix: current against the gap required.
4. Portfolio gaps and recommended moves (under 8 bullets).

## Quality checks
- H1 momentum excludes all new initiatives.
- Every horizon classification cites stage evidence.
- Probabilities are shown and editable, never buried.

## Notes from the source article
- **Replaces:** The growth-portfolio review: sorting every initiative into horizons, sizing the growth gap, and showing the board whether the pipeline closes it.
- **Example request:** “The board wants us at USD 900M by 2029 and we’re at USD 610M. Here’s the core forecast and our 14 growth initiatives. Show me whether this portfolio actually gets us there.”
- **What the user still owns:** Protecting H2 and H3 funding when H1 has a bad quarter. The first budget cut always comes from the future, and holding that line is an executive decision.
- When handing the deliverable back, name in one line the decision above that stays with the user.
