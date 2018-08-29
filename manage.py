#!/usr/bin/env python

from argparse import ArgumentParser as AP

parser = AP(description="Perform django commands in a reusable app")
parser.add_argument("action", help="command (e.g. 'makemigrations', 'shell', 'test')")
args = parser.parse_args()

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# https://stackoverflow.com/questions/30656162/migrations-in-stand-alone-django-app#answer-32379263
import sys
import django

from django.conf import settings
from django.core.management import call_command


settings.configure(
    DEBUG=True,
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'frontend.apps.FrontendConfig',
    ),
    TEMPLATES=[
        {
            "BACKEND": 'django.template.backends.django.DjangoTemplates',
            "DIRS": [
                os.path.join(BASE_DIR, "frontend", "templates"),
            ],
            "OPTIONS": {
                "context_processors": [
                    'django.contrib.auth.context_processors.auth',
                ],
            },
        }
    ],
    USE_TZ=True,
)
#endsnippet

if os.path.exists(os.path.join(BASE_DIR, "frontend", "urls.py")):
    settings.ROOT_URLCONF='frontend.urls'

if args.action == "test":
    # 'test' action requires the default database configured
    # Use in-memory sqlite3
    settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    }

django.setup()
try:
    call_command(args.action, 'frontend')
except django.core.management.base.CommandError:
    call_command(args.action)
