---
name: current-state-architecture
description: Builds a current-state map of applications, data flows, integrations, and ownership from system lists, interviews, and diagrams, and flags the fragile points. Use when the user needs to understand their systems before a transformation, an ERP or CRM change, an AI rollout, or an acquisition integration.
---

# Current-State Architecture Mapper

## What this produces
An application inventory, an integration and data-flow map, a diagram in Mermaid syntax, and a list of architectural risks.

## Inputs to ask for
- Application list or CMDB export (CSV), with owners if known
- Existing diagrams, even outdated ones
- Interface or integration lists (file transfers, APIs, middleware jobs)
- IT and process owner interview notes
- The business capabilities in scope (for example quote to cash)
- If no inventory exists, walk the user through each capability and ask which systems it touches

## Method
1. Build the inventory: system, capability, business and IT owner, hosting, vendor, version, users, cost.
2. Map integrations: source, target, data carried, method (API, file, manual re-keying, spreadsheet), frequency, and who fixes it when it breaks.
3. Identify the system of record for each core data entity (customer, product, supplier, employee, order). Two systems claiming the same entity is a finding.
4. Draw the map as a context view (systems and users) and an integration view, in Mermaid.
5. Mark fragile points: manual handoffs, spreadsheets acting as systems, single-person knowledge, unsupported versions, point-to-point integrations with no monitoring.
6. Note what the map means for the transformation in scope: which systems it must touch and which integrations it will break.

## Output format
- Application inventory table
- Integration table: Source | Target | Data | Method | Frequency | Owner
- System-of-record table: Entity | System of record | Other copies
- Mermaid diagrams (context and integration)
- Risk list: Risk | Where | Impact | Suggested fix

## Quality checks
- Every integration has a method and a named owner, or is flagged unknown
- Manual and spreadsheet steps are shown as integrations
- Every core entity has a system of record or a finding

## Notes from the source article
- **Replaces:** The architecture assessment: IT interviews and old diagrams turned into the systems map every later decision depends on.
- **Example request:** “Here’s our application list and the notes from interviews with IT and finance. Map our order-to-cash systems and show me where it’s held together with spreadsheets.”
- **What the user still owns:** Confirming the map with the people who run the systems, because the undocumented integration is always the one that breaks.
- When handing the deliverable back, name in one line the decision above that stays with the user.
