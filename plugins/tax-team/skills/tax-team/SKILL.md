---
name: tax-team
description: "Runs Matt's seven-specialist US tax review in order (income, entity, retirement, deductions, investments, real estate and exit, compliance), sets up the Tax Team folder and document checklist, and holds the shared rules every specialist follows. Use when Matt says \"run the tax team\", \"tax review\", \"tax check-up\", \"which tax specialist should I run\", asks for the October or quarterly tax pass, or asks what documents the tax team needs. For one specialist by name, use that specialist's skill directly."
---

# Tax Team (orchestrator)

Seven specialists, each with one job, run in a fixed order so each can read the reports of the
ones before it. This skill sets up the run, decides which specialists apply, and owns the rules
they share.

Adapted from Wally Darling's public Notion page "The Claude Tax Team: 7 Specialists" (Darling
Financial Group). The prompts were rewritten as skills; the partner marketing was removed.

**Scope: US federal income tax for a US resident filer, plus the state on the return.** Nothing
in this plugin is tax, legal or investment advice. The team finds and sizes; a licensed
professional decides. Nothing here files, elects, signs or trades.

## The team

| # | Skill | Job | Report file | Reads |
|---|---|---|---|---|
| 1 | `tax-income-analyst` | Which bracket every dollar hits; income taxed harder than needed | `01-income-map_<date>.md` | documents only |
| 2 | `tax-entity-specialist` | Sole prop / S-corp / C-corp and salary vs distributions at real profit | `02-entity_<date>.md` | 1 |
| 3 | `tax-retirement-specialist` | Contributed vs ceiling, including cash balance / DB room | `03-retirement_<date>.md` | 1, 2 |
| 4 | `tax-deduction-specialist` | What is claimed, what is never asked about, and whether the paper exists | `04-deductions_<date>.md` | 1 |
| 5 | `tax-investment-specialist` | Loss harvesting, Roth windows, equity comp, gains timing | `05-investments_<date>.md` | 1 |
| 6 | `tax-real-estate-exit` | Cost seg, REPS, QSBS clocks, sale structuring | `06-real-estate-exit_<date>.md` | 1, 5 |
| 7 | `tax-compliance-specialist` | Safe harbor, screening flags, paperwork, calendar, one-page brief | `07-compliance-brief_<date>.md` | all |

Skip rules, decided after the Income Analyst has run:

- No business income (no Schedule C, no K-1 from an active business, no 1120-S / 1065 / 1120): skip 2.
- Every investment sits in retirement accounts and there is no equity comp: skip 5.
- No rental property, no founder or early-stage C-corp stock, no planned sale of a property,
  business or large position: skip 6.
- 1 and 7 always run.

Say which ones were skipped and why at the top of the Compliance brief.

## Setup

### Working folder

`C:\Users\mattc\OneDrive\Documents\Claude\Projects\Tax Team\`, flat, no subfolders. If it does
not exist, create it (request folder access on the parent first if it is not connected). All
reports land here and every specialist reads earlier reports from here.

**Never write tax documents or reports into `claude-cowork-config`.** That repo holds
configuration only.

### Documents to gather

Whatever Matt has is enough to start; each specialist names what is missing and what it would
change.

- Last two personal returns (1040 with all schedules)
- Business returns if any (1120-S, 1065, 1120, or Schedule C)
- P&L: year to date and last full year
- K-1s
- Comp statement or recent pay stubs (W-2)
- Retirement plan statements
- Equity grant documents (RSUs, options, ESPP)
- Recent brokerage export (lots with dates and basis)
- Depreciation schedules (if any property)

Documents may come from files Matt attaches, the Tax Team folder, or the docs of a claude.ai
Project. Use whichever exists and say which.

## Running it

**First run: in order, 1 to 7.** After the Income Analyst, stop and show Matt the Income Map
summary and the skip decisions before going on: if the map is wrong, everything downstream is
wrong.

Large document sets: run each specialist in its own session. Each reads the earlier reports
from the folder, so nothing is lost between sessions. When asking Matt to start a new session,
hand him the text to paste, for example:

```
Run tax-retirement-specialist. Earlier reports are in the Tax Team project folder.
```

**Cadence after the first run:**

- Re-run `tax-compliance-specialist` each quarter with updated YTD numbers (estimated
  payments are the point).
- Re-run the whole team each October, while there is still time to act before December 31.

When a specialist re-runs, it reads the **most recent** dated report of each earlier
specialist and says which date it used.

## Shared rules (each specialist repeats these; this is the reference copy)

1. **Confirm figures before calculating.** Brackets, contribution limits, rates, thresholds and
   mileage rates change every year, and some changed with 2025 legislation. Before any
   calculation, look up the current-year value of every figure the specialist uses, preferably
   on irs.gov or another primary source, and put them in a **Figures used** table (figure,
   value, tax year, source). Numbers written into these skills are starting points as of 2025-26,
   not facts to reuse.
2. **Compute in code.** Every dollar figure is computed in Python from the documents, not
   estimated in prose. Show the inputs.
3. **Ranges, not points, when assumptions drive the number.** State each assumption. If the
   documents cannot support a range, write "not sizable from these documents" and name the
   document that would size it. Never invent a figure.
4. **One verdict per finding:**
   - **FINE AS IS**: the position is sound and supported. Move on.
   - **WORTH FIXING**: a different structure, timing or process does better. Model it before the
     next filing year.
   - **BRING IT TO A STRATEGIST**: the saving looks real, but implementing it crosses a licensing
     line (securities, insurance, actuarial, legal, or an election with state consequences).
5. **Findings are ranked** by the midpoint of their annual dollar range, largest first.
6. **Separate document facts from inference.** Cite the document and line or box for every
   figure taken from Matt's paperwork.
7. **Missing documents** are listed at the end with what each would change.
8. **Save and surface.** Write the report to the Tax Team folder under its file name with
   today's date (`YYYY-MM-DD`), then send it as a file card.

## Report skeleton (every specialist)

```
# <NN> <Specialist> - <date>
Documents read: ...        Earlier reports read: ...
## Figures used
## <specialist's working sections>
## Findings (ranked)
| # | Finding | Annual $ range | Verdict | Evidence |
## Missing documents
## Summary for the rest of the team   (fixed headings, see each skill)
```
