---
name: job-fit-analyzer
description: Analyzes how well Matt Cornet fits a specific job posting before he invests time tailoring a resume or applying. Produces a fit score, gap analysis, ATS keyword check, and a go/no-go recommendation. Use this whenever Matt shares a posting and asks "should I apply", "is this a fit", "how do I match up", or pastes a JD without explicitly saying what he wants — the right default is to triage fit before tailoring. Also use when he asks to compare multiple postings.
---

# Job Fit Analyzer

## What this skill does

Triage a job posting against Matt's profile in 2 to 3 minutes of reading time. The output
answers: *should he apply, and if yes, with what angle?*

This skill is upstream of `resume-tailor`. Running it first prevents wasted effort tailoring
resumes for poor-fit roles.

## Source materials (read these every run)

> Paths marked *(vault)* are relative to the connected `obsidian-vault` folder. Paths marked
> *(project)* are relative to the **Job Applications project root**, the folder that contains
> the application folders and `_assets/`. Resolve those against whichever folder Matt has
> connected for the current session (typically the one named "Job Applications").

1. *(vault)* `Notes/Matt Cornet.md` **read this first**. Every fact about who Matt is comes
   from here: `## Background`, `## Strengths`, `## Education`, `## Current focus`,
   `## Target roles`, `## Framing guardrails`, `## Technology and scope ceilings`.
2. *(project)* `_assets/candidate_profile.md` canonical experience detail and the append-only
   tailoring Q&A log. Use it for evidence at the bullet level, not for identity.
3. *(project)* `_assets/master_resume.docx` what is actually documented today. The coverage
   matrix and the ATS check score against this, not against what Matt could plausibly say.

### The vault is a hard requirement

Run `ls $HOME/mnt/` and check for `obsidian-vault`. If it is not connected, ask Matt to
connect `C:\Users\mattc\Obsidian\obsidian-vault`, or call `device_request_folder_access` on it.
**Do not produce a fit analysis without it.** There is no fallback: this skill carries no
sectors, no seniority band, no capability list and no years-of-experience figure of its own,
so without the note it has nothing to score against.

`_assets/voice_matt.md` and the "Voice & style guidelines" section of `candidate_profile.md`
are stubs pointing to the vault. Never read them as rules, never write to them.

This skill does **not** need *(vault)* `Notes/Writing voice.md`. Nothing it produces is sent to
an employer, so no voice rule applies to its output.

### No identity in this file

If a step below needs a fact about Matt, it names the vault section to read it from. Nothing
about his sectors, levels, geographies, languages, years or strengths is written into this
skill. When the note changes, the scoring changes with it and this file stays untouched.

## Workflow

### Step 0 — Company overview (prerequisite)

This skill relies on the application's `company_overview.md`. **If
`applications/<company>-<role-slug>/company_overview.md` does not exist, run the
`company-overview` skill first** to research the company and create it. If it already exists,
read and reuse it, refreshing it via `company-overview` if it is clearly stale.

Carry its insights into every later step, especially domain fit, the narrative angle, and the
ATS keyword read.

### Step 1 — Extract from the posting

- Role title, level, function, comp band (if disclosed)
- Hard requirements: years experience, must-have skills, certifications, geo, work authorization
- Soft requirements
- Domain, at the granularity the posting uses (sub-sector, buy-side or sell-side, and so on)
- Top 15 to 20 ATS keywords, verbatim

Extract the posting's own vocabulary here. Do not translate it yet into Matt's terms: that
mapping is Step 2.5's job and it needs both sides stated separately.

### Step 2 — Score on five dimensions (0 to 10 each)

Read the vault section named in each row **on this run**. Score the posting against what the
note says today.

| Dimension | Vault section to read | What to look for |
|---|---|---|
| **Domain fit** | `## Background`, `## Target roles` | Does the posting's sector appear in the Background table, or in the Target roles priority list? Tier 1 and 2 target roles score higher than tier 3 and 4. |
| **Seniority fit** | `## Background` (Scope column), `## Target roles` | Compare the posting's level and team or budget scope against the scope actually held in the table. Score the risk of being over-levelled as hard as being under-levelled. |
| **Functional fit** | `## Strengths`, `## Background` (Role column) | Match the posting's function against the listed strengths. A strength that is listed but has no matching row in the Background table is weaker evidence than one with both. |
| **Skill match** | `## Technology and scope ceilings` | Hard requirements he has versus lacks. A requirement named in "Never claim at all" is a definitive lack, not an open question. |
| **Hidden fit** | `## Strengths`, `## Education`, `## Current focus` | Attributes the posting does not ask for that would still elevate a borderline application. Take them from these sections only, never from assumption. |

Sum to a 0 to 50 score. Map to recommendation:

- 40 to 50: Strong fit, apply with a tailored resume
- 30 to 39: Borderline, apply only if the role is unusually attractive or the angle is clear
- 20 to 29: Stretch, likely a no, but flag if there is a unique hook
- 0 to 19: Pass

**Override:** two or more hard requirements marked 🚫 in Step 2.5 make it a Pass whatever the
total. Say so explicitly rather than letting a high score on the other four dimensions carry a
posting Matt cannot honestly answer.

### Step 2.5 — Requirement-by-requirement coverage matrix

The five-dimension score is the headline. This step is the detail that makes it trustworthy and
feeds `resume-tailor`. **Enumerate every requirement the posting lists**, each hard requirement,
each nice-to-have, and every named tool, certification, regulation, sector and scope bar, as its
own row. For each, mark coverage:

| Coverage | Meaning |
|---|---|
| ✅ Strong | Clearly evidenced in `candidate_profile.md` or `master_resume.docx` with specifics |
| 🟡 Partial | Adjacent or implied, but not explicit or not at full scope |
| 🚫 Blocked | The vault forbids the claim: named under "Never claim at all", blocked by `## Framing guardrails`, or asked for beyond what "Claim only within these bounds" allows |
| ❌ Absent | Nothing on record, and no ceiling involved |
| ❓ Unknown | Plausibly in his background but not documented, and no ceiling involved: a likely *hidden match* |

Rules:

- One JD line, one row. Do not collapse multiple requirements into a single row.
- **Check `## Technology and scope ceilings` and `## Framing guardrails` before assigning any
  other mark.** A ceiling item is 🚫, never ❓. Marking a forbidden tool as a hidden match to
  mine sends `resume-tailor` to ask Matt a question the vault has already answered no to.
- A requirement blocked by a guardrail is 🚫, not a framing gap. Framing is what `resume-tailor`
  does with true material, and a guardrail says the material is not there.
- 🟡 covers the "Claim only within these bounds" case where the JD's ask sits *inside* the
  bound. It becomes 🚫 when the ask sits outside it. State which bound and why.
- Lean toward ❓ rather than ❌ only on rows no ceiling and no guardrail touches.
- Total the coverage, for example "6 Strong / 3 Partial / 2 Blocked / 1 Absent / 2 Unknown", and
  use it to sanity-check the five-dimension score.

**Hand-off:** flag every 🟡 and ❓ row as a question for `resume-tailor`'s mining step (Step 2b).
Never hand off a 🚫 row: it is settled. State explicitly that the fit score reflects only what is
documented today, and that resolving the 🟡 and ❓ rows through questioning could raise it.

### Step 3 — Gap and risk analysis

For each gap, classify as:

- **Ceiling gap** the vault forbids the claim. No mitigation exists. Say plainly that the
  requirement is not claimable and let the go/no-go absorb it. Never reclassify a ceiling gap as
  a framing gap to make a posting look more winnable.
- **Real gap** he does not have this and it cannot be papered over, for example a required
  number of years in a sector absent from `## Background`.
- **Framing gap** he has the underlying capability but the posting labels it differently. Give
  the posting's term and Matt's term side by side, both quoted, so `resume-tailor` can reuse the
  mapping.
- **Recency gap** he has done it, but the matching row in `## Background` is older than the
  posting implies. State the year.
- **Coverage gap** he has done part of it but not the full scope. Name the missing part.

Then rate the application's overall risk:

- **High** any hard requirement is a ceiling gap or a real gap
- **Medium** the gaps are framing, recency or coverage only
- **Low** gaps are confined to nice-to-haves

For every gap except ceiling gaps, propose one mitigation and say where it lands: a resume
bullet, the cover letter, or an interview answer.

### Step 4 — ATS keyword check

Table of the top 15 JD keywords from Step 1. For each: whether it appears in
`master_resume.docx` verbatim, paraphrased, or not at all, plus a claimability flag.

**A keyword is not weavable just because the ATS wants it.** Cross-check every absent keyword
against `## Technology and scope ceilings` and `## Framing guardrails` before flagging it for
`resume-tailor`:

| Flag | Meaning |
|---|---|
| ✅ Verbatim | Already in the master. Nothing to do. |
| ✏️ Paraphrased | Present in different words. Worth aligning to the JD's phrasing. |
| ➕ Weave in | Absent, true, and no ceiling or guardrail touches it. |
| 🚫 Do not weave | Absent and blocked. Name the ceiling or guardrail. |

The 🚫 keywords are the highest-value output of this step. They are precisely the words an ATS
optimizer would insert, and inserting them would put a false claim on the resume. Hand them to
`resume-tailor` as prohibitions, not as gaps.

### Step 5 — Output

Report the fit analysis **in chat**. The fit report itself stays in chat: no file is written for
it. Make sure the `company_overview.md` from Step 0 has been saved to the application folder and
link it for Matt. Structure:

```
## Fit summary
**Recommendation:** [Apply / Borderline / Pass]
**Score:** XX/50   **Risk:** [High / Medium / Low]
**One-line angle:** [the narrative thread to lead with if applying]
[if the Step 2 override fired, say so here and why]

## Score breakdown
[5 dimensions, score, 1-line justification each, naming the vault section used]

## Requirement coverage
[one row per JD requirement: requirement | ✅/🟡/🚫/❌/❓ | evidence, or the ceiling that blocks it]
[totals line, e.g. "6 Strong / 3 Partial / 2 Blocked / 1 Absent / 2 Unknown"]
[note: which 🟡/❓ rows resume-tailor should mine, and that the score could rise if they resolve]

## Not claimable
[the 🚫 rows, each with the ceiling or guardrail behind it, and what the posting asked for]
[omit this section only if there are none]

## Strengths to emphasize
[3-5 bullets, from `## Strengths` and the matching rows of `## Background`]

## Gaps and how to handle
[table or short list, gap class + mitigation, "none" for ceiling gaps]

## ATS keywords
[top 15 keywords, presence flag, claimability flag]

## Recommended next step
[either "run resume-tailor with angle X", or "skip this one because Y"]
```

## Comparing several postings

Run Steps 1 to 4 for each, then give one table: posting, score, risk rating, blocked hard
requirements, verdict. Rank by score, but lead the commentary with the risk rating, since a 38
with no ceiling gaps beats a 43 with two.

## Hard rules

- **Be honest about gaps.** A score of 25/50 is reported as 25/50. Matt's time is better spent
  on better fits.
- **Don't pad domain fit.** An adjacent sector is not one of the sectors in `## Background` or
  `## Target roles`. Name the difference instead of blurring it.
- **Comp transparency:** if the JD discloses a band below the level of his most recent role in
  `## Background`, flag it.
- **Never soften a 🚫** because the posting is attractive.
- **Re-read `Notes/Matt Cornet.md` every run.** Do not score from memory of a previous run.
- **Report vault silence as silence.** If the note says nothing about a sector, a level or a
  language the posting asks for, say so and offer to add it, rather than inferring it from the
  resume.
- **Do not quantify the AI side of the profile.** `## Technology and scope ceilings` records that
  decision and the reason for it.
