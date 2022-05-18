import os
from .base import *


DB_USERNAME = env("POSTGRES_USER")
DB_PASSWORD = env("POSTGRES_PASSWORD")
DB_HOST = env("POSTGRES_HOST")
DB_PORT = env("POSTGRES_PORT")
DB_DATABASE = env('DB_DATABASE')

DB_IS_AVAIL = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_DATABASE
])


if DB_IS_AVAIL:
    DATABASES = {
        "default": {
            "ENGINE": "django.contrib.gis.db.backends.postgis",
            "NAME": DB_DATABASE,
            "USER": DB_USERNAME,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
        }
    }
    print(DATABASES)
