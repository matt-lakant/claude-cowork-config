---
name: as-is-process-mapper
description: Builds a SIPOC and a role-by-role swimlane map of the current process from observation logs and interviews, tagging every step by source and flagging conflicts. Use when the user needs a current-state process map, is starting a redesign or system implementation, or has observation notes and interview transcripts to turn into a map.
---

# As-Is Process Mapper

## What this produces
A SIPOC, a swimlane map, and a step table showing each step's source (observed, interviewed, documented) and every conflict between sources.

## Inputs to ask for
- Observation log and gap log (from the Frontline Observation Protocol)
- Interview notes or transcripts with staff and managers
- Existing SOPs or system documentation
- Where the process starts and ends (the trigger and the final output)
If there is no observation data, build the map but mark every step "unverified."

## Method
1. SIPOC first: Suppliers, Inputs, 5 to 7 high-level Process steps, Outputs, Customers. Fix the start trigger and end point.
2. Detail the steps under each high-level step. One verb-noun action per box ("verify policy number").
3. Assign each step a lane: the role or system that performs it.
4. Mark decision points, handoffs between lanes, rework loops, and off-system work (email, spreadsheets, phone).
5. Tag every step with its source. Observed beats interviewed, which beats documented.
6. Where sources conflict, show the observed path in the main flow and log the conflict.
7. Count handoffs, decision points, systems touched, and rework loops.

## Output format
- SIPOC table
- Mermaid flowchart with one subgraph per lane
- Step table: ID | Step | Lane | System | Source | Handoff (Y/N) | Rework loop (Y/N) | Notes
- Conflict log: Step | Manager says | Staff say | Observed
- Summary counts

## Quality checks
- The map starts at the trigger and ends at the customer output
- Every step has one lane and one source tag
- Off-system work appears on the map
- The main flow follows observed reality

## Notes from the source article
- **Replaces:** The current-state mapping workshops, where a facilitator covers a conference room wall in sticky notes and the team spends days reconciling what managers say happens with what staff say happens.
- **Example request:** “Here are my observation notes and six interview transcripts from our vendor onboarding team. Build the as-is swimlane and show where managers and staff disagree.”
- **What the user still owns:** Deciding whose version to trust when the observed process embarrasses someone, and presenting the map without turning it into blame.
- When handing the deliverable back, name in one line the decision above that stays with the user.
