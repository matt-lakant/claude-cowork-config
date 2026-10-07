---
name: cs-brain
description: "Sets up and runs the customer success brain: one shared folder of plain-text account, people, signal, rule and handoff files that every cs- skill reads and writes. Holds the shared rules, the file formats and the seven routines (intake, account librarian, signal watcher, briefing, handoff, rules keeper, reporter). Use when Matt says \"set up the CS brain\", \"run the intake agent\", \"run the signal watcher\", \"wrap up\" (CS day), \"run the reporter\", asks which CS skill to use, or asks where the brain lives. For one task by name, use that cs- skill directly."
---

# CS Brain (orchestrator)

One shared folder of plain-text files gives a customer success team a single memory of every
account. Twenty-two skills read from it and write back to it; seven routines chain them into
standing jobs. This skill owns the setup, the formats, the shared rules and the routines.

Adapted from Kevin Lau's "Claude Brain System for Customer Success" (The Customer Continuum,
kevinkennethlau.substack.com). The prompts were rewritten as skills and the seven agents as the
routines below.

## Where the brain lives

Resolve it in this order and say which one was used:

1. A folder named `brain` containing `INDEX.md` inside a folder connected to this session.
2. The default: `C:\Users\mattc\OneDrive\Documents\Claude\Projects\Customer Success\brain\`.
   If the parent is not connected, request folder access on it straight away.
3. No linked computer (phone, cloud only): the docs of the claude.ai Project this session is
   bound to, under `brain/...` paths (Projects tool, `project_read` / `project_write`).
4. None of these: say so and stop. Do not build a brain in a temporary location.

If the team keeps the brain on a shared drive or SharePoint, use that path once Matt names it.

The brain has subfolders because every skill addresses its files by path. This is a deliberate
exception to the flat project-folder rule. **Never create or write the brain inside
`claude-cowork-config`.** That repo holds configuration only.

**Before importing any customer data**, confirm with Matt that the company's policy allows
customer data in AI tools. Ask once per brain and record the answer as the first line of
`rules.md`.

## Setup (first run)

Create this structure. Copy the starter files from the `templates/` folder next to this
`SKILL.md`; create the other folders empty.

```
brain/
  INDEX.md          one line per file: path · what it is · last touched
  rules.md          standing rules the team has agreed
  signals-log.md    dated one-line signals, newest on top
  accounts/         one file per account (acme.md); _TEMPLATE.md is the shape
  people/           one file per customer contact who matters
  handoffs/         one file per day (2026-09-17.md)
  imports/          raw exports of old chats, before they are filed
  imports/done/     processed imports, renamed with the processing date
  reports/          renewal reports and readouts
  archive/          anything retired, with the date in the file name
  agents/           custom routines built with cs-agent-builder
```

You do not need every skill on day one. Start with four: `cs-account-file-builder` on the live
accounts, `cs-call-note-filer` after each call, `cs-session-opener` before each piece of
account work, and `cs-memory-keeper` at the end of each session. Add the rest as needed.

## File formats

| File | Format |
|---|---|
| `accounts/<slug>.md` | `templates/account-template.md`: Snapshot (plan, seats, renewal date, owner) · Why they bought · What success looks like (their words) · People · Promises we made (table) · History (dated) · Risks · Open questions |
| `people/<first-last>.md` | Name, account, role, cares about, last contact `YYYY-MM-DD`, warmth (warm, neutral, cold, unknown), then dated notes |
| `signals-log.md` | Newest on top. `date · account · signal · good/bad/unclear · source` |
| `rules.md` | `When X happens, we do Y within Z days. Owner. How we check.` |
| `handoffs/<date>.md` | Under 25 lines: per account touched, what happened, promised, waiting on them, waiting on us; not done; first three for tomorrow |
| `reports/<report>_<date>.md` | Renewal reports, readouts, share packs |
| `INDEX.md` | `path · what it is · last touched YYYY-MM-DD`. Update it on every write. |

Slugs are lowercase with hyphens (`acme-corp.md`, `jane-doe.md`).

## The skills

| Stage | Skill | Job |
|---|---|---|
| Memory between sessions | `cs-memory-keeper` | Saves what mattered in this session to the brain |
| | `cs-session-opener` | Loads only the context a task needs, with a stale list |
| Importing past chats | `cs-chat-importer` | One exported chat into dated lines filed against the right account |
| | `cs-chat-history-miner` | Ranks a batch of old chats by what the brain would gain |
| Account context | `cs-account-file-builder` | Builds the one-page account file everything else depends on |
| | `cs-people-map` | Who decides, who uses it, who went quiet, who left |
| | `cs-promise-tracker` | Every promise made to a customer and whether it was kept |
| Call notes and signals | `cs-call-note-filer` | Transcript or notes into dated lines in the account file |
| | `cs-quiet-account-spotter` | Accounts gone quiet before the forecast notices |
| | `cs-signal-log` | One running log of small signals; flags real patterns |
| Search | `cs-account-search` | Answers a question about a customer with a source per claim |
| | `cs-team-answer-finder` | Who already handled a situation like this, and what they did |
| Lessons into rules | `cs-lost-renewal-review` | Earliest catchable moment in a lost or shrunk renewal |
| | `cs-rule-writer` | A lesson into a checkable standing rule |
| Own routines | `cs-agent-builder` | A new routine for a job Matt keeps doing by hand |
| Daily briefs | `cs-morning-brief` | The day in one screen |
| | `cs-end-of-day-handoff` | Where everything stands, so anyone can pick it up cold |
| Keeping it clean | `cs-memory-cleaner` | Stale, duplicate and orphaned notes, with a proposed tidy-up |
| | `cs-conflict-checker` | Places where the brain says two things about one fact |
| Reporting | `cs-renewal-report` | Weekly renewal report with evidence behind every status |
| | `cs-exec-readout` | The report as a one-page readout for a leader, behind a private link |
| Sharing | `cs-team-share-pack` | What sales, support or product need, without the raw notes |

## Routines

Each routine is a standing job that runs several skills in order. Matt asks for it by name
("run the intake agent", "wrap up"). Every routine that writes stops at the change list and
waits for approval. If a file a routine needs is missing or empty, it says so and stops.

Every routine also follows these limits: never contacts a customer, never deletes a file,
never invents data.

### A1. Intake

- **When:** something lands in `brain/imports/`, or Matt pastes a transcript or notes. If a
  recording connector (such as Plaud) is connected, Matt may point at a recording instead.
- **Reads:** `imports/`, `accounts/`, `people/`. **May write:** `accounts/`, `people/`,
  `signals-log.md` (adds lines only), `imports/done/`.
- **Steps:** work out what each item is (old chat, transcript, notes, email). Run
  `cs-chat-history-miner` first if there are ten or more chats, then `cs-chat-importer` on
  chats and `cs-call-note-filer` on transcripts and notes. Show the lines to add, grouped by
  file. File them once approved. Move each processed item to `imports/done/` with today's date
  in the name.
- **Never:** file a draft as sent; overwrite an existing line (add and flag conflicts); import
  anything marked confidential.

### A2. Account librarian

- **When:** weekly, and whenever sales hands over a new account.
- **Reads:** `accounts/`, `people/`. **May write:** `accounts/`, `people/`.
- **Steps:** for a new account, run `cs-account-file-builder` from whatever sales handed over.
  For existing accounts, list the UNKNOWNs and anything older than 60 days. Run
  `cs-people-map` and `cs-promise-tracker` on every account inside 120 days of renewal. Return
  one list: what to go and find out this week, by account.
- **Never:** fill an UNKNOWN with a guess; change a renewal date, seat count or value without a
  source.

### A3. Signal watcher

- **When:** Monday morning, and whenever lines are added to the signal log.
- **Reads:** `accounts/`, `signals-log.md`. **May write:** `signals-log.md` (adds lines only).
- **Steps:** run `cs-quiet-account-spotter` across all accounts, then the pattern check from
  `cs-signal-log`. Return the three accounts to call this week, the reason for each and the
  lines that back it.
- **Never:** call one signal a trend; mark an account "at risk" in its file (tell Matt; he
  decides).

### A4. Briefing

- **When:** weekday mornings, and before any customer meeting.
- **Reads:** `handoffs/`, `accounts/`, `people/`, `signals-log.md`, `rules.md`.
  **May write:** nothing.
- **Steps:** run `cs-morning-brief` at the start of the day. Before each customer call, run
  `cs-session-opener` for that account. Check `rules.md` and say if a standing rule applies to
  any of today's calls.
- **Never:** pad a brief with general knowledge about the company; hide that a file is stale or
  a handoff is missing.

### A5. Handoff ("wrap up")

- **When:** end of each working day, or when Matt says "wrap up" in a CS session.
- **Reads:** this session, `accounts/`. **May write:** `handoffs/`, `accounts/`,
  `signals-log.md`.
- **Steps:** run `cs-memory-keeper` on today's work and show the change list. Run
  `cs-end-of-day-handoff`. File both once approved, then give the first three things for
  tomorrow.
- **Never:** file something inferred as a fact; pad an empty day; skip showing the change list.

### A6. Rules keeper

- **When:** after any lost or shrunk renewal, and on the first working day of each month.
- **Reads:** all of `brain/`. **May write:** `rules.md`, `INDEX.md`, `archive/`.
- **Steps:** after a loss, run `cs-lost-renewal-review`, then `cs-rule-writer` only if the
  lesson has shown up before. Monthly, run `cs-memory-cleaner` and `cs-conflict-checker`.
  Bring one change list for approval and apply it once Matt says go.
- **Never:** delete anything (archive with a date); write a rule from a single example;
  resolve a conflict on its own (show both versions).

### A7. Reporter

- **When:** Friday, and whenever sales, support or product asks about an account.
- **Reads:** `accounts/`, `signals-log.md`, `handoffs/`. **May write:** `reports/`.
- **Steps:** run `cs-renewal-report` for the next 90 days, then `cs-exec-readout` for whoever
  reads it this week. When another team asks about an account, run `cs-team-share-pack` (and
  `cs-team-answer-finder` if the question is "has anyone seen this before").
- **Never:** report "on track" without evidence on file; put customer contact names or
  confidences on a shared page; send anything.

### Custom routines

Routines built with `cs-agent-builder` are saved in `brain/agents/<name>.md`. When Matt asks for
a routine that is not listed above, look there and run it as written. To make one part of the
plugin, add it to this section through `config-sync`.

### Running routines on a schedule

Only when Matt asks. A scheduled run has nobody to approve a change list, so a scheduled
routine stops at the change list and saves it to `reports/pending-changes_<date>.md` instead of
writing to the brain. Read-only routines (A4, A3's report) can run unattended.

## Shared rules (each skill repeats a short version; this is the reference copy)

1. **Find the brain first** (above). Missing or empty file: say so and stop.
2. **Only what was said.** File facts, decisions, promises and open questions from the
   sources. Anything inferred is labelled INFERRED and kept out until Matt confirms.
3. **UNKNOWN beats a guess.** Never invent a renewal date, seat count, plan, contract value or
   a person's role.
4. **Change list before writing.** Show `File | Add | Change | Conflict`, then write only after
   Matt says go. Add lines; never overwrite an existing one silently.
5. **Archive, never delete.** Move retired files to `archive/` with the date in the name.
6. **Sources on every claim.** File and date after each claim. When files disagree, show both
   and say which is newer.
7. **Dates.** `YYYY-MM-DD`. Lines imported from old material keep the material's date, not
   today's.
8. **Customer confidences stay out** of shared outputs (readouts, share packs) and out of the
   brain entirely if Matt says so.
9. **Never contact a customer, never send anything.** Drafts only. Any message written in
   Matt's name goes through `writing-voice`.
10. **Keep `INDEX.md` current** on every write.
11. **Surface deliverables.** Reports, readouts, share packs and handoffs are sent as file
    cards after they are saved. Brain line edits are reported as a list of files changed.
