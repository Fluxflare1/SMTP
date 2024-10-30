

from rest_framework import viewsets
from .models import Trip
from .serializers import TripSerializer
from .permissions import IsDispatcherOrAdmin

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsDispatcherOrAdmin]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)




from .models import NotificationPreference

def get_active_recipients(notification_type):
    return [
        pref.user.email
        for pref in NotificationPreference.objects.filter(
            notification_type=notification_type, enabled=True
        )
    ]



class VehicleReactivateView(APIView):
    permission_classes = [IsAuthenticated, CanImmobilizeVehicle]

    def post(self, request, vehicle_id):
        vehicle = Vehicle.objects.get(id=vehicle_id)
        
        if vehicle.is_immobilized:
            vehicle.is_immobilized = False
            vehicle.immobilization_reason = None  # Clear reason on re-activation
            vehicle.save()
            logger.info(f"Vehicle {vehicle_id} re-activated by {request.user.username} at {timezone.now()}")
            return Response({"message": "Vehicle re-activated"}, status=status.HTTP_200_OK)
        
        return Response({"error": "Vehicle is not immobilized"}, status=status.HTTP_400_BAD_REQUEST)





class VehicleImmobilizationView(APIView):
    def post(self, request, vehicle_id):
        vehicle = Vehicle.objects.get(id=vehicle_id)
        reason = request.data.get("reason")
        
        if not reason:
            return Response({"error": "Reason for immobilization required"}, status=status.HTTP_400_BAD_REQUEST)
        
        vehicle.is_immobilized = True
        vehicle.immobilization_reason = reason
        vehicle.save()
        
        # Additional code for logging and notification...





from rest_framework.response import Response
from rest_framework import status

class VehicleImmobilizationConfirmView(APIView):
    permission_classes = [IsAuthenticated, CanImmobilizeVehicle]

    def post(self, request, vehicle_id):
        vehicle = Vehicle.objects.get(id=vehicle_id)
        if not vehicle.is_immobilized:
            # Mark for confirmation
            vehicle.pending_immobilization = True
            vehicle.save()
            return Response({"message": "Confirm immobilization by re-sending this request"}, status=status.HTTP_202_ACCEPTED)
        return Response({"error": "Vehicle already immobilized"}, status=status.HTTP_400_BAD_REQUEST)




from rest_framework.permissions import IsAuthenticated
from .permissions import CanImmobilizeVehicle

class VehicleImmobilizationView(APIView):
    permission_classes = [IsAuthenticated, CanImmobilizeVehicle]
    # Existing code...



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vehicle
from .serializers import VehicleImmobilizationSerializer
from .utils import immobilize_vehicle

class VehicleImmobilizationView(APIView):
    def post(self, request):
        serializer = VehicleImmobilizationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        vehicle_id = serializer.validated_data["vehicle_id"]

        try:
            # Immobilize vehicle using the external service
            immobilization_response = immobilize_vehicle(vehicle_id)
            
            # Update immobilization status in the database
            vehicle = Vehicle.objects.get(id=vehicle_id)
            vehicle.is_immobilized = True
            vehicle.save()

            return Response(
                {"status": "Vehicle immobilized", "data": immobilization_response},
                status=status.HTTP_200_OK
            )
        except Vehicle.DoesNotExist:
            return Response(
                {"error": "Vehicle not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )





from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RouteOptimizationSerializer
from .utils import get_optimized_route

class RouteOptimizationView(APIView):
    def post(self, request):
        serializer = RouteOptimizationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        origin = serializer.validated_data['origin']
        destination = serializer.validated_data['destination']
        waypoints = serializer.validated_data.get('waypoints', [])
        
        try:
            optimized_route = get_optimized_route(origin, destination, waypoints)
            return Response(optimized_route, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleStatusSerializer

class VehicleStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleStatusSerializer




from rest_framework.views import APIView
from .models import Incident
from rest_framework.response import Response

class ResolveIncidentView(APIView):
    def post(self, request, incident_id):
        incident = Incident.objects.get(id=incident_id)
        incident.resolved = True
        incident.save()
        return Response({"status": "Incident resolved"})



from rest_framework.views import APIView
from .models import VehicleLocation
from rest_framework.response import Response
from django.utils.dateparse import parse_datetime

class RouteHistoryReplayView(APIView):
    def get(self, request, vehicle_id):
        start_time = parse_datetime(request.query_params.get("start_time"))
        end_time = parse_datetime(request.query_params.get("end_time"))
        locations = VehicleLocation.objects.filter(
            vehicle_id=vehicle_id,
            timestamp__range=(start_time, end_time)
        ).order_by("timestamp")
        
        serialized_data = [
            {"latitude": loc.latitude, "longitude": loc.longitude, "timestamp": loc.timestamp}
            for loc in locations
        ]
        return Response(serialized_data)




# Path: backend/api/fleet_management/views.py

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .utils import generate_invoice_pdf, send_invoice_email

class InvoiceViewSet(viewsets.ModelViewSet):
    # existing code...
    
    @action(detail=True, methods=["post"])
    def send_pdf(self, request, pk=None):
        invoice = self.get_object()
        pdf_buffer = generate_invoice_pdf(invoice)
        send_invoice_email(invoice, pdf_buffer)
        return Response({"message": "Invoice PDF sent via email."}, status=status.HTTP_200_OK)






# Path: backend/api/fleet_management/views.py

from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer
from rest_framework.permissions import IsAuthenticated

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)





from rest_framework import generics, views
from rest_framework.response import Response
from .models import Trip, FleetIncomeReport
from .serializers import TripSerializer, FleetIncomeReportSerializer

class TripListView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class FleetIncomeReportView(views.APIView):
    def get(self, request, *args, **kwargs):
        report, created = FleetIncomeReport.objects.get_or_create(date=kwargs['date'])
        if created:
            report.calculate_totals()
        serializer = FleetIncomeReportSerializer(report)
        return Response(serializer.data)





from rest_framework import viewsets
from .models import VehiclePerformance, VehicleUsage
from .serializers import VehiclePerformanceSerializer, VehicleUsageSerializer

class VehiclePerformanceViewSet(viewsets.ModelViewSet):
    queryset = VehiclePerformance.objects.all()
    serializer_class = VehiclePerformanceSerializer

class VehicleUsageViewSet(viewsets.ModelViewSet):
    queryset = VehicleUsage.objects.all()
    serializer_class = VehicleUsageSerializer





from rest_framework import viewsets
from .models import Driver, DriverCredential
from .serializers import DriverSerializer, DriverCredentialSerializer
from rest_framework.response import Response
from rest_framework import status

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def create(self, request, *args, **kwargs):
        user_data = request.data.get('user')
        user = User.objects.create(**user_data)
        driver = Driver.objects.create(
            user=user,
            license_number=request.data.get('license_number'),
            phone=request.data.get('phone'),
            address=request.data.get('address')
        )
        serializer = self.get_serializer(driver)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DriverCredentialViewSet(viewsets.ModelViewSet):
    queryset = DriverCredential.objects.all()
    serializer_class = DriverCredentialSerializer




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
