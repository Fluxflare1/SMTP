

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from tracking.views import GeofenceNotificationConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracking_monitoring.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/geofence/', GeofenceNotificationConsumer.as_asgi()),  # WebSocket URL
        ])
    ),
})




import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import tracking.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracking_monitoring.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            tracking.routing.websocket_urlpatterns
        )
    ),
})
