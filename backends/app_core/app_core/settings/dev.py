import os
from .base import *





DB_USERNAME=os.environ.get("POSTGRES_USER")
DB_PASSWORD=os.environ.get("POSTGRES_PASSWORD")
DB_HOST=os.environ.get("POSTGRES_HOST")
DB_PORT=os.environ.get("POSTGRES_PORT")
DB_DATABASE=os.environ.get("POSTGRES_DB")
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
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DB_DATABASE,
            "USER": DB_USERNAME,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
        }
    }