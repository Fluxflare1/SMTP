import os

ALERT_EMAIL_FROM = os.getenv("ALERT_EMAIL_FROM", "alerts@fluxtrans.com")
ALERT_EMAIL_RECIPIENT = os.getenv("ALERT_EMAIL_RECIPIENT", "fleetmanager@fluxtrans.com")
EXPENSE_ALERT_THRESHOLD = float(os.getenv("EXPENSE_ALERT_THRESHOLD", 500.00))
