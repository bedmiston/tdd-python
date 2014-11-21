from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(DJANGO_ROOT, 'testdb.sqlite3'),
    }
}
