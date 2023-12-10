frappe.ready(function () {
	// frappe.msgprint('Please fill all values carefully');
})
frappe.web_form.handle_success = () => {
	frappe.msgprint(__('Thank You for applying!'));
	window.location = frappe.web_form.app;
}