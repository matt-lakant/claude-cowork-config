# Level framing (rules R18, R19, R20)

Read this before drafting. What Matt cares about most is the seniority the CV conveys, and that it shows his capacity to do the work himself wherever the role calls for it (his words, 2026-11-16). Length matters far less.

## Why

Most of his applications are to roles where the person does the work: manager, team lead, individual contributor, and most freelance missions. His history says Global Director, 80+ people, ~USD 40M P&L. Read in six seconds, that answers a question nobody asked and raises two: why this job, and for how long. Two independent reviewers rejected drafts on 2026-11-16 for the same reason: "reads as a Global Director who delegates, not as someone who will do this job".

## `hands_on` role

| Where | Rule | Example |
|---|---|---|
| Header, profile, areas of expertise | No scale marker: no 80+ or 110 people, no ~USD 40M P&L, no board, C-level, SVP, no "through regional directors" | "ran its services department with 5 to 10 direct managers" |
| Above the skills matrix | At least two first-hand facts, written as facts, never the adjective "hands-on" | "SQL controls on migrated data written personally"; "effort estimates and SOWs written personally" |
| First bullet of each role | What he did himself or with his direct team | "Ran delivery with 5 to 10 direct managers and experts: regional delivery managers, solution architects, program and project leads" |
| Context line of each role | Scale, once | "Context: department of up to 110 people across sales engineering, implementation, consulting, customer success and support; ~USD 40M P&L" |
| Verbs | "oversaw", "sponsored", "governed", "ran through" become what he did (wrote, reviewed, staffed, decided, recovered) when the record supports it. When it does not, the line moves down; it is not rewritten into a claim | "Wrote and reviewed effort estimates, SOWs and RFP responses" |
| Audience of a deliverable | The voice note asks to name who a piece of work was presented to ("for the executive committee", "restitué au COMEX"). That is kept in an experience bullet below the matrix: it says what the work was, not how senior he is. It is not written above the matrix on a hands-on CV, where the script reads it as a scale marker | "AI audit presented to the executive committee" (bullet, kept) |
| Job titles | Never altered. "Global Director" stays in the role titles. The scale is placed lower, not hidden | |

First-hand facts on record (check the brief and the log for more): SQL control scripts written on data migrations, both FactSet periods; effort estimates and SOWs written personally; the Standard Chartered deployment put back on plan as last point of escalation; lakant.io built end to end; the Power BI data model and reports built personally; led implementation engineers on site at client premises (2007-2018).

## `leadership` role

The capacity to do the work oneself is not what is being bought. Scale and seniority lead and are not deflated (R20). Keep one or two first-hand facts in the experience bullets all the same: they cost nothing and answer the "too far from the ground" doubt.

## The contract type never decides

A rule of September 2026 said seniority is never deflated on a freelance mission. Matt corrected it on 2026-11-16: most freelance missions are individual-contributor roles and follow the `hands_on` rules. Only leadership mandates, permanent or freelance, keep seniority up front.

## What the script checks and what it cannot

With the tag `hands_on`, `cv_check.py` fails a scale marker above the skills matrix, warns on one in the first bullet of a role, and requires the two fragments passed with `--hands-on` to be above the matrix. It matches words. Whether a line reads as distant from the work is your judgment, and then the reviewer's.
