from config.settings.base import *


DATABASES = {
	"default": env.db_url("DATABASE_URL")
}



DEBUG = env.bool("DJANGO_DEBUG")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


DEFAULT_FROM_EMAIL = env("DJANGO_DEFAULT_FROM_EMAIL")
EMAIL_HOST = env("DJANGO_EMAIL_HOST")
EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_PORT = 587

GOOGLE_ANALYTICS_KEY =""