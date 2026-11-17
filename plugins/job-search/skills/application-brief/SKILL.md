---
name: application-brief
description: "Prepares the brief for one job application before any CV or letter is drafted: parses the posting, decides whether the role is hands-on or leadership, searches Matt Cornet's record for the strongest fact behind each requirement, asks him the questions a reviewer would ask, records his decisions, and picks the base CV. Writes application_brief.md, which resume-tailor and cover-letter draft from. Use it whenever Matt wants a resume or a letter for a posting and the application folder has no application_brief.md yet, and as the first stage of 'prepare my application', 'tailor my resume', or 'check fit and prepare resume'."
---

# Application Brief

## Step map

Run the steps in this order. Each one leaves something in `applications/<slug>/application_brief.md`; Step 8 checks that everything is there. Do not start `resume-tailor` on a brief that has not passed its gate.

| Step | What it does | What it leaves in the brief | Stops the run when |
|---|---|---|---|
| 1 | Checks the inputs exist | nothing | the folder, `job_description.md` or `company_overview.md` is missing |
| 2 | Parses the posting and tags the role | `## Role`, `## Top-third keywords`, `## Form questions`, the requirement list | the posting cannot be read |
| 3 | Searches the record, requirement by requirement | `## Requirements and evidence`, `## Not claimable`, `## First-hand facts` | never: a requirement with no fact becomes a question or a gap |
| 4 | Reads the lessons of past red-teams | `## Lessons applied` | never |
| 5 | Asks Matt the reviewer's questions, logs the answers | `## Questions put to Matt` | Matt has not answered (unattended run: list them as open) |
| 6 | Records the decisions | `## Decisions` | never |
| 7 | Chooses and audits the base CV | `## Base file` | no usable base and no master |
| 8 | Writes the angle and runs the gate | `## Angle`, gate `PASS` | the gate lists a missing item |

Why a separate skill (2026-11-17): these steps used to open `resume-tailor`, which had grown to 16 steps in one file, and the ones that decide the quality of the first draft (searching the record, asking the hard questions early, applying Matt's decisions) were the ones that got skipped. They now have their own file, their own output, and a script that checks the output.

> **The record is three files (2026-11-17).** *(project)* `_assets/candidate_profile.md` is the short profile: identity, the Current values table, the Experience summary, the guardrails. `_assets/profile_log.md` is the dated, append-only log: **every answer and correction from Matt is appended there**, one fact per entry, never in the profile. `_assets/facts/` holds one generated sheet per theme (list in `facts/INDEX.md`): read the sheet when a whole subject is needed. Wherever this skill says "the log in `candidate_profile.md`" or "the Q&A log", it means `profile_log.md`. After appending to the log, rebuild the sheets: `python3 <asset-updater skill dir>/scripts/build_facts.py <project>/_assets`.

## What it reads

> *(project)* paths are relative to the Job Applications project root, the folder that holds `applications/`, `_assets/` and `applications_tracker.md`. *(vault)* paths are relative to the connected `obsidian-vault` folder. If either folder is not connected, request it (`device_request_folder_access`) and stop if it is refused.

1. `applications/<slug>/job_description.md` and `company_overview.md`. `fit_report.md` if `job-fit-analyzer` ran: reuse its requirement matrix, its "Not claimable" list and its role tag.
2. *(vault)* `Notes/Matt Cornet.md`: "Framing guardrails" and "Technology and scope ceilings". A ceiling is a hard limit; nothing in this brief may plan a claim beyond one.
3. *(project)* `_assets/candidate_profile.md`: the Current values table at the top (current wording of each figure), the structured sections, and the log, which is searched (Step 3), never read in full.
4. *(project)* `_assets/cv_rules.md` Part 1: the standing rules and the tags that trigger them.
5. *(project)* `_assets/redteam_lessons.md`.

This skill writes no sentence that Matt signs, so it does not load the voice note.

## Step 1: Check the inputs

Run `opportunity-intake` if `applications/<slug>/` does not exist. `job_description.md` must exist (intake Step 3b creates it) and `company_overview.md` too (`company-overview` creates it). If the folder already holds a brief, a CV or a memo for this posting, follow the re-run rule of `opportunity-intake` (never overwrite; a comparison run uses a suffix on every file, and the gate takes `--suffix`).

## Step 2: Parse the posting and tag the role

Read `job_description.md`. Extract, in the posting's own words:

- **Role tag: `hands_on` or `leadership`.** It drives the framing of the CV and the letter (rules R18 to R20). The question is whether the role requires doing the work oneself. It is not the title and not the contract type.
  - `hands_on`: the person in the role produces the work (builds, writes, configures, delivers, runs the projects), alone or with a small team. Individual-contributor and manager postings, and most freelance missions.
  - `leadership`: the role is held through other people and the posting does not ask for the work to be done personally. Director, head-of, VP, C-level, and freelance leadership mandates.
  - A "Head of" with a team of 4 or a "player-coach" is `hands_on`. A freelance programme director steering several project managers is `leadership`. A posting that asks for both is `hands_on`.
  - Write which words of the posting decided it.
- **The other tags for `cv_check.py`:** `non_sales` (the role is not a sales role: most postings), `non_finance` (the employer is outside financial services), `ps_role` (professional services, implementation, delivery, customer engineering).
- **Requirements:** every hard requirement and every nice-to-have, one per line, plus each named tool, method, certification, regulation, sector and scale bar.
- **Top-third keywords (3 to 6):** the words of the job title that qualify the role (a region such as "EMEA", a function) and the posting's core nouns (what the employer sells or what the role runs). Only words Matt can claim: a word blocked by a ceiling is never listed. `resume-tailor` must place them above the skills matrix.
- **ATS keywords (15 to 25),** verbatim.
- **Every question the application form asks,** verbatim. For a Collective.work posting they are at the end of `job_description.md`.
- **Language** of the posting: every deliverable follows it.

**Earlier application to the same employer.** Search `applications_tracker.md` and `applications/` for the company. If a similar role was applied to before, compare the two postings and note what changed in the required profile. Two postings are not proof of one re-post: say it is an inference unless the older posting is confirmed closed.

## Step 3: Search the record for every requirement

This is the step that decides how much the red-team will have to correct. Up to 2026-11-16 the red-team rewrote about 20% of each CV, and the largest cause was facts already in Matt's log that the draft had not used. The reviewer found them by searching the log requirement by requirement. Do that search here, first.

First read `_assets/facts/INDEX.md` and the one or two sheets that match the role (a delivery role: `factset_delivery_and_programs` and `factset_clients`; an AI role: `ai_practice`, `bluematrix`, `lakant_io`). A sheet gives the whole subject in one read, most recent first, with the replaced statements set apart at the bottom. The search below still runs for every requirement: the sheets are sorted by keyword and a fact can sit in a neighbouring theme.

For each requirement:

```text
python3 <this skill's dir>/scripts/profile_search.py <project>/_assets/candidate_profile.md "<term>;<term>;..."
```

- Give 3 to 6 terms: the posting's word, **its French equivalent (most of the log is in French)** and the words Matt would use. For "SOW": `SOW;statement of work;chiffrage;estimation d'effort`. One search per requirement, never one for the whole posting.
- Read the entries returned, most recent first. An entry flagged "may supersede" replaces something: check the dates. For any figure, the Current values table wins.
- Check the ceilings before counting a fact: a tool under "Never claim at all" is `blocked`, whatever the log says.

Write one row per requirement (table format under "The brief"). Up to three facts per row, the most specific first: a number, a named client, something he did himself. Mark a fact `first-hand` when it is work he did personally.

- A requirement with a fact on record: the fact must appear in the CV. `resume-tailor` fills where.
- A requirement with no fact: it becomes a question (Step 5), or a stated gap when a ceiling blocks it or he has confirmed he lacks it. A gap is never dressed up: no "transferable from" wording is planned for the CV.

List under `## First-hand facts` the two to four first-hand facts that best match the posting, each with the few verbatim words `resume-tailor` will pass to `cv_check.py --hands-on`. A `hands_on` role needs at least two.

## Step 4: Read the lessons

Read `_assets/redteam_lessons.md` in full (it is short). List in the brief the lines that match this role family and what each changes for this application. If none applies, say so.

## Step 5: Ask the reviewer's questions before the draft

Write down the attacks a skeptical reviewer will make on this application, then check each against the evidence table and the Current values table. What the record does not answer is a question for Matt, now. Questions asked after the draft come back as redline.

The recurring ones:

- **The number behind each KPI the posting names** (utilization, margin, forecast, time to value, NPS, on-time rate): the figure, what it was measured on, the period. If the record has only an estimate, ask whether it can be printed and how he would defend it.
- **First-hand proof** for the two or three central requirements: what he did himself, not what his organization delivered.
- **A recovery or a failure**, when the posting mentions escalations, projects off track or turnarounds.
- **The split that matches the posting:** how much of his scope was in the posting's region, sector, team profile or client type.
- **Third parties**, when the posting names partners, subcontractors or vendors: who, how many, what he controlled.
- **Every requirement still partial, absent or unknown** after Step 3.
- **The role tag**, only when the posting does not settle it.

Ask with `AskUserQuestion`, in rounds of up to 4, **until every question has been put to him**. Options are concrete and grounded in his record, so he can answer in one click; multi-select where natural. Skip only what the record already answers or a ceiling blocks. If the answers for this posting are already in the log (a re-run), use them and ask only what they leave open.

**Log every answer** in the log of `candidate_profile.md` (last section of the file, appended at the end, dated, one fact per entry where possible). An answer that sets or changes a figure also updates the Current values table; one that moves a ceiling goes to the vault note. Hand both to `asset-updater`.

If Matt is not there to answer, do not invent: list the questions as open in the brief and say so in your closing message.

## Step 6: Record the decisions

Some answers are decisions about the documents, not facts: what to lead with, what to leave out, how to word a title. Facts go to the log; decisions go in the `## Decisions` table, with the place where a reader will see each one. The standing rows are always there:

- the role tag and what it implies (R18 and R19 for `hands_on`, R20 for `leadership`);
- each rule of `cv_rules.md` that the tags trigger (for example R3 for `non_sales`, R4 for `non_finance`, R5 for `ps_role`).

`resume-tailor` must quote, for each row, the line of the CV that applies it. On 2026-11-16 Matt answered "lead with the direct team" and the draft opened on 80+ people and a USD 40M P&L: the answer had been logged as a fact and nothing carried it into the draft.

## Step 7: Choose and audit the base CV

The base is the `.docx` that `resume-tailor` will edit in place.

1. **Candidates:** CVs Matt finalized and sent (the tracker and each folder's `redteam_notes.md` name the file that went out), in the posting's language, for the nearest role family and the same role tag. Take the most recent that fits. A draft or a redline he never returned is not a candidate.
2. **Fallback:** *(project)* `_assets/master_resume.docx`.
3. **Audit it:** `python3 <resume-tailor skill dir>/scripts/cv_check.py <base.docx> --rules <project>/_assets/cv_rules.md --profile <project>/_assets/candidate_profile.md --tags <tags of this posting>`. Each `FAIL` is a line `resume-tailor` must rewrite: a superseded figure, a title or a wording that was right for the earlier posting and is not for this one. Paste the result lines in the brief.
4. **The base is layout and phrasing Matt validated, not evidence.** A figure is printed because the Current values table or the log supports it, never because the base had it.

## Step 8: Write the angle, run the gate

Add `## Angle`: two or three sentences on the thread of this application, the two or three facts that carry it, and the fact about the employer (from `company_overview.md`) that the letter can tie them to. Then:

```text
python3 <this skill's dir>/scripts/gate.py brief <project>/applications/<slug>
```

Fix whatever it lists and run it again until it prints `GATE brief: PASS`. Send `application_brief.md` to Matt as a file card (`SendUserFile`), add a Timeline line to `notes.md`, and continue with `resume-tailor` in the same turn unless Matt asked for the brief only.

## The brief

`applications/<slug>/application_brief.md`. **The `##` headings are keys read by the gate and by the other skills: keep them exactly, in English, whatever the language of the posting.** The content follows the posting's language. A section with nothing in it says `None`, with the reason.

```markdown
# Application brief: <Company>, <Role>

## Role
- Role tag: hands_on | leadership (<the words of the posting that decided it>)
- cv_check tags: <non_sales, non_finance, ps_role, hands_on ...>
- Language: <English | French>
- Level in the posting: <title, team size, reporting line>
- Earlier application to this employer: <none | folder, what changed>

## Requirements and evidence
| # | Requirement | Hard / nice | Coverage | Strongest facts on record (entry date) | First-hand | Open question |
|---|---|---|---|---|---|---|
| 1 | <posting's words> | hard | strong / partial / gap / blocked | <fact (2026-10-15); fact (2026-11-16)> | yes / no | <question, or empty> |

## Not claimable
- <requirement>: <ceiling or guardrail that blocks it>

## Top-third keywords
- <keyword>

## ATS keywords
<comma-separated, verbatim>

## First-hand facts
- <fact> | fragment for cv_check: "<few verbatim words>"

## Questions put to Matt
| # | Question | Answer | Logged (date of the log entry) |
|---|---|---|---|

## Decisions
| Decision | Source | Where it must show |
|---|---|---|
| Role is hands_on: no scale marker above the skills matrix, scale once in the Context line | R18 | header, profile, expertise lines; first bullet of each role |

## Lessons applied
- <line of redteam_lessons.md> -> <what it changes here>

## Base file
- File: <path of the .docx>
- Why this one: <role family, language, date sent>
- Audit: <last lines of cv_check.py on the base, and the lines to rewrite>

## Form questions
1. <question, verbatim>

## Angle
<two or three sentences>
```

## Hard rules

- **Files for an opportunity live in `applications/<slug>/`**, never at the project root (see `opportunity-intake`).
- **Nothing is invented.** A fact enters the brief because the record or Matt's answer supports it, with its date. A requirement he does not meet is a gap, stated as one.
- **Ceilings are hard limits.** A blocked requirement is never turned into a question, a hidden match or a softened claim.
- **One search per requirement, in English and in French.** A brief whose evidence table was filled from memory of the profile's top section has skipped the step this skill exists for.
- **Every question is asked before the draft, or listed as open.** Not after.
- **The gate decides when the brief is finished.** `GATE brief: PASS`, or the run is not done.
