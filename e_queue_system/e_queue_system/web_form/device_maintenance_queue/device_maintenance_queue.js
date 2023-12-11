frappe.ready(function () {
	frappe.web_form.handle_success = () => {
		frappe.msgprint(__('Thank You for applying!'));
		window.location = frappe.web_form.success_url;
	}
});