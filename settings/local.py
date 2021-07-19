from diplom_django_netology.settings import *

ALLOWED_HOSTS = ['127.0.0.1']

DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]
