from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-c-w4tai3cz_z8yavk(-2lo7#2^yj67j+)1b*%m=1o@0vm9mcod"

DEBUG = True

ALLOWED_HOSTS = []

CORS_ALLOWED_ORIGINS = ("http://localhost:3000",)

AUTH_USER_MODEL = "user_credentials.UserCredentials"

THIRD_PARTY_APPS = [
    "cities_light",
]

CUSTOM_APPS = [
    "drf_react_gems_backend.user_credentials",
    "drf_react_gems_backend.user_profile",
    "drf_react_gems_backend.product",
    "drf_react_gems_backend.inventory",
]

INSTALLED_APPS = (
    [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "rest_framework",
        "rest_framework.authtoken",
        "corsheaders",
    ]
    + THIRD_PARTY_APPS
    + CUSTOM_APPS
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ]
}

ROOT_URLCONF = "drf_react_gems_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "drf_react_gems_backend.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "drf_react_gems_db",
        "USER": "postgres",
        "PASSWORD": "S@3ana3a",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STRIPE_SECRET_KEY = "sk_test_51QTRGcAlmA9HkGjCXN0PDgsUwk1wg9wAZgvHo1VCEZ8UXooIOEar92iUoZwnabYpfRcf5QrlvXCeyrl6QzrEb9ZH00fACp4k26"
STRIPE_PUBLISHABLE_KEY = "pk_test_51QTRGcAlmA9HkGjCAEAcWsWRIwdtKF6BI8JFMafi1ULDhB267bzyaCC0zUWwJ7raKrZ3PFfpC3jkFzFeMvkHeazz00oPIvWG4m"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        }
    },
}
