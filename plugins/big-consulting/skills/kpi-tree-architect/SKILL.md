---
name: kpi-tree-architect
description: Builds a KPI tree that links a top financial outcome (such as ROIC, EBITDA, or free cash flow) down to operational metrics owned by named teams, with definitions, formulas, and targets. Use when the company tracks too many metrics, when KPIs conflict across functions, or when designing a performance dashboard.
---

# KPI Tree Architect

## What this produces
A KPI tree from one financial outcome to operational leaf metrics, a metric dictionary with definitions and owners, and a cut list of metrics to retire.

## Inputs to ask for
- The top outcome leadership manages to (default: EBITDA or ROIC)
- The current KPI list or dashboards (attach)
- Org structure: which teams own which processes
If no top outcome is given, propose ROIC and confirm before building.

## Method
1. Decompose the top outcome by arithmetic identity. For ROIC use DuPont-style logic (DuPont analysis splits return on equity into margin x asset turnover x equity multiplier; the ROIC version is NOPAT margin x invested capital turnover), then split margin into revenue and cost lines and turnover into working capital and fixed assets.
2. Continue to operational levers a team can move weekly: on-time delivery, first-pass yield, DSO, utilization, conversion rate.
3. Assign each leaf a single accountable owner. A metric with two owners has none.
4. Write each definition: formula, data source, frequency, unit, and whether higher is better.
5. Mark leading versus lagging indicators; each branch needs at least one leading metric.
6. Map the existing KPI list onto the tree. Metrics that sit nowhere on it go to the retire list unless they serve compliance.

## Output format
- KPI tree as an indented outline with formulas at each node
- Metric dictionary: Metric | Formula | Source | Frequency | Owner | Leading/Lagging | Direction
- Retire list: Metric | Reason
- Recommended executive dashboard: 8 to 12 metrics maximum

## Quality checks
- Each level reconciles mathematically to its parent
- Every leaf has exactly one owner
- Every branch has at least one leading indicator
- The dashboard stays under 12 metrics

## Notes from the source article
- **Replaces:** The metric architecture work in a performance-management project: consultants decomposing the financial outcomes into operational KPIs, defining each one, and cutting a list of 200 metrics to the few that matter.
- **Example request:** “We track about 150 KPIs and nobody knows which matter. Build a KPI tree from EBITDA down to what our plant and sales teams control.”
- **What the user still owns:** Enforcing the retire list. Every metric has a sponsor who built a report around it, and cutting them is a leadership call.
- When handing the deliverable back, name in one line the decision above that stays with the user.
