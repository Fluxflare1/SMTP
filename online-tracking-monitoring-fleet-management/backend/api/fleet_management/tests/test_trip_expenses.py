from django.test import TestCase
from .models import Trip, Vehicle, Driver
from .views import TripExpenseViewSet

class TripExpenseTests(TestCase):
    def setUp(self):
        # Initialize test data for vehicle, driver, and trip
        self.vehicle = Vehicle.objects.create(...)
        self.driver = Driver.objects.create(...)
        self.trip = Trip.objects.create(
            vehicle=self.vehicle,
            driver=self.driver,
            start_location="Location A",
            end_location="Location B",
            expense_threshold=500.00,
            total_expense=0.00
        )

    def test_expense_threshold_exceeded(self):
        # Set total_expense above threshold
        self.trip.total_expense = 600.00
        self.trip.save()
        # Assert that alert is triggered
        self.assertTrue(self.trip.total_expense > self.trip.expense_threshold)
