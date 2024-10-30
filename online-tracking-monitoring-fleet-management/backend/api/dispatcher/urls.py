from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet, TripStatusViewSet

router = DefaultRouter()
router.register(r'trips', TripViewSet)
router.register(r'trip-status', TripStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
