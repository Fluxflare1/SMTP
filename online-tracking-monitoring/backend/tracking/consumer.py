

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GeofenceNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'geofence_alerts'

        # Join geofence alert group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave geofence alert group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        pass

    # Send message to WebSocket
    async def send_geofence_alert(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))




import json
from channels.generic.websocket import WebsocketConsumer

class GeofenceNotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def send_geofence_alert(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
