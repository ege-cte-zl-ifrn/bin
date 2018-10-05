"""
The MIT License (MIT)

Copyright 2015 Umbrella Tech.
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import os
import json
from python_brfied.env import env, env_as_bool, env_as_list, env_as_list_of_maps, env_as_int, env_from_json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = env('DJANGO_SECRET_KEY', 'changeme')
DEBUG = env_as_bool('DJANGO_DEBUG', True)
ALLOWED_HOSTS = env_as_list('DJANGO_ALLOWED_HOSTS', '*' if DEBUG else '')

URL_PATH_PREFIX = env('URL_PATH_PREFIX', 'id/perfil/')

MY_APPS = env_as_list('MY_APPS', 'suap_id')

DEV_APPS = env_as_list('DEV_APPS', 'debug_toolbar,django_extensions' if DEBUG else '')

THIRD_APPS = env_as_list('THIRD_APPS', 'ege_django_theme,social.apps.django_app.default')

DJANGO_APPS = env_as_list('DJANGO_APPS', 'django.contrib.admin,'
                                         'django.contrib.auth,'
                                         'django.contrib.contenttypes,'
                                         'django.contrib.sessions,'
                                         'django.contrib.messages,'
                                         'django.contrib.staticfiles')

INSTALLED_APPS = MY_APPS + THIRD_APPS + DEV_APPS + DJANGO_APPS


MIDDLEWARE = env_as_list('MIDDLEWARE', 'django.middleware.security.SecurityMiddleware,'
                                       'django.contrib.sessions.middleware.SessionMiddleware,'
                                       'django.middleware.common.CommonMiddleware,'
                                       'django.middleware.csrf.CsrfViewMiddleware,'
                                       'django.contrib.auth.middleware.AuthenticationMiddleware,'
                                       'django.contrib.messages.middleware.MessageMiddleware,'
                                       'django.middleware.clickjacking.XFrameOptionsMiddleware,'
                                       'social_django.middleware.SocialAuthExceptionMiddleware')
if DEBUG:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

ROOT_URLCONF = env('DJANGO_ROOT_URLCONF', 'urls')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = env('DJANGO_WSGI_APPLICATION', 'wsgi.application')

DATABASES = {
    'default': {
        'ENGINE': env('POSTGRES_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'HOST': env('POSTGRES_HOST_ID', 'db_id'),
        'PORT': env('POSTGRES_PORT', '5432'),
        'NAME': env('POSTGRES_DB_ID', 'postgres'),
        'USER': env('POSTGRES_USER', 'postgres'),
        'PASSWORD': env('POSTGRES_PASSWORD', 'postgres'),
    }
}

# AUTHENTICATION_BACKENDS = env_as_list('AUTHENTICATION_BACKENDS', 'oauth2_provider.backends.OAuth2Backend')
AUTHENTICATION_BACKENDS = env_as_list('DJANGO_AUTHENTICATION_BACKENDS', 'ifrnid.backends.IfrnIdOAuth2')

LOGIN_REDIRECT_URL = env("DJANGO_LOGIN_REDIRECT_URL", 'http://sso/id/perfil')
LOGIN_URL = '/id/perfil/login/ifrnid/'

AUTH_PASSWORD_VALIDATORS = env_as_list_of_maps('DJANGO_UTH_PASSWORD_VALIDATORS', 'NAME', '')

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'ifrnid.pipelines.create_or_update_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.debug.debug',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social.pipeline.debug.debug',
)

SOCIAL_AUTH_IFRNID_KEY = env('SOCIAL_AUTH_IFRNID_KEY')
SOCIAL_AUTH_IFRNID_SECRET = env('SOCIAL_AUTH_IFRNID_KEY')


LANGUAGE_CODE = env('DJANGO_USE_I18N', 'pt-br')
TIME_ZONE = env('DJANGO_USE_I18N', 'UTC')
USE_I18N = env_as_bool('DJANGO_USE_I18N', True)
USE_L10N = env_as_bool('DJANGO_USE_L10N', True)
USE_TZ = env_as_bool('DJANGO_USE_TZ', True)

STATIC_URL = "/%s%s" % (URL_PATH_PREFIX, env('DJANGO_STATIC_URL', 'static/'))
STATIC_ROOT = "/static"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler', 'formatter': 'console'}},
    'formatters': {'console': {'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}},
    'loggers': {
        '': {'handlers': ['console'], 'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG')},
    },
}

USE_X_FORWARDED_HOST = True

CORS_ORIGIN_ALLOW_ALL = True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: 'localhost' in request.get_host() or '127.0.0.1' in request.get_host() or 'sso' in request.get_host(),
}
