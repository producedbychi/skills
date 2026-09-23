# Invoices

Read [paperwork mode](paperwork.md) first for the terms ledger and authorization limits. Create an invoice for an agreed billing event or when the user explicitly requests a draft. An invoice is not a substitute for an estimate or approval of new work.

## Required inputs and output

Use issuer and client details, a unique invoice number from the user's numbering system, issue and due dates, project and agreement or purchase-order reference when required, the billing event or service period, approved line items, quantities and rates, approved expenses or changes, currency, subtotal, verified tax treatment if applicable, total, payment instructions, and payment terms. Mark missing fields `unresolved`. Do not invent a tax rate, late fee, bank account, payment link, purchase-order number, or invoice number.

Calculate each line as quantity times rate with decimal-safe arithmetic. Reconcile subtotals, applicable verified tax, approved credits, prior payments, and balance due. Keep currency consistent. If tax treatment is unknown, show it as unresolved rather than silently applying zero tax. Do not bill an optional or unapproved change. If the invoice is for a deposit or milestone, name that milestone and avoid implying that the full project has already been delivered.

Compare the invoice with the signed scope, payment schedule, earlier invoices, payment records, and approved changes when those records are available. Check for duplicate billing of a milestone or expense. If they are missing, label the result `draft pending reconciliation` and identify what must be checked before sending. Do not claim a balance is final when payment history is unknown.

## Check before delivery

- Every charge points to agreed scope, a payment milestone, an approved expense, or an approved change.
- Line arithmetic, subtotal, tax or credit treatment, and balance agree.
- The billed event and amount agree with the contract or approved billing instruction, and no prior invoice duplicates them.
- Invoice number, due date, payee details, and payment instructions came from the user or approved records.
- The draft is clearly distinguished from a sent invoice.
