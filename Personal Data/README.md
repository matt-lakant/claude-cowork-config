# Personal Data

Versioned copies of the personal assets the `job-search` skills read.

**Source on Matt's machine:**
`C:\Users\mattc\OneDrive\Documents\Claude\Projects\Job Applications\_assets`

> **Private repo.** This folder holds a resume and a candidate profile.
> Keep the repository private, and think twice before adding collaborators.

## What is here

| File | What it is |
|---|---|
| `_assets/candidate_profile.md` | Canonical experience, voice rules, target roles, and the append-only tailoring Q&A log. The ground truth every job-search skill reads first. |
| `_assets/master_resume.docx` | The formatted master resume. Used as the .docx template so tailored output keeps its fonts and table layout. |
| `_assets/master_resume_v2.docx` | Alternate master layout. |
| `_assets/master_resume_v3.docx` | Alternate master layout. |

## What is deliberately not here

- **`applications_tracker.md` and `applications/`** — working state, not personal
  data. Not versioned, by Matt's decision.
- **`master_resume_*_pre_<date>.docx`** — automatic pre-edit backups written by
  `asset-updater`. Git history replaces them; mirroring them here would version
  the same document twice.

## Sync

Copy direction is **machine → repo**. This is a backup and a history, not the
working copy: the skills always read and write the OneDrive folder above.
Never copy repo → machine without checking which side is newer.
