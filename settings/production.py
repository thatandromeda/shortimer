"""
Production settings for shortimer.
"""

from base import *

# TODO: edsu, make this make sense for production.

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["jobs.code4lib.org"]

STATIC_ROOT = ''

# The cached loader is faster, but annoying to develop with, so it's in
# production.py but not base.py.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
