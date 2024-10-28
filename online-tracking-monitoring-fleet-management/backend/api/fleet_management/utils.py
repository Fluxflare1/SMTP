

# Path: backend/api/fleet_management/utils.py

from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Invoice

def generate_invoice_pdf(invoice: Invoice) -> BytesIO:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.drawString(100, 750, f"Invoice #{invoice.id}")
    pdf.drawString(100, 730, f"Client: {invoice.client.username}")
    pdf.drawString(100, 710, f"Issued Date: {invoice.issued_date}")
    pdf.drawString(100, 690, f"Due Date: {invoice.due_date}")
    pdf.drawString(100, 670, f"Amount: ${invoice.amount}")
    pdf.drawString(100, 650, f"Status: {invoice.status}")
    pdf.drawString(100, 630, f"Description: {invoice.description}")
    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer






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
