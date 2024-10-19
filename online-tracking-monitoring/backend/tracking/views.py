




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
