---
name: spans-and-layers-analyzer
description: Rebuilds the reporting hierarchy from an HRIS export, calculates spans of control and layers by function, flags narrow spans and excess layers, and sizes the opportunity. Use when the user suspects the organization is top-heavy, is planning a delayering or cost program, or wants manager capacity data by team.
---

# Spans and Layers Analyzer

## What this produces
Span and layer statistics by function and level, a list of outlier managers and chains, and a sized range of manager roles that could be consolidated.

## Inputs to ask for
- HRIS export (CSV or XLSX): employee ID, manager ID, title, function, location, level, FTE, fully loaded cost.
- The type of work each function does (standardized, variable, expert).
- If manager IDs are missing or broken, report the orphan count before proceeding.

## Method
1. Rebuild the tree from employee-manager pairs. Report orphans, loops, and people reporting to vacant positions.
2. Compute per manager: direct reports, total org below, and layer number from the CEO.
3. Summarize by function: median span, share of managers with 1 to 3 directs, maximum layers to the frontline.
4. Set target span ranges by work type with the user. Starting heuristics: 3 to 6 for complex expert work, 7 to 12 for mixed professional work, 12 to 20 for standardized operational work.
5. Flag outliers: managers below target range, single-report chains (a manager with one direct who also manages), and functions with more layers than the company median.
6. Size the opportunity: manager roles removable if outliers moved to the low end of the target range, with cost. Exclude roles with a documented reason (licensing, site coverage).

## Output format
1. Summary: total managers, median span, layers, % managers with 3 or fewer directs.
2. Function table: Function | Headcount | Managers | Median Span | Max Layers | Target Range | Outliers.
3. Outlier list: Manager | Function | Directs | Layer | Flag.
4. Opportunity range: roles and cost, low and high.

## Quality checks
- Headcount reconciles to the HRIS total.
- Player-coach roles are identified before being counted as narrow spans.
- The opportunity is a range, with exclusions listed.

## Notes from the source article
- **Replaces:** A delayering diagnostic, when analysts rebuild the reporting tree from the HRIS, count managers and layers, and flag every narrow span.
- **Example request:** “Attached is our HRIS export with manager IDs. Show me where we have too many layers or managers with two direct reports, and roughly what consolidating them is worth.”
- **What the user still owns:** Whether a narrow span is waste or a deliberate bet. Some managers with two reports are building a team; you know which ones.
- When handing the deliverable back, name in one line the decision above that stays with the user.
