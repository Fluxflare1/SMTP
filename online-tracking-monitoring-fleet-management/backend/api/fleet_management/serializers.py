




from rest_framework import serializers
from .models import DriverProfile

class DriverProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        fields = "__all__"




# Path: backend/api/fleet_management/serializers.py

from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"







from rest_framework import serializers
from .models import Trip, FleetIncomeReport

class TripSerializer(serializers.ModelSerializer):
    total_expense = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    profitability = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Trip
        fields = ['id', 'distance_traveled', 'fuel_cost', 'tolls_cost', 'driver_pay', 'income_generated', 'total_expense', 'profitability']


class FleetIncomeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetIncomeReport
        fields = ['date', 'total_income', 'total_expenses', 'net_profit']




from rest_framework import serializers
from .models import VehiclePerformance, VehicleUsage

class VehiclePerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclePerformance
        fields = ["vehicle", "date_recorded", "mileage", "fuel_efficiency", "issues_reported"]

class VehicleUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleUsage
        fields = ["vehicle", "date", "trip_count", "total_distance"]





from .models import Driver, DriverCredential
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class DriverCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverCredential
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    credentials = DriverCredentialSerializer(many=True, read_only=True)

    class Meta:
        model = Driver
        fields = ['id', 'user', 'license_number', 'phone', 'address', 'credentials']




from .models import Client, Invoice

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'




from rest_framework import serializers
from .models import TripIncome, FleetExpense

class TripIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripIncome
        fields = '__all__'

class FleetExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleetExpense
        fields = '__all__'




from rest_framework import serializers
from .models import Trip

class TripExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'vehicle', 'driver', 'start_location', 'end_location', 'expense_threshold', 'total_expense']

    def validate(self, data):
        if data['total_expense'] > data['expense_threshold']:
            # Trigger alert for expense threshold exceeded
            self.create_expense_alert(data)
        return data

    def create_expense_alert(self, trip_data):
        # Placeholder logic to create and send expense alert
        pass





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
