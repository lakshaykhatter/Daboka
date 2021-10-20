from config.settings.base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = env.bool("DJANGO_DEBUG")

CRISPY_FAIL_SILENTLY = not DEBUG 
