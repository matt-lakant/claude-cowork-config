---
name: company-overview
description: Researches the company behind a job posting and produces a one-page company_overview.md in the application folder. Use whenever a job-application skill needs company context and no company_overview.md exists yet, when another skill (job-fit-analyzer, resume-tailor, interview-prep, recruiter-followup, offer-negotiator) calls for it, or when Matt asks to research a company. Also use to refresh a stale overview.
---

# Company Overview

## Step map

| Step | What it does | What it produces | Stops the run when |
|---|---|---|---|
| 0 | Opens the opportunity (`opportunity-intake`) | `applications/<slug>/` | the slug is unknown |
| 1 | Identifies the real employer (intermediary or end client) | the entity researched | never: an unnamed end client is stated as unnamed |
| 2 | Researches the company from current sources | dated, sourced facts | never: a fact not found is written as not found |
| 3 | Writes the overview, positioning section last | `company_overview.md` | never |
| 4 | Sends the file card | the card | never |

## Before anything else — open the opportunity

**Run the `opportunity-intake` skill first.** It confirms the opportunity name, resolves
the kebab-case slug, creates `applications/<slug>/` if it does not already exist, and
starts the opportunity's `notes.md`. Every file this skill produces goes inside that
folder.

Do not write anything before the folder exists. If the slug is unknown, ask. If the
Job Applications project folder is not connected, stop and say so — never fall back to
the project root, to another connected folder, or to chat-only delivery.

## What this skill does

Produces a concise, factual one-page brief on the company behind a specific opportunity, saved as `company_overview.md` in that application's folder. It is the single source of company context that every other job-application skill reads. Generate it once per opportunity; the other skills reuse it rather than re-researching.

## When to run

- A job-application skill (`job-fit-analyzer`, `resume-tailor`, `interview-prep`, `recruiter-followup`, `offer-negotiator`) needs company context and `applications/<slug>/company_overview.md` does not exist.
- Matt asks to research a company, or "what does this company do".
- An existing overview is clearly stale (the company changed materially, or it's more than ~3 months old) and needs a refresh.

## Source materials

> All paths in this skill are relative to the **Job Applications project root** — the folder that holds `applications/`, `_assets/` and `applications_tracker.md`. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications").

- The job posting (URL or pasted text) — for the employer name and role context.
- `WebSearch` / `web_fetch` for research. The company's own website is the primary source; supplement with recent, reputable news.

## Inputs to gather (ask only if you can't infer them)

- Company name (or the posting URL/text to derive it from).
- Opportunity slug / application folder (default: `applications/<company>-<role-slug>/`).

## Workflow

### Step 1 — Identify the real employer

Derive the employing company from the posting. On aggregators (Lever, Greenhouse, LinkedIn) and freelance platforms (Collective, Comet, Malt), the posting entity may be a recruiter/agency, or the end client may be anonymous. Identify the actual employer where possible. If it's a staffing intermediary or the client is undisclosed, say so explicitly and research whoever can be identified (the intermediary, plus any clues about the end client's sector and size).

### Step 2 — Research

Use `WebSearch` / `web_fetch` (company site first, then secondary sources). Cover:

- What the company does (products / services)
- Business model — how it makes money
- Clients, customers, and sectors served
- Size and stage — headcount, revenue, funding, ownership (bootstrapped / VC / PE / public)
- Recent signals — funding rounds, growth, M&A, product launches, leadership changes, notable news
- **Funding and growth trajectory (mandatory, never skipped):** every round with date, amount
  and investors, or an explicit "no round found" with the sources checked; headcount and
  revenue trend over 2 to 3 years; any published targets or forecasts, or "none published".
  For a French company always check the registry (Pappers / BODACC via SIREN): creation
  date, share capital and its changes, accounts filed or filed confidential, auditor
  appointments, officer changes. Also check press, Crunchbase or Dealroom, and the company's
  own site and legal notice. Beware of name collisions (several companies share short names);
  confirm the match by SIREN, website or address.
- LinkedIn "associated members" and growth charts count anyone listing the company,
  including trainees or freelancers: say so when the figure is not staff.
- Competitive landscape — main competitors / category

### Step 3 — Write `company_overview.md`

Save to `applications/<slug>/company_overview.md` (create the folder if it doesn't exist yet). Keep it to ~1 page:

- **Website:** the company's official website URL, as the first line of the file, above the title or any other content (write "not found" + where checked if none exists; for an intermediary, give the intermediary's site and the end client's if identified)
- **Company:** name (+ a note if the real employer is reached via an intermediary or is anonymous)
- **What they do:** 1–2 sentences
- **Business model:** how they make money
- **Clients & sectors:** who they serve
- **Size & stage:** headcount, revenue, funding, ownership
- **Funding & growth trajectory:** rounds (or "none found" + where checked), headcount and revenue trend, published forecasts (or "none published"), registry signals
- **Recent signals:** 2–4 dated bullets
- **Why this role exists:** the problem they're hiring to solve (infer from the posting + the business)
- **Sources:** the URLs used
- **Positioning implications for Matt:** 3–5 bullets — how he should frame himself given this company **Always the last section of the file, under its own heading `## Positioning implications for Matt`.** Everything above it describes the company; this section is advice to the drafting skills. The red-team skills cut the file at this heading before giving it to the reviewer, so nothing a reviewer needs may be written below it, and no positioning advice may be written above it.

### Step 4 — Output

Save the file, present it to Matt with a link, and return a 2-line summary. Other skills then read this file instead of re-researching.

## Hard rules

- **Files for an opportunity live in `applications/<slug>/`, never at the project root.** The rule and its exceptions are in `opportunity-intake` (Hard rules), which wins on any conflict.
- **Search before writing — never fabricate.** Every factual claim must come from a source; cite URLs. If something can't be verified, mark it "unconfirmed" rather than guessing.
- **Flag intermediaries / anonymity.** Be explicit when the posting is via a recruiter/agency or the end client is undisclosed.
- **Website first.** The company's official website URL is always the first line of `company_overview.md`, above everything else.
- **Keep it to ~1 page.** This is a working brief, not a dossier.
- **Date recent facts** (funding, headcount, news) and prefer current sources — company facts go stale.
- **One file per opportunity.** Reuse or refresh `company_overview.md`; don't create duplicates.
