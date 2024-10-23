from django.urls import path
from .api.trip_scheduling import ScheduleTripView
from .api.vehicle_assignment import AssignVehicleView
from .api.route_optimization import OptimizeRouteView

urlpatterns = [
    path('schedule-trip/', ScheduleTripView.as_view(), name='schedule_trip'),
    path('assign-vehicle/', AssignVehicleView.as_view(), name='assign_vehicle'),
    path('optimize-route/', OptimizeRouteView.as_view(), name='optimize_route'),
]
