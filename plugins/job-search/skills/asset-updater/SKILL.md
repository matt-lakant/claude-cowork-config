---
name: asset-updater
description: "Closes the learning loop after each application cycle by diffing Matt Cornet's edits against Claude-drafted deliverables (resumes, cover letters, form answers) and propagating systemic corrections back into the master assets — candidate_profile.md, voice_matt.md, master_resume.docx, and feedback memories. Use whenever Matt edits a tailored deliverable, says \"save this for next time\", asks to \"update the master\", flags an inflated framing, or mentions running a quarterly sweep across recent applications. Also use proactively after resume-tailor when Matt has made non-trivial edits to the output."
---

# Asset Updater

## What this skill does

Keeps Matt's master assets honest and current as the application cadence picks up. Without this loop, three things rot:

1. **The master drifts from real voice** — every tailoring run that goes uncorrected leaves a slightly inflated or off-tone framing in the wild
2. **The same overreach resurfaces** — a correction made in application A is forgotten by the time application B is tailored, and the panel for B sees the same inflated wording the panel for A would have
3. **Memory becomes incoherent** — feedback memories accumulate without dedup, contradict each other, or stay too narrow ("for the Anthropic CV") when they should be promoted to general guardrails

This skill triages Matt's edits, classifies them, and either promotes them to the master assets (with sign-off) or files them as application-specific notes.

## Source materials (read these every run)

> All paths in this skill are relative to the **Job Applications project root** — the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications").

1. `_assets/candidate_profile.md` — current master profile, facts, and accuracy guardrails
2. `_assets/voice_matt.md` — the voice reference: corpus of Matt's own sentences, banned constructions, review test. **This file is the primary destination for every voice-class edit.**
3. `_assets/master_resume.docx` — current master CV
4. The Claude-drafted deliverable that Matt edited (tailored resume, cover letter, form answers, recruiter message)
5. Matt's edited final version (provided by Matt or read from the same file if he edited in place)
6. Recent feedback memories under the auto-memory directory — to dedup against existing guardrails

## Inputs Matt will give you

- **Required:** the deliverable that was edited, plus either (a) Matt's final version, or (b) a description of the edits if the change is small
- **Optional:** explicit guidance ("treat as systemic", "this is one-off for the Munich form", "don't change the master, just remember it")

## Workflow

## Opportunity name — MANDATORY

**Before any other step,** check whether Matt has already provided an opportunity name in this conversation.

- If yes: use it.
- If no: ask him — *"Quel est le nom de cette opportunité ?"* (FR) or *"What is the name of this opportunity?"* (EN) — wait for his answer before proceeding.

Once the name is confirmed, **immediately display this reminder as a blockquote at the top of your response**, before any other output:

> 📝 **Renommer cette conversation en :** "[OpportunityName]"

The opportunity name is used to:
- Name the application folder: `applications/<opportunity-slug>/` (kebab-case)
- Name output files: `<OpportunityName>_<YYYY-MM-DD>_v1.docx` (underscores, increment version if file exists)

### Step 1 — Compute the diff

Compare Claude's draft to Matt's edited version. For each change, capture:
- The original wording
- The new wording
- Where it appears (profile, expertise bullet, role bullet, skills cell, form-field text, message body)

Skip cosmetic changes (whitespace, single-word polish that doesn't shift meaning). Focus on factual, framing, scope, and voice changes.

### Step 2 — Classify each change

| Class | Definition | Where it propagates |
|---|---|---|
| **Factual correction** | Matt's version is more accurate (location, role, scope, count, date, who-did-what) | Master assets + feedback memory |
| **Scope guardrail** | Matt walks back an embellishment Claude introduced | Master assets (as an "Accuracy guardrails" entry) + feedback memory |
| **Voice / tone preference** | Matt rewrites for register, brevity, or directness without changing facts | **`_assets/voice_matt.md`** — see Step 2b, which governs this class |
| **Role-specific framing** | Matt's edit only fits this one application (e.g., a JD-specific keyword) | Application folder only — do NOT promote |
| **Net-new fact** | Matt adds an experience, certification, or metric not in the master | Master assets (with explicit confirmation) + new candidate-profile bullet |

When in doubt, ask Matt to classify. Do not silently promote a change to a systemic guardrail.

### Step 2b — Voice edits: two different propagations, two different thresholds

Voice-class edits split in two, and conflating them is why the voice guidance stayed abstract and ineffective for months.

**The sample — no threshold, propagate immediately.** Matt's rewritten sentence goes verbatim into section 2 of `_assets/voice_matt.md`, in the same turn, every time. A sentence he actually wrote is ground truth for imitation; it needs no pattern to justify keeping. This is the single highest-value output of this skill, because imitating examples works where following rules does not.

**The rule — threshold of two, then generalize.** Only when the same underlying construction has been cut twice does it earn a row in the banned-constructions table in section 3, stated as a form rather than an instance: not "don't write *où ranger les méthodes*" but "no metaphor". A rule generalized from one edit over-fits and quietly bans phrasings Matt would have accepted.

Strip the sample of anything application-specific before filing it, and keep both the version Claude wrote and the version Matt wrote when the contrast is what teaches.

### Step 3 — Show the propagation plan

Before touching anything, present a short table to Matt in chat:

| Change | Class | Proposed action |
|---|---|---|
| "trading floor" → "research floor" (Santander) | Scope guardrail | Add to Accuracy guardrails in candidate_profile.md + save feedback memory |
| "où ranger les méthodes" → "établir des méthodes pour ne pas refaire deux fois la même erreur" | Voice preference | Sample → voice_matt.md §2 now; second metaphor cut, so "no metaphor" → §3 |
| "across NY/London/Tokyo/HK" → "in London" (Goldman) | Factual correction | Same as above |
| Added "OpenAI platform exposure" framing | Role-specific | Application folder only, not propagated |

Wait for Matt's go-ahead. The default is "do nothing without confirmation" for any change touching `master_resume.docx`. For `candidate_profile.md`, `voice_matt.md` and feedback memories, propose-then-apply is acceptable for factual corrections and voice samples; ask first for banned-construction rules and net-new facts.

### Step 4 — Apply the changes

In order:

1. **`_assets/voice_matt.md`** — append the sample to section 2; add a row to section 3 only if the threshold in Step 2b is met.
2. **Feedback memory** — write or update the memory file under the auto-memory directory. Dedup against existing memories first; update in place rather than creating a new file when the topic overlaps. Keep the index (`MEMORY.md`) tidy.
3. **`candidate_profile.md`** — append to the relevant section (Accuracy guardrails, Areas of expertise, Experience, Confirmed details log). Use the existing markdown structure; never rewrite from scratch.
4. **`master_resume.docx`** — only with explicit Matt sign-off. Edit text in place using `python-docx`, preserve styles. Save a versioned backup (`master_resume_pre_<YYYY-MM-DD>.docx`) before overwriting.

**A guardrail written only into a log does not propagate itself.** When a correction implies a change to the skills matrix, the profile body or the master CV, make that change in the same run. On 2026-09-04 a "remove PMP" decision sat in the Q&A log for nine days while the matrix in the same file still said PMP, and the error shipped in a tailored CV.

### Step 5 — Surface stale prior tailored CVs

If a propagated correction means earlier tailored CVs in `applications/<company-role>/` carry the now-stale framing, list them:

| Application | Status (from tracker) | Stale framing | Suggested action |
|---|---|---|---|
| anthropic-technical-deployment-lead | applied 2026-05-02 | "trading floor" + cross-asset Santander | Flag for interview prep, do not re-submit |
| capgemini-invent-director | drafted | "trading floor" | Regenerate before submission |

Default action for `applied` apps: flag for interview prep, do NOT auto-resubmit. Default action for `drafted` apps: offer to regenerate.

### Step 6 — Update memory index and confirm

Update `MEMORY.md` index entries if any memory titles changed. Show Matt a 3-line summary of what was changed and where. Provide computer:// links to every modified file.

## Quarterly sweep mode

When Matt asks "do a sweep" or "review my master", run this passive variant:

1. List all `applications/<company-role>/tailoring_notes.md` files modified in the last 90 days
2. For each, identify any "Trade-offs made" entries that introduced framings beyond the master
3. Surface a consolidated table of repeated tailoring choices (e.g., "10 of 12 recent CVs added 'partner-channel delivery' to the profile" → propose promoting it to the master)
4. Surface any feedback memories older than 90 days that haven't been used and may be stale
5. Check `_assets/voice_matt.md`: if the corpus in section 2 has not grown in 90 days while applications shipped, the sample loop is not running — say so explicitly

Output is a single markdown report (`asset_sweep_<YYYY-MM-DD>.md` at the project root) plus a chat summary. No edits without Matt's go-ahead.

## Hard rules

- **Never silently edit `master_resume.docx`.** Matt sign-off required, every time. Save a timestamped backup before overwriting.
- **Every Matt rewrite feeds the corpus.** Section 2 of `voice_matt.md` grows on every run where he changed a sentence. Skipping it is the failure mode this skill exists to prevent.
- **Never promote a role-specific framing to the master.** When in doubt, leave it in the application folder.
- **Never delete memory entries without showing Matt the content first.** Stale ≠ wrong.
- **Always dedup memories.** If a feedback memory already covers a topic, update it in place instead of writing a second file. Two memories that disagree are worse than one memory that's slightly out of date.
- **Always link to the source application** when a guardrail is added — so future-Matt can see where the correction came from.
- **Be conservative on voice *rules*, never on voice *samples*.** One edit is not a systemic rule; one edit is always a usable sample.

## Edge cases

- **Matt edits a deliverable that's already been submitted:** still propagate the correction to the master so the next application doesn't repeat it; flag the submitted version under "stale prior tailored CVs" for interview prep.
- **Matt's edit contradicts an existing feedback memory:** show him the conflict explicitly. Do not silently overwrite the older memory — ask which is canonical.
- **Edit is genuinely a one-off (e.g., Munich-specific phrasing):** save it in the application folder as `local_voice_notes.md` so it's available if the same JD comes around again, but do not touch the master or memory.
- **No master_resume.docx access (file locked / OneDrive placeholder):** skip the master step, complete everything else, and surface the blocker so Matt can unstick it. Never create a "fresh" master from scratch — that loses formatting.

## Output: present to Matt

After every run:
- 3-line summary of what changed: `Updated candidate_profile.md (+1 guardrail), added 2 samples to voice_matt.md, saved 1 feedback memory, flagged 2 stale CVs in applications/.`
- Computer:// links to every file touched
- A "next time" hint: the one thing that would have made this run unnecessary, so the drafting skills stop reintroducing the same correction.