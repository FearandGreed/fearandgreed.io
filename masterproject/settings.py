from pathlib import Path
import os #--- after django 3.1 is no longer used
import django_heroku
import dj_database_url
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cdo2n@7)@fpaf7r)_ktl8x*v9ly5qlntvr0ey*y4bb6(mqec%q'

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
    'pages',
    'blog',
    'members',
    'ckeditor'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'masterproject.urls'

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

WSGI_APPLICATION = 'masterproject.wsgi.application'


# Database
#https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# ------------ Local Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------- Heroku Database
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#    }
#}

#DATABASES['default'] = dj_database_url.config(default='postgres://hgmxzgzwfpblmh:edfc21692556fe89e8c55058993572c850df5796e2e8be5728e9382b93b7a6ee@ec2-174-129-225-160.compute-1.amazonaws.com:5432/d6pc5vduejq10p')


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )

#STATICFILES_DIRS = [
#    BASE_DIR.joinpath('static'),
#]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'fearandgreed.io@gmail.com'
EMAIL_HOST_PASSWORD = 'Cracker70!'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesSTorage'
django_heroku.settings(locals())

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


# … Make function availabe across all templates https://betterprogramming.pub/django-quick-tips-context-processors-da74f887f1fc
TEMPLATES = [
 {
   'BACKEND': 'django.template.backends.django.DjangoTemplates',
   'DIRS': [os.path.join(BASE_DIR, 'templates')],
   'APP_DIRS': True,
   'OPTIONS': {
      'context_processors': [
      'django.template.context_processors.debug',
      'django.template.context_processors.request',
      'django.contrib.auth.context_processors.auth',
      'django.contrib.messages.context_processors.messages',
      'blog.custom_context_processor.subject_renderer'
   ],
  },
 },
]
# …