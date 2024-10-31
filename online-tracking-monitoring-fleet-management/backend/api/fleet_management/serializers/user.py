from rest_framework import serializers
from .models import User

class NotificationPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['geofence_alerts', 'trip_updates', 'maintenance_reminders']
