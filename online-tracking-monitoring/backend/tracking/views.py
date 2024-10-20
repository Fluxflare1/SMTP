





from geopy.distance import geodesic
from tracking.models import Vehicle

def calculate_distance_traveled(vehicle_id):
    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    distance = geodesic((vehicle.start_latitude, vehicle.start_longitude), (vehicle.latitude, vehicle.longitude)).km
    vehicle.total_distance += distance
    vehicle.save()
    return vehicle.total_distance






from django.utils.timezone import now
from tracking.models import Vehicle

def update_idle_time(vehicle_id):
    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    if vehicle.status == 'idle':
        idle_duration = now() - vehicle.last_active  # Assuming `last_active` stores the last active timestamp
        vehicle.idle_time += idle_duration.total_seconds()  # Add to total idle time
        vehicle.last_active = now()  # Reset last active time
        vehicle.save()





from django.http import JsonResponse
from tracking.models import Vehicle  # Assuming there is a Vehicle model to store vehicle info

def get_all_vehicles_location(request):
    vehicles = Vehicle.objects.filter(is_active=True)  # Get all active vehicles
    vehicle_data = [
        {
            'vehicle_id': vehicle.vehicle_id,
            'latitude': vehicle.latitude,
            'longitude': vehicle.longitude,
            'status': vehicle.status,  # idle, active, etc.
        }
        for vehicle in vehicles
    ]
    return JsonResponse({'vehicles': vehicle_data})






CORNERING_THRESHOLD = 30  # Threshold for harsh cornering in degrees
DISTRACTED_DRIVING_THRESHOLD = 15  # Threshold for sudden phone usage or distractions




from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def trigger_geofence_alert(vehicle_id, geofence_name, status):
    # Send WebSocket notifications
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'geofence_alerts',
        {
            'type': 'send_geofence_alert',
            'message': f"Vehicle {vehicle_id} has {status} the geofence: {geofence_name}"
        }
    )
    # Send Email and SMS notifications (from previous steps)





def trigger_geofence_alert(vehicle_id, geofence_name, status):
    # Send WebSocket notifications
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'geofence_alerts',
        {
            'type': 'send_geofence_alert',
            'message': f"Vehicle {vehicle_id} has {status} the geofence: {geofence_name}"
        }
    )

    # Send Email notification
    send_email_notification(vehicle_id, geofence_name, status)

    # Send SMS notification
    send_sms_notification(vehicle_id, geofence_name, status)




from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def trigger_geofence_alert(vehicle_id, geofence_name, status):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'geofence_alerts',
        {
            'type': 'send_geofence_alert',
            'message': f"Vehicle {vehicle_id} has {status} the geofence: {geofence_name}"
        }
    )

def check_geofence(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
        geofences = Geofence.objects.all()

        for geofence in geofences:
            distance = haversine(vehicle.current_latitude, vehicle.current_longitude, geofence.center_latitude, geofence.center_longitude)
            if distance <= geofence.radius_in_km:
                trigger_geofence_alert(vehicle_id, geofence.name, "entered")
                return Response({"message": f"Vehicle {vehicle_id} is inside the geofence: {geofence.name}"})
        
        trigger_geofence_alert(vehicle_id, "all geofences", "left")
        return Response({"message": f"Vehicle {vehicle_id} is outside all geofences"})

    except Vehicle.DoesNotExist:
        return Response({"error": "Vehicle not found"}, status=404)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vehicle, Geofence
from .utils import haversine

@api_view(['GET'])
def check_geofence(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
        geofences = Geofence.objects.all()

        for geofence in geofences:
            distance = haversine(vehicle.current_latitude, vehicle.current_longitude, geofence.center_latitude, geofence.center_longitude)
            if distance <= geofence.radius_in_km:
                return Response({"message": f"Vehicle {vehicle_id} is inside the geofence: {geofence.name}"})
        
        return Response({"message": f"Vehicle {vehicle_id} is outside all geofences"})

    except Vehicle.DoesNotExist:
        return Response({"error": "Vehicle not found"}, status=404)



from rest_framework import viewsets
from .models import Geofence
from .serializers import GeofenceSerializer

class GeofenceViewSet(viewsets.ModelViewSet):
    queryset = Geofence.objects.all()
    serializer_class = GeofenceSerializer



from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
