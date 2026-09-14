---
name: paper-digest
description: "Reads a technical paper, article, or long-form post that Matt shares, explains it in plain language, judges honestly whether it contains a business, and files it in the Obsidian vault as a `type: source` note with the PDF attached. Use whenever Matt shares a paper, article, blog post, arXiv link, or Medium link and asks to summarize it, explain it, understand it, save it, add it to the vault, or check it for business ideas. Also use when he says \"digest this\", \"is there a business in this\", \"read this for me\", or pastes a link with little other instruction. The business assessment runs through a fixed 7-gate rubric and a fresh-context adversarial subagent, so the default answer is allowed to be \"nothing here\"."
---

# Paper Digest (read, explain, judge, file)

> Paths marked *(vault)* are relative to the connected `obsidian-vault` folder, normally
> `C:\Users\mattc\Obsidian\obsidian-vault`. Check the connected folders first
> (`get_device_info`, or `ls $HOME/mnt/`). If the vault is not connected, request access to
> that path before doing any work that has to land in it, and say so rather than writing the
> note somewhere else.

## Purpose

Matt reads technical material above his hands-on implementation level and wants three things
from it: to actually understand the mechanism, to know whether there is a business in it, and
to keep the artifact. The deliverable is one *(vault)* `source` note plus the PDF.

**The honest answer is often "no business here."** Most good engineering writing is good
engineering writing. A run that concludes "interesting, not a business" and says why is a
successful run. A run that manufactures a venture out of a competent blog post has failed.

## Non-negotiables

- **Read the whole source before writing anything.** For a PDF, that means every page range,
  not the first twenty. The business case usually turns on a limitation the author buries
  two thirds of the way in, and an author selling a thesis in the first third may refute it
  himself in the last.
- **The author's numbers are the author's claims.** Write them as "the author reports" /
  "measured on his own hardware." Never restate an unverified benchmark as fact. Verify with
  a search only when a number is load-bearing for the business verdict, and say what you did.
- **Apply skepticism in both directions.** When an author corrects or reverses his own
  earlier results, the corrections are self-reported too, usually unreplicated and produced
  by the same harness that generated the original errors. Discount them the same way, and say
  so in the note rather than treating the latest number as the true one.
- **Never invent market sizes, competitor details, funding figures, or statistics.** This is a
  standing vault rule. An empty gate is information; write "unknown" and move on.
- **Separate Matt's material from your inference.** Everything you conclude goes under
  `## AI notes` or inside the assessment sections, never mixed into his own words.
- Vault house style: English (US), concise, bullets over prose, **no em dashes**.

## Workflow

### Step 1 — Acquire the source and produce the PDF

The note must point at a PDF that lives in *(vault)* `Attachments/`. Get one, in this order:

1. **Matt attached a PDF** → use it as is. Do not regenerate.
2. **Link with a paywall bypass token** (Medium `?sk=` friend link, arXiv abs/pdf, a public
   post) → fetch and render in the container. Chromium is preinstalled at
   `/opt/pw-browsers/chromium` with Playwright configured; never run `playwright install`.
   Render at A4, `printBackground: true`, and wait for network idle so lazy images land.
3. **Link needing his session** (member-only with no token, corporate portal) → read it
   through Chrome (`claude-in-chrome`) so the content is available, then tell Matt the render
   came back as a paywall stub and ask him to print the page to PDF himself. Do not pass a
   stub off as the artifact, and do not try to route around the paywall.
4. **Direct PDF URL** → download it.

Sanity-check every generated PDF before filing: page count above 1, and the body text
present, not a "Sign in to continue" wall. If the check fails, say so in the reply.

### Step 2 — Read it, then write the explainer

Extract the load-bearing claims with their anchors (page or section). Then write the
explanation for a reader who is technically literate but not hands-on in this subfield:

- **What problem is it solving**, and what the standard approach costs.
- **What the author changed** — the one structural move everything else follows from. If you
  cannot name it in a sentence, you have not finished reading.
- **Why that works**, in mechanism terms, not vocabulary terms. No sentence that only
  restates a term with its own jargon.
- **What the headline numbers actually measure**, including any place the author admits two
  numbers measure different things. Authors of good posts flag these; quote the flag.
- **What would break it** — the stated limits, and the unstated ones you can identify.

### Step 3 — Run the 7 gates, in order, and stop early

Score each gate **Pass / Weak / Fail** with one line of evidence from the source. Order is
deliberate: the cheap kills come first.

| # | Gate | The question |
|---|---|---|
| 1 | Asymmetry | Does it reveal something cheap for the author and expensive for everyone else? Name the asymmetry and its size. A clever engineering choice is not an asymmetry. Neither is an asymmetry that nobody building on it would own, that is decaying, or that produces a component the source's own numbers show is beaten by a free baseline. |
| 2 | Transferability | Is the asymmetry portable, or an artifact of this one dataset/corpus/domain? List the preconditions it needs, then name real candidates that meet **all** of them. A corpus meeting every precondition usually already has a vendor built entirely around it, so say who. |
| 3 | Buyer | Who has this pain acutely enough to pay, by role and segment, with an existing budget line? "Enterprises" is a Fail. Check for a structural conflict: if the buyer is the person the finding indicts, or is also the technical approver on the purchase, that is a Fail, not a hard sale. |
| 4 | Wedge | Why would that buyer not use the incumbent already in their stack? Include "doing nothing" and "a spreadsheet" as competitors. Ask separately whether a won engagement has a second sale, or is consumed on first use. |
| 5 | Moat at 12 months | If a competent team copies the core insight in a week, where does the defensibility actually sit? Pipeline ops, domain ontology mapping, evals and calibration, compliance, distribution. Advice published free in the source itself is not a moat. If nowhere, Fail. |
| 6 | Founder fit | Fit for **Matt specifically**, against *(vault)* `Notes/Matt Cornet.md`, including its technology and scope ceilings. Solo, Paris, advisory-led, no production-AI shipping record. Do not transfer the author's credibility to Matt. Check his closed data points too: lakant.io was nearer his expertise and signed zero clients, which is a completed kill test on easier terrain. |
| 7 | Kill test | The cheapest experiment that would falsify the whole thing inside a week, with the threshold written before it runs. It must be able to FAIL: a warm-network pitch with a low conversion bar passes by default and carries no information. Pre-register the price, not just the intent. Prefer a factual question whose every possible answer kills the idea over any pitch. |

**Hard rule:** a Fail on gate 1, 2, or 3 caps the verdict at *interesting, not a business*.
No amount of strength further down lifts it. Write the cap and the reason.

### Step 4 — Adversarial pass in a fresh-context subagent

The context that wrote the business case will defend it. Spawn a fresh subagent
(`Agent`, type `general-purpose`) and hand it **only** the extracted claims and the draft
business case. Never hand it the explainer's enthusiasm or a "why this is promising" framing.
This spawn is a sanctioned, standing part of Matt's setup.

Brief it:

> You are a skeptical pre-seed investor who passes on 99 of 100 technical founders. Below are
> claims extracted from a technical article and a draft argument that there is a business in
> it. Your job is to kill it. Do not validate, do not hedge to be fair.
> Return: (1) the single strongest reason this is a feature and not a company; (2) every
> place the argument smuggles in an assumption the source does not support, quoting the
> assumption; (3) who already does this, including the incumbent the buyer already pays;
> (4) which of the 7 gate scores is too generous and what it should be; (5) the cheapest
> experiment that would falsify the whole thesis in under a week, and attack whether the
> draft's own kill test is any good.
> End with one line: pass / worth a week / worth a month, and the one thing that would
> change your mind.

Include Matt's actual position in the packet (solo, Paris, no production-AI record, no
capital or team, current business is selling his own time) so gate 6 gets attacked properly.

Require at least **three substantive attacks**. A thin or congratulatory critique is a failed
adversary, not a clean idea. Re-run it.

Then **reconcile, do not merely append.** Where the adversary is right, change the gate score
in the note and mark it revised. Where it overreaches, keep your score and record the counter
in one line. The note shows the final scores, not two competing tables. Expect it to be right
more often than not; if nothing got revised, suspect the reconciliation rather than the draft.

### Step 5 — Verdict

One of these six, nothing in between and no numeric score:

1. **Nothing here** — no asymmetry, or a known result.
2. **Interesting, not a business** — real insight, no buyer or no transferability.
3. **Feature, not a company** — a capability someone else ships as a line item.
4. **Consulting offer, not a product** — sellable as Matt's time or a fixed-price build, not
   as software. Check before using this that the offer does not silently depend on something
   the client does not have (their own labelled data, a held-out set, internal access).
5. **Possible wedge** — one buyer and one experiment worth running. Requires a named kill test.
6. **Strong** — reserve it. If nothing has been Strong in months, the rubric is working.

Then two mandatory pieces, in this order:

- **Why this is not a business** — a paragraph written in good faith even when the verdict is
  5 or 6. If it comes out thin, the verdict is too high.
- **The kill test** — the week-one experiment and its pre-written threshold.

When the verdict is 1 or 2, add a short **what it is actually worth** section. A paper can be
a first-rate methodology document with no business in it, and saying which parts to reuse is
the real value of the run.

### Step 6 — File it

**PDF** → *(vault)* `Attachments/<Descriptive Title>.pdf`
**Note** → *(vault)* `Notes/<Descriptive Title>.md`

Filenames: descriptive, no leading dates, no special characters. If either path exists, ask
before overwriting; never bulk-rename. Build the note on `Templates/T-source.md` with the
assessment sections added under `## AI notes`.

**Frontmatter rules:**

- `type: source`, `status: done`, `created` as `YYYY-MM-DD`. `type` and `created` are fixed at
  creation and never edited later. Preserve existing frontmatter when updating; add, never
  replace.
- `domain` is **always a list**, even with one value.
- **There is no `tags` property in this vault.** Do not add one, and do not use inline
  `#hashtags`. `domain` is the classifier and `related` carries the meaning. Confirmed: zero
  `tags:` keys and zero inline tags across the vault.
- `related` uses a YAML list of quoted wikilinks, matching `Notes/Green Mango.md`:
  ```yaml
  related:
    - "[[Rebuild lakant.com]]"
  ```
  Not `related: []` when there is anything to link.
- Embed the PDF with `![[<Descriptive Title>.pdf]]`, which is an embed and not a wikilink.
  Do not convert between the two.

**The note must be reachable. An orphan is a failed run.** A `source` note links to nothing by
default, and nothing populates `related` later. Worse, Matt's `Dashboard.md` queries `type` of
question, venture and idea, so a `source` note never surfaces there. So before finishing:

1. Search the vault for an existing note this one genuinely touches, and link it **both ways**
   (add the backlink to the other note's `related`, preserving its existing frontmatter).
2. If nothing exists, the paper almost always raises one live thread that bears on Matt's
   actual work. Create **one** `type: question` note from `Templates/T-question.md` for it,
   linked both ways. That note then appears in his Dashboard. It needs his prior in "What I
   currently believe", which you cannot invent, so **ask him for it** rather than filling it.
3. If neither applies, say plainly in the reply that the note is an orphan and why. Do not
   file it silently.

Never create a `venture` note from a paper; that type is for something Matt has decided to
pursue. Create at most one spin-off note per run, and ask before creating it.

### Step 7 — Deliver

Surface both written files as clickable file cards in the chat (`SendUserFile`), even though
they were written straight into the vault. Writing to the folder alone is not delivery.

**Give every delivered file a distinct, specific filename.** Never `SendUserFile` a generically
named file such as `SKILL.md`, `notes.md` or `output.md`: a delivered file can be written back
beside the last file of that name staged from the device, which silently creates a stray copy
in the wrong folder. A session also cannot delete files on Matt's machine, so a stray file
becomes his cleanup. Name it `paper-digest-SKILL.md`, not `SKILL.md`.

Then, in the chat reply and nothing more: the verdict, the one sentence behind it, and the
kill test. The reasoning lives in the note. Do not restate the note in the conversation.

Matt commits and pushes the vault himself in GitHub Desktop, so end with a ready-to-paste
commit message covering every file written.

## Failure modes to watch in yourself

- **Verdict inflation.** The pull toward "possible wedge" is strong because it feels more
  useful. It is not more useful; it wastes his week. Re-read gate 3 before settling.
- **Summarizing instead of explaining.** A list of the author's section headings restated is
  not the explainer. The test is whether Matt could describe the mechanism to someone else
  after reading it.
- **Transferability hand-waving.** "This could apply to any document-heavy industry" is the
  single most common failure. Gate 2 wants named corpora that meet every stated precondition,
  or a Fail.
- **Letting the author's framing set the business frame.** The author is optimizing for a
  compelling post. The headline metric is usually not where the value sits, and the title may
  name a component the author measured and rejected.
- **Inheriting the framing you just rejected.** After concluding the source's approach does
  not work, check that no later step still assumes it is needed. If the source shows a
  component is unnecessary, the alternative is not a cheaper version of that component.
- **Filing an orphan.** A note nothing links to is a note he will never see again.
