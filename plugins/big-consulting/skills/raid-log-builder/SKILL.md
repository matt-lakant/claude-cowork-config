---
name: raid-log-builder
description: Extracts and maintains a RAID log (risks, assumptions, issues, dependencies) from status reports, meeting notes, and plans, with scoring, owners, responses, and stale-item flags. Use when starting a program log, when updating it weekly, or before a steering committee to find what should be escalated.
---

# RAID Log Builder

## What this produces
A cleaned RAID log with scores, owners, and responses, a top-ten list, and the items to escalate this week.

## Inputs to ask for
- Recent status reports, meeting notes, and emails (attach as text or PDF)
- The existing RAID log, if any (XLSX or CSV)
- The plan milestones, so impact can be tied to dates
If there is no existing log, build one from the documents and mark every item "new, confirm owner."

## Method
1. Extract candidate items and classify: Risk (may happen), Assumption (believed true, unverified), Issue (happening now), Dependency (needs another team or party).
2. Write each risk as: "Because [cause], [event] may occur, leading to [impact on date, cost, or benefit]."
3. Score risks: probability 1 to 5 x impact 1 to 5. Issues get severity: critical, high, medium, low.
4. Assign a response: avoid, reduce, transfer, or accept, with an owner, due date, and trigger.
5. Give each assumption a validation owner and date. An assumption past its date becomes a risk.
6. For dependencies, record provider, receiver, need-by date, and whether the provider has agreed.
7. Merge duplicates. Flag items with no update in 14 days.
8. Escalate: risks scoring 15 or more, critical issues, dependencies not agreed within 20 working days of need.

## Output format
- Four tables, one per type, with ID | Description | Owner | Score or severity | Response | Due | Last updated
- Top ten by score
- Escalations this week with the decision needed
- Stale items list

## Quality checks
- Every item has one owner and a date
- Every risk states a cause
- Anything already happening is logged as an issue
- Expired assumptions have been converted to risks

## Notes from the source article
- **Replaces:** The PMO analyst who reads every status report and meeting note to maintain the risks, assumptions, issues, and dependencies log.
- **Example request:** “Here are the last four weeks of status reports and steerco notes. Build our RAID log and tell me what I need to escalate on Friday.”
- **What the user still owns:** Acting on the escalations. A well-kept log that nobody resolves is only a record of what went wrong.
- When handing the deliverable back, name in one line the decision above that stays with the user.
