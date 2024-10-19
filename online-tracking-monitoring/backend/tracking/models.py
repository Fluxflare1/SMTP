from django.db import models

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=100, unique=True)
    current_latitude = models.FloatField()
    current_longitude = models.FloatField()
    current_speed = models.FloatField()
    status = models.CharField(max_length=50)  # E.g., Active, Idle, Inactive
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle_id} - {self.status}"
