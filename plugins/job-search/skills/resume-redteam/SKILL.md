---
name: resume-redteam
description: "Adversarial recruiter review of a resume produced by `resume-tailor`, run before the file reaches Matt. Its job is to FIND PROBLEMS, not validate. It re-reads the job description, company_overview.md, and candidate_profile.md, then attacks the tailored resume for what is weakest, vaguest, removable, missing, or over-claimed, redlines it with tracked changes, and asks Matt questions where a fix needs a fact it does not have. Use as the mandatory gate at the end of `resume-tailor`, or on demand when Matt says \"red-team\", \"adversarial review\", \"poke holes\", \"stress-test my resume\", \"have a recruiter tear it apart\", or \"what's weak here\". The critique runs in a fresh-context subagent so it never sees the drafting rationale."
---

# Resume Red-Team (Adversarial Recruiter)

## Step map

Run the steps in this order. Steps 0 and 6 are gates.

| Step | What it does | What it produces | Stops the run when |
|---|---|---|---|
| 0 | Opens the opportunity, runs the draft gate, reads past rejections | `GATE draft: PASS` | the gate lists a missing item: go back to `resume-tailor` (standalone run on an older CV: see Step 0) |
| 1 | Assembles the reviewer's packet from primary sources | the brief for the subagent | the vault or the project folder cannot be read |
| 2 | Spawns the fresh-context reviewer | its report: 7 categories, figure audit, redline plan, questions | the report praises, or skips a category: re-run |
| 2b | Verifies the entries the reviewer cites | confirmed edits | never |
| 3 | Sorts edits into corrections and choices, applies them, checks the result | `CORNET_..._redline.docx`, `RESULT: 0 FAIL` | `redline.py` names an unapplied edit, or `cv_check.py` fails |
| 4 | Puts every reviewer question to Matt, or records why not | answers logged, edits added | never (unattended: questions listed as open) |
| 5 | Writes the memo, feeds the lessons file | `redteam_notes.md`, lines in `redteam_lessons.md` | never |
| 6 | Runs the red-team gate, presents to Matt | `GATE redteam: PASS`, file cards | the gate lists a missing item |

## Step 0: Open the opportunity and run the draft gate

**Run the `opportunity-intake` skill first.** It confirms the opportunity name, resolves
the kebab-case slug, creates `applications/<slug>/` if it does not already exist, and
starts the opportunity's `notes.md`. Every file this skill produces goes inside that
folder.

Do not write anything before the folder exists. If the slug is unknown, ask. If the
Job Applications project folder is not connected, stop and say so — never fall back to
the project root, to another connected folder, or to chat-only delivery.

Then check that the drafting stage left what this skill needs:

```text
python3 <application-brief skill dir>/scripts/gate.py draft <project>/applications/<slug>
```

- `GATE draft: PASS`: continue.
- Items missing on a CV drafted in this pipeline: go back to `resume-tailor` and complete them. A red-team run on a draft whose evidence and decisions were never matched to CV lines produces the heavy redline this pipeline exists to avoid.
- **Standalone run on a CV that predates the brief** (no `application_brief.md` in the folder): say so in one line, continue without the gate, decide the role tag yourself from the posting (what the role requires: `hands_on` or `leadership`), and write it at the top of the memo.

Read the role tag, the cv_check tags, the top-third keywords and the first-hand facts from `application_brief.md`: Step 3 passes them to `cv_check.py`, and brief item 7 needs the tag. **Nothing else from that file goes anywhere near the reviewer.**

Read the "Rejected by Matt" section of the last three `redteam_notes.md` files in `applications/`, if any. Edits he keeps rejecting are a calibration signal: do not propose the same kind of edit again without a new reason.

> Paths marked *(project)* are relative to the **Job Applications project root** — the folder that holds `applications/`, `_assets/` and `applications_tracker.md`. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications"). Paths marked *(vault)* are relative to the connected `obsidian-vault` folder.

> **Voice reference moved, 2026-09-10.** Replacement text is governed by *(vault)* `Notes/Writing voice.md`: §2 corpus, §3 banned constructions, §4 review test, §5.2 resume surface. Run `ls $HOME/mnt/` and check for `obsidian-vault`; if it is not connected, ask Matt to connect `C:\Users\mattc\Obsidian\obsidian-vault` before writing any replacement string. `_assets/voice_matt.md` and the "Voice & style guidelines" section of `candidate_profile.md` are stubs — never read them as rules, never write to them.

## Purpose & stance

Play a **skeptical hiring manager / senior recruiter for this specific role** who screens hundreds of applications and is looking for reasons to **reject**. The deliverable is not reassurance — it is a list of concrete problems and a redlined resume that is harder to screen out.

**This skill does not validate the resume `resume-tailor` produced. It tries to break it.** If it finishes a run without surfacing real problems, it has failed.

## Why this runs in a fresh-context subagent

If the same context that wrote (or just read the rationale for) the resume also critiques it, it will defend its own choices. To stay genuinely adversarial, **the critique MUST run in a fresh-context subagent** (the session's agent tool, named `Agent` in current sessions and `Task` in older ones) that is handed only the primary sources and the resume text — never the tailoring rationale, the fit memo, or "why this is a good fit" framing. This subagent spawn is an explicit, standing part of Matt's setup; it is sanctioned even though agents are not spawned by default.

## Source materials (the subagent reads these, not Claude's prior work)

1. The job description: `applications/<slug>/job_description.md` (the most recent `job_description_<YYYY-MM-DD>.md` if dated copies exist). Only if no `.md` exists, fall back to the posting PDF (`*_JobPost_*.pdf`, or `job_description.pdf` in older folders), and tell Matt the `.md` is missing so `opportunity-intake` Step 3b can create it.
2. `applications/<slug>/company_overview.md` — what the company actually wants and screens for. **Without its "Positioning implications for Matt" section**: that section is drafting advice written for the tailoring step, and a reviewer who reads it knows the angle the CV was built on. Cut from that heading (or bold label, in older files) to the next heading or to "Sources".
3. *(project)* `_assets/candidate_profile.md` — the **ground truth** of what Matt has really done, including the append-only Q&A log. Used to tell "unsupported claim" apart from "under-sold real experience."
4. *(vault)* `Notes/Matt Cornet.md` — the **"Technology and scope ceilings" section is the truth ceiling**. Any resume line that exceeds a ceiling is a High-severity credibility risk, not a matter of taste. Include this section in the subagent's packet.
5. The tailored resume `.docx` produced by `resume-tailor` (extract its text).
6. *(project)* the **"Current values" table at the top of `_assets/candidate_profile.md`** — the current wording of each figure. The reviewer audits every printed figure against it (brief item 6).
7. *(project)* `_assets/cv_rules.md` — Matt's standing CV rules. Part 1 goes into the brief as constraints, so the reviewer does not spend edits on proposals Matt has already refused.

Claude (not the subagent) also reads *(vault)* `Notes/Writing voice.md` before writing any replacement text in Step 3. For a CV redline, the **CV mode** of `general:writing-voice` is enough (§1, §3, §4 with 4.1, §5.2).

## Workflow

### Step 1 — Assemble the adversary's packet
**Build the packet from text, not from memory of the drafting.**

- **Resume text:** `python3 <this skill's dir>/scripts/docx_dump.py <cv.docx>` prints the body in document order, tables included (the skills matrix and the role titles live in tables, and `python-docx`'s `paragraph.text` misses both them and any tracked insertion). Paste that output.
- **Pasted in full:** the JD, `company_overview.md` minus its positioning section, the "Framing guardrails" and "Technology and scope ceilings" sections of `Notes/Matt Cornet.md`, the Current values table, and Part 1 of `_assets/cv_rules.md`.
- **Given as a path, not pasted:** `_assets/candidate_profile.md`. It is several hundred kilobytes and no longer fits in a brief. Tell the reviewer to read the top of the file through the Experience section in full, then to grep the append-only log for each claim it checks, citing the date and line of each entry, and to take the latest entry when two disagree. Tell it which tool reaches the file (`device_bash` when the project folder is on Matt's computer) and that it must not write anything.
- **Named as off-limits:** `application_brief.md`, `tailoring_notes.md`, `fit_report.md`, `redteam_notes.md`, any other CV or redline in the folder, and any other application folder. Say so explicitly in the brief: a reviewer that can read the folder will otherwise open them.

Do **not** include the fit score, the tailoring memo, or any "this is why it fits" narrative. If the JD file carries an internal coverage or fit matrix, tell the subagent explicitly to ignore that section — it is your own note, not a primary source, and it leaks the drafting rationale into the adversary's packet.

### Step 2 — Spawn the adversarial subagent
Use the session's agent tool (`Agent`; `Task` in older sessions), subagent type `general-purpose`, and wait for its report before doing anything else on the CV. Give it this brief (fill the braces):

> You are a skeptical hiring manager screening for **{role}** at **{company}**. You reject most resumes in 6 seconds. Your job is to find every reason this candidate would NOT make the shortlist — do not praise, do not validate.
> Inputs: [paste JD] / [paste company_overview.md without its positioning section] / [path of candidate_profile.md, the ground truth, with how to read it] / [paste the Framing guardrails and the Technology and scope ceilings sections as the hard truth ceiling] / [paste the tailored resume text from docx_dump.py] / [list of files it must not open].
> Also given: the Current values table (current wording of each figure) and the candidate's standing CV rules. Treat the rules as constraints: do not propose an edit that breaks one.
> Do two reads: (1) a 6-second skim — does the top third earn a deep read for THIS role? (2) a deep read against every JD requirement.
> Return, with severity (High/Med/Low) on each item:
> 1. **Weakest bullets** — limp, generic, or low-signal lines that waste prime space.
> 2. **Vague / filler** — unquantified claims, buzzwords, hedges, anything a skeptic would not believe without proof.
> 3. **Removable** — lines that add nothing for THIS JD and should be cut to tighten the read.
> 4. **Missing** — JD must-haves, company-overview signals, and ATS keywords absent or buried; note which are likely real-but-undocumented (check candidate_profile) vs genuine gaps vs blocked by a stated ceiling.
> 5. **Credibility risks** — over-claims, unsupported scope/scale, seniority mismatch, any line that breaches a ceiling, or anything that invites a hostile interview question.
> 6. **Figure audit** — a table with one row for EVERY figure, duration, count, percentage, amount and list of places or clients printed on the resume (the same figure printed twice gets one row with both locations). Columns: resume wording | record wording | source (the Current values row, or the log entry with its date and line number) | verdict: `matches`, `superseded` (a later entry changes it: quote that entry), `differs` (scope, period, unit or attribution is not what the record says), or `no record`. Read the Current values table first. For a figure with no row there, grep the log and take the LATEST dated entry, because the log is append-only and a later entry can annul an earlier one. A place or client list counts as a figure: check that each item is attributed to the right client and period. Every `superseded`, `differs` and `no record` row is a High-severity credibility risk and gets an edit in the redline plan.
> 7. **Level and distance from the work.** The role is **{hands-on: the person does the work themselves | leadership: the role is held through other people}** (judged on what the posting requires, not on the title, and not on whether it is a permanent job or a freelance mission). For a hands-on role, answer first: would this person still do the work themselves next month, and which lines above the skills matrix prove it? Quote them; fewer than two first-hand facts there is High. Then quote every line that reads as executive distance: scale (headcount, P&L, board, C-level, SVP), delegation ("through regional directors", "oversaw", "sponsored", "governed"), or a first bullet of a role that opens on scale. Each is High above the matrix and Med elsewhere; for each, give the `OLD → NEW` that moves the scale to the Context line or replaces the verb with what he did, using only facts on record. Do not propose changing a job title. For a leadership role the test is reversed: flag any place where seniority was understated. If you think the role was tagged wrongly, say so and why.
> Then produce: (a) a prioritized **redline plan** as specific `OLD → NEW` text edits (or `CUT`), each grounded only in facts present in candidate_profile and within the ceilings — never invent. Copy the `OLD` text verbatim from the resume so each edit can be applied automatically. (b) a short list of **questions for the candidate** where a line could be stronger but you lack the fact to fix it.
> End with a one-line verdict: shortlist / borderline / reject, and the single biggest thing holding it back.

**The figure audit must be complete.** Count the figures in the resume text yourself before reading the report; if the audit table has fewer rows, send the reviewer back for the missing ones. On 2026-11-16 a reviewer without this item verified twenty claims it chose itself and missed two errors it had not picked: an EBITDA duration superseded six days earlier, and a four-country footprint attributed to a client present in one country.

**No quota of problems or edits (changed 2026-11-16).** The earlier rule, at least 5 problems, guaranteed a long redline whatever the draft was worth. What is required instead: for each of the seven categories, either findings or one sentence saying what was checked and why it is clean, naming the lines or requirements looked at. A report with no High finding must list the three strongest attacks the reviewer tried and why each failed. A report that praises, or declares a category clean without saying what it checked, is a failed adversary: push back and re-run. Tell the reviewer not to propose a rewording that fixes nothing (no rule, no fact, no figure, no cut of at least a line): a preference is not a finding.

### Step 2b — Verify the critique before acting on it

The subagent argues from dated entries in `candidate_profile.md` and from the vault ceilings. **Check that the entries behind the edits you are about to apply actually say what it claims.** One grep on the dates it cites is enough. Watch for superseded entries in particular: the log is append-only, so a later entry can annul an earlier one, and an adversary reading only the earlier one will produce a confident, wrong edit. This check is what separates a redline Matt can trust from one he has to audit himself.

**Check the figure audit the same way.** For each `superseded`, `differs` or `no record` row, open the cited entry and confirm it before applying the edit. A confirmed `superseded` row is a factual error: fix it directly in both files (it is not a proposal), and hand the figure to `asset-updater` so the Current values row is added or corrected in the same run.

### Step 3 — Apply the redline as tracked changes
**Sort every verified edit into a correction or a choice before applying anything (changed 2026-11-16).** Until then every edit was a tracked change, so Matt arbitrated thirty-odd marks per CV, most of which were not his to decide.

- **Correction: written straight into the text, not tracked.** The draft was wrong against something already settled: a figure or wording superseded in the Current values table or the log, a fact that contradicts the record, a rule of `cv_rules.md` (title wording, the 90% reference, level framing R18 when it only moves a scale marker to the Context line, a job-title keyword missing from the top third and added inside a sentence that stays true), a ceiling, a decision of the decisions table that was not applied, a point Matt already settled, a typo. There is one right answer and Matt has already given it.
- **Choice: tracked change authored "Recruiter".** Anything with a trade-off that is his: cutting a line or a bullet, adding a fact or a bullet (even one on record: it changes emphasis and length), rewording that changes the strength or the emphasis of a claim, reordering, and any new wording built on an answer he just gave.
- When in doubt, it is a choice.

Give each edit a cause code for the memo (Step 5):

| Code | Cause | Where it should have been caught |
|---|---|---|
| A | A fact already on record was not used | `application-brief` Step 3, then `resume-tailor` Step 5.2 |
| B | A fact Matt gave only after the draft (late question) | `application-brief` Step 5, reviewer's questions asked first |
| C | Figure, wording or rule error against the Current values table, `cv_rules.md` or a ceiling | `cv_check.py`, `resume-tailor` Step 5.1 |
| D | Level: reads too senior or not hands-on (or the reverse for a leadership role) | `resume-tailor` Step 3.1, level framing |
| E | A decision of the decisions table was not applied | `application-brief` Step 6, then `resume-tailor` Step 5.3 |
| F | Cut or tightening | drafting |
| G | Wording preference with no rule behind it | not an error: should be rare |

Write the edits to a JSON file, corrections with `"track": false`, and apply them with the script shipped in this skill:

```text
python3 <this skill's dir>/scripts/redline.py <draft.docx> <redline.docx> <edits.json>
```

`edits.json` is a list of `{"old": "<verbatim text>", "new": "<replacement>"}` (an empty `new` deletes) and `{"cut": "<first words of the paragraph>"}` for a whole paragraph; add `"track": false` to a correction. The output is one file: corrections already in the text, choices as tracked changes. The script writes Word tracked changes authored **"Recruiter"**, so Matt can accept or reject each one, handles an `OLD` that spans several runs, and **exits with an error naming every edit it could not apply**. Fix those edits (usually an `OLD` that is not verbatim, or one that overlaps an earlier edit: merge the two into one) and run again until all are applied. Copy `OLD` strings from the `docx_dump.py` output, never from the reviewer's report, which may have normalized quotes or spaces. Read the result with `docx_dump.py <redline.docx> --view marked`.

Do not write a tracked-changes script of your own: until 2026-11-16 each run did, and it was the most error-prone step of the pipeline (insertions invisible to `paragraph.runs`, header line breaks lost, edits skipped without notice).

Apply only edits grounded in `candidate_profile.md` and within the vault ceilings; hold back any edit that would require an unconfirmed fact and route it to Step 4 instead.

**Every `NEW` string lands in Matt's resume, so it follows *(vault)* `Notes/Writing voice.md`** — no metaphor, no calque of an English idiom, no self-definition against an implied lesser candidate, no sentence announcing what the next one will do, and §5.2's resume rules on top. An adversary optimizing for punch will happily write a flourish; run the §4 review test over every `NEW` string and rewrite it plain before it goes in the file.

Save a redline copy — never overwrite the tailored file: `applications/<slug>/CORNET_<...>_redline.docx` (or `_vN` if a redline already exists). Office files are versioned, never edited in place.

**Never produce a PDF.** Matt makes his own PDF from Word, after he has validated and reformatted the `.docx`. Do not save a `.pdf` beside the `.docx`, do not attach one, and do not offer one. If you need a PDF to check pagination, convert into a temp directory **outside** the project folder (e.g. `$HOME/tmp`), read the page count there, and leave nothing behind. A `.pdf` in an application folder is a stale copy of a document that is about to change, and on Matt's machine a session cannot delete files, so it becomes his cleanup.

**Two mechanical traps in tracked changes**, both worth knowing before writing the script:
- Runs living inside `<w:ins>` are not direct children of the paragraph, so `python-docx`'s `paragraph.runs` will not see them. Any later text pass over the file must walk `w:t` nodes at the XML level, or it will silently skip everything you inserted.
- A header run often carries a `<w:br/>`. Replacing that run drops the line break and welds two lines into one. Preserve the break when rebuilding the run.

**Decisions Matt has already made are corrections, not proposals.** If he has settled a point — in this session, in `cv_rules.md` or in a logged preference — it goes in with `"track": false` and is listed in the memo. Every settled item left as a tracked change is one more click of noise.

**Run `cv_check.py` on the redline before presenting it** (`resume-tailor` Step 5.1: same script, same tags including the role tag (`hands_on` or `leadership`), same `--top-keywords` and `--hands-on`, all read from the brief; the redline keeps the page size of the draft, which must be A4). It reads the file with every tracked change accepted, so it tests the CV Matt gets if he accepts everything. A `NEW` string can break a rule the draft respected: `0 FAIL` is required here too.

### Step 4 — Question Matt, then strengthen
**Account for every question the reviewer raised.** Number them in `redteam_notes.md` under "Questions". Each one ends in exactly one state:

- **asked**: put to Matt with `AskUserQuestion`, in rounds of up to 4 (grounded, one-click options, room to add detail), **until none is left**. The reviewer may return eight; the tool takes four per call, so that is two rounds, not a selection of four;
- **dropped**, with the reason written next to it: already answered in the log (cite the entry and apply it), blocked by a ceiling, or not worth Matt's time for this posting (say why).

On 2026-11-16 one run asked 4 of the reviewer's 8 questions and another asked none, and nothing recorded what happened to the rest. A question that is neither asked nor listed is a fact that could have fixed a weak line and was lost. If Matt is not there to answer (unattended run), list the questions as open in the memo and in your closing message instead of dropping them.

For every answer:
- Append it (dated) to the `## Confirmed details from tailoring Q&A (append-only log)` in `candidate_profile.md` (standing rule), and promote durable items via `asset-updater`.
- Convert "under-sold real experience" flags into real, specific tracked-change edits. Never invent — if Matt confirms nothing, leave the gap and name it in the memo.
- **If a finding is a factual error rather than a weakness** — a certification he does not hold, a guardrail decided but never applied — fix it at the source in the same run: *(project)* `_assets/candidate_profile.md`, *(project)* `_assets/master_resume.docx`, and *(vault)* `Notes/Matt Cornet.md` when it is a ceiling, not only the CV in hand. Otherwise it returns on the next tailoring run.
- **If an answer moves a ceiling** — he has in fact done the thing a ceiling said he had not — update the ceilings section in the same run and note which log entry it supersedes. A stale ceiling silently under-sells him on every future application.
- **If an answer sets or changes a figure or its wording**, the Current values table is updated in the same run through `asset-updater`: new wording in "Print as", old wording in "Never print", today's date in "Since". The log entry alone does not stop the old wording from coming back.
- **If Matt rewrites one of the redline strings**, add his version verbatim to §2 of *(vault)* `Notes/Writing voice.md` in the same turn.

### Step 5 — Present to Matt
Save the critique memo `applications/<slug>/redteam_notes.md`. **The six headings below are read by the gate: keep them exactly, in English.** The content follows the posting's language.

```markdown
# Red-team notes: <Company>, <Role>

Role tag: <hands_on | leadership>

## Verdict
<shortlist / borderline / reject, and the biggest blocker>

## Corrections applied directly
| Was | Now | Reason | Source | Cause |
|---|---|---|---|---|
<every untracked edit. Matt does not see these in Word: this table is how he checks them, so it must be complete. He can reverse any of them by saying so. "None" if there is none.>

## Choices for Matt
| # | Tracked change | Severity | Trade-off, in one line | Cause |
|---|---|---|---|---|

## Not applied
<the problems the reviewer raised that were not applied, and why>

## Questions
| # | Question | State | Answer or reason |
|---|---|---|---|
<State is `asked`, `dropped: <reason>` or `open`. "None" if the reviewer raised none.>

## First-pass count
<N corrections, M choices; then the count by cause code A to G>
<when there are more than 10 choices, or any cause A, B, C or E: one line naming the step of application-brief or resume-tailor that should have caught it>

## Rejected by Matt
<left empty; asset-updater fills it when Matt returns the file>
```

**Feed the lessons file.** Append to *(project)* `_assets/redteam_lessons.md` one line per finding of cause A, B, D or E (create the file with its heading if missing): `- <YYYY-MM-DD> | <role family> | <cause code> | <what the first pass missed, in one sentence that the next drafting run can act on>`. Do not append causes C, F or G: the check script covers C, and F and G teach nothing. `application-brief` Step 4 reads this file; it is how a finding stops recurring.

### Step 6 — Gate, then present

```text
python3 <application-brief skill dir>/scripts/gate.py redteam <project>/applications/<slug>
```

Complete whatever it lists until it prints `GATE redteam: PASS`.

Present the **redlined `.docx`** and the memo, each as a file card. Open the summary with the count ("6 corrections applied, 4 choices for you"), then the most important attacks in 3 lines. Do not paste the full resume into chat.

## Hard rules

- **Files for an opportunity live in `applications/<slug>/`, never at the project root.** The rule and its exceptions are in `opportunity-intake` (Hard rules), which wins on any conflict.
- **Find problems — never rubber-stamp, and never pad.** Each category has findings or a specific statement of what was checked. No minimum number of problems or edits.
- **Corrections are written directly, choices are tracked.** Every correction is listed in the memo; the redline holds only what Matt has to decide.
- **Every edit carries a cause code**, and causes A, B, D and E go to `_assets/redteam_lessons.md`.
- **Independence is mandatory.** The critique runs in a fresh-context subagent; do not let prior drafting rationale leak into its packet.
- **The level test is answered every time** (brief item 7). On a role that requires doing the work oneself, "too senior, not hands-on" is the rejection Matt fears most, and the one both reviewers of 2026-11-16 reached.
- **Every printed figure is audited.** Brief item 6 is not optional and not a sample: one row per figure, checked against the Current values table or the latest dated log entry.
- **Truth ceiling holds.** Tracked-change edits may cut, sharpen, and reorder freely, but must not invent experience, metrics, employers, dates, or certifications, and must not breach the ceilings in `Notes/Matt Cornet.md`. Under-selling becomes a question, not a fabrication. Respect the accuracy guardrails in `candidate_profile.md`.
- **Replacement text follows `Notes/Writing voice.md`.** A sharper line that Matt would never say is not an improvement.
- **Never read voice rules from `_assets/voice_matt.md` or from `candidate_profile.md`.** Both are stubs as of 2026-09-10.
- **Tracked changes are applied with `scripts/redline.py`** and the result is read with `scripts/docx_dump.py`. No hand-written tracked-changes code.
- **Every reviewer question is asked or listed as dropped with its reason.**
- **`GATE draft: PASS` before the reviewer is spawned, `GATE redteam: PASS` before anything is presented.**
- **The reviewer never sees `application_brief.md`, `tailoring_notes.md` or `fit_report.md`.**
- **Redline, don't overwrite.** Tracked changes authored "Recruiter"; save a new `_redline` / `_vN` file; `CORNET_` filename prefix.
- **No PDF, ever.** The redlined `.docx` is the deliverable; tracked changes are meaningless in a PDF anyway. See Step 3.
- **Match the application language** (EN posting → EN edits; FR posting → FR edits).

## Pipeline position
Third of three skills: `application-brief` plans, `resume-tailor` drafts, this skill attacks. Runs as the **final gate of `resume-tailor`** (after its draft gate, before the file is presented to Matt) and is also invokable standalone on any existing tailored resume.

What follows it (2026-09-24): Matt downloads the redlined `.docx`, accepts or rejects the Recruiter changes and edits in Word, then attaches the final file back to the chat. That triggers `asset-updater` in returned-file mode (his rewrites go to `Writing voice.md` §2, and the Recruiter edits he rejected are logged under "Rejected by Matt" in `redteam_notes.md` so this skill can see where it over-reaches), then `cover-letter`, which drafts from that final CV.
