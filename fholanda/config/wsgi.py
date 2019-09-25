"""
WSGI config for fholanda project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys
from os.path import abspath, join, dirname

from django.core.wsgi import get_wsgi_application

# This allows easy placement of apps within the interior of fholanda directory
app_path = abspath(join(dirname(abspath(__file__)), os.pardir))
sys.path.append(join(app_path, "apps"))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')

application = get_wsgi_application()
