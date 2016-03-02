from .base import*

DEBUG = True

TEMPLANTE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ventas',
        'USER': 'alfred',
        'PASSWORD':'5dv4rrgq8au7',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = 'staticfiles'