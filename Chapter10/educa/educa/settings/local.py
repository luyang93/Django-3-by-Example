from .base import *

DEBUG = True

ALLOWED_HOSTS = ['.resyz.tk']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'singleron',
        'PASSWORD': 'singleron',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}
