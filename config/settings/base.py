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

#BASE_DIR = Path(__file__).resolve().parent.parent
#PARENT_DIR = Path(__file__).resolve().parent.parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PARENT_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_NAME = os.path.basename(BASE_DIR)

env_path = PARENT_DIR / "auth/.env"
load_dotenv(env_path)


#############################
#----------security----------
#############################

SECRET_KEY = os.environ.get("secret_key")

DEBUG = os.environ.get("DEBUG")

ALLOWED_HOSTS = [os.environ.get("allowed_hosts")]

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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#SECURE_SSL_REDIRECT = False


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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


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

port_num = 10022  # エックスサーバーではデフォルトでポート番号が10022に設定されている
key_path = os.environ.get("keypath")

ssh_tunnel = SSHTunnelForwarder(
	 (os.environ.get("server_id"), port_num),
	 ssh_username= os.environ.get("ssh_username"),
	 ssh_password= os.environ.get("ssh_password"),
     ssh_pkey=key_path,
	 remote_bind_address=('127.0.0.1', 3306),
)
 
ssh_tunnel.start()

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get("name"),
            'USER': os.environ.get("user"),
            'PASSWORD': os.environ.get("password"),
            'HOST': "127.0.0.1",
            'PORT': ssh_tunnel.local_bind_port,
            'OPTIONS':{
                'init_command':"SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


#################################
#----------static/media----------
#################################

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PARENT_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PARENT_DIR, 'media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]







