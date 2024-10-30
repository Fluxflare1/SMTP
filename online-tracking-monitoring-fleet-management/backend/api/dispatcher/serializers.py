from rest_framework import serializers
from .models import Trip, TripStatus

class TripStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripStatus
        fields = ['id', 'status_name']

class TripSerializer(serializers.ModelSerializer):
    vehicle = serializers.StringRelatedField()
    driver = serializers.StringRelatedField()
    status = TripStatusSerializer(read_only=True)

    class Meta:
        model = Trip
        fields = [
            'id', 'vehicle', 'driver', 'origin', 'destination',
            'estimated_time_of_arrival', 'status', 'created_at', 'updated_at'
        ]
