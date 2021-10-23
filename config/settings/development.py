from config.settings.base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



DEBUG = env.bool("DJANGO_DEBUG")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = env("DJANGO_DEFAULT_FROM_EMAIL")
EMAIL_HOST = env("DJANGO_EMAIL_HOST")
EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_PORT = 587
