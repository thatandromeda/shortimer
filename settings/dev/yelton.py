"""
Personal shortimer settings file for Andromeda Yelton.

Feel free to pillage this for your own settings files!
"""
from ..base import *

# Needed to allow admin user to log in to /admin, which in turn allows for
# testing of login-required pages without setting up apps for socialauth. See
# https://github.com/omab/django-social-auth/issues/154 .
AUTHENTICATION_BACKENDS += (
    'django.contrib.auth.backends.ModelBackend',
)
