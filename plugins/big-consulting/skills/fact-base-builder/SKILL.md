---
name: fact-base-builder
description: Builds a reconciled, source-graded fact base from attached financials, KPI reports, exports, and documents, flagging conflicts and gaps against the issue tree. Use at the start of any analytical project, when numbers from different sources disagree, or before building a baseline for a business case.
---

# Fact Base Builder

## What this produces
A fact register of every material number with source and reliability grade, a conflicts log with the reconciled value, and a data request list for the gaps.

## Inputs to ask for
- All available sources: P&L and GL exports, KPI dashboards, operational system exports (CSV or spreadsheet), board decks, annual reports
- The key question or issue tree, so facts can be mapped to branches
- The baseline period (e.g., trailing twelve months, last fiscal year)
If no issue tree exists, organize facts by P&L line and operating KPI instead.

## Method
1. Inventory every source: owner, period, system of origin, date produced.
2. Grade reliability: A (system of record, e.g., GL, billing), B (management report derived from a system), C (estimate, spreadsheet model, or anecdote).
3. Extract facts: value, unit, period, definition, source, grade.
4. Normalize: same currency, same period, same unit, same definition (gross vs net, booked vs billed).
5. Reconcile conflicts: when two sources disagree by more than 2%, explain the difference (timing, definition, scope) and choose the value from the higher-grade source.
6. Map each fact to the issue-tree branch it informs. Branches with no A or B fact are gaps.
7. Write the data requests: exact field, system, period, and who likely owns it.

## Output format
- Fact register: Fact | Value | Unit | Period | Definition | Source | Grade | Branch
- Conflicts log: Metric | Source 1 value | Source 2 value | Cause of difference | Value used
- Gap list by branch
- Data request list: Field | System | Period | Likely owner | Priority

## Quality checks
- Every fact carries a source and a grade
- No computed figure mixes periods or definitions
- Every conflict above 2% is explained, not averaged
- Grade C facts are never used as a baseline without a label

## Notes from the source article
- **Replaces:** The first two weeks of data gathering: analysts collecting every report, export, and deck the client has, reconciling the three different revenue numbers, and building the baseline the whole project argues from.
- **Example request:** “I’ve attached our GL export, the ops dashboard, and last quarter’s board deck. Build a clean fact base for the procurement savings project and tell me where the numbers disagree.”
- **What the user still owns:** Declaring which number is the official baseline. Finance and operations will each defend their version, and someone senior has to pick.
- When handing the deliverable back, name in one line the decision above that stays with the user.
