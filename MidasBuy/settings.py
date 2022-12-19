"""
Django settings for MidasBuy project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u%ywcq27eic)sj&*_&-4v*jwriir790b_vs3o57lx^0%0s&r3#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'rest_auth',
    'corsheaders',
    'core',
    #oauth
    'oauth2_provider',
    'social_django',
    'drf_social_oauth2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MidasBuy.urls'

REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES': (
      'rest_framework.permissions.AllowAny',
  ),
  'DEFAULT_AUTHENTICATION_CLASSES': (
    #   'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    #   'rest_framework.authentication.SessionAuthentication',
    #   'rest_framework.authentication.BasicAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'drf_social_oauth2.authentication.SocialAuthentication',
  ),
}


CORS_ALLOWED_ORIGINS = [
"https://127.0.0.1:3000", #REACT app run on port 3000
"http://localhost:3000",
]



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
                # Oauth
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'MidasBuy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'MidasBuy_DB',
        'USER': 'postgres', 
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': 5432,

    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'core.User'

AUTHENTICATION_BACKENDS = (
    'drf_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = True
