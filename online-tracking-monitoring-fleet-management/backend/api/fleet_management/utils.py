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
