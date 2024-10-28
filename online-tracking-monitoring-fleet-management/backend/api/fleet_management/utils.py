



from django.urls import path
from .views import TripListView, FleetIncomeReportView

urlpatterns = [
    path('trips/', TripListView.as_view(), name='trip-list'),
    path('income-report/<str:date>/', FleetIncomeReportView.as_view(), name='fleet-income-report'),
]





from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiclePerformanceViewSet, VehicleUsageViewSet

router = DefaultRouter()
router.register(r'vehicle-performance', VehiclePerformanceViewSet, basename='vehicle-performance')
router.register(r'vehicle-usage', VehicleUsageViewSet, basename='vehicle-usage')

urlpatterns = [
    path('', include(router.urls)),
]





from django.core.mail import send_mail
from django.conf import settings

def send_email_reminder(credential):
    subject = f"Reminder: Credential Expiration for {credential.credential_type}"
    message = (
        f"Dear {credential.driver.user.first_name},\n\n"
        f"Your {credential.credential_type} (ID: {credential.id}) will expire on "
        f"{credential.expiration_date}. Please take necessary actions to renew it.\n\n"
        "Best regards,\nFleet Management Team"
    )
    recipient_list = [credential.driver.user.email]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
