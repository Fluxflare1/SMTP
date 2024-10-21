from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vehicle, Trip
from .serializers import VehicleSerializer, TripSerializer

class VehicleList(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

class TripSchedule(APIView):
    def post(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class VehicleStatus(APIView):
    def get(self, request, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)
