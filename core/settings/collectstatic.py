# core/settings/collectstatic.py
# Special settings for collecting static files to Google Cloud Storage

from os import getenv

from core.settings.base import *  # noqa: F403

# --- General Settings ---
SECRET_KEY = "django-insecure-4!@#%&*()_+abc1234567890"  # Simple key for collectstatic
DEBUG = False
ALLOWED_HOSTS = ["*"]

# --- Database ---
# Use SQLite for collectstatic (we don't need MySQL just for static files)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    }
}

