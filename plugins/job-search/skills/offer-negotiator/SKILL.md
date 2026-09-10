---
name: offer-negotiator
description: "Helps Matt Cornet negotiate a job offer — drafts counter-offer emails, verbal scripts, and scenario plans for handling pushback. Use whenever Matt mentions receiving an offer, asks to negotiate salary/comp, mentions \"they came back with X\", or asks for a counter-offer email. Also use when he's evaluating multiple offers and needs leverage framing."
---

# Offer Negotiator

## What this skill does

Drafts negotiation collateral grounded in:
- The offer details (base, bonus, equity, signing, benefits, level, start date)
- Matt's BATNA — current consulting income, other interviews in flight, his last comp at FactSet
- Market data for the role/level/geography
- His actual leverage points (bilingual, NY/Paris flexibility, post-merger integration scarcity, immediate availability)

The deliverable is a tailored email + a verbal script + an "if they say X, you say Y" cheat sheet.

**The email and the script are spoken and signed by Matt.** A counter-offer that does not sound like him is worse than a plain one: the person reading it has already met him.

## Source materials

> Paths marked *(project)* are relative to the **Job Applications project root** — the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications"). Paths marked *(vault)* are relative to the connected `obsidian-vault` folder.

> **Voice reference moved, 2026-09-10.** How Matt writes lives in *(vault)* `Notes/Writing voice.md`: §2 corpus, §3 banned constructions, §4 review test, §5.1 the candidature-prose surface this skill writes in. Run `ls $HOME/mnt/` and check for `obsidian-vault`; if it is not connected, ask Matt to connect `C:\Users\mattc\Obsidian\obsidian-vault` before drafting. `_assets/voice_matt.md` and the "Voice & style guidelines" section of `candidate_profile.md` are stubs — never read them as rules, never write to them.

1. ***(vault)* `Notes/Writing voice.md` — read before drafting the email or the script.** Corpus of Matt's own sentences, the literal list of constructions never to write, and the review test.
2. *(vault)* `Notes/Matt Cornet.md` — durable identity, target roles, and the "Technology and scope ceilings" list. A leverage claim that breaches a ceiling is a claim he cannot defend on the call that follows.
3. *(project)* `_assets/candidate_profile.md` — for leverage framing and factual guardrails
4. The offer details (Matt provides)
5. Optional: market comp data from public sources (Levels.fyi, BLS, recent role-specific surveys)

## Inputs to gather (ask if missing)

- Company, role, level
- Full offer breakdown: base, target bonus %, equity (RSUs/options, vesting, refresh), signing, relocation, benefits delta vs. current
- Geography (NY, Paris, remote, hybrid)
- Other offers or active processes (BATNA)
- Matt's target / floor numbers
- Tone he wants — collaborative, firm, walk-away-ready
- Whether the offer was verbal or written, and the deadline

If Matt only gives the headline number, push gently for the full package — equity and bonus can swing total comp by 30%+ at his level.

## Workflow

### Step 0 — Company overview (prerequisite)

This skill relies on the application's `company_overview.md`. **If `applications/<company>-<role>/company_overview.md` does not exist, run the `company-overview` skill first** to research the company and create it; otherwise read and reuse it. Use the company's stage, funding, ownership, and business model to calibrate leverage, comp expectations, and equity framing.

### Step 1 — Sanity-check the offer

Quick analysis in chat:
- Is the level appropriate (vs. his last FactSet Global Director role)?
- Is the base in market range for role/geo? Use public comp data; cite sources.
- What's the all-in TC (base + bonus + equity/4)?
- What looks soft and likely negotiable? (Almost always: base, signing, equity, start date. Rarely: title, level, bonus structure.)

### Step 2 — Identify leverage

Match Matt's leverage to the gap he's asking to close:
- **Other offers / processes:** name them generically ("a competing offer at a similar-stage firm")
- **Scarcity of his combo:** post-merger integration + AI productization + bilingual + NY/Paris is genuinely rare
- **Immediate availability:** at his level, this is worth real money
- **His current consulting rate as anchor:** if the offer is below his blended consulting rate, that's a fact, not a bluff

### Step 3 — Draft the counter

**Email format (default):**
- 4–6 short paragraphs
- Open: enthusiasm + reaffirmation of mutual fit (1 paragraph)
- Middle: specific asks with rationale grounded in market + his leverage (2–3 paragraphs, max 2–3 specific asks — bundling is fine, scattershot is bad)
- Close: collaborative framing, propose a specific next step (call, written response by date)

**Write it in Matt's voice, per *(vault)* `Notes/Writing voice.md`.** Plain declaratives, no metaphor, no image, no defining himself against an implied lesser candidate, no sentence announcing what the next one will do. In a negotiation this matters twice over: rhetorical flourish reads as pressure, and pressure invites resistance. The number and the reason carry the ask.

Save: `applications/<company>-<role>/negotiation/counter_email_<date>.md`

**Verbal script:** for the follow-up call, a 60-second opening + bullet talking points. Written to be spoken aloud, so short sentences and ordinary verbs matter more here than anywhere else. Save: `applications/<company>-<role>/negotiation/verbal_script.md`

**Pushback playbook:** "if they say X, you say Y" for the 6 most likely responses (e.g., "we don't move on base" → pivot to signing/equity; "this is our best offer" → silence + restate top priority; "we need an answer today" → buy 24-48h with a specific reason).

### Step 4 — Decision framework

If Matt has multiple offers or is weighing this against staying independent, give him a comparison table:
- All-in TC year 1, year 4
- Cash vs. equity mix
- Career optionality (does the role open or close future moves?)
- Risk profile (early-stage vs. established)
- Lifestyle (geo, travel, hours)

### Step 5 — Review against the voice test, then deliver

Run the §4 review test in *(vault)* `Notes/Writing voice.md` over the email and the script before showing them: strike every image, every self-definition by negation, every announcement sentence, every verb of certainty that should be an observation.

If Matt rewrites any part, **add his version verbatim to §2 of *(vault)* `Notes/Writing voice.md`** in the same turn. If the vault is not connected, hand him the sentence and say it still needs filing rather than writing it into `_assets/`.

## Output: present to Matt

Deliver the email, verbal script and playbook to the outputs panel with `SendUserFile` so he can open and copy them, plus a 5-line summary in chat of the strategy. Keep the copies in the application folder. Never produce a PDF.

## Hard rules

- **Never lie.** Don't suggest claiming a competing offer that doesn't exist or inflating prior comp. Reputational risk in his sector (small fintech world) outweighs any negotiation gain.
- **No figures of speech**, in the email or the script. See `Notes/Writing voice.md` §3.
- **Never read voice rules from `_assets/voice_matt.md` or from `candidate_profile.md`.** Both are stubs as of 2026-09-10.
- **Never anchor below market.** If Matt's target floor is below market median, push back on the floor before drafting.
- **Don't write inflammatory language.** Even firm asks should preserve the relationship — he might work with these people for a decade.
- **Surface deadline pressure.** If they're rushing, name it in the strategy and recommend a counter that buys time.
- **Consider the level question first.** Sometimes the right negotiation is on title/scope, not comp — a bigger role at the same money compounds for years.
- **Never give personalized financial advice.** Lay out the numbers and the trade-offs; the decision is his.

## Edge cases

- **The vault is not connected:** ask Matt to connect it before drafting. Do not fall back to the stubs.
- **Verbal offer only:** First step is to get it in writing before negotiating. Draft the "thank you, please send written terms" email instead.
- **Lowball offer:** Don't counter — ask for context first ("help me understand how you arrived at this number"). Lowballs sometimes signal level disagreement, not budget.
- **He's in the middle of multiple processes:** treat this like a competitive sales close — sequence, deadlines, who's in the lead.