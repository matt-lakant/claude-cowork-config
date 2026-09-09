---
name: recruiter-followup
description: "Drafts follow-up messages from Matt Cornet to recruiters and hiring managers — application follow-ups, post-interview thank-yous, ghosted-process check-ins, and reactivation notes. Use whenever Matt mentions following up with a recruiter, sending a thank-you, or reaching out to a hiring manager. Also use when he says he hasn't heard back from someone and wants to nudge."
---

# Recruiter Follow-up

## What this skill does

Drafts short, in-voice follow-up messages for the four most common recruiter touchpoints: post-application, post-interview, ghosted-process nudge, and warm reactivation of a stale lead. Output is paste-ready email/LinkedIn copy.

**Everything this skill produces goes out under Matt's name.** Voice is not a finishing touch here, it is the deliverable.

## Source materials

> All paths in this skill are relative to the **Job Applications project root** — the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications").

1. **`_assets/voice_matt.md` — read this before writing a single sentence.** It holds the corpus of Matt's own sentences, the literal list of constructions never to write, and the review test. Abstract guidance ("sober, no hype") has repeatedly failed to prevent the specific turns of phrase he cuts; the corpus and the banned-construction table are what actually work.
2. `_assets/candidate_profile.md` — for concrete hooks and factual guardrails
3. Any prior thread context Matt provides (paste of original message, last reply, etc.)

## Inputs to gather

- Recipient name + role (recruiter, hiring manager, exec)
- Channel (email, LinkedIn DM, InMail, **LinkedIn connection note — hard cap 300 characters**)
- Stage (applied, screened, interviewed, ghosted N weeks, dormant lead)
- Company + role (or "general networking")
- Key thread context: what was the last touch, what was promised, what's the open question

## Workflow

### Step 0 — Company overview (prerequisite)

This skill relies on the application's `company_overview.md`. **If `applications/<company>-<role>/company_overview.md` does not exist, run the `company-overview` skill first** to research the company and create it; otherwise read and reuse it. Use it to make the "one concrete value-add" in each message specific to the company's business, sector, and recent signals.

### Step 1 — Pick the template

| Stage | Template | Send-after timing |
|---|---|---|
| Post-application | `applied_followup` | 7–10 days after applying |
| Post-screen / interview | `post_interview_thanks` | Within 24h |
| Ghosted process | `ghosted_nudge` | 2 weeks after expected response |
| Stale lead / past conversation | `warm_reactivation` | Anytime; reference the prior thread |
| Recruiter cold reach-back | `cold_recruiter_reply` | Within 48h, even if not interested |
| Cold approach to a named contact | `connection_request` | Anytime; 300-character cap on LinkedIn |

### Step 2 — Draft principles (apply across all templates)

- **Length:** 4–8 sentences max. Recruiters skim. Senior leaders skim harder. A LinkedIn connection note is 300 characters, full stop — count them before delivering.
- **Subject lines:** specific, not generic. "Following up — [Role] at [Company]" beats "Touching base."
- **Open:** name a specific thing from the last interaction. Generic "hope you're well" is dead weight.
- **Middle:** one concrete value-add — a recent relevant insight, a link, a clarification, or a fresh data point. Never just "checking in."
- **Close:** a clear, low-friction ask. Specific question or concrete CTA, not "let me know."
- **Voice: follow `_assets/voice_matt.md`.** Matt writes plain declaratives. No metaphor, no image, no calque of an English idiom, no defining himself against an implied lesser peer, no sentence announcing what the next one will do, no self-commentary. Facts carry the message; figures of speech get cut.
- **Sign-off:** "Best, Matt" in English, "Matthieu" or "Matthieu Cornet" + phone in French correspondence.

### Step 3 — Templates (use as starting points, customize per context)

#### applied_followup
Open: reference role + date applied. Middle: a 1-sentence reminder of why he's a strong fit (specific to the JD, drawn from `candidate_profile.md`). Close: ask if there's an update on timing or a next step.

#### post_interview_thanks
Open: thanks + name one moment from the conversation that resonated (Matt provides; if not, ask). Middle: one substantive follow-on — a thought he's developed since the call, a resource link, or an answer to something left open. Close: looking forward to next steps.

#### ghosted_nudge
Open: brief, not passive-aggressive. Middle: one new piece of information that justifies the touch (e.g., a relevant article, a milestone, a competing-process update if true). Close: explicit ask — "would it help if I sent X?" or "should I assume the role is on hold?" Give them an out.

#### warm_reactivation
Open: name the prior context ("we spoke last March about [Role]"). Middle: what's changed on his side that makes the conversation timely now. Close: propose a specific next step (15-min call, intro to someone).

#### cold_recruiter_reply
Open: thanks for reaching out. Middle: 1-sentence read of the role from his perspective + 1 honest signal (interested / interested-but-conditional / not-this-one-but-future). Close: practical next step or a graceful pass.

#### connection_request
Under 300 characters. State the concrete reason for reaching out, ask one answerable question, and give one line of who he is. **If Matt has already applied to a role at that company, say so** — it sits in their ATS, and staying silent about it looks worse than naming it. **Do not ask why nobody replied**: it extracts no information and puts the recipient on the defensive. "Is the recruitment still open?" gets the same answer at no relational cost.

### Step 4 — Review against the voice test, then deliver

Before output, run the review test in `_assets/voice_matt.md`: strike every image, every "I am not the kind of person who…", every sentence that announces the next one, every verb of certainty that should be an observation. Count characters if there is a cap.

Deliver the message to the outputs panel with `SendUserFile` so Matt can open and copy it (see the `feedback_show_short_texts_in_chat` guidance), and keep a copy under `applications/<company>-<role>/correspondence/<YYYY-MM-DD>_<recipient>.md`. Never produce a PDF.

### Step 5 — Feed the corpus

If Matt rewrites any part of the message, **add his version verbatim to section 2 of `_assets/voice_matt.md`** in the same turn. A sample needs no threshold to be worth keeping. If his edit reveals a recurring construction to avoid, add a row to the banned table in section 3.

## Hard rules

- **No figures of speech.** If a word does not mean literally what it says, cut it. This is the single most frequent correction Matt makes.
- **Never claim "I have a competing offer" if he doesn't.** Reputational damage is permanent.
- **Don't apologize for following up.** "Sorry to bother you" weakens the message.
- **Don't oversell.** A senior candidate over-pitching reads as desperate. State value once, clearly.
- **Match the channel.** LinkedIn DMs are shorter than emails. InMails get one shot. Connection notes are capped at 300 characters and the cap is not negotiable.
- **Match the language of the relationship.** French recipients get French, even when the posting was in English (see `feedback_application_language`).
- **If Matt names the recruiter,** check if the recruiter is internal (TA at the company) vs. external (agency) — the tone differs slightly. Internal: peer-collaborative. External: respect-the-relationship-they-have-with-the-company.