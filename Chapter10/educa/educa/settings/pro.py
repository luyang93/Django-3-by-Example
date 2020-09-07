from .base import *

DEBUG = False

ADMINS = (
    ('luyang', '510426762@qq.com'),
)

ALLOWED_HOSTS = ['*']

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

SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True
