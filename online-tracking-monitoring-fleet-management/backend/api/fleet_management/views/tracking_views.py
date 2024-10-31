from .models import VehicleTracking
from .serializers import VehicleTrackingSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class RealTimeTrackingView(generics.ListAPIView):
    queryset = VehicleTracking.objects.select_related('vehicle').only('vehicle_id', 'location', 'timestamp')
    serializer_class = VehicleTrackingSerializer
    permission_classes = [IsAuthenticated]
