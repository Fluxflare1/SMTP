from celery.schedules import crontab

app.conf.beat_schedule = {
    'trip-reminders-every-15-minutes': {
        'task': 'fleet_management.tasks.schedule_trip_notifications',
        'schedule': crontab(minute='*/15'),
    },
}
