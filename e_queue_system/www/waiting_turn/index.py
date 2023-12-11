import frappe
from frappe import _

def get_context(context):
    last_four_people = frappe.db.get_all("Queue System", {"status": "Pending"}, ["full_name", "name", "desk"], order_by="name asc")

    if not last_four_people:
        last_four_people = [{"full_name": "No one in queue", "name": "No queue number", "desk": "No desk assigned"}] * 4

    context.last_person1 = last_four_people[0]['full_name']
    context.queue_number1 = last_four_people[0]['name'].split('-')[-1]  # keep only the last part
    context.desk1 = last_four_people[0]['desk']

    context.last_person2 = last_four_people[1]['full_name']
    context.queue_number2 = last_four_people[1]['name'].split('-')[-1]  # keep only the last part
    context.desk2 = last_four_people[1]['desk']

    context.last_person3 = last_four_people[2]['full_name']
    context.queue_number3 = last_four_people[2]['name'].split('-')[-1]  # keep only the last part
    context.desk3 = last_four_people[2]['desk']

    context.last_person4 = last_four_people[3]['full_name']
    context.queue_number4 = last_four_people[3]['name'].split('-')[-1]  # keep only the last part
    context.desk4 = last_four_people[3]['desk']