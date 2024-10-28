




from rest_framework import viewsets
from .models import Client, Invoice, TripIncome, FleetExpense
from .serializers import ClientSerializer, InvoiceSerializer
from rest_framework.response import Response
from rest_framework import status

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        # Logic to calculate total income, expenses, and profit for invoicing
        client = Client.objects.get(id=request.data.get('client_id'))
        income = TripIncome.objects.filter(trip__client=client).aggregate(total=models.Sum('income'))['total'] or 0
        expenses = FleetExpense.objects.filter(trip__client=client).aggregate(total=models.Sum('amount'))['total'] or 0
        profit = income - expenses
        
        invoice = Invoice.objects.create(
            client=client,
            total_income=income,
            total_expense=expenses,
            total_profit=profit,
            due_date=request.data.get('due_date')
        )
        serializer = self.get_serializer(invoice)
        return Response(serializer.data, status=status.HTTP_201_CREATED)







from rest_framework import viewsets
from .models import TripIncome, FleetExpense
from .serializers import TripIncomeSerializer, FleetExpenseSerializer

class TripIncomeViewSet(viewsets.ModelViewSet):
    queryset = TripIncome.objects.all()
    serializer_class = TripIncomeSerializer

class FleetExpenseViewSet(viewsets.ModelViewSet):
    queryset = FleetExpense.objects.all()
    serializer_class = FleetExpenseSerializer





from rest_framework import viewsets
from rest_framework.response import Response
from .models import Trip
from .serializers import TripExpenseSerializer

class TripExpenseViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripExpenseSerializer
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.total_expense > instance.expense_threshold:
            # Trigger alert logic here
            self.send_expense_alert(instance)

    def send_expense_alert(self, trip):
        # Placeholder function for sending an alert to fleet managers
        pass





from .models import MaintenanceRecord
from .serializers import MaintenanceRecordSerializer

class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()




from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Driver
from .serializers import DriverSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)






from django.db.models import Sum, Avg
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class FleetReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Optional filters
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        vehicles = Vehicle.objects.all()

        if start_date and end_date:
            vehicles = vehicles.filter(last_service_date__range=[start_date, end_date])

        total_mileage = vehicles.aggregate(Sum('mileage'))['mileage__sum'] or 0
        total_maintenance_cost = MaintenanceRecord.objects.filter(
            vehicle__in=vehicles
        ).aggregate(Sum('cost'))['cost__sum'] or 0
        average_mileage = vehicles.aggregate(Avg('mileage'))['mileage__avg'] or 0

        data = {
            'total_vehicles': vehicles.count(),
            'total_mileage': total_mileage,
            'total_maintenance_cost': total_maintenance_cost,
            'average_mileage': average_mileage,
        }
        return Response(data, status=status.HTTP_200_OK)




@action(detail=True, methods=['get'], url_path='maintenance-history')
    def maintenance_history(self, request, pk=None):
        vehicle = self.get_object()
        maintenance_records = MaintenanceRecord.objects.filter(vehicle=vehicle).order_by('-date')
        serializer = MaintenanceRecordSerializer(maintenance_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['type', 'operational_status', 'last_service_date']
    search_fields = ['make', 'model', 'license_plate']
    ordering_fields = ['year', 'mileage', 'last_service_date']




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
