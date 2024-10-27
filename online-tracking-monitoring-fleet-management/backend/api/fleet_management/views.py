

@action(detail=True, methods=['patch'], url_path='schedule-maintenance')
    def schedule_maintenance(self, request, pk=None):
        vehicle = self.get_object()
        next_service_date = request.data.get('next_service_date')
        
        if next_service_date:
            MaintenanceRecord.objects.create(
                vehicle=vehicle,
                date=next_service_date,
                description="Scheduled Maintenance"
            )
            vehicle.last_service_date = next_service_date
            vehicle.save()
            return Response({'status': 'maintenance scheduled'}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Next service date not provided'}, status=status.HTTP_400_BAD_REQUEST)





from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['patch'], url_path='update-mileage')
    def update_mileage(self, request, pk=None):
        vehicle = self.get_object()
        mileage = request.data.get('mileage')
        
        if mileage is not None:
            vehicle.mileage = mileage
            vehicle.save()
            return Response({'status': 'mileage updated'}, status=status.HTTP_200_OK)
        return Response({'error': 'Mileage not provided'}, status=status.HTTP_400_BAD_REQUEST)





from rest_framework import viewsets
from .models import Vehicle, MaintenanceRecord
from .serializers import VehicleSerializer, MaintenanceRecordSerializer
from rest_framework.permissions import IsAuthenticated

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer
    permission_classes = [IsAuthenticated]
