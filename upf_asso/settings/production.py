from .base import *

DEBUG = False

SECRET_KEY = 's3cr3t-k3y-tr3s-longue-64-chars-changez-moi-maintenant-django-upf-asso-2026!'

# Base de données PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "upf_asso",
        "USER": "upf_asso",
        "PASSWORD": "TON_MOT_DE_PASSE_POSTGRES",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "upf_asso" / "templates",
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

STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# HTTPS Production
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['https://upf-asso.fr', 'https://www.upf-asso.fr']
ALLOWED_HOSTS = ['upf-asso.fr', 'www.upf-asso.fr', '87.106.3.191']
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

try:
    from .local import *
except ImportError:
    pass