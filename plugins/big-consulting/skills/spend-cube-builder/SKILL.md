---
name: spend-cube-builder
description: Builds a classified spend cube (category, supplier, business unit, period) from raw AP, GL, or PO exports, with Pareto, fragmentation, and addressability flags. Use when starting a cost or procurement program, when someone asks where the money goes, or when third-party spend has never been classified.
---

# Spend Cube Builder

## What this produces
A classified spend table and one-page summary: category spend, supplier concentration, tail, PO coverage, addressable spend, data gaps. In Claude Code, also save the cleaned CSV.

## Inputs to ask for
- AP invoice-line export, 12 to 24 months (CSV or XLSX): vendor, amount, date, GL account, cost center, line description
- Vendor master (tax ID if available), PO file, chart of accounts, cost-center hierarchy
- GL total for the same period, for reconciliation
With no PO file, build on AP only and mark PO coverage unknown.

## Method
1. Reconcile AP to the GL total. If the gap exceeds 2%, stop and ask.
2. Normalize vendors: strip legal suffixes and punctuation, match on tax ID, roll children to a parent.
3. Classify every line to a three-level taxonomy (L1 such as IT, Facilities, Professional Services, Logistics, Travel; then L2, L3) from GL account, vendor, and description, with confidence high, medium, or low.
4. Tag addressability: non-addressable covers taxes, payroll, intercompany, and rent locked under lease.
5. Run Pareto: suppliers making up 80% of spend, and the tail (suppliers under USD 10K per year).
6. Per category, compute supplier count, top-supplier share, number of business units buying, and PO coverage.
7. Flag anomalies: repeat vendor and amount within 7 days, one-time vendors, negative lines.

## Output format
- Table: L1 | L2 | Spend | % of total | Suppliers | Top supplier share | BUs buying | PO coverage % | Addressable
- Top 20 suppliers by parent
- Tail: supplier count, spend, % of total
- Anomalies; data gaps

## Quality checks
- Cube total reconciles to the GL within 2%, gap stated
- Unclassified spend is under 5% or reported as a limitation
- Low-confidence classifications are listed for human review

## Notes from the source article
- **Replaces:** Week one of a cost program: two analysts pulling AP and GL extracts, cleaning vendor names by hand, and building the cube in a spreadsheet.
- **Example request:** “Here’s 18 months of AP invoice lines and our vendor master. Build me the spend cube and tell me where the fragmentation is.”
- **What the user still owns:** Category owners must accept the taxonomy, or they will reject every savings number built on it.
- When handing the deliverable back, name in one line the decision above that stays with the user.
