---
name: ai-use-case-prioritizer
description: Builds an inventory of AI use cases from workflow descriptions, interview notes, or idea lists, scores each on value and feasibility, and ranks a funded shortlist. Use when the user is collecting AI ideas across departments, choosing where to start with AI, or cleaning up a sprawling list of pilots.
---

# AI Use-Case Inventory and Prioritizer

## What this produces
A use-case inventory, a value-feasibility matrix, and a shortlist of three to five with reasons.

## Inputs to ask for
- Idea lists, workshop notes, or interview notes by function
- Process volumes: transactions per month, hours spent
- Systems and data each process uses
- Pilots already running
- If volumes are missing, ask for rough ranges and mark the scores as estimates

## Method
1. Rewrite each idea as a workflow change: who does the work today, what step changes, what the output is. Drop ideas that name a tool but no workflow.
2. Merge duplicates; the same document-reading task often appears in three departments.
3. Score value 1 to 5: hours or cost removed (volume times time per unit times loaded rate), revenue or error impact, and strategic fit.
4. Score feasibility 1 to 5: data quality, system access, process stability, error tolerance (how bad a wrong answer is), and change burden on the people doing the work.
5. Plot a 2x2. High-value, low-feasibility items become data or process fixes first.
6. Flag any use case that makes decisions about people (hiring, credit, benefits) for governance review before funding.
7. Pick the shortlist: mostly quick wins, at most one bet, spread across functions.

## Output format
- Inventory: ID | Function | Workflow step | Current effort | AI change | Data needed | Value | Feasibility
- 2x2 matrix listing IDs per quadrant
- Shortlist: Use case | Annual value estimate | Why now | First step | Owner

## Quality checks
- Every value score shows its arithmetic or is marked an estimate
- No use case is scored without naming the data it needs
- The shortlist has a named business owner, not only IT

## Notes from the source article
- **Replaces:** The AI discovery phase: cross-functional workshops producing a use-case long list and a value-feasibility matrix.
- **Example request:** “Here are the AI ideas from our ops, finance, and customer service offsites, about 60 in total. Build the inventory and tell me the five we should fund first.”
- **What the user still owns:** Choosing the business owners who will change how their teams work, which decides whether any of this ships.
- When handing the deliverable back, name in one line the decision above that stays with the user.
