---
name: data-readiness-assessment
description: Assesses whether data is ready for a specific AI or analytics use case by profiling samples against quality dimensions, access, ownership, and governance, and produces a remediation plan. Use when the user attaches data extracts or schemas and asks whether their data is good enough for AI or what data work comes first.
---

# Data Readiness Assessment

## What this produces
A data profile per source, a readiness rating for the named use case, and a ranked remediation plan with effort estimates.

## Inputs to ask for
- The use case and the decision or task the data must support
- Sample extracts (CSV or XLSX, a few thousand rows) and field definitions
- For documents, emails, or calls: a sample set
- Access and privacy constraints
- If only a schema is available, assess structure and ownership and say quality is untested

## Method
1. List the data the use case needs, field by field, with its source and owner.
2. Profile each sample: row counts, null rates per field, distinct values, format validity, duplicates, date ranges, and outliers.
3. Rate quality dimensions per field: completeness, accuracy (check against a known source where possible), consistency across systems, timeliness, validity, and uniqueness.
4. For unstructured data, check volume, format mix, legibility, and labeling.
5. Assess access: scheduled extraction, by whom, with what approval.
6. Rate readiness per required field: ready, fixable, or missing. The use case is only as ready as its most critical missing field.
7. Plan remediation: fix at source, clean in pipeline, or collect new data, with owner and effort.

## Output format
- Required data map: Field | Source | Owner | Readiness
- Profile table: Field | Null % | Valid % | Duplicates | Notes
- Readiness rating with a three-sentence rationale
- Remediation plan: Issue | Fix | Where | Owner | Effort (S/M/L)

## Quality checks
- Profile statistics are computed from the supplied sample, and sample size is stated
- Every required field has a readiness rating
- Personal data is flagged
- The rating is tied to the named use case

## Notes from the source article
- **Replaces:** The data assessment before an AI program: profiling source data, rating quality, listing what to fix first.
- **Example request:** “We want AI to predict which orders will ship late. Here are extracts from our ERP and the carrier file. Tell me if the data is good enough and what to fix first.”
- **What the user still owns:** Making the source-system owners fix the data at the source, which takes a management decision.
- When handing the deliverable back, name in one line the decision above that stays with the user.
