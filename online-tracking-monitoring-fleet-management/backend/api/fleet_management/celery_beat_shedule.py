

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
