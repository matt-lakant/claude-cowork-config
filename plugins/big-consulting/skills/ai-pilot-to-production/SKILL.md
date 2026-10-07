---
name: ai-pilot-to-production
description: Assesses an AI pilot's results and builds the plan to move it into production: evidence review, production requirements, operating model, rollout waves, monitoring, and success metrics. Use when the user has an AI pilot that worked (or seems to) and needs to scale it, or a pilot that has stalled short of production.
---

# AI Pilot-to-Production Plan

## What this produces
An evidence review, readiness gaps, an operating model, rollout waves, and a monitoring spec.

## Inputs to ask for
- Pilot scope, duration, users, and volumes
- Results: accuracy or quality measures, time saved, user feedback, error examples
- The baseline the pilot was compared to
- How the pilot connects to systems, and who supports it
- If there was no baseline, flag value as unproven

## Method
1. Review evidence: was the result measured against a baseline, on real volume, with the real users? Separate measured results from anecdotes.
2. Review errors: sample failures, classify their cause, and decide which need a fix before scale.
3. List what the pilot skipped: real integration, access controls, logging, cost at full volume, security and governance review.
4. Design the operating model: business owner, technical owner, who handles exceptions the AI cannot, who updates prompts or models, and how users report problems.
5. Redesign the workflow: which steps humans keep, where review happens, which jobs change.
6. Plan rollout waves by team or site, each with entry criteria and a checkpoint.
7. Define monitoring: quality sampled weekly, usage, cost per transaction, and business outcome against baseline.

## Output format
- Evidence review: Claim | Measured or anecdotal | Result | Confidence
- Readiness gaps: Area | Gap | Fix | Owner | Before wave
- Operating model table: Role | Responsibility | Named owner
- Rollout plan: Wave | Scope | Entry criteria | Date | Checkpoint metric
- Monitoring: Metric | Frequency | Threshold | Action

## Quality checks
- Measured results are separated from anecdotes
- Cost is projected at full production volume
- Every wave has entry criteria
- The workflow change for users is written down

## Notes from the source article
- **Replaces:** The scale-up plan that turns a successful AI pilot into a supported, measured part of daily work.
- **Example request:** “Our AI claims triage pilot ran for eight weeks in one region and the team loves it. Here are the results. Build the plan to take it to all five regions.”
- **What the user still owns:** Changing the jobs and the workflow around the tool, and funding the support it needs after the pilot team moves on.
- When handing the deliverable back, name in one line the decision above that stays with the user.
