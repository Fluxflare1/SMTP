


from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'send_maintenance_alerts_daily': {
        'task': 'fleet_management.tasks.send_maintenance_alerts',
        'schedule': crontab(hour=0, minute=0),
    },
}



CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Example using Redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
