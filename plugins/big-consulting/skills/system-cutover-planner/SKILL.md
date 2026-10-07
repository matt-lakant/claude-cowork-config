---
name: system-cutover-planner
description: Builds a cutover plan for a system go-live: strategy choice, hour-by-hour runbook, data migration and reconciliation steps, rehearsals, go or no-go criteria, rollback plan, and hypercare. Use when the user is preparing to switch to a new ERP, CRM, billing, or other core system, or planning a migration weekend.
---

# System Cutover Planner

## What this produces
A cutover strategy, an hour-by-hour runbook, go or no-go criteria, a rollback plan, and a hypercare plan for the first weeks.

## Inputs to ask for
- Legacy and new systems and affected integrations
- Data objects to migrate, volumes, and migration tooling
- Business calendar: period close, peak periods, blackout dates
- Test status: open defects by severity, rehearsal results
- If no rehearsal has run, the first deliverable is a rehearsal plan

## Method
1. Choose strategy: big bang, phased, or parallel run, weighing risk against the cost of two systems.
2. Pick a window away from period close and peak volume.
3. Build the runbook backward from go-live: freeze legacy, final extracts, loads, reconciliations, integration switches, smoke tests, business sign-off. Each task has owner, start, duration, predecessor, and verification.
4. Define reconciliation per data object: record counts, control totals (open AR, inventory value), and spot checks by business users.
5. Set go or no-go criteria: no open critical defects, reconciliations within tolerance, rehearsal completed within the planned window, key users trained, rollback tested.
6. Define the rollback point of no return and the steps and time to revert before it.
7. Plan hypercare: support model, daily defect triage, business metrics watched (orders shipped, invoices sent), and exit criteria.

## Output format
- Strategy memo, under 200 words
- Runbook: Step | Task | Owner | Start | Duration | Predecessor | Verification
- Go or no-go checklist with thresholds
- Rollback plan with point of no return
- Hypercare plan and exit criteria

## Quality checks
- Every task has one owner and a verification step
- Reconciliation uses control totals, not only record counts
- The point of no return is explicit
- Business sign-off appears before go-live, not after

## Notes from the source article
- **Replaces:** The cutover workstream: the hour-by-hour runbook, rehearsals, go or no-go criteria, and rollback plan.
- **Example request:** “We go live on the new ERP at our two plants in November. Here’s the migration object list and our test status. Build the cutover plan.”
- **What the user still owns:** Making the go or no-go call in the room, including calling a no-go when everyone is tired and wants to be done.
- When handing the deliverable back, name in one line the decision above that stays with the user.
