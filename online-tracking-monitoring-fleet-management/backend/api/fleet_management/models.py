

from django.db import models

class Geofence(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.FloatField()  # Radius in meters

class VehicleLocation(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)



from django.db import models
from django.utils import timezone

class MaintenanceRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="maintenance_records")
    description = models.CharField(max_length=255)
    date_scheduled = models.DateField()
    date_completed = models.DateField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vehicle} - {self.description} - Scheduled on {self.date_scheduled}"

    @property
    def is_overdue(self):
        return self.date_scheduled < timezone.now().date() and not self.is_completed





from django.db import models

class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    license_number = models.CharField(max_length=20, unique=True)
    license_expiry_date = models.DateField()
    total_trips_completed = models.PositiveIntegerField(default=0)
    safety_score = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"





from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('car', 'Car'),
        ('truck', 'Truck'),
        ('van', 'Van'),
        ('motorcycle', 'Motorcycle'),
    ]
    
    type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=20, unique=True)
    operational_status = models.CharField(max_length=20, default='available')
    mileage = models.PositiveIntegerField(default=0)
    last_service_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"

class MaintenanceRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="maintenance_records")
    date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    next_service_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Maintenance on {self.date} for {self.vehicle.license_plate}"
