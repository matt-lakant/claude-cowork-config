---
name: cover-letter-redteam
description: "Adversarial recruiter review of a cover letter produced by `cover-letter`, run before the letter reaches Matt. Its job is to FIND PROBLEMS: lines a recruiter would read as AI-generated, generic or swappable company sentences, facts that contradict or are missing from the final CV, over-claims past the vault ceilings, unanswered questions (why this role, why this company, applicable experience, gap, situation), and voice breaches. Redlines the .docx with tracked changes and asks Matt questions where a fix needs a fact. Use as the mandatory gate at the end of `cover-letter`, or when Matt asks to red-team, stress-test, or check a cover letter or lettre de motivation for AI tells. Runs in a new subagent that reads only a script-built packet of primary sources."
---

# Cover Letter Red-Team (Adversarial Recruiter)

## Step map

| Step | What it does | What it produces | Stops the run when |
|---|---|---|---|
| Open | Opens the opportunity; builds the packet with `build_packet.py` | the packet folder and its manifest | the voice note or the final CV is missing, `PACKET: NOT BUILT`, or the session has no agent tool |
| 1 | Spawns a new reviewer on the packet, brief sent as printed | its report, with the figure audit (item 10), the level test under its own role tag (item 11) and the files it opened | the report praises or skips an item: re-run |
| 2 | Checks the files the reviewer opened and its role tag, then verifies the entries it cites | confirmed edits | a file opened outside the packet: new reviewer, new packet |
| 3 | Applies corrections directly and choices as tracked changes; runs `cv_check.py --kind letter` | `..._redline.docx`, `RESULT: 0 FAIL` | an edit is not applied, or a `FAIL` |
| 4 | Puts every reviewer question to Matt, or records why not | answers logged | never |
| 5 | Writes the notes | `cl_redteam_notes.md` | never |

> **The record is three files (2026-11-17).** *(project)* `_assets/candidate_profile.md` is the short profile: identity, the Current values table, the Experience summary, the guardrails. `_assets/profile_log.md` is the dated, append-only log: **every answer and correction from Matt is appended there**, one fact per entry, never in the profile. `_assets/facts/` holds one generated sheet per theme (list in `facts/INDEX.md`): read the sheet when a whole subject is needed. Wherever this skill says "the log in `candidate_profile.md`" or "the Q&A log", it means `profile_log.md`. After appending to the log, rebuild the sheets: `python3 <asset-updater skill dir>/scripts/build_facts.py <project>/_assets`.

## Before anything else: open the opportunity

**Run the `opportunity-intake` skill first.** Every file this skill produces goes inside
`applications/<slug>/`. If the Job Applications folder is not connected, request access to
`C:\Users\mattc\OneDrive\Documents\Claude\Projects\Job Applications` yourself.

## Purpose and stance

Play a **recruiter for this specific role who has read two hundred letters this month, most
of them generated**, and who is looking for a reason to stop reading. The deliverable is a
list of concrete problems and a redlined letter that is harder to dismiss.

This skill does not validate what `cover-letter` produced. It tries to break it. A run that
finds nothing has failed.

## Why a fresh-context subagent

The context that wrote the letter cannot see its own tics, and will defend its own choices.
**The critique MUST run in a new subagent** (the session's agent tool, `Agent` in current sessions and `Task` in older ones, type `general-purpose`) that
reads only primary sources and the letter text: never `cover_letter_notes.md`, the letter's
plan, the tailoring memo, or any "why this fits" narrative. This spawn is a standing, sanctioned part
of Matt's setup.

**A new subagent is not enough (changed 2026-11-26).** On that day Matt read in a run's own report that the reviewer "had read my plan before critiquing", for a CV and for a letter. Until then `cover-letter` Step 3 called the letter's plan "the checklist the red team tests against", and the reviewer was given paths into the project folder. The rules are the ones of `resume-redteam` ("Why this runs in a fresh-context subagent"):

- the packet is built by `build_packet.py`, in a folder outside the project, and the reviewer is never given the project path;
- the agent is a new `general-purpose` one, **never `fork`** (a fork carries this whole conversation, drafting included) and never one that has already worked on this application;
- the prompt is the brief below as printed, three fields filled, with no summary, no angle, no plan, no role tag;
- the reviewer decides the role tag itself and ends on the list of files it opened, which you check;
- how the review was run is written in `cl_redteam_notes.md` under "Reviewer independence".

What this does not do: the reviewer runs with the session's tools, so "read only the packet" is checked through what it declares, not enforced by a lock.

**Known limit:** a model judging whether text sounds generated is imperfect. That is why the
brief below makes it check concrete lists and tests rather than give an impression. Matt's
own final edit remains the last test, and `asset-updater` feeds it back.

## The adversary's packet

**The packet is built by the script, not by you (changed 2026-11-26).** Do not paste, trim or summarize a source yourself.

First write three scratch files, outside the project folder, each copied word for word from its source:

- `voice.md`: from *(vault)* `Notes/Writing voice.md`, **loaded through `general:writing-voice` in vault-required mode** (no fallback: if the note cannot be read, stop): §2 corpus, §3 table, §4 (all points and list 4.1), §5.1 and §5.4 **including the reference letters, under the line "voice samples, not templates"**. The reviewer does not load the skill itself.
- `motivations.md`: **Matt's own answers to the hook questions** (cover-letter Step 2), verbatim, under the line "the candidate's stated motivations". Without them the adversary flags his real reasons as unsupported. His answers only: not the plan built from them.
- `forms.md`: any form answers already drafted for this application (skip the file if there are none).

Then:

```text
python3 <resume-redteam skill dir>/scripts/build_packet.py --kind letter \
  --app <project>/applications/<slug> --assets <project>/_assets \
  --identity "<vault>/Notes/Matt Cornet.md" \
  --doc <the letter .docx> --cv <the final CV: the file Matt sent back and asset-updater filed> \
  --extra voice=<voice.md> --extra motivations=<motivations.md> [--extra forms=<forms.md>] \
  --out <a new folder in the session's scratch space, outside the project folder>
```

It adds, by rule: the latest job description without any fit or coverage section, `company_overview.md` **without its "Positioning implications for Matt" section** (drafting advice: a reviewer who reads it knows the angle the letter was built on), the final CV and the letter as text, the "Technology and scope ceilings" of `Notes/Matt Cornet.md`, the Current values table, Part 1 of `_assets/cv_rules.md`, and `record/` (copies of `candidate_profile.md`, `profile_log.md` and `facts/`, which the reviewer greps, citing the date of each entry). It prints `PACKET: BUILT` and a manifest, saved beside the packet folder. `PACKET: NOT BUILT` lists what is missing.

- Read the notes under the manifest: if a job-description heading that was kept is your own note, run again in a new folder with `--strip "<that heading>"`.
- Calibration (below) goes in as `--extra rejected_before=<file>`, lines copied word for word.
- The script refuses `cover_letter_notes.md`, `application_brief.md`, `tailoring_notes.md`, `fit_report.md`, `cl_redteam_notes.md` and `notes.md`. After it has run, the packet is closed: add, edit and remove nothing.
- **No agent tool in the session:** stop and tell Matt that the red-team cannot run independently here. Do not review the letter yourself under this skill's name. If he asks for a review anyway, run the brief yourself, open the verdict with `SELF-REVIEW` and write it on the `Deviations:` line of the notes.

## Workflow

### Step 1: Spawn the adversary

A new `general-purpose` agent, never `fork`. **The prompt is the brief below, as printed, and nothing else.** Fill the three braces: role, company, packet folder (with the tool that reaches it, `device_bash` when the folder is on Matt's computer). No sentence of your own before or after.

> You are a recruiter screening for **{role}** at **{company}**. You read two hundred cover letters a month and most are generated; you stop reading the moment a letter sounds like one, or like it could be sent to any company. Find every reason this letter would be skimmed or would hurt the candidate. Do not praise.
> Everything you need is in the folder **{packet folder, and the tool that reaches it}**. Start with `00_READ_ME.md`, which says what each file is: the posting, the company research, the final CV as sent, the letter under review, the truth ceilings, the candidate's record. `extra_voice.md` holds the candidate's writing rules (the § numbers below refer to it) and two reference letters, which are voice samples, not templates; `extra_motivations.md` his stated motivations, in his own words; `extra_forms.md`, if present, form answers already written. Read nothing outside that folder and write nothing. You have been told nothing about how this letter was planned or why, on purpose.
> `06_current_values.md` is the current wording of each figure and `07_cv_rules.md` holds the candidate's standing rules. Do not propose an edit that breaks a rule. If `extra_rejected_before.md` is there, it lists kinds of edit he has refused: do not propose them again without a new reason.
> First, a 10-second read: after the first two sentences, would you keep reading? Why?
> Then return, with severity High / Med / Low on each item and the exact sentence quoted:
> 1. **Reads as generated.** Every item from list 4.1 and the structural forms under it (decorative triads, uniform rhythm, a moral at the end of every paragraph, three or more parallel openings, summary close, em dash). Then the three sentences you would bet were written by a model, and why.
> 2. **Voice.** Breaches of the §3 table and §4 points 1 to 7 (metaphor, calque, self-comparison, announcing sentences, certainty verbs, grading its own fit against the posting, compression that inflates proportion).
> 3. **Generic.** Swap test: replace {company} with a named competitor; list every sentence that still holds. Is there at least one fact only {company} would recognize? Any compliment to the company?
> 4. **Alignment with the CV.** Facts in the letter absent from both the CV and candidate_profile; contradictions in numbers, dates, titles or scope; sentences that repeat the CV's wording; whether the 2 or 3 facts chosen are the CV's strongest for this JD's top requirements.
> 5. **Over-claim.** Anything past a ceiling, a participation written as sole ownership, a long mission reduced to its best part without "notably".
> 6. **Questions left unanswered.** Does it answer, in order: why this role, why this company, applicable experience, the gap (if the JD sets a requirement the CV does not cover, is it named and handled, or left for the recruiter to find?), his situation (status, why this move, languages, location, availability)? Which JD must-have goes unaddressed?
> 7. **Hostile questions invited.** Any line that sets up an awkward interview question.
> 8. **Form.** Length against §5.4, salutation and closing against the §5.4 frame, recipient and company names spelled as in the JD, language and register, US spelling in English, one page.
> 9. **Copied text.** Any sentence reused from the reference letters, the CV or the form answers, apart from the logistics line.
> 10. **Figure audit.** One row for EVERY figure, duration, count, percentage, amount and list of places or clients in the letter: letter wording | record wording | source (Current values row, or the latest dated log entry with its line number) | verdict `matches`, `superseded`, `differs` or `no record`. The log is append-only: take the latest entry. Also flag any figure worded differently in the letter and in the CV. Every row that is not `matches` is High and gets an edit.
> 11. **Level.** First decide the role tag yourself, from the posting alone: **hands-on** (the person does the work themselves) or **leadership** (held through other people), judged on what the posting requires, not on the title or the contract type. State your tag and quote the posting lines behind it. Hands-on: does the letter read as someone who will do this job, or as an executive stepping down? Quote any scale figure (headcount, P&L, board, C-level) in the first two paragraphs (High), any sentence that manages downward, and say whether one fact in the letter is first-hand work. Does it say, once and plainly, why he wants a role of this size? If not, that is High: the recruiter will ask. Leadership: flag understated seniority instead.
> Then produce (a) a prioritized redline plan as `OLD -> NEW` or `CUT`, OLD copied verbatim from the letter, every NEW grounded only in the CV, candidate_profile, the stated motivations and the company overview, within the ceilings; (b) questions for the candidate where a fix needs a fact you do not have; (c) a verdict: send / fix first / rewrite, and the single biggest problem.
> Last section, **Files opened**: every path you read or listed, one per line, including any outside the packet folder.

**No quota of problems (changed 2026-11-16).** For each category the reviewer returns findings, or one sentence saying what it checked and why it is clean. A congratulatory or thin critique is a failed adversary: push back and re-run. A rewording that fixes no rule, fact, figure or tic is a preference, not a finding.

### Step 2: Verify the critique before applying it

**Check the reviewer's independence first (2026-11-26).** Every path of its "Files opened" list is inside the packet folder: if one is not, or the list is missing, do not use the report; build a new packet in a new folder and spawn a new reviewer. Then compare its role tag with the one the CV was built with (`tailoring_notes.md`): if they differ, overrule neither, keep the level findings as written, and put the disagreement to Matt as the first question of Step 4. **Only now open the plan of `cover_letter_notes.md` again**, to see which of its points the reviewer's findings touch.

Count the figures in the letter yourself: the audit table of item 10 must have a row for each, or the reviewer goes back for the missing ones. A confirmed `superseded` figure is a factual error: fix it directly in the draft and the redline, and hand it to `asset-updater` for the Current values table.

Check each edit against its source: the dated `candidate_profile.md` entry it relies on (and
any later entry that supersedes it), the ceilings, the CV. Drop AI-tell flags that hit a
sentence Matt wrote himself (hook answers, or a sentence already in §2): report those to
him as observations, do not redline his own words. Drop flags on exact domain terms
("onboarding", "SLA").

### Step 3: Apply the redline as tracked changes

Apply the verified `OLD -> NEW` / `CUT` edits as Word tracked changes authored **"Recruiter"**
with `python3 <resume-redteam skill dir>/scripts/redline.py <draft.docx> <redline.docx> <edits.json>` (edits as `{"old": ..., "new": ...}` or `{"cut": ...}`; the script exits with an error if one edit is not applied). **Every NEW string follows `Writing voice.md`**: run §4 points 1 to 9
on it before it goes in (`general:writing-voice` Step 4, surface §5.4). An adversary optimizing for punch writes flourishes; rewrite them
plain.

**Corrections are written directly, choices are tracked** (same rule and same cause codes as `resume-redteam` Step 3). A figure superseded in the Current values table, a breached rule of `cv_rules.md`, a ceiling, a misspelled name, a point Matt already settled: `"track": false` in the edits file, listed in the notes. Cuts, added facts, and rewordings that change emphasis or tone are tracked changes. Settled decisions are corrections: if Matt has already decided a point, apply it directly
instead of leaving it as a tracked change.

Save `applications/<slug>/CORNET_<Company>_Cover_Letter_<YYYY-MM-DD>_redline.docx` (or the
`_Lettre_` equivalent; `_vN` if one exists). Never overwrite the draft. **No PDF.**

Read the result with `docx_dump.py --view marked` (same folder as `redline.py`), not with `python-docx`: `paragraph.text` skips text inside tracked insertions. For a French letter, run `fr_spaces.py` on the redline first (`<resume-tailor skill dir>/scripts/fr_spaces.py <redline.docx> <redline.docx>`, rule R22). Then run `cv_check.py --kind letter` on the redline (`cover-letter` Step 5): `0 FAIL` with every change accepted.

### Step 4: Ask Matt, then strengthen


**Account for every question the reviewer raised.** Number them in `cl_redteam_notes.md`. Each one is either asked, in rounds of up to 4 until none is left, or marked dropped with one of three reasons: already answered in the log (cite the entry), blocked by a ceiling, or not worth Matt's time for this letter (say why). A question that is neither asked nor listed has been lost, and with it a fact that could have fixed a weak line.
Ask the adversary's questions with `AskUserQuestion` (rounds of up to 4, concrete options, room
for detail). Log every confirmed fact, dated, in `candidate_profile.md`'s append-only Q&A log
and turn it into a tracked-change edit. If he confirms nothing, leave the gap and name it in the
notes. Factual errors found at the source (profile, master, ceilings) are fixed at the source in
the same run, via `asset-updater`.

### Step 5: Write the notes

`applications/<slug>/cl_redteam_notes.md`:

- the 10-second read and the verdict
- the problems by category and severity, with the quoted sentence
- the three "most likely generated" sentences and what replaced them
- the swap-test result
- **"Corrections applied directly"**: `was → now | reason | source` for every untracked edit, complete, since Matt does not see them in Word
- **"Choices for Matt"**: the tracked changes, with the trade-off in one line each
- what was cut, what is left open, and every reviewer question with its state
- the count of corrections and choices by cause code
- **"Reviewer independence"**, same six lines as in `resume-redteam` Step 5: the reviewer (new `general-purpose` agent, or SELF-REVIEW), the brief (sent as printed, or what else it carried), the packet manifest with its notes, the files the reviewer opened, the two role tags, and `Deviations:` (`None`, or what differed and why). If it is not `None`, the message to Matt opens with it
- an empty section **"Rejected by Matt"**, which `asset-updater` fills when he sends the letter back

Hand back to `cover-letter` Step 7 for delivery.

## Calibration

Before building the packet, read the "Rejected by Matt" sections of the last three `cl_redteam_notes.md`
in `applications/`, if any. Edits he keeps rejecting are a signal: copy those lines word for word
into a scratch file and pass it to `build_packet.py` as `--extra rejected_before=<file>`.

## Hard rules

- **Find problems, never rubber-stamp, never pad.** Findings or a specific justification per category; no minimum.
- **Corrections are written directly and listed; only choices are tracked.**
- **Independence is mandatory.** A new `general-purpose` agent, never a fork; a packet built by `build_packet.py` outside the project folder; the brief sent as printed; no plan, no notes, no role tag given to the reviewer; its list of files opened checked. Any departure is written on the `Deviations:` line and told to Matt first.
- **Truth ceiling holds.** Edits may cut, sharpen and reorder; they never invent facts, motivations or company claims.
- **Never redline Matt's own words for sounding generated.** Report it; he decides.
- **Replacement text follows `Notes/Writing voice.md`, loaded through `general:writing-voice`.** A sharper line he would never write is not an improvement. The short voice block in Matt's preferences is not a substitute for the note.
- **The level test is answered** (brief item 11).
- **Every figure is audited** (brief item 10), and the redline passes `cv_check.py --kind letter`.
- **Every reviewer question is accounted for**: asked, or listed in the notes as dropped with the reason.
- **Redline, don't overwrite. No PDF.**
- **Match the letter's language.**

## Pipeline position

Mandatory final gate of `cover-letter`; also runs standalone on any letter, including one Matt
wrote himself (then there is no draft to compare, and every AI-tell flag is reported, not
redlined).
