---
name: config-sync
description: "Mirrors a saved or updated Claude skill into Matt's claude-cowork-config git repo and commits it, so he only has to run git push. Use immediately after Matt saves or updates any skill, and when he says \"sync my config\", \"push the skill\", or asks whether the repo is up to date."
---

# Config Sync

Keeps `matt-lakant/claude-cowork-config` in step with Matt's live Claude skills.

**Why this skill exists:** Cowork does not run user hooks, and saving a skill
happens in Matt's claude.ai account rather than inside a session's tool loop, so
nothing fires automatically. This skill is the trigger.

## The arrangement

| Who | Does what |
|---|---|
| Claude | Drafts the skill, proposes it, and after Matt saves it, writes the file into the local clone and commits |
| Matt | Saves the proposal, then runs `git push` |

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
Personal Data/_assets/          candidate_profile.md, master_resume*.docx
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
commit happened.

### Step 2 — Make git usable in the mount (do this before any git write)

`device_bash` cannot delete files by default, and git cannot commit without
creating and removing `.git/index.lock`. A stale lock blocks every later git
command, including Matt's own from PowerShell. So:

1. Call `device_request_delete_permission` on `C:\Users\mattc\repos`. This is
   session-scoped, so it is needed once per session, not once ever.
2. Then run:

```bash
cd "$HOME/mnt/repos/claude-cowork-config"
rm -f .git/index.lock
git config core.checkstat minimal
git config core.trustctime false
git config core.fileMode false
git update-index --refresh >/dev/null 2>&1
```

Without the `core.checkstat` / `trustctime` settings the mount reports fresh
stat data on every call and **every file shows as modified when nothing
changed**. Confirm with `git diff --quiet` (silent means the tree is clean)
before concluding anything from `git status`.

### Step 3 — Mirror the skill

Copy `SKILL.md` (and any `references/`, `scripts/`, `assets/` the skill carries)
from the synced cache to
`plugins/<group>/skills/<skill-name>/`. Overwrite in place. Drop `LICENSE.txt`
from Anthropic-derived scaffolding.

For a **new** skill, also bump the `version` in that plugin's
`.claude-plugin/plugin.json` and add the skill to the table in `README.md`.

### Step 4 — Commit

One commit per save, describing the change to the skill rather than the file
move:

```bash
git add -A
git commit -m "<skill-name>: <what changed and why>"
```

If the commit is rejected for a missing signing key, retry once with
`git -c commit.gpgsign=false commit`.

### Step 5 — Tell Matt exactly one thing

Name the commit and give him the command. Nothing more:

> Committed `a1b2c3d` (`resume-tailor: <change>`). Run `git push` in
> `C:\Users\mattc\repos\claude-cowork-config`.

Do not claim it is on GitHub. It is not until he pushes.

## Reconciling the whole repo

When Matt asks whether the repo is current, or a skill was saved in a session
that never ran this skill, diff every one of his skills in the synced cache
against its counterpart in the repo. Report which skills differ, which are in
the repo but no longer in his account, and which are new. Commit the drift as
one commit: `sync: reconcile <n> skills with live account`.

A skill present in the repo but gone from the account was probably deleted
deliberately — ask before removing it, since the git history is the only
remaining copy.

## Hard rules

- **Never `git push`.** The session's git proxy refuses this repo (it is not in
  the session's authorized source set). Matt pushes; you commit.
- **Mirror only what Matt saved.** Do not commit a skill you merely proposed. If
  you are unsure whether he saved it, check the synced cache for the change, and
  ask if it is not there.
- **Never commit into `Personal Data/` casually.** Those files are refreshed
  from `C:\Users\mattc\OneDrive\Documents\Claude\Projects\Job Applications\_assets`
  only when Matt asks, or when `asset-updater` has changed the master. Never
  copy repo → OneDrive; that direction clobbers in-flight work.
- **`applications_tracker.md` and `applications/` are not versioned.** Matt's
  decision. Do not add them.
- **The repo is private and holds his full career history.** Do not suggest
  making it public, adding collaborators, or mirroring it elsewhere.