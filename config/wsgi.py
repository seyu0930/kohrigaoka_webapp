"""
WSGI config for mywebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from pathlib import Path
from dotenv import load_dotenv

PARENT_DIR = Path(__file__).resolve().parent.parent

env_path = PARENT_DIR / "auth/.env"
load_dotenv(env_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ.get("settings"))


application = get_wsgi_application()
