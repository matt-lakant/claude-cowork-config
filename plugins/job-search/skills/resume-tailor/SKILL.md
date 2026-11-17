---
name: resume-tailor
description: "Drafts Matt Cornet's tailored resume for a specific job posting from the application brief, checks it mechanically, and hands it to the red-team. Use this skill whenever Matt mentions tailoring, customizing, or rewriting his resume for a posting, applying to a role, or asks to \"make my resume match this job\", even if he does not say the word \"tailor\". It needs applications/<slug>/application_brief.md: when that file is missing, run application-brief first."
---

# Resume Tailor

## Step map

Run the steps in this order. Steps 1, 5 and 8 are gates: the run does not go past them until they pass.

| Step | What it does | What it produces | Stops the run when |
|---|---|---|---|
| 1 | Checks the brief exists and is complete | `GATE brief: PASS` | the brief is missing or incomplete: run `application-brief` |
| 2 | Loads the rules that govern the text | nothing | the vault note cannot be read |
| 3 | Drafts the content: framing, profile, expertise, bullets, matrix | the text of the CV | never |
| 4 | Writes the `.docx` on the base file; French: runs `fr_spaces.py` on it | `CORNET_<Company>_<Role>_<date>.docx` | the base file cannot be opened |
| 5 | Runs the mechanical check, matches evidence and decisions to CV lines | `RESULT: 0 FAIL`; two filled tables | any `FAIL`, an unused fact, an unapplied decision |
| 6 | Writes the form answers, if the posting has questions | `form_answers.md` | the voice note was not read in full |
| 7 | Writes the memo and updates the tracker | `tailoring_notes.md`, tracker row | never |
| 8 | Runs the draft gate, then the red-team | `GATE draft: PASS`, then the redline | the gate lists a missing item |
| 9 | When Matt returns the file: learns from his edits | via `asset-updater` | never |

This skill drafts. It does not parse the posting, search the record, question Matt or choose the base file: `application-brief` does, and its output is this skill's input. If you find yourself doing one of those things here, the brief is incomplete: go back to it.

> **The record is three files (2026-11-17).** *(project)* `_assets/candidate_profile.md` is the short profile: identity, the Current values table, the Experience summary, the guardrails. `_assets/profile_log.md` is the dated, append-only log: **every answer and correction from Matt is appended there**, one fact per entry, never in the profile. `_assets/facts/` holds one generated sheet per theme (list in `facts/INDEX.md`): read the sheet when a whole subject is needed. Wherever this skill says "the log in `candidate_profile.md`" or "the Q&A log", it means `profile_log.md`. After appending to the log, rebuild the sheets: `python3 <asset-updater skill dir>/scripts/build_facts.py <project>/_assets`.

## What it reads

> *(project)* paths are relative to the Job Applications project root, the folder that holds `applications/`, `_assets/` and `applications_tracker.md`. *(vault)* paths are relative to the connected `obsidian-vault` folder.

1. `applications/<slug>/application_brief.md`: role tag, requirements and evidence, first-hand facts, decisions, base file, top-third keywords, form questions, angle. **The brief is the plan. Draft from it.**
2. `applications/<slug>/job_description.md` and `company_overview.md`.
3. *(project)* `_assets/cv_rules.md`, Part 1: the standing rules.
4. *(project)* the Current values table at the top of `_assets/candidate_profile.md`: the wording of every figure.
5. *(vault)* `Notes/Matt Cornet.md`: "Framing guardrails" and "Technology and scope ceilings".
6. *(vault)* `Notes/Writing voice.md`, through `general:writing-voice`: **CV mode** (§1, §3, §4 with 4.1, §5.2) when the run writes a CV only; **the note in full** as soon as a form answer or any other prose is drafted.
7. `references/level-framing.md` (always) and `references/sector-wording.md` (when the brief carries `non_finance`), in this skill's folder.

`_assets/voice_matt.md` and the "Voice & style guidelines" section of the profile are pointers to the vault note. They hold no rule.

## Step 1: Gate on the brief

```text
python3 <application-brief skill dir>/scripts/gate.py brief <project>/applications/<slug>
```

If it does not print `GATE brief: PASS`, run `application-brief` (or complete the brief) before anything else. Then read the brief in full.

## Step 2: Load the rules

Read `cv_rules.md` Part 1, the Current values table, the ceilings, the voice note in the mode above, and `references/level-framing.md`. If the vault cannot be read, stop: no fallback to the pointer files or to memory of the rules.

## Step 3: Draft the content

Work in this order. The role tag in the brief decides the framing before a single line is written.

**3.1 Level framing (R18 to R20).** Details and examples in `references/level-framing.md`.
- **`hands_on` role** (most postings, most freelance missions): no scale marker in the header, the profile or the areas of expertise (no 80+ or 110 people, no ~USD 40M P&L, no board, C-level, SVP, no "through regional directors"). At least two first-hand facts above the skills matrix: the ones listed in the brief. The first bullet of each role says what he did himself or with his direct team of 5 to 10, and carries no headcount, including a build figure ("from zero to 50+" reads "from zero", with "grown to 50+ people" in the Context line). Scale appears once, in the Context line of the role. Verbs of distance ("oversaw", "sponsored", "governed") become what he did, when the record supports it.
- **`leadership` role:** scale and seniority lead and are not deflated. Keep one or two first-hand facts in the bullets.
- **Job titles are facts and are never altered**, whatever the tag. The tag follows what the role requires, never the title or the contract type.

**3.2 Header.** Name, then the title on two lines (role, then specialty), then one contact line starting with "Paris". Every line fits on one line. No citizenship line. Languages go in Education.

**3.3 Profile (3 to 4 sentences).** Impersonal constructions, never third person, "I" only if unavoidable. Open on the experience that answers the core of the role. Name two or three of his most relevant contexts. BlueMatrix is "last engagement at BlueMatrix, with notably...", never "9 months at BlueMatrix". No self-awarded adjective, no degree repeated from Education, no sentence that grades his fit.

**3.4 Areas of expertise (up to 6 lines).** The first three answer the posting's must-haves, in its vocabulary where it is true. Cut a line that the matrix and the bullets already make: saying one thing in three places is paying three times for one point.

**3.5 Experience bullets.**
- Every hard requirement that has a fact in the brief shows that fact, in the top three bullets of its role or above the matrix.
- Each role keeps at least 2 bullets; the most relevant role up to 8.
- Structure: action verb, what was done, scope, measurable result when there is one. Keywords sit inside real achievements, never in a bare list.
- **Every figure is written as the Current values table words it** (duration, reference, unit). A figure with no row is checked against the latest dated log entry and reported to `asset-updater`. Never take a figure from the base file.
- Lakant: lakant.io and lakant builders under one "Lakant – Founder" header. lakant.io has no client and no production traffic: built, developed, tested. BlueMatrix is integration plus AI roadmap and governance, not production AI.
- `ps_role`: 3 client engagements under FactSet 2019-2024 and 2 under FactSet 2007-2018, each showing what the role does (integration, migration, go-live, users), with figures from the record (R5).
- `non_sales`: the FactSet 2019-2024 title reads "Global Director, Sales Engineering, Implementation and Support", the sales part of his department is labelled "sales engineering", and every sales mandate is removed (R3).
- `non_finance`: the wording of the whole CV is rewritten in the employer's vocabulary, in this first draft (R4). Read `references/sector-wording.md`.
- English CVs: no definite article at the head of a nominal group. Posting in French: the CV is in French, English trade terms kept where professional usage is English.
- Drop what is irrelevant to this role. Length is reported for information (R17); it is not a target.

**3.6 Skills matrix.** Kept (R7). Reorder so the first row answers the must-haves. Add a tool or method only if he used it and no ceiling blocks it.

**3.7 Education.** Unchanged, plus the languages line.

**Never, anywhere:** an invented fact, metric, employer, date or certification; a claim beyond a ceiling; a "transferable from..." phrase for a tool he has not used; a limitation offered on the CV (gaps go in the letter); an em dash; a figure of speech; filler vocabulary.

## Step 4: Write the `.docx`

Edit the base file named in the brief, in place, with `python-docx`: replace text and keep styles, fonts and tables. Do not rebuild the document. If the base is not A4, convert the working copy first: `python3 <this skill's dir>/scripts/to_a4.py <base.docx> <working copy.docx>`.

**French CV: fix the spacing on the file you just wrote** (R22): `python3 <this skill's dir>/scripts/fr_spaces.py <cv.docx> <cv.docx>`. The CVs Matt returns from Word carry plain spaces before `;` `:` `?` `!`, so every French base brings them into the draft, and the text you add is right or wrong depending on the run. The script puts a non-breaking space everywhere in one pass; `cv_check.py` fails the file otherwise. Run it on `form_answers.md` too when the answers are in French.

Save as `applications/<slug>/CORNET_<Company>_<Role>_<YYYY-MM-DD>.docx`, with today's date. Never overwrite an Office file: a revision is `_v2`, `_v3`. **Never produce a PDF** of the CV; Matt makes his own from Word. To count pages, convert in a temporary folder outside the project and leave nothing behind.

## Step 5: Check

**5.1 Mechanical check.**

```text
python3 <this skill's dir>/scripts/cv_check.py <cv.docx> --rules <project>/_assets/cv_rules.md \
        --profile <project>/_assets/candidate_profile.md --tags <cv_check tags of the brief> \
        --top-keywords "<top-third keywords of the brief, separated by ;>" \
        --hands-on "<fragments of the first-hand facts of the brief, separated by ;>"
```

The scripts ship with the plugin: stage the `.docx`, `cv_rules.md` and `candidate_profile.md` into the cloud workspace and run them there, or run them through `device_bash` if the plugin folder is reachable there. Nothing is installed anywhere.

- A `FAIL` blocks: fix the CV and run again until the last line reads `RESULT: 0 FAIL`.
- A `WARN` is a judgment: keep it only with a reason, written in the memo.
- The script tests words and positions. Rules such as "no sales mandate" or "wording that echoes the employer" still need your reading of the whole CV against `cv_rules.md` Part 1.

**5.2 Evidence.** For each row of the brief's evidence table that has a fact on record, quote the CV line that carries it, or write `not used:` and the reason. A requirement stated in the posting's title or opening lines has its proof **above the skills matrix**, not only in a bullet below it. A hard requirement with a fact and no line is the commonest cause of a heavy redline: fix the CV.

**5.3 Decisions.** For each row of the brief's decisions table, quote the CV line that applies it. No line to quote means the decision was not applied: fix the CV.

## Step 6: Form answers

Only when the brief lists form questions. Read the voice note in full first (`general:writing-voice`, vault required), surface §5.1.

- A form field answers the question it asks, literally, with the CV facts that answer it. Never a generic pitch beside the question.
- The same fact may appear in the CV and in an answer. A sentence or a framing never appears twice.
- Open on his experience, never on "I would like to lead <job title>" and never on a standalone fact about the role or the employer.
- Run the §4 review test, including the AI-tell list and, for a "why us" answer, the swap test. Run `cv_check.py --kind text` on the file.
- Save `applications/<slug>/form_answers.md`, each answer under its question, and send it as a file card.

The cover letter is not written here. `cover-letter` writes it from the CV Matt returns.

## Step 7: Memo and tracker

Write `applications/<slug>/tailoring_notes.md`. **The three headings marked "key" are read by the gate: keep them exactly, in English.** The content follows the posting's language.

```markdown
# Tailoring notes: <Company>, <Role>

## Summary
<the posting in 3 sentences, the angle taken>

## Check result        (key)
<the cv_check.py command with its tags, and its last lines down to RESULT>
<each WARN kept, with the reason>

## Evidence used        (key)
| Requirement | Fact on record | CV line, or "not used: reason" |
|---|---|---|

## Decisions applied        (key)
| Decision | CV line that applies it |
|---|---|

## Keywords
<top-third keywords and where each sits; top 10 ATS keywords and where>

## Trade-offs
<what was cut or moved down, and why>

## Form answers
<each question, and the facts used to answer it>

## Open questions
<what Matt should verify before sending; gaps to prepare for the interview>

## Cover letter angle
<two sentences: the two or three CV facts that best answer the posting, and the fact about the employer to tie them to>
```

Then add or update the row in `applications_tracker.md` through `application-tracker` (status `drafted`). On a re-run of a posting already tracked (a comparison run with a suffix), leave the summary row as it is: add a dated note to the application's section in `applications_tracker_details.md` and a line to the history file.

## Step 8: Gate, then red-team

```text
python3 <application-brief skill dir>/scripts/gate.py draft <project>/applications/<slug>
```

When it prints `GATE draft: PASS`, run `resume-redteam` on the `.docx`. **Matt does not see the CV before the red-team has run.** What the red-team finds wrong against the record is fixed at the source in the same run (profile, Current values table, vault note for a ceiling), not only in this CV.

Present to Matt: the redlined `.docx`, `tailoring_notes.md`, `redteam_notes.md`, `application_brief.md` and `company_overview.md`, each as a file card (`SendUserFile`). Open with the count from the red-team ("6 corrections applied, 4 choices for you"), then the angle and the biggest weakness in three lines. Do not paste the CV into the chat. End with the next step in one line: finalize the redline in Word and attach it back here; that starts `cover-letter` and feeds his edits into the voice note.

## Step 9: When Matt returns the file

Run `asset-updater` in returned-file mode before anything else. It files his version, compares it with the draft and the redline, sends every sentence he wrote to the voice note, logs the reviewer edits he rejected, and routes factual changes to the profile and the vault. If he returned the CV to get a letter, continue with `cover-letter` in the same turn.

## Hard rules

- **Files for an opportunity live in `applications/<slug>/`**, never at the project root (see `opportunity-intake`).
- **No draft without a brief that passed its gate.**
- **Level framing first** (R18 to R20), decided by the role tag of the brief.
- **Nothing invented, nothing beyond a ceiling, no gap dressed up.**
- **Rules come from `cv_rules.md`, figures from the Current values table, voice from the vault note.** None is recalled from memory or copied from a previous CV.
- **`RESULT: 0 FAIL`, every fact on record used, every decision applied, `GATE draft: PASS`**, before the red-team.
- **Edit the base file in place. A4. `.docx` only, never a PDF, never an overwrite.**
- **Never "I" in bullets, never third person, no em dash, no figure of speech.**

## Edge cases

- **The vault is not connected:** `general:writing-voice` requests access; if refused, stop before drafting.
- **The brief has open questions** (Matt was not there to answer): draft without the missing facts, never with guesses, and list the open questions first in your closing message.
- **The posting changed since the brief:** re-run `application-brief` Step 2 and update the brief before drafting.
- **Register in French:** if the posting does not settle formal or informal address in the form answers, ask.
