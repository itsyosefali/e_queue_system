frappe.ui.form.on('Queue System Settings', {
	validate: function (frm) {
		var receptionistDeskCount = {};
		$.each(frm.doc.desk_settings || [], function (i, row) {
			var receptionist = row.receptionist_name;
			if (receptionist) {
				if (receptionist in receptionistDeskCount) {
					receptionistDeskCount[receptionist].push(row);
				} else {
					receptionistDeskCount[receptionist] = [row];
				}
			}
		});
		$.each(receptionistDeskCount, function (receptionist, desks) {
			if (desks.length > 1) {
				$.each(desks.slice(1), function (i, desk) {
					frm.fields_dict['desk_settings'].grid.grid_rows[desk.idx - 1].remove();
				});
				frappe.throw(__("Receptionist {0} is assigned to more than one desk. Removing duplicates.", [receptionist]));
			}
		});
	}
});
