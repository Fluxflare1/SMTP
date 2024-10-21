from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Trip(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField()
