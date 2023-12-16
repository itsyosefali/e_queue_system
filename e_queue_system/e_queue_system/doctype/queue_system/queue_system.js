// Copyright (c) 2023, itsyosefali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Queue System', {
	refresh: function (frm) {
		frm.add_custom_button(__('Assinged To Me'), function () {
			frappe.call({
				method: 'e_queue_system.api.get_assigned_to_me',
				args: {
					user: frappe.session.user,
				},
				callback: function (r) {
					console.log(r.message);
					if (r.message) {
						frm.set_value('desk', r.message[0]);
						frm.set_value('receptionist_name', r.message[1]);
						frm.save();
					}
					else {
						frappe.msgprint('No Desk Assigned to you');
					}
				},
			});
		})
	}
});
