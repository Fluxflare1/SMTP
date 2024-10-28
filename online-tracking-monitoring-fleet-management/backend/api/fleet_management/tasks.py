



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
