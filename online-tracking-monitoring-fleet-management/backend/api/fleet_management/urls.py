

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
