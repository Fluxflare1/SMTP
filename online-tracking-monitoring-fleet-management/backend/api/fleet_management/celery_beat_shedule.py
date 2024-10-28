



from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'check-fuel-usage': {
        'task': 'fleet_management.tasks.check_fuel_usage',
        'schedule': crontab(minute=0, hour='*/1'),  # Every hour
    },
}




from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'check-driver-behavior': {
        'task': 'fleet_management.tasks.check_driver_behavior',
        'schedule': crontab(minute='*/5'),  # Every 5 minutes
    },
}




from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'check-geofence-status': {
        'task': 'fleet_management.tasks.check_geofence_status',
        'schedule': crontab(minute='*/5'),  # Every 5 minutes
    },
}





from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'check-vehicle-health': {
        'task': 'fleet_management.tasks.check_vehicle_health',
        'schedule': crontab(hour=1, minute=0),  # Daily at 1 AM
    },
}




from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'check-overdue-maintenance': {
        'task': 'fleet_management.tasks.check_overdue_maintenance',
        'schedule': crontab(hour=0, minute=0),  # Daily at midnight
    },
}




from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'check-upcoming-maintenance': {
        'task': 'fleet_management.tasks.check_upcoming_maintenance',
        'schedule': crontab(hour=0, minute=0),  # Daily at midnight
    },
}
