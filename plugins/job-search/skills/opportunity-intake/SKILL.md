---
name: opportunity-intake
description: "The front door of the job-search pipeline. Opens an opportunity: confirms its name, creates its folder under applications/, starts its notes file, and routes to the right next skill. Use whenever a named company, recruiter, hiring manager, agency contact, mission or role enters the conversation and anything at all is going to come out of it — a LinkedIn thread, a call to prepare, a freelance enquiry, a targeting note, a spontaneous application — and before any other job-search skill writes a file. Every other job-search skill calls this first."
---

# Opportunity Intake

## What this skill does

Opens an opportunity and gives it a home before any work happens:

1. Confirms the opportunity name.
2. Creates `applications/<slug>/` if it does not exist.
3. Starts `applications/<slug>/notes.md` if it does not exist.
4. Routes to the skill that should actually do the work.

It exists because the pipeline's entry point was implicit. When no other skill
fired — a LinkedIn thread, a call to prepare, a mission enquiry — deliverables got
written wherever the session happened to be, and the opportunity lost its file history.
Observed repeatedly in September 2026: seven opportunity files loose in the project root.

## When this runs

- **First, in every other job-search skill.** They all point here.
- **On its own**, whenever a named company, recruiter, hiring manager, agency contact,
  mission or role enters the conversation and a file is going to come out of it.

Trigger on the **subject**, not the verb. *"Prépare-moi pour l'appel avec Nick de
Masento"* opens an opportunity even though nobody said *interview*, *resume* or *apply*.
So does a targeting note, a LinkedIn message to a named person at a named company, a
freelance mission brief, or a spontaneous candidature. Nothing has to have been applied
to yet — a first call is an opportunity.

Work that is genuinely **not** tied to one opportunity — a market sweep, a list of open
roles across several companies, a review of Matt's own LinkedIn profile — does not open
one. See *Non-opportunity outputs* below.

## Precondition — the project folder must be connected

> Paths in this skill are relative to the **Job Applications project root** — the folder
> holding `applications/`, `_assets/` and `applications_tracker.md`.

1. Run `ls $HOME/mnt/` and look for `Job Applications`.
2. If it is not there, call `device_request_folder_access` on
   `C:\Users\mattc\OneDrive\Documents\Claude\Projects\Job Applications`.
3. If that fails, **stop and tell Matt**. Do not fall back to another connected folder,
   to the `claude-cowork-config` repo, or to chat-only delivery. A deliverable with no
   folder is a deliverable that gets lost.

## Step 1 — Confirm the opportunity name

Check whether Matt has already named it in this conversation.

- If yes: use it.
- If no: ask — *"Quel est le nom de cette opportunité ?"* (FR) or *"What is the name of
  this opportunity?"* (EN) — and wait for the answer before writing anything.

Once confirmed, display this reminder as a blockquote at the top of the response:

> 📝 **Renommer cette conversation en :** "[OpportunityName]"

## Step 2 — Resolve the slug

Format: `applications/<company>-<role-slug>/`, kebab-case, ASCII, no accents
(`mister-ia-consultant-freelance`, `masento-freelance-manufacturing`).

**List `applications/` and compare before creating anything.** If a folder for the same
company and a similar role already exists, reuse it — do not create a near-duplicate. If
two existing folders could both fit, ask Matt rather than guessing. A genuinely different
or re-posted role at the same company gets its own folder with a distinguishing suffix;
record the relationship in `notes.md`.

## Step 3 — Create the folder and the notes file

```bash
mkdir -p "$HOME/mnt/Job Applications/applications/<slug>"
```

If `notes.md` does not exist yet, create it with this skeleton and fill what is known.
Leave a field blank rather than inventing it.

```markdown
# <Opportunity name>

| | |
|---|---|
| Company | |
| Role / mission | |
| Source | LinkedIn / recruiter / job board / referral / spontaneous |
| Contacts | name, title, how reached |
| Opened | <YYYY-MM-DD> |
| Status | first contact |

## What we know

## Open questions

## Timeline
- <YYYY-MM-DD> — opened
```

State the resolved path once, in one line, then get on with the real work. No ceremony.

## Step 4 — Route

Hand off to the skill that does the work. Run it in the same turn — do not stop and ask
Matt what he wants next when the request already says.

| What Matt is asking for | Next skill |
|---|---|
| A name or a contact, no posting yet | `company-overview`, then come back |
| "Should I apply?", a posting to triage | `job-fit-analyzer` |
| A resume or cover letter for this role | `resume-tailor` then `resume-redteam` (mandatory gate) |
| A call, screen or interview to prepare | `interview-prep` |
| A message to a recruiter or hiring manager | `recruiter-followup` |
| An offer on the table | `offer-negotiator` |
| Nothing yet, just capture it | stay here; `notes.md` is the deliverable |

Whatever runs, `application-tracker` owns the row in `applications_tracker.md`. Creating
the folder is **not** logging the application — the row is the record, the folder is not.

## Step 5 — Pin the folder for the session

Every file produced for this opportunity from here on goes inside that folder, whatever
skill produces it: call preps, company overviews, tailored resumes, cover letters,
LinkedIn messages, correspondence, notes. Subfolders (`interview_prep/`,
`correspondence/`, `negotiation/`) follow the owning skill's own convention.

Per Matt's standing preference, every file is **also** surfaced as a clickable card with
`SendUserFile`. The card and the folder are both required; the card alone is not delivery.

## Non-opportunity outputs

Market sweeps, multi-company role lists, and reviews of Matt's own profile or assets go to:

```
_research/<topic>_<YYYY-MM-DD>.md
```

Create `_research/` if it does not exist. These do not open an opportunity and they do
not belong in the project root either.

## Hard rules

- **Never write an opportunity-scoped file to the project root.** If the slug is unknown,
  ask. If the folder is missing, create it. If it cannot be created, stop and say so.
- **The "project folders are kept flat, no subfolders" preference does not apply to
  Job Applications.** This project is an explicit exception: `applications/<slug>/`,
  `_assets/`, `_research/`. When the flat rule and this skill conflict, this skill wins.
- **Do not wait for a formal application.** A first call, a recruiter DM or an
  exploratory coffee opens an opportunity. The folder is cheap; the lost history is not.
- **Do not rename or move existing application folders** without asking. The tracker's
  `Folder` column points at them.
- **Do not stall on the routing table.** This skill is the front door, not a gate. Open
  the opportunity in one line and continue to the real work in the same turn.
