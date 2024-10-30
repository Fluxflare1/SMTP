




from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging
from .models import Vehicle

# Set up logging
logger = logging.getLogger(__name__)

def send_vehicle_reactivation_notification(vehicle):
    subject = "Vehicle Re-Activated"
    html_message = render_to_string("notifications/vehicle_reactivation.html", {
        "driver_name": vehicle.assigned_driver.name if vehicle.assigned_driver else "Driver",
        "vehicle_registration_number": vehicle.registration_number,
    })
    plain_message = strip_tags(html_message)
    recipient_list = [vehicle.assigned_driver.email] if vehicle.assigned_driver else []

    # Send email notification
    try:
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            html_message=html_message,
        )
        logger.info(f"Re-activation notification sent to {recipient_list} for vehicle {vehicle.registration_number}")
    except Exception as e:
        logger.error(f"Failed to send re-activation notification for vehicle {vehicle.registration_number}: {str(e)}")





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
