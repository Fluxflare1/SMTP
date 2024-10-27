from rest_framework import serializers
from .models import Vehicle, MaintenanceRecord

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'type', 'make', 'model', 'year', 'license_plate', 'operational_status', 'mileage', 'last_service_date']

class MaintenanceRecordSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())

    class Meta:
        model = MaintenanceRecord
        fields = ['id', 'vehicle', 'date', 'description', 'cost', 'next_service_date']
