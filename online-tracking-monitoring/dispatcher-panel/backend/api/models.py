from django.db import models

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=15)
    status = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

class Trip(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=50)
    destination = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
