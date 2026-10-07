---
name: controls-walkthrough-narrative
description: Plans a controls walkthrough and turns interview notes and evidence into an audit-ready process narrative with design-effectiveness conclusions. Use when the user must document a walkthrough, prepare process owners for auditors, or write a narrative from meeting notes or a recording transcript.
---

# Controls Walkthrough Narrative

## What this produces
A walkthrough plan with questions, then a process narrative that traces one transaction through every control, with a design conclusion per control.

## Inputs to ask for
- The RCM or control list for the process
- Walkthrough notes or transcript, if the meeting has happened
- Evidence collected: screenshots, reports, approvals, tickets
- Names and roles of process owners
- If the meeting has not happened, produce the plan first and stop

## Method
1. Plan: select one real transaction per significant flow. Prepare questions per control: who performs it, when, what they look at, what triggers follow-up, what happens to exceptions, what evidence remains.
2. During the walkthrough, confirm by inquiry plus at least one of observation, inspection, or reperformance. Inquiry alone does not support a design conclusion.
3. Write the narrative in sequence: initiation, authorization, processing, recording, reporting. Name the system and role at each step; embed control IDs where they operate.
4. For each control, conclude on design: does it address the risk at the right precision, is it performed by someone competent and independent, is evidence retained?
5. Note every difference between the documented and observed process.
6. List design gaps with the risk left open.

## Output format
- Walkthrough plan: Control ID | Question | Evidence to request
- Narrative: numbered paragraphs, control IDs in brackets, under 1,500 words per flow
- Design conclusions: Control ID | Designed effectively (Y/N) | Basis | Gap
- Differences from documentation list

## Quality checks
- Every control in the RCM appears in the narrative or is noted as not observed
- Every conclusion cites the evidence type used
- No step lacks a named role or system
- The transaction selected is identified by reference number

## Notes from the source article
- **Replaces:** The walkthrough meetings where a consultant follows one transaction end to end with process owners and writes the narrative the auditors will read.
- **Example request:** “Here’s the transcript from this morning’s revenue walkthrough and the screenshots the AR lead sent. Write the narrative and tell me which controls look weak.”
- **What the user still owns:** Whether the process owner’s answers are true, and fixing the gaps before testing starts.
- When handing the deliverable back, name in one line the decision above that stays with the user.
