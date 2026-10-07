---
name: big-consulting
description: "Index and router for the big-consulting plugin: 150 consulting skills in 15 practices (strategy, markets, growth, pricing, board communication, FP&A, cost, risk, M&A, org design, operations, supply chain, technology, customer service, program delivery). Use when Matt asks which consulting skill fits a problem, wants to run a practice end to end, says \"run the full engagement\", \"big consulting\", \"consulting playbook\", or describes a business problem without naming a skill. For one specific deliverable, the matching skill loads on its own."
---

# Big Consulting

150 skills from Grant Baldwin's article "Big Consulting, Rebuilt as 150 Claude Skills"
(The Craft of AI, geniant): https://www.thecraftofai.com/read/150-consulting-skills-opus-5-5. Each skill produces one deliverable and has the same
five parts: what it produces, inputs to ask for, method, output format, quality checks.

This skill does not produce a deliverable. It picks the skill, the order, and the inputs.

## Three ways to run it

| Mode | When | What to do |
|---|---|---|
| One skill, one deliverable | Matt names a document he needs | Load the matching skill from the index below and follow it |
| One practice, end to end | Matt wants a whole workstream (e.g. "do the pricing work") | Run the practice's ten skills in numerical order; each feeds the next |
| Full engagement | Matt wants the whole project on one problem | Run the sequence below, one skill at a time, saving each output before the next starts |

### Full engagement sequence

The source article names the stages; the skill picked for each stage is this plugin's mapping,
not the author's. Skip a stage when it does not bear on the decision, and say which were skipped.

| Stage | Skills |
|---|---|
| 1. Frame the problem | `key-question-sharpener`, `issue-tree-builder`, `hypothesis-workplan` |
| 2. Size the market | `market-sizing-triangulator`, then practice 02 as needed |
| 3. Choose where to play | `adjacency-screen`, `where-to-play-how-to-win-cascade` |
| 4. Model the money | practices 04, 06, 07 as the question requires |
| 5. Check the risk | practice 08; `assumption-red-team` on the draft answer |
| 6. Redesign the work | practices 10 to 14 as the question requires |
| 7. Plan the delivery | practice 15 |
| 8. Write the board memo | `pyramid-storyline-builder`, `board-memo-writer`, `hostile-qa-rehearsal` |

Hand-offs the author names explicitly: the Issue Tree Builder feeds the Hypothesis-Driven
Workplan, the Spend Cube Builder feeds the Savings Validator, and the Frontline Observation
Protocol feeds every process skill after it.

## Shared rules (apply on top of every skill in this plugin)

1. **Real inputs first.** Every skill lists the inputs to ask for. Ask for them before starting.
   When one is missing, proceed only with figures labeled as estimates, and never invent a
   number that should come from Matt's documents.
2. **One skill at a time.** In a practice or full-engagement run, finish and save one
   deliverable before loading the next, and read the earlier outputs as inputs.
3. **Where outputs go.** Deliverables go to the session's project folder under
   `C:\Users\mattc\OneDrive\Documents\Claude\Projects\<Project Name>\`, flat, never into
   the `claude-cowork-config` repo. Name files `NNN-<skill-name>.md` (or the format the
   deliverable needs) so the run order is visible.
4. **What stays with Matt.** Every skill ends with a "Notes from the source article" section
   naming the decision the user still owns. State it in one line when handing back.
5. **Treat output as an analyst's first draft.** Point out the weakest assumption in the
   deliverable instead of presenting it as final.
6. **Not a licensed opinion.** Legal, tax, audit and regulatory conclusions are flagged for
   the relevant professional; the skills size and structure, they do not sign off.

## Index

### 01. Problem Framing & Issue Trees (McKinsey lane, 001 to 010)

| # | Skill | Replaces |
|---|---|---|
| 001 | `key-question-sharpener` | Week one of a strategy engagement |
| 002 | `issue-tree-builder` | The team-room whiteboard session where the engagement manager and associates argue for two days over how to break the key question into the tree that organizes the whole project |
| 003 | `mece-auditor` | The engagement manager’s red pen on every tree and slide structure, checking for overlaps and gaps against MECE, the principle associated with Barbara Minto’s work at McKinsey |
| 004 | `hypothesis-workplan` | The workplan the engagement manager builds in week one |
| 005 | `fact-base-builder` | The first two weeks of data gathering |
| 006 | `expert-interview-guide` | The interview guides a project team writes before talking to frontline staff, managers, customers, and outside industry experts, each one built to test specific hypotheses instead of collecting opinions |
| 007 | `interview-synthesizer` | The late-night team session after a round of 20 interviews, where associates sort sticky notes into themes and try to tell the partner what the interviews actually proved |
| 008 | `assumption-red-team` | The partner’s challenge session before a recommendation goes to the client |
| 009 | `analysis-prioritizer` | The mid-project reset where the engagement manager asks what each of 40 planned analyses would change and cuts to the eight that decide the answer |
| 010 | `day-one-answer` | The partner’s habit of writing the answer on day one as a storyline of testable claims, so every later analysis either proves it or changes it |

### 02. Market & Competitive Intelligence (McKinsey lane, 011 to 020)

| # | Skill | Replaces |
|---|---|---|
| 011 | `market-sizing-triangulator` | The first two weeks of a market entry study |
| 012 | `industry-value-chain-mapper` | The industry primer chapter of a strategy study, where a team spends a week on expert calls drawing every step from raw input to end customer and tracing where the money changes hands |
| 013 | `five-forces-industry-read` | The industry attractiveness module of a strategy review |
| 014 | `profit-pool-mapper` | The profit pool exhibit that anchors a strategy deck |
| 015 | `competitor-filing-teardown` | The competitor profile workstream |
| 016 | `peer-benchmark-set-builder` | The benchmarking workstream |
| 017 | `market-share-bridge` | The question every quarterly business review eventually asks |
| 018 | `entrant-substitute-scan` | The “emerging threats” section of a strategy review, where a team compiles a long list of startups and adjacent players from news and funding databases, then struggles to say which could matter within three years |
| 019 | `trend-implication-translator` | The megatrends pre-read for a leadership offsite, where a team condenses forty articles and reports into a page that finally says what any of it means for this company’s P&L |
| 020 | `two-uncertainty-scenario-builder` | A scenario planning workshop |

### 03. Growth & Customer Strategy (McKinsey lane, 021 to 030)

| # | Skill | Replaces |
|---|---|---|
| 021 | `customer-segmentation-builder` | The first weeks of a growth program |
| 022 | `needs-based-persona-synthesizer` | The synthesis week after twenty customer interviews, when a team codes every transcript on sticky notes and argues its way to four personas |
| 023 | `jobs-to-be-done-mapper` | An outcome-mapping workshop |
| 024 | `adjacency-screen` | The growth-options phase |
| 025 | `where-to-play-how-to-win-cascade` | The strategy-choice workshops that narrow a list of options to one integrated set of choices, then test what would have to be true |
| 026 | `churn-driver-analysis` | A retention diagnostic |
| 027 | `share-of-wallet-gap-finder` | Account-potential work |
| 028 | `go-to-market-channel-designer` | A channel strategy study |
| 029 | `new-offer-business-case` | The business-case phase for a new offer |
| 030 | `three-horizons-growth-portfolio` | The growth-portfolio review |

### 04. Pricing & Commercial Excellence (McKinsey lane, 031 to 040)

| # | Skill | Replaces |
|---|---|---|
| 031 | `price-waterfall-leakage` | The first month of a pricing engagement |
| 032 | `value-based-price-setter` | The value workstream |
| 033 | `wtp-study-designer` | The research design phase |
| 034 | `packaging-tiering-architect` | The offer-architecture workstream |
| 035 | `discount-governance-designer` | The governance workstream |
| 036 | `deal-desk-reviewer` | The deal desk analyst who checks a large or non-standard deal’s economics and terms before signature |
| 037 | `price-increase-playbook` | The price-increase program |
| 038 | `sales-coverage-territory-designer` | The sales-effectiveness workstream |
| 039 | `pipeline-health-review` | The commercial diagnostic |
| 040 | `key-account-plan-builder` | The key-account program |

### 05. Board & Executive Communication (McKinsey lane, 041 to 050)

| # | Skill | Replaces |
|---|---|---|
| 041 | `pyramid-storyline-builder` | The storyline session near the end of an engagement, where the engagement manager stands at a whiteboard and forces a pile of analysis into one governing thought and three supporting arguments |
| 042 | `action-title-rewriter` | The associate’s late-night pass through a 40-page deck, turning “Q3 Revenue by Region” into sentences that say what each chart proves, followed by the manager’s red pen doing it all again |
| 043 | `ghost-deck-drafter` | Day three of an engagement, when the team sketches the final deck on blank pages before any analysis exists, each page carrying a hypothesis headline and a hand-drawn chart, then walks the sponsor through it to agree on the shape of the answer |
| 044 | `board-memo-writer` | The board pre-read a strategy team drafts with the CFO and general counsel over several rounds, trying to get a real decision onto four pages the directors will actually read |
| 045 | `exec-summary-pressure-test` | The partner review the night before a client meeting, where someone who has not seen the work reads the executive summary cold and finds every place it breaks |
| 046 | `hostile-qa-rehearsal` | The murder board before a major board or investor session, where the team plays the toughest directors and drills the executive until every answer is short, true, and backed by a number |
| 047 | `stakeholder-alignment-map` | The engagement manager’s private stakeholder grid and the calendar of one-on-one “pre-wiring” conversations that makes sure nobody in the final meeting hears the recommendation for the first time |
| 048 | `steerco-readout-builder` | The weekly or monthly steering committee pack a program team assembles from workstream updates, where too much effort goes into making every workstream look green |
| 049 | `decision-memo-builder` | The options paper an engagement team writes when leadership is split |
| 050 | `change-narrative-writer` | The change-story workshop where the leadership team argues out why the company is changing, and the communications team then cascades it into town-hall remarks, manager talking points, and an FAQ |

### 06. Finance & FP&A Transformation (Deloitte lane, 051 to 060)

| # | Skill | Replaces |
|---|---|---|
| 051 | `driver-based-forecast-designer` | Phase one of an FP&A redesign |
| 052 | `variance-bridge-builder` | The monthly scramble where FP&A analysts pull actuals against budget, chase business leads for explanations, and turn the answers into a waterfall and commentary for the executive pack |
| 053 | `close-process-diagnostic` | A close diagnostic |
| 054 | `rolling-forecast-redesigner` | A planning-process redesign |
| 055 | `kpi-tree-architect` | The metric architecture work in a performance-management project |
| 056 | `working-capital-diagnostic` | A working capital diagnostic |
| 057 | `management-reporting-rationalizer` | A reporting rationalization |
| 058 | `thirteen-week-cash-forecaster` | The 13-week cash model restructuring advisors build in week one of a liquidity crunch and update weekly |
| 059 | `finance-operating-model-designer` | The finance operating model phase of a transformation |
| 060 | `business-partnering-review` | A business partnering assessment |

### 07. Cost & Margin Diagnostics (Deloitte lane, 061 to 070)

| # | Skill | Replaces |
|---|---|---|
| 061 | `spend-cube-builder` | Week one of a cost program |
| 062 | `sga-benchmark-read` | The benchmarking workstream that lines up SG&A by function against peers and turns the gaps into a savings range |
| 063 | `margin-bridge-pvm` | The analyst who spends a week splitting a gross margin change into price, volume, mix, and cost for the CFO’s deck |
| 064 | `cost-to-serve-analyzer` | A customer profitability study |
| 065 | `sku-profitability-screen` | The complexity workstream that loads each SKU with hidden costs and brings a delist list to a product committee |
| 066 | `process-cost-calculator` | An activity-based costing study |
| 067 | `zero-based-budget-review` | A zero-based budgeting wave |
| 068 | `demand-lever-finder` | The demand-management workstream |
| 069 | `indirect-spend-quick-wins` | The first 90 days of an indirect procurement program, banking savings before any sourcing event runs |
| 070 | `cost-savings-validator` | The finance validation step when the PMO reports a big number and the CFO asks how much is in the P&L |

### 08. Risk, Controls & Compliance (Deloitte lane, 071 to 080)

| # | Skill | Replaces |
|---|---|---|
| 071 | `enterprise-risk-register` | The ERM refresh |
| 072 | `risk-control-matrix` | The documentation phase of a SOX program |
| 073 | `controls-walkthrough-narrative` | The walkthrough meetings where a consultant follows one transaction end to end with process owners and writes the narrative the auditors will read |
| 074 | `policy-regulation-gap` | The regulatory gap assessment |
| 075 | `third-party-risk-assessor` | The vendor risk program team that tiers suppliers, sends questionnaires, reads SOC reports, and writes a risk rating for each vendor |
| 076 | `audit-finding-remediation` | The remediation workstream after a bad audit |
| 077 | `ai-use-case-governance` | The AI governance assessment |
| 078 | `privacy-impact-assessment` | The privacy assessment run before a new system or data use goes live |
| 079 | `contract-risk-reviewer` | The first-pass review of each third-party agreement against the company’s negotiating playbook |
| 080 | `business-continuity-plan` | The continuity program |

### 09. M&A Diligence & Integration (Deloitte lane, 081 to 090)

| # | Skill | Replaces |
|---|---|---|
| 081 | `acquisition-target-screen` | The long-list to short-list exercise |
| 082 | `commercial-due-diligence` | The commercial diligence workstream |
| 083 | `qoe-red-flag-screen` | The first pass a financial diligence team makes through the seller’s adjusted EBITDA, monthly financials, and working capital before the formal quality of earnings report comes back |
| 084 | `deal-value-sizer` | The combination-benefits model a deal team builds during diligence to defend the purchase price |
| 085 | `imo-designer` | Standing up the integration management office between signing and close |
| 086 | `day-one-readiness-check` | The Day 1 checklist and readiness assessment, where every workstream certifies that on the first day of combined ownership people get paid, customers get served, and legal requirements are met |
| 087 | `hundred-day-plan` | The 100-day integration plan leadership presents after close |
| 088 | `culture-diligence-assessment` | The culture workstream of diligence |
| 089 | `tsa-planner` | The transition services agreement workstream in a carve-out |
| 090 | `carve-out-separation-plan` | The separation workstream in a sale or spin-off |

### 10. Workforce & Org Design (Deloitte lane, 091 to 100)

| # | Skill | Replaces |
|---|---|---|
| 091 | `org-design-options-builder` | The design phase of a restructuring, when a team turns strategy into design criteria, sketches three or four structures, and scores them with the executive team in a workshop |
| 092 | `spans-and-layers-analyzer` | A delayering diagnostic, when analysts rebuild the reporting tree from the HRIS, count managers and layers, and flag every narrow span |
| 093 | `decision-rights-mapper` | The decision-rights workstream of a reorg, when a team interviews leaders about who really decides, finds the collisions, and writes a RACI or RAPID chart everyone signs |
| 094 | `job-architecture-builder` | A job architecture project, when consultants collapse hundreds of inconsistent titles into families and levels with leveling criteria, then map every employee |
| 095 | `strategic-workforce-planner` | A workforce planning engagement, when a team projects talent supply against demand driven by the business plan and recommends build, buy, or borrow moves for the critical roles |
| 096 | `skills-gap-ai-exposure-map` | A future-of-work assessment, when a team breaks roles into tasks, rates which tasks AI changes, and maps the skills each role will need next |
| 097 | `change-impact-assessment` | The impact assessment that precedes a change plan, when consultants grid every stakeholder group against what changes for them and rate the severity |
| 098 | `change-management-plan` | The change workstream in a transformation, when a team builds the sponsor plan, training, resistance management, and adoption metrics around a go-live |
| 099 | `employee-survey-analyzer` | The survey readout, when analysts run key driver analysis, cut results by every demographic, code thousands of comments, and build the heat map for the leadership offsite |
| 100 | `incentive-alignment-review` | A rewards review, when consultants test whether the bonus and commission plans actually pay for the behavior the strategy needs and model what the plans cost |

### 11. Operations & Process Redesign (Accenture lane, 101 to 110)

| # | Skill | Replaces |
|---|---|---|
| 101 | `frontline-observation-protocol` | The discovery weeks of an operations engagement, when consultants sit beside frontline staff with stopwatches to learn how the work really gets done |
| 102 | `as-is-process-mapper` | The current-state mapping workshops, where a facilitator covers a conference room wall in sticky notes and the team spends days reconciling what managers say happens with what staff say happens |
| 103 | `value-stream-waste-mapper` | The value stream mapping exercise, where a lean team times every step and queue and learns the work spends most of its life waiting |
| 104 | `root-cause-analyzer` | The problem-solving session after a recurring failure |
| 105 | `cycle-time-log-study` | The time study done with system data |
| 106 | `automation-candidate-scorer` | The automation opportunity assessment |
| 107 | `future-state-process-designer` | The future-state design workshops, where a team redraws the process around fewer handoffs, earlier decisions, and clear ownership |
| 108 | `frontline-sop-writer` | The procedure-writing phase after a redesign, where a team turns the new process into standard operating procedures that are often too long to use and written for auditors instead of the person doing the job |
| 109 | `process-capacity-model` | The staffing spreadsheet that answers how many people a process needs, usually built on handle times someone once estimated |
| 110 | `tiered-daily-management` | The operating rhythm a lean team installs at the end of an engagement |

### 12. Supply Chain & Procurement (Accenture lane, 111 to 120)

| # | Skill | Replaces |
|---|---|---|
| 111 | `category-strategy-builder` | The category strategy phase of a sourcing wave |
| 112 | `rfp-builder` | Sourcing analysts drafting the RFP package |
| 113 | `bid-should-cost-analyzer` | The bid analysis after an RFP closes |
| 114 | `supplier-scorecard-designer` | The supplier performance program |
| 115 | `negotiation-prep-brief` | A senior sourcing lead’s preparation before a big renewal |
| 116 | `sop-process-designer` | An S&OP implementation |
| 117 | `inventory-policy-setter` | An inventory optimization study |
| 118 | `network-footprint-analyzer` | A network strategy study |
| 119 | `supplier-resilience-mapper` | A supply risk assessment |
| 120 | `contract-leakage-finder` | A post-sourcing leakage review |

### 13. Technology & AI Transformation (Accenture lane, 121 to 130)

| # | Skill | Replaces |
|---|---|---|
| 121 | `ai-use-case-prioritizer` | The AI discovery phase |
| 122 | `ai-business-case` | The business case that gets an AI program through the investment committee |
| 123 | `current-state-architecture` | The architecture assessment |
| 124 | `build-buy-partner` | The sourcing-options analysis a technology strategy team runs before a major capability investment |
| 125 | `vendor-selection-scorecard` | The software selection project |
| 126 | `requirements-user-stories` | The business analysts who run requirements sessions and turn them into a backlog of user stories with acceptance criteria |
| 127 | `data-readiness-assessment` | The data assessment before an AI program |
| 128 | `app-portfolio-rationalizer` | The portfolio rationalization |
| 129 | `system-cutover-planner` | The cutover workstream |
| 130 | `ai-pilot-to-production` | The scale-up plan that turns a successful AI pilot into a supported, measured part of daily work |

### 14. Customer Operations & Service (Accenture lane, 131 to 140)

| # | Skill | Replaces |
|---|---|---|
| 131 | `contact-driver-analyzer` | The first service diagnostic |
| 132 | `customer-journey-mapper` | Journey-mapping workshops, when a team walks one customer journey stage by stage, captures pain points on the wall, and adds the backstage processes behind each moment |
| 133 | `interaction-qa-scorecard` | A quality program redesign, when consultants rebuild the QA form, weight the criteria, set auto-fail rules, and run calibration sessions until evaluators agree |
| 134 | `self-service-deflection-sizer` | The digital self-service business case, when a team screens every contact reason for self-service fit, estimates realistic adoption, and sizes the savings |
| 135 | `erlang-c-staffing-model` | A workforce management review, when analysts forecast interval volume, run Erlang C to service level, apply shrinkage, and show how many agents each hour needs |
| 136 | `knowledge-base-gap-finder` | A knowledge management audit, when a team matches contact reasons and search logs against the article library to find what is missing, wrong, or stale |
| 137 | `customer-verbatim-analyzer` | The voice-of-customer readout, when analysts code thousands of NPS and CSAT comments, link themes to scores, and tell leadership what is really driving detractors |
| 138 | `service-level-designer` | Service-level design work, when a team sets response and resolution targets by channel, priority, and customer tier, then prices what each target costs to hit |
| 139 | `escalation-playbook-writer` | The escalation design workstream, when a team defines severity levels, triggers, handoffs, and communication cadences, then writes the runbook frontline teams follow |
| 140 | `renewal-risk-review` | An account health program |

### 15. Program Delivery & Value Realization (Accenture lane, 141 to 150)

| # | Skill | Replaces |
|---|---|---|
| 141 | `transformation-roadmap-sequencer` | The roadmap workstream that turns forty approved initiatives into capacity-checked waves on one slide |
| 142 | `initiative-charter-writer` | Mobilization week, when the PMO sends each charter back three times for missing benefits and owners |
| 143 | `critical-path-mapper` | The planner who rebuilds the integrated plan across workstreams every month to find which dependencies actually drive the go-live date |
| 144 | `pmo-operating-rhythm` | PMO setup |
| 145 | `raid-log-builder` | The PMO analyst who reads every status report and meeting note to maintain the risks, assumptions, issues, and dependencies log |
| 146 | `program-status-report-writer` | The Thursday scramble where the PMO chases workstream leads, reconciles updates that contradict each other, and produces a status report that is mostly green |
| 147 | `go-live-readiness-gate` | The go/no-go assessment before a major launch |
| 148 | `benefits-realization-tracker` | The value office that tracks every benefit promised in the business cases, month by month, against a ramp curve, after the project team has moved on |
| 149 | `post-implementation-review` | The lessons-learned exercise run 60 to 90 days after go-live, which usually produces a list nobody reads before the next program |
| 150 | `quarterly-value-review` | The quarterly portfolio review where executives see what the transformation delivered and cost, and what to stop |
