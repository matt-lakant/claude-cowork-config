---
name: erlang-c-staffing-model
description: Calculates required agents by interval using Erlang C from volume, handle time, and service-level targets, then converts to scheduled FTE with shrinkage and tests scenarios. Use when the user is sizing a contact center or support team, checking whether current staffing fits demand, or modeling a change in volume, handle time, or service level.
---

# Erlang C Staffing Model

## What this produces
Required agents by interval, scheduled FTE after shrinkage, expected service level and occupancy, and a scenario table.

## Inputs to ask for
- Contact volume by 30-minute interval, or by day with an interval profile (CSV or XLSX).
- Average handle time (talk plus hold plus after-contact work).
- Service-level target (for example, 80% answered in 20 seconds) and occupancy cap.
- Shrinkage (breaks, training, absence, meetings). If unknown, use 30% and label it.
- Current scheduled headcount for comparison.

## Method
1. Traffic intensity per interval: A = contacts x AHT (seconds) / interval length (seconds).
2. For N agents above A, compute the Erlang C probability of waiting, P(wait). Service level = 1 minus P(wait) x e^(minus (N minus A) x target seconds / AHT).
3. Find the smallest N that meets the service-level target with occupancy (A / N) at or below the cap (85 to 90% is a common ceiling).
4. Scheduled agents = N / (1 minus shrinkage). Sum to FTE using paid hours per FTE.
5. Note that Erlang C assumes no caller abandons, so it overstates need when abandonment is material; if abandonment exceeds 5%, say so and suggest Erlang A.
6. Run scenarios: volume plus 10%, AHT minus 10%, service-level target change.

## Output format
1. Interval table: Interval | Volume | AHT | A | Required N | Service Level | Occupancy | Scheduled.
2. Summary: peak and average requirement, total FTE, gap versus current.
3. Scenario table: Scenario | FTE | Change.
4. Assumptions.

## Quality checks
- Show the calculation for one interval step by step.
- Occupancy never exceeds the cap.
- Shrinkage is applied once.

## Notes from the source article
- **Replaces:** A workforce management review, when analysts forecast interval volume, run Erlang C to service level, apply shrinkage, and show how many agents each hour needs.
- **Example request:** “Here’s our interval volume for the last four weeks and 6.5-minute AHT. How many agents do we need to hit 80/20, and what happens if AHT drops a minute?”
- **What the user still owns:** The service-level target itself. The model prices each second of speed; what customers deserve at that price is a business call.
- When handing the deliverable back, name in one line the decision above that stays with the user.
