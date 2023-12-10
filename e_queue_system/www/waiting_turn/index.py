import queue
import frappe
from frappe import _
def get_context(context):
    last_pending_person = frappe.db.get_value("Queue System", {"status": "Pending"}, "full_name", order_by="modified desc")
    queue_number = frappe.db.get_value("Queue System", {"status": "Pending"}, "name", order_by="modified desc")
    desk = frappe.db.get_value("Queue System", {"status": "Pending"}, "desk", order_by="modified desc")
    if not queue_number:
        queue_number = "No queue number"
    if not desk:
        desk = "No desk assigned"
    if not last_pending_person:
        last_pending_person = "No one in queue"
    context.desk = desk
    context.last_pending_person = last_pending_person
    context.queue_number = queue_number[-1:]
