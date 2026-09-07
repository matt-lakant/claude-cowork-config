---
name: application-tracker
description: Maintains the live tracker file of Matt Cornet's job applications in applications_tracker.md — adds new rows, updates statuses, computes follow-up due dates, and surfaces what needs action this week. Use whenever Matt mentions tracking applications, asks "what's open", "what should I follow up on", "did I apply to X", or wants to add a new application. Also use proactively when other skills (resume-tailor, recruiter-followup) complete a meaningful action that should be logged.
---

# Application Tracker

## What this skill does

> All paths in this skill are relative to the **Job Applications project root** — the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications").

Owns the application tracker file at the project root: `applications_tracker.md`.

The tracker is the single source of truth for what Matt has applied to, where each application stands, and what the next action is. It's append-only on history (Notes) but mutable on status fields.

**Format note (2026-05-04 onwards):** the tracker is now a single **markdown file**, not the legacy `applications_tracker.xlsx`. Reason: the xlsx triggered persistent OneDrive Files-On-Demand placeholder issues + Excel exclusive-lock problems that made automated updates unreliable. Plain text removes both. The xlsx is preserved as a frozen historical archive — do not edit it.

## File structure (must be preserved on every edit)

The markdown file has two sections:

1. **Summary table** at the top — one row per application, compact (7 columns: ID, Company, Role, Status, Next action due, Geo, Folder). Used for at-a-glance scan.
2. **Per-application detail sections** below — one `### ID N — Company — Role` heading per application, followed by a 17-row metadata table and free-form Notes. This is the rich record.

Plus a **"What's open this week"** sub-block under the summary that lists overdue and upcoming actions.

## Schema

Per-application detail table fields:

| Field | Type | Notes |
|---|---|---|
| Company | str | Canonical name |
| Role | str | Title as posted |
| Level | str | Director / VP / SVP / C-suite / IC / Lead / etc. |
| Source | str | LinkedIn, referral name, recruiter name, direct |
| URL | str | Job posting URL |
| Date drafted | date | First touch (CV started, etc.) |
| Date applied | date | When the application went in |
| Last touch | date | Most recent contact in either direction |
| Status | enum | `drafted`, `applied`, `screen`, `interview-1`, `interview-2`, `interview-final`, `offer`, `negotiating`, `accepted`, `rejected`, `withdrawn`, `ghosted` |
| Next action | str | "Follow up by 2026-05-02", "Prep for panel 5/8", etc. |
| Next action due | date | Drives the "what's open this week" view |
| Recruiter | str | Name + company if external |
| Hiring manager | str | If known |
| Comp band | str | If disclosed |
| Geo | str | NY / Paris / remote / hybrid-X |
| Folder | str | Pointer to `applications/<company>-<role>/` |
| Notes | str | **Append-only** with date stamps — never overwrite |

## Workflow

## Opportunity name — MANDATORY

**Before any other step,** check whether Matt has already provided an opportunity name in this conversation.

- If yes: use it.
- If no: ask him — *"Quel est le nom de cette opportunité ?"* (FR) or *"What is the name of this opportunity?"* (EN) — wait for his answer before proceeding.

Once the name is confirmed, **immediately display this reminder as a blockquote at the top of your response**, before any other output:

> 📝 **Renommer cette conversation en :** "[OpportunityName]"

The opportunity name is used to:
- Name the application folder: `applications/<opportunity-slug>/` (kebab-case)
- Name output files: `<OpportunityName>_<YYYY-MM-DD>_v1.docx` (underscores, increment version if file exists)

### Adding a new application

1. **Read the file** with the file tools (Read), confirm current state.
2. Find the next ID (max existing ID + 1).
3. **Append a row** to the summary table.
4. **Append a detail section** below (heading `### ID N — Company — Role` + metadata table + Notes).
5. Set Status defaults: `drafted` if `resume-tailor` just ran but Matt hasn't said it's submitted; `applied` if he confirms.
6. Compute Next-action-due:
   - `drafted` → +2 days (review and submit)
   - `applied` → +10 days (follow-up if no response)
   - `screen` / `interview-*` → +2 days post-interview (thank-you note)
   - `offer` → +3 days (decision/counter)
7. **Re-render the "what's open this week" sub-block** with the new row included.
8. Save. Show Matt a 1-line confirmation in chat plus a computer:// link.

### Updating status

1. Read the file.
2. Find the row by Company + Role (fuzzy match — confirm if multiple match).
3. Update Status, Last-touch, Next-action, Next-action-due in **both** the summary table and the detail section.
4. **Append** to Notes with a date stamp (`2026-05-12: ...`) — never replace.
5. Re-render the "what's open this week" sub-block.
6. Save.

### "What's open" / weekly review

When Matt asks what's open or what to do this week:

1. Read the file.
2. Filter rows where Next-action-due ≤ today + 7 days, grouped by status.
3. Render a markdown table in chat: ID | 