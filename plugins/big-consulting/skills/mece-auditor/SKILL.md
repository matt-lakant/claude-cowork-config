---
name: mece-auditor
description: Audits any issue tree, framework, list of options, or slide structure for MECE violations (overlaps, gaps, mixed logic, level mismatches) and proposes a corrected structure. Use when reviewing a problem breakdown, a workstream split, a list of recommendations, or any categorization before it goes in front of executives.
---

# MECE Auditor

## What this produces
A findings table of every MECE violation with a specific fix, and a corrected version of the structure.

## Inputs to ask for
- The structure to audit (tree, list, table of contents, workstream chart; paste or attach)
- The parent question or category each list is meant to cover
- Any numbers that belong to the buckets, so exhaustiveness can be tested arithmetically
If the parent question is missing, infer it, state the inference, and audit against it.

## Method
1. Restate the parent of each list; nothing is exhaustive of an undefined parent.
2. Overlap test: for each pair of siblings, name one real item that could fall into both. If you can, it is an overlap.
3. Gap test: name something that belongs to the parent but fits no sibling. Where numbers exist, check that children sum to the parent; a residual above 10% of the parent is a gap.
4. "Other" test: an "other" or "miscellaneous" bucket larger than 10 to 15% means the split is wrong.
5. Mixed-logic test: siblings must use one dimension (all regions, or all products, never "North America, Retail, Pricing").
6. Level test: siblings should sit at the same altitude; "Europe" next to "the Hamburg plant" is a level mismatch.
7. Propose the fix: re-split on a single dimension, promote or demote nodes, or convert to a mathematical identity.

## Output format
- Findings table: Node | Violation type (Overlap / Gap / Mixed logic / Level mismatch / Oversized other) | Evidence (the specific item or number) | Fix
- Corrected structure as an indented outline
- One-line verdict: MECE, MECE with minor fixes, or rebuild

## Quality checks
- Every overlap names a concrete item that falls in two buckets
- Every gap names a concrete missing item or a numeric residual
- The corrected structure is itself re-tested and passes
- Fixes do not change the parent question

## Notes from the source article
- **Replaces:** The engagement manager’s red pen on every tree and slide structure, checking for overlaps and gaps against MECE, the principle associated with Barbara Minto’s work at McKinsey.
- **Example request:** “Audit these five workstreams for our cost program and tell me where they overlap or leave something out.”
- **What the user still owns:** Accepting a structure that is 95% clean when the last 5% is not worth the fight. MECE is a tool for clear thinking, and sometimes the org chart wins.
- When handing the deliverable back, name in one line the decision above that stays with the user.
