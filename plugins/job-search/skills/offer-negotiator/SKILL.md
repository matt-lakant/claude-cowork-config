---
name: offer-negotiator
description: "Helps Matt Cornet negotiate a job offer — drafts counter-offer emails, verbal scripts, and scenario plans for handling pushback. Use whenever Matt mentions receiving an offer, asks to negotiate salary/comp, mentions \"they came back with X\", or asks for a counter-offer email. Also use when he's evaluating multiple offers and needs leverage framing."
---

# Offer Negotiator

## What this skill does

Drafts negotiation collateral grounded in three things: the offer as stated, Matt's BATNA as he
reports it this run, and the durable profile held in the vault note. Market data for the role,
level and geography is researched per run, never carried in this file.

The deliverable is a tailored email, a verbal script, and an "if they say X, you say Y" cheat
sheet.

**The email and the script are spoken and signed by Matt.** A counter-offer that does not sound
like him is worse than a plain one: the person reading it has already met him.

## Source materials (read these every run)

> Paths marked *(vault)* are relative to the connected `obsidian-vault` folder. Paths marked
> *(project)* are relative to the **Job Applications project root**, the folder that contains the
> application folders and `_assets/`. Resolve those against whichever folder Matt has connected
> for the current session (typically the one named "Job Applications").

1. *(vault)* `Notes/Matt Cornet.md` **read this first**. Every fact about who Matt is comes from
   here: `## Background`, `## Strengths`, `## Education`, `## Current focus`, `## Target roles`,
   `## Framing guardrails`, `## Technology and scope ceilings`. A leverage claim that breaches a
   ceiling is a claim he cannot defend on the call that follows.
2. *(vault)* `Notes/Writing voice.md` **read before drafting the email or the script**. §2 the
   corpus of his own sentences, §3 the banned-construction table, §4 the review test, §5.1 the
   candidature-prose surface this skill writes in.
3. *(project)* `_assets/candidate_profile.md` evidence at the engagement level: what he actually
   delivered where. Use it for detail, never for identity.
4. The offer details and his BATNA, as Matt states them this run. Comp figures live nowhere in
   this repo, in this file or in the vault. If a number is needed and Matt has not given it, ask.
5. Optional, researched per run: public market comp data. Cite the source and its date.

### The vault is a hard requirement

Run `ls $HOME/mnt/` and check for `obsidian-vault`. If it is not connected, ask Matt to connect
`C:\Users\mattc\Obsidian\obsidian-vault`, or call `device_request_folder_access` on it.
**Do not draft the email, the script or the playbook without it.** There is no fallback: this
skill carries no sectors, no seniority band, no capability list and no scarcity claim of its own,
so without the note it has nothing to build leverage from and no ceiling to stay inside.

`_assets/voice_matt.md` and the "Voice & style guidelines" section of `candidate_profile.md` are
stubs pointing to the vault. Never read them as rules, never write to them.

### No identity in this file

If a step below needs a fact about Matt, it names the vault section to read it from. Nothing
about his sectors, levels, geographies, languages, years, strengths, employers or compensation is
written into this skill. When the note changes, the negotiation posture changes with it and this
file stays untouched.

## Inputs to gather (ask if missing)

- Company, role, level, and the geography and work pattern the offer specifies
- Full offer breakdown: base, target bonus %, equity (RSUs or options, vesting, refresh), signing,
  relocation, benefits delta against his current situation
- BATNA: other offers or live processes, and his current income position as he describes it
- His target number and his floor
- Tone he wants: collaborative, firm, or walk-away-ready
- Whether the offer was verbal or written, and the deadline

If Matt gives only the headline number, push for the full package. Equity and bonus can swing
total comp materially at the levels listed in `## Target roles`.

## Workflow

### Step 0 — Company overview (prerequisite)

This skill relies on the application's `company_overview.md`. **If
`applications/<company>-<role-slug>/company_overview.md` does not exist, run the
`company-overview` skill first** to research the company and create it. If it already exists,
read and reuse it, refreshing it via `company-overview` if it is clearly stale. Use the company's
stage, funding, ownership and business model to calibrate leverage, comp expectations and equity
framing.

### Step 1 — Sanity-check the offer

Quick analysis in chat:

- **Is the level appropriate?** Compare the offered level and scope against the most recent rows
  of `## Background` in the vault note, and against `## Target roles`. Name the row you compared
  to. Do not assert a past title or scope from memory of an earlier run.
- **Is the base in market range** for the role, level and geography? Use public comp data and
  cite sources with dates.
- **What is the all-in TC** (base + bonus + equity/4)?
- **What looks soft and likely negotiable?** Usually base, signing, equity, start date. Rarely
  title, level, bonus structure.

### Step 2 — Identify leverage

Match Matt's leverage to the gap he is asking to close. Every leverage line must trace to a
source, and the source is named in the strategy summary:

| Leverage type | Where it comes from | Guardrail |
|---|---|---|
| **Other offers or live processes** | Matt, this run | Name them generically ("a competing offer at a similar-stage firm"). Never invent one. |
| **Scarcity of his combination** | `## Strengths` crossed with `## Background` | A strength listed in the note with a matching row in the Background table is defensible. One with neither is not a leverage point. |
| **Availability** | `## Current focus` | State it as the note states it. Do not embellish the timeline. |
| **Income position as anchor** | Matt, this run | Use only figures he has given you in this session. |

**Check `## Technology and scope ceilings` and `## Framing guardrails` before writing any
leverage line.** A ceiling item cannot be leverage, however well it would serve the ask. A
negotiation claim is the one place where an overreach gets tested immediately: they will ask him
about it on the call, and the offer is still revocable.

If the note supports no strong leverage for the gap Matt wants to close, say so plainly and
recommend a smaller ask, rather than manufacturing a claim.

### Step 3 — Draft the counter

**Email format (default):**

- 4 to 6 short paragraphs
- Open: enthusiasm and reaffirmation of mutual fit, one paragraph
- Middle: specific asks with rationale grounded in market data and the Step 2 leverage table.
  Two to three paragraphs, two to three asks maximum. Bundling is fine, scattershot is bad.
- Close: collaborative framing, propose a specific next step (call, or written response by a date)

**Write it in Matt's voice, per *(vault)* `Notes/Writing voice.md`.** Plain declaratives, no
metaphor, no image, no defining himself against an implied lesser candidate, no sentence
announcing what the next one will do. In a negotiation this matters twice over: rhetorical
flourish reads as pressure, and pressure invites resistance. The number and the reason carry the
ask.

Save: `applications/<company>-<role-slug>/negotiation/counter_email_<date>.md`

**Verbal script:** for the follow-up call, a 60-second opening plus bullet talking points.
Written to be spoken aloud, so short sentences and ordinary verbs matter more here than anywhere
else. Save: `applications/<company>-<role-slug>/negotiation/verbal_script.md`

**Pushback playbook:** "if they say X, you say Y" for the 6 most likely responses. For example
"we don't move on base" pivots to signing or equity; "this is our best offer" gets silence and a
restatement of the top priority; "we need an answer today" buys 24 to 48 hours with a specific
reason.

### Step 4 — Decision framework

If Matt has multiple offers, or is weighing this against staying independent, give him a
comparison table:

- All-in TC year 1 and year 4
- Cash versus equity mix
- Career optionality, read against `## Target roles`: does the role open or close the moves that
  note prioritises?
- Risk profile (early-stage versus established)
- Lifestyle: geography, travel, hours, against what `## Current focus` says he is optimising for

Lay out the numbers and the trade-offs. The decision is his.

### Step 5 — Review against the voice test, then deliver

Run the §4 review test in *(vault)* `Notes/Writing voice.md` over the email and the script before
showing them: strike every image, every self-definition by negation, every announcement sentence,
every verb of certainty that should be an observation.

Then run the ceiling pass: re-read every claim in the email and the script against
`## Technology and scope ceilings` and `## Framing guardrails`. Anything that breaches one comes
out before Matt sees it.

If Matt rewrites any part, **add his version verbatim to §2 of *(vault)* `Notes/Writing voice.md`**
in the same turn. If the vault is not connected, hand him the sentence and say it still needs
filing rather than writing it into `_assets/`.

## Output: present to Matt

Deliver the email, verbal script and playbook with `SendUserFile` so he can open and copy them,
plus a summary in chat of the strategy, at most 5 lines, naming the vault sections each leverage
line came from. Keep the copies in the application folder. Never produce a PDF.

## Hand-off to `application-tracker`

An offer is a status change, and the tracker is the record of record. **After
delivering the email and the script, run `application-tracker` in the same turn**
rather than leaving Matt to log it himself.

What to pass:

- **Status** `offer` once the written terms are in hand and no counter has gone out
  yet; `negotiating` once it has. A verbal-only offer does not become `offer`: leave
  the status where it is and record the verbal offer in the Notes, consistent with
  the edge case below that says to get it in writing first.
- **Last touch** the date the offer arrived, as Matt states it. Never compute a date
  he has not given.
- **Next action** and **Next action due** the tracker's own default for `offer` is
  +3 days for a decision or counter. If the company set a deadline, that deadline
  wins and becomes the due date; say in the Notes that it came from them, so a later
  reader can tell an imposed deadline from a computed one.
- **Comp band** only if the posting or the offer disclosed it. Do not put Matt's own
  figures into the tracker uninvited: the numbers in this run belong to the
  conversation, not to a file that outlives it.
- **Notes** one date-stamped line, append-only: what was offered at a headline level,
  what was asked for, and the deadline.

If the application has no row yet, add it retroactively rather than skipping the log,
and ask Matt for the dates instead of guessing them.

## Hard rules

- **Always log the outcome.** Hand off to `application-tracker` after delivering, per
  the section above. An offer that never reaches the tracker is invisible to the
  weekly review.
- **Never lie.** Do not suggest claiming a competing offer that does not exist, or inflating
  prior comp. Reputational risk in the sectors listed in `## Background` outweighs any
  negotiation gain.
- **Never use a ceiling item as leverage**, and never soften a ceiling because the ask is
  attractive. See `## Technology and scope ceilings`.
- **Re-read `Notes/Matt Cornet.md` every run.** Do not build leverage from memory of a previous
  run.
- **Report vault silence as silence.** If the note says nothing about a sector, a level, a
  language or an availability the negotiation would use, say so and offer to add it, rather than
  inferring it from the resume or from the conversation.
- **No figures of speech**, in the email or the script. See `Notes/Writing voice.md` §3.
- **Never read voice rules or identity from `_assets/voice_matt.md` or from
  `candidate_profile.md`.** Both are stubs as of 2026-09-10.
- **Never anchor below market.** If Matt's floor is below market median, push back on the floor
  before drafting.
- **Do not write inflammatory language.** Even firm asks should preserve the relationship. He
  may work with these people for a decade.
- **Surface deadline pressure.** If they are rushing, name it in the strategy and recommend a
  counter that buys time.
- **Consider the level question first.** Sometimes the right negotiation is on title and scope,
  not comp. A bigger role at the same money compounds for years.
- **Never give personalized financial advice.** Lay out the numbers and the trade-offs; the
  decision is his.

## Edge cases

- **The vault is not connected:** stop and ask Matt to connect it. Do not draft, and do not fall
  back to the stubs.
- **Verbal offer only:** get it in writing before negotiating. Draft the "thank you, please send
  written terms" email instead.
- **Lowball offer:** do not counter. Ask for context first ("help me understand how you arrived
  at this number"). A lowball sometimes signals level disagreement rather than budget.
- **He is in the middle of several processes:** treat it like a competitive sales close.
  Sequence, deadlines, who is in the lead.
- **The note is silent on a leverage point Matt asserts in chat:** use it for this run, flag it,
  and hand it to `asset-updater` so the note gains it with his confirmation.
