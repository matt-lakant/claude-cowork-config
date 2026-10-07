---
name: escalation-playbook-writer
description: Writes an escalation playbook with severity definitions, escalation triggers, tier-by-tier ownership, handoff requirements, customer communication cadences, and post-incident review steps. Use when escalations bounce between teams, executives hear about problems from customers first, or a new support model needs escalation rules.
---

# Escalation Playbook Writer

## What this produces
A playbook of 3 to 5 pages: severity levels, triggers, an escalation path by tier, handoff and communication templates, and a closure and review process.

## Inputs to ask for
- Current escalation practice, including recent escalations that went badly.
- Support tiers, teams, and on-call arrangements.
- Contractual SLAs and any regulatory reporting duties.
- Customer tiers that get special handling.
- If no process exists, draft from these inputs and mark owners for confirmation.

## Method
1. Define 3 to 4 severity levels by customer impact, with examples and the response and update times for each.
2. Write triggers: functional (needs skills the tier lacks), time-based (unresolved past a threshold), and hierarchical (customer requests an executive, legal or safety risk, top-tier account).
3. Map the path: who owns at each tier, who is informed, and when an executive sponsor joins.
4. Specify the handoff record: issue summary, customer impact, steps tried, evidence, and next update time. Nobody escalates without it.
5. Set the communication cadence for the customer and internally, by severity.
6. Define closure: customer confirmation, root cause logged, and a review within 5 business days for top severities.
7. Add a weekly escalation review: volume by trigger, time at each tier, and repeat causes.

## Output format
1. Severity table: Level | Definition | Examples | Response | Update Cadence.
2. Trigger list by type.
3. Escalation path: Tier | Owner | Time Limit | Next Step.
4. Handoff template and customer update template.
5. Closure and review checklist.

## Quality checks
- Every trigger has an owner and a time limit.
- Severity examples come from the user's recent escalations where available.
- Regulatory notification duties appear with their deadlines.

## Notes from the source article
- **Replaces:** The escalation design workstream, when a team defines severity levels, triggers, handoffs, and communication cadences, then writes the runbook frontline teams follow.
- **Example request:** “Our biggest customer escalated a billing error straight to our CEO last month because support sat on it for nine days. Write us an escalation playbook that makes that impossible.”
- **What the user still owns:** Protecting the frontline person who escalates early. If escalating gets someone blamed, the playbook will be ignored.
- When handing the deliverable back, name in one line the decision above that stays with the user.
