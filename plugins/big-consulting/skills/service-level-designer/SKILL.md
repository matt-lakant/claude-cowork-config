---
name: service-level-designer
description: Designs service levels (response time, resolution time, availability) by channel, priority, and customer tier, defines priority rules, and estimates the staffing cost of each target. Use when the user is writing or renegotiating SLAs, launching tiered support, or seeing service targets missed with no clear reason.
---

# Service Level Designer

## What this produces
A priority definition matrix, service-level targets by channel and tier, the cost of each target option, and the measurement rules that make the targets auditable.

## Inputs to ask for
- Current SLAs, contract commitments, and actual performance by channel (attach).
- Contact volume by channel and priority, with handle and resolution times.
- Customer tiers or segments and their revenue.
- Customer expectation evidence: survey data, complaints about speed, competitor published SLAs.

## Method
1. Define priority from impact x urgency (a common ITIL approach): 3 to 4 levels, each with plain examples.
2. Set measures per channel: first response time, time to resolution, and service level for live channels (percent answered within a threshold).
3. Propose 2 to 3 target options per tier and priority, from current performance to stretch.
4. Price each option: staffing required (use Erlang C for live channels, backlog math for queued work) and cost difference.
5. Test targets against evidence: where customer satisfaction stops rising as speed improves, a faster target is spend with no return.
6. Write measurement rules: clock start and stop, business hours, pause conditions, and exclusions.
7. Flag contractual SLAs the current operation cannot meet.

## Output format
1. Priority matrix: Priority | Impact | Urgency | Examples.
2. Target options: Tier | Priority | Channel | Measure | Current | Option A | B | C | Cost.
3. Measurement rules.
4. Contractual risks.

## Quality checks
- Every target has a clock definition.
- Cost is shown for each option.
- Priority examples are specific enough for agents to classify consistently.

## Notes from the source article
- **Replaces:** Service-level design work, when a team sets response and resolution targets by channel, priority, and customer tier, then prices what each target costs to hit.
- **Example request:** “We’re launching premium support for our top 200 accounts. Here are current response times and volumes. Design the service levels by tier and tell me what each option costs.”
- **What the user still owns:** Saying no to the SLA a big customer wants. Promising a target you cannot fund turns a sales win into a penalty clause.
- When handing the deliverable back, name in one line the decision above that stays with the user.
