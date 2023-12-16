# Copyright (c) 2023, itsyosefali and contributors
# For license information, please see license.txt

# import frappe
import re
import frappe
from frappe.model.document import Document

class QueueSystemSettings(Document):
	def validate(self):
		try:
			self.check_number_of_desk()
		except Exception as e:
			frappe.log_error(frappe.get_traceback(), "Queue System Settings Validation Error"
			, "Queue System Settings")
	def check_number_of_desk(self):
		if len(self.desk_settings) > self.number_of_desks:
			frappe.throw("Number of desks should be greater than or equal to number of desk settings")