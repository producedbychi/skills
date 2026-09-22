# Billing

Use approved project rates and payment terms. Never invent a tax rate, late fee, bank account, payment link, invoice number, or purchase-order number.

An invoice needs the issuer and client details, unique invoice number, issue and due dates, project reference, line items with quantities and rates, approved expenses or change orders, currency, subtotal, any verified tax treatment, total, payment instructions, and the applicable payment terms. Omit an unavailable optional field or mark it unresolved rather than filling it with plausible data.

Calculate line totals, subtotal, tax, credits, and balance with decimal-safe arithmetic. Compare the amount billed with the signed scope, payment schedule, previous invoices, and approved changes when those records are available. If they are not, label the invoice a draft pending reconciliation. Do not submit an invoice or trigger payment collection without the user's explicit instruction.
