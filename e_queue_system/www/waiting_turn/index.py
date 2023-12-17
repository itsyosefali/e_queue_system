import frappe
from frappe import _

def get_context(context):
    last_four_people = frappe.db.get_all("Queue System",
        {
            "status": "Pending",
            "desk": ["!=", ""]
        },
        ["full_name", "name", "desk", "receptionist_name"], order_by="name asc"
    )

    context.last_four_people = last_four_people

    num_cards = frappe.get_single("Queue System Settings").number_of_cards
    context.num_cards = num_cards
