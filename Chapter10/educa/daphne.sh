#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE=educa.settings.pro
daphne -p 8001 -b 127.0.0.1 educa.asgi:application
