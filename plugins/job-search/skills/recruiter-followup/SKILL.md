---
name: recruiter-followup
description: Drafts follow-up messages from Matt Cornet to recruiters and hiring managers — application follow-ups, post-interview thank-yous, ghosted-process check-ins, and reactivation notes. Use whenever Matt mentions following up with a recruiter, sending a thank-you, or reaching out to a hiring manager. Also use when he says he hasn't heard back from someone and wants to nudge.
---

# Recruiter Follow-up

## What this skill does

Drafts short, in-voice follow-up messages for the four most common recruiter touchpoints: post-application, post-interview, ghosted-process nudge, and warm reactivation of a stale lead. Output is paste-ready email/LinkedIn copy.

## Source materials

> All paths in this skill are relative to the **Job Applications project root** — the folder that contains this `skills/` directory. Resolve them against whichever folder Matt has connected for the current session (typically the one named "Job Applications").

1. `_assets/candidate_profile.md` — for voice and concrete hooks
2. Any prior thread context Matt provides (paste of original message, last reply, etc.)

## Inputs to gather

- Recipient name + role (recruiter, hiring manager, exec)
- Channel (email, LinkedIn DM, InMail)
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

### Step 2 — Draft principles (apply across all templates)

- **Length:** 4–8 sentences max. Recruiters skim. Senior leaders skim harder.
- **Subject lines:** specific, not generic. "Following up — [Role] at [Company]" beats "Touching base."
- **Open:** name a specific thing from the last interaction. Generic "hope you're well" is dead weight.
- **Middle:** one concrete value-add — a recent relevant insight, a link, a clarification, or a fresh data point. Never just "checking in."
- **Close:** a clear, low-friction ask. Specific question or concrete CTA, not "let me know."
- **Voice:** professional, warm, no hype. Mirror Matt's resume profile tone — strategic, business-impact-led, never salesy.
- **Sign-off:** "Best, Matt" — not "Cheers" or "Thanks!" with multiple exclamations.

### Step 3 — Templates (use as starting points, customize per context)

#### applied_followup
Open: reference role + date applied. Middle: a 1-sentence reminder of why he's a strong fit (specific to the JD, drawn from `candidate_profile.md`). Close: ask if there's an update on timing or a next step.

#### post_interview_thanks
Open: thanks + name one moment from the conversation that resonated (Matt provides; if not, ask). Middle: one substantive follow-on — a thought he's developed since the call, a resource link, or an answer to something left open. Close: looking forward to next steps.

#### ghosted_nudge
Open: brief, not passive-aggressive. Middle: one new piece of information that justifies the touch (e.g., a relevant article, a milestone, a competing-process update if true). Close: explicit ask — "would it help if I sent X?" or "should I assume the role is on hold?" Give them an out.

#### warm_reactivation
Open: name the prior context ("we spoke last March about [Role]"). Middle: what's changed on his side that makes the conversation timely now (lakant engagement wrapping, BlueMatrix project transitioning, AI-platform expertise deepened). Close: propose a specific next step (15-min call, intro to someone).

#### cold_recruiter_reply
Open: thanks for reaching out. Middle: 1-sentence read of the role from his perspective + 1 honest signal (interested / interested-but-conditional / not-this-one-but-future). Close: practical next step or a graceful pass.

### Step 4 — Output

Give Matt the message in chat (it's short — file output is overkill unless he asks).

If the message is high-stakes (counter-offer follow-up, exec-level), save to `applications/<company>-<role>/correspondence/<YYYY-MM-DD>_<recipient>.md` so there's a record.

## Hard rules

- **Never claim "I have a competing offer" if he doesn't.** Reputational damage is permanent.
- **Don't apologize for following up.** "Sorry to bother you" weakens the message.
- **Don't oversell.** A senior candidate over-pitching reads as desperate. State value once, clearly.
- **Match the channel.** LinkedIn DMs are shorter than emails. InMails get one shot — make the subject and first sentence carry the message.
- **If Matt names the recruiter,** check if the recruiter is internal (TA at the company) vs. external (agency) — the tone differs slightly. Internal: peer-collaborative. External: respect-the-relationship-they-have-with-the-company.
