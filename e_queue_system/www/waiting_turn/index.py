import frappe
from frappe import _

def get_context(context):
    last_four_people = frappe.db.get_all("Queue System",
        {
            "status": "Pending",
            "desk": ["!=", ""]
        },
        ["full_name", "name","desk","receptionist_name"], order_by="name asc"
    )

    if len(last_four_people) < 4:
        last_four_people += [{"full_name": "", "name": "", "desk": ""}] * (4 - len(last_four_people))

    context.last_person1 = last_four_people[0]['full_name']
    context.queue_number1 = last_four_people[0]['name'].split('-')[-1]
    context.desk1 = last_four_people[0]['desk']
    context.last_person2 = last_four_people[1]['full_name']
    context.queue_number2 = last_four_people[1]['name'].split('-')[-1]
    context.desk2 = last_four_people[1]['desk']
    context.last_person3 = last_four_people[2]['full_name']
    context.queue_number3 = last_four_people[2]['name'].split('-')[-1]
    context.desk3 = last_four_people[2]['desk']
    context.last_person4 = last_four_people[3]['full_name']
    context.queue_number4 = last_four_people[3]['name'].split('-')[-1]
    context.desk4 = last_four_people[3]['desk']

    # Calculate num_cards based on the length of last_four_people
    num_cards = frappe.get_single("Queue System Settings").number_of_cards
    context.num_cards = num_cards

# Now you can use {{ num_cards }} in your Jinja2 template.
