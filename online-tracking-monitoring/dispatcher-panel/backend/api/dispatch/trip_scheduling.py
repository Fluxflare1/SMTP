from django.http import JsonResponse
from rest_framework.views import APIView
from .models.trip_model import Trip
from .services.dispatch_service import DispatchService

class TripSchedulingAPI(APIView):
    
    def post(self, request):
        """
        Schedule a new trip and assign a driver.
        """
        try:
            trip_data = request.data
            trip = DispatchService.schedule_trip(trip_data)
            return JsonResponse({"message": "Trip scheduled successfully", "trip_id": trip.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def put(self, request, trip_id):
        """
        Update an existing trip details (e.g. reschedule or reassign driver).
        """
        try:
            trip_data = request.data
            trip = DispatchService.update_trip(trip_id, trip_data)
            return JsonResponse({"message": "Trip updated successfully", "trip_id": trip.id}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def get(self, request, trip_id):
        """
        Retrieve a specific trip's details.
        """
        try:
            trip = Trip.objects.get(id=trip_id)
            return JsonResponse({"trip": trip.to_dict()}, status=200)
        except Trip.DoesNotExist:
            return JsonResponse({"error": "Trip not found"}, status=404)
