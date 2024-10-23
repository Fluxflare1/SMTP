from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=20)

class Driver(models.Model):
    name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=20)

class Trip(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    pickup = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default="scheduled")
