# Invoices

Read [paperwork mode](paperwork.md) first for the terms ledger and authorization limits. Create an invoice for an agreed billing event or when the user explicitly requests a draft. An invoice is not a substitute for an estimate or approval of new work.

## Required inputs and output

Use issuer and client details, a unique invoice number, issue and due dates, project reference, approved line items, quantities and rates, approved expenses or changes, currency, subtotal, verified tax treatment if applicable, total, payment instructions, and payment terms. Include a purchase-order reference when required and supplied. Mark missing fields `unresolved`. Do not invent a tax rate, late fee, bank account, payment link, purchase-order number, or invoice number.

Calculate each line as quantity times rate with decimal-safe arithmetic. Reconcile subtotals, applicable verified tax, approved credits, prior payments, and balance due. Keep currency consistent. If tax treatment is unknown, show it as unresolved rather than silently applying zero tax. Do not bill an optional or unapproved change.

Compare the invoice with the signed scope, payment schedule, earlier invoices, and approved changes when those records are available. If they are missing, label the result `draft pending reconciliation` and identify what must be checked before sending. Do not claim a balance is final when payment history is unknown.

## Check before delivery

- Every charge points to agreed scope, a payment milestone, an approved expense, or an approved change.
- Line arithmetic, subtotal, tax or credit treatment, and balance agree.
- Invoice number, due date, payee details, and payment instructions came from the user or approved records.
- The draft is clearly distinguished from a sent invoice.
