---
name: assumption-red-team
description: Extracts every explicit and hidden assumption behind a plan, recommendation, or business case, rates each on importance and evidence, runs a premortem, and names the cheapest test for the riskiest ones. Use before a recommendation goes to executives or a board, when a plan feels too clean, or when a team has converged fast.
---

# Assumption Red Team

## What this produces
An assumption register ranked by risk, a premortem, a sensitivity read on which assumptions flip the answer, and a test plan for the top three.

## Inputs to ask for
- The plan, recommendation, or business case (attach document or model)
- The decision it supports and the threshold that matters (e.g., payback under 24 months)
If a financial model is attached, read the input cells; that is where assumptions hide.

## Method
1. Extract assumptions, explicit and implicit, across five types: market, customer behavior, operational, financial, organizational (will people adopt it, will leaders fund it).
2. Rate each on importance (does the answer change if it is wrong) and evidence (Strong, Some, None).
3. Run a premortem, a technique from psychologist Gary Klein: assume it is 18 months later and the plan failed. Write the five most likely reasons.
4. Base-rate check: compare key assumptions to typical outcomes for similar efforts (adoption rates, cost overruns, timeline slippage) and state the reference used.
5. Sensitivity: for the top five, find the break-even value where the recommendation no longer clears the threshold.
6. For high-importance, low-evidence assumptions, design the cheapest test that would settle them in under two weeks.

## Output format
- Assumption register: # | Assumption | Type | Importance (H/M/L) | Evidence | Break-even value | Source
- Premortem: five failure stories, three sentences each
- Top three risks with test design: Test | Cost | Time | Result that would change the plan
- Verdict: Proceed, Proceed after tests, or Rework

## Quality checks
- Organizational assumptions sit alongside the financial ones
- Every break-even value is calculated from the model or labeled as estimated
- Base rates cite their reference or are labeled as judgment
- Tests are cheap and fast enough to run before the decision

## Notes from the source article
- **Replaces:** The partner’s challenge session before a recommendation goes to the client: pulling out every assumption the team made, finding the one that could flip the answer, and sending the team back to test it.
- **Example request:** “Red-team the business case for consolidating our three service centers into one. Model attached. What has to be true, and what are we kidding ourselves about?”
- **What the user still owns:** Deciding whether to stop. The skill will find the weak assumption; choosing to delay a plan the CEO already announced is yours.
- When handing the deliverable back, name in one line the decision above that stays with the user.
