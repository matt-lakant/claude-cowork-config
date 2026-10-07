---
name: market-share-bridge
description: Decomposes the user's revenue change into market growth, segment mix, and within-segment share change, then attributes share movement to segments, channels, and competitors. Use when the user's growth differs from market growth, when leadership asks whether a result came from the market or from execution, or before a business review.
---

# Market Share Bridge

## What this produces
A revenue bridge from period 0 to period 1 split into market, mix, and share effects, plus a table of which competitors gained what the user lost.

## Inputs to ask for
- User revenue (and units, if available) by segment, channel, and region for both periods (spreadsheet)
- Market size for the same cuts and periods
- Competitor share data, win/loss records, or channel sell-through
- Price changes taken in the period
If market data exists only at the total level, run the total bridge and state the limit.

## Method
1. Lock one market definition for both periods and remove out-of-market revenue.
2. Total bridge: change in revenue = (M1 minus M0) x s0 + (s1 minus s0) x M1, with M as market size and s as share. First term is market effect, second is share effect.
3. Split share effect into mix (overweight in segments growing slower or faster than the market) and within-segment share, computed per segment and summed.
4. Where units exist, split value share from volume share. Holding value while losing volume means price is doing the work, which rarely lasts.
5. For segments losing share, identify the gainers from competitor, win/loss, or channel data, and quantify.
6. Test the top three causes against evidence: price gaps, availability, coverage changes, launches.

## Output format
- Waterfall: Start | Market effect | Mix effect | Share effect | End
- Segment table: Segment | Market growth | User growth | Share P0 | Share P1 | Change (pts) | Revenue impact
- To whom: Segment | Share lost | Main gainers | Evidence
- Top three causes with confidence

## Quality checks
- The bridge sums exactly to the actual revenue change
- Market definition and source match across periods, or the break is disclosed
- Mix and share effects are not double counted
- Competitor attributions cite data

## Notes from the source article
- **Replaces:** The question every quarterly business review eventually asks: we grew 6%, the market grew 9%, so where did we lose share and to whom. Answering it usually takes an analyst a week across three data sources that disagree.
- **Example request:** “We grew 4% last year and the market grew 7%. Build a share bridge by region and channel from the attached sales file and market data, and tell me who took the share.”
- **What the user still owns:** The conversation with the leader whose segment lost share, and the decision to buy it back or let it go.
- When handing the deliverable back, name in one line the decision above that stays with the user.
