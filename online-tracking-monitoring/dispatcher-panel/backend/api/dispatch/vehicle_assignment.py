from django.http import JsonResponse
from django.views import View
from .models import Trip, Vehicle

class AssignVehicleView(View):
    def post(self, request):
        trip_id = request.POST.get('trip_id')
        vehicle_id = request.POST.get('vehicle_id')

        trip = Trip.objects.get(id=trip_id)
        vehicle = Vehicle.objects.get(id=vehicle_id)

        trip.vehicle = vehicle
        trip.save()

        return JsonResponse({'status': 'success', 'trip_id': trip.id})
