 
from pathlib import Path
import os
import environ
#la variable env es para guardar en otro archivo todas las contraseñas que se van a usar en el backend

env=environ.Env()
environ.Env.read_env()
 # Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#los dos siguientes paramatros es para la seguridad de la aplicacion web la primera un codigo de seguridad
#y el siguiente parametro es para ayudar a los desarolladores a desarrollar si es true aparecen errores y si es false no 
#en nuestro caso se ha guardado en la variable env donde estan las cosas sensibles
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']


#modulos/aplicaciones que estan instaladas dentro de la pagina web
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',



    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'aplicacionnweb',
    'blog',
]

#configuracion de  seguridad de la propia pagina web 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#especificamos donde estaran las rutas padres aqui se pondran las dems rutas
ROOT_URLCONF = 'aplicacionnweb.urls'
#configuracion de donde estan los templates del modulo de los usuarios 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'Templates')],
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
#configuracion del modulo de los usuarios
WSGI_APPLICATION = 'aplicacionnweb.wsgi.application'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}
#conexion a la base de datos la que se usara por defecto 
DATABASES = {
 'default': {

 'ENGINE': 'django.contrib.gis.db.backends.postgis',

 'NAME': 'PATG',

 'USER': 'PATG',

 'PASSWORD': 'PATG',

 'HOST': '127.0.0.1',

 'PORT': '5432',

 }

}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
#configuracion del modulo de los usuarios
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

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
#configuracion de otros parametros para el funcionamiento de la pagina web 
LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


