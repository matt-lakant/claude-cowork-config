---
name: risk-control-matrix
description: Builds a risk and control matrix (RCM) for a business process, mapping risks to controls with full attributes, financial statement assertions, and test procedures. Use when the user is documenting controls for SOX or internal audit, preparing for an external audit, or finding where a process has no control.
---

# Risk and Control Matrix Builder

## What this produces
An RCM for one process, a list of uncovered risks, and a test procedure per key control.

## Inputs to ask for
- The process in scope (order to cash, procure to pay, record to report, payroll, IT general controls)
- Process narratives, flowcharts, or SOPs
- Existing control lists or prior RCMs
- Systems and materiality thresholds
- If no documentation exists, interview the user through the process first

## Method
1. List process steps from initiation to recording in the ledger.
2. At each step ask "what could go wrong" and write the risk. Tie financial risks to the relevant assertions: existence or occurrence, completeness, valuation or allocation, rights and obligations, presentation and disclosure (the PCAOB AS 1105 set; AICPA and IAASB standards also list accuracy and cutoff separately).
3. Map existing controls to each risk. Record owner, frequency, type (preventive or detective), nature (manual, automated, IT-dependent manual), and evidence retained.
4. For review controls, record precision: the threshold that triggers follow-up. A review with no threshold is weak by design.
5. Flag reports used in controls as information produced by the entity; they need a completeness and accuracy check.
6. Mark key controls: the fewest controls that cover every significant risk.
7. Check segregation of duties between initiate, approve, record, and custody.
8. Write a test procedure per key control: sample size by frequency, attributes tested, evidence.

## Output format
- RCM: Risk ID | Step | Risk | Assertion | Control ID | Control description | Owner | Frequency | Type | Nature | Key (Y/N) | Test procedure
- Gaps: Risk | Why uncovered | Proposed control
- Segregation of duties conflicts list

## Quality checks
- Every significant risk maps to at least one key control
- Every control description states who, what, when, and evidence
- Review controls state precision
- Automated controls are linked to IT general controls

## Notes from the source article
- **Replaces:** The documentation phase of a SOX program: mapping every process risk to a control, with attributes and test steps.
- **Example request:** “Here’s our procure-to-pay SOP and last year’s control list. Build the RCM and show me where we have risks with no control.”
- **What the user still owns:** Deciding which gaps to fix before year-end and defending your key-control selection to the external auditor.
- When handing the deliverable back, name in one line the decision above that stays with the user.
