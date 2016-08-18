#!/usr/bin/env python
import os
import sys
from django.conf import settings
import linnaen.settings

if __name__ == "__main__":
    original_settings = linnaen.settings.__dict__
    original_settings["DATABASES"] = { 'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': sys.argv[3]
        }
    }
    settings.configure(**original_settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv[:-1])
