from .settings import *

'''create settings for test environment. use in memory sqlite3 for db'''

DATABASES = {
     "default": {
         "ENGINE": "django.db.backends.sqlite3",
         "NAME": "memory"
     }
 }

# avoid sending emails to actual recepients so use locmem

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend" 

# install pytest, pytest-django git+git://github.com/mverteuil/pytest-ipdb.git
# install pytest-cov