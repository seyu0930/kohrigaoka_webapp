"""
ASGI config for mywebsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from pathlib import Path
from dotenv import load_dotenv

PARENT_DIR = Path(__file__).resolve().parent.parent

env_path = PARENT_DIR / "auth/.env"
load_dotenv(env_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ.get("settings"))

application = get_asgi_application()
