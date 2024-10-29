from rest_framework import generics
from ..models.gps_tracking import GPSTracking
from ..serializers.gps_tracking_serializer import GPSTrackingSerializer

class GPSTrackingListCreateView(generics.ListCreateAPIView):
    queryset = GPSTracking.objects.all()
    serializer_class = GPSTrackingSerializer
    filterset_fields = ['vehicle']

class GPSTrackingDetailView(generics.RetrieveAPIView):
    queryset = GPSTracking.objects.all()
    serializer_class = GPSTrackingSerializer
