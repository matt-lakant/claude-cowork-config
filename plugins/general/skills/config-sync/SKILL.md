---
name: config-sync
description: "Mirrors a saved or updated Claude skill into Matt's claude-cowork-config repo working tree and hands him a ready-to-paste commit message, so he commits and pushes himself in GitHub Desktop. Use immediately after Matt saves or updates any skill, and when he says \"sync my config\", \"mirror the skill\", or asks whether the repo is up to date."
---

# Config Sync

Keeps `matt-lakant/claude-cowork-config` in step with Matt's live Claude skills.

**Why this skill exists:** Cowork does not run user hooks, and saving a skill
happens in Matt's claude.ai account rather than inside a session's tool loop, so
nothing fires automatically. This skill is the trigger.

## The arrangement (changed 2026-09-09)

| Who | Does what |
|---|---|
| Claude | Drafts the skill, proposes it, and after Matt saves it, **writes the file into the local clone and verifies the bytes landed**. Then hands him a commit message. |
| Matt | Saves the proposal, then **commits and pushes in GitHub Desktop** |

**Claude does not run `git` in this repo any more.** No `git add`, no
`git commit`, no branch or history operation, unless Matt asks for one
explicitly in the moment. Leave the working tree dirty on purpose: the pending
changes are what Matt sees in GitHub Desktop, and they are the handover.

This also removes two frictions that existed only because Claude committed: the
session no longer needs delete permission on `repos` (that was for
`.git/index.lock`), and there is no risk of leaving a stale lock that blocks
Matt's own client.

Matt cannot author `SKILL.md` by hand, so the repo is an accurate **mirror** of
his live skills, not their source of truth. Never tell him to edit a file in the
repo and expect it to reach his skills; it will not.

## Paths

| What | Where |
|---|---|
| Local clone (his machine) | `C:\Users\mattc\repos\claude-cowork-config` |
| Same path in `device_bash` | `$HOME/mnt/repos/claude-cowork-config` |
| Live skills (read-only cache, this container) | `~/.claude/skills/synced/<uuid>/<skill-name>/SKILL.md` |
| Remote | `https://github.com/matt-lakant/claude-cowork-config` (private) |

The synced cache is **read-only and rebuilt each session**. It is the best
available copy of what Matt actually saved, so it is what you mirror from.
Editing it changes nothing.

## Repo layout

Skills are grouped as plugins, never as nested category folders — discovery is
flat at `skills/<skill-name>/SKILL.md`, so a category directory would hide them.

```
.claude-plugin/marketplace.json
plugins/job-search/{.claude-plugin/plugin.json, skills/<name>/SKILL.md}
plugins/general/{.claude-plugin/plugin.json, skills/<name>/SKILL.md}
Personal Data/_assets/          candidate_profile.md, voice_matt.md, master_resume*.docx
```

Placement rule: anything in the job application pipeline goes in `job-search`;
domain-agnostic skills go in `general`. If a new skill fits neither, ask Matt
rather than inventing a third plugin.

**Never mirror** Anthropic-provided or example skills (`docx`, `xlsx`, `pptx`,
`pdf`, `skill-creator`, `morning`, `import-memory`). Check `source` in the
synced `manifest.json`: only `custom` and `plugin` entries are Matt's.

## Workflow

### Step 1 — Confirm the folder is reachable

If `C:\Users\mattc\repos` is not connected, call
`device_request_folder_access` on it. If that fails because the session has no
linked computer, say so plainly and hand Matt the file instead of pretending the
mirror happened.

### Step 2 — Mirror the files

Copy `SKILL.md` (and any `references/`, `scripts/`, `assets/` the skill carries)
from the synced cache to `plugins/<group>/skills/<skill-name>/`. Overwrite in
place. Drop `LICENSE.txt` from Anthropic-derived scaffolding.

The reliable route is to stage the file under `/mnt/user-data/outputs/` in the
container, then `device_commit_files` with `stagedPath` → `devicePath`. Writing
large markdown through a `device_bash` heredoc invites escaping bugs.

For a **new** skill, also bump the `version` in that plugin's
`.claude-plugin/plugin.json` and add the skill to the table in `README.md`.

### Step 3 — Verify the bytes actually landed (mandatory)

**`device_commit_files` can report `written` without the content arriving.**
Observed 2026-09-09: two `SKILL.md` files came back in `written` with no
rejection, and the files on disk still held the previous version. The identical
call a moment later worked.

So never trust the tool's own report, and never conclude anything from
`git status` alone — on this mount its stat cache misleads in both directions.
Compare content:

```bash
cd "$HOME/mnt/repos/claude-cowork-config"
md5sum plugins/<group>/skills/<name>/SKILL.md      # then compare with the source
grep -c "<a distinctive string from the new version>" plugins/<group>/skills/<name>/SKILL.md
```

If the hashes differ, write again and re-check. Do not hand Matt a commit
message for a change that is not on his disk: GitHub Desktop would simply show
nothing to commit, and he would push an empty change believing it landed.

### Step 4 — Hand Matt the commit message

He writes the commit, so give him something he can paste straight into GitHub
Desktop: a summary line, then a body explaining the change to the **skill**
rather than the file move. Append the co-author trailer.

```
<skill-name>: <what changed>

<why it changed, in a sentence or two — the reason is what future-Matt needs>

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Then tell him which files are waiting, and nothing more:

> `plugins/job-search/skills/resume-tailor/SKILL.md` is updated in the clone and
> waiting in GitHub Desktop. Suggested message below.

Do not say it is committed, and do not say it is on GitHub. Neither is true
until he does it.

## Reconciling the whole repo

When Matt asks whether the repo is current, or a skill was saved in a session
that never ran this skill, diff every one of his skills in the synced cache
against its counterpart in the repo. Report which skills differ, which are in
the repo but no longer in his account, and which are new. Mirror the drift and
suggest one message: `sync: reconcile <n> skills with live account`.

A skill present in the repo but gone from the account was probably deleted
deliberately — ask before removing it, since the git history is the only
remaining copy.

## Git identity, for reference only

The repo's **local** config is `Matt Cornet <matt.cornet@lakant.io>` (set
2026-09-09). Commits made before that date are authored `Claude
<noreply@anthropic.com>`, which is why the history is mixed and why GitHub
Desktop once warned about misattribution. This is settled — do not
"fix" it, and do not rewrite history to make it uniform unless Matt asks.

## Hard rules

- **Never run `git` in this repo.** No commit, no push, no rebase, no branch
  surgery. Matt owns the history and does it in GitHub Desktop. The one
  exception is a read-only inspection he asked for, or an operation he requests
  explicitly in the moment.
- **Never claim a commit happened.** You mirrored files; that is what you say.
- **Always verify the bytes** before handing over a commit message. See Step 3.
- **Mirror only what Matt saved.** Do not mirror a skill you merely proposed. If
  you are unsure whether he saved it, check the synced cache for the change, and
  ask if it is not there.
- **Never write into `Personal Data/` casually.** Those files are refreshed
  from `C:\Users\mattc\OneDrive\Documents\Claude\Projects\Job Applications\_assets`
  only when Matt asks, or when `asset-updater` has changed the master. Never
  copy repo → OneDrive; that direction clobbers in-flight work.
- **`applications_tracker.md` and `applications/` are not versioned.** Matt's
  decision. Do not add them.
- **The repo is private and holds his full career history.** Do not suggest
  making it public, adding collaborators, or mirroring it elsewhere.