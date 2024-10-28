from .models import Invoice
from .notifications import send_invoice_overdue_notification

def send_overdue_invoice_alerts():
    overdue_invoices = Invoice.objects.filter(status="overdue")
    for invoice in overdue_invoices:
        send_invoice_overdue_notification(invoice)
