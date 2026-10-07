---
name: driver-based-forecast-designer
description: Designs a driver-based forecast model by identifying the operational drivers behind each P&L line, testing them against history, and specifying the model logic. Use when a forecast is built by trending last year, when forecast accuracy is poor, or when moving from a line-item budget to a driver model.
---

# Driver-Based Forecast Designer

## What this produces
A driver map for every material P&L line, each driver's historical fit, and a buildable model specification.

## Inputs to ask for
- 24 to 36 months of monthly P&L by line (attach spreadsheet or CSV)
- Operational data for the same months: volumes, headcount, orders, units, locations, customers
- The current forecast method and its accuracy against actuals
If operational data is missing, propose candidate drivers and list exactly which data to request.

## Method
1. Rank P&L lines by size and volatility. Small, stable lines (under 2% of revenue) get a simple trend.
2. For each material line, write one or two drivers as an equation: revenue = customers x orders per customer x average order value; labor = FTE x loaded cost per FTE.
3. Test each driver against history: calculate the implied rate each month and check its stability (coefficient of variation under roughly 10% suggests a usable rate).
4. Classify drivers as business-owned (volume, mix) or finance-owned (rates, inflation, FX). Name the owner for each input.
5. Separate fixed, variable, and step-fixed costs; mark step thresholds (a new shift at 85% capacity, a new hire every 40 accounts).
6. Specify the model: inputs tab, rate assumptions, calculation logic, outputs, and the scenario levers.

## Output format
- Driver map: P&L line | Driver equation | Input owner | Historical rate range | Stability | Fixed/Variable/Step
- Model specification (inputs, calculations, outputs, scenario levers), maximum one page
- Data gaps list

## Quality checks
- Drivers cover at least 80% of total cost and revenue
- Every rate is calculated from history or labeled an assumption
- Step costs have explicit thresholds

## Notes from the source article
- **Replaces:** Phase one of an FP&A redesign: consultants interviewing business leads to find the few operational drivers that move the P&L, then rebuilding the forecast around them.
- **Example request:** “Here’s three years of monthly P&L and our order and headcount data. Design a driver-based forecast so we stop budgeting by adding 4% to last year.”
- **What the user still owns:** Getting business leads to own their volume inputs. A driver model with finance guessing the volumes is last year’s forecast with more tabs.
- When handing the deliverable back, name in one line the decision above that stays with the user.
