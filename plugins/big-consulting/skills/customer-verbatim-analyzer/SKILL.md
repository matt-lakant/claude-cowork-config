---
name: customer-verbatim-analyzer
description: Codes NPS, CSAT, and customer effort survey comments into themes, links each theme to scores and segments, and ranks the themes that move detractors and promoters. Use when the user has customer survey results with open comments and wants to know what drives the scores and what to fix first.
---

# Customer Verbatim Analyzer

## What this produces
Headline scores, a coded theme set, each theme's impact on score, results by segment, and a ranked fix list with representative quotes.

## Inputs to ask for
- Survey export (CSV or XLSX): score, comment, date, and any segment, product, channel, or region fields.
- Which metric: NPS (0 to 10), CSAT (1 to 5), or customer effort.
- Prior-period results for trend.
- If comments are fewer than 200, report themes as directional.

## Method
1. Compute NPS as % promoters (9 to 10) minus % detractors (0 to 6), or CSAT as % scoring 4 to 5. Report confidence intervals when sample sizes are small.
2. Code comments into 10 to 20 themes with sentiment. A comment can carry multiple themes.
3. For each theme: mention rate among detractors and among promoters, and the average score of comments that mention it against those that do not.
4. Rank themes by impact: mention volume x score gap.
5. Cut by segment, channel, and product. Flag themes concentrated in one segment.
6. Pull 2 to 3 representative quotes per top theme, with identifying details removed.
7. Separate themes the service team controls from product, pricing, and policy themes.

## Output format
1. Headline: score, n, trend, confidence.
2. Theme table: Theme | Mentions | % of Detractors | % of Promoters | Score Gap | Impact | Owner Area.
3. Segment concentrations.
4. Top 5 fixes with quotes.

## Quality checks
- Theme counts come from coded comments, never estimates.
- Quotes are verbatim.
- Score changes within the margin of error are called noise.

## Notes from the source article
- **Replaces:** The voice-of-customer readout, when analysts code thousands of NPS and CSAT comments, link themes to scores, and tell leadership what is really driving detractors.
- **Example request:** “Attached are 4,000 NPS responses from last quarter with comments. What’s driving our detractors, and which of those can the service team actually fix?”
- **What the user still owns:** Closing the loop with the customers who complained. The analysis finds the themes; calling detractors back is a practice you have to staff.
- When handing the deliverable back, name in one line the decision above that stays with the user.
