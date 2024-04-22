###########################
#----------import----------
###########################

from pathlib import Path
from dotenv import load_dotenv
import os
import MySQLdb as mydb
from sshtunnel import SSHTunnelForwarder

##############################
#----------dir_path----------
##############################

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PARENT_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_NAME = os.path.basename(BASE_DIR)

env_path = PARENT_DIR / "auth/.env"
load_dotenv(env_path)

#############################
#----------security----------
#############################

SECRET_KEY = os.environ.get("secret_key")

DEBUG = True

ALLOWED_HOSTS = []

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


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


#########################
#----------apps----------
#########################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'accounts.apps.AccountsConfig',
    'toppage.apps.ToppageConfig',
]


#########################
#----------others----------
#########################

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

AUTH_USER_MODEL = 'accounts.CustomUser'


LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = "/mypage/"

#LOGOUT_REDIRECT_URL = "accounts/logout/"


##############################
#----------templates----------
##############################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

#############################
#----------database----------
#############################

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': "kohrigaokaweb",
            'USER': "root",
            'PASSWORD': os.environ.get("password"),
            'HOST': "",
            'PORT': "3306",
    }
}

#################################
#----------static/media----------
#################################

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(PARENT_DIR, 'static')

STATICFILES_DIRS = ([os.path.join(BASE_DIR, 'static'),])

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PARENT_DIR, 'media')