---
name: config-sync
description: "Governs how Claude edits Matt's claude-cowork-config repo: where a skill file goes, how to verify it actually landed, and the commit message handed to Matt so he commits and pushes himself in GitHub Desktop. Use whenever a skill is created or changed, when Matt says \"sync my config\", \"mirror the skill\", or asks whether the repo is up to date."
---

# Config Sync

Governs Claude's access to `matt-lakant/claude-cowork-config`, the repo that
serves Matt's skills.

## The repo is the source of truth (changed 2026-09-10)

Until 2026-09-10 this skill mirrored: Matt saved a skill in his claude.ai
account, and Claude copied it from the read-only synced cache into the repo. That
flow is gone. The account-skill copies were deleted, the plugins are the only
source, and the direction reversed.

**Editing `plugins/<plugin>/skills/<name>/SKILL.md` in the working tree is now
how a skill changes.** Do not propose a skill for Matt to save; he cannot author
`SKILL.md` by hand and there is no account copy left to save into.

How the edit reaches a session:

1. Claude edits the file in the clone at `C:\Users\mattc\repos\claude-cowork-config`.
2. Matt commits and pushes in GitHub Desktop.
3. The personal marketplace syncs to the new commit on `main` (`Sync automatically`
   is ON since 2026-09-10).
4. The client resolves a new plugin version and re-downloads.
5. The **next** session loads it. The current one does not.

| Who | Does what |
|---|---|
| Claude | Edits the working tree, verifies the bytes landed, hands over a commit message |
| Matt | Commits and pushes in GitHub Desktop |

Leave the working tree dirty on purpose. The pending changes are what Matt sees
in GitHub Desktop, and they are the handover.

## Paths

| What | Where |
|---|---|
| Local clone (his machine) | `C:\Users\mattc\repos\claude-cowork-config` |
| Remote | `https://github.com/matt-lakant/claude-cowork-config` (private) |

In `device_bash` the clone sits under `$HOME/mnt/<connected-folder-name>`, and the
folder name is whichever one Matt connected: `claude-cowork-config` if he connected
the repo itself, `repos/claude-cowork-config` if he connected the parent. **Run
`ls $HOME/mnt/` first and use what is actually there** rather than assuming either
shape.

A synced cache may exist at `~/.claude/skills/synced/<uuid>/` in the container. It
is a delivery artifact of the current session, not a source. Reading it can confirm
what this session loaded; it is never what an edit is copied from.

## Repo layout

Skills are grouped as plugins, never as nested category folders. Discovery is flat
at `skills/<skill-name>/SKILL.md`, so a category directory would hide them.

```
.claude-plugin/marketplace.json
plugins/job-search/{.claude-plugin/plugin.json, skills/<name>/SKILL.md}
plugins/general/{.claude-plugin/plugin.json, skills/<name>/SKILL.md}
plugins/venture-lab/{.claude-plugin/plugin.json, skills/<name>/SKILL.md}
```

Placement rule: anything in the job application pipeline goes in `job-search`;
idea generation and evaluation go in `venture-lab`; domain-agnostic skills go in
`general`. If a new skill fits none of them, ask Matt rather than inventing a
fourth plugin.

**This repo holds configuration only.** Personal data was removed on 2026-09-10
and `/Personal Data/` is in `.gitignore`.

**Nothing else belongs at the repo root.** The complete list is `plugins/`,
`.claude-plugin/`, `README.md` and `.gitignore`. Any other folder or file
appearing there is a mistake, not a new convention.

**Never add** Anthropic-provided or example skills (`docx`, `xlsx`, `pptx`, `pdf`,
`skill-creator`, `morning`, `import-memory`). They are versioned by Anthropic.

## Where personal data lives

The repo used to carry a `Personal Data/` mirror of the Job Applications assets.
It went stale within two days and nothing ever read it. It is gone, and it does
not come back.

| Content | Single source of truth |
|---|---|
| Who Matt is: bio, background, education, scope and technology ceilings, target roles | Obsidian vault, `Notes/Matt Cornet.md` |
| How Matt writes: corpus, banned constructions, review test, per-surface rules | Obsidian vault, `Notes/Writing voice.md` |
| Job-search working files: tailoring Q&A log, master resumes, tracker, applications | OneDrive, `Projects/Job Applications/` |

The vault is its own private git repo (`obsidian-vault`), so identity data is
still versioned, just not here.

## Workflow

### Step 1 - Confirm the folder is reachable

Run `ls $HOME/mnt/` to see what is connected. If the clone is not there, call
`device_request_folder_access` on `C:\Users\mattc\repos\claude-cowork-config`. If
that fails because the session has no linked computer, say so plainly and hand
Matt the file content instead of pretending the edit happened.

### Step 2 - Edit the files

Write to `plugins/<plugin>/skills/<skill-name>/SKILL.md`. For a sizeable file the
reliable route is to write it in the container and `device_commit_files` with
`stagedPath` to `devicePath`; a `device_bash` heredoc works but invites escaping
bugs on large markdown. For a surgical change, edit in place with `sed -i` or a
short python read-modify-write rather than re-typing the file from tool output,
which may have been truncated.

For a **new** skill, add a row to the table in `README.md` and update that
plugin's skill count in its heading.

**Do not add a `version` field to `plugin.json`.** It was deliberately removed in
`3a8ed14`. Version resolution falls through to the commit SHA, which changes on
every commit and cannot be forgotten; a pinned string takes precedence over the
SHA and reintroduces the stale-plugin bug that cost the 2026-09-10 afternoon. If a
human-readable release marker is ever wanted, use a git tag, which does not
participate in version resolution. `marketplace.json`'s `metadata.version` is
marketplace-level metadata and does not gate plugin updates; leave it.

### Step 3 - Verify the bytes actually landed (mandatory)

**`device_commit_files` can report `written` without the content arriving.**
Observed 2026-09-09 and again 2026-09-10: files came back in `written` with an
empty `rejected` list, and the file on disk still held the previous content. The
identical call a moment later worked.

Never trust the tool's own report. Compare content:

```bash
cd "$HOME/mnt/<connected-folder>"
md5sum plugins/<plugin>/skills/<name>/SKILL.md     # compare with the source
grep -c "<a distinctive string from the new version>" plugins/<plugin>/skills/<name>/SKILL.md
```

If they differ, write again and re-check. Do not hand Matt a commit message for a
change that is not on his disk: GitHub Desktop would show nothing to commit, and
he would push an empty change believing it landed.

Verify with `md5sum` and `grep`, never with `git status`. See the hard rule below.

### Step 4 - Hand Matt the commit message

He writes the commit, so give him something he can paste straight into GitHub
Desktop: a summary line, then a body explaining the change to the **skill** rather
than the file operation. Append the co-author trailer.

```
<skill-name>: <what changed>

<why it changed, in a sentence or two; the reason is what future-Matt needs>

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Then tell him which files are waiting, and nothing more:

> `plugins/job-search/skills/resume-tailor/SKILL.md` is updated in the clone and
> waiting in GitHub Desktop. Suggested message below.

Do not say it is committed, and do not say it is on GitHub. Neither is true until
he does it.

If the change spans several unrelated things (a skill plus a README catch-up from
an earlier session), say so and name the files, so he can stage selectively rather
than discovering the mix in the diff.

## Is the repo current?

When Matt asks whether the repo or the runtime is up to date, **read files under
`.git/`**. This takes no lock and answers what git would:

| File | Tells you |
|---|---|
| `.git/refs/heads/main` | the local commit |
| `.git/refs/remotes/origin/main` | the last pushed commit; equal to the above means pushed |
| `.git/logs/HEAD` | the reflog: history with SHAs, authors and epoch timestamps |

Then compare `refs/heads/main` against **Settings > Directory > Plugins > Personal
> `claude-cowork-config` > `...` > `Synced commit`**. Equal means the runtime is
serving the current code. Different means the sync has not run; `Check for updates`
in that same menu forces it. The `Update` button on the plugin card is downstream
and stays greyed while the marketplace has nothing newer, so it is not the control
to press.

A skill that exists in the repo is served. There is no separate account copy to
reconcile against any more.

## The `Claude outputs/` folder

Observed twice on 2026-09-10: a `Claude outputs/` directory at the repo root
holding copies of files Claude had just delivered in chat.

**Claude did not write it. The desktop app did.** Every `SendUserFile` delivery is
mirrored by the app into `Claude outputs/` inside a connected folder. The second
occurrence came back within three minutes of the folder being deleted, holding the
two files from that same turn, timestamped to the second of the `SendUserFile` call.

Which connected folder the app picks is **not established**. Both
`claude-cowork-config` and `Documents\Claude\Projects` were connected and it chose
the repo. Do not assume that connecting the project folder is enough to steer it
elsewhere.

What follows:

- **Do not send a `SKILL.md` from this repo as a chat card.** It is already on
  Matt's disk under `plugins/`; the card buys a duplicate in a folder that should
  not exist. Give him the path. This is the one place where his standing preference
  for a file card on every deliverable does not apply, because the file already
  landed where he wanted it.
- `/Claude outputs/` is in `.gitignore`. That is the durable guard: a recurrence
  stays untracked and never reaches a commit. Deleting the folder is cosmetic.
- If it reappears and Matt wants it gone, delete it **at the very end of the turn**,
  after the last `SendUserFile`, or it returns before the turn is over.

## Git identity, for reference only

The repo's **local** config is `Matt Cornet <matt.cornet@lakant.io>` (set
2026-09-09). Commits before that date are authored `Claude
<noreply@anthropic.com>`, which is why the history is mixed and why GitHub Desktop
once warned about misattribution. This is settled: do not "fix" it, and do not
rewrite history to make it uniform unless Matt asks.

Matt avoids pull requests here and commits straight to `main`.

## Hard rules

- **Never run `git` in this repo. This includes `git status` and `git diff`.**
  They refresh the index, which creates a 0-byte `.git/index.lock` that the mount
  cannot delete, and GitHub Desktop then refuses to commit with "A lock file
  already exists in the repository". Broken on 2026-09-10 and again on 2026-09-17,
  both times by a read-only inspection that felt harmless. There is no safe
  read-only git command here. Read `.git/refs/...` as files instead, and verify
  edits with `md5sum` and `grep`. If a lock is already there, it is 0 bytes and
  stale (a genuine lock carries a PID), and clearing it needs
  `device_request_delete_permission` on the repo folder.
- **Never claim a commit happened.** You edited files; that is what you say.
- **Always verify the bytes** before handing over a commit message. See Step 3.
- **Never write session outputs into this repo.** No report, no draft, no scratch
  copy of a file that already lives under `plugins/`. Session deliverables go to
  `C:\Users\mattc\OneDrive\Documents\Claude\Projects\<Project Name>\` and they go
  there **even when this repo is the only folder connected**. A mounted repo is not
  a reason to write into it.
- **Do not call `SendUserFile` on a file in this repo.** See "The `Claude outputs/`
  folder" above.
- **Never version personal data here.** No `Personal Data/`, no profile, no voice
  reference, no resume, no application material, whoever asks and however
  convenient a mirror would look. Those live in the vault and in OneDrive, and a
  second copy here is exactly the drift this repo just got rid of. If a skill or a
  session tries to write one, stop and say why.
- **`applications_tracker.md` and `applications/` are not versioned.** Matt's
  decision. Do not add them.
- **The repo is private.** Do not suggest making it public, adding collaborators,
  or mirroring it elsewhere.
