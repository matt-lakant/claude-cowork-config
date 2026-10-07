---
name: renewal-risk-review
description: Scores upcoming renewals for risk using usage, support, sentiment, relationship, and commercial signals, validates the score against past renewals, and assigns a save plan and owner to each at-risk account. Use when account managers are preparing a quarter's renewals, the user wants an early warning list, or renewal forecasts keep surprising leadership.
---

# Renewal Risk Review

## What this produces
Upcoming renewals ranked by risk with the signals behind each score, save plans for high-risk accounts, and a risk-adjusted forecast.

## Inputs to ask for
- Renewal list: account, renewal date, contract value, owner (CSV or XLSX).
- Signals per account: usage trend, tickets and escalations, survey scores, sponsor changes, payment history, competitor mentions in CRM.
- Past renewals with outcome (renewed, reduced, lost) for validation.
- If a signal is unavailable, drop it and reweight; state which were used.

## Method
1. Score each signal 0 to 3 for risk. Common high-risk signals: usage down 20% or more over 90 days, sponsor departed, open escalation, detractor score, late payments.
2. Weight signals using past renewals: signals that separated lost from renewed accounts get more weight. With fewer than 30 past outcomes, use equal weights and say so.
3. Test the score on past renewals: share of lost accounts that would have been flagged high risk 90 days out.
4. Tier accounts: high, medium, low. Sort high risk by contract value and days to renewal.
5. For each high-risk account, assign a save play matched to the driver (usage: adoption plan; sponsor: executive re-introduction; service: fix and credit), an owner, and a date. Start at least 90 to 120 days before renewal.
6. Adjust the forecast: contract value x renewal probability by tier, using past rates.

## Output format
1. Risk table: Account | Renewal Date | Value | Score | Tier | Top Signals | Owner.
2. Save plans: Account | Driver | Play | Owner | Due.
3. Risk-adjusted renewal forecast by quarter.

## Quality checks
- Every score shows the signals behind it.
- Validation is reported, including misses.
- No save play lacks an owner and a date.

## Notes from the source article
- **Replaces:** An account health program: building a health score, validating it on past renewals, and assigning save plays.
- **Example request:** “Here are our 85 renewals for the next two quarters with usage, tickets, and CRM notes. Tell me which ones are at risk, why, and what we do about each.”
- **What the user still owns:** The executive call on the account that matters most. Some saves need a senior leader on the phone, and no score makes that call.
- When handing the deliverable back, name in one line the decision above that stays with the user.
