






import requests
from django.conf import settings

def get_optimized_route(origin, destination, waypoints=None):
    """
    Fetch optimized route from external service.
    :param origin: Starting point (latitude, longitude)
    :param destination: Ending point (latitude, longitude)
    :param waypoints: Optional list of waypoints for the route
    :return: Optimized route data
    """
    api_key = settings.ROUTE_OPTIMIZATION_API_KEY
    url = "https://maps.googleapis.com/maps/api/directions/json"  # Google Maps API endpoint
    params = {
        'origin': f"{origin[0]},{origin[1]}",
        'destination': f"{destination[0]},{destination[1]}",
        'waypoints': '|'.join([f"{wp[0]},{wp[1]}" for wp in waypoints]) if waypoints else None,
        'key': api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()






# Path: backend/api/fleet_management/utils.py

from django.core.mail import EmailMessage

def send_invoice_email(invoice: Invoice, pdf_buffer: BytesIO):
    email = EmailMessage(
        subject=f"Invoice #{invoice.id} - {invoice.client.username}",
        body=f"Dear {invoice.client.username},\n\nPlease find attached your invoice.",
        to=[invoice.client.email],
    )
    email.attach(f"invoice_{invoice.id}.pdf", pdf_buffer.getvalue(), "application/pdf")
    email.send()







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
