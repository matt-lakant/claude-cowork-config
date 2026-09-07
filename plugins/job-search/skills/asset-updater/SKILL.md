---
name: asset-updater
description: Closes the learning loop after each application cycle by diffing Matt Cornet's edits against Claude-drafted deliverables (resumes, cover letters, form answers) and propagating systemic corrections back into the master assets — candidate_profile.md, master_resume.docx, and feedback memories. Use whenever Matt edits a tailored deliverable, says "save this for next time", asks to "update the master", flags an inflated framing, or mentions running a quarterly sweep across recent applications. Also use proactively after resume-tailor when Matt has made non-trivial edits to the output.
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

1. `_assets/candidate_profile.md` — current master profile and voice rules
2. `_assets/master_resume.docx` — current master CV
3. The Claude-drafted deliverable that Matt edited (resume_<company>_<date>.docx, cover_letter.md, application_form_answers.md, etc.)
4. Matt's edited final version (provided by Matt or read from the same file if he edited in place)
5. Recent feedback memories under the auto-memory directory — to dedup against existing guardrails

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
- Where it appears (profile, expertise bullet, role bullet, skills cell, form-field text)

Skip cosmetic changes (whitespace, single-word polish that doesn't shift meaning). Focus on factual, framing, scope, and voice changes.

### Step 2 — Classify each change

Apply this taxonomy:

| Class | Definition | Where it propagates |
|---|---|---|
| **Factual correction** | Matt's version is more accurate (location, role, scope, count, date, who-did-what) | Master assets + feedback memory |
| **Scope guardrail** | Matt walks back an embellishment Claude introduced | Master assets (as an "Accuracy guardrails" entry) + feedback memory |
| **Voice / tone preference** | Matt rewrites for register, brevity, or directness without changing facts | Voice guidelines section of `candidate_profile.md` + feedback memory |
| **Role-specific framing** | Matt's edit only fits this one application (e.g., a JD-specific keyword) | Application folder only — do NOT promote |
| **Net-new fact** | Matt adds an experience, certification, or metric not in the master | Master assets (with explicit confirmation) + new candidate-profile bullet |

When in doubt, ask Matt to classify. Do not silently promote a change to a systemic guardrail.

### Step 3 — Show the propagation plan

Before touching anything, present a short table to Matt in chat:

| Change | Class | Proposed action |
|---|---|---|
| "trading floor" → "research floor" (Santander) | Scope guardrail | Add to Accuracy guardrails in candidate_profile.md + save feedback memory |
| Removed "mutualized across equity, credit, FX and macro" | Scope guardrail | Same as above |
| "across NY/London/Tokyo/HK" → "in London" (Goldman) | Factual correction | Same as above |
| Tightened "Why Anthropic?" by 50 words | Voice preference | Append to candidate_profile.md voice guidelines |
| Added "OpenAI platform exposure" framing | Role-specific | Application folder only, not propagated |

Wait for Matt's go-ahead. The default is "do nothing without confirmation" for any change touching `master_resume.docx`. For `candidate_profile.md` and feedback memories, propose-then-apply is acceptable if the change is clearly a factual correction; ask first for voice changes and net-new facts.

### Step 4 — Apply the changes

In order:

1. **Feedback memory** — write or update the memory file under the auto-memory directory. Dedup against existing memories first; update in place rather than creating a new file when the topic overlaps. Keep the index (`MEMORY.md`) tidy.
2. **`candidate_profile.md`** — append to the relevant section (Accuracy guardrails, Voice & style guidelines, Areas of expertise, Experience). Use the existing markdown structure; never rewrite from scratch.
3. **`master_resume.docx`** — only with explicit Matt sign-off. Edit text in place using `python-docx`, preserve styles. Save a versioned backup (`master_resume_pre_<YYYY-MM-DD>.docx`) before overwriting.

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

Output is a single markdown report (`asset_sweep_<YYYY-MM-DD>.md` at the project root) plus a chat summary. No edits without Matt's go-ahead.

## Hard rules

- **Never silently edit `master_resume.docx`.** Matt sign-off required, every time. Save a timestamped backup before overwriting.
- **Never promote a role-specific framing to the master.** When in doubt, leave it in the application folder.
- **Never delete memory entries without showing Matt the content first.** Stale ≠ wrong.
- **Always dedup memories.** If a feedback memory already covers a topic, update it in place instead of writing a second file. Two memories that disagree are worse than one memory that's slightly out of date.
- **Always link to the source application** when a guardrail is added — so future-Matt can see where the correction came from.
- **Be conservative on voice changes.** A single edit on a single application is rarely a systemic preference; wait for the pattern to repeat at least twice before promoting to the master voice guidelines.

## Edge cases

- **Matt edits a deliverable that's already been submitted:** still propagate the correction to the master so the next application doesn't repeat it; flag the submitted version under "stale prior tailored CVs" for interview prep.
- **Matt's edit contradicts an existing feedback memory:** show him the conflict explicitly. Do not silently overwrite the older memory — ask which is canonical.
- **Edit is genuinely a one-off (e.g., Munich-specific phrasing):** save it in the application folder as `local_voice_notes.md` so it's available if the same JD comes around again, but do not touch the master or memory.
- **No master_resume.docx access (file locked / OneDrive placeholder):** skip the master step, complete everything else, and surface the blocker so Matt can unstick it. Never create a "fresh" master from scratch — that loses formatting.

## Output: present to Matt

After every run:
- 3-line summary of what changed: `Updated candidate_profile.md (+1 guardrail), saved 1 feedback memory, flagged 2 stale CVs in applications/.`
- Computer:// links to every file touched
- A "next time" hi