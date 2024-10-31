from .models import User

def send_geofence_alert(user, message):
    if user.geofence_alerts:
        # Send notification only if the user has enabled it
        send_notification(user, message)
