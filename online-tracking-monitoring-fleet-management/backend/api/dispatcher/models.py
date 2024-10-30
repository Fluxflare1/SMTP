from django.db import models
from backend.api.fleet_management.models import Vehicle, Driver

class TripStatus(models.Model):
    status_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.status_name

class Trip(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="trips")
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="trips")
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    estimated_time_of_arrival = models.DateTimeField()
    status = models.ForeignKey(TripStatus, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trip from {self.origin} to {self.destination} with {self.driver}"
