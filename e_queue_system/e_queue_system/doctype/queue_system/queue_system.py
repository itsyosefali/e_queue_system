# Copyright (c) 2023, itsyosefali and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class QueueSystem(Document):
	def validate(self):
		# set full name for contact
		if self.first_name and self.last_name:
			self.full_name = self.first_name + " " + self.last_name
