---
name: critical-path-mapper
description: Computes the critical path and float across a multi-workstream plan, maps cross-team and external dependencies, and proposes schedule compression options. Use when a go-live date is at risk, when integrating workstream plans, or when someone asks what is really driving the timeline.
---

# Critical Path Mapper

## What this produces
The critical path, near-critical tasks, a cross-workstream dependency matrix, the top schedule risks, and compression options with trade-offs.

## Inputs to ask for
- Plan export (CSV or XLSX from Excel, Project, or Smartsheet): task, workstream, owner, duration, predecessors with type (FS, SS, FF) and lag
- Working calendar: holidays, blackout dates
- For critical tasks: optimistic, likely, and pessimistic durations if known
If predecessors are missing, draft them from task names and mark each as inferred for owner review.

## Method
1. Check the network: every task has a predecessor except the start; no loops; no dangling ends.
2. Forward pass for early start and finish; backward pass for late start and finish.
3. Total float = late start minus early start. Critical path = the chain with zero float (or the least float, if the end date is imposed). Near-critical = under 10 working days of float.
4. Flag cross-workstream and external dependencies (vendors, regulators, other programs).
5. Flag resource conflicts: one person on overlapping critical tasks.
6. For critical tasks with three estimates, expected duration = (optimistic + 4 x likely + pessimistic) / 6. Compare the expected end with the committed date; merging paths add risk beyond this.
7. Compression options: crash (add resources to critical tasks) or fast-track (overlap sequential tasks), with the added cost or risk of each.

## Output format
- Critical path: Task | Workstream | Owner | Duration | Early finish
- Near-critical tasks with float
- Dependency matrix: From workstream | To workstream | Task pairs | Type
- Top 5 schedule risks; expected versus committed end date
- Compression options: Option | Days saved | Cost or risk

## Quality checks
- No circular dependencies remain
- Dates are computed from the network, never typed in
- Inferred links are marked for review
- The working calendar is stated

## Notes from the source article
- **Replaces:** The planner who rebuilds the integrated plan across workstreams every month to find which dependencies actually drive the go-live date.
- **Example request:** “Here’s the integrated plan export for our ERP program. What’s the real critical path, and can we still make the March go-live?”
- **What the user still owns:** Choosing which option to pay for. Crashing costs money and fast-tracking costs risk, and only the sponsor can spend either.
- When handing the deliverable back, name in one line the decision above that stays with the user.
