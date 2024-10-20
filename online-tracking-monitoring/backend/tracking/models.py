



import math

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    total_distance_traveled = models.FloatField(default=0)  # Already exists
    speed = models.FloatField()

    def calculate_distance(self, new_latitude, new_longitude):
        # Haversine formula to calculate distance between two points on the Earth
        R = 6371  # Radius of the Earth in kilometers
        lat1 = math.radians(self.latitude)
        lon1 = math.radians(self.longitude)
        lat2 = math.radians(new_latitude)
        lon2 = math.radians(new_longitude)
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c  # Distance in kilometers

        # Update total distance traveled
        self.total_distance_traveled += distance
        self.latitude = new_latitude
        self.longitude = new_longitude
        self.save()

        return distance




from django.db import models
from datetime import datetime

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    total_distance_traveled = models.FloatField(default=0)
    speed = models.FloatField()
    idle_start_time = models.DateTimeField(null=True, blank=True)
    is_idle = models.BooleanField(default=False)

    def update_idle_status(self):
        if self.speed == 0 and not self.is_idle:
            self.is_idle = True
            self.idle_start_time = datetime.now()
            self.save()
        elif self.speed > 0 and self.is_idle:
            self.is_idle = False
            self.idle_start_time = None
            self.save()

    def get_idle_duration(self):
        if self.is_idle and self.idle_start_time:
            now = datetime.now()
            idle_duration = now - self.idle_start_time
            return idle_duration.total_seconds() / 60  # returns duration in minutes
        return 0




class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    total_distance_traveled = models.FloatField(default=0)
    immobilized = models.BooleanField(default=False)  # New field for immobilization status
    speed = models.FloatField()

    def immobilize(self):
        self.immobilized = True
        self.save()

    def release_immobilization(self):
        self.immobilized = False
        self.save()



from django.db import models

class Geofence(models.Model):
    name = models.CharField(max_length=100)
    center_latitude = models.FloatField()
    center_longitude = models.FloatField()
    radius_in_km = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.radius_in_km} km"




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
