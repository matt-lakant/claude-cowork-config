---
name: future-state-process-designer
description: Designs a future-state process from the observed current state, applying redesign principles to cut handoffs, waits, and rework, and compares current vs future on steps, handoffs, and lead time. Use when the user has an as-is map and waste analysis and needs a redesigned process, is preparing for a system implementation, or wants to test a proposed redesign.
---

# Future-State Process Designer

## What this produces
A future-state swimlane, a design rationale tied to observed pain, a before and after scorecard, and the prerequisites and pilot plan.

## Inputs to ask for
- As-is map, gap log, value stream, and root causes
- Target outcomes (lead time, cost, quality, customer experience)
- Constraints: systems, regulation, labor agreements, budget
- Automation scoring, if done
If the as-is map or waste analysis is missing, build it first.

## Method
1. Turn the top observed pain points into 4 to 6 design principles ("decide at first touch," "one owner end to end").
2. Apply the redesign moves in order: eliminate, combine, reorder, parallelize, move decisions earlier, triage simple cases into a fast lane, then automate.
3. Build workarounds that exist for good reasons into the design.
4. Give every case a single accountable owner and every handoff a service level.
5. Design the exception path explicitly; exceptions often consume most of the effort.
6. Score current vs future: steps, handoffs, decision points, systems touched, lead time, touch time.
7. List prerequisites (system changes, policy changes, skills) and a pilot: one team, 4 to 6 weeks, with measures.
8. Write a day-in-the-life walkthrough for each role and test it with the people who were observed.

## Output format
- Design principles, each linked to a gap log finding
- Mermaid swimlane of the future state
- Scorecard: Measure | Current | Future | Change
- Prerequisites: Item | Type | Owner role | Needed by
- Pilot plan and day-in-the-life walkthroughs (under 150 words per role)

## Quality checks
- Every change traces to an observed problem or root cause
- The exception path is designed
- Lead time targets reconcile with the value stream math
- Frontline validation is scheduled before rollout

## Notes from the source article
- **Replaces:** The future-state design workshops, where a team redraws the process around fewer handoffs, earlier decisions, and clear ownership.
- **Example request:** “Using the as-is map, value stream, and root causes for our new-customer onboarding, design the future state. Our goal is to cut onboarding from 21 days to under 7.”
- **What the user still owns:** Deciding which ownership lines move, which is where redesigns get political, and backing the frontline when the pilot shows what the design missed.
- When handing the deliverable back, name in one line the decision above that stays with the user.
