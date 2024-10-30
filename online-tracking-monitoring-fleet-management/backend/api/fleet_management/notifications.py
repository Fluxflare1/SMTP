


from django.core.mail import send_mail
from django.conf import settings
from .models import Vehicle

def send_vehicle_reactivation_notification(vehicle):
    subject = "Vehicle Re-Activated"
    message = f"The vehicle '{vehicle.registration_number}' has been successfully re-activated."
    recipient_list = [vehicle.assigned_driver.email] if vehicle.assigned_driver else []

    # Send email notification
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

    # Add additional in-app notification logic here if necessary



from django.core.mail import send_mail

def send_expense_alert(trip):
    message = f"Alert: Trip {trip.id} has exceeded its expense threshold!"
    send_mail(
        subject="Trip Expense Alert",
        message=message,
        from_email="alerts@fluxtrans.com",
        recipient_list=["fleetmanager@fluxtrans.com"],
    )
