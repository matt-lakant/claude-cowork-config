---
name: company-overview
description: Researches the company behind a job posting and produces a one-page company_overview.md in the application folder. Use whenever a job-application skill needs company context and no company_overview.md exists yet, when another skill (job-fit-analyzer, resume-tailor, interview-prep, recruiter-followup, offer-negotiator) calls for it, or when Matt asks to research a company. Also use to refresh a stale overview.
---

# Company Overview

## What this skill does

Produces a concise, factual one-page brief on the company behind a specific opportunity, saved as `company_overview.md` in that application's folder. It is the single source of company context that every other job-application skill reads. Generate it once per opportunity; the other skills reuse it rather than re-researching.

## When to run

- A job-application skill (`job-fit-analyzer`, `resume-tailor`, `interview-prep`, `recruiter-followup`, `offer-negotiator`) needs company context and `applications/<slug>/company_overview.md` does not exist.
- Matt asks to research a company, or "what does this company do".
- An existing overview is clearly stale (the company changed materially, or it's more than ~3 months old) and needs a refresh.

## Source materials

> All paths in this skill are relative to the **Job Applications project root** — the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications").

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
- Competitive landscape — main competitors / category

### Step 3 — Write `company_overview.md`

Save to `applications/<slug>/company_overview.md` (create the folder if it doesn't exist yet). Keep it to ~1 page:

- **Company:** name (+ a note if the real employer is reached via an intermediary or is anonymous)
- **What they do:** 1–2 sentences
- **Business model:** how they make money
- **Clients & sectors:** who they serve
- **Size & stage:** headcount, revenue, funding, ownership
- **Recent signals:** 2–4 dated bullets
- **Why this role exists:** the problem they're hiring to solve (infer from the posting + the business)
- **Positioning implications for Matt:** 3–5 bullets — how he should frame himself given this company
- **Sources:** the URLs used

### Step 4 — Output

Save the file, present it to Matt with a link, and return a 2-line summary. Other skills then read this file instead of re-researching.

## Hard rules

- **Search before writing — never fabricate.** Every factual claim must come from a source; cite URLs. If something can't be verified, mark it "unconfirmed" rather than guessing.
- **Flag intermediaries / anonymity.** Be explicit when the posting is via a recruiter/agency or the end client is undisclosed.
- **Keep it to ~1 page.** This is a working brief, not a dossier.
- **Date recent facts** (funding, headcount, news) and prefer current sources — company facts go stale.
- **One file per opportunity.** Reuse or refresh `company_overview.md`; don't create duplicates.
