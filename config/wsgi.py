import os
import environ
env = environ.Env()

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')import os
os.environ['DJANGO_SETTINGS_MODULE'] = env("DJANGO_SETTINGS_MODULE")


application = get_wsgi_application()
