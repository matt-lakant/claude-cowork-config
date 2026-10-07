---
name: acquisition-target-screen
description: Screens a long list of potential acquisition targets against a deal thesis using pass/fail gates and weighted fit scores, then tiers them and profiles the top candidates. Use when building an acquisition pipeline, testing a buy-versus-build idea, or when someone hands over a list of companies and asks "which of these are worth pursuing?"
---

# Acquisition Target Screen

## What this produces
A gate log, a scored and tiered target table, and one-paragraph profiles of the A-tier targets.

## Inputs to ask for
- The deal thesis: what the acquisition must add (capability, geography, customers, scale)
- Hard criteria: revenue range, margin floor, geography, ownership type
- The long list (attach a CSV export or paste it) with whatever fields exist
- Valuation ceiling and the multiple range the user considers realistic
If there is no written thesis, draft one from the user's answers and confirm it before screening.

## Method
1. Turn the thesis into 3 to 5 pass/fail gates and 4 to 6 weighted fit criteria (strategic fit, financial profile, integration complexity, likelihood the owner will transact). Weights sum to 100.
2. Apply the gates. Record the reason for every exclusion.
3. Score survivors 1 to 5 per criterion, each with an evidence note. Scores without data are labeled ESTIMATED.
4. Apply the user's multiple range to each target's revenue or EBITDA for a rough value band; flag targets above the ceiling.
5. Flag integration complexity: conflicting customers, incompatible systems, unionized sites, likely regulatory reviews.
6. Tier: A (approach now), B (monitor), C (drop).
7. For each A-tier target, write why it fits and the first five questions to answer on a call.

## Output format
- Gate log: Company | Failed gate | Reason
- Scoring table: Company | Criterion scores | Weighted score | Confidence | Value band | Tier
- A-tier profiles, 120 words maximum each

## Quality checks
- Every exclusion has a stated reason
- Every score based on missing data is labeled ESTIMATED
- No fact about a company appears unless it is in the inputs or marked "verify"
- Weights sum to 100

## Notes from the source article
- **Replaces:** The long-list to short-list exercise: analysts pull a few hundred companies from databases, score them against the deal thesis, and cut to the ten worth a phone call.
- **Example request:** “Attached are 240 specialty distributors from our database export. Our thesis is adding Southeast coverage under USD 150M revenue. Screen them and give me the ten to call.”
- **What the user still owns:** Whether to buy at all. A clean screen makes any thesis look executable, so settle buy versus build before you open the list.
- When handing the deliverable back, name in one line the decision above that stays with the user.
