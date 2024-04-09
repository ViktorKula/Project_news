"""
Django settings for NewsPaper01 project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
import logging
import logging.config
from django.conf import settings


logger = logging.getLogger('Project_news.NewsPaper.NewsPaper01')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_c5r9)wzf!%72&c!ox+_ngvj_7a956z)s56i*fc^^v4@%5ly9c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'fpages',
    'news.apps.NewsConfig',
    'accounts',

    'django_filters',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',

    "django_apscheduler",
]

SITE_ID = 1
SITE_URL = 'http://127.0.0.1:8000'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Указали форму для дополнительной обработки регистрации пользователя
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

LOGIN_REDIRECT_URL = "/news"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "info.news.portal"
EMAIL_HOST_PASSWORD = "uirnduztnftjaxuf"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "info.news.portal@yandex.ru"

SERVER_EMAIL = "info.news.portal@yandex.ru"

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

ADMINS = (
    ('NP', 'info.news.portal@yandex.ru'),
)

MANAGERS = (
    ('Vic', 'vicyru@yandex.ru'),
)


# SOCIALACCOUNT_PROVIDERS = {
#     'yandex': {
#
#         'APP': {
#             'client_id': '123',
#             'secret': '123',
#             'key': ''
#         }
#     }
# }

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        # Указываем, куда будем сохранять кэшируемые файлы!
        # Не забываем создать папку cache_files внутри папки с manage.py!
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'NewsPaper01.urls'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # `allauth` обязательно нужен этот процессор
                'django.template.context_processors.request',
            ],
        },
    },
]

# Этого раздела может не быть, добавьте его в указанном виде.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'NewsPaper01.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '1111',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_debug',
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning',
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'file_and_console_error',
        },

        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'logs/general.log',
            'formatter': 'file_info',
        },
        'file_errors': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': 'logs/errors.log',
            'formatter': 'file_and_console_error',
        },
        'file_security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/security.log',
            'formatter': 'file_info',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'console_warning',
        },
    },
    'loggers': {
        'django': {
            'handlers': [
                'console_debug',
                'console_warning',
                'console_error',
                'file_general',
            ],
            'level': 'DEBUG'
        },
        'django.request': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['file_security', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
        },
    },


    'formatters': {
        'console_debug': {
            'format': '[{asctime}] {levelname} - "{message}"',
            'datefmt': '%d/%b/%Y %H:%M:%S',
            'style': '{',
        },
        'console_warning': {
            'format': '[{asctime}] {levelname} - pathname: "{pathname}" - "{message}"',
            'datefmt': '%d/%b/%Y %H:%M:%S',
            'level': 'WARNING',
            'style': '{',
        },
        'file_and_console_error': {
            'format': '[{asctime}] {levelname} - pathname: "{pathname}" - "{message}" :: {exc_info}',
            'datefmt': '%d/%b/%Y %H:%M:%S',
            'level': 'ERROR',
            'style': '{',
        },
        'file_info': {
            'format': '{asctime} - {levelname} - {module}: {message}',
            'datefmt': '%d/%b/%Y %H:%M:%S',
            'level': 'INFO',
            'style': '{',
        }
    },
}
