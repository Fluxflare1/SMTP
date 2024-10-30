




LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'fleet_management.log',
        },
    },
    'loggers': {
        'fleet_management': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}



import os
VEHICLE_IMMOBILIZATION_API_URL = os.getenv("VEHICLE_IMMOBILIZATION_API_URL")
VEHICLE_IMMOBILIZATION_API_KEY = os.getenv("VEHICLE_IMMOBILIZATION_API_KEY")



import os
ROUTE_OPTIMIZATION_API_KEY = os.getenv("ROUTE_OPTIMIZATION_API_KEY")
