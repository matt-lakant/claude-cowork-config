---
name: job-watch
description: Daily watch for senior job openings for Matt, at the source (target companies' applicant tracking systems, Welcome to the Jungle, Indeed, recent funding rounds). Registers every matching opening in _research/job_watch_log.md, reports only the new ones in a numbered table, and keeps the access instructions and issues for each source in _research/job_sources.md. When Matt replies with numbers or "all", runs "check fit and prep resume if good" for each selected opening in a separate subagent. Use for the scheduled job-watch task and for any numbered reply to a job-watch report.
---

# Job watch

You run the daily job watch for Matt (Matthieu Cornet), based in Paris and actively looking. Goal: flag relevant new openings as soon as possible after they are posted, at the source rather than on LinkedIn, where they show up late.

## Precondition: the Job Applications folder

Both files live on Matt's computer, in the Job Applications project folder (the folder holding `applications/`, `_assets/`, `_research/` and `applications_tracker.md`).

1. Run `ls $HOME/mnt/` and look for `Job Applications`.
2. If it is not there, call `device_request_folder_access` on `C:\Users\mattc\OneDrive\Documents\Claude\Projects\Job Applications`.
3. If that fails (computer asleep or off, or no computer linked to this run), send Matt one line via SendUserMessage: "Job watch did not run: the Job Applications folder on your computer was not reachable." Then stop. Do not search, and do not fall back to a project file or to chat-only state: an opening reported without being logged is reported again the next day.

## Files

Both are in `_research/` and keep fixed names (they are standing files, not dated research notes).

| File | Holds | Who changes what |
|---|---|---|
| `_research/job_sources.md` | How to reach each source: one row per target company (applicant tracking system, jobs URL or access instructions), one row per job board or radar, the search keywords, and the issues met | The watch fills in URLs it finds, the last-checked date and result, and logs issues. Matt and Claude rewrite the access instructions when an issue is fixed |
| `_research/job_watch_log.md` | Every opening the watch has found that matches the target profile, one row per opening, never deleted; plus the latest numbered report | The watch adds and updates rows. `opportunity-intake` fills the Intake column |

Read both at the start of every run. If one is missing, create it with the layout below. Edit them in place with `device_bash` (a short python read-modify-write), never by retyping the file from tool output.

**One-time migration.** If the log has no opening rows yet and the Projects tool shows `claude/job_watch_state.md` or `claude/veille_offres_etat.md`, import it once: openings into the log (first seen = their date first reported, status `reported`, "analyzed on" dates into the Intake column), applicant tracking system URLs into the sources file. After that, never read those project files again.

### `job_watch_log.md` layout

```
# Job watch log

Every opening the job watch found that matches the target profile. Rows are never deleted.

## Latest report (YYYY-MM-DD)

| # | Company | Title | Key |
|---|---|---|---|

## Openings

| Key | Company | Title | Location | URL | Source | First seen | Last seen | Status | Intake |
|---|---|---|---|---|---|---|---|---|---|
```

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
   - Otherwise: new. Add a row (First seen and Last seen today, Status `listed`, Intake empty) and include it in the report.
4. For each source whose check succeeded, set every `listed` opening from that source that was not seen today to `no longer listed since [today]`. Leave openings from a failed source untouched.
5. If at least one opening is new, replace the Latest report section with the numbered table exactly as sent. On days with nothing new, leave it untouched.

## Report
Short message to Matt in English via SendUserMessage, no em dash:
- "New openings": table # | company | title | location | posting date if known | link | one line on why it fits. Number rows from 1. Openings posted in the last 24 h first.
- "Startups to approach": 0 to 3 lines, funding round + hiring signal + founder or CEO name. No numbers: they have no posting to analyze.
- If any source failed today: one line "Sources with issues: [names]. Details in _research/job_sources.md."
- Last line, only if there is at least one opening: "To run the analysis, reply with the numbers (e.g. 2 5) or 'all'."
- If nothing is new: "Nothing new today." (plus the sources line if any failed).

Never invent an opening, a date or a link: write only what was seen on the page. Flag an uncertain posting date as uncertain. Do not apply and do not contact anyone.

## When Matt replies with numbers
Matt can reply in the run's conversation, the same day or later, with numbers ("2 5", "1, 3") or "all" ("tout" means the same).
1. Run the precondition, re-read `_research/job_watch_log.md` and resolve each number in Latest report. Flag any number that does not exist and process the others. Skip an opening whose Intake is already filled and say so (its folder exists).
2. For each opening, launch a separate subagent (Agent tool, type general-purpose, run_in_background false), one after another and never in parallel, so two openings never write to `applications_tracker.md` or the log at the same time. Exact prompt:
   "check fit and prep resume if good [URL]
   (Opening: [company], [title]. Matt is not available to answer questions: make the most reasonable assumption, record it in the opening's notes.md, and carry on. Do not apply and do not contact anyone. End with a 5-line summary: fit verdict, folder path, files produced, assumptions made.)"
   The subagent follows the job-search skills as in a session Matt started himself: opportunity-intake first (its own `applications/[slug]/` folder, and the Intake column of the log), then job-fit-analyzer, then resume-tailor only if the verdict is favorable.
3. If the Agent tool is not available: process the openings in this conversation, one at a time, finishing each one completely (folder, analysis, resume if any) before the next, and reloading the job-search skills for each.
4. After each opening, check that its Intake cell is filled; if intake ran but did not fill it, fill it with the date and the folder from the subagent's summary.
5. At the end, send Matt a summary in English via SendUserMessage: table # | company | verdict | folder | resume produced (yes / no), then any assumptions made. Send each resume produced with SendUserFile so it shows as a clickable file card.

## Rules
- No opening-specific file in the project root, and no dated copy of the log or of the sources file.
- Never delete a row of the log. Never delete an issue: move it to Resolved.
- No angle brackets in this skill's description (they trigger an XML warning on sync).
