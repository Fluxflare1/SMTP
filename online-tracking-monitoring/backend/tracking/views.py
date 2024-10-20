


from django.http import JsonResponse
from .models import Vehicle

def get_all_vehicles_data(request):
    vehicles = Vehicle.objects.all()
    vehicle_data = []

    for vehicle in vehicles:
        vehicle_data.append({
            'vehicle_id': vehicle.vehicle_id,
            'latitude': vehicle.latitude,
            'longitude': vehicle.longitude,
            'total_distance_traveled': vehicle.total_distance_traveled,
            'immobilized': vehicle.immobilized,
            'speed': vehicle.speed
        })

    return JsonResponse({'vehicles': vehicle_data})




from django.http import JsonResponse
from .models import Vehicle

def update_vehicle_location(request, vehicle_id):
    # Example data: {'latitude': 10.123, 'longitude': 12.456}
    new_latitude = float(request.GET.get('latitude'))
    new_longitude = float(request.GET.get('longitude'))

    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    distance_traveled = vehicle.calculate_distance(new_latitude, new_longitude)

    return JsonResponse({
        'status': 'success',
        'distance_traveled': distance_traveled,
        'total_distance_traveled': vehicle.total_distance_traveled
    })




from django.http import JsonResponse
from .models import Vehicle

IDLE_THRESHOLD = 15  # idle time threshold in minutes

def check_idle_time(vehicle_id):
    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    vehicle.update_idle_status()
    idle_duration = vehicle.get_idle_duration()

    if idle_duration >= IDLE_THRESHOLD:
        trigger_idle_alert(vehicle_id, idle_duration)
    
    return JsonResponse({'status': 'success', 'idle_duration': idle_duration})

def trigger_idle_alert(vehicle_id, idle_duration):
    # Logic for triggering an idle alert (could be a WebSocket message, email, etc.)
    print(f"Alert: Vehicle {vehicle_id} has been idle for {idle_duration} minutes.")





from django.http import JsonResponse
from .models import Vehicle

def immobilize_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    vehicle.immobilize()
    return JsonResponse({'status': 'immobilized', 'vehicle_id': vehicle_id})

def release_vehicle_immobilization(request, vehicle_id):
    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    vehicle.release_immobilization()
    return JsonResponse({'status': 'released', 'vehicle_id': vehicle_id})





from django.http import JsonResponse
from tracking.models import Vehicle

CORNERING_THRESHOLD = 30  # Threshold for harsh cornering in degrees
DISTRACTED_DRIVING_THRESHOLD = 15  # Threshold for distracted driving

def monitor_driver_behavior(request, vehicle_id):
    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    if vehicle.acceleration > ACCELERATION_THRESHOLD:
        trigger_geofence_alert(vehicle_id, "harsh acceleration", "triggered")
    if vehicle.braking > BRAKING_THRESHOLD:
        trigger_geofence_alert(vehicle_id, "harsh braking", "triggered")
    if vehicle.cornering > CORNERING_THRESHOLD:
        trigger_geofence_alert(vehicle_id, "harsh cornering", "triggered")
    if vehicle.distracted_driving_score > DISTRACTED_DRIVING_THRESHOLD:
        trigger_geofence_alert(vehicle_id, "distracted driving", "triggered")
    return JsonResponse({'status': 'Driver behavior monitored'})




from django.http import JsonResponse
from tracking.models import Geofence  # Assuming there is a Geofence model

def create_geofence(request):
    if request.method == 'POST':
        data = request.POST
        geofence = Geofence.objects.create(
            name=data['name'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            radius=data['radius'],  # Radius of the geofence in meters
            alert_on_enter=data['alert_on_enter'],  # Boolean for alert on enter
            alert_on_exit=data['alert_on_exit'],  # Boolean for alert on exit
        )
        return JsonResponse({'status': 'Geofence created', 'geofence_id': geofence.id})
    return JsonResponse({'status': 'Invalid method'}, status=405)



from django.http import JsonResponse
from tracking.models import Vehicle  # Assuming Vehicle model stores health data

def get_vehicle_health(request, vehicle_id):
    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    health_data = {
        'engine_status': vehicle.engine_status,  # Engine on/off
        'temperature': vehicle.temperature,  # Engine temperature
        'maintenance_due': vehicle.maintenance_due,  # Maintenance status
    }
    return JsonResponse(health_data)





from django.http import JsonResponse
from tracking.models import Vehicle  # Assuming Vehicle model stores fuel data

def get_fuel_consumption(request, vehicle_id):
    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    fuel_data = {
        'current_fuel_level': vehicle.fuel_level,  # Assuming fuel level is stored
        'average_fuel_consumption': vehicle.average_fuel_consumption,  # Historical fuel consumption
    }
    return JsonResponse(fuel_data)





from tracking.models import Vehicle

def immobilize_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    vehicle.is_immobilized = True
    vehicle.save()
    return JsonResponse({'status': 'Vehicle immobilized successfully'})




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
