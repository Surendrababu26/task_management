from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv


# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(os.path.join(BASE_DIR, '.env'))


# SECURITY
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')


# CORS
CORS_ALLOW_ALL_ORIGINS = True


# INSTALLED APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'corsheaders',

    # Your app
    'backend.tasks',
]


# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # ✅ Added

    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URLS
ROOT_URLCONF = 'backend.urls'


# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],   # ✅ Updated
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# WSGI
WSGI_APPLICATION = 'backend.wsgi.application'


# DATABASES
# Priority 1: DATABASE_URL (Render/Standard)
# Priority 2: Clever Cloud MySQL variables
# Priority 3: Fallback defaults

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', ''),
        conn_max_age=600,
        ssl_require=True if os.getenv('DATABASE_URL') else False
    )
}

# If DATABASE_URL was not found or failed, try Clever Cloud variables
if not DATABASES['default'] or not DATABASES['default'].get('NAME'):
    if os.getenv('MYSQL_ADDON_HOST'):
        DATABASES['default'] = {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('MYSQL_ADDON_DB'),
            'USER': os.getenv('MYSQL_ADDON_USER'),
            'PASSWORD': os.getenv('MYSQL_ADDON_PASSWORD'),
            'HOST': os.getenv('MYSQL_ADDON_HOST'),
            'PORT': os.getenv('MYSQL_ADDON_PORT'),
            'OPTIONS': {
                'ssl': {'ssl-mode': 'REQUIRED'}
            }
        }
    else:
        # Final fallback for local development
        DATABASES['default'] = {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DB_NAME', 'db_name'),
            'USER': os.getenv('DB_USER', 'db_user'),
            'PASSWORD': os.getenv('DB_PASSWORD', ''),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '3306'),
        }

# Ensure ENGINE is always set for mysql if not already (dj-database-url handles this but just in case)
if 'mysql' in DATABASES['default'].get('ENGINE', ''):
     DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'

# PASSWORD VALIDATION
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


# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise static handling
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Render-specific security settings
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # SECURE_HSTS_SECONDS = 31536000
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURE_HSTS_PRELOAD = True