---
name: peer-benchmark-set-builder
description: Selects a defensible peer set with explicit criteria, normalizes peer financials for a fair comparison, and sizes the user's gap to median and top quartile in dollars. Use when the user wants to benchmark against competitors or peers, needs a peer group for a board or investor discussion, or is setting margin, growth, or productivity targets.
---

# Peer Benchmark Set Builder

## What this produces
A documented set of 6 to 12 peers, a normalized metric table with quartiles, and the dollar value of closing each gap.

## Inputs to ask for
- Purpose: operating performance, valuation, or compensation (each needs a different set)
- The user's P&L, balance sheet, and headcount for matching periods
- Candidate peers and any peer groups used in past board materials
- Candidate filings (attach, or work from public knowledge and flag gaps)

## Method
1. Set criteria before naming companies: business mix overlap, size band (roughly 0.5x to 2x the user's revenue), asset-light vs asset-heavy model, geography, ownership.
2. Build a long list from competitor mentions in filings, the peer groups companies publish in their proxies, and industry classification codes.
3. Score candidates and cut to 6 to 12, recording each exclusion's reason. Show 1 or 2 aspirational peers in a separate column, outside the median.
4. Normalize: calendarize fiscal years, strip one-time items, adjust for lease accounting, isolate comparable segments, convert currency at average rates, adjust productivity for outsourcing.
5. Compute metrics that fit the purpose: growth, gross margin, SG&A % revenue, operating margin, ROIC, working capital days, revenue per employee.
6. Gap value = (peer median metric minus user metric) x the user's own base.
7. Give a first hypothesis for each large gap: mix, scale, model, or execution.

## Output format
- Long list: Company | Criteria met | Include? | Reason
- Metrics: Metric | Bottom quartile | Median | Top quartile | User | Rank | Gap to median ($) | Gap to top quartile ($)
- Top three gaps with hypotheses (under 200 words)

## Quality checks
- Criteria were fixed before names were scored
- At least 6 peers, or the weakness is stated
- All peers are normalized the same way, with adjustments listed
- Dollar gaps use the user's base

## Notes from the source article
- **Replaces:** The benchmarking workstream: a team picks which eight to twelve companies count as peers, normalizes their numbers, and rebuilds the set after the CFO challenges it in the first meeting.
- **Example request:** “Build a peer set for a USD 400M specialty chemicals distributor and benchmark our SG&A and working capital. The board keeps comparing us to companies five times our size, and I want a set that holds up.”
- **What the user still owns:** Whether a gap is a target or a feature of your model. Some gaps are the price of how you chose to win, and only you can say which.
- When handing the deliverable back, name in one line the decision above that stays with the user.
