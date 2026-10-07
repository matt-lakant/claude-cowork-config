---
name: employee-survey-analyzer
description: Analyzes employee engagement or pulse survey data, finds the drivers of engagement, cuts results by team and group while protecting anonymity, codes open comments, and recommends 3 focus areas. Use when the user has survey results (item scores and comments) and needs to know what matters, where problems are concentrated, and what to act on.
---

# Employee Survey Analyzer

## What this produces
Headline scores and trends, a driver analysis, a heat map by group, coded comment themes with counts, and three focus areas with owners.

## Inputs to ask for
- Item-level responses or aggregated scores by group (CSV or XLSX), with the question text.
- Prior survey results for trend, if available.
- Open-comment text.
- The minimum group size for reporting. Default to 5 and suppress any smaller cut.

## Method
1. Compute favorability (% agree and strongly agree) per item and the engagement index. If there is an eNPS question: % scoring 9 to 10 minus % scoring 0 to 6.
2. Run key driver analysis: correlate each item with the engagement index (or regress if item-level data exists). Plot importance against favorability.
3. Priorities are high-importance, low-favorability items. High favorability items are strengths to protect.
4. Cut by function, location, tenure, and manager, suppressing groups under the minimum. Flag cuts more than 10 points below company average.
5. Code comments into themes; count mentions and quote examples with identifying details removed.
6. Pick three focus areas, each tied to a driver item, with a target and owner.

## Output format
1. Headline: engagement, eNPS, response rate, change versus prior survey.
2. Driver table: Item | Favorable % | Importance | Quadrant.
3. Heat map: Group | n | Engagement | Top 3 Items.
4. Comment themes: Theme | Mentions | Example.
5. Three focus areas with targets and owners.

## Quality checks
- No group under the minimum size is shown.
- No quote could identify its author.
- Changes under 3 points are called noise unless samples are large.

## Notes from the source article
- **Replaces:** The survey readout, when analysts run key driver analysis, cut results by every demographic, code thousands of comments, and build the heat map for the leadership offsite.
- **Example request:** “Attached are our engagement survey results by team and 2,400 comments. Tell me what’s driving the scores and the three things we should act on.”
- **What the user still owns:** Acting visibly on the results. Employees judge the next survey on whether this one changed anything.
- When handing the deliverable back, name in one line the decision above that stays with the user.
