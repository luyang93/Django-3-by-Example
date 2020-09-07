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

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 5

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

SECURE_REFERRER_POLICY = 'no-referrer'
