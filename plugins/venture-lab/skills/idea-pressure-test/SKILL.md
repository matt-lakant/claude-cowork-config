---
name: idea-pressure-test
description: "Pressure-tests a business idea that Matt originated or is already carrying, rather than one extracted from a source document. Scores it against an 11-gate rubric, attacks it with three fresh-context adversaries (investor, incumbent PM, target buyer), returns one of six verdicts, pre-registers a kill test, and files it in the Obsidian vault as a `type: idea` note whose re-tests are appended by date. Use whenever Matt describes a business idea and asks whether it holds up, says \"pressure test this\", \"stress test this idea\", \"poke holes in it\", \"red-team this\", \"should I build this\", \"is this a business\", \"what am I missing\", or points at an existing vault idea or venture note and asks for a critique or a re-test. Use `paper-digest` instead when the input is a paper, article, or post he wants read and judged."
---

# Idea Pressure Test (screen, attack, verdict, file)

> Paths marked *(vault)* are relative to the connected `obsidian-vault` folder, normally
> `C:\Users\mattc\Obsidian\obsidian-vault`. Check the connected folders first
> (`get_device_info`, or `device_list_dir`). If the vault is not connected, request access to
> that path before doing any work that has to land in it, and say so rather than writing the
> note somewhere else. *(vault)* `CLAUDE.md` is the house rules and wins over this file on any
> vault question: property schema, allowed `type` and `status` values, filing conventions.

## Purpose

Matt generates more ideas than he can test, and the expensive failure is not a bad idea, it is
a plausible idea that absorbs a month. This skill exists to spend twenty minutes killing an
idea so it cannot spend four weeks.

**The default answer is no.** A run that concludes "interesting, not a business" and names the
gate that killed it is a successful run. A run that promotes a pleasant idea to "possible
wedge" because the conversation had momentum has failed, and the cost lands on his calendar,
not in this file.

The vault already says it: be a critic, not a cheerleader. This skill is where that is
operationalized.

## What this is not

- Not `paper-digest`. That reads a source Matt shares and judges whether there is a business in
  it. This one starts from an idea Matt already has, with no document to anchor claims to,
  which makes invention a bigger risk here, not a smaller one.
- Not a business plan writer. No decks, no financial models, no go-to-market sections.
- Not a promotion mechanism. This skill never creates a `type: venture` note. Promoting an idea
  to a venture is Matt's decision and it happens outside this skill.

## Non-negotiables

- **Never invent market sizes, competitor details, funding figures, customer counts, or
  statistics.** Standing vault rule. An empty gate is information. Write "unknown" and move on.
  "Unknown" scored honestly beats a plausible number, every time.
- **Do not fill in facts Matt has not given.** Empty sections in an idea note are information.
  Ask, or mark the gap. The `T-idea.md` sections "What made me think of it" and "Why me" carry
  his reasoning and cannot be written for him.
- **Separate Matt's material from your inference.** His words go in the body sections. Every
  conclusion you reach goes under `## AI notes`. Never blend the two.
- **Research the market, never the note.** The vault holds personal and financial material. Web
  queries are about incumbents, categories, and public companies. Never paste note content,
  vault text, or Matt's own framing into a search query or a fetched form.
- **Attribution discipline on anything you looked up.** Name the source and its date. A
  competitor's own marketing page is a claim, not a fact. A funding round from three years ago
  does not establish that a company is alive today, so say when you could not confirm.
- **Do not transfer credibility.** An idea being good for someone is not it being good for a
  solo consultant in Paris with no capital and no team. Gate 10 exists for this.
- Vault house style: English (US), concise, bullets over prose, **no em dashes**.

## Workflow

### Step 0 — Restate the idea in one sentence, and locate the note

Write the idea back in one sentence: **who buys what, and what it replaces.** Put it at the top
of the run.

If that restatement needs an assumption Matt did not state (which buyer, which of two possible
products, sold as software or as his time), **stop and ask before scoring anything.** Half the
bad runs come from pressure-testing a slightly different idea than the one he has.

Then check whether this already exists in the vault:

- Search *(vault)* `Notes/` for a `type: idea` or `type: venture` note on this subject, by
  topic and by likely alternative names, not just the title he used.
- **Found, and it holds a previous pressure test** → this is a re-test. Go to Step 1b.
- **Found, no previous test** → work on that note. Never open a second note for the same idea.
- **Not found** → this is a first run, and the note gets created in Step 7.

### Step 1a — Fast screen (default entry point)

Three gates, no web research, no subagents. Target: a few minutes. Score each **Pass / Weak /
Fail** with one line of evidence.

| # | Gate | The question |
|---|---|---|
| 1 | Buyer | Who has this pain acutely enough to pay, by role and segment, with a budget line that already exists? "Enterprises", "SMBs", "compliance teams" are all Fail. Name the title that signs. Check for a structural conflict: if the buyer is the person the idea indicts, or is also the technical approver, that is a Fail, not a hard sale. |
| 2 | Insight | What does Matt know, or have access to, that a competent team starting today does not? Name it and name its size. An observation anyone in the industry shares is not an insight. Neither is a preference about how software should work. |
| 3 | Why now | What changed in the last 24 months that makes this possible or urgent? A regulation with a date, a price that collapsed, a capability that just became reliable. If the idea was equally possible in 2021, either someone built it (gate 4 will find them) or nobody wants it. "AI is better now" is a Fail unless you can say which capability and what it unlocked. |

**Hard cap:** a Fail on 1, 2, or 3 caps the verdict at *interesting, not a business*, whatever
the rest would score. Write the cap and the reason, skip the full pass, and go to Step 5.
Do not run adversaries on an idea already dead. Tell Matt what killed it and stop.

If all three are Pass or Weak, tell him the screen survived and what the full pass will cost
him (research plus three subagents, roughly fifteen to thirty minutes), then run it. Do not ask
permission for the full pass unless he is clearly mid-flow on something else.

**Batch input.** If Matt hands over more than three ideas at once, screen all of them first,
report a ranked table of screen results, and ask which survivors he wants fully tested. Never
full-pass a list.

### Step 1b — Re-test of an existing idea

Read the note's most recent `## Pressure test <date>` section before anything else.

**The standing rule: if the last run pre-registered a kill test and it was never run, this run
does not produce a new verdict.** Hand him back the same kill test, its threshold, and the date
it was set. An idea re-scored instead of tested is how a month disappears with nothing learned.

He can override that in the moment, and sometimes should: new information arrived, the buyer
changed, the kill test turned out to be unrunnable. Take the override, but **record the reason
in the new section** so the pattern is visible if it repeats.

Otherwise, open the re-test by naming what changed since the last run: the kill test result,
new facts, a different buyer. Then run Steps 2 to 4 normally. Gate scores may move in either
direction, and a re-test that moves every score upward with no new evidence is a failed
re-test.

### Step 2 — Research, then the remaining eight gates

Research first, score second. Scoring before looking is how gate 4 comes back empty.

Look up, with web search: who sells this today, including the incumbent the buyer already pays;
who tried it and is gone; what the adjacent category costs. Nothing about Matt, nothing from the
vault. If a search returns nothing usable, write "unknown" and score the gate on that, which is
usually a worse result for the idea than a crowded field.

| # | Gate | The question |
|---|---|---|
| 4 | Graveyard | Who already tried this, and what killed them? Name companies and dates where you can, and say when you could not confirm one is still trading. A large obvious market nobody has attacked is a warning, not an opening: find the reason before assuming there is none. |
| 5 | Wedge | Why would that buyer not use what is already in their stack? Include "doing nothing" and "a spreadsheet" as competitors, because they usually win. Then ask separately whether a won account has a second sale or is consumed on first use. |
| 6 | Repeatability | Is sale two the same product as sale one, or is every deal bespoke? List the preconditions a buyer must meet, then name real segments that meet **all** of them. If each engagement needs its own data model, its own integration, and its own ontology, this is consulting wearing a product's clothes, and the verdict has a slot for that. |
| 7 | Moat at 12 months | A competent team copies the core idea in a week. Where does defensibility actually sit after that: proprietary data, pipeline operations, domain ontology, evals and calibration, compliance posture, distribution. If nowhere, Fail. Being first is not a moat. Being better is not a moat. |
| 8 | Distribution | How do the first ten buyers hear about this, with no marketing budget and no team? Warm network counts only **by name**: three people Matt can call who hold the budget. "My LinkedIn network" and "content marketing" are Fail. If acquisition needs paid channels, gate 9 has to carry that cost. |
| 9 | Economics | Back of envelope, and say it is one. Revenue per customer, how many customers to matter against Matt's actual income floor, and roughly what it costs to serve one. An idea needing 400 customers at a low monthly price is not a solo business, whatever else is true about it. Check the cost to serve against how much of it is Matt's own hours. |
| 10 | Founder fit | Fit for **Matt specifically**, read against *(vault)* `Notes/Matt Cornet.md`, including its technology and scope ceilings and its framing guardrails. Solo, Paris, advisory-led, no production-AI shipping record, no capital, no team, current business is selling his own time. His closed data points count: lakant.io was nearer his expertise and signed zero clients, which is a completed kill test on easier terrain. Ask what that one taught that applies here. |
| 11 | Kill test | The cheapest experiment that falsifies the whole thing inside a week, with the threshold written **before** it runs. It has to be able to fail: a warm-network conversation with a low bar passes by default and carries no information. Pre-register the number, not the intent. Prefer a factual question whose every possible answer kills something over any pitch. |

**Second cap:** a Fail on gate 8 or 9 caps the verdict at *consulting offer, not a product*.
The idea may still be sellable as Matt's time. It is not a software business.

### Step 3 — Three adversaries, fresh context, in parallel

The context that built the gate table will defend it. Spawn three subagents (`Agent`, type
`general-purpose`). This is a sanctioned, standing part of Matt's setup.

Hand each one **only**: the one-sentence restatement, the gate table with scores and evidence,
the research findings, and Matt's actual position (solo, Paris, no production-AI record, no
capital or team, current business is selling his own time). **Never hand over the reasoning that
produced the scores, or any "why this is promising" framing.** They are there to kill it.

**A. The investor.**

> You are a skeptical pre-seed investor who passes on 99 of 100 technical founders. Below is a
> business idea and a scored rubric. Your job is to kill it. Do not validate, do not hedge to be
> fair. Return: (1) the single strongest reason this is a feature and not a company; (2) every
> place the argument smuggles in an assumption nothing supports, quoting it; (3) which gate
> scores are too generous and what they should be; (4) whether the pre-registered kill test is
> any good, and a cheaper one that would falsify the thesis faster. End with one line: pass /
> worth a week / worth a month, and the one thing that would change your mind.

**B. The incumbent product manager.**

> You are a product manager at the vendor this buyer already pays. Someone proposes the idea
> below as a startup. Explain how you would neutralize it: what you ship as a line item next
> quarter, what you already have that covers most of it, how your account team frames it on a
> renewal call, and what it would cost your customer to switch. Then name the one thing you
> could not copy within a year, if there is one. Be specific about the product surface.

**C. The target buyer.**

> You are the exact person named as the buyer below: that role, that segment, that budget
> reality. A consultant pitches you this. You say no. Explain why, in your own terms. Cover:
> what you actually do about this problem today and what it costs you; whose budget this would
> come out of and what it would displace; who else has to approve it and what they will say; and
> what would have to be true for you to take a first meeting. Do not be polite about it.

Require at least **three substantive attacks from each**. A thin or congratulatory critique is a
failed adversary, not a clean idea. Re-run that one.

### Step 4 — Reconcile, do not append

Where an adversary is right, **change the gate score** in the note and mark it revised. Where
one overreaches, keep the score and record the counter in one line. The note shows one final
table, not four competing ones.

Expect them to be right more often than not. **If nothing got revised, suspect the
reconciliation, not the idea.** Re-read the buyer's objection first, because that is the one
most often waved away.

Record separately, in one line each: the strongest attack that survived reconciliation, and any
attack that was wrong and why. The second one matters on re-tests, so a settled objection does
not get re-litigated every run.

### Step 5 — Verdict

One of these six. Nothing in between, no numeric score, no percentage.

1. **Nothing here** — no insight, or a solved problem.
2. **Interesting, not a business** — real observation, no buyer or no repeatability.
3. **Feature, not a company** — a capability someone else ships as a line item.
4. **Consulting offer, not a product** — sellable as Matt's time or a fixed-price build, not as
   software. Before using this, check the offer does not silently depend on something the client
   does not have: their own labelled data, a held-out set, internal access, a sponsor.
5. **Possible wedge** — one named buyer and one experiment worth running. Requires a
   pre-registered kill test with a number.
6. **Strong** — reserve it. If nothing has been Strong in months, the rubric is working.

Then three mandatory pieces, in this order:

- **Why this is not a business** — a paragraph written in good faith even at verdict 5 or 6. If
  it comes out thin, the verdict is too high. Go back and re-read gate 1.
- **The kill test** — the week-one experiment, its pre-registered threshold, and the date.
- **What it is actually worth** — required at verdicts 1 to 3. An idea can be a first-rate
  observation about a market with no business in it, and saying which part to keep, or which
  other idea it strengthens, is the real output of most runs.

### Step 6 — Kill criteria and the experiment note

Fill the `## Kill criteria` section of the idea note from the pressure test, not from
imagination. It is the section Matt wrote the template to force, and it is worth more than the
verdict.

At verdict **5 or 6 only**, offer to create one `type: experiment` note from *(vault)*
`Templates/T-experiment.md`, carrying the pre-registered threshold into `## Success threshold`
and linked both ways to the idea note. **Ask first, and create at most one per run.** Its
`## Hypothesis` needs Matt's own belief, which you cannot write for him.

Never create a `type: venture` note. Never create a `type: decision` note; a decision record is
his to write after the experiment runs.

### Step 7 — File it

**Note** → *(vault)* `Notes/<Descriptive Title>.md`, built on *(vault)* `Templates/T-idea.md`.

Filenames: descriptive, no leading dates, no special characters. If the path exists and is a
different idea, ask before writing; never bulk-rename.

**Frontmatter:**

- `type: idea`, `created` as `YYYY-MM-DD`. Both fixed at creation and **never edited later**.
- `domain` is **always a list**, even with one value.
- **There is no `tags` property in this vault.** Do not add one, and no inline `#hashtags`.
  `domain` classifies, `related` carries the meaning.
- `related` is a YAML list of quoted wikilinks, not `related: []` when there is anything to link.
- Preserve all existing frontmatter on a re-test. Add, never replace.

**`status`, mapped from the verdict:** verdict 4, 5, 6 → `exploring`. Verdict 2 or 3 →
`parked`. Verdict 1 → propose `dead` in the reply and **write `parked` until Matt says
otherwise**. Killing a note is his call, not yours. Never invent a status outside the vault's
allowed list.

**Assessment placement.** Everything you concluded goes under `## AI notes`, inside a dated
section:

```markdown
## AI notes

### Pressure test 2026-09-14

**Verdict:** Feature, not a company
**Restated as:** <one sentence>
...
```

**A re-test appends a new dated section. It never edits or deletes an earlier one.** The
history of an idea's failed tests is the most useful thing in the note, and it is the only
defence against re-running the same optimism in six weeks.

**The note must be reachable. An orphan is a failed run.** Before finishing:

1. Search the vault for an existing note this genuinely touches, and link it **both ways**,
   preserving the other note's frontmatter.
2. If nothing exists, the run has almost always surfaced one live question bearing on Matt's
   actual work. Create **one** `type: question` note from *(vault)* `Templates/T-question.md`,
   linked both ways. Its "What I currently believe" needs his prior, so **ask him** rather than
   filling it.
3. If neither applies, say plainly in the reply that the note is an orphan and why. Do not file
   it silently.

### Step 8 — Deliver

Surface the written vault files as clickable file cards in the chat (`SendUserFile`), even
though they were written straight into the vault. Writing to the folder alone is not delivery.
Give every delivered file a distinct, specific filename; never `SendUserFile` a generically
named file, because a delivered file can be written back beside the last file of that name
staged from the device and silently leave a stray copy in the wrong folder.

Then, in the chat reply and nothing more:

- The verdict, in the six-verdict vocabulary.
- The one sentence behind it, naming the gate that decided it.
- The kill test and its threshold.

The reasoning lives in the note. Do not restate the note in the conversation.

Matt commits and pushes the vault himself in GitHub Desktop, so end with a ready-to-paste
commit message covering every file written.

## Failure modes to watch in yourself

- **Verdict inflation.** The pull toward "possible wedge" is strong because it feels more
  useful to say. It is not more useful. It costs him a week. Re-read gate 1 before settling, and
  if the "why this is not a business" paragraph came out thin, the verdict is wrong.
- **Scoring the idea you would have had.** Step 0 exists because it is easy to quietly improve
  the idea into a better one and then score that. If the version you scored is better than the
  version he described, you have tested nothing.
- **Buyer inflation.** "Compliance teams at mid-size European banks" is a segment, not a buyer.
  The gate wants the title that signs and the budget line it comes from.
- **Treating an empty graveyard as an opening.** Nobody having tried a large obvious thing is
  evidence against it, not for it, until you find the reason.
- **Letting the founder-fit gate be polite.** It is the gate most likely to be softened, because
  scoring it honestly means telling Matt this is not for him. Score it against the ceilings in
  `Notes/Matt Cornet.md`, not against enthusiasm in the room.
- **Re-scoring instead of testing.** Step 1b's rule is there because rescoring feels like
  progress and is not. An untested kill test from three weeks ago outranks a new rubric run.
- **Inheriting a framing you just rejected.** After concluding the buyer is wrong, check no
  later gate still assumes that buyer. Scores below a killed gate are usually stale.
- **Congratulatory adversaries.** If a subagent comes back agreeing, it failed. Re-run it with a
  harder brief rather than treating the agreement as a signal.
