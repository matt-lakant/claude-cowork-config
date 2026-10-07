---
name: transformation-roadmap-sequencer
description: Sequences a portfolio of initiatives into waves by value, dependency, and scarce-team capacity, and produces a quarter-by-quarter roadmap with a cumulative value curve. Use when a transformation has more approved initiatives than capacity, when building a multi-year roadmap, or when leadership asks what goes first.
---

# Transformation Roadmap Sequencer

## What this produces
A wave plan, a quarterly roadmap, a capacity heat table for scarce teams, a cumulative cost and value curve, and a named "not now" list.

## Inputs to ask for
- Initiative list (XLSX or CSV): annual value, one-time cost, duration, months to first value, confidence
- Teams each initiative needs (IT, data, finance, frontline groups) and those teams' quarterly capacity
- Hard dependencies, blackout windows (year-end close, peak season), fixed deadlines
If capacity is unknown, ask for headcount of the three scarcest teams and assume 60% is free for change work, labeled.

## Method
1. Normalize each initiative: annual value, one-time cost, months to first value, confidence high, medium, or low.
2. Separate hard dependencies (data, platform, policy, contract) from soft preferences.
3. Tag enablers (data foundations, platforms) and link each to the initiatives that depend on it.
4. Wave 1: initiatives with first value inside 6 months that fund or de-risk later waves, plus enablers on the critical path.
5. Load each scarce team by quarter. Flag any quarter above 100%.
6. Check change saturation: count concurrent major changes per frontline group. Flag more than two.
7. Build the cumulative cost and benefit curve by quarter and find the payback quarter.
8. List what is deliberately deferred, and why.

## Output format
- Wave table: Initiative | Wave | Start quarter | First value | Annual value | Cost | Dependencies | Confidence
- Quarterly roadmap (text Gantt, 6 to 8 quarters)
- Capacity heat table: Team | Q1 to Q8 load %
- Value curve table with payback quarter
- Not-now list with reasons

## Quality checks
- No hard dependency is violated
- Every over-capacity quarter is flagged with a proposed shift
- Value figures trace to business cases or are labeled estimates
- Each enabler lists the value that depends on it

## Notes from the source article
- **Replaces:** The roadmap workstream that turns forty approved initiatives into capacity-checked waves on one slide.
- **Example request:** “We have 32 approved initiatives and one IT team. Here’s the list with values and durations. Sequence it into waves we can deliver.”
- **What the user still owns:** Telling sponsors their initiative is in wave three, and defending it.
- When handing the deliverable back, name in one line the decision above that stays with the user.
