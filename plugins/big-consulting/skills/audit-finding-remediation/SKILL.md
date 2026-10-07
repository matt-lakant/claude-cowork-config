---
name: audit-finding-remediation
description: Analyzes internal or external audit findings for root cause, groups related findings, and builds a remediation plan with owners, dates, and validation steps. Use when the user has an audit report, a material weakness or significant deficiency, repeat findings, or a regulator exam letter to respond to.
---

# Audit Finding Root Cause and Remediation Planner

## What this produces
Root cause per finding, systemic causes grouped, a remediation plan with validation criteria, and draft management responses.

## Inputs to ask for
- The audit report or findings list (attach PDF)
- Prior findings from the last two cycles, to spot repeats
- Deadlines set by auditors or regulators
- If root-cause facts are missing, write the questions for the control owners

## Method
1. Restate each finding in five parts: condition (what was found), criteria (what should be), cause, effect (risk or impact), and corrective action.
2. Find root cause with five whys. Stop at a cause management can act on. Classify it: people (skills, capacity), process (design gap), technology (system limit, access), or governance (unclear ownership, no monitoring).
3. Group findings by shared root cause. Five findings from one cause need one fix.
4. Flag repeats; they signal the prior fix treated a symptom.
5. Design remediation that removes the cause: named deliverable, owner, due date, and evidence of completion.
6. Define validation: how and when the fix will be tested, over what period of operation, before the finding closes.
7. Draft management responses: agree or disagree, action, owner, date.

## Output format
- Finding table: ID | Condition | Criteria | Root cause | Category | Repeat (Y/N) | Severity
- Systemic causes: Cause | Findings affected | Fix
- Remediation plan: Action | Owner | Due | Evidence | Validation method | Validation date
- Draft management responses

## Quality checks
- No root cause is "human error" without asking why the error was possible
- Every action has one owner and a date
- Validation includes a period of operation
- Repeat findings get a stronger fix than last time

## Notes from the source article
- **Replaces:** The remediation workstream after a bad audit: root-cause sessions and the corrective action plan the audit committee tracks.
- **Example request:** “Internal audit gave us six findings on user access, three of them repeats. Here’s the report. Find the real cause and write our management responses.”
- **What the user still owns:** Funding the fix and holding the owners to their dates when the audit committee asks again next quarter.
- When handing the deliverable back, name in one line the decision above that stays with the user.
