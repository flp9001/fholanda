#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from os.path import dirname, abspath, join

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # This allows easy placement of apps within the interior fholanda directory:
    current_path = dirname(abspath(__file__))
    sys.path.append(join(current_path, "fholanda"))

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
