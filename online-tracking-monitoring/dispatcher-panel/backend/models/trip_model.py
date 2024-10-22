
from django.db import models

class Trip(models.Model):
    vehicle_id = models.IntegerField()
    driver_id = models.IntegerField()
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=50, default="scheduled")

    def to_dict(self):
        return {
            "id": self.id,
            "vehicle_id": self.vehicle_id,
            "driver_id": self.driver_id,
            "start_location": self.start_location,
            "end_location": self.end_location,
            "scheduled_time": self.scheduled_time,
            "status": self.status,
        }
