---
name: skills-gap-ai-exposure-map
description: Breaks roles into tasks, rates each task's exposure to AI (automate, augment, or unchanged), estimates hours shifted per role, and maps the resulting skills gaps and reskilling needs. Use when the user wants to know how AI will change specific jobs, where capacity will free up, or what skills the workforce needs next.
---

# Skills Gap and AI Exposure Map

## What this produces
A task inventory per role with AI exposure ratings, hours freed or changed, a skills gap table, and a reskilling priority list.

## Inputs to ask for
- Roles in scope with headcount (HRIS export or list).
- Job descriptions, SOPs, or time studies showing what each role does.
- Any skills inventory or assessment data.
- If task data is missing, draft task lists from O*NET-style task statements and mark them for validation by role managers.

## Method
1. Break each role into 8 to 15 tasks with an estimated share of time. Shares sum to 100%.
2. Rate each task: automate (AI completes with light review), augment (AI speeds the person), or unchanged (physical, relational, judgment-heavy). This follows the task-level approach in public research such as Eloundou et al., 2023, "GPTs are GPTs."
3. Estimate time change: automate tasks at 50 to 80% time reduction, augment at 20 to 40%, as editable assumptions.
4. Compute hours shifted per role and in total FTE equivalents.
5. List skills each role needs after the shift (reviewing AI output, exception handling, customer judgment) and compare against current skills data.
6. Rank reskilling needs by headcount affected times gap size.

## Output format
1. Task table: Role | Task | Time Share | Exposure | Time Change.
2. Role summary: Role | Headcount | Hours Shifted % | FTE Equivalent.
3. Skills gap: Role | Future Skill | Current Level | Gap.
4. Reskilling priorities (top 10).

## Quality checks
- Time shares per role sum to 100%.
- Freed hours are labeled as capacity; any headcount reduction is a separate, explicit decision.
- Every rating has a one-line reason.

## Notes from the source article
- **Replaces:** A future-of-work assessment, when a team breaks roles into tasks, rates which tasks AI changes, and maps the skills each role will need next.
- **Example request:** “Here are job descriptions for our 12 largest roles in accounts payable and customer service. Show me which tasks AI changes and what skills these people need next.”
- **What the user still owns:** What you do with the freed hours. Redeploy, absorb growth, or reduce: that call and its message to the workforce belong to leadership.
- When handing the deliverable back, name in one line the decision above that stays with the user.
