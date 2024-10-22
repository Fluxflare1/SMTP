from .models.trip_model import Trip
from django.core.exceptions import ValidationError

class DispatchService:
    
    @staticmethod
    def schedule_trip(trip_data):
        """
        Business logic for scheduling a new trip.
        """
        try:
            trip = Trip(
                vehicle_id=trip_data.get("vehicle_id"),
                driver_id=trip_data.get("driver_id"),
                start_location=trip_data.get("start_location"),
                end_location=trip_data.get("end_location"),
                scheduled_time=trip_data.get("scheduled_time")
            )
            trip.save()
            return trip
        except ValidationError as e:
            raise e

    @staticmethod
    def update_trip(trip_id, trip_data):
        """
        Business logic for updating an existing trip.
        """
        try:
            trip = Trip.objects.get(id=trip_id)
            trip.vehicle_id = trip_data.get("vehicle_id", trip.vehicle_id)
            trip.driver_id = trip_data.get("driver_id", trip.driver_id)
            trip.start_location = trip_data.get("start_location", trip.start_location)
            trip.end_location = trip_data.get("end_location", trip.end_location)
            trip.scheduled_time = trip_data.get("scheduled_time", trip.scheduled_time)
            trip.save()
            return trip
        except Trip.DoesNotExist:
            raise ValidationError("Trip not found")
