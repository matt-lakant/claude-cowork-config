---
name: cover-letter-redteam
description: "Adversarial recruiter review of a cover letter produced by `cover-letter`, run before the letter reaches Matt. Its job is to FIND PROBLEMS: lines a recruiter would read as AI-generated, generic or swappable company sentences, facts that contradict or are missing from the final CV, over-claims past the vault ceilings, unanswered questions (why this role, why this company, applicable experience, gap, situation), and voice breaches. Redlines the .docx with tracked changes and asks Matt questions where a fix needs a fact. Use as the mandatory gate at the end of `cover-letter`, or when Matt asks to red-team, stress-test, or check a cover letter or lettre de motivation for AI tells. Runs in a fresh-context subagent."
---

# Cover Letter Red-Team (Adversarial Recruiter)

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
**The critique MUST run in a fresh-context subagent** (`Task` tool, `general-purpose`) that
receives only primary sources and the letter text: never `cover_letter_notes.md`, the
tailoring memo, or any "why this fits" narrative. This spawn is a standing, sanctioned part
of Matt's setup.

**Known limit:** a model judging whether text sounds generated is imperfect. That is why the
brief below makes it check concrete lists and tests rather than give an impression. Matt's
own final edit remains the last test, and `asset-updater` feeds it back.

## The adversary's packet

1. `applications/<slug>/job_description.md` (most recent dated copy if several).
2. `applications/<slug>/company_overview.md`.
3. **The final CV**: the file Matt sent back and `asset-updater` filed (`..._final.docx` or the most recent Matt-returned CV), as text.
4. *(project)* `_assets/candidate_profile.md`: ground truth. Tell the subagent the Q&A log is append-only and a later entry can supersede an earlier one.
5. *(vault)* `Notes/Matt Cornet.md`, "Technology and scope ceilings" section only.
6. *(vault)* `Notes/Writing voice.md`: §2 corpus, §3 table, §4 (all points and list 4.1), §5.1 and §5.4 **including the reference letters, labelled "voice samples, not templates"**.
7. **Matt's own answers to the hook questions** (cover-letter Step 2), verbatim, labelled as the candidate's stated motivations. Without them the adversary flags his real reasons as unsupported.
8. Any form answers already drafted for this application.
9. The letter text.

Leave out `cover_letter_notes.md`, `tailoring_notes.md` and any fit matrix inside the JD file.

## Workflow

### Step 1: Spawn the adversary

Brief (fill the braces):

> You are a recruiter screening for **{role}** at **{company}**. You read two hundred cover letters a month and most are generated; you stop reading the moment a letter sounds like one, or like it could be sent to any company. Find every reason this letter would be skimmed or would hurt the candidate. Do not praise.
> Inputs: [JD] / [company overview] / [final CV, the version actually sent] / [candidate_profile as ground truth] / [ceilings as the hard truth limit] / [Writing voice rules and the two reference letters, which are voice samples, not templates] / [candidate's stated motivations] / [form answers] / [the letter].
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
> Then produce (a) a prioritized redline plan as `OLD -> NEW` or `CUT`, OLD copied verbatim from the letter, every NEW grounded only in the CV, candidate_profile, the stated motivations and the company overview, within the ceilings; (b) questions for the candidate where a fix needs a fact you do not have; (c) a verdict: send / fix first / rewrite, and the single biggest problem.

Require at least **3 substantive problems**, or a specific justification per category for why
it is clean. A congratulatory or thin critique is a failed adversary: push back and re-run.

### Step 2: Verify the critique before applying it

Check each edit against its source: the dated `candidate_profile.md` entry it relies on (and
any later entry that supersedes it), the ceilings, the CV. Drop AI-tell flags that hit a
sentence Matt wrote himself (hook answers, or a sentence already in §2): report those to
him as observations, do not redline his own words. Drop flags on exact domain terms
("onboarding", "SLA").

### Step 3: Apply the redline as tracked changes

Apply the verified `OLD -> NEW` / `CUT` edits as Word tracked changes authored **"Recruiter"**
(see the `docx` skill). **Every NEW string follows `Writing voice.md`**: run §4 points 1 to 9
on it before it goes in. An adversary optimizing for punch writes flourishes; rewrite them
plain.

Settled decisions are not proposals: if Matt has already decided a point, apply it directly
instead of leaving it as a tracked change.

Save `applications/<slug>/CORNET_<Company>_Cover_Letter_<YYYY-MM-DD>_redline.docx` (or the
`_Lettre_` equivalent; `_vN` if one exists). Never overwrite the draft. **No PDF.**

Tracked-change traps, as in `resume-redteam`: runs inside `w:ins` are invisible to
`python-docx`'s `paragraph.runs`, so later passes must walk `w:t` nodes; a run carrying
`<w:br/>` loses its line break if rebuilt carelessly.

### Step 4: Ask Matt, then strengthen

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
- what was redlined, what was cut, what is left open
- an empty section **"Rejected by Matt"**, which `asset-updater` fills when he sends the letter back

Hand back to `cover-letter` Step 7 for delivery.

## Calibration

Before spawning, read the "Rejected by Matt" sections of the last three `cl_redteam_notes.md`
in `applications/`, if any. Edits he keeps rejecting are a signal: tell the adversary which
kinds of edit he has rejected before, and do not propose them again without a new reason.

## Hard rules

- **Find problems, never rubber-stamp.** At least 3 substantive issues, or a justification per category.
- **Independence is mandatory.** No drafting rationale in the packet.
- **Truth ceiling holds.** Edits may cut, sharpen and reorder; they never invent facts, motivations or company claims.
- **Never redline Matt's own words for sounding generated.** Report it; he decides.
- **Replacement text follows `Notes/Writing voice.md`.** A sharper line he would never write is not an improvement.
- **Redline, don't overwrite. No PDF.**
- **Match the letter's language.**

## Pipeline position

Mandatory final gate of `cover-letter`; also runs standalone on any letter, including one Matt
wrote himself (then there is no draft to compare, and every AI-tell flag is reported, not
redlined).
