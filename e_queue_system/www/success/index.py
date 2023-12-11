from numpy import full
import frappe
from frappe import _
def get_context(context):
    queue_number = frappe.db.get_value("Queue System", {"status": "Pending"}, "name", order_by="modified desc")
    full_name = frappe.db.get_value("Queue System", {"status": "Pending"}, "full_name", order_by="modified desc")
    context.full_name = full_name
    context.queue_number = queue_number[-1:]