from rest_framework import serializers
from django.utils import timezone
from .models import Trip, Vehicle, Driver

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

    def validate(self, data):
        # Check vehicle availability
        vehicle = data.get("vehicle")
        start_time = data.get("start_time")
        end_time = data.get("end_time")
        
        overlapping_trips = Trip.objects.filter(
            vehicle=vehicle,
            start_time__lt=end_time,
            end_time__gt=start_time,
        ).exists()

        if overlapping_trips:
            raise serializers.ValidationError("Vehicle is unavailable for the selected times.")

        # Check driver availability
        driver = data.get("driver")
        overlapping_trips = Trip.objects.filter(
            driver=driver,
            start_time__lt=end_time,
            end_time__gt=start_time,
        ).exists()

        if overlapping_trips:
            raise serializers.ValidationError("Driver is unavailable for the selected times.")

        return data
