from django.core.mail import send_mail

def send_expense_alert(trip):
    message = f"Alert: Trip {trip.id} has exceeded its expense threshold!"
    send_mail(
        subject="Trip Expense Alert",
        message=message,
        from_email="alerts@fluxtrans.com",
        recipient_list=["fleetmanager@fluxtrans.com"],
    )
