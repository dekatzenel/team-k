DEBUG = True
''' Global debug level. Should be set to False in production environments. '''

TEMPLATE_DEBUG = DEBUG
''' Template debug level. Should be set to False in production environments. '''

ADMINS = (
    ('admin', 'admin@localhost.com'),
)
''' Tuple of admin names and email addresses. '''

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'NAME': '/var/local/db/sqlite.db',
        'ENGINE': 'django.db.backends.sqlite3',
        'USER': '',
        'PASSWORD': ''
    },
    # PostgreSQL
    #'default': {
    #    'NAME': 'mds',
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'USER': 'mds',
    #    'PASSWORD': 'SanaM0b1l3',
    #    'HOST': 'localhost',
    #    'PORT': '',
    #},
}
""" Database configuration:
    NAME: 'app_label' or path to database file if using sqlite3.
    ENGINE: 'django.db.backends' + one of:
            'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3', 'oracle'.
    USER: Not used with sqlite3.
    PASSWORD: Not used with sqlite3.
    HOST: Set to empty string for localhost. Not used with sqlite3.
    PORT: Set to empty string for default. Not used with sqlite3.
    
    The default path to      
"""


TIME_ZONE = 'America/New_York'
"""Local time zone for this installation. Choices can be found here:

    http://en.wikipedia.org/wiki/List_of_tz_zones_by_name

although not all choices may be available on all operating systems.
If running in a Windows environment this must be set to the same as your
system time zone.
"""

LANGUAGE_CODE = 'en-us'
"""Language code for this installation. All choices can be found here:

    http://www.i18nguy.com/unicode/language-identifiers.html
"""

SITE_ID = 1
"""Don't touch this unless you know what you are doing."""

SITE_ROOT = ""

USE_I18N = True
"""If you set this to False, Django will make some optimizations so as not to 
load the internationalization machinery."""

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)
"""List of callables that know how to import templates from various sources."""

MEDIA_ROOT = '/var/local/www/wsgi/media/'
"""Absolute path to the directory that holds media. For a typical Sana 
deployment use: "/opt/sana/media/"
"""

MEDIA_URL = SITE_ROOT + '/mds/media/'
"""URL that handles the media served from MEDIA_ROOT. Make sure to use a
trailing slash if there is a path component (optional in other cases). For a 
typical Sana deployment use: "/mds/media/". """

STATIC_URL = SITE_ROOT+"/mds/static/"
STATIC_ROOT = '/var/local/www/wsgi/static/'
"""Absolute path to the directory that holds static media. For a typical Sana 
deployment use: "/var/local/www/wsgi/static/" """

ADMIN_MEDIA_PREFIX = SITE_ROOT+"/mds/static/admin/"
"""URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
trailing slash. Examples: "http://foo.com/media/", "/media/".
"""

SECRET_KEY = 'b#%x46e0f=jx%_#-a9b5(4bvxlfz-obm*gs4iu3i6k!034j(mx'
"""Make this unique, and don't share it with anybody. Seriously."""


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'mds.api.contrib.middleware.LoggingMiddleware',
)
"""Don't touch this unless you know what you are doing."""

ROOT_URLCONF = 'mds.urls'
"""Don't touch this unless you know what you are doing."""

TEMPLATE_DIRS = (
        '/var/local/www/mds/templates',
)
"""Put strings here, like "/home/html/django_templates" or 
"C:/www/django/templates". Always use forward slashes, even on Windows. Don't 
forget to use absolute paths, not relative paths.For a typical Sana 
deployment use: "/var/local/www/mds/templates"."""

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'django_extensions',
    'mds.core',       
    'mds.mrs',
    'mds.tasks',
    'mds.clients', 
    'gmapi',
)
"""Don't touch this unless you know what you are doing."""

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

FIXTURE_DIRS = (
    '/var/local/www/mds/fixtures'
)

try:
    from local_settings import *
except ImportError, exp:
    pass
