from tracking.views import check_geofence, GeofenceViewSet

# Geofence endpoints
router.register(r'geofences', GeofenceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/check-geofence/<str:vehicle_id>/', check_geofence),  # Geofence check API
]
