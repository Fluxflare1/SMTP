from django.apps import AppConfig

class FleetManagementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fleet_management"

    def ready(self):
        import fleet_management.signals  # Import signals to register them
