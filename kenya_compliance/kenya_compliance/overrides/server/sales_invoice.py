from frappe.model.document import Document

from .shared_overrides import generic_invoices_on_submit_override


def on_submit(doc: Document, method: str) -> None:
    """Intercepts submit event for document"""

    if not doc.is_pos:
        generic_invoices_on_submit_override(doc, "Sales Invoice")
