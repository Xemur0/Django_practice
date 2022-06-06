from .base import *


SECRET_KEY = 'django-insecure-&7+55x^3(h%nbw&1)9&zksoe3p6wg_!$i6r4%=ij1veqy74rf$'

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop',
        'USER': 'xemur0',
        'PASSWORD': 'qwerty123',
        'HOST': 'db',
        'PORT': '5432',
    }
}