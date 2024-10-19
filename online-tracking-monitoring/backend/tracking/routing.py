from django.urls import re_path
from .consumers import GeofenceNotificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/notifications/$', GeofenceNotificationConsumer.as_asgi()),
]
