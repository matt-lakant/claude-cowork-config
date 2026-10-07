---
name: tsa-planner
description: Builds a transition services agreement plan for a carve-out or divestiture: a priced service catalog, durations, service levels, reverse services, dependencies, and a dated exit plan for each service. Use when buying or selling a business unit that relies on a parent's shared services, reviewing a draft TSA, or when someone asks "what do we need the seller to keep running for us?"
---

# TSA Planner

## What this produces
A service-level TSA schedule with pricing basis, duration, service levels, and exit plan per service, plus a reverse TSA list and governance terms.

## Inputs to ask for
- The parent's shared services the business uses (IT, payroll, HR, finance, facilities, logistics)
- Current cost allocations to the business
- The buyer's existing capabilities (or the standalone plan)
- Target standalone date
- Any draft TSA (attach it)
If allocations are missing, list services first and flag pricing as the open item.

## Method
1. Catalog services specifically enough to price and exit: "biweekly payroll for 1,200 US employees," never "HR."
2. For each service, decide whether the buyer can provide it on Day 1. If not, it needs a TSA, a duration, and an exit path: build, buy, or migrate to the buyer's systems.
3. Set duration to the realistic exit time plus a buffer, with extension terms and price step-ups that reward exiting on schedule.
4. Price on cost or cost plus a stated markup, with the allocation method written down, and compare to the buyer's own cost.
5. Set service levels at historical performance.
6. List reverse TSAs: services the carved-out business provides back to the parent.
7. Flag dependencies: data separation, third-party software licenses that need vendor consent to transfer, people who deliver the service.
8. Governance: a TSA manager each side, monthly review, a dispute path.

## Output format
- Table: Service | Description | Provider | Pricing basis | Monthly cost | Duration | Service level | Exit path | Exit date
- Reverse TSA table
- Dependency list with owners
- Governance terms

## Quality checks
- Every service has an exit path and date
- No service is described at the function level
- License consent issues are listed separately

## Notes from the source article
- **Replaces:** The transition services agreement workstream in a carve-out: cataloging every service the parent provides, then pricing and scheduling the exit from each.
- **Example request:** “We’re buying a division off a conglomerate and it runs entirely on the parent’s IT and payroll. Here’s the allocation file. Build the TSA plan and tell me how long we’ll really need it.”
- **What the user still owns:** The exit. TSAs are easy to sign and expensive to live on; holding the team to exit dates is on you.
- When handing the deliverable back, name in one line the decision above that stays with the user.
