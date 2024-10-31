from django.db import models

class User(models.Model):
    # existing fields...
    geofence_alerts = models.BooleanField(default=True)
    trip_updates = models.BooleanField(default=True)
    maintenance_reminders = models.BooleanField(default=True)
