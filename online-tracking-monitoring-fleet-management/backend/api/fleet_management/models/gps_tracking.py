from django.db import models
from .vehicle import Vehicle  # assuming Vehicle model exists in fleet_management/models/vehicle.py

class GPSTracking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="gps_logs")
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"GPS Log for {self.vehicle} at {self.timestamp}"
