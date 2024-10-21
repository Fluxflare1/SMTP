from django.urls import path
from . import views

urlpatterns = [
    path('vehicles/', views.VehicleList.as_view(), name='vehicle-list'),
    path('trip-schedule/', views.TripSchedule.as_view(), name='trip-schedule'),
    path('vehicle-status/<int:pk>/', views.VehicleStatus.as_view(), name='vehicle-status'),
]
