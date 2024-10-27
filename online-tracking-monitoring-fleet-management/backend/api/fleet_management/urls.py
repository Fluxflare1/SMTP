from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, MaintenanceRecordViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'maintenance-records', MaintenanceRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
