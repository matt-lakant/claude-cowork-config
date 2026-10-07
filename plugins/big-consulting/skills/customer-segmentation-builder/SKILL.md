---
name: customer-segmentation-builder
description: Builds a behavioral and value-based customer segmentation from transaction and account data, then sizes and names each segment. Use when the user attaches a customer, order, or revenue export and asks who their customers really are, which customers matter most, or how to segment the base for sales, marketing, or service.
---

# Customer Segmentation Builder

## What this produces
A segmentation of 4 to 7 sized, named segments, with what each implies for coverage, offer, and service.

## Inputs to ask for
- Transaction export (CSV or XLSX), 24+ months: customer ID, date, SKU, revenue, gross margin. If margin is missing, label margin conclusions unavailable.
- Account attributes: industry, size, region, channel, tenure, assigned rep.
- The decision the segmentation must serve (coverage, pricing, service tiering).

## Method
1. Fix the unit of analysis (bill-to account, parent company, or buyer) and roll transactions up to it. Report how many records failed to map.
2. Build one row per customer: recency, frequency, monetary value (RFM), gross margin, number of product lines bought, tenure, trailing 12-month growth, and firmographics.
3. Run concentration: share of revenue and margin held by the top 1%, 10%, and 20% of customers. Flag any customer above 5% of revenue.
4. Try a rule-based cut (value tier x product breadth) first; cluster only if it fails the step 6 tests.
5. If clustering: standardize, cap outliers at the 99th percentile, run k-means for k = 3 to 8, pick k on silhouette score and interpretability.
6. Test each segment: size (at least 5% of customers or revenue), distinctness (differs from the base on 2+ variables), stability (70%+ of customers land in the same segment on prior-year data), identifiability (sales can assign an account from CRM fields).
7. Name segments by behavior ("Broad, high-margin loyalists"), never by a letter.

## Output format
1. Segment table: Segment | Customers | % Revenue | % Margin | Avg Revenue | Growth | Product Lines | Defining Traits.
2. Concentration summary (3 lines).
3. Per segment: 3 bullets on coverage, offer, and service.

## Quality checks
- Segment revenue sums to total revenue within 1%.
- Every segment passes all four tests in step 6, or the failure is stated.
- Every number traces to the input file or is labeled as an assumption.

## Notes from the source article
- **Replaces:** The first weeks of a growth program: analysts roll up every transaction into a customer table and iterate on clusters until a segmentation survives the sales leaders.
- **Example request:** “Here are three years of invoices and our CRM account list. Segment the base so I can decide who gets a dedicated rep and who moves to inside sales.”
- **What the user still owns:** Deciding which segments you will deliberately underserve. The analysis can show you the tail; only you can tell the sales team to stop chasing it.
- When handing the deliverable back, name in one line the decision above that stays with the user.
