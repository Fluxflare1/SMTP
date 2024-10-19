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
