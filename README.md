# claude-cowork-config

Matt Cornet's personal Claude / Cowork configuration, under version control.

**This repository is the source of truth.** The skills Claude runs from
(`~/.claude/skills/synced/...`) are a read-only cache that the platform syncs
down. Edit here, publish from here.

## Layout

```
.claude-plugin/marketplace.json    marketplace manifest (lists the plugins below)
plugins/
  job-search/                      the job application pipeline
    .claude-plugin/plugin.json
    skills/<skill-name>/SKILL.md
  general/                         domain-agnostic working skills
    .claude-plugin/plugin.json
    skills/<skill-name>/SKILL.md
  venture-lab/                     generating and killing business ideas
    .claude-plugin/plugin.json
    skills/<skill-name>/SKILL.md
  tax-team/                        seven-specialist US tax review
    .claude-plugin/plugin.json
    skills/<skill-name>/SKILL.md
  customer-success/                CS brain: account memory, signals, renewals
    .claude-plugin/plugin.json
    skills/<skill-name>/SKILL.md
  big-consulting/                  150 consulting skills in 15 practices
    .claude-plugin/plugin.json
    skills/<skill-name>/SKILL.md
```

> Personal data is **not** versioned here. Removed 2026-09-10. Matt's identity and
> writing voice live in the Obsidian vault (`Notes/Matt Cornet.md`, `Notes/Writing voice.md`),
> which is versioned in its own private repo. Job-search working files stay in OneDrive under
> `Projects/Job Applications/`. This repo holds configuration only.

Skills are discovered one level deep: `skills/<skill-name>/SKILL.md`. The
directory name is the skill name. A category folder cannot be inserted between
`skills/` and the skill directory, which is why grouping is done with **plugins**
rather than nested folders.

## Plugins

### `job-search` (12 skills)

The pipeline, roughly in the order it runs:

| Skill | Role in the pipeline |
|---|---|
| `opportunity-intake` | Front door: confirms the opportunity, creates `applications/<slug>/` and its `notes.md`, routes to the right skill |
| `job-fit-analyzer` | Triage a posting before investing: fit score, gap analysis, go/no-go |
| `company-overview` | Research the company into `company_overview.md` (prerequisite for several skills) |
| `resume-tailor` | Tailor the master resume to the posting; ATS keywords, requirement mining |
| `resume-redteam` | Mandatory adversarial gate: a hostile recruiter tries to reject the resume |
| `cover-letter` | Writes the cover letter after Matt returns the final CV: his hook answers, §5.4 structure, AI-tell self-check |
| `cover-letter-redteam` | Mandatory gate: a recruiter who has read too many generated letters attacks AI tells, genericness, CV alignment, over-claims |
| `interview-prep` | Predicted questions + STAR answers grounded in real experience |
| `recruiter-followup` | Follow-ups, thank-yous, ghosted-process nudges |
| `offer-negotiator` | Counter-offer emails, verbal scripts, scenario plans |
| `application-tracker` | Maintains `applications_tracker.md` and follow-up due dates |
| `asset-updater` | Closes the loop: propagates Matt's edits back into the master assets; returned-file mode learns from the CV or letter he sends back |

### `general` (4 skills)

| Skill | Purpose |
|---|---|
| `config-sync` | Governs edits to this repo: where a skill file goes, the mandatory version bump, byte-level verification, and the commit message Matt pastes in GitHub Desktop (Claude never commits) |
| `tackle-task` | Kickoff for work no dedicated skill covers: frames task + success criteria, gathers context before starting |
| `writing-voice` | Any text written in Matt's name: reads `Notes/Writing voice.md` in the vault (single source, no copy here), falls back to the preference block on claude.ai and says so, flags drift between the two; called by `cover-letter` and `cover-letter-redteam` |
| `skeptical-person` | Reads a document as its most skeptical reader: five hardest questions with the line that invites each, which are already answered, the fact and owner for the rest, and the one assumption that sinks it. Shows gaps, rewrites nothing |

### `venture-lab` (2 skills)

Both write into the Obsidian vault and both default to "no business here".

| Skill | Purpose |
|---|---|
| `paper-digest` | Reads a paper or article Matt shares, explains the mechanism, judges it against a 7-gate rubric, files a `type: source` note with the PDF |
| `idea-pressure-test` | Pressure-tests an idea Matt already has: 11 gates, three adversaries (investor, incumbent PM, target buyer), six verdicts, a pre-registered kill test, filed as a `type: idea` note with dated re-tests |

### `tax-team` (8 skills)

Seven specialists run in order, each reading the reports of the ones before it, plus an
orchestrator. US federal + state, resident filer. Every finding gets a dollar range and one
verdict: FINE AS IS / WORTH FIXING / BRING IT TO A STRATEGIST. Reports and tax documents live in
`OneDrive\Documents\Claude\Projects\Tax Team\`, never here. Adapted from Wally Darling's public
Notion page "The Claude Tax Team: 7 Specialists" (Darling Financial Group), rewritten as skills.

| Skill | Purpose |
|---|---|
| `tax-team` | Orchestrator: setup, document checklist, run order and skip rules, shared rules, cadence (compliance quarterly, full team each October) |
| `tax-income-analyst` | 1. Income by bracket, marginal vs effective rate, SE tax / NIIT / under-withholding flags, carryforwards; writes the Income Map |
| `tax-entity-specialist` | 2. Sole prop vs S-corp vs C-corp at real profit, S-corp salary floor and ceiling, salary sensitivity for QBI and retirement |
| `tax-retirement-specialist` | 3. Contributed vs limits, room above the 401(k) (profit sharing, cash balance / DB), deadlines with days left |
| `tax-deduction-specialist` | 4. Claimed deductions with substantiation check, commonly missed ones (accountable plan, Augusta rule, vehicle, depreciation elections) |
| `tax-investment-specialist` | 5. Loss harvesting with wash-sale checks, Roth conversion room and backdoor Roth, RSU / ISO / ESPP, gains timing |
| `tax-real-estate-exit` | 6. Cost seg (usable vs suspended), REPS test, QSBS tier clocks, sale scenarios (1031, DST, installment, opportunity zones) |
| `tax-compliance-specialist` | 7. Safe harbor by quarter, screening flags, paperwork list, dated calendar, one-page brief for the tax meeting |

### `customer-success` (23 skills)

A shared "brain" folder of plain-text files (accounts, people, signals log, rules, daily
handoffs, reports) that every skill reads and writes. Default location
`OneDrive\Documents\Claude\Projects\Customer Success\brain\`, never here; it keeps
subfolders because skills address files by path. Every skill shows a change list before
writing, marks gaps UNKNOWN, never contacts a customer. Adapted from Kevin Lau's "Claude Brain
System for Customer Success" (The Customer Continuum); the 22 prompts became skills and the 7
agents became routines inside `cs-brain`.

| Skill | Purpose |
|---|---|
| `cs-brain` | Orchestrator: brain location and setup (templates bundled), file formats, shared rules, the 7 routines (intake, librarian, signal watcher, briefing, handoff, rules keeper, reporter) and custom routines in `brain/agents/` |
| `cs-memory-keeper` | Saves what mattered in a session to the brain, as a change list |
| `cs-session-opener` | Loads only the files a task needs; 10-line recap and stale list |
| `cs-chat-importer` | One exported chat into dated lines against the right account; drafts stay DRAFT |
| `cs-chat-history-miner` | Ranks a batch of old chats by what the brain would gain |
| `cs-account-file-builder` | The one-page account file; UNKNOWN rather than a guess |
| `cs-people-map` | Who signed, uses, decides; warmth; single-threaded flag |
| `cs-promise-tracker` | Every commitment made and its status, ranked by renewal proximity |
| `cs-call-note-filer` | Transcript or notes into summary, verbatim quotes and dated lines |
| `cs-quiet-account-spotter` | Active / slowing / quiet against days to renewal |
| `cs-signal-log` | Dated one-line signals; flags patterns (3 in 30 days) |
| `cs-account-search` | Answers about a customer with file and date per claim |
| `cs-team-answer-finder` | Similar past situations, what was tried, who to ask |
| `cs-lost-renewal-review` | Timeline and earliest catchable moment of a loss |
| `cs-rule-writer` | Lesson into a checkable "when X, we do Y within Z days" rule |
| `cs-agent-builder` | New routine for a repeated job, saved to `brain/agents/` |
| `cs-morning-brief` | The CS day in one screen (not the general `morning` skill) |
| `cs-end-of-day-handoff` | Under-25-line handoff anyone can act on |
| `cs-memory-cleaner` | Duplicates, stale files, orphans; archive, never delete |
| `cs-conflict-checker` | Two values for one fact, shown side by side, never resolved alone |
| `cs-renewal-report` | Weekly renewal report, evidence behind every status |
| `cs-exec-readout` | One-page readout for a leader as a private Docs artifact |
| `cs-team-share-pack` | Brief for sales, support or product without raw notes or confidences |

### `big-consulting` (151 skills)

150 single-deliverable consulting skills in 15 practices of ten, each listing its inputs, method,
output format and quality checks, plus `big-consulting`, an index and router (one skill, one
practice end to end, or the full engagement) with shared rules: real inputs first, outputs to the
project folder, name the decision that stays with Matt. The full skill index is in
`skills/big-consulting/SKILL.md`.

Source: Grant Baldwin (geniant), "Big Consulting, Rebuilt as 150 Claude Skills", The Craft of AI,
<https://www.thecraftofai.com/read/150-consulting-skills-opus-5-5>, retrieved 2026-10-07. The 150 `SKILL.md` bodies are as published, with two changes:
each ends with a "Notes from the source article" section (what it replaces, an example request,
what the user still owns), and dollar amounts written as `$<digit>` were rewritten as `USD`
because the skill loader substitutes `$1`-style tokens as arguments.

| Practice | Lane | Skills |
|---|---|---|
| Problem Framing & Issue Trees | McKinsey | `001` to `010` |
| Market & Competitive Intelligence | McKinsey | `011` to `020` |
| Growth & Customer Strategy | McKinsey | `021` to `030` |
| Pricing & Commercial Excellence | McKinsey | `031` to `040` |
| Board & Executive Communication | McKinsey | `041` to `050` |
| Finance & FP&A Transformation | Deloitte | `051` to `060` |
| Cost & Margin Diagnostics | Deloitte | `061` to `070` |
| Risk, Controls & Compliance | Deloitte | `071` to `080` |
| M&A Diligence & Integration | Deloitte | `081` to `090` |
| Workforce & Org Design | Deloitte | `091` to `100` |
| Operations & Process Redesign | Accenture | `101` to `110` |
| Supply Chain & Procurement | Accenture | `111` to `120` |
| Technology & AI Transformation | Accenture | `121` to `130` |
| Customer Operations & Service | Accenture | `131` to `140` |
| Program Delivery & Value Realization | Accenture | `141` to `150` |

## Not in this repo

Anthropic-provided and example skills are versioned by Anthropic, not here:
`docx`, `xlsx`, `pptx`, `pdf`, `skill-creator`, `morning`, `import-memory`.

## Editing a skill

1. Edit `plugins/<group>/skills/<name>/SKILL.md` in this repo.
2. Commit. The git history is the version history.
3. Publish the change to the live skill (see below).

The frontmatter `description` is what decides when Claude invokes a skill, so
treat it as the most load-bearing line in the file.
