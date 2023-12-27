from pathlib import Path
import os
BASE_DIR            = Path(__file__).resolve().parent.parent
SECRET_KEY          = 'django-insecure-@imh6cz9cmj99sdj34!ce!7@k+9#emb*_^=qudukfsa&p25'
DEBUG               = True
ALLOWED_HOSTS       = ['*']
LANGUAGE_CODE       = 'en-us'
TIME_ZONE           = 'Egypt'
USE_I18N            = True
USE_L10N            = True
USE_TZ              = True
DEFAULT_AUTO_FIELD  = 'django.db.models.BigAutoField'
STATIC_URL          = '/static/'
STATIC_ROOT         = os.path.join(BASE_DIR,'RootStaticFiels')
STATICFILES_DIRS    = [os.path.join(BASE_DIR,'StatiFilesDirs')]
MEDIA_URL           = '/media/'
MEDIA_ROOT          = os.path.join(BASE_DIR, 'mediafiles')


INSTALLED_APPS = [

"jazzmin",
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'core',
'acc',


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

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'
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


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Grand aqua",  

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "grand",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Grand aqua",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "media/grabd_logo-1.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "bad",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "media/grabd_icon.png",

    # Welcome text on the login screen
    "welcome_sign": "welcome to Grand aqua system",

    # Copyright on the footer
    "copyright": "Omar Hosny AbdElmotaleb|omarhosnay09@gmail.com",
    "custom_css": "css/main.css",
    # "custom_js": "common/js/main.js"
    "search_model" : ['core.zabon', "core.Warehouse", "core.Products"]
    }



# JAZZMIN_SETTINGS["show_ui_builder"] = True


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-white",
    "accent": "accent-primary",
    "navbar": "navbar-info navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-primary",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}
# "order_with_respect_to" : ['core.modelname', ...]