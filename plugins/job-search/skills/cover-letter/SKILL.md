---
name: cover-letter
description: "Writes Matt Cornet's cover letter for a specific role, in his voice and from his final CV, so it reads as written by him and not generated. Starts when Matt attaches the CV he finalized in Word after resume-redteam, or when he asks for a cover letter, lettre de motivation, or a letter to go with an application. Answers why this role, why this company, which experience applies, the gap, and his situation; learns from the CV he sends back; ends with the mandatory cover-letter-redteam gate."
---

# Cover Letter

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

1. *(vault)* `Notes/Writing voice.md`: §2 corpus, §3 banned constructions, §4 review test
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
7. *(project)* `_assets/candidate_profile.md`: ground truth, including the append-only Q&A log.
8. `applications/<slug>/notes.md` and any form answers already drafted (`form_answers*.md`),
   to avoid twin sentences.
9. *(project)* `_assets/cover_letter_template_<EN|FR>.docx`: the layout.

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

This plan is also the checklist the red team tests against. Keep it in `cover_letter_notes.md`.

### Step 4: Draft

- **Language:** the posting's language. Register per §5.4 frame (EN: "Dear <First name>,"; FR: "Bonjour <Prénom>," or "Bonjour,").
- **Length:** one page; EN about 300 to 380 words, FR about 180 to 250 unless the posting asks for more.
- **Voice:** §2 corpus to imitate, §3 to avoid, §5.1 and §5.4 for structure. One interpretive sentence per selected fact at most, the rest factual.
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

Run the full §4 review test, points 1 to 9, then:

- Read the letter next to the final CV and any form answers: no twin sentences.
- Count words.
- Check each §5.4 question is answered, in order.

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
- **Passes the swap test.** If it still works with a competitor's name, it is not finished.
- **No sentence from the CV, the reference letters, or another employer's letter.**
- **Voice rules come only from `Notes/Writing voice.md`.** Never from `_assets/voice_matt.md` or `candidate_profile.md`, both stubs since 2026-09-10.
- **No PDF, no em dash, no bold or bullets in the body.**
- **The red team is mandatory.** A letter that skipped it is a draft, and is presented as one.

## Edge cases

- **The posting asks form questions that duplicate the letter** ("Why do you want to join?"): the form field answers the question in its own words (resume-tailor Step 4b). Read both side by side for twin sentences.
- **No recipient named:** EN "Dear Hiring Team,", FR "Bonjour,". Never "To whom it may concern" or "Madame, Monsieur".
- **Spontaneous application (no posting):** Q1 becomes what he would do there; Q2 and Q3 rest on `company_overview.md`; no gap paragraph.
- **Matt wants a letter without a tailored CV** (e.g. the posting takes the master CV): use `_assets/master_resume.docx` as the CV of record and say so.
