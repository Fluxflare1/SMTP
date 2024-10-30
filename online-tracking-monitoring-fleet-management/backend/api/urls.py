


from django.urls import path, include

urlpatterns = [
    path('fleet/', include('api.fleet_management.urls')),
    # ... other paths
]




from django.urls import path, include

urlpatterns = [
    path('fleet/', include('api.fleet_management.urls')),
    # ... other paths
]




from django.urls import path, include

urlpatterns = [
    path('dispatcher/', include('api.dispatcher_panel.urls')),
    # ... other paths
]



# Path: backend/api/urls.py

from django.urls import path, include

urlpatterns = [
    path('fleet_management/', include('fleet_management.urls')),
    # Other included paths
]
