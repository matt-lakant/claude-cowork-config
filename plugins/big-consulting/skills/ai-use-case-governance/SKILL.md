---
name: ai-use-case-governance
description: Reviews an AI use case against the NIST AI Risk Management Framework (Govern, Map, Measure, Manage) and screens it against the EU AI Act risk tiers, producing a risk rating and required controls. Use when the user is approving an AI tool, building an AI inventory, or assessing whether a system is high-risk.
---

# AI Use-Case Governance Review

## What this produces
A use-case risk profile, an EU AI Act tier screen, NIST AI RMF control gaps, and an approve, approve-with-conditions, or reject recommendation.

## Inputs to ask for
- Use-case description: purpose, users, people affected, decisions it informs or makes
- Model or vendor, data used (including personal data), where it runs
- Human oversight: who reviews outputs before action
- Where users and affected people are located
- Vendor documentation or model cards
- If the decision the AI influences is unclear, ask; tiering depends on it

## Method
1. Screen EU AI Act tier when EU people or markets are involved: prohibited (for example social scoring or manipulative techniques), high-risk (listed areas such as employment and worker management, creditworthiness, education, access to essential services, critical infrastructure), limited risk with transparency duties (chatbots, generated content), or minimal risk. Flag borderline cases for counsel.
2. Map (NIST): context, intended and foreseeable misuse, affected groups, impact if wrong.
3. Measure (NIST): what is tested for accuracy, bias across groups, resilience to bad inputs, privacy, and security, with thresholds.
4. Manage (NIST): human review points, fallback when the system fails, incident response, monitoring for drift.
5. Govern (NIST): named owner, policy coverage, inventory entry, vendor terms, user training.
6. Rate residual risk and list conditions for approval.

## Output format
- Use-case profile table
- Tier screen: Tier | Basis | Confidence | Counsel review needed (Y/N)
- Control gaps: NIST function | Expected practice | Current state | Gap | Fix
- Recommendation with conditions and review date

## Quality checks
- Tier basis names the specific use area, not a general impression
- Every gap maps to a NIST function
- The output says legal classification requires counsel confirmation

## Notes from the source article
- **Replaces:** The AI governance assessment: mapping each AI use case to regulatory risk tiers and writing the controls it needs.
- **Example request:** “HR wants to use an AI tool to rank job applicants in the US and Germany. Here’s the vendor’s documentation. Run the governance review.”
- **What the user still owns:** The decision to deploy, the accountability when the system gets something wrong, and the legal sign-off.
- When handing the deliverable back, name in one line the decision above that stays with the user.
