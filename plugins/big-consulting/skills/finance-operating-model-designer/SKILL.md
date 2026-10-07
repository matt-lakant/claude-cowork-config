---
name: finance-operating-model-designer
description: Designs a finance operating model by mapping activities and FTEs, then allocating work across shared services, centers of excellence, and business partnering, with sizing and a transition path. Use when finance headcount is growing faster than the business, after acquisitions leave duplicate finance teams, or when planning finance shared services.
---

# Finance Operating Model Designer

## What this produces
A current-state activity and FTE map, a future-state model allocating each activity to a delivery channel, the FTE shift, and a phased transition plan.

## Inputs to ask for
- Finance org chart with FTEs by team and location
- An activity survey: percent of time per person by activity
- Entities, ERPs, and geographies
- Total finance cost and company revenue, to compute finance cost as a percent of revenue
If no activity data exists, draft a survey of 20 to 30 standard activities (order-to-cash, procure-to-pay, record-to-report, FP&A, tax, treasury).

## Method
1. Build the activity-by-FTE matrix and total FTE per activity. Flag activities spread across many teams (fragmentation).
2. Classify each activity: transactional and rules-based (shared services), specialist expertise (center of excellence: tax, treasury, technical accounting), or decision support close to the business (business partnering).
3. Location test: transactional work consolidates; partnering stays with the business.
4. Size the future state by channel, noting consolidation and automation effects as labeled assumptions.
5. Define interfaces: service catalog, handoffs, and service levels between channels.
6. Sequence the transition in waves, starting with the most standardized processes.

## Output format
- Activity matrix: Activity | Current FTE | Teams involved | Channel | Future FTE
- Model summary: Channel | Scope | FTE | Location
- Interface list: Handoff | From | To | Service level
- Transition waves with timing and risks

## Quality checks
- Current FTE total reconciles to the org chart
- Every activity lands in exactly one channel
- FTE reductions are labeled assumptions with their basis
- Control and segregation-of-duties risks are listed for each move

## Notes from the source article
- **Replaces:** The finance operating model phase of a transformation: consultants mapping every finance activity and FTE, then designing which work moves to shared services, which to centers of excellence, and which stays with business partners.
- **Example request:** “We’ve done three acquisitions and have finance teams in five places doing the same work. Here’s the org chart. Design the target finance operating model.”
- **What the user still owns:** The people. An operating model moves jobs and changes careers, and the communication, sequencing, and fairness are leadership work.
- When handing the deliverable back, name in one line the decision above that stays with the user.
