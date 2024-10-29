from rest_framework import serializers
from ..models.gps_tracking import GPSTracking

class GPSTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSTracking
        fields = ["vehicle", "latitude", "longitude", "timestamp"]
        read_only_fields = ["timestamp"]
