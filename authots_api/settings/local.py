from .base import *  # noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="LC-vloE4Oq_Dq_7WQMpebMQdLIpVGbmD_HyyFBSKtKx9iL_F6-s"
)

DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
