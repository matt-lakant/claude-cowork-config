---
name: interview-prep
description: "Prepares Matt Cornet for a specific interview — generates likely questions from the job posting and grounds STAR-format model answers in his actual experience from the master resume. Use this whenever Matt mentions an upcoming interview, asks for \"interview prep\", \"likely questions\", \"behavioral questions\", \"case prep\", or names a company he's interviewing with. Also use proactively after resume-tailor when Matt says he got an interview."
---

# Interview Prep

## What this skill does

Generates a personalized interview prep pack: predicted questions tied to the role, model answers grounded in Matt's real experience (not generic templates), and a one-page "cheat sheet" of metrics and stories he should have at his fingertips.

The grounding is what makes this useful — generic STAR prompts produce generic answers. By anchoring on `candidate_profile.md`, every answer references real engagements (APG, BlueMatrix, NBIM, Citadel, etc.) with real metrics.

## Source materials

> All paths in this skill are relative to the **Job Applications project root** — the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications").

1. `_assets/candidate_profile.md`
2. `_assets/voice_matt.md` — **model answers are spoken aloud by Matt.** A sentence he would not say is worse here than in any written deliverable: he has to deliver it out loud, under pressure, to someone watching his face. Corpus, banned constructions, review test.
3. The job posting (Matt should provide; if missing, ask)
4. Optional: the tailored resume from `applications/<company>-<role>/` — read it if it exists, since the interviewer probably read it too
5. Optional: `applications/<company>-<role>/redteam_notes.md` — if a red-team ran on this application, its "gaps assumed" and "prepare for interview" sections are the hostile questions, already identified by something trying to reject him. Start there.

## Inputs Matt will give you

- Company name and role
- Interview type (HR screen, hiring manager, panel, technical, case, exec round) — if he doesn't say, ask
- Interviewer name(s) — optional but useful for tailoring tone
- Time available to prep — affects depth (5 questions deep vs. 15 broad)

## Workflow

### Step 0 — Company overview (prerequisite)

This skill relies on the application's `company_overview.md`. **If `applications/<company>-<role>/company_overview.md` does not exist, run the `company-overview` skill first** to research the company and create it; otherwise read and reuse it. Use it to ground the "why this company" answers, sharpen the domain questions, and align the cheat sheet with the company's business and sector.

### Step 1 — Predict the questions

Generate 15 likely questions split across these buckets:

1. **Walk me through your background** (1 question) — the opener
2. **Behavioral / leadership** (4) — drawn from the JD's leadership signals: P&L, team scale, change management, stakeholder mgmt
3. **Domain expertise** (3) — financial services, the sub-sector named in the JD, AI/ML productization
4. **Situational / case** (3) — "how would you approach X in your first 90 days", "what's your view on Y trend"
5. **Why this role / why this company** (2)
6. **Tough / risk** (1) — "tell me about a failure", "why are you leaving"
7. **Questions he should ask back** (1 slot, 5+ candidate questions)

Bias the predictions toward what *this specific JD* signals — not a generic top-15 list. Any gap the application file already names — a missing pedigree, a sector he has never worked in, a scale mismatch between his past scope and the role — **will** be asked. Draft its answer whether or not it fits the buckets above.

### Step 2 — Draft model answers (STAR where applicable)

For each behavioral/situational question, draft a 4–6 sentence model answer using STAR (Situation–Task–Action–Result) anchored on a real entry from `candidate_profile.md`. Specifically:

- Match the question to the most relevant engagement (APG, NBIM, FactSet P&L, lakant.io platform, BlueMatrix integration, Goldman quant tools, etc.)
- Include the real metric ("drove 15% YoY growth", "~60 institutional accounts", "global deployment NY/London/Tokyo/HK")
- Keep it conversational — bullet-form STAR answers sound robotic when spoken
- Close with the lesson or the link to "and that's why I'd approach this role's challenge by..."

**Write every answer in Matt's voice, per `_assets/voice_matt.md`.** Plain declaratives, ordinary verbs, no metaphor, no calque of an English idiom, no defining himself against an implied lesser candidate, no announcing what he is about to say. Read each answer aloud in your head: if it needs a run-up before it says anything, cut the run-up.

For "why this company / why this role" questions, leave a short framework but ask Matt to fill in the specific motivation — that part can't be ghosted.

**Every name on the CV creates a follow-up question.** Wherever the resume cites a client, a partner, or a firm by name, prepare the second question rather than the first: what the engagement actually was, what he personally decided, what he pushed back on. The name proves nothing on its own; the detail behind it is what shows he held the role instead of watching it.

### Step 3 — Build the cheat sheet

A one-page "stories at the ready" reference Matt can review the morning of:

- **Top 5 hero stories** with one-line setup, metric, and lesson
- **Numbers to memorize:** every quantified achievement from the resume in a 2-column table
- **Five questions to ask back:** tailored to the company and role
- **Two sentences:** "why I'm leaving / what I'm looking for"
- **The three hostile questions**, each with the first sentence of its answer. The opening is what he needs ready; the rest he can improvise once he is moving.

### Step 4 — Save outputs

Save to `applications/<company>-<role>/interview_prep/`:

- `questions_and_answers.md` — full prep pack with all 15 questions and model answers
- `cheat_sheet.md` — the one-pager

**Never produce a PDF.** If Matt wants to print the one-pager, hand him the `.md` (or a `.docx` if he asks for one) and let him make the PDF himself from Word. Do not use the `pdf` skill for deliverables in this project.

Deliver both to the outputs panel with `SendUserFile` so he can open them from the conversation, plus a 3-line summary of the angle of the prep.

### Step 5 — Feed the voice corpus

If Matt rewrites a model answer, or reports back after the interview how he actually phrased something, **add his wording verbatim to section 2 of `_assets/voice_matt.md`**. Spoken answers are the richest source of his real voice available anywhere in this project, and they are the ones most often lost.

## Hard rules

- **Never invent stories.** Every STAR answer must be traceable to a real engagement in `candidate_profile.md`. If a question requires experience he doesn't have (e.g., "tell me about scaling a 200-person team"), draft a thoughtful answer that reframes around what he *has* done — and flag this as a gap.
- **Match register to interviewer level.** Exec-round answers are more strategic and concise; hiring-manager answers are more operational. Adapt accordingly.
- **Answers must sound like Matt, out loud.** See `_assets/voice_matt.md`. A line he would not say is unusable regardless of how well it reads.
- **Don't write a script.** Model answers are starting points; Matt should sound like himself. Note this at the top of the output.
- **For technical/case rounds**, include 2–3 frameworks he can lean on (e.g., for "how would you approach a data-quality issue in research", offer a 4-step framework grounded in his FactSet work).
- **Never produce a PDF.** See Step 4.