# Personal Data

Versioned copies of the personal files the `job-search` skills read and write.
These live on Matt's machine in the **Job Applications** project folder; this
directory is the git-tracked mirror of them.

> **Private repo.** This folder holds a resume, a candidate profile, and an
> application tracker that names real companies and real people. Keep the
> repository private, and think twice before adding collaborators.

## Expected layout

| Path | What it is | Written by |
|---|---|---|
| `_assets/candidate_profile.md` | Canonical experience, voice rules, target roles, and the append-only tailoring Q&A log. The ground truth every skill reads first. | `asset-updater`, `resume-tailor`, `resume-redteam` |
| `_assets/master_resume.docx` | The formatted master resume. Used as the .docx template so tailored output keeps its fonts and table layout. | `asset-updater` |
| `applications_tracker.md` | Live tracker of every application: company, role, date, source URL, status, follow-up due date. | `application-tracker` |
| `applications/<slug>/` | One folder per opportunity: job description, `company_overview.md`, tailored `CORNET_*.docx`, `tailoring_notes.md`, `redteam_notes.md`, `interview_prep/`. | the pipeline |

## Sync

This mirror is populated by hand or by a Claude session that has the
**Job Applications** folder connected. It is a backup and a history, not the
working copy: the skills always read and write the folder on Matt's machine.

Copy direction is **machine → repo**. Never copy repo → machine without
checking which side is newer, or an in-flight application gets clobbered.
