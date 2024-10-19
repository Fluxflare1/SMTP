


INSTALLED_APPS = [
    # Other apps
    'channels',
]

ASGI_APPLICATION = 'tracking_monitoring.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],  # Make sure Redis is installed and running
        },
    },
}




TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Example for Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'your_email_password'  # Replace with your password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER



INSTALLED_APPS = [
    # other apps
    'channels',
]

ASGI_APPLICATION = 'tracking_monitoring.asgi.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}




# settings.py

INSTALLED_APPS = [
    # Other apps
    'tracking',
    'rest_framework',  # For API handling
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
