from django.http import JsonResponse
from django.views import View
from .models import Trip, Vehicle, Driver

class ScheduleTripView(View):
    def post(self, request):
        vehicle_id = request.POST.get('vehicle_id')
        driver_id = request.POST.get('driver_id')
        destination = request.POST.get('destination')
        pickup = request.POST.get('pickup')

        vehicle = Vehicle.objects.get(id=vehicle_id)
        driver = Driver.objects.get(id=driver_id)

        # Create new trip
        trip = Trip.objects.create(
            vehicle=vehicle,
            driver=driver,
            destination=destination,
            pickup=pickup
        )
        trip.save()

        return JsonResponse({'status': 'success', 'trip_id': trip.id})
