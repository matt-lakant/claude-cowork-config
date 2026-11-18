---
name: job-watch
description: Daily watch for senior job openings for Matt, at the source (target companies' applicant tracking systems, Welcome to the Jungle, Indeed, recent funding rounds). Registers every matching opening under a permanent ID (J001...) in _research/job_watch_log.md, reports only the new ones, keeps each source's access instructions and issues in _research/job_sources.md, and refreshes the Job openings dashboard. Runs "check fit and prep resume if good" on the openings Matt picks, any day after they were found - by ID, by "all", or ticked on the dashboard. Use for the scheduled Daily job watch and Analyze job openings tasks, for any reply with opening IDs, and whenever Matt asks to analyze the openings ticked on the dashboard.
---

# Job watch

You run the daily job watch for Matt (Matthieu Cornet), based in Paris and actively looking. Goal: flag relevant new openings as soon as possible after they are posted, at the source rather than on LinkedIn, where they show up late. Matt picks which openings to analyze whenever he wants, the day they are found or later.

## Precondition: the Job Applications folder

Both files live on Matt's computer, in the Job Applications project folder (the folder holding `applications/`, `_assets/`, `_research/` and `applications_tracker.md`).

1. Run `ls $HOME/mnt/` and look for `Job Applications`.
2. If it is not there, call `device_request_folder_access` on `C:\Users\mattc\OneDrive\Documents\Claude\Projects\Job Applications`.
3. If that fails (computer asleep or off, or no computer linked to this run), send Matt one line via SendUserMessage: "Job watch did not run: the Job Applications folder on your computer was not reachable." Then stop. Do not search, and do not fall back to a project file or to chat-only state: an opening reported without being logged is reported again the next day.

## Files and dashboard

| Where | Holds | Who changes what |
|---|---|---|
| `_research/job_sources.md` | How to reach each source: one row per target company (applicant tracking system, jobs URL or access instructions), one row per job board or radar, the search keywords, and the issues met | The watch fills in URLs it finds, the last-checked date and result, and logs issues. Matt and Claude rewrite the access instructions when an issue is fixed |
| `_research/job_watch_log.md` | Every opening the watch has found that matches the target profile, one row per opening under a permanent ID, never deleted; plus the latest report | The watch adds and updates rows. `opportunity-intake` fills the Intake column |
| Job openings dashboard: artifact `b95da0b6-cef1-439f-ab20-d4245191da5f` (https://claude.ai/artifact/Ptc87342pDwaCH3nWFFGyc) | A copy of the log's openings for Matt to browse and tick, plus his ticks | The watch writes the openings; Matt ticks; the analysis clears a tick once the opening is taken in |

The log is the record. The dashboard is a view of it plus Matt's selection: when the two disagree on an opening's data, the log wins.

Read both files at the start of every run. If one is missing, create it with the layout below. Edit them in place with `device_bash` (a short python read-modify-write), never by retyping the file from tool output.

**One-time migration.** If the log has no opening rows yet and the Projects tool shows `claude/job_watch_state.md` or `claude/veille_offres_etat.md`, import it once: openings into the log (first seen = their date first reported, status `listed`, "analyzed on" dates into the Intake column), applicant tracking system URLs into the sources file. After that, never read those project files again.

### `job_watch_log.md` layout

```
# Job watch log

Every opening the job watch found that matches the target profile. Rows are never deleted.

## Latest report (YYYY-MM-DD)

| ID | Company | Title | Key |
|---|---|---|---|

## Openings

| ID | Key | Company | Title | Location | URL | Source | First seen | Last seen | Status | Intake |
|---|---|---|---|---|---|---|---|---|---|---|
```

- **ID**: `J` plus three digits (four once past J999), given when the row is created: the highest existing ID plus one. Never reused, never renumbered.
- **Key**: the opening's URL normalized: lowercase host, no `www.`, no query string or fragment, no trailing slash. Keep the full URL in the URL column.
- **Status**: `listed` (seen on the last successful check of its source) or `no longer listed since YYYY-MM-DD`.
- **Intake**: empty, or `YYYY-MM-DD applications/[slug]/` once `opportunity-intake` has opened the opportunity.

### `job_sources.md` layout

```
# Job watch sources

## Companies

| Company | Tracking system | Jobs URL or access instructions | Last checked | Last result |
|---|---|---|---|---|

## Job boards and radars

| Source | Access instructions | Last checked | Last result |
|---|---|---|---|

## Search keywords

## Open issues

| Since | Source | What happened | Runs affected |
|---|---|---|---|

## Resolved issues

| Since | Resolved | Source | What happened | Fix |
|---|---|---|---|---|
```

**Last result** is one of: `ok, N matching`, `ok, none matching`, `blocked: [reason]`, `not found`.

### Dashboard data

Written with the artifact tools (`db_write`, `db_list`, `db_query`, `db_get`) on slug `b95da0b6-cef1-439f-ab20-d4245191da5f`:

| Path | Fields |
|---|---|
| `openings/[ID]` | `key`, `company`, `title`, `location`, `url`, `source`, `firstSeen`, `lastSeen`, `status`, `intake`: the log row, same values |
| `ticks/[ID]` | `id`, `at`: present while Matt has the opening ticked |
| `meta/watch` | `lastRun` (date), `latestReport` (list of the IDs in the latest report) |
| `meta/request` | `ids`, `at`: what the dashboard button last asked for |

`db_write` takes at most 50 ops per call, and an op on a document that already exists needs its `ifVersion` (from `db_list` or `db_query`). Send one call at a time and wait 2 seconds between calls.

## Target profile
- Senior: Head of, Director, VP, Lead, Global Head, COO. No junior roles, nothing asking for under 8 years of experience.
- Functions: Customer Success, Professional Services, client implementation and delivery, Customer Operations, AI deployment and transformation (AI deployment, AI adoption, applied AI), product leadership, business transformation, PMO and programme management, solutions and pre-sales.
- Location: Paris, Île-de-France, or remote France or Europe. Exclude US-based roles.
- Posting language: French or English.
- Senior freelance missions (AI project director, AI Product Lead, Data Product Lead) count too.

## Sources, in this order

The targets, the boards and the keywords are the rows of `_research/job_sources.md`. To add or drop a target, edit that file, not this skill.

1. Each company row: use the access instructions as written. When a row says `not found yet`, look for the company's applicant tracking system (Welcome Kit, Lever, Greenhouse, Ashby, Workday, SmartRecruiters, Teamtailor) or careers page, and write the URL you used into the row.
2. Welcome to the Jungle: the targets' company pages, plus a keyword search filtered on Paris.
3. Indeed (Indeed connector if available), same keywords, location Paris.
4. Startup radar: recent French funding rounds (Maddyness, Les Echos Start, FrenchWeb, Eldorado) of EUR 10M or more that announce hiring, even with no posting yet, since that is the moment to write to the founder. Also VC portfolio job boards (Partech, Alven, Serena, Breega, Elaia, Isai, Daphni, XAnge, Eurazeo) when accessible.

**Browser.** Many tracking systems (Workday, SmartRecruiters, some Welcome Kit pages) build their job list in JavaScript, so WebFetch returns an empty page. When WebFetch gets no job list from a company page, open the same URL in the browser (Claude in Chrome, or the built-in browser if Chrome is not reachable) and read the list there. When the browser works where WebFetch did not, add `browser` to that company's access instructions so the next run goes straight to it. If no browser is reachable during the run, log one open issue `no browser in this run` and list the companies it affected.

Do not use LinkedIn. If a page refuses access, log it (below) and move to the next source without any workaround.

## Each run

1. For every source checked, update its row in `job_sources.md`: Last checked (today), Last result, and the URL actually used if it changed (redirect, new tracking system).
2. **Issues.** When a source fails (blocked, timeout, page empty or unreadable, URL gone, connector error), add a row to Open issues with today's date, what was seen, and `1` in Runs affected. If an open issue already exists for that source, increment Runs affected instead of adding a row. When a source with an open issue works again, move the issue to Resolved issues with today's date and `worked again, no change` (or the URL change that made it work). Never change the access instructions of a company to work around a block: say what happened and leave the fix to Matt.
3. For each opening found that matches the target profile, decide whether it is new:
   - Its key is in the log: known. Update Last seen, and Status back to `listed` if needed.
   - Its key is not in the log but a row has the same company and the same title (ignoring case, accents and punctuation): known, reposted under a new URL. Update that row's URL, key and Last seen.
   - Otherwise: new. Add a row with the next ID (First seen and Last seen today, Status `listed`, Intake empty) and include it in the report.
4. For each source whose check succeeded, set every `listed` opening from that source that was not seen today to `no longer listed since [today]`. Leave openings from a failed source untouched.
5. If at least one opening is new, replace the Latest report section with the table of the new openings (ID, company, title, key). On days with nothing new, leave it untouched.
6. **Refresh the dashboard**, once the log is written:
   - `db_list` the `openings` collection (limit 1000, follow the cursor). For each log row, `set` `openings/[ID]` when the document is missing or any field differs from the log (with `ifVersion` when it exists).
   - `set` `meta/watch` to today and the IDs of the Latest report section.
   - `db_list` `ticks`, and `delete` the tick of every opening whose Intake is filled.
   - If the artifact tools are not available in this run, or a write keeps failing, log an open issue with source `Job openings dashboard` and carry on: the log is still complete.

## Report
Short message to Matt in English via SendUserMessage, no em dash:
- "New openings": table ID | company | title | location | posting date if known | link | one line on why it fits. Openings posted in the last 24 h first.
- "Startups to approach": 0 to 3 lines, funding round + hiring signal + founder or CEO name. No ID: they have no posting to analyze.
- If any source failed today: one line "Sources with issues: [names]. Details in _research/job_sources.md."
- Last lines, only if there is at least one new opening: "To run the analysis, reply with the IDs (e.g. J054 J056) or 'all', today or any later day. Or tick openings on the dashboard: https://claude.ai/artifact/Ptc87342pDwaCH3nWFFGyc"
- If nothing is new: "Nothing new today." (plus the sources line if any failed, and the dashboard link).

**Attach both files.** After the report, and after the summary of an analysis, attach the current `_research/job_watch_log.md` and `_research/job_sources.md` to the conversation: stage them with `device_stage_files` (paths `C:\Users\mattc\OneDrive\Documents\Claude\Projects\Job Applications\_research\job_watch_log.md` and `...\job_sources.md`), then send the staged copies with SendUserFile in one call. Stage them only once every edit of the run is written, since a card is a fixed copy. Do it on days with nothing new too.

Never invent an opening, a date or a link: write only what was seen on the page. Flag an uncertain posting date as uncertain. Do not apply and do not contact anyone.

## Analyze selected openings

Runs when Matt replies to a report, when he asks in any session to analyze openings, and in every run of the "Analyze job openings" scheduled task (which the dashboard button starts). Run the precondition first.

1. **Work out the selection**, in this order:
   - IDs written in the message (in a reply, or appended to the Analyze job openings task's prompt): those IDs, and only those.
   - "all" (or "tout"): every ID in the Latest report section of the log.
   - Plain numbers (1, 2, 3) from a report sent before IDs existed: the opening at that position in the Latest report section.
   - Otherwise, or when the message says "ticked": `db_list` `ticks` on the dashboard and take those IDs. If the artifact tools are not available, say so and ask Matt for the IDs.
2. Resolve each ID in the log. Flag an ID that does not exist and process the others. Skip an opening whose Intake is already filled, say so (its folder exists), and delete its tick if it has one. If nothing is left, say "Nothing to analyze: no opening ticked or named." and stop.
3. For each opening, launch a separate subagent (Agent tool, type general-purpose, run_in_background false), one after another and never in parallel, so two openings never write to `applications_tracker.md` or the log at the same time. Exact prompt:
   "check fit and prep resume if good [URL]
   (Opening: [ID], [company], [title]. Matt is not available to answer questions: make the most reasonable assumption, record it in the opening's notes.md, and carry on. Do not apply and do not contact anyone. End with a 5-line summary: fit verdict, folder path, files produced, assumptions made.)"
   The subagent follows the job-search skills as in a session Matt started himself: opportunity-intake first (its own `applications/[slug]/` folder, and the Intake column of the log), then job-fit-analyzer, then resume-tailor only if the verdict is favorable.
4. If the Agent tool is not available: process the openings in this conversation, one at a time, finishing each one completely (folder, analysis, resume if any) before the next, and reloading the job-search skills for each.
5. After each opening: check its Intake cell is filled in the log (fill it with the date and folder from the subagent's summary if intake did not), then `merge` the same `intake` value into `openings/[ID]` on the dashboard and `delete` `ticks/[ID]`.
6. At the end, send Matt a summary in English via SendUserMessage: table ID | company | verdict | folder | resume produced (yes / no), then any assumptions made. Send each resume produced with SendUserFile so it shows as a clickable file card, then attach the two `_research/` files as above.

## Rules
- No opening-specific file in the project root, and no dated copy of the log or of the sources file.
- Never delete a row of the log, never reuse or change an ID. Never delete an issue: move it to Resolved.
- Never write a tick yourself: ticks are Matt's selection. Only delete one once its opening is taken in.
- No angle brackets in this skill's description (they trigger an XML warning on sync).
