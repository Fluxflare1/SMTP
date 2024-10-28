


from celery import shared_task
from .tasks import driver_behavior_alert

@shared_task
def check_driver_behavior():
    driver_behavior_alert()





from celery import shared_task
from .tasks import geofence_alert

@shared_task
def check_geofence_status():
    geofence_alert()




from celery import shared_task
from .tasks import vehicle_health_alert

@shared_task
def check_vehicle_health():
    vehicle_health_alert()




from celery import shared_task
from .tasks import overdue_maintenance_alert

@shared_task
def check_overdue_maintenance():
    overdue_maintenance_alert()




from celery import shared_task
from .tasks import upcoming_maintenance_alert

@shared_task
def check_upcoming_maintenance():
    upcoming_maintenance_alert()



from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('fleet_management')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
