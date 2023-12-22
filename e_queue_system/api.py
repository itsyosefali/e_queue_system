import frappe
@frappe.whitelist()
def get_assigned_to_me(user):
    try:
        queue_settings = frappe.get_single("Queue System Settings")
        for desk in queue_settings.desk_settings:
            if desk.receptionist_name == user:
                return [desk.desk_name,desk.receptionist_name]
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Queue System Assigned Error"
			, "Queue System")
