---
name: business-continuity-plan
description: Runs a business impact analysis and builds a business continuity plan with recovery time and recovery point objectives, dependencies, recovery strategies, and a tabletop exercise. Use when the user needs a BCP, a BIA, recovery priorities for a site, system, or supplier outage, or an exercise scenario.
---

# Business Continuity Plan Builder

## What this produces
A business impact analysis, a recovery plan per critical process, and a tabletop exercise script.

## Inputs to ask for
- List of business processes by function
- Systems, sites, key suppliers, and key people each process depends on
- Current IT recovery capabilities (backups, failover)
- Past outages and contractual service commitments
- If impact data is missing, interview the user per process using the questions in step 1

## Method
1. For each process, estimate impact of disruption at 4 hours, 1 day, 3 days, and 1 week: revenue, customer, regulatory, safety, and reputation.
2. Set the maximum tolerable period of disruption, then a recovery time objective (RTO) inside it, and a recovery point objective (RPO) for data loss.
3. Map dependencies: people, systems, sites, suppliers, data. Compare required RTO to what each dependency can actually deliver. Each mismatch is a gap.
4. Plan for loss scenarios, not causes: loss of site, loss of systems (including cyberattack), loss of people, loss of a key supplier.
5. Write recovery strategies per scenario: manual workarounds, alternate site, backup supplier.
6. Define activation: who declares, call tree, communication templates for staff, customers, and regulators.
7. Write a tabletop exercise that tests the largest gap.

## Output format
- BIA table: Process | Impact at 4h / 1d / 3d / 1w | MTPD | RTO | RPO | Dependencies
- Gap table: Process | Dependency | Required RTO | Achievable | Gap | Fix
- Recovery plan per scenario: trigger, roles, steps, communications
- Tabletop script: scenario, injects, questions, success criteria

## Quality checks
- Every RTO is within its MTPD
- Every critical process has at least one tested or testable workaround
- Contact roles are named, not "the team"

## Notes from the source article
- **Replaces:** The continuity program: a business impact analysis across functions and recovery plans sized to what the business can tolerate.
- **Example request:** “Build our business continuity plan. We have two plants, one ERP, and a single supplier for our main resin. Here’s the process list and our IT recovery setup.”
- **What the user still owns:** Funding the gaps the analysis exposes and running the exercise with the people who will actually be in the room.
- When handing the deliverable back, name in one line the decision above that stays with the user.
