
from django.urls import path
from .views import get_filtered_vehicles_data

urlpatterns = [
    # Other URL patterns...
    path('get-filtered-vehicles-data/', get_filtered_vehicles_data, name='get-filtered-vehicles-data'),
]


from django.urls import path
from .views import get_all_vehicles_data

urlpatterns = [
    # Other URL patterns...
    path('get-all-vehicles-data/', get_all_vehicles_data, name='get-all-vehicles-data'),
]




from django.urls import path
from .views import update_vehicle_location

urlpatterns = [
    # Other URL patterns...
    path('update-vehicle-location/<str:vehicle_id>/', update_vehicle_location, name='update-vehicle-location'),
]



from django.urls import path
from .views import check_idle_time

urlpatterns = [
    # Other URL patterns...
    path('check-idle-time/<str:vehicle_id>/', check_idle_time, name='check-idle-time'),
]




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
