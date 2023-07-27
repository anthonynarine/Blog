

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-84#b^94qc!w(0a74k8e%m%brqi)*899laq)j@!*a=im0_&lz#n'

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
    "corsheaders.middleware.CorsMiddleware",
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
SITE_ID = 1 

WSGI_APPLICATION = 'api.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


# ADDED.. 
SPECTACULAR_SETTINGS = {
    "TITLE": "JULIA'S BLOG",
    "DESCRIPTION": "BUILDING A BLOG FOR MY KID",
    "VERSION": "1.O.",
    "SERVICE_INCLUDE_SCHEMA": False,
}