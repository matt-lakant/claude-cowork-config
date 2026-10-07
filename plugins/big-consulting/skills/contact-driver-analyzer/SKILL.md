---
name: contact-driver-analyzer
description: Classifies why customers contact you from ticket, call, chat, and email data, separates avoidable contacts from value-adding ones, and sizes the cost of each driver. Use when contact volume is rising, the user wants to cut cost to serve, or reason codes are too messy to trust.
---

# Contact Driver Analyzer

## What this produces
A clean reason taxonomy, volume and cost by driver, and the avoidable drivers ranked by cost with an upstream owner.

## Inputs to ask for
- Ticket or call export, 6 to 12 months (CSV or XLSX): date, channel, reason code, free-text subject or notes, handle time, repeat flag.
- Cost per contact by channel, or agent loaded cost per hour.
- Order, account, or customer counts per month to normalize volume.
- If reason codes are missing or unreliable, classify from free text and report the share classified with low confidence.

## Method
1. Build a two-level taxonomy (8 to 12 categories, 30 to 60 reasons) from the free text. Reclassify a 200-record sample and report agreement with existing codes.
2. Normalize: contacts per 100 orders or per active customer, by month, to separate growth from failure.
3. Tag each reason: value-adding (sales, advice), failure demand (a contact caused by something the company failed to do or do right, John Seddon's term), or self-service candidate.
4. Compute repeat rate per reason (same customer, same reason, within 7 days).
5. Cost each reason: volume x handle time x cost per minute, plus repeat contacts.
6. Assign each top avoidable driver to the upstream team that causes it (billing, logistics, product), following the principle in Price and Jaffe's The Best Service Is No Service.

## Output format
1. Taxonomy with volume share.
2. Driver table: Reason | Volume | Per 100 Orders | Repeat % | AHT | Annual Cost | Type | Upstream Owner.
3. Top 10 avoidable drivers with the likely root cause.

## Quality checks
- Volumes reconcile to the export total.
- "Other" and "General inquiry" are under 10% of volume.
- Every root cause is labeled hypothesis until confirmed.

## Notes from the source article
- **Replaces:** The first service diagnostic: analysts pull a year of tickets, rebuild the reason codes, and show which contacts should never have happened.
- **Example request:** “Here’s 12 months of Zendesk tickets and call logs. Tell me why customers are contacting us and which reasons we could eliminate.”
- **What the user still owns:** Getting the upstream team to fix the cause. The contact center can measure failure demand but rarely controls it.
- When handing the deliverable back, name in one line the decision above that stays with the user.
