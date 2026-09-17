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

### `job-search` (10 skills)

The pipeline, roughly in the order it runs:

| Skill | Role in the pipeline |
|---|---|
| `opportunity-intake` | Front door: confirms the opportunity, creates `applications/<slug>/` and its `notes.md`, routes to the right skill |
| `job-fit-analyzer` | Triage a posting before investing: fit score, gap analysis, go/no-go |
| `company-overview` | Research the company into `company_overview.md` (prerequisite for several skills) |
| `resume-tailor` | Tailor the master resume to the posting; ATS keywords, requirement mining |
| `resume-redteam` | Mandatory adversarial gate: a hostile recruiter tries to reject the resume |
| `interview-prep` | Predicted questions + STAR answers grounded in real experience |
| `recruiter-followup` | Follow-ups, thank-yous, ghosted-process nudges |
| `offer-negotiator` | Counter-offer emails, verbal scripts, scenario plans |
| `application-tracker` | Maintains `applications_tracker.md` and follow-up due dates |
| `asset-updater` | Closes the loop: propagates Matt's edits back into the master assets |

### `general` (2 skills)

| Skill | Purpose |
|---|---|
| `config-sync` | Mirrors a saved skill into this repo and commits it, so Matt only runs `git push` |
| `tackle-task` | Kickoff for work no dedicated skill covers: frames task + success criteria, gathers context before starting |

### `venture-lab` (2 skills)

Both write into the Obsidian vault and both default to "no business here".

| Skill | Purpose |
|---|---|
| `paper-digest` | Reads a paper or article Matt shares, explains the mechanism, judges it against a 7-gate rubric, files a `type: source` note with the PDF |
| `idea-pressure-test` | Pressure-tests an idea Matt already has: 11 gates, three adversaries (investor, incumbent PM, target buyer), six verdicts, a pre-registered kill test, filed as a `type: idea` note with dated re-tests |

## Not in this repo

Anthropic-provided and example skills are versioned by Anthropic, not here:
`docx`, `xlsx`, `pptx`, `pdf`, `skill-creator`, `morning`, `import-memory`.

## Editing a skill

1. Edit `plugins/<group>/skills/<name>/SKILL.md` in this repo.
2. Commit. The git history is the version history.
3. Publish the change to the live skill (see below).

The frontmatter `description` is what decides when Claude invokes a skill, so
treat it as the most load-bearing line in the file.
