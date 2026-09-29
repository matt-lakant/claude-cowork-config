---
name: writing-voice
description: "Writes any text Matt will send or publish as himself (email, WhatsApp or LinkedIn message, letter, post, form answer, reply) in his voice, reading Notes/Writing voice.md in his Obsidian vault as the single source of truth. Use whenever Matt asks Claude to write, draft, answer or rewrite something in his name, including « écris-lui », « rédige un mail », « réponds à ce message », « fais-moi un post », or when he says « utilise ma Writing Voice ». Also called by job-search skills (cover-letter, cover-letter-redteam) to load the voice. When the vault cannot be reached, falls back to the voice rules in his preferences and says the full corpus was not read."
---

# Writing Voice

## What this skill is, and what it is not

It is the one entry point for writing in Matt's name. It **holds no voice rules**.

| Content | Lives in |
|---|---|
| The voice: corpus, banned constructions, review test, per-surface rules | Obsidian vault, `Notes/Writing voice.md`. **Single source of truth.** |
| A short summary of the key rules, for surfaces without the vault (claude.ai) | Matt's preferences, Settings > Profile, block headed `Writing voice` |
| How to load, apply, check and feed the voice | This file |

Never copy a rule, a corpus sentence or a banned-construction row into this file or anywhere
else in `claude-cowork-config`. `config-sync` forbids it: a second copy drifts within days.
The preference block is the only sanctioned summary, and this skill checks it against the
note every time the vault is readable.

## When a more specific skill applies

If a job-search skill owns the deliverable (`cover-letter`, `recruiter-followup`,
`interview-prep`, `offer-negotiator`, `resume-tailor`), that skill runs and this one loads the
voice for it. Otherwise this skill does the whole job: personal emails and messages, WhatsApp,
administrative letters, syndic and copropriété correspondence, LinkedIn posts, anything signed
by Matt.

## Mode: vault or fallback

| Mode | When | Rules come from |
|---|---|---|
| **Vault** | The note can be read | `Notes/Writing voice.md`, read in full |
| **Fallback** | No linked computer (claude.ai chat), folder access declined, or the device is offline | The `Writing voice` block in the preferences Claude receives (`<user_preferences>`) |
| **Vault required** | A calling skill says so (`cover-letter`, `cover-letter-redteam`) | The note only. **No fallback**: if it cannot be read, stop and say why |

## Step 1: Reach the vault

1. If the remote-device tools are present, run `ls $HOME/mnt/`. If `obsidian-vault` is not
   there, call `device_request_folder_access` on `C:\Users\mattc\Obsidian\obsidian-vault`
   straight away, without asking in chat first.
2. Read `$HOME/mnt/obsidian-vault/Notes/Writing voice.md` **in full** with `cat`. Not a grep,
   not a section: the corpus in §2 is what gets imitated, and the rules in §3 and §4 only work
   next to it.
3. If there are no remote-device tools, or the request is declined or unanswered, or the
   device is unreachable: fallback mode (unless the caller requires the vault).

## Step 2: Check the preference block against the note (vault mode only)

Matt's preferences carry a short `Writing voice` block so that claude.ai applies the key rules
without the vault. Every time the note is read, compare the two:

- **Rule in the block that the note no longer states, or states differently.**
- **Rule the note added after the block's date** (the block carries a date in its heading;
  rows in the note carry theirs in italics) that belongs among the key rules: a new row in the
  §3 table, a new category in list 4.1, a change to §1.
- **No `Writing voice` block** in the preferences at all.

If any of these holds, tell Matt in two or three lines, naming the rule, and offer the
replacement block (Step 6). If they match, say nothing. Never edit his preferences yourself:
he pastes the block.

## Step 3: Pick the surface

The voice (§1 to §4 of the note) applies everywhere. §5 sets the structure per surface:

| Text | Note section |
|---|---|
| Cover letter | §5.4 (and §5.1) |
| Form answer, LinkedIn message, recruiter email, written interview answer | §5.1 |
| CV lines | §5.2 |
| Analytical LinkedIn post | §5.3 |
| Anything else (personal email, WhatsApp, administrative letter, syndic mail) | §1 to §4 only |

For the last row the note has no surface rule and no corpus sample of Matt's personal
register. Keep the register of the conversation he is answering (a WhatsApp to a friend is
not a formal letter), write no greeting or sign-off he did not ask for, and apply §1 to §4
without exception. Say once, briefly, that no personal-register sample exists yet.

**Language:** the language the recipient will read. Matt writes to French recipients in French
and to English ones in English (US spelling). If unclear, the language of the message he is
answering.

## Step 4: Draft, then run the review test

1. Draft from the facts Matt gave. Never invent a fact, a motivation, a date or a figure.
   If a sentence needs one, ask.
2. Run the §4 review test of the note: points 1 to 7 on every text; point 8 (list 4.1) on
   §5.1, §5.2 and §5.4 surfaces, with §5.3's exemption; point 9 (swap test) on anything
   addressed to an employer or a recruiter.
3. In fallback mode, run the rules of the preference block instead, then say in one line,
   under the draft: `Rédigé avec les règles de voix de tes préférences ; le corpus complet
   (Notes/Writing voice.md) n'a pas été consulté.` (or the English equivalent when the
   conversation is in English).

## Step 5: Deliver

- A message or email: the text in a copyable block in chat, nothing around it but the
  fallback line if it applies.
- A file (letter, document): per Matt's standing rule, into
  `C:\Users\mattc\OneDrive\Documents\Claude\Projects\<Project Name>\`, flat, and surfaced as a
  file card.
- Never send, post or schedule anything on his behalf unless he asks in that turn. A draft in
  Gmail or Outlook only when he asks for a draft there.

## Step 6: The preference block (on request, or when Step 2 finds drift)

Build it from the note as read in this session, never from an earlier copy of the block:

- Heading `Writing voice (from Notes/Writing voice.md, <YYYY-MM-DD>)`, so Step 2 can date it.
- One line pointing to the note as the full reference.
- About ten bullets, one rule each, taken from §1, the §3 table and list 4.1: the rules Matt
  has corrected most often, stated as instructions. No corpus sentences, no reference letters,
  no per-surface detail.
- Short enough to paste into Settings > Profile alongside his other preferences.

Hand it to Matt in a copyable block. It is not written into this repo or into memory.

## Step 7: Feed the corpus

Per §6 of the note: whenever Matt rewrites a sentence Claude drafted in his name, add his
version verbatim to §2 in the same turn, with the date and the surface in italics, and
Claude's version underneath if the correction teaches something. Insert above the line that
starts `**Ce qu'on observe dans ces phrases`. A form that recurs becomes a row in the §3 table.
Show Matt the lines added.

- Do this with a short python read-modify-write on the note, never by re-typing the file.
  Never run `git` in the vault.
- When `asset-updater` is already filing the same edit (returned-file mode), let it; do not
  file twice.
- In fallback mode the note cannot be written: list his rewrite in chat and say it has not
  been filed, so it can be added next time the vault is reachable.

## Hard rules

- **The note is the only source.** No voice rule in this skill, in the repo, or in memory.
- **Read the note in full** in vault mode, every run.
- **Fallback is announced.** A draft written from the preference block always carries the line
  saying the full corpus was not read.
- **No fallback when the caller requires the vault.**
- **Flag drift, never fix it silently.** Matt pastes the preference block himself.
- **Never invent** facts, motivations or figures in his name.
- **Never an em dash**, in any language.
