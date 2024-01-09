import frappe
from frappe import _

def get_context(context):
    # Fetch desks from the child table in Queue System Settings
    desks = frappe.get_all("Desk Receptionist", filters={"parent": "Queue System Settings"}, pluck="desk_name")

    queue_data = []

    for desk in desks:
        desk_data = frappe.db.get_all("Queue System",
            {
                "status": "Pending",
                "desk": desk
            },
            ["full_name", "name", "desk", "receptionist_name"], order_by="name asc"
        )

        queue_data.append({
            "desk_name": desk,
            "queue": desk_data
        })

    context.queue_data = queue_data
