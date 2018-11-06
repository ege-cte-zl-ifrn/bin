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

MY_APPS = env_as_list('MY_APPS', 'suap_perfil')

DEV_APPS = env_as_list('DEV_APPS', 'debug_toolbar,django_extensions' if DEBUG else '')

# THIRD_APPS = env_as_list('THIRD_APPS', 'ege_django_theme,social.apps.django_app.default')
# THIRD_APPS = env_as_list('THIRD_APPS', 'social.apps.django_app.default')
THIRD_APPS = env_as_list('THIRD_APPS', 'social_django')

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = env('DJANGO_WSGI_APPLICATION', 'wsgi.application')

DATABASES = {
    'default': {
        'ENGINE': env('POSTGRES_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'HOST': env('POSTGRES_HOST', 'db'),
        'PORT': env('POSTGRES_PORT', '5432'),
        'NAME': env('POSTGRES_DB_PERFIL', 'suap_perfil'),
        'USER': env('POSTGRES_USER', 'postgres'),
        'PASSWORD': env('POSTGRES_PASSWORD', 'postgres'),
    }
}


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

LOGIN_REDIRECT_URL = env("DJANGO_LOGIN_REDIRECT_URL", '/id/perfil')
LOGIN_URL = env("DJANGO_LOGIN_URL", '/id/perfil/login/suapsso/') 

AUTH_PASSWORD_VALIDATORS = env_as_list_of_maps('DJANGO_UTH_PASSWORD_VALIDATORS', 'NAME', '')

SUAPSSO_NAME = env('SUAPSSO_NAME', 'suapsso')
SUAPSSO_AUTHORIZATION_URL = env('SUAPSSO_AUTHORIZATION_URL', 'http://sso/id/acesso/oauth/authorize/')
SUAPSSO_ACCESS_TOKEN_METHOD = env('SUAPSSO_ACCESS_TOKEN_METHOD', 'POST')
SUAPSSO_ACCESS_TOKEN_URL = env('SUAPSSO_ACCESS_TOKEN_URL', 'http://sso/id/acesso/oauth/token/')
SUAPSSO_ID_KEY = env('SUAPSSO_ID_KEY', 'cpf')
SUAPSSO_RESPONSE_TYPE = env('SUAPSSO_RESPONSE_TYPE', 'code')
SUAPSSO_REDIRECT_STATE = env_as_bool('SUAPSSO_REDIRECT_STATE', True)
SUAPSSO_STATE_PARAMETER = env_as_bool('SUAPSSO_STATE_PARAMETER', True)
SUAPSSO_USER_DATA_URL = env('SUAPSSO_USER_DATA_URL', 'http://sso/id/acesso/api/v1/me/')

SOCIAL_AUTH_SUAPSSO_OAUTH2_KEY = env('SOCIAL_AUTH_SUAPSSO_KEY')
SOCIAL_AUTH_SUAPSSO_OAUTH2_SECRET = env('SOCIAL_AUTH_SUAPSSO_SECRET')
SOCIAL_AUTH_SUAPSSO_KEY = env('SOCIAL_AUTH_SUAPSSO_KEY')
SOCIAL_AUTH_SUAPSSO_SECRET = env('SOCIAL_AUTH_SUAPSSO_SECRET')
SOCIAL_AUTH_USER_MODEL = env('SOCIAL_AUTH_USER_MODEL', 'auth.User') 
SOCIAL_AUTH_RAISE_EXCEPTIONS = env_as_bool('SOCIAL_AUTH_RAISE_EXCEPTIONS', True)
SOCIAL_AUTH_LOGIN_REDIRECT_URL = LOGIN_REDIRECT_URL
SOCIAL_AUTH_LOGIN_URL = LOGIN_URL
SOCIAL_AUTH_LOGIN_ERROR_URL = env("SOCIAL_AUTH_LOGIN_ERROR_URL", '/id/perfil/login-error/')
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = env("SOCIAL_AUTH_DISCONNECT_REDIRECT_URL", '/id/perfil/disconnected/')
SOCIAL_AUTH_INACTIVE_USER_URL = env("SOCIAL_AUTH_INACTIVE_USER_URL", '/id/perfil/inactive-user/')
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    # 'social_core.pipeline.user.create_user',
    'suapsso.pipelines.create_or_update_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)
SOCIAL_AUTH_POSTGRES_JSONFIELD = True
# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.open_id.OpenIdAuth',
#     'social_core.backends.google.GoogleOpenId',
#     'social_core.backends.google.GoogleOAuth2',
#     'social_core.backends.google.GoogleOAuth',
#     'social_core.backends.twitter.TwitterOAuth',
#     'social_core.backends.yahoo.YahooOpenId',
#     'django.contrib.auth.backends.ModelBackend',
# )
AUTHENTICATION_BACKENDS = (
    'suapsso.backends.SuapSsoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
# SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['field1', 'field2']
# SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
# SOCIAL_AUTH_ADMIN_SEARCH_FIELDS = ['field1', 'field2']
SUAPSSO_SOCIAL_AUTH_RAISE_EXCEPTIONS = True
SOCIAL_AUTH_RAISE_EXCEPTIONS = True
RAISE_EXCEPTIONS = True
DEBUG = True

