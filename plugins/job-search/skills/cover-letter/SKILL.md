---
name: cover-letter
description: "Writes Matt Cornet's cover letter for a specific role, in his voice and from his final CV, so it reads as written by him and not generated. Starts when Matt attaches the CV he finalized in Word after resume-redteam, or when he asks for a cover letter, lettre de motivation, or a letter to go with an application. Answers why this role, why this company, which experience applies, the gap, and his situation; learns from the CV he sends back; ends with the mandatory cover-letter-redteam gate."
---

# Cover Letter

## Step map

| Step | What it does | What it produces | Stops the run when |
|---|---|---|---|
| Open | Opens the opportunity; checks the final CV is attached | `applications/<slug>/` | no final CV from Matt: run the resume skills first |
| 1 | Learns from the CV he sent back (`asset-updater`, returned-file mode) | his edits filed | never |
| 2 | Asks Matt for the hook, one round | his answers, logged | he is not there: draft without, say so first |
| 3 | Plans the letter against §5.4 of the voice note and the role tag | the plan | the voice note cannot be read |
| 4 | Drafts on the letter template | `CORNET_<Company>_Cover_Letter_<date>.docx` or `..._Lettre_<date>.docx` | never |
| 5 | Self-check: review test, `cv_check.py --kind letter` | `RESULT: 0 FAIL` | any `FAIL` |
| 6 | Mandatory gate: `cover-letter-redteam` | the redlined letter | never |
| 7 | Presents to Matt | file cards | never |
| 8 | Learns from the letter he sends back | via `asset-updater` | never |

> **The record is three files (2026-11-17).** *(project)* `_assets/candidate_profile.md` is the short profile: identity, the Current values table, the Experience summary, the guardrails. `_assets/profile_log.md` is the dated, append-only log: **every answer and correction from Matt is appended there**, one fact per entry, never in the profile. `_assets/facts/` holds one generated sheet per theme (list in `facts/INDEX.md`): read the sheet when a whole subject is needed. Wherever this skill says "the log in `candidate_profile.md`" or "the Q&A log", it means `profile_log.md`. After appending to the log, rebuild the sheets: `python3 <asset-updater skill dir>/scripts/build_facts.py <project>/_assets`.

## Before anything else: open the opportunity

**Run the `opportunity-intake` skill first.** It confirms the opportunity name, resolves
the kebab-case slug, creates `applications/<slug>/` if it does not already exist, and
starts the opportunity's `notes.md`. Every file this skill produces goes inside that
folder.

Do not write anything before the folder exists. If the slug is unknown, ask. If the
Job Applications project folder is not connected, request access to
`C:\Users\mattc\OneDrive\Documents\Claude\Projects\Job Applications` yourself; never fall
back to the project root, to another connected folder, or to chat-only delivery.

## Why this skill exists (2026-09-24)

The letter used to be drafted inside `resume-tailor`, in the same pass as the CV. Two
problems: it came out as CV prose in sentences, and nothing independent reviewed it. A
cover letter is the one document a recruiter reads as the candidate himself, so a letter
that sounds generated costs more than it earns. It does not get flagged by a detector; it
gets skimmed and counts for nothing.

So the letter is written **after** the CV is final, from the CV Matt actually sends, around
facts and motivations he supplies, and it goes through its own adversarial gate.

## Where it sits in the pipeline

```
resume-tailor -> resume-redteam -> Matt finalizes the CV in Word and attaches it here
  -> asset-updater (returned-file mode) -> cover-letter -> cover-letter-redteam
  -> Matt finalizes the letter in Word and attaches it here -> asset-updater (returned-file mode)
```

**Input that starts it:** the final CV `.docx` attached to the chat. If Matt asks for a
letter without attaching one, ask him to attach the CV he is sending. If no tailored CV
exists for this application at all, run `resume-tailor` first. A letter drafted against a
CV that is about to change is drafted twice.

## Source materials (read every run)

> *(project)* paths are relative to the Job Applications project root. *(vault)* paths are
> relative to the connected `obsidian-vault` folder. Run `ls $HOME/mnt/`; if `obsidian-vault`
> is missing, request access to `C:\Users\mattc\Obsidian\obsidian-vault` yourself. Do not
> draft a single sentence from memory of the voice rules.

1. *(vault)* `Notes/Writing voice.md`, **loaded through `general:writing-voice` in
   vault-required mode**: it reaches the vault, reads the note in full and flags drift with the
   voice block in Matt's preferences. No fallback here: if the note cannot be read, stop. §2 corpus, §3 banned constructions, §4 review test
   (points 8 and 9, list 4.1), §5.1 candidature prose, **§5.4 cover letter** (question order,
   length, frame, one reference letter per language).
2. *(vault)* `Notes/Matt Cornet.md`: the "Technology and scope ceilings" section is a hard
   limit on every claim.
3. The final CV Matt attached: the stock of facts the letter draws from.
4. `applications/<slug>/job_description.md` (the most recent dated copy if several).
5. `applications/<slug>/company_overview.md`. If missing, run `company-overview` first; the
   "why this company" sentence cannot come from anywhere else.
6. `applications/<slug>/tailoring_notes.md`: the recommended cover letter angle. A starting
   point, not a script.
6b. `applications/<slug>/application_brief.md`, when it exists: the role tag (it frames the letter as it framed the CV), the first-hand facts, Matt's answers to the questions and the decisions. A decision recorded there holds for the letter too.
7. *(project)* `_assets/candidate_profile.md`: ground truth, including the append-only Q&A log.
   Its **"Current values" table** (top of the file) gives the current wording of every figure. A figure in the letter is written as worded there, even when the final CV words it differently: the CV may predate a correction. If the two disagree, say so to Matt instead of choosing silently.
7b. *(project)* `_assets/cv_rules.md`: the standing rules. The ones that apply to a letter are R4 (wording for a non-finance employer), R6 (the 90% wording, which Matt set for letters and emails too), R11 to R15. R10 works the other way here: the gap between the profile and the posting is handled in the letter.
8. `applications/<slug>/notes.md` and any form answers already drafted (`form_answers*.md`),
   to avoid twin sentences.
9. *(project)* `_assets/cover_letter_template_<EN|FR>.docx`: the layout only (header block, date, addressee, subject, salutation, signature). Since 2026-11-17 its body holds bracketed instructions, one per paragraph, not a letter: replace each with the paragraph it describes, delete the ones the letter does not need, and leave no bracket behind (rule R21, checked by `cv_check.py`). The order and the content rules are those of §5.4 of the voice note, which wins over the brackets.

## Workflow

### Step 1: Learn from the CV he sent back

Run `asset-updater` in **returned-file mode** on the attached CV before drafting. It files
the CV in the application folder, sends every sentence Matt wrote or rewrote to
`Writing voice.md` §2, and logs the Recruiter edits he rejected. Then treat **his** file as
the CV of record. Where it differs from Claude's version, his version wins, including facts
he removed: a fact he cut from the CV does not come back in the letter.

### Step 2: Ask Matt for the hook (one round, before drafting)

The parts of a letter that most need to be his are why he wants this job and why this
company. Ask with `AskUserQuestion`, one round of 2 to 4 questions, each with concrete
options drawn from the JD, `company_overview.md` and the CV, and room for his own words:

| Ask about | Why |
|---|---|
| **Why this role**: what in the job itself draws him | Opening sentence (§5.4, question 1) |
| **Why this company**: which fact about them matters to him | The one sentence that must pass the swap test |
| **Which fact to lead with**: 2 or 3 candidate CV facts for the top JD requirements | Picks the evidence paragraphs |
| **The gap**, only if a JD requirement is not covered: how he would handle it | Gap paragraph (§5.4, question 4) |

Skip a question the tailoring memo or notes already answer and Matt confirmed. If he types a
sentence of his own, use it as close to verbatim as grammar allows, and add it to
`Writing voice.md` §2: it is his voice, unedited.

### Step 3: Plan the letter against §5.4

Before writing, list in a few lines:

- **Q1 Why this role:** the intent sentence, from his answer.
- **Q2 Why this company:** one fact only this employer would recognize, with its source (JD line or `company_overview.md`).
- **Q3 Applicable experience:** 2 or 3 JD needs, each with the CV fact that answers it, the employer it happened at, and at most two numbers. Each fact must be on the final CV or in `candidate_profile.md`, and within the ceilings.
- **Q4 Gap:** the uncovered requirement, the adjacent evidence, what he would do first. Omit the paragraph if there is no real gap; never invent one to look modest.
- **Q5 Situation:** current status and why this move, languages, location, availability.
- **Close.**

Keep this plan in `cover_letter_notes.md`. **It never goes to the reviewer (changed 2026-11-26):** `cover-letter-redteam` reads the letter with no knowledge of the plan, and you compare its report with the plan only after the report is in. A reviewer that knows what each paragraph was meant to do checks the letter against your intent, not against what a recruiter reads.

### Step 4: Draft

**Level framing (R18 and R19 of `cv_rules.md`; same treatment as the CV, Matt, 2026-11-16).** Use the role tag the CV was built with (`tailoring_notes.md`): `hands_on` when the role requires doing the work oneself, which covers individual-contributor and manager postings and most freelance missions; `leadership` when it is held through other people. The tag follows what the role requires, never the title or the contract type. For a `hands_on` role:

- **No scale figure in the first two paragraphs**: no headcount of 80+ or 110, no ~USD 40M P&L, no board or C-level. The opening starts from work he did, as §5.4 already requires.
- **At least one first-hand fact** among the two or three facts the letter selects: something he did himself (wrote, built, recovered), not something his organization delivered.
- **The level is addressed once, plainly**, where §5.4 asks for his situation: why he wants a role of this size, in one or two factual sentences drawn from his hook answers (Step 2). This is the one place a scale fact may appear, as context for the choice, never as a credential. If the hook answers do not cover it, ask him in Step 2: a recruiter reading a Global Director's letter for a manager job will ask, and a letter that does not answer leaves the question to work against him.
- No sentence that manages downward ("I would bring a director's perspective"). He applies for the job as posted.

For a `leadership` role, permanent or freelance, scale leads and is not deflated (R20).

- **Language:** the posting's language. Register per §5.4 frame (EN: "Dear <First name>,"; FR: "Bonjour <Prénom>," or "Bonjour,").
- **Length:** one page; EN about 300 to 380 words, FR about 180 to 250 unless the posting asks for more.
- **Voice:** as loaded by `general:writing-voice`: §2 corpus to imitate, §3 to avoid, §5.1 and §5.4 for structure. One interpretive sentence per selected fact at most, the rest factual.
- **Reference letters are not templates.** Read them for length, order and rhythm. Never reuse a sentence from them or from a letter to another employer, apart from the logistics line (languages, location, availability).
- **No sentence copied from the CV.** Same facts, different job: the CV lists, the letter says what the fact means for this employer.
- **Names:** recipient and company spelled exactly as in the JD or on the company's site.

Generate the `.docx` from `_assets/cover_letter_template_<LANG>.docx`, replacing text in place
to keep the layout. If the FR template does not exist yet, use the EN one, translate the
header labels, and after Matt finalizes his first French letter offer to save it as
`cover_letter_template_FR.docx`.

Save as `applications/<slug>/CORNET_<Company>_Cover_Letter_<YYYY-MM-DD>.docx` (EN) or
`CORNET_<Company>_Lettre_<YYYY-MM-DD>.docx` (FR), today's date. Never overwrite; `_v2`,
`_v3` if the name exists. **Never produce a PDF**; Matt makes his own from Word.

### Step 5: Self-check before the gate

Run the full §4 review test, points 1 to 9 (`general:writing-voice` Step 4, surface §5.4), then:

- Read the letter next to the final CV and any form answers: no twin sentences.
- Count words.
- Check each §5.4 question is answered, in order.
- French letter: run `python3 <resume-tailor skill dir>/scripts/fr_spaces.py <letter.docx> <letter.docx>` on the file you just wrote, so every space before `;` `:` `?` `!` and inside `« »` is non-breaking (R22).
- Run the mechanical check on the `.docx`: `python3 <resume-tailor skill dir>/scripts/cv_check.py <file> --rules <project>/_assets/cv_rules.md --profile <project>/_assets/candidate_profile.md --lang <fr or en> --kind letter --tags <tags>` (same tags as the CV, role tag included, see `resume-tailor` Step 4a). `0 FAIL` is required before the gate. A `WARN` on a ceiling word is expected when the letter names a gap; any other kept warning is listed in `cover_letter_notes.md` with its reason.

The self-check does not replace the red team. The drafter is the worst judge of its own tics.

### Step 6: Mandatory gate

Run `cover-letter-redteam` on the `.docx`. Do not show Matt the letter before it has been
through the gate.

### Step 7: Present to Matt

Deliver the redlined `.docx` (Recruiter tracked changes), `cl_redteam_notes.md` and
`cover_letter_notes.md`, each written to the application folder **and** surfaced as a file
card with `SendUserFile`. In chat: three lines (the angle, the red team's verdict, the one
thing to look at first) and the next step: finalize in Word and attach it back here.

Update `applications_tracker.md` through `application-tracker` (letter drafted).

### Step 8: Learn from the letter he sends back

When Matt attaches the letter he finalized, run `asset-updater` in returned-file mode. His
rewrites go verbatim to `Writing voice.md` §2 the same turn; the Recruiter edits he rejected go
to `cl_redteam_notes.md`; a change to the frame is proposed for the template and §5.4; and he is
asked whether this letter should replace the §5.4 reference letter for its language.

## Hard rules

- **Never invent** experience, metrics, employers, dates, motivations or company facts. A motivation he did not state is not written.
- **Every fact is on the final CV or in `candidate_profile.md`**, and within the ceilings in `Notes/Matt Cornet.md`. A fact he cut from the CV stays out.
- **The letter answers the §5.4 questions in order**: why this role, why this company, applicable experience, the gap if any, his situation, a one-line close.
- **Figures are worded as in the Current values table**, and the letter passes `cv_check.py --kind letter` before the red team. Until 2026-11-16 only the CV skills checked figures, so a duration or a count corrected in the log could still go out in a letter.
- **Level framing as on the CV.** Role that requires doing the work oneself (`hands_on`): no scale figure in the first two paragraphs, one first-hand fact, and the choice of level answered once.
- **Passes the swap test.** If it still works with a competitor's name, it is not finished.
- **No sentence from the CV, the reference letters, or another employer's letter.**
- **Voice rules come only from `Notes/Writing voice.md`, loaded through `general:writing-voice` in vault-required mode.** Never from `_assets/voice_matt.md` or `candidate_profile.md`, both stubs since 2026-09-10, and never from the short voice block in Matt's preferences.
- **No PDF, no em dash, no bold or bullets in the body.**
- **The red team is mandatory.** A letter that skipped it is a draft, and is presented as one.

## Edge cases

- **The posting asks form questions that duplicate the letter** ("Why do you want to join?"): the form field answers the question in its own words (resume-tailor Step 6). Read both side by side for twin sentences.
- **No recipient named:** EN "Dear Hiring Team,", FR "Bonjour,". Never "To whom it may concern" or "Madame, Monsieur".
- **Spontaneous application (no posting):** Q1 becomes what he would do there; Q2 and Q3 rest on `company_overview.md`; no gap paragraph.
- **Matt wants a letter without a tailored CV** (e.g. the posting takes the master CV): use `_assets/master_resume.docx` as the CV of record and say so.
