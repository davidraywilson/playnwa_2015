import logging
import os

logging.log(logging.INFO, 'loading settings for ' + __name__)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = BASE_DIR

DEVELOPMENT = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't8%+b87azv!0)#)bc^x!1h*m(ar#z7flxls!r6mu*+pj6n_q!4'

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['*', ]

SITE_ID = 1

# EMAIL SETTINGS
EMAILTO = 'davidw@playnwa.com'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'play_info'
EMAIL_HOST_PASSWORD = 'Redhawks234'
EMAIL_PORT = '25'
DEFAULT_FROM_EMAIL = "the playnwa team <info@playnwa.com>"
SERVER_EMAIL = "davidw@playnwa.com"
ONLINE_CONTACT_EMAIL = 'davidw@playnwa.com'

# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # 3rd Party Applications
    'filebrowser',
    'suit',
    'django.contrib.admin',
    'reversion',
    'classytags',
    'front',
    'mptt',
    # My Applications
    'contact',
    'home_content',
    'navigation',
    'page_content',
    'webapp',
    'webapp_admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'webapp.urls'

WSGI_APPLICATION = 'webapp.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_UPLOAD_PATH = os.path.join(MEDIA_ROOT, '/media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

FILE_UPLOAD_PERMISSIONS = 0644

SESSION_COOKIE_AGE = 3600
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(filename)s %(funcName)s %(lineno)d %(message)s'
        },
        'normal': {
            'format': '%(levelname)s %(asctime)s %(funcName)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'webapp': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
    }
}

SUIT_CONFIG = {
    'ADMIN_NAME': 'playnwa',
    'HEADER_DATE_FORMAT': 'l, F jS, Y',
    'HEADER_TIME_FORMAT': 'h:i a',
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True,  # Default True
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True,  # Default True
    'MENU': (
        {'app': 'auth', 'label': 'Administration', 'icon': 'icon-lock', 'models': ('user', 'group')},
        {'app': 'navigation', 'icon': 'icon-list'},
        {'app': 'home_content', 'label': 'Home Content', 'icon': 'icon-file', 'models': ('homesection', 'billboard', 'minibillboard')},
        {'app': 'page_content', 'label': 'Page Content', 'icon': 'icon-file', 'models': ('logo', 'footer', 'webpage')},
        {'app': 'contact', 'icon': 'icon-user'},
        {'label': 'Site Media', 'icon': 'icon-picture', 'url': '/admin/filebrowser/browse/'},
        'sites',
    ),
    'LIST_PER_PAGE': 30
}

FILEBROWSER_SUIT_TEMPLATE = True

DJANGO_FRONT_KEY = ']Xav5XjYw35W*>743+jk@4-=dGT85)~t'
DJANGO_FRONT_EDIT_MODE = 'inline'
DJANGO_FRONT_EDITOR_OPTIONS = {
    'filebrowserBrowseUrl': '/admin/filebrowser/browse/?pop=3'
}
