



import requests
from django.conf import settings

def fetch_driver_data(vehicle_id):
    url = f'https://api.telemetryservice.com/vehicles/{vehicle_id}/data'
    headers = {'Authorization': f'Bearer {settings.TELEMETRY_API_KEY}'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def monitor_driver_advanced_behavior(vehicle_id):
    data = fetch_driver_data(vehicle_id)
    
    if data['acceleration'] > ACCELERATION_THRESHOLD:
        trigger_geofence_alert(vehicle_id, "harsh acceleration", "triggered")
    if data['braking'] > BRAKING_THRESHOLD:
        trigger_geofence_alert(vehicle_id, "harsh braking", "triggered")




from twilio.rest import Client
from django.conf import settings

def send_sms_notification(vehicle_id, geofence_name, status):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=f"Vehicle {vehicle_id} has {status} the geofence: {geofence_name}.",
        from_=settings.TWILIO_PHONE_NUMBER,
        to='+1234567890'  # Replace with actual phone number
    )
    return message.sid





from django.core.mail import send_mail
from django.conf import settings

def send_email_notification(vehicle_id, geofence_name, status):
    subject = f"Geofence Alert for Vehicle {vehicle_id}"
    message = f"Vehicle {vehicle_id} has {status} the geofence: {geofence_name}."
    recipient_list = ['recipient@example.com']  # Replace with real email addresses
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)


def monitor_driver_behavior(vehicle):
    if vehicle.acceleration > ACCELERATION_THRESHOLD:
        trigger_geofence_alert(vehicle.vehicle_id, "harsh acceleration", "triggered")
    if vehicle.braking > BRAKING_THRESHOLD:
        trigger_geofence_alert(vehicle.vehicle_id, "harsh braking", "triggered")




import time

def track_idle_time(vehicle):
    if vehicle.is_stationary:
        current_time = time.time()
        idle_duration = current_time - vehicle.last_movement_time

        if idle_duration > IDLE_TIME_THRESHOLD:
            trigger_geofence_alert(vehicle.vehicle_id, "idle time", "has exceeded idle time")




import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c  # Distance in kilometers
