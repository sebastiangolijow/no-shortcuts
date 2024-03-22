from .base import *  # noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="LC-vloE4Oq_Dq_7WQMpebMQdLIpVGbmD_HyyFBSKtKx9iL_F6-s"
)

DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

ALLOWED_HOSTS = ["*"]
DOMAIN_NAME = "http://localhost:8000"

EMAIL_BACKEND = "djcelery_email.backend.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "sebastian.golijow@gmail.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors haven"
