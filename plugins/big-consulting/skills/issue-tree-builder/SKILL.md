---
name: issue-tree-builder
description: Builds a diagnostic (why) or solution (how) issue tree from a key question, decomposed three to four levels deep until each leaf maps to a single analysis. Use when a problem statement is agreed and the work needs to be broken into pieces, or when a team needs to divide workstreams.
---

# Issue Tree Builder

## What this produces
An issue tree three to four levels deep, as an indented outline plus a table mapping every leaf to its analysis and data.

## Inputs to ask for
- The key question (if none exists, run a key-question sharpening pass first)
- Whether the need is diagnostic ("why is this happening") or solution ("how do we fix it")
- Revenue lines, cost structure, segments, main processes
- Financial or KPI exports (attach CSV or spreadsheet) to size the branches
If the business model is unclear, ask for the P&L by line rather than guessing.

## Method
1. Pick the tree type. Diagnostic trees end in root causes; solution trees end in actions. Never mix them in one tree.
2. Choose the first split by strongest logic, in this order: a mathematical identity (revenue = volume x price; cost = units x unit cost), then a process sequence (order, fulfill, bill, collect), then segments, then stakeholders.
3. Split each branch by one dimension only per level. State the splitting logic next to every node.
4. Go three to four levels until each leaf is answerable by one analysis in under a week.
5. For each leaf, write the analysis, data source, and whether data likely exists.
6. Size branches with any numbers provided.
7. Mark any branch the user cannot influence as "context, not lever".

## Output format
1. Key question at the top
2. Indented tree, with the splitting logic in brackets at each level, e.g. "[split by: price x volume]"
3. Leaf table: Leaf | Analysis | Data source | Data exists? (Y/N/Partial) | Est. value at stake
4. The branches most likely to hold the answer, in three lines

## Quality checks
- Each level uses one splitting dimension
- Children of every node add up to the parent where the logic is mathematical
- Every leaf has a concrete analysis, not a topic
- Depth never exceeds four levels

## Notes from the source article
- **Replaces:** The team-room whiteboard session where the engagement manager and associates argue for two days over how to break the key question into the tree that organizes the whole project.
- **Example request:** “Build me an issue tree for why our gross margin in the distribution business fell four points in 18 months. P&L export attached.”
- **What the user still owns:** Deciding which branches are politically live. When a branch runs straight through someone’s department, you choose how to open it.
- When handing the deliverable back, name in one line the decision above that stays with the user.
