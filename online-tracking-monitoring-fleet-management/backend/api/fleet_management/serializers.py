



from .models import MaintenanceRecord

class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = ['id', 'vehicle', 'description', 'date_scheduled', 'date_completed', 'cost', 'is_completed', 'is_overdue']




from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'license_number', 'license_expiry_date', 'total_trips_completed', 'safety_score']






class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = ['id', 'date', 'description', 'cost']




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
