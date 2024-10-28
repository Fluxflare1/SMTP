


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
