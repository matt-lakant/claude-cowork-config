---
name: job-fit-analyzer
description: Analyzes how well Matt Cornet fits a specific job posting before he invests time tailoring a resume or applying. Produces a fit score, gap analysis, ATS keyword check, and a go/no-go recommendation. Use this whenever Matt shares a posting and asks "should I apply", "is this a fit", "how do I match up", or pastes a JD without explicitly saying what he wants — the right default is to triage fit before tailoring. Also use when he asks to compare multiple postings.
---

# Job Fit Analyzer

## What this skill does

Triage a job posting against Matt's profile in 2–3 minutes of reading time. The output answers: *should he apply, and if yes, with what angle?*

This skill is upstream of `resume-tailor` — running it first prevents wasted effort tailoring resumes for poor-fit roles.

## Source materials

> All paths in this skill are relative to the **Job Applications project root** — the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications").

1. `_assets/candidate_profile.md` — read this first.

## Workflow

### Step 0 — Company overview (prerequisite)

This skill relies on the application's `company_overview.md`. **If `applications/<opportunity-slug>/company_overview.md` does not exist, run the `company-overview` skill first** to research the company and create it. If it already exists, read and reuse it (refresh it via `company-overview` if it's clearly stale).

Carry its insights into every later step — especially domain fit, the narrative angle, and the ATS keyword read.

### Step 1 — Extract from the posting
- Role title, level, function, comp band (if disclosed)
- Hard requirements: years experience, must-have skills, certifications, geo/work-auth
- Soft requirements
- Domain (fintech sub-sector? buy-side, sell-side, market data, payments, banking?)
- Top 15–20 ATS keywords (verbatim)

### Step 2 — Score on five dimensions (0–10 each)

| Dimension | What to look for |
|---|---|
| **Domain fit** | Financial services depth, sub-sector match (research, asset management, market data) |
| **Seniority fit** | Director/VP/Head-of vs. IC; is he over- or under-leveled? |
| **Functional fit** | Product, sales, professional services, transformation, AI — match against his 20-year track |
| **Skill match** | Hard requirements he has vs. lacks (be precise) |
| **Hidden fit** | Bilingual EN/FR, NY/Paris, post-merger integration, AI productization, P&L ownership — these can elevate a borderline role |

Sum to a 0–50 score. Map to recommendation:
- 40–50: Strong fit — apply with a tailored resume
- 30–39: Borderline — apply only if the role is unusually attractive or the angle is clear
- 20–29: Stretch — likely a no, but flag if there's a unique hook
- 0–19: Pass

### Step 2.5 — Requirement-by-requirement coverage matrix

The five-dimension score is the headline; this step is the detail that makes it trustworthy and feeds `resume-tailor`. **Enumerate every requirement the posting lists** — each hard requirement, each soft / "nice-to-have", and every named tool, certification, regulation, sector, and scope bar — as its own row. For each, mark coverage against `candidate_profile.md` + `master_resume.docx`:

| Coverage | Meaning |
|---|---|
| ✅ Strong | Clearly evidenced in the profile/master with specifics |
| 🟡 Partial | Adjacent or implied, but not explicit or not at full scope |
| ❌ Absent | Nothing on record |
| ❓ Unknown | Plausibly in his 20-yr background but not documented — a likely *hidden match* |

Rules:
- One JD line = one row. Do not collapse multiple requirements into a single row.
- Lean toward ❓ rather than ❌ when the requirement is the kind of thing he may well have done but never wrote down — those are exactly the rows `resume-tailor` will mine.
- Total the coverage (e.g. "6 Strong / 3 Partial / 1 Absent / 2 Unknown") and use it to sanity-check the five-dimension score.

**Hand-off:** flag every 🟡 / ❓ row as a question for `resume-tailor`'s mining step (Step 2b). State explicitly that the fit score reflects only what is documented *today*, and that resolving the 🟡 / ❓ rows through questioning could raise it.

### Step 3 — Gap and risk analysis

For each gap, classify as:
- **Real gap** — he doesn't have this; can't be papered over (e.g., "10 years in payments")
- **Framing gap** — he has the underlying capability but it's labeled differently (e.g., JD says "data mesh", he's done "lakehouse + governed domains")
- **Recency gap** — he's done it but not in the last N years
- **Coverage gap** — he's done some of it but not the full scope

Rec