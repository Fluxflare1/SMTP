from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="available")  # Status: available, on trip, unavailable

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "license_number": self.license_number,
            "status": self.status,
        }
