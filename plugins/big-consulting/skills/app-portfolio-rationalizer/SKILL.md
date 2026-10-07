---
name: app-portfolio-rationalizer
description: Scores an application portfolio on business value, technical health, cost, and redundancy, assigns each app a disposition (tolerate, invest, migrate, eliminate), and sizes the savings. Use when the user wants to cut IT run cost, reduce overlapping software, prepare for a cloud or ERP program, or clean up after acquisitions.
---

# Application Portfolio Rationalizer

## What this produces
A scored application portfolio, a disposition per application, a redundancy map by business capability, and a savings and sequencing plan.

## Inputs to ask for
- Application inventory (CSV) with owner, users, vendor, annual cost (licenses, hosting, support), and contract end dates
- Business capability each app supports
- Version, support status, and known issues
- Usage data (active users, logins) if available
- If costs are missing, match finance's software spend by vendor to apps

## Method
1. Map every app to a business capability. Capabilities with three or more apps are the first place to look.
2. Score business value 1 to 5: criticality to operations, user reach, fit to current process, and actual usage.
3. Score technical health 1 to 5: vendor support status, security posture, integration quality, and skills available to maintain it.
4. Assign disposition using the TIME model: tolerate (low value, good health), invest (high value, good health), migrate (high value, poor health), eliminate (low value, poor health, or redundant).
5. For each eliminate or migrate, name the target app and what data must move.
6. Size savings from licenses, hosting, and support, net of migration cost, timed to contract end dates.
7. Sequence retirements to hit renewal dates and avoid paying for overlap.

## Output format
- Portfolio table: App | Capability | Owner | Annual cost | Value | Health | Disposition | Target
- Redundancy map: Capability | Apps | Recommended survivor
- Savings plan: App | Action | Contract end | Gross saving | Migration cost | Net saving | Quarter

## Quality checks
- Low-usage apps are checked for seasonal or regulatory use before elimination
- Every eliminated app has a target or a reason none is needed
- Savings are timed to contract dates
- Totals reconcile to the total software spend supplied

## Notes from the source article
- **Replaces:** The portfolio rationalization: scoring every application on value and technical health, then a retire-and-replace plan.
- **Example request:** “We have 340 applications after three acquisitions. Here’s the inventory with costs. Tell me which ones to kill and what we save.”
- **What the user still owns:** Telling a department its favorite tool is going away, and enforcing the retirement date.
- When handing the deliverable back, name in one line the decision above that stays with the user.
