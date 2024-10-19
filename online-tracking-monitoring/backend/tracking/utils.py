


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
