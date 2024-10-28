



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
