
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
