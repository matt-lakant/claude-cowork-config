---
name: asset-updater
description: "Closes the learning loop after each application cycle by diffing Matt Cornet's edits against Claude-drafted deliverables (resumes, cover letters, form answers) and propagating systemic corrections back into the master assets: the vault notes Writing voice.md and Matt Cornet.md, candidate_profile.md, master_resume.docx, and feedback memories. Use whenever Matt edits a tailored deliverable, says \"save this for next time\", asks to \"update the master\", flags an inflated framing, or mentions running a quarterly sweep across recent applications. Also use proactively after resume-tailor when Matt has made non-trivial edits to the output, and always in returned-file mode when Matt attaches back a CV or cover letter he finalized in Word (resume-tailor and cover-letter call it for this)."
---

# Asset Updater

## Before anything else — open the opportunity

**Run the `opportunity-intake` skill first.** It confirms the opportunity name, resolves
the kebab-case slug, creates `applications/<slug>/` if it does not already exist, and
starts the opportunity's `notes.md`. Every file this skill produces goes inside that
folder.

Do not write anything before the folder exists. If the slug is unknown, ask. If the
Job Applications project folder is not connected, stop and say so — never fall back to
the project root, to another connected folder, or to chat-only delivery.

## What this skill does

Keeps Matt's master assets honest and current as the application cadence picks up. Without this loop, three things rot:

1. **The master drifts from real voice** — every tailoring run that goes uncorrected leaves a slightly inflated or off-tone framing in the wild
2. **The same overreach resurfaces** — a correction made in application A is forgotten by the time application B is tailored, and the panel for B sees the same inflated wording the panel for A would have
3. **Memory becomes incoherent** — feedback memories accumulate without dedup, contradict each other, or stay too narrow ("for the Anthropic CV") when they should be promoted to general guardrails

This skill triages Matt's edits, classifies them, and either promotes them to the master assets (with sign-off) or files them as application-specific notes.

## Where the voice reference lives (changed 2026-09-10)

**The voice reference is `Notes/Writing voice.md` in Matt's Obsidian vault.** It is the single source of truth for how he writes, on every surface: resume bullets, cover letters, form answers, LinkedIn messages and posts, recruiter emails, prepared interview answers.

| Section of that note | Holds |
|---|---|
| §2 Corpus | Matt's own sentences, verbatim. The imitation material. |
| §3 Constructions à ne jamais écrire | The banned-construction table. |
| §4 Test de relecture | The mechanical review pass, including point 8 (AI-tell check against the §4.1 list) and point 9 (swap test). |
| §5 Surfaces | Per-surface structure: 5.1 candidature prose, 5.2 resume, 5.3 LinkedIn analytical post, 5.4 cover letter (question order, length, frame, one reference letter per language). |

The old locations are now pointers and **must never be written to**:

- `_assets/voice_matt.md` — stub redirecting to the vault note
- `candidate_profile.md`, section "Voice & style guidelines" — stub redirecting to §5.2

**Precondition, check before any voice-class propagation:** the vault folder must be connected to this session. Run `ls $HOME/mnt/` and look for `obsidian-vault`. If it is not there, ask Matt to connect `C:\Users\mattc\Obsidian\obsidian-vault`, or call `device_request_folder_access` on it. **Do not fall back to writing the sample into `_assets/`** — that recreates the split this move removed. If the vault cannot be reached, say so, hand Matt the sample text so nothing is lost, and complete the non-voice steps.

## Source materials (read these every run)

> Paths marked *(project)* are relative to the **Job Applications project root**, the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications"). Paths marked *(vault)* are relative to the connected `obsidian-vault` folder.

1. *(vault)* `Notes/Writing voice.md` — the voice reference. **Primary destination for every voice-class edit.**
2. *(vault)* `Notes/Matt Cornet.md` — durable identity: background, education, technology and scope ceilings, target roles. Read before classifying anything as a factual correction or a net-new fact.
3. *(project)* `_assets/candidate_profile.md` — the append-only tailoring Q&A log and the resume-facing profile detail
4. *(project)* `_assets/master_resume.docx` — current master CV
5. The Claude-drafted deliverable that Matt edited (tailored resume, cover letter, form answers, recruiter message)
6. Matt's edited final version (provided by Matt or read from the same file if he edited in place)
7. Recent feedback memories under the auto-memory directory — to dedup against existing guardrails

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
| **Factual correction** | Matt's version is more accurate (location, role, scope, count, date, who-did-what) | *(vault)* `Notes/Matt Cornet.md` when it is a durable fact or ceiling; *(project)* `candidate_profile.md` log + feedback memory |
| **Scope guardrail** | Matt walks back an embellishment Claude introduced | *(vault)* `Notes/Matt Cornet.md`, "Technology and scope ceilings" + feedback memory |
| **Voice / tone preference** | Matt rewrites for register, brevity, or directness without changing facts | *(vault)* `Notes/Writing voice.md` — see Step 2b, which governs this class |
| **Role-specific framing** | Matt's edit only fits this one application (e.g., a JD-specific keyword) | Application folder only — do NOT promote |
| **Net-new fact** | Matt adds an experience, certification, or metric not in the master | *(vault)* `Notes/Matt Cornet.md` (with explicit confirmation) + *(project)* `candidate_profile.md` log |

When in doubt, ask Matt to classify. Do not silently promote a change to a systemic guardrail.

### Step 2b — Voice edits: two different propagations, two different thresholds

Voice-class edits split in two, and conflating them is why the voice guidance stayed abstract and ineffective for months.

**The sample — no threshold, propagate immediately.** Matt's rewritten sentence goes verbatim into **§2 of the vault note `Notes/Writing voice.md`**, in the same turn, every time. A sentence he actually wrote is ground truth for imitation; it needs no pattern to justify keeping. This is the single highest-value output of this skill, because imitating examples works where following rules does not.

**The rule — threshold of two, then generalize.** Only when the same underlying construction has been cut twice does it earn a row in the banned-constructions table in **§3**, stated as a form rather than an instance: not "don't write *où ranger les méthodes*" but "no metaphor". A rule generalized from one edit over-fits and quietly bans phrasings Matt would have accepted.

**A surface-specific habit goes to §5, not §2 or §3.** If the edit is about how a *kind* of text is shaped (resume header layout, how a LinkedIn post opens, what a form answer may concede) rather than about a turn of phrase, add it to the matching subsection of §5.

Strip the sample of anything application-specific before filing it, and keep both the version Claude wrote and the version Matt wrote when the contrast is what teaches.

### Step 3 — Show the propagation plan

Before touching anything, present a short table to Matt in chat:

| Change | Class | Proposed action |
|---|---|---|
| "trading floor" → "research floor" (Santander) | Scope guardrail | Ceilings section of `Matt Cornet.md` + feedback memory |
| "où ranger les méthodes" → "établir des méthodes pour ne pas refaire deux fois la même erreur" | Voice preference | Sample → `Writing voice.md` §2 now; second metaphor cut, so "no metaphor" → §3 |
| "across NY/London/Tokyo/HK" → "in London" (Goldman) | Factual correction | Same as above |
| Added "OpenAI platform exposure" framing | Role-specific | Application folder only, not propagated |

Wait for Matt's go-ahead. The default is "do nothing without confirmation" for any change touching `master_resume.docx` or `Notes/Matt Cornet.md`. For `Writing voice.md`, the `candidate_profile.md` log and feedback memories, propose-then-apply is acceptable for factual corrections and voice samples; ask first for banned-construction rules and net-new facts.

### Step 4 — Apply the changes

In order:

1. *(vault)* **`Notes/Writing voice.md`** — append the sample to §2; add a row to §3 only if the threshold in Step 2b is met; add a surface habit to §5 where it belongs. Leave the YAML frontmatter untouched. Never restructure the note while adding a line.
2. **Feedback memory** — write or update the memory file under the auto-memory directory. Dedup against existing memories first; update in place rather than creating a new file when the topic overlaps. Keep the index (`MEMORY.md`) tidy.
3. *(vault)* **`Notes/Matt Cornet.md`** — only for durable identity facts and ceilings, only with Matt's confirmation. Add to the existing section; never edit `type` or `created` in the frontmatter; use `[[wikilinks]]` for internal references. The vault's own `CLAUDE.md` governs, and it wins over this skill on any conflict.
4. *(project)* **`candidate_profile.md`** — append to the append-only "Confirmed details from tailoring Q&A" log, and to Areas of expertise / Experience where the resume needs the detail. Use the existing markdown structure; never rewrite from scratch. **Do not write voice or style rules here** — that section is a pointer now.
5. *(project)* **`master_resume.docx`** — only with explicit Matt sign-off. Edit text in place using `python-docx`, preserve styles. Save a versioned backup (`master_resume_pre_<YYYY-MM-DD>.docx`) before overwriting.

**A guardrail written only into a log does not propagate itself.** When a correction implies a change to the skills matrix, the profile body, the vault ceilings section or the master CV, make that change in the same run. On 2026-09-04 a "remove PMP" decision sat in the Q&A log for nine days while the matrix in the same file still said PMP, and the error shipped in a tailored CV.

### Step 5 — Surface stale prior tailored CVs

If a propagated correction means earlier tailored CVs in `applications/<company-role>/` carry the now-stale framing, list them:

| Application | Status (from tracker) | Stale framing | Suggested action |
|---|---|---|---|
| anthropic-technical-deployment-lead | applied 2026-05-02 | "trading floor" + cross-asset Santander | Flag for interview prep, do not re-submit |
| capgemini-invent-director | drafted | "trading floor" | Regenerate before submission |

Default action for `applied` apps: flag for interview prep, do NOT auto-resubmit. Default action for `drafted` apps: offer to regenerate.

### Step 6 — Update memory index and confirm

Update `MEMORY.md` index entries if any memory titles changed. Show Matt a 3-line summary of what was changed and where. Provide computer:// links to every modified file, vault notes included.

## Returned-file mode (added 2026-09-24)

**Trigger:** Matt attaches to the chat a CV or cover letter he finalized in Word, usually the `_redline.docx` from `resume-redteam` or `cover-letter-redteam` after accepting, rejecting and editing. `resume-tailor` (Step 8) and `cover-letter` (Steps 1 and 9) call this mode; it also runs on its own whenever such a file arrives. It is how both skills learn from what he actually sends.

### R1 — Identify and file the returned document

1. Work out the application slug and the document type (CV or letter) from the filename and content. If unclear, ask.
2. Save the file in `applications/<slug>/` under its own filename if that name is free, otherwise with `_final` appended (`_final2` next). Never overwrite. This copy is the version that was sent, and later skills (interview prep, follow-ups) read it.
3. Find the two Claude baselines in the same folder:
   - **A, Claude's draft:** the tailored `.docx` (CV) or the letter draft (`CORNET_<Company>_Cover_Letter_<date>.docx` / `_Lettre_`), before red-team.
   - **B, Claude's final proposal:** the `_redline.docx` with **every Recruiter change accepted** (drop `w:del` elements, unwrap `w:ins` elements, then extract text at the `w:t` level, since runs inside `w:ins` are invisible to `paragraph.runs`).
   If only one baseline exists, use it for both. If none exists (a letter Matt wrote alone), there is nothing to diff: offer to add the whole letter to the corpus and stop.

### R2 — Diff at sentence level and sort each change

Split the returned text (M) and both baselines into sentences, align them, and ignore layout-only changes (fonts, header block moved, paragraphs merged, whitespace).

| M compared with A and B | Meaning | Where it goes |
|---|---|---|
| M = B | He accepted Claude's final proposal | Nothing |
| M = A, M ≠ B | He **rejected a Recruiter edit** | `redteam_notes.md` (CV) or `cl_redteam_notes.md` (letter), section "Rejected by Matt", with OLD / proposed NEW. Red-team calibration, **not** a voice sample: the sentence is Claude's |
| M ≠ A and M ≠ B | **Matt wrote or rewrote it** | Classify with Step 2 below. Every voice-class change goes to §2 of *(vault)* `Notes/Writing voice.md` **verbatim, in the same turn**, with Claude's version (B) under it and one line on what he changed. Facts follow the Step 2 table |
| Sentence present in B, deleted in M | He cut it | Record the cut next to the sample. A cut that repeats a §3 or §4.1 pattern is evidence for that row; a new pattern repeated twice becomes a row (Step 2b threshold) |

### R3 — Propagate within the application

A correction he made in one deliverable applies to every deliverable of the same application (`Writing voice.md` §2, lesson of 2026-09-09). If he corrected a fact, a scope or a phrasing in the CV that also appears in the form answers or an unsent letter draft, fix it there too, or flag it if the piece is already sent.

### R4 — Template and reference letter

- If he changed the letter's **frame** (header block, salutation, closing, signature), propose updating `_assets/cover_letter_template_<EN|FR>.docx` and the frame bullets in `Writing voice.md` §5.4. Ask first.
- If the returned letter is final and complete, ask whether it should replace the §5.4 reference letter for its language. Never replace it without his yes.

### R5 — Report

Three lines, then continue with whatever he asked for (typically `cover-letter` when he returned a CV):
`Filed CORNET_..._final.docx. 3 rewrites added to Writing voice.md §2, 2 rejected Recruiter edits logged in redteam_notes.md, 1 fact logged in candidate_profile.md.`

If the vault is not connected, do not skip the voice samples silently: hand him the sentences verbatim and say they still need filing.

## Quarterly sweep mode

When Matt asks "do a sweep" or "review my master", run this passive variant:

1. List all `applications/<company-role>/tailoring_notes.md` files modified in the last 90 days
2. For each, identify any "Trade-offs made" entries that introduced framings beyond the master
3. Surface a consolidated table of repeated tailoring choices (e.g., "10 of 12 recent CVs added 'partner-channel delivery' to the profile" → propose promoting it to the master)
4. Surface any feedback memories older than 90 days that haven't been used and may be stale
5. Check *(vault)* `Notes/Writing voice.md`: if the corpus in §2 has not grown in 90 days while applications shipped, the sample loop is not running — say so explicitly
6. Check that `_assets/voice_matt.md` is still only a stub. If anything has written content back into it, that is a skill still pointing at the old location — name it so it can be fixed

Output is a single markdown report (`asset_sweep_<YYYY-MM-DD>.md` at the project root) plus a chat summary. No edits without Matt's go-ahead.

## Hard rules

- **No opportunity-scoped file is ever written to the project root.** Everything for an
  opportunity lives in `applications/<slug>/`. Only `applications_tracker.md`, `README.md`,
  `_assets/` and `_research/` belong at the root. The standing "project folders are kept
  flat, no subfolders" preference does **not** apply to Job Applications — see the
  `opportunity-intake` skill, which wins on any conflict.
- **Never silently edit `master_resume.docx`.** Matt sign-off required, every time. Save a timestamped backup before overwriting.
- **Every Matt rewrite feeds the corpus.** §2 of the vault note grows on every run where he changed a sentence. Skipping it is the failure mode this skill exists to prevent.
- **Never write voice content into `_assets/voice_matt.md` or into `candidate_profile.md`.** Both are pointers as of 2026-09-10. Writing there splits the source of truth again, and the split will not be noticed for weeks.
- **Never promote a role-specific framing to the master.** When in doubt, leave it in the application folder.
- **Never delete memory entries without showing Matt the content first.** Stale is not the same as wrong.
- **Always dedup memories.** If a feedback memory already covers a topic, update it in place instead of writing a second file. Two memories that disagree are worse than one memory that's slightly out of date.
- **Always link to the source application** when a guardrail is added, so future-Matt can see where the correction came from.
- **Be conservative on voice *rules*, never on voice *samples*.** One edit is not a systemic rule; one edit is always a usable sample.

## Edge cases

- **The vault is not connected:** do not fall back to the old paths. Ask Matt to connect it, or hand him the sample text verbatim so he can paste it himself, and complete every non-voice step.
- **Matt edits a deliverable that's already been submitted:** still propagate the correction so the next application doesn't repeat it; flag the submitted version under "stale prior tailored CVs" for interview prep.
- **Matt's edit contradicts an existing feedback memory or a vault ceiling:** show him the conflict explicitly. Do not silently overwrite the older one — ask which is canonical.
- **Edit is genuinely a one-off (e.g., Munich-specific phrasing):** save it in the application folder as `local_voice_notes.md` so it's available if the same JD comes around again, but do not touch the vault, the master or memory.
- **No master_resume.docx access (file locked / OneDrive placeholder):** skip the master step, complete everything else, and surface the blocker so Matt can unstick it. Never create a "fresh" master from scratch — that loses formatting.

## Output: present to Matt

After every run:
- 3-line summary of what changed: `Added 2 samples to Writing voice.md §2, +1 ceiling in Matt Cornet.md, logged 1 confirmed detail in candidate_profile.md, flagged 2 stale CVs in applications/.`
- Computer:// links to every file touched
- A "next time" hint: the one thing that would have made this run unnecessary, so the drafting skills stop reintroducing the same correction.
