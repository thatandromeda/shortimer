"""
Django shared settings for the shortimer project.

You must set a SECRET_KEY environment variable.  You will probably want to set
at least some of the environment variables referenced under Social auth and
Misc credentials. You probably do not need to override anything else. If you
do, you should override that in your personal settings file in
`settings/dev/yourfile.py` and make sure that your DJANGO_SETTINGS_MODULE
points to that file.
"""

import os

from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(PROJECT_DIR, ...)
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(SETTINGS_DIR, '..')
LOG_DIR = os.path.join(PROJECT_DIR, "logs")

def get_env_requirement(var_name):
    """
    Get the environment variable or return exception. Use this for variables
    that are required for the project to run.
    """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Could not find the environment variable %s" % var_name
        raise ImproperlyConfigured(error_msg)

def get_env_variable(var_name):
    """
    Get the environment variable or don't. Use only for optional settings.
    """
    try:
        return os.environ[var_name]
    except KeyError:
        pass


###############################################################################
#
# Misc yaks
#
###############################################################################

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

# This is insecure and should be overridden in production.py and other servers.
ALLOWED_HOSTS = ["*"]

SITE_ID = 1

SECRET_KEY = get_env_requirement('SECRET_KEY')

USE_THOUSAND_SEPARATOR = True

JOB_FEEDS = [
    'http://joblist.ala.org/news/',
    'http://archivesgig.wordpress.com/feed/',
    'http://feeds.feedburner.com/alljobs',
    'http://digital-scholarship.org/digitalkoans/category/digital-library-jobs/feed/',
    'http://www.higheredjobs.com/rss/categoryFeed.cfm?catID=34',
    'http://www.museumsandtheweb.com/jobs-available-and-wanted/feed/'
    'http://jobs.educause.edu/jobs?keywords=library&resultsPerPage=12&noStem=false&titlesOnly=false&salary_open=false&showMoreOptions=false&display=rss',
    'http://careers.archivists.org/jobs?resultsPerPage=12&display=rss'
    'http://www.libraryjobline.org/rss',
    'http://pipes.yahoo.com/arljobstorss/c8f6fa1c3aa9c60d39bc01a35e899fa5?_render=rss'
]


###############################################################################
#
# Application definition
#
###############################################################################

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'social_auth',
    'south',
    'shortimer.jobs',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'shortimer.urls'

#this might need to be set
#WSGI_APPLICATION = 'librarycloud.wsgi.application'


###############################################################################
#
# Databases
#
###############################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'jobs.db'),
        'USER': '',        # Not used with sqlite3.
        'PASSWORD': '',    # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}


###############################################################################
#
# Internationalization
#
###############################################################################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = False
DATETIME_FORMAT = 'Y-m-d H:i:s T'

# This was unset in a prior version of shortimer. That version of Django
# defaulted USE_TZ to False; we're setting it here because explicit is
# better than implicit.
USE_TZ = False


###############################################################################
#
# Static files
#
###############################################################################

STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MEDIA_ROOT = ''

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/static/admin/'


###############################################################################
#
# Templates
#
###############################################################################

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)


###############################################################################
#
# Authentication
#
###############################################################################

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.github.GithubBackend',
)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'


###############################################################################
#
# Logging
#
###############################################################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'pop': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_DIR, 'pop.log')
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'shortimer.jobs.management.commands.pop': {
            'handlers': ['pop'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}


###############################################################################
#
# Social auth
#
###############################################################################

TWITTER_CONSUMER_KEY = get_env_variable('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = get_env_variable('TWITTER_CONSUMER_SECRET')
TWITTER_EXTRA_DATA = [('profile_image_url', 'profile_image_url')]

FACEBOOK_APP_ID = get_env_variable('FACEBOOK_APP_ID')
FACEBOOK_API_SECRET = get_env_variable('FACEBOOK_API_SECRET')

LINKEDIN_CONSUMER_KEY = get_env_variable('LINKEDIN_CONSUMER_KEY')
LINKEDIN_CONSUMER_SECRET = get_env_variable('LINKEDIN_CONSUMER_SECRET')

GITHUB_APP_ID = get_env_variable('GITHUB_APP_ID')
GITHUB_API_SECRET = get_env_variable('GITHUB_API_SECRET')

GOOGLE_CONSUMER_KEY = get_env_variable('GOOGLE_CONSUMER_KEY')
GOOGLE_CONSUMER_SECRET = get_env_variable('GOOGLE_CONSUMER_SECRET')
GOOGLE_DISPLAY_NAME = get_env_variable('GOOGLE_DISPLAY_NAME')
GOOGLE_API_KEY = get_env_variable('GOOGLE_API_KEY') # for freebase suggest


###############################################################################
#
# Misc credentials
#
###############################################################################

# Protip: don't recycle these passwords.

# Credentials for the code4lib twitter account, to tweet new job postings.

CODE4LIB_TWITTER_OAUTH_CONSUMER_KEY = \
    get_env_variable('CODE4LIB_TWITTER_OAUTH_CONSUMER_KEY')
CODE4LIB_TWITTER_OAUTH_CONSUMER_SECRET = \
    get_env_variable('CODE4LIB_TWITTER_OAUTH_CONSUMER_SECRET')
CODE4LIB_TWITTER_OAUTH_ACCESS_TOKEN_KEY = \
    get_env_variable('CODE4LIB_TWITTER_OAUTH_ACCESS_TOKEN_KEY')
CODE4LIB_TWITTER_OAUTH_ACCESS_TOKEN_SECRET = \
    get_env_variable('CODE4LIB_TWITTER_OAUTH_ACCESS_TOKEN_SECRET')

# bit.ly credentials for shortening job urls.

BITLY_USERNAME = get_env_variable('BITLY_USERNAME')
BITLY_PASSWORD = get_env_variable('BITLY_PASSWORD')

GA_USERNAME = get_env_variable('GA_USERNAME')
GA_PASSWORD = get_env_variable('GA_PASSWORD')
GA_PROFILE_ID = get_env_variable('GA_PROFILE_ID')

# Email account to pop for new job emails, and sending out new emails.

EMAIL_HOST = 'pop.gmail.com'
EMAIL_PORT = 587
EMAIL_POP_PORT = 995
EMAIL_HOST_USER = 'jobs4lib@gmail.com'
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_ANNOUNCE = ['you@example.com', 'me@example.com']

