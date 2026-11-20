---
name: writing-voice-mntrl
description: Writes, reviews or rewrites any text Matt signs for the MNTRL association (emails and messages to the Ville de Montreuil, the Maison des associations, élus, youth workers, partners, suppliers). Loads the voice rules from the vault and the MNTRL corpus, and files every rewrite Matt makes into Notes/Writing voice MNTRL.md. Use it in the MNTRL project instead of writing-voice.
---

# Writing Voice MNTRL

## What this skill is, and what it is not

The entry point for any text Matt signs **for the MNTRL association**: emails and messages to
the Ville de Montreuil (Maison des associations, élus, services), youth workers, partners,
suppliers, funders. It **holds no voice rules and no corpus sentences**.

| Content | Lives in |
|---|---|
| The voice rules that apply everywhere: diagnostic, banned constructions, review test | Obsidian vault, `Notes/Writing voice.md`, §1, §3, §4 with 4.1 |
| The MNTRL corpus: Matt's association emails, with Claude's version underneath | Obsidian vault, `Notes/Writing voice MNTRL.md`. **Single source for this register** |
| The facts about the association (RNA, SIRET, siège, bureau, contacts, démarches) | MNTRL project docs (`claude/MNTRL_Identite_administrative.md`, `claude/MNTRL_Maison_des_associations_Montreuil.md`, `claude/MNTRL_Partenaires.md`, ...) |
| A short summary of the key rules, for surfaces without the vault | Matt's preferences, block headed `Writing voice` |

`Notes/Writing voice.md` is the job-search note: its corpus and its §5 surfaces (letters, CV,
forms, LinkedIn) are **not** read here, and **nothing MNTRL is ever filed there** (Matt's
decision, 2026-11-20). Never copy a rule or a corpus line into this file or anywhere else in
`claude-cowork-config`.

## When to use it, and when not

- Use it for anything signed by Matt as président of MNTRL, or about MNTRL, in any project.
- Job applications stay with `writing-voice` and the job-search skills.
- Other personal texts (syndic, copropriété, friends) stay with `writing-voice`.

## Step 1: Reach the vault

1. If the remote-device tools are present, run `ls $HOME/mnt/`. If `obsidian-vault` is not
   there, call `device_request_folder_access` on `C:\Users\mattc\Obsidian\obsidian-vault`
   straight away, without asking in chat first.
2. Read `$HOME/mnt/obsidian-vault/Notes/Writing voice MNTRL.md` **in full** with `cat`. The
   corpus is what gets imitated: greeting, register, length, signature, how Matt asks.
3. From `$HOME/mnt/obsidian-vault/Notes/Writing voice.md`, read **only §1, §3, and §4 with
   4.1**, printed with `sed` between the section headings. The file is very long (120k+
   characters); `cat` on it overflows the tool output.
4. No remote-device tools, access declined or device offline: **fallback mode**. Apply the
   `Writing voice` block of the preferences Claude receives, and say so under the draft (Step 4).

## Step 2: Gather the facts

1. Read the MNTRL project docs that the text needs (`project_read` / `project_search`), and
   the email thread Matt is answering if he pasted or attached it. Never Glob the disk for
   project docs.
2. **Never invent** a fact, a date, a figure, a name or a title. If a sentence needs one, ask.
   Check spellings of people and titles against the latest thing Matt wrote, not an older note.
3. If a fact Matt states contradicts a doc or the thread (a deadline, an amount, a rule the
   other side gave), keep it out of the draft or phrase it neutrally, and flag it in one line.

## Step 3: Draft

- Language: French unless the recipient writes in another language.
- Register and structure: follow the corpus of `Writing voice MNTRL.md`. Where it is silent,
  apply §1, §3 and §4 of `Writing voice.md`, and keep the register of the message being answered.
- A reply in an existing thread: no re-introduction of the association the recipient already
  received; go to what is new.
- French typography: non-breaking space (U+00A0) before ; : ? ! and inside « ». No em dash.

## Step 4: Review, then deliver

1. Run the §4 review test of `Writing voice.md`: points 1 to 7, plus point 8 (list 4.1). Points
   9 and 10 are for job applications and do not apply.
2. Deliver an email or message as a copyable draft in chat (the message-compose card when
   available), with at most a few lines of flags under it.
3. In fallback mode, add under the draft: `Rédigé avec les règles de voix de tes préférences ;
   le corpus MNTRL (Notes/Writing voice MNTRL.md) n'a pas été consulté.`
4. Never send, post or schedule anything. A Gmail or Outlook draft only when Matt asks for one.

## Step 5: Feed the corpus (every time Matt rewrites)

When Matt pastes the version he sent, or rewrites a sentence Claude drafted:

1. Add his version **verbatim** to the `## Corpus` section of `Notes/Writing voice MNTRL.md`,
   in date order, in the same turn. Format, as in the existing entries:
   `- « his sentence » / « his next changed sentence » *(YYYY-MM-DD, surface and recipient)*`
   then an indented `  - Version de Claude : « ... »` line and one or two sentences on what the
   correction teaches.
2. Use a short python read-modify-write on the note, never re-type the file. Never run `git`
   in the vault.
3. When a form recurs (second occurrence in the MNTRL corpus), say so and propose a rule line
   for Matt to validate; do not add rule sections to the note on your own.
4. Show Matt the lines added. In fallback mode, list his rewrite in chat and say it has not
   been filed.

## Hard rules

- **MNTRL text is filed in `Notes/Writing voice MNTRL.md` only**, never in `Notes/Writing voice.md`.
- **No voice rule or corpus line in this skill, the repo or memory.**
- **Fallback is announced.**
- **Never invent** facts, dates, figures or titles in Matt's name.
- **Never an em dash**, in any language.
