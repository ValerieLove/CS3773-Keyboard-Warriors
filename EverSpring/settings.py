"""
Django settings for EverSpring project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# TEMP_PATH = os.path.realpath('.')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-0jp*tb!la+!eeq*5j(9t%)%j!bs%&59)3ix&w&yx(8k1ne!#0w"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# UNCOMMENT THIS WHEN PUSHING TO THE SERVER
ALLOWED_HOSTS = [
    "34.125.88.240",
    "www.everspringdesigns.tech",
    "everspringdesigns.tech",
]

# COMMENT THIS OUT WHEN DEVELOPING LOCALLY
# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "EverSpring",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "pages.apps.PagesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "EverSpring.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(BASE_DIR.joinpath("templates"))
            #"templates"
        ],  # tells django the location of the new templates directory
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "EverSpring.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# UNCOMMENT THIS WHEN PUSHING TO THE SERVER
DATABASES = {
    "default": {
       "ENGINE": "django.db.backends.mysql",
       "NAME": "project",
       "USER": "djangouser",
       "PASSWORD": "Tdizzlefizzle1!",
       "HOST": "localhost",
       "PORT": "3306",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"  # tells django to look for the static files in this directory
STATICFILES_DIRS = [str(BASE_DIR.joinpath("static"))]
# STATIC_ROOT = "/django-project/src/static/css"
STATIC_ROOT = "/django-project/site/public/static"
MEDIA_ROOT = "/django-project/site/public/media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"