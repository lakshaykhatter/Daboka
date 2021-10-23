from config.settings.base import *

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


DEFAULT_FROM_EMAIL = "no_replay@daboka.com"
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'sendgrid_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

