

from pathlib import Path
import os
from environs import Env

# ..ADDED..
env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic", # ADDED....
    'django.contrib.staticfiles',
    #local
    'accounts',
    'post',
    # 3rd party
    'rest_framework',
    "corsheaders",
    "drf_spectacular",
    # 3rd party for user registration
    'allauth',
    'allauth.account',
    "dj_rest_auth", 
    'django.contrib.sites',
    'allauth.socialaccount',
    "rest_framework.authtoken",
    'dj_rest_auth.registration',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", # ADDED...
    "corsheaders.middleware.CorsMiddleware",      # ADDED..
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

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
                "django.template.context_processors.request", # ADDED... FOR USER REG
            ],
        },
    },
]

# ADDED.............
# NEEDED SINCE BY DEFAULT AN EMAIL WIL BE SENT WHEN A NEW USER IS REGISTERED
# ASKING THEM TO CONFIRM THEIR ACCOUNT. THIS PROJECT WILL OUTPUT THE EMAIL TO THE CONSOLE
# RATHER THAN SET UP AND EMAIL SERVER. 
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ADDED.....
# SITE ID IS PART OF DJANGO'S BUILT IN SITES FRAMEWORK WHICH IS A WAY TO HOST MULTIPLE   WEBSITES FROM THE SAME DJANGO PROJECT. WE ONLY HAVE 1 BUT django-allauth USES THE SITES FRAMEWORK SO WE MUST SPECIFY A DEFAULT SETTING. 
SITE_ID = 1   # ADDED...

WSGI_APPLICATION = 'api.wsgi.application'


# ADDED...
# DATABASES = {
#     'default': env.dj_db_url("DATABASE_URL")  
    
# }

# DATABASES = {
#     'default': dj_database_url.config()
# }
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
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

# ADDED...
STATICFILES_DIRS = [str(BASE_DIR.joinpath("static"))]
STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#.. ADDED
AUTH_USER_MODEL = "accounts.CustomUser"

#.. ADDED
REST_FRAMEWORK = { 
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
#SESSION AUTH IS USED TO POWER THE BROWSABLE API AND THE ABILITY TO LOG IN AND OUT
        'rest_framework.authentication.SessionAuthentication',
#TOKEN AUTH IS USED TO PASS THE TOKEN BACK AND FORTH IN THE HTTP HEADERS FOR THE API ITSELF
        'rest_framework.authentication.TokenAuthentication',

    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema", 
}

# ADDED..
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000"
]

# ADDED..   
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:3000",
]


# ADDED...
SPECTACULAR_SETTINGS = {
    "TITLE": "Blog API Project",
    "DESCRIPTION": "Building a Blog API to learn DRF.",
    "VERSION": "1.O.",
    "SERVICE_INCLUDE_SCHEMA": True,
}


# ADDED...
ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]