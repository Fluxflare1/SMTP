from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'check-upcoming-maintenance': {
        'task': 'fleet_management.tasks.check_upcoming_maintenance',
        'schedule': crontab(hour=0, minute=0),  # Daily at midnight
    },
}
