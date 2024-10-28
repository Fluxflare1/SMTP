# Path: backend/api/urls.py

from django.urls import path, include

urlpatterns = [
    path('fleet_management/', include('fleet_management.urls')),
    # Other included paths
]
