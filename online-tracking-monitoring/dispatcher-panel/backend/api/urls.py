from django.urls import path
from .views import TripScheduleView, VehicleStatusView

urlpatterns = [
    path('schedule-trip/', TripScheduleView.as_view(), name='schedule_trip'),
    path('vehicle-status/<int:vehicle_id>/', VehicleStatusView.as_view(), name='vehicle_status'),
]
