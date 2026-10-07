---
name: knowledge-base-gap-finder
description: Compares contact reasons, search queries, and agent notes against the knowledge base to find missing, outdated, duplicate, and unhelpful articles, then prioritizes fixes by contact volume. Use when agents can't find answers, handle times vary widely for the same issue, or the user is preparing content for self-service or an AI assistant.
---

# Knowledge Base Gap Finder

## What this produces
A coverage map of contact reasons against articles, lists of missing, stale, duplicate, and low-performing articles, and a prioritized content backlog.

## Inputs to ask for
- Article export: title, body or summary, last updated date, views, helpfulness votes.
- Search logs, including zero-result queries, from the help center or agent tool.
- Contact reasons with volume, and a sample of agent notes or resolutions.
- If search logs are unavailable, rely on contact reasons and agent notes and say so.

## Method
1. Map each top contact reason (covering 80% of volume) to the articles that answer it. Unmapped reasons are gaps.
2. Cluster zero-result and low-click searches into topics; each topic with volume but no article is a gap.
3. Flag stale articles: not updated in 12 months, or conflicting with a policy or product change the user names.
4. Flag duplicates: two or more articles answering the same question with different answers.
5. Flag low performers: high views with low helpfulness, or views followed by a contact on the same topic.
6. Mine agent notes for resolutions that exist in practice but not in the knowledge base, following the capture-in-the-workflow practice of Knowledge-Centered Service (KCS).
7. Prioritize the backlog by contact volume affected.

## Output format
1. Coverage map: Contact Reason | Volume | Article(s) | Status.
2. Gap lists: Missing | Stale | Duplicate | Low Performing, each with volume.
3. Content backlog: Article to Write or Fix | Volume Affected | Source of Answer | Owner.

## Quality checks
- Every gap ties to volume data.
- Duplicate pairs show the conflicting statements.
- Draft article content is marked for expert review before publishing.

## Notes from the source article
- **Replaces:** A knowledge management audit, when a team matches contact reasons and search logs against the article library to find what is missing, wrong, or stale.
- **Example request:** “Here’s our help center export, three months of search logs, and top contact reasons. Tell me what’s missing or wrong before we point an AI assistant at this content.”
- **What the user still owns:** The owner for every article. Knowledge rots when nobody’s job includes keeping it current.
- When handing the deliverable back, name in one line the decision above that stays with the user.
