# Why the rules are what they are

Not loaded during a run. Kept so that a rule can be traced to the incident that produced it before anyone removes it.

| Date | What happened | Rule it produced |
|---|---|---|
| 2026-09-04 | A re-post was assumed and written up as fact; five days later the new posting vanished and the old one stayed up | `application-brief` Step 2: two postings are an inference, not proof of a re-post |
| 2026-09-04 | A "remove PMP" decision sat in the log for nine days while CVs kept printing it | A correction is applied at the source in the same run |
| 2026-09-10 | Voice rules were split between the project and the vault | The vault note is the only voice reference |
| 2026-09-24 | The cover letter drafted in the same pass as the CV read like a CV | The letter is written by `cover-letter` from the final CV |
| 2026-10-07 | Professional services CVs listed too few client engagements | R5: 3 under FactSet 2019-2024, 2 under 2007-2018 |
| 2026-10-08 | Finance wording left on CVs for non-finance employers until Matt flagged it | R4, applied in the first draft |
| 2026-11-10 | "90% on the planned date" was ambiguous | R6: the reference to the date planned at project start is mandatory |
| 2026-11-13 | A reviewer proposed removing the skills matrix; Matt refused | R7: the matrix stays |
| 2026-11-16 | A CV printed "EBITDA 27% to 32% over 3 years", superseded six days earlier; it came in through the base file | Current values table; the base file is audited; figures are never taken from a previous CV |
| 2026-11-16 | Two drafts for an "EMEA" role lacked "EMEA"; one lacked the employer's core noun | Top-third keywords, checked by script |
| 2026-11-16 | Matt answered "lead with the direct team"; the draft opened on 80+ and USD 40M | Decisions table, each row matched to a CV line |
| 2026-11-16 | The red-team rewrote about 20% of each CV, mostly with facts already on record | Evidence search before drafting (`application-brief` Step 3) |
| 2026-11-16 | Four questions were asked only after the reviewer's attack | Reviewer's questions asked before drafting (`application-brief` Step 5) |
| 2026-11-16 | CVs and letters were US Letter | R15: A4, checked by script |
| 2026-11-16 | Matt: what matters is the seniority conveyed, not the word count; and it depends on the role, not on freelance or permanent | R18 to R20, role tag `hands_on` or `leadership` |
| 2026-11-17 | `resume-tailor` had grown to 44 KB and 16 steps | Split into `application-brief`, `resume-tailor` and `resume-redteam`, each with a step map and a gate |
