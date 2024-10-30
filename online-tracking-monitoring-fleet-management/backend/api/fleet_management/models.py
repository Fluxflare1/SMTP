
from django.db import models

class NotificationLog(models.Model):
    notification_type = models.CharField(max_length=50)
    recipient = models.EmailField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[("sent", "Sent"), ("failed", "Failed")])

    def __str__(self):
        return f"{self.notification_type} to {self.recipient} at {self.sent_at}"



from django.db import models

class Vehicle(models.Model):
    # Existing fields...
    immobilization_reason = models.CharField(max_length=255, blank=True, null=True)
    # New fields...




from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vehicle

@receiver(post_save, sender=Vehicle)
def send_immobilization_notification(sender, instance, **kwargs):
    if instance.is_immobilized:
        # Logic for sending notification, e.g., email, push notification
        send_notification(
            title="Vehicle Immobilized",
            message=f"Vehicle {instance.id} has been immobilized.",
        )




from django.db import models

class Vehicle(models.Model):
    # Existing fields...
    is_immobilized = models.BooleanField(default=False)

    def __str__(self):
        return self.name  # Example field



class Vehicle(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'Maintenance'),
        ('unavailable', 'Unavailable')
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    # Other fields and methods



class DriverSafetyScore(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    score = models.FloatField()
    speeding_count = models.IntegerField()
    harsh_braking_count = models.IntegerField()
    sudden_acceleration_count = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)




class Incident(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    incident_type = models.CharField(max_length=50)
    severity = models.CharField(max_length=10, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")])
    description = models.TextField()
    resolved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vehicle} - {self.incident_type} ({self.severity})"



from django.db import models

class Geofence(models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.JSONField()  # Stores geofence as a list of coordinates
    is_active = models.BooleanField(default=True)  # Enable/disable geofence

    def __str__(self):
        return self.name



from django.db import models
from django.utils import timezone

class DriverProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    license_number = models.CharField(max_length=100, unique=True)
    license_expiration_date = models.DateField()
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def is_license_expired(self):
        return timezone.now().date() > self.license_expiration_date




from django.db import models
from django.utils import timezone

class Invoice(models.Model):
    ...
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("overdue", "Overdue"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    due_date = models.DateField(blank=True, null=True)

    def check_overdue_status(self):
        if self.due_date and self.due_date < timezone.now().date() and self.status != "paid":
            self.status = "overdue"
            self.save()




from django.db import models
from django.utils import timezone

class Invoice(models.Model):
    ...
    is_recurring = models.BooleanField(default=False)
    recurrence_frequency = models.CharField(
        max_length=20,
        choices=[("weekly", "Weekly"), ("monthly", "Monthly"), ("yearly", "Yearly")],
        blank=True,
        null=True
    )
    next_recurrence_date = models.DateField(blank=True, null=True)

    def schedule_next_recurrence(self):
        # Logic to calculate and update `next_recurrence_date` based on frequency
        pass






# Path: backend/api/fleet_management/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Invoice(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="invoices")
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("paid", "Paid")])
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.client.username}"







from django.db import models

class Trip(models.Model):
    # Existing fields...
    distance_traveled = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fuel_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tolls_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    driver_pay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    income_generated = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    @property
    def total_expense(self):
        return (self.fuel_cost or 0) + (self.tolls_cost or 0) + (self.driver_pay or 0)
    
    @property
    def profitability(self):
        return (self.income_generated or 0) - self.total_expense


class FleetIncomeReport(models.Model):
    date = models.DateField(auto_now_add=True)
    total_income = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_expenses = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    net_profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def calculate_totals(self):
        trips = Trip.objects.filter(created_at__date=self.date)
        self.total_income = sum(trip.income_generated or 0 for trip in trips)
        self.total_expenses = sum(trip.total_expense for trip in trips)
        self.net_profit = self.total_income - self.total_expenses
        self.save()





from django.db import models
from .vehicle import Vehicle

class VehiclePerformance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="performance")
    date_recorded = models.DateField(auto_now_add=True)
    mileage = models.FloatField()  # in kilometers
    fuel_efficiency = models.FloatField()  # km per liter
    issues_reported = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-date_recorded"]

    def __str__(self):
        return f"{self.vehicle} Performance on {self.date_recorded}"

class VehicleUsage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="usage")
    date = models.DateField(auto_now_add=True)
    trip_count = models.IntegerField(default=0)
    total_distance = models.FloatField()  # total distance in kilometers

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.vehicle} Usage on {self.date}"





from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()

class DriverCredential(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='credentials')
    credential_type = models.CharField(max_length=50)  # e.g., "License", "Certification"
    issue_date = models.DateField()
    expiration_date = models.DateField()
    is_active = models.BooleanField(default=True)




from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total_income = models.DecimalField(max_digits=10, decimal_places=2)
    total_expense = models.DecimalField(max_digits=10, decimal_places=2)
    total_profit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)




from django.db import models

class TripIncome(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class FleetExpense(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)





def calculate_total_expense(self):
    # Add up fuel, tolls, driver pay, etc.
    return self.fuel_cost + self.toll_cost + self.driver_pay



from django.db import models
from .vehicle import Vehicle
from .driver import Driver

class Trip(models.Model):
    # existing fields...
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    expense_threshold = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_expense = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def calculate_total_expense(self):
        # Placeholder for the actual expense calculation
        # This could include fuel, tolls, and other trip-related expenses
        return self.total_expense




from django.db import models
from django.contrib.auth import get_user_model
from datetime import timedelta

User = get_user_model()

class DriverDocumentation(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=100)  # e.g., License, Medical Certificate
    expiration_date = models.DateField()

    def is_expiring_soon(self):
        return self.expiration_date <= timezone.now().date() + timedelta(days=30)  # 30-day threshold




from django.db import models

class FuelUsage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    fuel_level = models.DecimalField(max_digits=5, decimal_places=2)  # in liters or percentage
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']



from django.db import models

class DriverBehaviorEvent(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)  # e.g., "Speeding", "Harsh Braking"
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)





from django.db import models

class Geofence(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.FloatField()  # Radius in meters

class VehicleLocation(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)



from django.db import models
from django.utils import timezone

class MaintenanceRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="maintenance_records")
    description = models.CharField(max_length=255)
    date_scheduled = models.DateField()
    date_completed = models.DateField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vehicle} - {self.description} - Scheduled on {self.date_scheduled}"

    @property
    def is_overdue(self):
        return self.date_scheduled < timezone.now().date() and not self.is_completed





from django.db import models

class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    license_number = models.CharField(max_length=20, unique=True)
    license_expiry_date = models.DateField()
    total_trips_completed = models.PositiveIntegerField(default=0)
    safety_score = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"





from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('car', 'Car'),
        ('truck', 'Truck'),
        ('van', 'Van'),
        ('motorcycle', 'Motorcycle'),
    ]
    
    type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=20, unique=True)
    operational_status = models.CharField(max_length=20, default='available')
    mileage = models.PositiveIntegerField(default=0)
    last_service_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"

class MaintenanceRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="maintenance_records")
    date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    next_service_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Maintenance on {self.date} for {self.vehicle.license_plate}"
