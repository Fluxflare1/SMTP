from django.http import JsonResponse
from rest_framework.views import APIView
from .services.driver_service import DriverService

class DriverAssignmentAPI(APIView):

    def post(self, request):
        """
        Assign a driver to a specific trip.
        """
        try:
            trip_id = request.data.get('trip_id')
            driver_id = request.data.get('driver_id')
            DriverService.assign_driver(trip_id, driver_id)
            return JsonResponse({"message": "Driver assigned successfully"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def get(self, request, trip_id):
        """
        Retrieve the driver assigned to a specific trip.
        """
        try:
            driver = DriverService.get_assigned_driver(trip_id)
            return JsonResponse({"assigned_driver": driver.to_dict()}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)
