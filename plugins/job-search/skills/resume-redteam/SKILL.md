---
name: resume-redteam
description: "Adversarial recruiter review of a resume produced by `resume-tailor`, run before the file reaches Matt. Its job is to FIND PROBLEMS, not validate. It re-reads the job description, company_overview.md, and candidate_profile.md, then attacks the tailored resume for what is weakest, vaguest, removable, missing, or over-claimed, redlines it with tracked changes, and asks Matt questions where a fix needs a fact it does not have. Use as the mandatory gate at the end of `resume-tailor`, or on demand when Matt says \"red-team\", \"adversarial review\", \"poke holes\", \"stress-test my resume\", \"have a recruiter tear it apart\", or \"what's weak here\". The critique runs in a fresh-context subagent so it never sees the drafting rationale."
---

# Resume Red-Team (Adversarial Recruiter)

> All paths in this skill are relative to the **Job Applications project root** — the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications").

## Purpose & stance

Play a **skeptical hiring manager / senior recruiter for this specific role** who screens hundreds of applications and is looking for reasons to **reject**. The deliverable is not reassurance — it is a list of concrete problems and a redlined resume that is harder to screen out.

**This skill does not validate the resume `resume-tailor` produced. It tries to break it.** If it finishes a run without surfacing real problems, it has failed.

## Why this runs in a fresh-context subagent

If the same context that wrote (or just read the rationale for) the resume also critiques it, it will defend its own choices. To stay genuinely adversarial, **the critique MUST run in a fresh-context subagent** (the `Task` tool) that is handed only the primary sources and the resume text — never the tailoring rationale, the fit memo, or "why this is a good fit" framing. This subagent spawn is an explicit, standing part of Matt's setup; it is sanctioned even though agents are not spawned by default.

## Source materials (the subagent reads these, not Claude's prior work)

1. The job description (`applications/<slug>/job_description.*`, or the posting Matt provided).
2. `applications/<slug>/company_overview.md` — what the company actually wants and screens for.
3. `_assets/candidate_profile.md` — the **ground truth** of what Matt has really done, including the append-only Q&A log. Used to tell "unsupported claim" apart from "under-sold real experience."
4. The tailored resume `.docx` produced by `resume-tailor` (extract its text).

Claude (not the subagent) also reads `_assets/voice_matt.md` before writing any replacement text in Step 3.

## Workflow

### Step 1 — Assemble the adversary's packet
Extract the tailored resume to plain text (`extract-text` or unpack). Gather the JD, `company_overview.md`, and `candidate_profile.md`. Do **not** include the fit score, the tailoring memo, or any "this is why it fits" narrative. If the JD file carries an internal coverage or fit matrix, tell the subagent explicitly to ignore that section — it is your own note, not a primary source, and it leaks the drafting rationale into the adversary's packet.

### Step 2 — Spawn the adversarial subagent
Use the `Task` tool (subagent type `general-purpose`). Give it this brief (fill the braces):

> You are a skeptical hiring manager screening for **{role}** at **{company}**. You reject most resumes in 6 seconds. Your job is to find every reason this candidate would NOT make the shortlist — do not praise, do not validate.
> Inputs: [paste JD] / [paste company_overview.md] / [paste candidate_profile.md as ground truth] / [paste the tailored resume text].
> Do two reads: (1) a 6-second skim — does the top third earn a deep read for THIS role? (2) a deep read against every JD requirement.
> Return, with severity (High/Med/Low) on each item:
> 1. **Weakest bullets** — limp, generic, or low-signal lines that waste prime space.
> 2. **Vague / filler** — unquantified claims, buzzwords, hedges, anything a skeptic would not believe without proof.
> 3. **Removable** — lines that add nothing for THIS JD and should be cut to tighten the read.
> 4. **Missing** — JD must-haves, company-overview signals, and ATS keywords absent or buried; note which are likely real-but-undocumented (check candidate_profile) vs genuine gaps.
> 5. **Credibility risks** — over-claims, unsupported scope/scale, seniority mismatch, or anything that invites a hostile interview question.
> Then produce: (a) a prioritized **redline plan** as specific `OLD → NEW` text edits (or `CUT`), each grounded only in facts present in candidate_profile — never invent. Copy the `OLD` text verbatim from the resume so each edit can be applied automatically. (b) a short list of **questions for the candidate** where a line could be stronger but you lack the fact to fix it.
> End with a one-line verdict: shortlist / borderline / reject, and the single biggest thing holding it back.

Require at least **5 substantive problems**. If the subagent returns a thin or congratulatory critique, push back and re-run — that is a failed adversary, not a clean resume.

### Step 2b — Verify the critique before acting on it

The subagent argues from dated entries in `candidate_profile.md`. **Check that the entries behind the edits you are about to apply actually say what it claims.** One grep on the dates it cites is enough. An adversary reasoning from a misread guardrail produces a confident, wrong edit, and this check is what separates a redline Matt can trust from one he has to audit himself.

### Step 3 — Apply the redline as tracked changes
Bring the subagent's `OLD → NEW` / `CUT` edits into the `.docx` as **Word tracked changes** (see the `docx` skill: `<w:ins>` / `<w:del>`), authored **"Recruiter"** so Matt can accept/reject each one and see exactly what was attacked. Apply only edits grounded in `candidate_profile.md`; hold back any edit that would require an unconfirmed fact and route it to Step 4 instead.

**Every `NEW` string lands in Matt's resume, so it follows `_assets/voice_matt.md`** — no metaphor, no calque of an English idiom, no self-definition against an implied lesser candidate, no sentence announcing what the next one will do. An adversary optimizing for punch will happily write a flourish; rewrite it plain before it goes in the file.

Save a redline copy — never overwrite the tailored file: `applications/<slug>/CORNET_<...>_redline.docx` (or `_vN` if a redline already exists). Office files are versioned, never edited in place.

**Never produce a PDF.** Matt makes his own PDF from Word, after he has validated and reformatted the `.docx`. Do not save a `.pdf` beside the `.docx`, do not attach one, and do not offer one. If you need a PDF to check pagination, convert into a temp directory **outside** the project folder (e.g. `$HOME/tmp`), read the page count there, and leave nothing behind. A `.pdf` in an application folder is a stale copy of a document that is about to change, and on Matt's machine a session cannot delete files, so it becomes his cleanup.

**Two mechanical traps in tracked changes**, both worth knowing before writing the script:
- Runs living inside `<w:ins>` are not direct children of the paragraph, so `python-docx`'s `paragraph.runs` will not see them. Any later text pass over the file must walk `w:t` nodes at the XML level, or it will silently skip everything you inserted.
- A header run often carries a `<w:br/>`. Replacing that run drops the line break and welds two lines into one. Preserve the break when rebuilding the run.

**Decisions Matt has already made are not proposals.** If he has settled a point — in this session or in a logged preference — apply it directly to both files instead of offering it as a tracked change. The redline is for the arbitrations he still owes; every settled item left in it is one more click of noise.

### Step 4 — Question Matt, then strengthen
Ask the subagent's questions with `AskUserQuestion` (batch into rounds of up to 4; grounded, one-click options; room to add detail). For every answer:
- Append it (dated) to the `## Confirmed details from tailoring Q&A (append-only log)` in `candidate_profile.md` (standing rule), and promote durable items via `asset-updater`.
- Convert "under-sold real experience" flags into real, specific tracked-change edits. Never invent — if Matt confirms nothing, leave the gap and name it in the memo.
- **If a finding is a factual error rather than a weakness** — a certification he does not hold, a guardrail decided but never applied — fix it at the source in the same run: `_assets/candidate_profile.md` and `_assets/master_resume.docx`, not only the CV in hand. Otherwise it returns on the next tailoring run.
- **If Matt rewrites one of the redline strings**, add his version verbatim to section 2 of `_assets/voice_matt.md` in the same turn.

### Step 5 — Present to Matt
Save a short critique memo: `applications/<slug>/redteam_notes.md` — the prioritized problem list with severities, what was redlined, what was cut, open gaps, and the verdict + biggest blocker. Present the **redlined `.docx`** and the memo, with a 3-line summary of the most important attacks. Do not paste the full resume into chat.

## Hard rules
- **Find problems — never rubber-stamp.** ≥5 substantive issues per run, or an explicit, specific justification for why a category is genuinely clean.
- **Independence is mandatory.** The critique runs in a fresh-context subagent; do not let prior drafting rationale leak into its packet.
- **Truth ceiling holds.** Tracked-change edits may cut, sharpen, and reorder freely, but must not invent experience, metrics, employers, dates, or certifications. Under-selling becomes a question, not a fabrication. Respect the accuracy guardrails in `candidate_profile.md`.
- **Replacement text follows `voice_matt.md`.** A sharper line that Matt would never say is not an improvement.
- **Redline, don't overwrite.** Tracked changes authored "Recruiter"; save a new `_redline` / `_vN` file; `CORNET_` filename prefix.
- **No PDF, ever.** The redlined `.docx` is the deliverable; tracked changes are meaningless in a PDF anyway. See Step 3.
- **Match the application language** (EN posting → EN edits; FR posting → FR edits).

## Pipeline position
Runs as the **final gate of `resume-tailor`** (after the product/balanced passes, before the file is presented to Matt) and is also invokable standalone on any existing tailored resume.