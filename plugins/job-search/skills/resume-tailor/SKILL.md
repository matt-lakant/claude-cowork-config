---
name: resume-tailor
description: "Tailors Matt Cornet's master resume to a specific job posting, optimizing for ATS keywords and recruiter signal while preserving truthfulness. Use this skill whenever Matt mentions tailoring, customizing, or rewriting his resume for a posting, applying to a role, or asks to \"make my resume match this job\" — even if he doesn't say the word \"tailor\". Also use when he pastes a job description and his master resume in the same turn."
---

# Resume Tailor

## Before anything else — open the opportunity

**Run the `opportunity-intake` skill first.** It confirms the opportunity name, resolves
the kebab-case slug, creates `applications/<slug>/` if it does not already exist, and
starts the opportunity's `notes.md`. Every file this skill produces goes inside that
folder.

Do not write anything before the folder exists. If the slug is unknown, ask. If the
Job Applications project folder is not connected, stop and say so — never fall back to
the project root, to another connected folder, or to chat-only delivery.

## What this skill does

Produces a tailored version of Matt's master resume for a specific job posting. The output preserves all factual content from the master but reorders, rewrites, and reweights bullets so the most relevant experience leads, ATS keywords from the posting are surfaced naturally, and the profile paragraph speaks to the role.

## Inputs Matt will give you

- **Required:** the job posting (URL, pasted text, or PDF). Whatever the form, it is turned into `job_description.md` first (Step 0b). For a URL other than LinkedIn or Collective.work that you can't fetch verbatim, ask him to paste the text.
- **Optional:** company notes, hiring manager name, application deadline.

## Source materials (read these every run)

> Paths marked *(project)* are relative to the **Job Applications project root** — the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications"). Paths marked *(vault)* are relative to the connected `obsidian-vault` folder.

> **Voice reference moved, 2026-09-10.** How Matt writes now lives in *(vault)* `Notes/Writing voice.md`, not in this project. §2 is the corpus of his own sentences, §3 the banned-construction table, §4 the review test, §5 the per-surface rules (5.1 candidature prose, 5.2 resume, 5.3 LinkedIn post). Load it through `general:writing-voice` in vault-required mode: it requests `C:\Users\mattc\Obsidian\obsidian-vault` itself if the folder is not connected, reads the note in full, and flags drift with the voice block in Matt's preferences. No fallback: if the note cannot be read, do not draft any prose. `_assets/voice_matt.md` and the "Voice & style guidelines" section of `candidate_profile.md` are stubs pointing there — never read them as rules, never write to them.

> **CV-only runs read the rules, not the corpus (2026-11-16).** When this run produces a CV and no prose piece (no form answer, no message), load the note in the **CV mode** of `general:writing-voice`: §1, §3, §4 with 4.1, and §5.2. The corpus in §2 is sentences from letters and messages, and a CV is bullets governed by §3 and §5.2. As soon as a form field or any other prose is drafted in the run, read the note in full first.

1. *(vault)* `Notes/Writing voice.md` — the voice reference. Governs **every line of prose** (profile paragraph, form answers) via §5.1, and **every resume bullet** via §5.2.
2. *(vault)* `Notes/Matt Cornet.md` — durable identity and the "Technology and scope ceilings" list. Read the ceilings before writing any claim about a tool, a certification, a sector or a scope.
3. *(project)* `_assets/candidate_profile.md` — canonical experience, target roles, accuracy guardrails, and the append-only tailoring Q&A log. **Read this first.**
4. *(project)* `_assets/master_resume.docx` — the formatted master (A4 since 2026-11-16). It is the template of last resort: Step 3a picks the base file, which is usually a CV Matt has already finalized for a similar role.
5. *(project)* `_assets/cv_rules.md` — Matt's standing CV rules in one place (title wording for non-sales roles, wording for non-finance employers, number of client engagements, header, mandatory wordings). **Read Part 1 before drafting.** The rules used to live in session memory, the voice note and the Q&A log, and a run that missed one source missed the rule: on 2026-11-16 a draft went out with finance wording and a four-line header because both rules were only in memory.
6. *(project)* the **"Current values" table at the top of `_assets/candidate_profile.md`** — the current wording of every figure that goes on a CV. The log under it is append-only and too long to read in full (900+ lines), so a later entry can annul an earlier one without anyone noticing. On 2026-11-16 a CV printed "EBITDA margin 27% to 32% over 3 years", a duration Matt had replaced by "24 to 30 months" six days earlier; the stale wording came in through the previous CV used as the base file.

## Workflow

### Step 0 — Company overview (prerequisite)

This skill relies on the application's `company_overview.md`. **If `applications/<company>-<role-slug>/company_overview.md` does not exist, run the `company-overview` skill first** to research the company and create it. If it already exists (e.g. from a prior `job-fit-analyzer` run), read and reuse it. Carry its insights into the profile paragraph, the narrative angle, the ATS keyword choices, and the cover-letter angle recorded in the memo (Step 5).

### Step 0b — Get the posting into `job_description.md`

If `applications/<slug>/job_description.md` does not exist, run Step 3b of `opportunity-intake` now. For a LinkedIn or Collective.work link with no posting PDF, that generates `<Company>_JobPost_<Role>.pdf` from the web page with Claude in Chrome and extracts the `.md` from it (for Collective, the form questions are included, since the page only shows them behind *Postuler*); for a PDF Matt supplied, it extracts the `.md` from that PDF; pasted text goes straight to the `.md`. **Every step below reads `job_description.md`**, not the PDF and not a browser read.

The posting PDF is the employer's text, not Matt's document: the "never produce a PDF" rule in Step 4 is about the resume and the letter and does not block it.

### Step 1 — Parse the posting
Extract:
- Role title, level, function
- **Role tag, `hands_on` or `leadership` (decide it here, it drives the framing of the whole CV).** The question is whether the role requires doing the work oneself, not the title and not the contract type. `hands_on`: the person in the role produces the work (builds, writes, configures, delivers, runs the projects), alone or with a small team. That is the case of individual-contributor and manager postings, and of **most freelance missions**, which are individual-contributor roles. `leadership`: the role is held through other people and the posting does not ask for the work to be done personally (director, head-of, VP, C-level, and the freelance missions that are leadership mandates, such as running a department or a programme through its managers). A title can mislead in both directions: a "Head of" with a team of 4, or a "player-coach", is `hands_on`; a freelance "programme director" steering several project managers is `leadership`. When the posting asks for both, tag it `hands_on`: showing that he can do the work never hurts a leadership reader, and the reverse does. Say in the memo which words of the posting decided it. If `fit_report.md` gives the tag, use the same one.
- Hard requirements (must-have skills, certifications, years of experience)
- Soft requirements (nice-to-haves)
- Top 15–25 ATS keywords (skills, tools, methodologies, domain terms — verbatim phrasing)
- **Top-third keywords (3 to 6):** the words of the job title that qualify the role (a region such as "EMEA", a function such as "Professional Services") and the posting's core nouns (what the employer sells or what the role runs, e.g. "master data"). Keep only words Matt can claim; a word blocked by a ceiling is never in this list. They must appear above the skills matrix, and Step 4a tests it. On 2026-11-16 two drafts for an "EMEA" role at a master-data vendor went to the red-team without "EMEA", and one without "master data".
- Hiring signal: what would make a candidate stand out (impact metrics, scale, geos, regulatory, AI/ML, etc.)
- Tone of the JD (corporate, startup, consulting) — match it in the cover sections
- **Every question the application asks, verbatim.** Form fields ("why do you want to join us?") are deliverables in their own right, governed by Step 4b.

Parse from `job_description.md` (Step 0b).

**LinkedIn (`linkedin.com/jobs/view/<id>/`) and Collective.work (`collective.work/jobs/<lang>/<slug>`) postings:** never server-fetch them (LinkedIn returns nothing, Collective returns a summary). Step 0b captures them from the web page.

**Re-posted roles.** Before tailoring, check `applications_tracker.md` and the `applications/` folders for a prior application to the same company under a similar title. Companies re-post unfilled roles under a new name, often with a harder required profile. If you find one, diff the two postings and lead the diagnostic with what changed in the *required profile*, not in the missions — that delta is the whole tailoring brief. Treat the earlier application as a fact to handle (it is sitting in their ATS), not as something to quietly repeat.

**Two postings are not proof of one re-post.** Identical missions are suggestive, not conclusive. The decisive check is whether the older posting is still live: two live postings mean two roles. State the inference as an inference in `job_description.md` and name the check; on 2026-09-04 a re-post was assumed and written up as fact, and five days later the new posting vanished while the old one stayed up — the opposite conclusion. A hypothesis written as a finding is a hypothesis nobody will question at interview time.

### Step 2 — Score Matt against the posting (briefly, in chat)

Before generating, give Matt a **1-paragraph diagnostic** in chat:
- Strong-fit dimensions (3–5 bullets)
- Gap dimensions where the resume needs to lean harder or where a skill is genuinely missing (2–3 bullets)
- Top 10 ATS keywords from the JD that should appear in the tailored resume
- Recommended angle / narrative thread for this application

This lets Matt sanity-check before you spend tokens generating the .docx. Pause for confirmation only if the angle is non-obvious or the gap is significant; otherwise proceed.

### Step 2a — Evidence sheet and lessons (before any question, before any drafting)

**Why this step exists.** Across 20 applications up to 2026-11-16 the red-team made a median of 36 tracked changes per CV and rewrote about 20% of its words. The largest single cause was not style: it was facts already in Matt's log that the draft had not used, found afterwards by a reviewer who searched the log requirement by requirement. This step is that search, done first. A red-team that still has to add facts from the record means this step was skipped or done thinly.

1. **Search the record for every requirement.** Take the requirement list (from `fit_report.md` if it exists, else from Step 1). For each hard requirement and each nice-to-have, run:

   ```text
   python3 <skill dir>/scripts/profile_search.py <project>/_assets/candidate_profile.md "<term>;<term>;..."
   ```

   Give 3 to 6 terms per requirement: the posting's word, **its French equivalent (most of the log is in French)** and the words Matt would use (for "SOW": `SOW;statement of work;chiffrage;estimation d'effort`). One search per requirement, not one for the whole posting. Read the entries it returns, newest first, and check the Current values table for any figure.
2. **Write the evidence sheet** in `tailoring_notes.md`, one row per requirement:

   | Requirement | Strongest facts on record (entry date, line) | Where it goes in the CV | Open question |
   |---|---|---|---|

   Up to three facts per row, the most specific first: a number, a named client, something he did himself. Mark `first-hand` any fact that is work he did personally; a `hands_on` role needs two of them above the skills matrix (R19).
3. **Use it.** Every hard requirement with a fact on record gets that fact in the CV, in the top three bullets of its role or above the matrix. A row with no fact becomes a question for Step 2b, or a stated gap if a ceiling blocks it. Fill the third column when the draft is written; Step 4a checks that no hard requirement has a fact on record and an empty third column.
4. **Read the lessons.** Read *(project)* `_assets/redteam_lessons.md`: one line per past red-team finding, with its cause and the role family. Apply the lines that match this role family, and list in the memo which ones you applied. The red-team reads what Matt rejected so as not to repeat it; this is the same loop in the other direction.

### Step 2b — Mine every requirement (ask Matt before generating)

Matt has 20+ years of broad experience; the master resume captures only the headline version. The goal of this step is that **no requirement is left weakly evidenced when he actually has the experience to back it** — for the resume *and* the cover letter. So work requirement-by-requirement, not by a fixed quota of questions.

1. **Build the requirement checklist.** List every requirement the posting states — each hard requirement, each soft / "nice-to-have", and every named tool, platform, method, certification, regulation, sector, and scope/scale bar. If `job-fit-analyzer` already ran, read `applications/<slug>/fit_report.md` and start from its Requirement coverage matrix and its "Not claimable" list.
2. **Classify each against the vault ceilings + `_assets/candidate_profile.md` + `master_resume.docx`:**
   - **Blocked** — the "Technology and scope ceilings" section of *(vault)* `Notes/Matt Cornet.md` says it cannot be claimed. Do not question, do not soften; it is a stated gap.
   - **Strong** — already clearly evidenced with specifics. No question needed.
   - **Partial / Absent / Unknown** — adjacent, missing, or plausibly-in-his-background-but-undocumented. **Each of these gets a question.**
3. **Ask the reviewer's questions now, not after the draft.** Before questioning Matt, write down the attacks a skeptical reviewer will make on this application, then check each against the evidence sheet and the Current values table. The ones the record does not answer are questions for this round. The recurring ones:
   - **The number behind each KPI the posting names** (utilization, margin, forecast, time to value, NPS, on-time rate...): the figure, what it was measured on, the period. If the record has only an estimate, ask whether it can be printed and how he would defend it.
   - **First-hand proof** for the two or three central requirements: what he did himself, as opposed to what his organization delivered.
   - **A recovery or a failure**, when the posting talks about escalations, projects off track or turnarounds: which one, what he did, how it ended.
   - **The split that matches the posting**: how much of his scope was in the posting's region, sector, team profile or type of client.
   - **Third parties**, when the posting names partners, subcontractors or vendors: who, how many, what he controlled.
   - **Level**, only when the role tag is unclear from the posting.

   On 2026-11-16 a run asked 4 questions before drafting and 4 more after the reviewer's attack; the second 4 (the utilization figure, who wrote the SQL controls, what was done with partners, time to value) were all predictable from the posting, and their answers went in as redline. A question the red-team has to ask that could have been asked here is counted as a late question (cause B) in its memo.
3b. **Question Matt on every Partial / Absent / Unknown requirement** using the `AskUserQuestion` tool. The tool allows max 4 questions per call, so **batch them into successive rounds of up to 4 and keep going until every such requirement has been put to him** — do not stop at an arbitrary 3–5. Make each option concrete and grounded in something plausibly in his background so he can confirm in one click; use multi-select where natural; always leave room for him to add detail. For each requirement, probe what he actually did and at what scope:
   - **Named tools/platforms** (e.g. Jira / JSM, CI-CD, specific clouds, AI labs/hyperscalers, ITSM/SDLC tooling) — what did he build or run, and at what scope?
   - **Sector / domain** framing, and any non-finance work to surface.
   - **Scope & scale** (team size, budget, P&L, regions, client tier) where the JD implies a bar. When the JD's scale is *smaller* than Matt's headline numbers, ask for the intermediate figure — direct reports, missions run in parallel, typical engagement length — because the headline alone reads as overqualification and invites "why would you come here, and for how long?".
   - **Regulations, risk controls, and operating models** the JD names — which has he dealt with hands-on?
   - **Adjacent / non-obvious work** the headline resume omits.
4. **Asking a lot is expected.** A senior role with 10+ requirements may warrant 2–3 rounds of questions. One extra question costs far less than shipping a resume or cover letter that under-sells real experience. The only requirements you skip are those already rated **Strong** or **Blocked**.
5. **Record every confirmed answer in `candidate_profile.md`** (standing rule, 2026-06-25): append each answer (dated) to the `## Confirmed details from tailoring Q&A (append-only log)` section, and promote durable items into the relevant Experience bullets / master via `asset-updater`. A confirmed answer that raises or lowers a ceiling belongs in *(vault)* `Notes/Matt Cornet.md` too — hand that to `asset-updater`. Then **fold them into the rewrite as real, specific bullets.** Because they are logged, `cover-letter` reuses the same confirmed specifics later. Never invent — surface only what Matt confirms. If he confirms nothing for a requirement, keep it as a stated gap in the memo.

This step is **mandatory on every run** (not just for out-of-track or tool-heavy roles). It can be abbreviated only for a near-identical re-tailor of a role he has already been fully mined on — and even then, re-ask any requirement the prior run left Partial / Absent. (Implements the `feedback_tailoring_alignment_questions` practice.)

### Step 2c — Record the decisions before writing

Matt's answers in Step 2b include decisions about the CV itself, not only facts: how to handle the level, what to lead with, what to leave out, which title wording. Facts go to the log; **decisions go into a table in `tailoring_notes.md`, written now, before any drafting:**

| Decision | Source | Where it must show |
|---|---|---|
| e.g. open on the direct team of 5 to 10, keep 80+ and the P&L lower | Matt, Step 2b, question 4 | profile sentence 2; first bullet of FactSet 2019-2024 |

Add the rules of `cv_rules.md` that the tags trigger for this posting (for example R3 and R5), one row each. The third column is filled before drafting, with the place where a reader will see the decision.

Why a table: on 2026-11-16 Matt answered "lead with the direct team", and the draft still opened on "through regional directors", 80+ people and ~USD 40M. The answer had been logged as a fact and nothing carried it into the draft. The red-team caught it as its first High finding.

### Step 3 — Rewrite with these rules

**Level framing comes first (rules R18 to R20 of `cv_rules.md`, Matt, 2026-11-16).** What Matt cares about most is the seniority the CV conveys, and that it shows his capacity to do the work himself wherever the role calls for it. On such a posting he must not look too senior for the job or disconnected from the work, and both independent reviewers of 2026-11-16 rejected drafts for exactly that: "reads as a Global Director who delegates". Length matters far less.

*Role that requires doing the work oneself (`hands_on`), whatever the title and whether it is a permanent job or a freelance mission:*
- **Scale markers stay out of the top third**: no headcount of 80+ or 110, no ~USD 40M P&L, no board, C-level or SVP, no "through regional directors" in the header, the profile or the areas of expertise. The reader of a manager role stops reading there, and those words answer a question nobody asked while raising two: why this job, and for how long.
- **The first bullet of each role says what he did himself or with his direct team** (5 to 10 managers and experts). Scale goes once into the Context line of the role, where a reader who wants it finds it.
- **At least two first-hand facts above the skills matrix** (R19): work he did himself, from the record. Examples on file: SQL control scripts he wrote on data migrations (both FactSet periods), effort estimates and SOWs he wrote, the Standard Chartered deployment he put back on plan as last point of escalation, lakant.io built end to end, the Power BI model and reports he built. Write the fact; never the adjective "hands-on".
- **Verbs of distance are replaced by what happened**: "oversaw", "sponsored", "governed", "ran through" become what he did (wrote, reviewed, staffed, decided, recovered), when the record supports it. When it does not, the line moves down, it is not rewritten into a claim.
- **Titles are facts.** "Global Director" stays in the role titles. Nothing is renamed, no scope is denied: the scale is placed lower, not hidden. If asked, Matt owns it.

*Leadership role (`leadership`), permanent or freelance:* the capacity to do the work oneself is not what is being bought. Scale and seniority lead and are not deflated (R20). Keep one or two first-hand facts in the experience bullets all the same: they cost nothing and answer the "too far from the ground" doubt.

**The contract type never decides the framing.** An earlier rule (September 2026) said seniority is never deflated on a freelance mission. Matt corrected it on 2026-11-16: most freelance missions are individual-contributor roles, so they follow the `hands_on` rules; only leadership mandates keep seniority up front.

Record the level and these choices as the first rows of the decisions table (Step 2c), whether or not Matt was asked: they are standing decisions, not a question to put to him again.

**Profile paragraph (3–4 sentences, impersonal voice — NEVER third person):**
- Follow §5.2 and the banned-construction table in §3 of *(vault)* `Notes/Writing voice.md`: impersonal/participial constructions ("Professional-services and product leader with 20+ years…", "Specialist in…"); use "I" only if a pronoun is unavoidable; never "Matt specializes…"
- Lead with the role's central challenge translated into Matt's idiom
- Name 2–3 of his most relevant past contexts (e.g., "post-merger integration at BlueMatrix", "Global Director at FactSet")
- Close with a hook tying his unique combo (fintech + AI + international P&L) to the role
- No self-awarded adjectives ("demanding and supportive manager", "culture of excellence") and no repeat of the degrees already listed under Education. Both spend the most expensive lines on the page for zero signal.

**Areas of expertise (6 bullets):**
- Reorder/reword the master's 6 expertise lines so the top 3 hit the JD's must-haves
- Use JD verbiage where natural; never invent expertise he doesn't have
- Cut a line rather than keep one the skills matrix and the experience bullets already make. Stating the same claim in the profile, the expertise list and the matrix is not emphasis; it is paying three times for one point.

**Experience bullets:**
- Each role keeps ≥2 bullets; the most relevant role gets up to 8
- Lead bullets with action verbs from the JD when accurate ("Spearheaded", "Drove", "Reorganized", "Designed", "Architected")
- Embed JD keywords inside real achievements, not as a stuffed keyword list
- Quantify wherever the master has a number — never invent metrics
- **Write every figure as the Current values table words it** (duration, reference date and unit included). For a figure with no row in the table, grep the log for it, take the latest dated entry, and report the figure to `asset-updater` so the row gets added. This applies to figures inherited from the base file too: a previous tailored CV is not evidence that a figure is still current.
- Drop bullets that are irrelevant to this role. Length is reported by Step 4a for information (R17: about 1,100 words for `hands_on` postings, 1,400 for `leadership` ones); it is not a target to hit at the cost of a relevant line
- Put the bullet answering the JD's entry criterion in the top three of its role. A line sitting seventh on page two does not exist during a six-second screen.

**Employer outside financial services: speak its domain (rule from Matt, 2026-10-08):**
When the employer is not a financial-services firm, rewrite the finance-specific wording of the whole CV, not just new lines, **by default and without being asked**. Do it in the first draft, not after Matt flags it.
- Describe what the work was in terms the employer's own products use. Read `company_overview.md` and the posting for their vocabulary first. FactSet's research production suite was software to **author, review (compliance), publish and distribute documents**; say that in the employer's words: "collaborative authoring, review and publishing" and "templates, workflows, views" for a workspace tool like Notion, "expert content" and "professional workflow software" for an information-services publisher like Wolters Kluwer, "financial data and reporting" for corporate-finance software like OneStream, "production et publication de contenus" for a generalist group.
- Typical swaps: "research production suite/software" to the domain phrase above; "AI-powered research authoring" to "AI-assisted report drafting" or "authoring of expert content"; "institutional accounts" to "enterprise accounts"; "index data platform for financial institutions" to "data platform"; "research databases for the investment teams" to "custom databases / internal knowledge bases for the client's teams"; "external managers" (APG) to "third parties"; Goldman "research teams/tools" to "teams" and "internal tools and databases".
- Keep: job titles, the department name (Research Management Solutions), client names, and **one** sector mention in the FactSet context line ("enterprise clients worldwide, mostly in financial services"), so the CV never reads as hiding the background.
- When the employer sells to finance functions (CPM, accounting software), finance words that echo its product ("CFO", "financial data and reporting") stay; sell-side jargon ("research", "brokers", "sovereign funds") goes.

**Professional Services, delivery and customer-engineering roles: client engagements (rule from Matt, 2026-10-07):**
List **3 client engagements under FactSet 2019-2024** and **2 under FactSet 2007-2018**, each showing what the role does (integration, migration, custom work, go-live time, users), with figures from `candidate_profile.md`. If the profile lacks the figures, ask for them in Step 2b.

**Skills matrix:**
- Reorder so the top row hits JD must-haves; cells unchanged in content
- If the JD names a tool/method that Matt has used (per `candidate_profile.md` and the vault ceilings) but isn't in the matrix, add it; if he hasn't used it, or a ceiling blocks it, do not add it

**Education and footer:** unchanged.

### Step 3a — Choose and audit the base file

The base file is the `.docx` you edit in place. Choose it deliberately and say which one in the memo.

1. **Candidates:** CVs Matt finalized and sent (the tracker and each folder's `redteam_notes.md` name the file that went out), in the posting's language, for the nearest role family (professional services, programme or transformation, customer success, product, AI adoption). Take the most recent one that fits. A draft or a redline Matt never returned is not a candidate.
2. **Fallback:** `_assets/master_resume.docx` when no finalized CV is close.
3. **Audit it before editing.** A finalized CV carries Matt's layout and phrasing, which is why it is a better start than the master. It also carries whatever was true on the day it was sent. Run `cv_check.py` on the base file with this posting's tags and `--profile`: each `FAIL` is a line to rewrite, not a line to keep (a superseded figure, a title or wording rule that did not apply to the earlier posting).
4. **Set the page to A4** if the base predates 2026-11-16: `python3 <skill dir>/scripts/to_a4.py <base.docx> <working copy.docx>`. It keeps the text width, so no line moves.
5. **The base is not evidence.** A sentence written for another employer (its keywords, its sector wording, its level framing) is rewritten or dropped. A figure is printed because the Current values table or the log supports it, never because the base file had it.

### Step 4 — Generate the .docx

Edit the base file chosen in Step 3a (`_assets/master_resume.docx` when no finalized CV fits). Open it with `python-docx`, replace text in place where possible to preserve styles, fonts, and table layout. Don't rebuild from scratch — that loses the template's polish.

Save to: `applications/<company>-<role-slug>/CORNET_<Company>_<Role>_<YYYY-MM-DD>.docx`

**Never produce a PDF.** Matt makes his own PDF from Word, after he has validated and reformatted the `.docx`. Do not save a `.pdf` beside the `.docx`, do not attach one, and do not offer one. If you need a PDF to check pagination, convert into a temp directory **outside** the project folder (e.g. `$HOME/tmp`), read the page count there, and leave nothing behind. A `.pdf` in an application folder is a stale copy of a document that is about to change, and on Matt's machine a session cannot delete files, so it becomes his cleanup.

Where:
- All CV/cover-letter filenames start with the `CORNET_` prefix (see `feedback_filename_convention`). If a same-dated file already exists and is locked (OneDrive placeholder) or you've materially revised it, save a `_v2` / `_v3` copy rather than overwriting — the per-application folder doubles as version history.
- `<role-slug>` is a kebab-cased short version of the role title (e.g., `head-of-product`).
- `<YYYY-MM-DD>` is **the date the file is being generated today** — i.e. today's date in the user's timezone, not the JD posting date, the application deadline, or any date pulled from the posting itself. Run `date +%Y-%m-%d` (or check `currentDate` in env) at generation time. If the resume is regenerated later (e.g., after Matt's manual edits or a JD update), save under a new file with the new date and leave the older one in place — the per-application folder doubles as a version history.

### Step 4a — Mechanical check (mandatory, before the memo and the red-team)

Run `scripts/cv_check.py` (in this skill's directory; standard library only) on the `.docx` just generated. It reads the file with tracked changes accepted, applies the machine-readable checks of `_assets/cv_rules.md` Part 2, and fails on any string listed under "Never print" in the Current values table.

```text
python3 <skill dir>/scripts/cv_check.py <cv.docx> --rules <project>/_assets/cv_rules.md \
        --profile <project>/_assets/candidate_profile.md --tags <tags> \
        --top-keywords "<keyword 1>;<keyword 2>;..."
```

- **`--top-keywords`** takes the top-third keywords from Step 1. A missing keyword is a `FAIL`: put it in the header, the profile or an expertise line as part of a true statement, never as a bare list.
- **Then check the evidence sheet from Step 2a by hand.** Every hard requirement that has a fact on record shows that fact in the CV: fill the "Where it goes" column with the line. An empty cell next to a fact on record is the most common reason for a heavy redline; fix it now.
- **Then check the decisions table from Step 2c by hand.** For each row, quote in the memo the CV line that applies it. A row with no line to quote means the decision was not applied: fix the CV before the red-team, not after.

- **Role tag:** always pass `hands_on` or `leadership` (Step 1). With `hands_on` the script fails a scale marker above the skills matrix (R18), warns on one in the first bullet of a role, and requires two first-hand facts above the matrix (R19). Without a role tag none of this is checked, and the script says so.
- **`--hands-on "<fragment 1>;<fragment 2>"`** names the first-hand facts of R19 by a few verbatim words each (for example `SQL control scripts;SOWs written`). Each must be found above the matrix. The script cannot tell a first-hand fact from another line: choosing honest fragments is your job, and the red-team checks them against the record.
- **Tags** describe the posting, and you decide them: `non_sales` when the role is not a sales role (most postings), `non_finance` when the employer is outside financial services, `ps_role` for Professional Services, implementation or delivery roles. Say in the memo which tags you passed.
- **Where to run it.** The script ships with the plugin, so it is in the cloud workspace. Stage the `.docx`, `cv_rules.md` and `candidate_profile.md` with `device_stage_files` and run it there; if the plugin folder is also reachable from `device_bash`, running it there is fine too. Nothing is installed anywhere.
- **`FAIL`** blocks delivery: fix the CV and run again until the result line reads `0 FAIL`.
- **`WARN`** is a judgment call (a finance term that is a client's own name, a header line near the limit). Keep it only with a reason, and list each kept warning with that reason under "Open questions" in the memo.
- The script checks what can be tested mechanically. It does not replace reading Part 1 of `cv_rules.md`: rules such as "no sales mandate" or "wording that echoes the employer's products" still need your reading of the whole CV.

### Step 4b — The prose pieces: facts travel, sentences do not

**The cover letter is no longer drafted here (changed 2026-09-24).** It is written by the `cover-letter` skill once the CV is final: Matt downloads the red-teamed `.docx`, finalizes it in Word, and attaches it back to the chat, which starts `cover-letter`. Drafting the letter in the same pass as the CV produced CV-style prose, and nothing independent reviewed it. This step now covers the form fields only.

Write every prose piece in Matt's voice per *(vault)* `Notes/Writing voice.md` as loaded by `general:writing-voice`, §5.1 for the surface rules, and run its Step 4 review test before delivery. Then give each piece its own job and let it draw from the shared stock of evidence whatever serves that job. **The same fact may appear in two pieces**, provided each does something different with it. What must never repeat is a sentence or a framing.

| Piece | Its job | What it takes |
|---|---|---|
| **CV** | Inventory the facts, scannable | Everything, no prose |
| **Form field** | **Answer the question it asks**, and nothing else | Whatever answers that question, from the CV |
| *Cover letter* | *Written later by `cover-letter`, from the final CV* | *n/a here* |

**The form field is not held to novelty.** It answers a specific question, and to do so it reuses the key elements of the CV that answer it. Its constraint is the question, not freshness. Read the question literally and answer that; never drop a generic pitch beside it.

**Order of drafting:** CV first (it fixes the stock of facts), then the form fields, which pick whatever best answers their question.

**Before delivering, read the pieces back to back looking for twin sentences, not for shared facts.** Rewrite any repeated phrasing or framing outright. Then run the §4 review test over all of them, including point 8 (the AI-tell list in §4.1) and, for any "why us" field, point 9 (the swap test).

Note in the file which anchoring sentence to restore if a piece is later sent on its own. Deliver short texts to the outputs panel with `SendUserFile` so Matt can open and copy them, and keep a copy in the application folder.

### Step 5 — Write a tailoring memo

Save alongside the resume: `applications/<company>-<role-slug>/tailoring_notes.md`

Contents:
- JD summary (3 sentences)
- Top 10 ATS keywords used + where they appear in the resume
- Trade-offs made (what was de-emphasized, what got cut)
- The exact question each form field asked, and which facts were used to answer it
- Evidence sheet (Step 2a), with the "Where it goes in the CV" column filled, and the lessons applied from `redteam_lessons.md`
- Reviewer's questions anticipated (Step 2b), each with its answer or the round in which it was asked
- Base file used (Step 3a) and what its audit flagged
- Decisions table (Step 2c), each row with the CV line that applies it
- Top-third keywords and the tags passed to `cv_check.py`
- Open questions / things to verify before submitting
- Recommended cover letter angle (2 sentences): the 2–3 CV facts that best answer this JD and the "why this company" fact from `company_overview.md`. `cover-letter` reads this as a starting point, not a script.

This memo is for Matt to skim before submitting and is invaluable when he prepares for the interview weeks later.

### Step 6 — Update the tracker

Update `applications_tracker.md` at the project root (the tracker is now markdown, not the legacy `.xlsx`) — add a row via the `application-tracker` skill. Include: company, role, date applied (or "drafted"), source URL, status = "drafted", notes pointer.

### Step 7 — Adversarial red-team (mandatory gate, before presenting)

**Do not hand the resume to Matt until it has survived an adversarial review.** Run the `resume-redteam` skill on the tailored `.docx` as the final gate. It re-reads the JD, `company_overview.md`, and `candidate_profile.md`, attacks the resume in a fresh-context subagent (what's weakest, vaguest, removable, missing, over-claimed), redlines it with tracked changes authored "Recruiter", and asks Matt questions where a fix needs a fact not yet on record. Fold its confirmed answers back into the resume and `candidate_profile.md` before presenting. This gate is the reason tailoring isn't "done" at Step 6 — a self-written resume hasn't been stress-tested until something independent has tried to break it.

**When the red-team finds a factual error rather than a weakness** — a certification he does not hold, a stale claim, a guardrail decided but never applied — fix it at the source in the same run: *(project)* `_assets/candidate_profile.md`, *(project)* `_assets/master_resume.docx`, and *(vault)* `Notes/Matt Cornet.md` if it is a ceiling, not just the CV in hand. A guardrail written only into the Q&A log does not propagate itself, and the error comes back on the next tailoring run.

### Step 8 — Learn from the file Matt sends back

Matt finalizes the red-teamed `.docx` in Word and attaches it back to the chat. **When he does, run `asset-updater` in returned-file mode** before anything else. It saves his file in the application folder, diffs it against both Claude versions (the tailored draft and the redline with every Recruiter change accepted), sends every sentence he wrote or rewrote verbatim to §2 of *(vault)* `Notes/Writing voice.md` in the same turn, logs the Recruiter edits he rejected in `redteam_notes.md`, and routes factual changes to `candidate_profile.md` and `Notes/Matt Cornet.md`. A sample needs no threshold to be worth keeping; a banned-construction rule waits for the pattern to repeat twice. If the vault is not connected, say so and hand Matt the sentence rather than writing it into `_assets/`.

If he attached the CV to get a cover letter, continue with `cover-letter` in the same turn.

## Output: present to Matt

Give him links to the red-teamed `.docx` (with the recruiter's tracked changes), the tailoring memo, the `redteam_notes.md` critique, and the `company_overview.md` company brief (from Step 0), plus a 3-line summary of the angle taken and the biggest weakness the red-team flagged. Don't paste the resume text into chat — the .docx is the deliverable. Short prose pieces go to the outputs panel, not into the conversation. End with the next step in one line: finalize the redline in Word and attach it back here; that starts `cover-letter` and feeds his edits into the voice note.

## Hard rules

- **No opportunity-scoped file is ever written to the project root.** Everything for an
  opportunity lives in `applications/<slug>/`. Only `applications_tracker.md`, `README.md`,
  `_assets/` and `_research/` belong at the root. The standing "project folders are kept
  flat, no subfolders" preference does **not** apply to Job Applications — see the
  `opportunity-intake` skill, which wins on any conflict.
- **Never invent experience, metrics, employers, dates, or certifications.** If the JD asks for something Matt doesn't have, surface it as a gap in the diagnostic — do not paper over it.
- **Standing rules come from `_assets/cv_rules.md`, figures from the Current values table.** Neither is recalled from memory or copied from a previous CV. `cv_check.py` must end on `0 FAIL` before the file goes to the red-team.
- **Respect the vault ceilings.** The "Technology and scope ceilings" section of `Notes/Matt Cornet.md` is a hard limit on every claim, however well the JD would be served by exceeding it.
- **Never use "I" in resume bullets.** Profile is third person; bullets are implicit-first-person action verbs.
- **No figures of speech in the prose.** No metaphor, no calque of an English idiom, no defining Matt against an implied lesser peer, no sentence announcing what the next one will do. See `Notes/Writing voice.md` §3.
- **Never read voice rules from `_assets/voice_matt.md` or from `candidate_profile.md`.** Both are stubs as of 2026-09-10. The vault note is the only source, loaded through `general:writing-voice`; the short voice block in Matt's preferences is not a substitute.
- **Facts travel between pieces; sentences and framings never repeat.** Each piece does its own job. See Step 4b.
- **A form field answers its question.** Never substitute a generic pitch for an answer to what was actually asked.
- **The first pass carries the record.** The evidence sheet (Step 2a) is built before drafting and every hard requirement with a fact on record shows it. The target after the red-team is fewer than 10 tracked changes, all of them choices for Matt; a redline that adds facts from the log is a first pass that skipped Step 2a.
- **Level framing before everything else** (R18 to R20). A CV for a `hands_on` role (most postings, most freelance missions included) with a scale marker above the skills matrix, or without two first-hand facts there, does not go to the red-team. The role tag follows what the role requires, never the title or the contract type. Length is informational (R17).
- **Preserve formatting** by editing the base file chosen in Step 3a in place rather than rebuilding. The page is A4.
- **Deliver the `.docx` and nothing else — never a PDF** of the resume or letter. See Step 4. The one exception is `<Company>_JobPost_<Role>.pdf`, the captured posting (LinkedIn, Collective or supplied PDF, Step 0b).

## Edge cases

- **The vault is not connected:** `general:writing-voice` requests access itself; if it is declined or the computer is unreachable, stop before drafting prose. Do not fall back to the stubs, and do not draft from memory of the voice rules.
- **JD is for a role well outside fintech (e.g., pure tech, generic consulting):** Lead the diagnostic with this fit gap. Ask Matt to confirm before tailoring.
- **JD requires a tool Matt hasn't used (e.g., Snowflake specifically vs. his MS Fabric / Spark experience):** Surface honestly; suggest "transferable from MS Fabric / Spark" framing rather than implying direct experience.
- **JD is in French:** Generate the resume in French. Matt is bilingual — ask him to confirm if the formal/informal register isn't obvious from the JD.
