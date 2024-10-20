



from django.urls import path
from .views import immobilize_vehicle, release_vehicle_immobilization

urlpatterns = [
    path('immobilize/<str:vehicle_id>/', immobilize_vehicle, name='immobilize-vehicle'),
    path('release-immobilization/<str:vehicle_id>/', release_vehicle_immobilization, name='release-immobilization'),
]




from tracking.views import check_geofence, GeofenceViewSet

# Geofence endpoints
router.register(r'geofences', GeofenceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/check-geofence/<str:vehicle_id>/', check_geofence),  # Geofence check API
]
