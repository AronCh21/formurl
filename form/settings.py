import os
from pathlib import Path
import django_heroku
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-cho*q3cjr-*=l-)xd(6la3basuc_xwpj@8s1$=@6esyc8t4%jb'

DEBUG = True

ALLOWED_HOSTS = ['formurl.herokuapp.com']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'form.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR, 'template' 
        ],
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

WSGI_APPLICATION = 'form.wsgi.application'



DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'd5av7kaivqu256',

        'USER': 'lrqjcuvdsqgmjz',

        'PASSWORD': 'a8cc3956f7ff5e1d9f4050e57b135af701ec335b410b0e986ecd89ede3b2e457',

        'HOST': 'ec2-3-234-204-26.compute-1.amazonaws.com',

        'PORT': '5432',

    }

}




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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(
    BASE_DIR, 'staticfiles'
)
STATICFILES_DIRS = (
    os.path.join(
        BASE_DIR, 'static'
    ),
)
django_heroku.settings(
    locals()
)



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
