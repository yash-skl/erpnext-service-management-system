import frappe
from frappe.utils import time_diff_in_hours


def on_submit(doc, method=None):

    # Calculate visit duration
    if doc.start_time and doc.end_time:
        duration = time_diff_in_hours(
            doc.end_time,
            doc.start_time
        )

        frappe.db.set_value(
            "Service Visit",
            doc.name,
            "duration",
            duration
        )

    # Update service ticket status
    if doc.service_ticket:
        frappe.db.set_value(
            "Service Ticket",
            doc.service_ticket,
            "status",
            "Resolved"
        )

        ticket = frappe.get_doc(
            "Service Ticket",
            doc.service_ticket
        )

        ticket.add_comment(
            "Comment",
            f"Service Visit {doc.name} completed."
        )
