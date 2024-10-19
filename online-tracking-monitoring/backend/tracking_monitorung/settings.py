


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
