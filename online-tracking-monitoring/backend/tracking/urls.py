



from django.urls import path
from .views import get_all_vehicles_location

urlpatterns = [
    path('api/vehicles/location/', get_all_vehicles_location, name='get_all_vehicles_location'),
]




from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracking.views import VehicleViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
