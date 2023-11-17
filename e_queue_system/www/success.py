import frappe
from frappe import _
def get_context(context):
    last_pending_person = frappe.db.get_value("Queue System", {"status": "Pending"}, "full_name", order_by="modified desc")
    context.last_pending_person = last_pending_person
    frappe.publish_realtime('last_pending_person_updated', last_pending_person, user=frappe.session.user)

@frappe.whitelist()
def update_status(doc, method):
    last_pending_person = frappe.db.get_value("Queue System", {"status": "Pending"}, "full_name", order_by="modified desc")
    frappe.publish_realtime('last_pending_person_updated', last_pending_person, user=frappe.session.user)
