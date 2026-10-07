---
name: share-of-wallet-gap-finder
description: Estimates each customer's total spend in your categories, calculates your share of that wallet, and ranks the revenue gap by account and product line. Use when the user wants to grow existing accounts, find cross-sell and upsell whitespace, or set account targets based on potential instead of last year's revenue.
---

# Share-of-Wallet Gap Finder

## What this produces
Wallet and share of wallet per account, a whitespace matrix, and accounts ranked by realistic gap.

## Inputs to ask for
- Revenue by customer and product line, trailing 12 months (CSV or XLSX).
- A size driver per customer (employees, sites, fleet, beds), whichever drives category spend here.
- Any known wallet data: customer-reported spend, rep estimates, bid data. If none, label all wallets low-confidence.

## Method
1. Choose the wallet driver with the user and justify it. Build a spend ratio (category spend per unit of driver) from accounts where wallet is known, or from industry ratios the user supplies.
2. Estimate wallet per account = driver x ratio, by product line. Show a low and high range at plus or minus 25% unless better data exists.
3. Share of wallet = our revenue / estimated wallet. Flag any account above 100% (the ratio is wrong there).
4. Set target share per segment at the 75th percentile of share among comparable accounts.
5. Gap = wallet x (target share minus current share), floored at zero.
6. Build a whitespace matrix: accounts in rows, product lines in columns, marked Buying / Not Buying / Gap Value.
7. Rank accounts by gap, then sort them into four groups: high wallet and low share (grow), high wallet and high share (defend), low wallet and high share (maintain efficiently), low wallet and low share (deprioritize).

## Output format
1. Summary: total wallet, total share, total gap, top 20 accounts' share of gap.
2. Account table: Account | Segment | Wallet (Low/High) | Our Revenue | Share | Target | Gap | Quadrant.
3. Whitespace matrix for the top 25 accounts.

## Quality checks
- Every wallet estimate shows the driver and ratio used.
- Targets come from observed peer shares in the same segment.
- Accounts over 100% share are flagged in the table with the likely cause.

## Notes from the source article
- **Replaces:** Account-potential work: estimating each customer’s total category spend, comparing it to what you capture, and handing sales a ranked whitespace list.
- **Example request:** “Here’s revenue by customer and product line plus headcount for each account. Show me our share of wallet and which 25 accounts have the most room to grow.”
- **What the user still owns:** Turning a gap into a target a rep believes. Quotas built on wallets the field thinks are fiction get sandbagged.
- When handing the deliverable back, name in one line the decision above that stays with the user.
