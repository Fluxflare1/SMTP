from rest_framework import serializers
from .models import Trip
from api.fleet_management.models import Vehicle, Driver

class TripSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())
    driver = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all())

    class Meta:
        model = Trip
        fields = ['id', 'vehicle', 'driver', 'start_time', 'end_time', 'destination', 'status']
        read_only_fields = ['id']
