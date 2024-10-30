



from celery import shared_task
from .notifications import send_reminder_for_trip
from .models import Trip
from django.utils import timezone
from datetime import timedelta

@shared_task
def schedule_trip_notifications():
    now = timezone.now()
    upcoming_trips = Trip.objects.filter(start_time__gte=now, start_time__lte=now + timedelta(minutes=15))
    for trip in upcoming_trips:
        send_reminder_for_trip(trip.id)





from celery import shared_task
from django.core.mail import send_mail
from django.utils.html import strip_tags
from .models import NotificationLog, Vehicle
from django.template.loader import render_to_string

@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def retry_failed_notifications(self, log_id):
    log_entry = NotificationLog.objects.get(id=log_id)
    vehicle = log_entry.vehicle

    html_message = render_to_string("notifications/vehicle_reactivation.html", {
        "driver_name": vehicle.assigned_driver.name if vehicle.assigned_driver else "Driver",
        "vehicle_registration_number": vehicle.registration_number,
    })
    plain_message = strip_tags(html_message)
    recipient = log_entry.recipient

    try:
        send_mail(
            "Vehicle Re-Activated",
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            html_message=html_message,
        )
        log_entry.status = "sent"
    except Exception as exc:
        log_entry.status = "failed"
        self.retry(exc=exc)
    
    log_entry.save()



from celery import shared_task
from .models import DriverProfile
from django.utils import timezone
from .notifications import send_license_expiration_notification

@shared_task
def notify_expiring_licenses():
    drivers = DriverProfile.objects.filter(license_expiration_date__lt=timezone.now().date() + timezone.timedelta(days=30))
    for driver in drivers:
        send_license_expiration_notification(driver)



from celery import shared_task
from .models import Invoice

@shared_task
def check_overdue_invoices():
    invoices = Invoice.objects.filter(status="pending", due_date__lt=timezone.now().date())
    for invoice in invoices:
        invoice.check_overdue_status()




from celery import shared_task
from .models import Invoice

@shared_task
def generate_recurring_invoices():
    invoices = Invoice.objects.filter(is_recurring=True, next_recurrence_date__lte=timezone.now())
    for invoice in invoices:
        # Logic to clone the invoice and set the next recurrence date
        invoice.schedule_next_recurrence()
        invoice.save()





from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import DriverCredential
from .utils import send_email_reminder  # Utility for sending email notifications

@shared_task
def check_driver_credentials_expiration():
    upcoming_expiration_date = timezone.now() + timedelta(days=30)
    expiring_credentials = DriverCredential.objects.filter(
        expiration_date__lte=upcoming_expiration_date,
        is_active=True
    )
    for credential in expiring_credentials:
        send_email_reminder(credential)






from celery import shared_task
from .models import Trip
from .notifications import send_expense_alert

@shared_task
def check_trip_expenses():
    trips = Trip.objects.filter(total_expense__gt=F('expense_threshold'))
    for trip in trips:
        send_expense_alert(trip)



from .models import DriverDocumentation
from notifications.models import Notification
from django.utils import timezone
from datetime import timedelta

def check_document_expirations():
    expiring_soon_docs = DriverDocumentation.objects.filter(
        expiration_date__lte=timezone.now().date() + timedelta(days=30)
    )
    for doc in expiring_soon_docs:
        message = f"Alert: {doc.document_type} for driver {doc.driver.username} is expiring on {doc.expiration_date}."
        
        # Notify fleet managers
        fleet_managers = User.objects.filter(role='fleet_manager')
        for manager in fleet_managers:
            Notification.objects.create(
                user=manager,
                message=message
            )



from .models import FuelUsage
from notifications.models import Notification
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

def fuel_usage_alert():
    vehicles = Vehicle.objects.all()
    for vehicle in vehicles:
        recent_fuel_data = FuelUsage.objects.filter(vehicle=vehicle, timestamp__gte=timezone.now() - timedelta(hours=1)).order_by('timestamp')
        
        if recent_fuel_data.count() > 1:
            # Calculate fuel consumption
            first = recent_fuel_data.first().fuel_level
            last = recent_fuel_data.last().fuel_level
            fuel_drop = first - last
            
            # Define thresholds
            excessive_drop_threshold = 5.0  # Customize this value as needed
            
            if fuel_drop > excessive_drop_threshold:
                message = f"Alert: Vehicle {vehicle.license_plate} shows an unusual fuel drop of {fuel_drop} liters within the last hour."
                
                # Send alert to fleet managers
                fleet_managers = User.objects.filter(role='fleet_manager')
                for manager in fleet_managers:
                    Notification.objects.create(
                        user=manager,
                        message=message
                    )



from .models import DriverBehaviorEvent
from notifications.models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

def driver_behavior_alert():
    unsafe_events = DriverBehaviorEvent.objects.filter(timestamp__gte=timezone.now() - timedelta(minutes=5))
    
    for event in unsafe_events:
        if event.event_type == "Speeding":
            message = f"Alert: Vehicle {event.vehicle.license_plate} driven by {event.driver.name} exceeded the speed limit."
        elif event.event_type == "Harsh Braking":
            message = f"Alert: Vehicle {event.vehicle.license_plate} experienced harsh braking."
        # Add additional behavior alerts as needed
        
        fleet_managers = User.objects.filter(role='fleet_manager')
        for manager in fleet_managers:
            Notification.objects.create(
                user=manager,
                message=message
            )




from geopy.distance import geodesic
from .models import Geofence, VehicleLocation
from notifications.models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

def geofence_alert():
    geofences = Geofence.objects.all()
    recent_vehicle_locations = VehicleLocation.objects.order_by('-timestamp')[:100]  # Limit to recent locations
    
    for location in recent_vehicle_locations:
        for geofence in geofences:
            vehicle_position = (location.latitude, location.longitude)
            geofence_position = (geofence.latitude, geofence.longitude)
            distance = geodesic(vehicle_position, geofence_position).meters
            
            if distance <= geofence.radius:
                message = f"Vehicle {location.vehicle.license_plate} has entered the geofence area '{geofence.name}'."
            else:
                message = f"Vehicle {location.vehicle.license_plate} has exited the geofence area '{geofence.name}'."
                
            fleet_managers = User.objects.filter(role='fleet_manager')
            for manager in fleet_managers:
                Notification.objects.create(
                    user=manager,
                    message=message
                )






from .models import Vehicle, VehicleHealthMetrics
from notifications.models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

def vehicle_health_alert():
    # Retrieve vehicles with critical health metrics
    critical_health_vehicles = VehicleHealthMetrics.objects.filter(
        engine_temperature__gt=95,  # Example threshold for high engine temperature
        battery_level__lt=20  # Example threshold for low battery
    )
    
    for health_metrics in critical_health_vehicles:
        vehicle = health_metrics.vehicle
        fleet_managers = User.objects.filter(role='fleet_manager')

        for manager in fleet_managers:
            Notification.objects.create(
                user=manager,
                message=f"Critical health alert for Vehicle {vehicle.license_plate}: Engine Temp {health_metrics.engine_temperature}°C, Battery {health_metrics.battery_level}%."
            )




from django.utils import timezone
from .models import MaintenanceTask
from notifications.models import Notification  # Assuming there's a central Notification model
from django.contrib.auth import get_user_model

User = get_user_model()

def overdue_maintenance_alert():
    # Retrieve overdue maintenance tasks
    overdue_tasks = MaintenanceTask.objects.filter(date_scheduled__lt=timezone.now(), status='Pending')
    
    for task in overdue_tasks:
        vehicle = task.vehicle
        fleet_manager = User.objects.filter(role='fleet_manager')  # Assuming fleet managers have this role

        for manager in fleet_manager:
            Notification.objects.create(
                user=manager,
                message=f"Overdue maintenance for Vehicle {vehicle.license_plate} was scheduled on {task.date_scheduled} and is pending."
            )



from datetime import timedelta
from django.utils import timezone
from .models import Vehicle, MaintenanceTask
from notifications.models import Notification  # Assuming there's a central Notification model
from django.contrib.auth import get_user_model

User = get_user_model()

def upcoming_maintenance_alert():
    # Define the alert timeframe
    alert_date = timezone.now() + timedelta(days=7)
    
    # Retrieve tasks scheduled within the next 7 days
    tasks_due = MaintenanceTask.objects.filter(date_scheduled__lte=alert_date, status='Pending')
    
    for task in tasks_due:
        vehicle = task.vehicle
        fleet_manager = User.objects.filter(role='fleet_manager')  # Assuming fleet managers are assigned this role

        for manager in fleet_manager:
            Notification.objects.create(
                user=manager,
                message=f"Upcoming maintenance for Vehicle {vehicle.license_plate} scheduled on {task.date_scheduled}."
            )





from celery import shared_task
from django.utils import timezone
from .models import MaintenanceRecord

@shared_task
def send_maintenance_alerts():
    today = timezone.now().date()
    upcoming_maintenance = MaintenanceRecord.objects.filter(
        date_scheduled__lte=today + timezone.timedelta(days=7), 
        is_completed=False
    )
    overdue_maintenance = MaintenanceRecord.objects.filter(
        date_scheduled__lt=today, 
        is_completed=False
    )

    for record in upcoming_maintenance:
        # Send alert for upcoming maintenance
        # Example function: send_alert(record, "Upcoming maintenance")

    for record in overdue_maintenance:
        # Send alert for overdue maintenance
        # Example function: send_alert(record, "Overdue maintenance")
