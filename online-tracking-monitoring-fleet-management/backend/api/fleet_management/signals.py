from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vehicle
from .notifications import send_vehicle_reactivation_notification

@receiver(post_save, sender=Vehicle)
def vehicle_reactivation_notification(sender, instance, **kwargs):
    if not instance.is_immobilized and instance.immobilization_reason:
        # Trigger notification only if vehicle was previously immobilized
        send_vehicle_reactivation_notification(instance)
