from rest_framework import viewsets
from .models import Trip, TripStatus
from .serializers import TripSerializer, TripStatusSerializer

class TripStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TripStatus.objects.all()
    serializer_class = TripStatusSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
