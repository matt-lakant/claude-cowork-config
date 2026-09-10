---
name: resume-tailor
description: "Tailors Matt Cornet's master resume to a specific job posting, optimizing for ATS keywords and recruiter signal while preserving truthfulness. Use this skill whenever Matt mentions tailoring, customizing, or rewriting his resume for a posting, applying to a role, or asks to \"make my resume match this job\" — even if he doesn't say the word \"tailor\". Also use when he pastes a job description and his master resume in the same turn."
---

# Resume Tailor

## What this skill does

Produces a tailored version of Matt's master resume for a specific job posting. The output preserves all factual content from the master but reorders, rewrites, and reweights bullets so the most relevant experience leads, ATS keywords from the posting are surfaced naturally, and the profile paragraph speaks to the role.

## Inputs Matt will give you

- **Required:** the job posting (URL, pasted text, or PDF). If Matt only gives a URL and you can't fetch it, ask him to paste the text.
- **Optional:** company notes, hiring manager name, application deadline.

## Source materials (read these every run)

> Paths marked *(project)* are relative to the **Job Applications project root** — the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications"). Paths marked *(vault)* are relative to the connected `obsidian-vault` folder.

> **Voice reference moved, 2026-09-10.** How Matt writes now lives in *(vault)* `Notes/Writing voice.md`, not in this project. §2 is the corpus of his own sentences, §3 the banned-construction table, §4 the review test, §5 the per-surface rules (5.1 candidature prose, 5.2 resume, 5.3 LinkedIn post). Run `ls $HOME/mnt/` and check for `obsidian-vault`; if it is not connected, ask Matt to connect `C:\Users\mattc\Obsidian\obsidian-vault` before drafting any prose, or call `device_request_folder_access` on it. `_assets/voice_matt.md` and the "Voice & style guidelines" section of `candidate_profile.md` are stubs pointing there — never read them as rules, never write to them.

1. *(vault)* `Notes/Writing voice.md` — the voice reference. Governs **every line of prose** (profile paragraph, cover letter, form answers) via §5.1, and **every resume bullet** via §5.2.
2. *(vault)* `Notes/Matt Cornet.md` — durable identity and the "Technology and scope ceilings" list. Read the ceilings before writing any claim about a tool, a certification, a sector or a scope.
3. *(project)* `_assets/candidate_profile.md` — canonical experience, target roles, accuracy guardrails, and the append-only tailoring Q&A log. **Read this first.**
4. *(project)* `_assets/master_resume.docx` — the formatted master. Use this as the template for the .docx output (preserve fonts, table layout, section structure).

## Workflow

### Step 0 — Company overview (prerequisite)

This skill relies on the application's `company_overview.md`. **If `applications/<company>-<role-slug>/company_overview.md` does not exist, run the `company-overview` skill first** to research the company and create it. If it already exists (e.g. from a prior `job-fit-analyzer` run), read and reuse it. Carry its insights into the profile paragraph, the narrative angle, the ATS keyword choices, and the cover-letter framing.

### Step 1 — Parse the posting
Extract:
- Role title, level, function
- Hard requirements (must-have skills, certifications, years of experience)
- Soft requirements (nice-to-haves)
- Top 15–25 ATS keywords (skills, tools, methodologies, domain terms — verbatim phrasing)
- Hiring signal: what would make a candidate stand out (impact metrics, scale, geos, regulatory, AI/ML, etc.)
- Tone of the JD (corporate, startup, consulting) — match it in the cover sections
- **Every question the application asks, verbatim.** Form fields ("why do you want to join us?") are deliverables in their own right, governed by Step 4b.

If the posting is a URL, fetch it. If fetching fails, ask Matt to paste it rather than guessing.

**LinkedIn postings (`linkedin.com/jobs/view/<id>/`) — use this exact method, don't retry server fetches:**
1. Do NOT use server-side web fetch. The job URL and the guest endpoint (`linkedin.com/jobs-guest/jobs/api/jobPosting/<id>`) both return empty — LinkedIn gates it and the page is client-rendered.
2. Use the Claude in Chrome browser tools: open/get a tab, navigate to the job URL, then read the page text. The first read returns only the header (title, company, location); the description body is lazy-loaded and not yet in the DOM.
3. **Scroll down the page about twice, then read the page text again.** The "About the job" card (FR: "Description du poste" / "Qualifications") only renders after scrolling. That second read has the full description.
4. If the Chrome extension isn't connected, ask Matt to paste the posting text.

**Re-posted roles.** Before tailoring, check `applications_tracker.md` and the `applications/` folders for a prior application to the same company under a similar title. Companies re-post unfilled roles under a new name, often with a harder required profile. If you find one, diff the two postings and lead the diagnostic with what changed in the *required profile*, not in the missions — that delta is the whole tailoring brief. Treat the earlier application as a fact to handle (it is sitting in their ATS), not as something to quietly repeat.

**Two postings are not proof of one re-post.** Identical missions are suggestive, not conclusive. The decisive check is whether the older posting is still live: two live postings mean two roles. State the inference as an inference in `job_description.md` and name the check; on 2026-09-04 a re-post was assumed and written up as fact, and five days later the new posting vanished while the old one stayed up — the opposite conclusion. A hypothesis written as a finding is a hypothesis nobody will question at interview time.

### Step 2 — Score Matt against the posting (briefly, in chat)

Before generating, give Matt a **1-paragraph diagnostic** in chat:
- Strong-fit dimensions (3–5 bullets)
- Gap dimensions where the resume needs to lean harder or where a skill is genuinely missing (2–3 bullets)
- Top 10 ATS keywords from the JD that should appear in the tailored resume
- Recommended angle / narrative thread for this application

This lets Matt sanity-check before you spend tokens generating the .docx. Pause for confirmation only if the angle is non-obvious or the gap is significant; otherwise proceed.

### Step 2b — Mine every requirement (ask Matt before generating)

Matt has 20+ years of broad experience; the master resume captures only the headline version. The goal of this step is that **no requirement is left weakly evidenced when he actually has the experience to back it** — for the resume *and* the cover letter. So work requirement-by-requirement, not by a fixed quota of questions.

1. **Build the requirement checklist.** List every requirement the posting states — each hard requirement, each soft / "nice-to-have", and every named tool, platform, method, certification, regulation, sector, and scope/scale bar. If `job-fit-analyzer` already produced a Requirement coverage matrix for this role, start from it.
2. **Classify each against the vault ceilings + `_assets/candidate_profile.md` + `master_resume.docx`:**
   - **Blocked** — the "Technology and scope ceilings" section of *(vault)* `Notes/Matt Cornet.md` says it cannot be claimed. Do not question, do not soften; it is a stated gap.
   - **Strong** — already clearly evidenced with specifics. No question needed.
   - **Partial / Absent / Unknown** — adjacent, missing, or plausibly-in-his-background-but-undocumented. **Each of these gets a question.**
3. **Question Matt on every Partial / Absent / Unknown requirement** using the `AskUserQuestion` tool. The tool allows max 4 questions per call, so **batch them into successive rounds of up to 4 and keep going until every such requirement has been put to him** — do not stop at an arbitrary 3–5. Make each option concrete and grounded in something plausibly in his background so he can confirm in one click; use multi-select where natural; always leave room for him to add detail. For each requirement, probe what he actually did and at what scope:
   - **Named tools/platforms** (e.g. Jira / JSM, CI-CD, specific clouds, AI labs/hyperscalers, ITSM/SDLC tooling) — what did he build or run, and at what scope?
   - **Sector / domain** framing, and any non-finance work to surface.
   - **Scope & scale** (team size, budget, P&L, regions, client tier) where the JD implies a bar. When the JD's scale is *smaller* than Matt's headline numbers, ask for the intermediate figure — direct reports, missions run in parallel, typical engagement length — because the headline alone reads as overqualification and invites "why would you come here, and for how long?".
   - **Regulations, risk controls, and operating models** the JD names — which has he dealt with hands-on?
   - **Adjacent / non-obvious work** the headline resume omits.
4. **Asking a lot is expected.** A senior role with 10+ requirements may warrant 2–3 rounds of questions. One extra question costs far less than shipping a resume or cover letter that under-sells real experience. The only requirements you skip are those already rated **Strong** or **Blocked**.
5. **Record every confirmed answer in `candidate_profile.md`** (standing rule, 2026-06-25): append each answer (dated) to the `## Confirmed details from tailoring Q&A (append-only log)` section, and promote durable items into the relevant Experience bullets / master via `asset-updater`. A confirmed answer that raises or lowers a ceiling belongs in *(vault)* `Notes/Matt Cornet.md` too — hand that to `asset-updater`. Then **fold them into the rewrite as real, specific bullets — and reuse the same confirmed specifics in the cover letter.** Never invent — surface only what Matt confirms. If he confirms nothing for a requirement, keep it as a stated gap in the memo.

This step is **mandatory on every run** (not just for out-of-track or tool-heavy roles). It can be abbreviated only for a near-identical re-tailor of a role he has already been fully mined on — and even then, re-ask any requirement the prior run left Partial / Absent. (Implements the `feedback_tailoring_alignment_questions` practice.)

### Step 3 — Rewrite with these rules

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
- Drop bullets that are irrelevant to this role to keep length tight (target 2 pages max)
- Put the bullet answering the JD's entry criterion in the top three of its role. A line sitting seventh on page two does not exist during a six-second screen.

**Skills matrix:**
- Reorder so the top row hits JD must-haves; cells unchanged in content
- If the JD names a tool/method that Matt has used (per `candidate_profile.md` and the vault ceilings) but isn't in the matrix, add it; if he hasn't used it, or a ceiling blocks it, do not add it

**Education and footer:** unchanged.

### Step 4 — Generate the .docx

Use `_assets/master_resume.docx` as the formatting template. Open it with `python-docx`, replace text in place where possible to preserve styles, fonts, and table layout. Don't rebuild from scratch — that loses the master's polish.

Save to: `applications/<company>-<role-slug>/CORNET_<Company>_<Role>_<YYYY-MM-DD>.docx`

**Never produce a PDF.** Matt makes his own PDF from Word, after he has validated and reformatted the `.docx`. Do not save a `.pdf` beside the `.docx`, do not attach one, and do not offer one. If you need a PDF to check pagination, convert into a temp directory **outside** the project folder (e.g. `$HOME/tmp`), read the page count there, and leave nothing behind. A `.pdf` in an application folder is a stale copy of a document that is about to change, and on Matt's machine a session cannot delete files, so it becomes his cleanup.

Where:
- All CV/cover-letter filenames start with the `CORNET_` prefix (see `feedback_filename_convention`). If a same-dated file already exists and is locked (OneDrive placeholder) or you've materially revised it, save a `_v2` / `_v3` copy rather than overwriting — the per-application folder doubles as version history.
- `<role-slug>` is a kebab-cased short version of the role title (e.g., `head-of-product`).
- `<YYYY-MM-DD>` is **the date the file is being generated today** — i.e. today's date in the user's timezone, not the JD posting date, the application deadline, or any date pulled from the posting itself. Run `date +%Y-%m-%d` (or check `currentDate` in env) at generation time. If the resume is regenerated later (e.g., after Matt's manual edits or a JD update), save under a new file with the new date and leave the older one in place — the per-application folder doubles as a version history.

### Step 4b — The prose pieces: facts travel, sentences do not

Write every prose piece in Matt's voice per *(vault)* `Notes/Writing voice.md`, §5.1 for the surface rules. Then give each piece its own job and let it draw from the shared stock of evidence whatever serves that job. **The same fact may appear in two pieces**, provided each does something different with it. What must never repeat is a sentence or a framing.

| Piece | Its job | What it takes |
|---|---|---|
| **CV** | Inventory the facts, scannable | Everything, no prose |
| **Cover letter** | Select 2–3 of the CV's strongest facts and make them mean something for this employer | Whatever carries the argument |
| **Form field** | **Answer the question it asks**, and nothing else | Whatever answers that question, from the CV or the letter |

**The letter must pick up the CV's key elements.** The CV is scanned; the letter is read. A letter that reuses nothing leaves its strongest evidence uninterpreted, and uninterpreted evidence does not weigh. Give the cause, the consequence, and why it answers this employer's problem: the CV states "margin taken from roughly 27 to 32 points in three years", the letter says what produced it and what it proves about how he runs a P&L. Select two or three facts, never the list. What to avoid is the letter that paraphrases the CV in sentences — a prose inventory with no cause, no consequence, no judgement.

**The form field is not held to novelty.** It answers a specific question, and to do so it reuses the key elements of the CV or the letter that answer it. Its constraint is the question, not freshness. Read the question literally and answer that; never drop a generic pitch beside it.

**Order of drafting:** CV first (it fixes the stock of facts), then the letter, then the form field, which picks last whatever best answers its question.

**Before delivering, read the pieces back to back looking for twin sentences, not for shared facts.** Rewrite any repeated phrasing or framing outright. Then run the §4 review test over all of them. And never announce the division of labour to the reader: a letter opening with "the form says why, this letter says what" explains its plan instead of executing it, which also breaks the §3 rule against sentences that announce the next one.

Note in the file which anchoring sentence to restore if a piece is later sent on its own. Deliver short texts to the outputs panel with `SendUserFile` so Matt can open and copy them, and keep a copy in the application folder.

### Step 5 — Write a tailoring memo

Save alongside the resume: `applications/<company>-<role-slug>/tailoring_notes.md`

Contents:
- JD summary (3 sentences)
- Top 10 ATS keywords used + where they appear in the resume
- Trade-offs made (what was de-emphasized, what got cut)
- Which CV facts the letter picked up, and what each one was made to mean
- The exact question each form field asked, and which facts were used to answer it
- Open questions / things to verify before submitting
- Recommended cover letter angle (2 sentences)

This memo is for Matt to skim before submitting and is invaluable when he prepares for the interview weeks later.

### Step 6 — Update the tracker

Update `applications_tracker.md` at the project root (the tracker is now markdown, not the legacy `.xlsx`) — add a row via the `application-tracker` skill. Include: company, role, date applied (or "drafted"), source URL, status = "drafted", notes pointer.

### Step 7 — Adversarial red-team (mandatory gate, before presenting)

**Do not hand the resume to Matt until it has survived an adversarial review.** Run the `resume-redteam` skill on the tailored `.docx` as the final gate. It re-reads the JD, `company_overview.md`, and `candidate_profile.md`, attacks the resume in a fresh-context subagent (what's weakest, vaguest, removable, missing, over-claimed), redlines it with tracked changes authored "Recruiter", and asks Matt questions where a fix needs a fact not yet on record. Fold its confirmed answers back into the resume and `candidate_profile.md` before presenting. This gate is the reason tailoring isn't "done" at Step 6 — a self-written resume hasn't been stress-tested until something independent has tried to break it.

**When the red-team finds a factual error rather than a weakness** — a certification he does not hold, a stale claim, a guardrail decided but never applied — fix it at the source in the same run: *(project)* `_assets/candidate_profile.md`, *(project)* `_assets/master_resume.docx`, and *(vault)* `Notes/Matt Cornet.md` if it is a ceiling, not just the CV in hand. A guardrail written only into the Q&A log does not propagate itself, and the error comes back on the next tailoring run.

### Step 8 — Feed the voice corpus

If Matt rewrites any sentence of the prose, **add his version verbatim to §2 of *(vault)* `Notes/Writing voice.md`** in the same turn, and hand the rest to `asset-updater`. A sample needs no threshold to be worth keeping; a banned-construction rule waits for the pattern to repeat twice. If the vault is not connected, say so and hand Matt the sentence rather than writing it into `_assets/`.

## Output: present to Matt

Give him links to the red-teamed `.docx` (with the recruiter's tracked changes), the tailoring memo, the `redteam_notes.md` critique, and the `company_overview.md` company brief (from Step 0), plus a 3-line summary of the angle taken and the biggest weakness the red-team flagged. Don't paste the resume text into chat — the .docx is the deliverable. Short prose pieces go to the outputs panel, not into the conversation.

## Hard rules

- **Never invent experience, metrics, employers, dates, or certifications.** If the JD asks for something Matt doesn't have, surface it as a gap in the diagnostic — do not paper over it.
- **Respect the vault ceilings.** The "Technology and scope ceilings" section of `Notes/Matt Cornet.md` is a hard limit on every claim, however well the JD would be served by exceeding it.
- **Never use "I" in resume bullets.** Profile is third person; bullets are implicit-first-person action verbs.
- **No figures of speech in the prose.** No metaphor, no calque of an English idiom, no defining Matt against an implied lesser peer, no sentence announcing what the next one will do. See `Notes/Writing voice.md` §3.
- **Never read voice rules from `_assets/voice_matt.md` or from `candidate_profile.md`.** Both are stubs as of 2026-09-10. The vault note is the only source.
- **Facts travel between pieces; sentences and framings never repeat.** Each piece does its own job. See Step 4b.
- **A form field answers its question.** Never substitute a generic pitch for an answer to what was actually asked.
- **Two pages max** for senior roles unless Matt asks otherwise. If the master overflows, cut the oldest/least-relevant role bullets first.
- **Preserve formatting** by editing `master_resume.docx` in place rather than rebuilding.
- **Deliver the `.docx` and nothing else — never a PDF.** See Step 4.

## Edge cases

- **The vault is not connected:** ask Matt to connect it before drafting prose. Do not fall back to the stubs, and do not draft from memory of the voice rules.
- **JD is for a role well outside fintech (e.g., pure tech, generic consulting):** Lead the diagnostic with this fit gap. Ask Matt to confirm before tailoring.
- **JD requires a tool Matt hasn't used (e.g., Snowflake specifically vs. his MS Fabric / Spark experience):** Surface honestly; suggest "transferable from MS Fabric / Spark" framing rather than implying direct experience.
- **JD is in French:** Generate the resume in French. Matt is bilingual — ask him to confirm if the formal/informal register isn't obvious from the JD.