---
name: application-tracker
description: Maintains the live tracker file of Matt Cornet's job applications in applications_tracker.md — adds new rows, updates statuses, computes follow-up due dates, and surfaces what needs action this week. Use whenever Matt mentions tracking applications, asks "what's open", "what should I follow up on", "did I apply to X", or wants to add a new application. Also use when he asks why applications get no reply, what is working, or what separates the ones that got interviews (outcome review). Also use proactively when other skills (resume-tailor, recruiter-followup) complete a meaningful action that should be logged.
---

# Application Tracker

## Before anything else — open the opportunity

**Run the `opportunity-intake` skill first.** It confirms the opportunity name, resolves
the kebab-case slug, creates `applications/<slug>/` if it does not already exist, and
starts the opportunity's `notes.md`. Every file this skill produces goes inside that
folder.

Do not write anything before the folder exists. If the slug is unknown, ask. If the
Job Applications project folder is not connected, stop and say so — never fall back to
the project root, to another connected folder, or to chat-only delivery.

## What this skill does

> All paths in this skill are relative to the **Job Applications project root** — the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications").

Owns the application tracker file at the project root: `applications_tracker.md`.

The tracker is the single source of truth for what Matt has applied to, where each application stands, and what the next action is. It's append-only on history (Notes) but mutable on status fields.

**Format note (2026-05-04 onwards):** the tracker is now a single **markdown file**, not the legacy `applications_tracker.xlsx`. Reason: the xlsx triggered persistent OneDrive Files-On-Demand placeholder issues + Excel exclusive-lock problems that made automated updates unreliable. Plain text removes both. The xlsx is preserved as a frozen historical archive — do not edit it.

## File structure (must be preserved on every edit)

The markdown file has two sections:

1. **Summary table** at the top — one row per application, 13 columns in this order: ID, Company, Role, Fit, Channel, Referral, AI title, Seniority, Status, Reply (days), Next action due, Geo, Folder. Used for at-a-glance scan and for the outcome review.
2. **Per-application detail sections** below — one `### ID N — Company — Role` heading per application, followed by a metadata table (the 17 fields below plus the six outcome fields) and free-form Notes. Some older sections use French labels (`Champ | Valeur`, `Statut`) or a bullet list instead of a table; keep the format a section already has. This is the rich record.

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

### Outcome fields (added 2026-09-24)

Six fields that exist in the summary table **and** the detail section. They exist so the
outcome review can say what separates applications that got a reply from those that did
not. The fit score alone did not: in September 2026 the two cold applications that got a
reply (Valiantys 38/50, UpSlide 37/50) scored no higher than four that were ghosted (40 to 43/50).

| Field | Values | Rule |
|---|---|---|
| Fit | `NN/50` or `—` | The `job-fit-analyzer` total. `—` means never scored; never estimate one after the fact. |
| Channel | `cold` / `agency` / `platform` / `inbound` / `outreach` / `referral` | `cold` = company ATS, careers page or LinkedIn apply. `agency` = Matt applied to a cabinet's posting. `platform` = freelance marketplace (Collective, WTTJ freelance). `inbound` = a recruiter or agency approached Matt first. `outreach` = Matt contacted an insider with no posting. `referral` = an insider introduced him. The ATS name stays in `Source`. |
| Referral | `yes` / `no` | `yes` only if a named insider vouched for him, even when the channel is `cold`. |
| AI title | `yes` / `no` | `yes` if the posted title contains AI, IA or agentic. Literal: an AI company's role with no AI word in the title is `no`. |
| Seniority | `match` / `below` / `above` / `?` | Role level against Matt's (Global Director / Head-of). Take it from the fit analysis (a "seniority inversion" is `below`); `?` if nothing says. |
| Reply (days) | `N (type)` / `≤N (type)` / `none` / `n/a` | Days from Date applied to the first human reply of any kind, with its type: `invite`, `call`, `screen`, `reject`. `≤N` when only an upper bound is known. `none` while nothing came back; `n/a` if never submitted. For `inbound`, count from when Matt sent his CV. |

## Workflow

### Opportunity name — MANDATORY

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
5. Fill the six outcome fields. Fit comes from the `job-fit-analyzer` run for this opportunity (`—` if it did not run); Reply starts at `n/a` for `drafted` and `none` for `applied`. Ask Matt for Referral if you do not know.
6. Set Status defaults: `drafted` if `resume-tailor` just ran but Matt hasn't said it's submitted; `applied` if he confirms.
7. Compute Next-action-due:
   - `drafted` → +2 days (review and submit)
   - `applied` → +10 days (follow-up if no response)
   - `screen` / `interview-*` → +2 days post-interview (thank-you note)
   - `offer` → +3 days (decision/counter)
8. **Re-render the "what's open this week" sub-block** with the new row included.
9. Save. Show Matt a 1-line confirmation in chat plus a computer:// link.

### Updating status

1. Read the file.
2. Find the row by Company + Role (fuzzy match — confirm if multiple match).
3. Update Status, Last-touch, Next-action, Next-action-due in **both** the summary table and the detail section.
4. **Append** to Notes with a date stamp (`2026-05-12: ...`) — never replace.
5. **On the first reply of any kind** (invite, call, screen, rejection), set Reply (days) in both places. It is set once and never overwritten by later replies. When a `drafted` row moves to `applied`, change Reply from `n/a` to `none`.
6. Re-render the "what's open this week" sub-block.
7. Save.

### "What's open" / weekly review

When Matt asks what's open or what to do this week:

1. Read the file.
2. Filter rows where Next-action-due ≤ today + 7 days, grouped by status.
3. Render a markdown table in chat: ID | Company | Role | Status | Next action | Due | Late by. Sort by due date ascending, overdue rows first.
4. Group into three blocks, in this order:
   - **Overdue** — `Next action due` < today. Show how many days late.
   - **This week** — due between today and today + 7.
   - **Waiting** — status `applied`, `screen` or `interview-*` with no `Next action due` set, so nothing falls silently out of view.
5. For each row, name the skill that resolves it: `recruiter-followup` for a follow-up or a thank-you, `interview-prep` for an interview, `offer-negotiator` for an offer, `resume-tailor` for a `drafted` row that was never submitted.
6. Close with a one-line count: "N overdue, N this week, N waiting."
7. A weekly review is read-only. Do not write to the file unless a status actually changed in the same turn.

### Outcome review ("why am I not getting interviews?")

When Matt asks what is working, why applications get no reply, or what separates the ones
that did:

1. Read the file. Keep only rows that were submitted (Reply is not `n/a`) at least 21 days
   ago; list the too-recent ones separately rather than counting them as silent. Valiantys
   replied after 61 days, so a young `none` is not yet a no.
2. Count replies by Channel, AI title, Seniority and fit band (`≥40`, `35-39`, `<35`, `—`).
   Show each as a markdown table: segment | submitted | human reply | rejections.
3. Compare rows **within the same fit band** that had different outcomes, and name what
   differs between them in the fields and the Notes.
4. Give the sample size with every conclusion, and label a pattern resting on fewer than
   five replies as a hypothesis.
5. A review is read-only unless Matt asks for a change. If a field is `?` or `—` on rows
   that matter to the comparison, ask him to fill it rather than guessing.

### Answering "did I apply to X?"

1. Read the file.
2. Match X against Company and Role across the summary table, fuzzy.
3. If found, answer with the ID, Status, Date applied and Next action, plus a `computer://` link to the application folder.
4. If not found, say so plainly and offer to add it. Never infer an application from the existence of a folder under `applications/` — the row is the record, the folder is not.

### Quarterly pruning

Once a quarter, propose moving rows whose Status is `rejected`, `withdrawn` or
`accepted-and-other-rejected` and whose Last touch is more than 6 months old into
`applications_tracker_archive.md`, same two-part structure as the live file.

**Propose, never do it unasked, and never delete.** An archived row keeps its ID and its
full Notes history; the live file loses the row entirely rather than keeping a stub. If Matt
declines, leave everything in place and do not ask again that quarter.

## Delivery

- The tracker file is the deliverable. After every write, confirm in one line in chat with a `computer://` link to it.
- Chat output is a table, never a prose summary.
- Never produce a PDF, and never export the tracker back to xlsx. See the format note above.

## Hard rules

- **No opportunity-scoped file is ever written to the project root.** Everything for an
  opportunity lives in `applications/<slug>/`. Only `applications_tracker.md`, `README.md`,
  `_assets/` and `_research/` belong at the root. The standing "project folders are kept
  flat, no subfolders" preference does **not** apply to Job Applications — see the
  `opportunity-intake` skill, which wins on any conflict.
- **Notes are append-only.** Add a date-stamped line; never rewrite or delete an existing one. A later line may supersede an earlier one, and that history is what makes the record trustworthy.
- **Both places or neither.** Status, Last touch, Next action, Next action due and the six outcome fields exist in the summary table *and* in the detail section. Updating one without the other corrupts the tracker silently.
- **Never invent a fit score or a reply date.** `—` and `≤N` exist so a missing value stays visible.
- **Never invent a date.** If Matt says "I applied last week", ask him for the date rather than computing one.
- **Never change an ID**, and never reuse the ID of a withdrawn or rejected application.
- **Do not edit `applications_tracker.xlsx`.** It is a frozen archive.
- **Do not add a value to the Status enum without asking.** The twelve statuses above are what
  the weekly review filters on; a thirteenth invented mid-turn makes a row invisible to it.
- **Preserve the markdown table alignment.** Keep the column widths consistent when you write a
  row, so the table stays scannable in a plain text editor and in git diffs, not only in a
  renderer.
- **Confirm before acting on a fuzzy match that hits more than one row.** Two applications at the same company are common.

## Edge cases

- **The tracker file does not exist yet:** create it with both sections and an empty "What's open this week" sub-block, then add the first application. Do not silently start a different file name.
- **Matt reports an outcome for an application that has no row:** add the row retroactively, ask for the dates rather than guessing them, and stamp the Notes with the date he told you.
- **A status moves backwards** (e.g. `interview-2` → `screen`): allow it, but append a Notes line saying so. It usually means a process restarted or a second role at the same company.
- **Matt re-applies to a role that already has a row** (the posting reopened, or he was rejected
  and the company came back): add a **new ID** rather than reopening the old one, and put a Notes
  line on both rows pointing at the other. The old row keeps its outcome; the history of the two
  attempts is the point.
- **`ghosted` vs `rejected`:** use `rejected` only for an explicit rejection. No answer after two follow-ups is `ghosted`.
