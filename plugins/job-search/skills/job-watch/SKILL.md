---
name: job-watch
description: Daily watch for senior job openings for Matt, at the source (target companies' applicant tracking systems, Welcome to the Jungle, Indeed, recent funding rounds). Sends a numbered table of new openings. When Matt replies with numbers or "all", runs "check fit and prep resume if good" for each selected opening in a separate subagent. Use for the scheduled job-watch task and for any numbered reply to a job-watch report.
---

# Job watch

You run the daily job watch for Matt (Matthieu Cornet), based in Paris and actively looking. Goal: flag relevant new openings as soon as possible after they are posted, at the source rather than on LinkedIn, where they show up late.

## Target profile
- Senior: Head of, Director, VP, Lead, Global Head, COO. No junior roles, nothing asking for under 8 years of experience.
- Functions: Customer Success, Professional Services, client implementation and delivery, Customer Operations, AI deployment and transformation (AI deployment, AI adoption, applied AI), product leadership, business transformation, PMO and programme management, solutions and pre-sales.
- Location: Paris, Île-de-France, or remote France or Europe. Exclude US-based roles.
- Posting language: French or English.
- Senior freelance missions (AI project director, AI Product Lead, Data Product Lead) count too.

## Sources, in this order
1. Target companies' career pages, through their applicant tracking system when they have one (Welcome Kit, Lever, Greenhouse, Ashby, Workday, SmartRecruiters, Teamtailor). Targets: Elax, Doctolib, Anthropic, OpenAI, Mistral AI, ElevenLabs, Datadog, Celonis, Spiko, Fabriq, Alice & Bob, UpSlide, Artefact, Theodo, Valiantys, EPAM Systems, Mister IA, Rakam AI, Bravi, AlixPartners, Kyndryl, Cornerstone OnDemand, OneStream, Merge, Edda, Wolters Kluwer, Wrike / Klaxoon, Wivoo, BGC Group, Inetum, Givaudan.
2. Welcome to the Jungle: the targets' company pages, plus a keyword search (Head of Customer Success, Head of Customer Operations, Director Professional Services, Head of AI, AI Deployment, Head of Delivery, Directeur de programme IA) filtered on Paris.
3. Indeed (Indeed connector if available), same keywords, location Paris.
4. Startup radar: recent French funding rounds (Maddyness, Les Echos Start, FrenchWeb, Eldorado) of EUR 10M or more that announce hiring, even with no posting yet, since that is the moment to write to the founder. Also VC portfolio job boards (Partech, Alven, Serena, Breega, Elaia, Isai, Daphni, XAnge, Eurazeo) when accessible.

Do not use LinkedIn. If a page refuses access, move to the next one without any workaround.

## State between runs
Project file `claude/job_watch_state.md` (Projects tool: project_read, then project_write). If it does not exist and `claude/veille_offres_etat.md` does, copy that content into the new file once and use only the new file from then on. The file holds:
- the applicant tracking system URL for each target, filled in on the first pass and reused after;
- openings already reported: company, title, URL, date first reported, and "analyzed on [date]" once Matt has had it analyzed;
- a "Latest report ([date])" section: the # | company | title | URL table exactly as sent. Replace it on every run that sends at least one opening; leave it untouched on days with nothing new.

Create the file if it is missing. Report only openings absent from the list, then update the file. Purge openings reported more than 60 days ago.

## Report
Short message to Matt in English via SendUserMessage, no em dash:
- "New openings": table # | company | title | location | posting date if known | link | one line on why it fits. Number rows from 1. Openings posted in the last 24 h first.
- "Startups to approach": 0 to 3 lines, funding round + hiring signal + founder or CEO name. No numbers: they have no posting to analyze.
- Last line, only if there is at least one opening: "To run the analysis, reply with the numbers (e.g. 2 5) or 'all'."
- If nothing is new: a single line "Nothing new today."

Never invent an opening, a date or a link: write only what was seen on the page. Flag an uncertain posting date as uncertain. Do not apply and do not contact anyone.

## When Matt replies with numbers
Matt can reply in the run's conversation, the same day or later, with numbers ("2 5", "1, 3") or "all" ("tout" means the same).
1. Re-read `claude/job_watch_state.md` and resolve each number in "Latest report". Flag any number that does not exist and process the others.
2. For each opening, launch a separate subagent (Agent tool, type general-purpose, run_in_background false), one after another and never in parallel, so two openings never write to `applications_tracker.md` at the same time. Exact prompt:
   "check fit and prep resume if good [URL]
   (Opening: [company], [title]. Matt is not available to answer questions: make the most reasonable assumption, record it in the opening's notes.md, and carry on. Do not apply and do not contact anyone. End with a 5-line summary: fit verdict, folder path, files produced, assumptions made.)"
   The subagent follows the job-search skills as in a session Matt started himself: opportunity-intake first (its own `applications/[slug]/` folder), then job-fit-analyzer, then resume-tailor only if the verdict is favorable.
3. If the Agent tool is not available: process the openings in this conversation, one at a time, finishing each one completely (folder, analysis, resume if any) before the next, and reloading the job-search skills for each.
4. After each opening, mark it "analyzed on [date]" in the state file.
5. At the end, send Matt a summary in English via SendUserMessage: table # | company | verdict | folder | resume produced (yes / no), then any assumptions made. Send each resume produced with SendUserFile so it shows as a clickable file card.

## Rules
- No opening-specific file in the project root.
- No angle brackets in this skill's description (they trigger an XML warning on sync).
