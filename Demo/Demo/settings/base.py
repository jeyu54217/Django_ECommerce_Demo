from pathlib import Path
import os

# Demo
BASE_DIR = Path(__file__).resolve().parent.parent.parent # settings -> Demo -> Demo (Base_Dir)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

ROOT_URLCONF = 'Demo.urls'
WSGI_APPLICATION = 'Demo.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Models - default Primary key field 

INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'orders',
    'cart',
    ### allauth ###
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # 'rest_framework',
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

### USER Authentication ###

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
# REDIRECT URL - Django auth_views
LOGIN_REDIRECT_URL = '/accounts'
LOGIN_URL = '/accounts/login'
LOGOUT_URL = '/accounts/logout'
# LOGIN_REDIRECT_URL = '/auth/logged_in'  :You're redirecting to a path that is appended to the current url. You need to use a leading slash to redirect to a path that is appended to the domain root.

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

### SESSION ###
CART_SESSION_ID = 'cart'
SESSION_COOKIE_AGE = 144000  # (s- 24 hr)
# SESSION_COOKIE_SECURE : ????????????HTTPS??????????????????cookie
# SESSION_EXPIRE_AT_BROWSER_CLOSE:?????????????????? session ???????????????
# SESSION_SAVE_EVERY_REQUEST: ????????? True?????????request ????????? session ??????????????????????????????????????? session ???????????????


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = True