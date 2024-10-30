



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleStatusViewSet

router = DefaultRouter()
router.register(r'vehicle-status', VehicleStatusViewSet, basename='vehicle-status')

urlpatterns = [
    path('', include(router.urls)),
]



from django.urls import path
from .views.gps_tracking_view import GPSTrackingListCreateView, GPSTrackingDetailView

urlpatterns = [
    path('gps/', GPSTrackingListCreateView.as_view(), name='gps_list_create'),
    path('gps/<int:pk>/', GPSTrackingDetailView.as_view(), name='gps_detail'),
    # Other paths for fleet management
]




from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.driver_profiles import DriverProfileViewSet

router = DefaultRouter()
router.register(r'drivers', DriverProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



# Path: backend/api/fleet_management/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('invoices/<int:pk>/send_pdf/', InvoiceViewSet.as_view({'post': 'send_pdf'}), name='send_invoice_pdf'),
]




# Path: backend/api/fleet_management/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



from .views import DriverViewSet, DriverCredentialViewSet

router.register(r'drivers', DriverViewSet)
router.register(r'driver-credentials', DriverCredentialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]






from .views import ClientViewSet, InvoiceViewSet

router.register(r'clients', ClientViewSet)
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]




from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripIncomeViewSet, FleetExpenseViewSet

router = DefaultRouter()
router.register(r'trip-income', TripIncomeViewSet)
router.register(r'fleet-expense', FleetExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripExpenseViewSet

router = DefaultRouter()
router.register(r'trip-expenses', TripExpenseViewSet, basename='trip-expenses')

urlpatterns = [
    path('', include(router.urls)),
]





from .views import MaintenanceRecordViewSet

router.register(r'maintenance', MaintenanceRecordViewSet, basename='maintenance')



from .views import VehicleViewSet, DriverViewSet, FleetReportView

router.register(r'drivers', DriverViewSet, basename='driver')




from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, FleetReportView

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')

urlpatterns = router.urls + [
    path('reports/', FleetReportView.as_view(), name='fleet-reports')
]




from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, MaintenanceRecordViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'maintenance-records', MaintenanceRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
