---
name: requirements-user-stories
description: Turns workshop notes, process maps, or transcripts into a structured requirements set and a backlog of user stories with acceptance criteria, priorities, and open questions. Use when the user is preparing for a system build or configuration, writing a backlog, or briefing developers or a vendor.
---

# Requirements and User Story Writer

## What this produces
A requirements catalog, a prioritized user story backlog with acceptance criteria, and an open-questions list.

## Inputs to ask for
- Workshop notes, interview transcripts, or a process map
- The users and roles involved
- Systems the solution must integrate with
- Known rules, policies, and compliance constraints
- Volumes and performance expectations
- If notes are thin, generate the questions to ask in the next session instead of guessing

## Method
1. Extract requirements and classify them: functional, data, integration, reporting, security and access, and non-functional (performance, availability, audit).
2. Group functional requirements into epics that match business capabilities.
3. Write each story as "As a [role], I want [capability], so that [outcome]." The role must be a real user, never "the system."
4. Write acceptance criteria in Given, When, Then form, including at least one error or exception case per story.
5. Test each story against INVEST: independent, negotiable, valuable, estimable, small, testable. Split any that fail small or testable.
6. Prioritize with MoSCoW, tying each must-have to a business outcome.
7. Log every ambiguity, conflict between stakeholders, and assumption as an open question with the person who can answer it.

## Output format
- Requirements catalog: ID | Type | Requirement | Source | Priority
- Backlog: Epic | Story ID | Story | Acceptance criteria | Priority | Dependencies
- Open questions: Question | Why it matters | Who answers | Needed by

## Quality checks
- Every story traces to a requirement and a source
- Every story has an exception case
- Non-functional requirements are present
- No story contains two capabilities

## Notes from the source article
- **Replaces:** The business analysts who run requirements sessions and turn them into a backlog of user stories with acceptance criteria.
- **Example request:** “Here’s the transcript from our two-hour session with the claims team about the new intake process. Write the requirements and the user stories for the vendor.”
- **What the user still owns:** Deciding between stakeholders who want conflicting things, and saying no to scope that does not earn its cost.
- When handing the deliverable back, name in one line the decision above that stays with the user.
