"""
WSGI config for noel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import dotenv

from django.core.wsgi import get_wsgi_application
dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'), override=True)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "noel.settings")

application = get_wsgi_application()
