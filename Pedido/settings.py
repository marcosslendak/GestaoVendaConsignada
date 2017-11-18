"""
Django settings for Pedido project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
#import pygraphviz
from decouple import config
#from unipath import Path
from dj_database_url import parse as dburl


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf.global_settings import MANAGERS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Antônio Marcos Krug Slendak', 'marcos.slendak@gmail.com'),
)
MANAGERS = ADMINS

#SEND_BRO

ALLOWED_HOSTS = ['gestao-venda-consignada.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'suit',
    #'grappelli',
#    'django_extensions',
    #'djando-dia',
#    'localflavor',
#    'phonenumber_field',
#    'input_mask',
#    'ajax_select',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DjPedido.apps.DjpedidoConfig',
    'report_builder',
    'mathfilters',
    'django.contrib.humanize',
#    'admin_reports',
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

ROOT_URLCONF = 'Pedido.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'Pedido.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = { 'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-br'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

#USE_L10N = True
#USE_TZ = True

# Date format
DATE_INPUT_FORMATS = ('%d/%m/%Y', )
DATE_FORMAT = 'd/m/Y'
SHORT_DATE_FORMAT = 'd/m/Y'
DATETIME_FORMAT = 'j N Y, H:i'
SHORT_DATETIME_FORMAT = 'j N Y, H:i'

USE_THOUSAND_SEPARATOR = True

SUIT_CONFIG = {
    # header
     'ADMIN_NAME': 'Gestão de Venda Consignada',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'DJpedido': 'icon-leaf',
    #    'Clientes': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': False, # Default True
    # 'MENU_EXCLUDE': ('auth.group', 'auth'),
       'MENU': (
           'sites',
           {'app': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
           '-',
           {'label': u'Cadastros', 'icon': 'icon-edit', 'models': (
               {'label': u'Itens', 'icon': 'icon-edit', 'url': '/admin/DjPedido/item/'},
               '-',
                   {'label': u'Colaboradores', 'icon': 'icon-edit', 'url': '/admin/DjPedido/colaborador/'},
               '-',
                   {'label': u'Supervisores', 'icon': 'icon-edit', 'url': '/admin/DjPedido/supervisor/'},
                   {'label': u'Vendedores', 'icon': 'icon-edit', 'url': '/admin/DjPedido/vendedor/'},

           )},
           '-',
           {'label': u'Pedido', 'icon': 'icon-share', 'models': (
               {'label': u'Solicitação', 'icon': 'icon-share', 'url': '/admin/DjPedido/pedidosolicitacao/'},
               {'label': u'Devolução', 'icon': 'icon-share', 'url': '/admin/DjPedido/pedidodevolucao/'},
           )},
           '-',
           {'label': 'Relatórios', 'icon': 'icon-th-list', 'models': (
               {'label': u'Lista pedidos em solicitação', 'icon': 'icon-th-list', 'url': '/listPedidosSolicitacao'},
               {'label': u'Lista pedidos em devolução', 'icon': 'icon-th-list', 'url': '/listPedidosDevolucao'},
               {'label': u'Lista pedidos já fechado', 'icon': 'icon-th-list', 'url': '/listPedidosFechado'},
           )},


       ),


#icon-keyboard
#icon-lock

     'LIST_PER_PAGE': 15
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

#STATIC_URL = '/static/'
STATIC_URL = '/assets/'


STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles'))
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets")
]
