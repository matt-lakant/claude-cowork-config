---
name: enterprise-risk-register
description: Builds or refreshes an enterprise risk register with defined scoring scales, inherent and residual ratings, owners, and a heat map of top risks. Use when the user is preparing an ERM refresh, an audit committee risk report, a top-risks list, or consolidating risk interview notes.
---

# Enterprise Risk Register and Heat Map

## What this produces
A scored risk register, a 5x5 heat map of residual risk, and a one-page top-10 risk summary for the board or audit committee.

## Inputs to ask for
- Existing risk register, if any
- Risk interview notes or workshop outputs
- Strategic plan and key objectives
- Risk appetite statement
- Recent incidents and audit findings
- If no appetite statement exists, propose draft thresholds

## Method
1. Rewrite every risk as cause, event, consequence: "Because of X, Y may happen, resulting in Z." Split any entry that holds two events.
2. Define scales before scoring. Likelihood 1 to 5 with probability bands over a stated horizon. Impact 1 to 5 across financial ($ bands sized to the company), operational, regulatory, reputational, and safety; score the worst dimension.
3. Score inherent risk (no controls), then residual risk (current controls), naming the controls relied on.
4. Add velocity (how fast impact arrives) and trend (rising, stable, falling).
5. Tie each risk to the objective it threatens and assign one accountable executive owner.
6. Compare residual score to appetite. Anything above appetite needs a response: reduce, transfer, accept with signoff, or avoid.
7. Scan for missing risks: cyber, key person, supplier concentration, AI misuse.

## Output format
- Register: ID | Risk statement | Objective | Owner | Inherent L/I | Key controls | Residual L/I | Velocity | Trend | Response
- Heat map grid with risk IDs placed by residual score
- Top 10 summary: risk, why now, response, owner, due date

## Quality checks
- Every risk has a cause, event, and consequence
- Scale definitions are printed with the register
- Residual is never higher than inherent
- Every above-appetite risk has a response and a date

## Notes from the source article
- **Replaces:** The ERM refresh: a month of executive risk interviews merged into a register and heat map.
- **Example request:** “Here are my notes from 14 executive risk interviews and last year’s register. Build the refreshed register and the heat map for the September audit committee.”
- **What the user still owns:** Setting appetite, and telling the board which risks you have decided to accept.
- When handing the deliverable back, name in one line the decision above that stays with the user.
