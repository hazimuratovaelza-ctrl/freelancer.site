#!/usr/bin/env python
import os, sys
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelancer_django_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Make sure it's installed.") from exc
    execute_from_command_line(sys.argv)
