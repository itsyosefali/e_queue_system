import frappe

def get_context(context):
    
    last_pending_person = frappe.db.get_value("Queue System", {"status": "Pending"}, "full_name", order_by="modified desc")
    context.last_pending_person = last_pending_person
