from .base import*


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'arenera2',
        'USER': 'root',
        'PASSWORD': 'Dedlr2406!',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


STATIC_URL = 'static/'