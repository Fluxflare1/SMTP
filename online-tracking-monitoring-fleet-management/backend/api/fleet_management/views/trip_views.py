from rest_framework import viewsets
from .permissions import IsDispatcherOrAdminOrFleetManager
from .models import Trip
from .serializers import TripSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsDispatcherOrAdminOrFleetManager]
    
    def perform_create(self, serializer):
        # Additional validation can be added here
        serializer.save(dispatcher=self.request.user)
