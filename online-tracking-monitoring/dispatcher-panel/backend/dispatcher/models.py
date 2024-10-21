from django.db import models

class Vehicle(models.Model):
    number_plate = models.CharField(max_length=10)
    model = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='idle')  # idle, on_trip, maintenance

    def __str__(self):
        return self.number_plate


class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Trip(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Trip for {self.vehicle.number_plate} to {self.destination}'
