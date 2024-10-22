from .models.driver_model import Driver
from .models.trip_model import Trip
from django.core.exceptions import ValidationError

class DriverService:

    @staticmethod
    def assign_driver(trip_id, driver_id):
        """
        Business logic to assign a driver to a trip.
        """
        try:
            trip = Trip.objects.get(id=trip_id)
            driver = Driver.objects.get(id=driver_id)

            if trip.status == "scheduled":
                trip.driver = driver
                trip.save()
            else:
                raise ValidationError("Driver cannot be assigned. Trip is not in 'scheduled' status.")
        except Exception as e:
            raise ValidationError(f"Failed to assign driver: {e}")

    @staticmethod
    def get_assigned_driver(trip_id):
        """
        Retrieve the driver assigned to a specific trip.
        """
        try:
            trip = Trip.objects.get(id=trip_id)
            if trip.driver:
                return trip.driver
            else:
                raise ValidationError("No driver assigned to this trip.")
        except Trip.DoesNotExist:
            raise ValidationError("Trip not found")
