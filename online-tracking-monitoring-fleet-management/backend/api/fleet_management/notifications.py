






from .models import Trip
from django.utils import timezone
from django.core.mail import send_mail

def notify_driver_of_trip(trip_id):
    trip = Trip.objects.get(id=trip_id)
    # Logic to send email/SMS notification to the driver about the scheduled trip
    send_mail(
        'Trip Scheduled',
        f'You have a trip scheduled from {trip.origin} to {trip.destination}.',
        'noreply@company.com',
        [trip.driver.email],
    )

def send_reminder_for_trip(trip_id):
    trip = Trip.objects.get(id=trip_id)
    send_mail(
        'Upcoming Trip Reminder',
        f'Reminder: You have a trip starting in 15 minutes from {trip.origin}.',
        'noreply@company.com',
        [trip.driver.email],
    )





def send_vehicle_reactivation_notification(vehicle, recipients):
    subject = "Vehicle Re-Activated"
    html_message = render_to_string("notifications/vehicle_reactivation.html", {
        "driver_name": vehicle.assigned_driver.name if vehicle.assigned_driver else "Driver",
        "vehicle_registration_number": vehicle.registration_number,
    })
    plain_message = strip_tags(html_message)
    
    # Log for each recipient
    for recipient in recipients:
        try:
            send_mail(
                subject,
                plain_message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient],
                html_message=html_message,
            )
            NotificationLog.objects.create(
                notification_type="Vehicle Re-Activation",
                recipient=recipient,
                vehicle=vehicle,
                status="sent",
                priority="high"
            )
        except Exception:
            NotificationLog.objects.create(
                notification_type="Vehicle Re-Activation",
                recipient=recipient,
                vehicle=vehicle,
                status="failed",
                priority="high"
            )




from .models import NotificationLog

def send_vehicle_reactivation_notification(vehicle):
    subject = "Vehicle Re-Activated"
    html_message = render_to_string("notifications/vehicle_reactivation.html", {
        "driver_name": vehicle.assigned_driver.name if vehicle.assigned_driver else "Driver",
        "vehicle_registration_number": vehicle.registration_number,
    })
    plain_message = strip_tags(html_message)
    recipient_list = [vehicle.assigned_driver.email] if vehicle.assigned_driver else []

    # Send email notification and log result
    try:
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            html_message=html_message,
        )
        NotificationLog.objects.create(
            notification_type="Vehicle Re-Activation",
            recipient=recipient_list[0],
            vehicle=vehicle,
            status="sent",
        )
    except Exception as e:
        NotificationLog.objects.create(
            notification_type="Vehicle Re-Activation",
            recipient=recipient_list[0] if recipient_list else "N/A",
            vehicle=vehicle,
            status="failed",
        )



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
