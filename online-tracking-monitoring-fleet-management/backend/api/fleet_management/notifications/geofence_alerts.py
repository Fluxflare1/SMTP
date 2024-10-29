from .models import VehicleLocation, Geofence, Notification
from django.utils import timezone

def check_geofence(vehicle_id):
    vehicle_location = VehicleLocation.objects.filter(vehicle_id=vehicle_id).last()
    active_geofences = Geofence.objects.filter(is_active=True)

    for geofence in active_geofences:
        if is_within_geofence(vehicle_location, geofence.coordinates):
            Notification.objects.create(
                vehicle_id=vehicle_id,
                message=f"Vehicle {vehicle_id} entered geofence {geofence.name}",
                created_at=timezone.now(),
            )
