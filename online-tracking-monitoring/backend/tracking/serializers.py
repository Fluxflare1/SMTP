



from .models import Geofence

class GeofenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geofence
        fields = ['id', 'name', 'center_latitude', 'center_longitude', 'radius_in_km', 'created_at']




from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['vehicle_id', 'current_latitude', 'current_longitude', 'current_speed', 'status', 'last_updated']
