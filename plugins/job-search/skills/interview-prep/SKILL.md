---
name: interview-prep
description: "Prepares Matt Cornet for a specific interview — generates likely questions from the job posting and grounds STAR-format model answers in his actual experience from the master resume. Use this whenever Matt mentions an upcoming interview, asks for \"interview prep\", \"likely questions\", \"behavioral questions\", \"case prep\", or names a company he's interviewing with. Also use proactively after resume-tailor when Matt says he got an interview."
---

# Interview Prep

## Step map

| Step | What it does | What it produces | Stops the run when |
|---|---|---|---|
| Open | Opens the opportunity; loads the voice note and the ceilings | `applications/<slug>/interview_prep/` | the vault cannot be read |
| 0 | Reads or creates the company overview | `company_overview.md` | never |
| 1 | Predicts the questions from the posting, the brief, the fit report and the red-team notes | the question list | never |
| 2 | Drafts model answers with figures from the Current values table | `questions_and_answers.md` | never |
| 3 | Builds the cheat sheet | `cheat_sheet.md` | never |
| 4 | Saves and sends the files | file cards | never |
| 5 | Feeds the voice corpus with what Matt rewrites | via `asset-updater` | never |

> **The record is three files (2026-11-17).** *(project)* `_assets/candidate_profile.md` is the short profile: identity, the Current values table, the Experience summary, the guardrails. `_assets/profile_log.md` is the dated, append-only log: **every answer and correction from Matt is appended there**, one fact per entry, never in the profile. `_assets/facts/` holds one generated sheet per theme (list in `facts/INDEX.md`): read the sheet when a whole subject is needed. Wherever this skill says "the log in `candidate_profile.md`" or "the Q&A log", it means `profile_log.md`. After appending to the log, rebuild the sheets: `python3 <asset-updater skill dir>/scripts/build_facts.py <project>/_assets`.

## Before anything else — open the opportunity

**Run the `opportunity-intake` skill first.** It confirms the opportunity name, resolves
the kebab-case slug, creates `applications/<slug>/` if it does not already exist, and
starts the opportunity's `notes.md`. Every file this skill produces goes inside that
folder.

Do not write anything before the folder exists. If the slug is unknown, ask. If the
Job Applications project folder is not connected, stop and say so — never fall back to
the project root, to another connected folder, or to chat-only delivery.

## What this skill does

Generates a personalized interview prep pack: predicted questions tied to the role, model answers grounded in Matt's real experience (not generic templates), and a one-page "cheat sheet" of metrics and stories he should have at his fingertips.

The grounding is what makes this useful — generic STAR prompts produce generic answers. By anchoring on `candidate_profile.md`, every answer references real engagements (APG, BlueMatrix, NBIM, Citadel, etc.) with real metrics.

## Source materials

> Paths marked *(project)* are relative to the **Job Applications project root** — the folder that holds `applications/`, `_assets/` and `applications_tracker.md`. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications"). Paths marked *(vault)* are relative to the connected `obsidian-vault` folder.

> **Voice reference moved, 2026-09-10.** How Matt speaks and writes lives in *(vault)* `Notes/Writing voice.md`: §2 corpus, §3 banned constructions, §4 review test, §5.1 the candidature-prose surface that spoken answers follow. Load it through `general:writing-voice` in vault-required mode: it requests `C:\Users\mattc\Obsidian\obsidian-vault` itself if the folder is not connected, reads the note in full, and flags drift with the voice block in Matt's preferences. No fallback: if the note cannot be read, do not draft answers. `_assets/voice_matt.md` and the "Voice & style guidelines" section of `candidate_profile.md` are stubs — never read them as rules, never write to them.

1. *(vault)* `Notes/Writing voice.md` — **model answers are spoken aloud by Matt.** A sentence he would not say is worse here than in any written deliverable: he has to deliver it out loud, under pressure, to someone watching his face. Corpus, banned constructions, review test.
2. *(vault)* `Notes/Matt Cornet.md` — durable identity and the "Technology and scope ceilings" list. In an interview a breached ceiling is not a bad line, it is a claim he will be asked to defend and cannot. Read it before drafting any answer about a tool, a certification, a sector or a scope.
3. *(project)* `_assets/candidate_profile.md` — real engagements, metrics, and the append-only Q&A log
   **Figures come from the "Current values" table at the top of that file**, worded as it words them. Matt will say these numbers aloud to someone holding his CV: a figure that differs from the CV, or one he corrected since, is the worst place for an error. For a figure with no row, take the latest dated log entry.
3a. Optional: `applications/<company>-<role>/application_brief.md` — the requirement and evidence table, what is not claimable, and Matt's answers for this posting. The rows with thin evidence are where the hard questions will come from.
3b. Optional: `applications/<company>-<role>/fit_report.md` — the requirement coverage matrix and the gaps, if `job-fit-analyzer` ran. The 🟡 and 🚫 rows are where the hard questions will come from.
4. The job posting (Matt should provide; if missing, ask)
4b. *(project)* `_assets/story_bank.md` — the bank of stories Matt can tell (client, symptom, what he did with his own hands, cause, fix, what changed for the team, the delivery process and the product), each in a 60-second and a 3-minute version. **Read it before drafting any behavioural or technical answer and build the answer on a story from it when one fits**; a new story Matt tells while preparing is added to it in the same format. It was opened after an interview where the answers stayed at the level of principles.
5. Optional: the tailored resume from `applications/<company>-<role>/` — read it if it exists, since the interviewer probably read it too
6. Optional: `applications/<company>-<role>/redteam_notes.md` — if a red-team ran on this application, its "gaps assumed" and "prepare for interview" sections are the hostile questions, already identified by something trying to reject him. Start there.

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

Bias the predictions toward what *this specific JD* signals — not a generic top-15 list. Any gap the application file already names — a missing pedigree, a sector he has never worked in, a scale mismatch between his past scope and the role — **will** be asked. Draft its answer whether or not it fits the buckets above. Every ceiling in `Notes/Matt Cornet.md` that the JD touches is a predicted question too: the interviewer will ask about the tool the resume does not claim.

### Step 2 — Draft model answers (STAR where applicable)

For each behavioral/situational question, draft a 4–6 sentence model answer using STAR (Situation–Task–Action–Result) anchored on a real entry from `candidate_profile.md`. Specifically:

- Match the question to the most relevant engagement (APG, NBIM, FactSet P&L, lakant.io platform, BlueMatrix integration, Goldman quant tools, etc.)
- Check each metric against the Current values table before writing it (duration, reference date, unit). Print the figure the CV he sent carries when both are current; flag to Matt any figure where the sent CV and the table disagree, so he knows what the interviewer has in hand
- Include the real metric, worded as in the Current values table (for example "NPS from 22 to 51 in 12 months", "~60 enterprise accounts", "50 platform replacements, 90% live on the date planned at project start"). Check every example against the ceilings before using it: Goldman Sachs was London with on-site work in New York, never "deployment in NY, London, Tokyo and Hong Kong"; a sales figure such as revenue growth is used only when the role is a sales role
- Keep it conversational — bullet-form STAR answers sound robotic when spoken
- Close with the lesson or the link to "and that's why I'd approach this role's challenge by..."

**Write every answer in Matt's voice, per *(vault)* `Notes/Writing voice.md`.** Plain declaratives, ordinary verbs, no metaphor, no calque of an English idiom, no defining himself against an implied lesser candidate, no announcing what he is about to say. Run the §4 review test over each answer (`general:writing-voice` Step 4, surface §5.1). Then read it aloud in your head: if it needs a run-up before it says anything, cut the run-up.

For "why this company / why this role" questions, leave a short framework but ask Matt to fill in the specific motivation — that part can't be ghosted.

**Every name on the CV creates a follow-up question.** Wherever the resume cites a client, a partner, or a firm by name, prepare the second question rather than the first: what the engagement actually was, what he personally decided, what he pushed back on. The name proves nothing on its own; the detail behind it is what shows he held the role instead of watching it.

**Where a ceiling is the honest answer, draft the honest answer.** "I have benchmarked it, I have not delivered on it" is a usable sentence and a strong one; an evasive answer is what loses the room. Pair each with what he *has* done that is nearest.

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

Before delivering, run `python3 <resume-tailor skill dir>/scripts/cv_check.py <file> --rules <project>/_assets/cv_rules.md --profile <project>/_assets/candidate_profile.md --kind text` on `questions_and_answers.md` and on `cheat_sheet.md`. A `FAIL` is a superseded figure or a mandatory wording missing: fix it. A `WARN` on a ceiling word (Snowflake, PMP...) is expected where an answer names a gap honestly; check that it names the gap and does not claim the tool.

**Never produce a PDF.** If Matt wants to print the one-pager, hand him the `.md` (or a `.docx` if he asks for one) and let him make the PDF himself from Word. Do not use the `pdf` skill for deliverables in this project.

Deliver both to the outputs panel with `SendUserFile` so he can open them from the conversation, plus a 3-line summary of the angle of the prep.

### Step 5 — Feed the voice corpus

If Matt rewrites a model answer, or reports back after the interview how he actually phrased something, **add his wording verbatim to §2 of *(vault)* `Notes/Writing voice.md`**. Spoken answers are the richest source of his real voice available anywhere in this project, and they are the ones most often lost. If the vault is not connected, hand him the sentence and say it still needs filing rather than writing it into `_assets/`.

## Hard rules

- **Files for an opportunity live in `applications/<slug>/`, never at the project root.** The rule and its exceptions are in `opportunity-intake` (Hard rules), which wins on any conflict.
- **Never invent stories.** Every STAR answer must be traceable to a real engagement in `candidate_profile.md`. If a question requires experience he doesn't have (e.g., "tell me about scaling a 200-person team"), draft a thoughtful answer that reframes around what he *has* done — and flag this as a gap.
- **Respect the vault ceilings.** An answer that claims past a ceiling sets him up to be caught live. See `Notes/Matt Cornet.md`.
- **Match register to interviewer level.** Exec-round answers are more strategic and concise; hiring-manager answers are more operational. Adapt accordingly.
- **Answers must sound like Matt, out loud.** See `Notes/Writing voice.md`. A line he would not say is unusable regardless of how well it reads.
- **Never read voice rules from `_assets/voice_matt.md` or from `candidate_profile.md`.** Both are stubs as of 2026-09-10. Nor from the short voice block in Matt's preferences: load the note through `general:writing-voice`.
- **Don't write a script.** Model answers are starting points; Matt should sound like himself. Note this at the top of the output.
- **For technical/case rounds**, include 2–3 frameworks he can lean on (e.g., for "how would you approach a data-quality issue in research", offer a 4-step framework grounded in his FactSet work).
- **Never produce a PDF.** See Step 4.
